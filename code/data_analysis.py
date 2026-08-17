import pandas as pd


def calc_on_time_rate_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """按月维度：计算按时交货率"""
    res = df.groupby(['月份', '货品交货状况']).size().unstack()
    res['按时交货率'] = round(res['按时交货'] / (res['按时交货'] + res['晚交货']) * 100, 2)
    return res


def calc_on_time_rate_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """按销售区域维度：按时交货率"""
    res = df.groupby(['销售区域', '货品交货状况']).size().unstack()
    res['按时交货率'] = round(res['按时交货'] / (res['按时交货'] + res['晚交货']) * 100, 2)
    res = res.sort_values(by='按时交货率', ascending=False)
    return res


def calc_on_time_rate_by_goods(df: pd.DataFrame) -> pd.DataFrame:
    """按货品维度：按时交货率"""
    res = df.groupby(['货品', '货品交货状况']).size().unstack()
    res['按时交货率'] = round(res['按时交货'] / (res['按时交货'] + res['晚交货']) * 100, 2)
    res = res.sort_values(by='按时交货率', ascending=False)
    return res


def calc_on_time_rate_goods_region(df: pd.DataFrame) -> pd.DataFrame:
    """货品+销售区域双维度：按时交货率"""
    res = df.groupby(['货品', '销售区域', '货品交货状况']).size().unstack()
    res['按时交货率'] = round(res['按时交货'] / (res['按时交货'] + res['晚交货']) * 100, 2)
    res = res.sort_values(by='按时交货率', ascending=False)
    return res


def calc_sales_month_goods(df: pd.DataFrame) -> pd.DataFrame:
    """月份‑货品销量统计"""
    res = df.groupby(['月份', '货品'])['数量'].sum().unstack()
    return res


def calc_sales_region_goods(df: pd.DataFrame) -> pd.DataFrame:
    """销售区域‑货品销量统计"""
    res = df.groupby(['销售区域', '货品'])['数量'].sum().unstack()
    return res


def calc_quality_indicator(df: pd.DataFrame) -> pd.DataFrame:
    """货品+区域维度：计算拒货率、返修率、合格率"""
    res = df.groupby(['货品', '销售区域'])['货品用户反馈'].value_counts().unstack()
    total = res.sum(axis=1)
    res['拒货率'] = res['拒货'] / total
    res['返修率'] = res['返修'] / total
    res['合格率'] = res['质量合格'] / total
    res = res.sort_values(['合格率', '返修率', '拒货率'], ascending=False)
    return res
