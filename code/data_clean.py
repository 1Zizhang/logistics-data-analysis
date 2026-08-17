import pandas as pd


def load_data(data_path: str) -> pd.DataFrame:
    """加载原始物流销售数据集"""
    df = pd.read_csv(data_path, encoding="gbk")
    return df


def format_sales_amount(number):
    """销售金额单位转换：万元/元 -> 纯数字"""
    if pd.isna(number):
        return number
    if number.find('万元') != -1:
        number_new = float(number[:number.find('万元')].replace(',', '')) * 10000
    elif number.find('元') != -1:
        number_new = float(number.replace('元', '').replace(',', ''))
    else:
        number_new = float(number)
    return number_new


def clean_logistics_data(df: pd.DataFrame) -> pd.DataFrame:
    """完整清洗流水线：去重、缺失、字段删除、金额转换、时间衍生月份"""
    # 删除重复行
    df.drop_duplicates(keep='first', inplace=True)
    # 删除含缺失值行
    df.dropna(axis=0, how='any', inplace=True)
    # 删除不需要的列
    df.drop(columns=['订单行'], inplace=True)
    # 重置索引
    df.reset_index(drop=True, inplace=True)
    # 销售金额格式化
    df['销售金额'] = df['销售金额'].map(format_sales_amount)
    # 过滤销售金额等于0异常数据
    df = df[df['销售金额'] != 0]
    # 时间字段处理，生成月份
    df['销售时间'] = pd.to_datetime(df['销售时间'])
    df['月份'] = df['销售时间'].apply(lambda x: x.month)
    # 字符串字段去除首尾空格
    df['货品交货状况'] = df['货品交货状况'].str.strip()
    df['货品用户反馈'] = df['货品用户反馈'].str.strip()

    return df


if __name__ == "__main__":
    pass
