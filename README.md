# GBDT_Simple_Tutorial（梯度提升树简易教程）
## 简介
利用python实现GBDT算法的回归、二分类以及多分类，将算法流程详情进行展示解读并可视化，便于读者庖丁解牛地理解GBDT。
***
## 项目进度：
- 回归 √
- 二分类 √
- 可视化 √ 
- 多分类 √
***
**算法原理以及公式推导请前往blog：**[GBDT算法原理以及实例理解](https://blog.csdn.net/zpalyq110/article/details/79527653)
***
## 依赖环境
- 操作系统：Windows/Linux
- 编程语言：Python3
- Python库：pandas、PIL、pydotplus，
 其中pydotplus库会自动调用Graphviz，所以需要去[Graphviz官网](https://graphviz.gitlab.io/_pages/Download/Download_windows.html)下载`graphviz的-2.38.msi`
，先安装，再将安装目录下的`bin`添加到系统环境变量，此时如果再报错可以重启计算机。详细过程不再描述，网上很多解答。
## 文件结构
- | - GBDT 主模块文件夹
- | --- gbdt.py 梯度提升算法主框架
- | --- decision_tree.py 单颗树生成，包括节点划分和叶子结点生成
- | --- loss_function.py 损失函数
- | --- tree_plot.py 树的可视化
- | - regression_example.py 回归测试文件
- | - binary_classification_example.py 二分类测试文件
- | - multi_classification_example.py 多分类测试文件

## 运行指南
- 回归测试：配置参数 `is_log` -- 是否打印树的生成过程, `is_plot` -- 是否可视化树的结构， 运行 `regression_example.py`

