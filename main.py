import os
from code.data_clean import load_data, clean_logistics_data
from code.data_analysis import (
    calc_on_time_rate_by_month,
    calc_on_time_rate_by_region,
    calc_on_time_rate_by_goods,
    calc_on_time_rate_goods_region,
    calc_sales_month_goods,
    calc_sales_region_goods,
    calc_quality_indicator
)
from code.data_visualization import plot_month_goods_sales, plot_region_goods_sales


def main():
    # -------- 相对路径配置（github可跨设备运行）--------
    BASE_DIR = os.path.dirname(__file__)
    data_file_path = os.path.join(BASE_DIR, "data", "data_wuliu.csv")
    output_dir = os.path.join(BASE_DIR, "output")
    # 不存在output文件夹自动新建
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # 1、加载清洗数据
    print("=====开始加载并清洗数据=====")
    raw_df = load_data(data_file_path)
    df = clean_logistics_data(raw_df)

    # 2、交货率分析
    print("\n=====按月-按时交货率=====")
    month_on_time = calc_on_time_rate_by_month(df)
    print(month_on_time)

    print("\n=====按销售区域-按时交货率=====")
    region_on_time = calc_on_time_rate_by_region(df)
    print(region_on_time)

    print("\n=====按货品-按时交货率=====")
    goods_on_time = calc_on_time_rate_by_goods(df)
    print(goods_on_time)

    print("\n=====货品+区域双维度-按时交货率=====")
    goods_region_on_time = calc_on_time_rate_goods_region(df)
    print(goods_region_on_time)

    # 3、销量潜力分析
    month_goods_sales = calc_sales_month_goods(df)
    region_goods_sales = calc_sales_region_goods(df)

    # 绘图并保存图片
    plot_month_goods_sales(month_goods_sales, os.path.join(output_dir, "month_goods_sales.png"))
    plot_region_goods_sales(region_goods_sales, os.path.join(output_dir, "region_goods_sales.png"))

    # 4、货品质量指标分析
    print("\n=====货品&区域质量指标(拒货率/返修率/合格率)=====")
    quality_result = calc_quality_indicator(df)
    print(quality_result)

    print("\n✅项目全部分析完成，结果图片已保存至 output 文件夹")


if __name__ == "__main__":
    main()
