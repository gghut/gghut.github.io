逻辑回归
===

回归一词源于最佳拟合,表示找到最佳拟合参数集

给定一个证券交易数据样本集,如下:

|time|price|turnover|trend|
|2017-11-08 09:30:00|12.54|196900|-|
|2017-11-08 09:31:00|12.52|58550|-0.2|
|2017-11-08 09:32:00|12.5|58850|-0.2|
|2017-11-08 09:33:00|12.52|169200|0.2|
|...|...|...|...|

假设:z = w<sub>1</sub>P<sub>1</sub> +
w<sub>2</sub>P<sub>2</sub> +
w<sub>3</sub>P<sub>3</sub> +
w<sub>4</sub>T<sub>1</sub> +
w<sub>5</sub>T<sub>2</sub> +
w<sub>6</sub>T<sub>3</sub>

其中:P<sub>1</sub>,P<sub>2</sub>,P<sub>3</sub>分别是过去的连续三点的价格

T<sub>1</sub>,T<sub>2</sub>,T<sub>3</sub>分别是过去连续三点的成交量

z是相对于上一点的价格差,大于0表示上涨,小于0标识下降

通过带入样本数据转化成求6元多项式的的解,通常这样的多项式是没有解的,所以转化为求该多项式的最优解$\vec{w}$


收集数据
---

训练数据来至于上海证券交易所网站,该网站每天延时半个小时公布当天证券交易信息

分析数据
---

每天交易时间为9:30~11:30和13:00~15:00,每隔一分钟数据统计一次当前交易价格和当前交易量,每天241条数据

我们假设每天的上升下降都是根据交易价格和交易量呈线性分布的,所以我们往前选择最近的三个点作为特征进行建模

训练算法
---

### 使用梯度上升算法找到最佳参数集

梯度计算:grandf(x,y) = &int;<sub>x</sub>(x,y)$\vec{i}$+&int;<sub>y</sub>(x,y)$\vec{j}$

通过公式可以看出一个特征的梯度为系数组成的向量,样本里面的梯度可以组成一个矩阵

```python
    weights = ones((n,1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights) 
        error = labelMat - h 
        weights += alpha * dataMatrix.transpose() * error
```

其中maxCycles为迭代次数,dataMatrix为特征矩阵,alpha为每次迭代的步长

weights及为要求的最佳拟合参数集

### 使用最小二乘法找到最佳参数集

最小二乘法: w = (X<sup>T</sup>X)<sup>-1</sup>X<sup>T</sup>y