"""
Created on ：2019/03/30
@author: Freeman
"""


class Node:
    def __init__(self, data_index, split_feature=None, split_value=None, is_leaf=False):
        self.split_feature = split_feature
        self.split_value = split_value
        self.data_index = data_index
        self.is_leaf = is_leaf
        self.predict_value = None
        self.left_child = None
        self.right_child = None

    def update_predict_value(self, data):
        self.predict_value = data.mean()

    def get_predict_value(self, instance):
        if self.is_leaf:
            return self.predict_value
        if instance[self.split_feature] < self.split_value:
            return self.left_child.get_predict_value(instance)
        else:
            return self.right_child.get_predict_value(instance)


class Tree:
    def __init__(self, data, max_depth, features, iter):
        self.max_depth = max_depth
        self.features = features
        self.target_name = 'res_' + str(iter)
        self.remian_index = [True] * len(data)
        self.leaf_nodes = []
        self.root_node = self.build_tree(data, self.remian_index, depth=0)

    def build_tree(self, data, remian_index, depth=0):
        now_data = data[remian_index]
        if depth < self.max_depth:
            mse = None
            split_feature = None
            split_value = None
            split_left_index = None
            split_right_index = None
            for feature in self.features:
                feature_values = now_data[feature].unique()
                for fea_val in feature_values:
                    # 尝试划分
                    left_index = list(now_data[feature] < fea_val)
                    right_index = list(now_data[feature] >= fea_val)
                    left_mse = self._calculate_mse(now_data[left_index][self.target_name])
                    right_mse = self._calculate_mse(now_data[right_index][self.target_name])
                    sum_mse = left_mse + right_mse
                    if mse is None or sum_mse < mse:
                        split_feature = feature
                        split_value = fea_val
                        mse = sum_mse
                        split_left_index = left_index
                        split_right_index = right_index

            node = Node(remian_index, split_feature, split_value)
            # trick for DataFrame, index revert
            a = []
            for i in remian_index:
                if i:
                    if split_left_index[0]:
                        a.append(True)
                        del split_left_index[0]
                    else:
                        a.append(False)
                        del split_left_index[0]
                else:
                    a.append(False)

            b = []
            for i in remian_index:
                if i:
                    if split_right_index[0]:
                        b.append(True)
                        del split_right_index[0]
                    else:
                        b.append(False)
                        del split_right_index[0]
                else:
                    b.append(False)

            node.left_child = self.build_tree(data, a,  depth + 1)
            node.right_child = self.build_tree(data, b, depth + 1)
            return node
        else:
            node = Node(remian_index, is_leaf=True)
            node.update_predict_value(now_data[self.target_name])
            self.leaf_nodes.append(node)
            return node

    def _calculate_mse(self, label):
        mean = label.mean()
        error = 0
        for y in label:
            error += (y - mean) * (y - mean)
        return error
