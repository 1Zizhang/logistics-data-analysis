import pandas as pd


# data-clean-func
def load_and_clean_data(file_path: str):
    # 数据清洗（重复，缺失，格式调整）
    data = pd.read_csv('../data/data_wuliu.csv', encoding='gbk')
    # 通过info函数可以看出有的列数据有缺失(订单号,货品交货状况,数量)，订单行删除，销售额列格式不对，需要调整转换
    # 删除重复记录
    data.drop_duplicates(keep='first', inplace=True)  # 遇到重复保留第一行，并修改数据
    # 删除缺失值(有NA就删除整行)
    data.dropna(axis=0, how='any', inplace=True)
    # 删除订单行
    data.drop(columns=['订单行'], inplace=True)
    # 更新索引
    data.reset_index(drop=True, inplace=True)

    # 调整金额格式
    def data_deal(number):
        if number.find('万元') != -1:
            number_new = float(number[:number.find('万元')].replace(',', '')) * 10000
        elif number.find('元') != -1:
            number_new = float(number.replace('元', '').replace(',', ''))
        else:
            number_new = number
        return number_new

    data['销售金额'] = data['销售金额'].map(data_deal)
    # 异常值处理
    # 1.销售金额为0，数量为1直接删除掉
    # 2.数量/销售金额标准值是均值的8倍之多，且二分之一分位数也为1，说明数据严重右偏(2/8法则)->属于正常现象无须处理
    data = data[data['销售金额'] != 0]
    # 月份预处理
    data['销售时间'] = pd.to_datetime(data['销售时间'])
    data['月份'] = data['销售时间'].apply(lambda x: x.month)
    return data
