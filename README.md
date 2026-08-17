# 商品配送与用户反馈数据分析项目 

## 1.项目简介

​	本项目基于某企业6种商品的送货配送数据与用户反馈数据，使用Python开展探索性数据分析。从配送服务质量、区域销售潜力、商品质量问题三个方向进行挖掘，定位当前业务痛点，输出物流优化、市场投放以及产品质检方面的决策建议。 

## 2.技术栈 

- Python - Pandas：数据清洗、指标统计、透视分析 
- Numpy：数据运算
- Matplotlib：可视化图表绘制

## 3.项目目录结构

```markdown
├── code/ # 存放数据分析 Python 源代码
├── data/ # 存放原始业务数据集
├── .gitignore # Git 忽略配置文件
└── README.md # 项目说明文档
```

## 4.需求分析结论

### 4.1.配送服务是否存在问题维度分析

#### 4.1.1.按时交货率维度分析

**通过按时交货率看，Q4季度比Q3季度低，猜测可能由于季节更替原因（气候原因导致）**

![image-20260817192044332](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20260817192044332.png)

#### 4.1.2.销售区域维度分析

**西北地区存在明显的延时交货情况，需要进行解决！**

![image-20260817192308356](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20260817192308356.png)

#### 4.1.3.货品维度分析

**货品4晚交货情况较为严重，其余货品按时交货率相对正常**

![image-20260817192426729](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20260817192426729.png)

#### 4.1.4.货品+销售区域维度分析

**销售区域：西北地区较差，货品配送主要为1和4，其中按时交货率低主要由于货品4晚交货导致！**

**货品：：货品2主要运往华东和马来西亚，主要为马来西亚晚交货导致！**

![image-20260817192723622](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20260817192723622.png)

## 4.2.是否存在尚有潜力的销售区域
