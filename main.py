# main.py
from code.data_clean import load_and_clean_data

if __name__ == "__main__":
    # 相对路径，往上一级进入data文件夹
    df = load_and_clean_data("data/data_wuliu.csv")
    # 清洗完成
    print("数据清洗完成，行数：", len(df))
    print(df.head())
