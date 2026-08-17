import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def plot_month_goods_sales(df, save_path: str):
    """月份‑货品销量折线图"""
    fig, ax = plt.subplots(figsize=(10, 5))
    df.plot(kind='line', ax=ax)
    ax.set_title("各货品月度销量变化趋势")
    ax.set_xlabel("月份")
    ax.set_ylabel("销售数量")
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"图表已保存: {save_path}")


def plot_region_goods_sales(df, save_path: str):
    """区域‑货品销量柱状图"""
    fig, ax = plt.subplots(figsize=(10, 5))
    df.plot(kind='bar', ax=ax)
    ax.set_title("各销售区域货品销量对比")
    ax.set_xlabel("销售区域")
    ax.set_ylabel("销售数量")
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"图表已保存: {save_path}")
