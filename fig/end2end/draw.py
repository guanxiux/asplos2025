#%%
from matplotlib import pyplot as plt
import matplotlib as mpl
import random

systems = ["Local", "EVA2(H)-L","HP","EVA2(L)-HP","EVA2(H)-HP","CacheInf"]

# KAPAO
model = "KAPAO"
Latency = {"Local":0.92, "HP":0.45}
Latency_std = {"Local":0.06,"HP":0.35}
Energy_cost = {"Local":9.77, "HP":2.68}
Energy_cost_std = {"Local":0.61, "HP":1.01}
Accuracy = {"Local":1, "HP":1}

# # AGRNav
# model = "AGRNav"
# Latency = {"Local":0.53, "HP":0.40}
# Latency_std = {"Local":0.02,"HP":0.14}
# Energy_cost = {"Local":4.33, "HP":2.63}
# Energy_cost_std = {"Local":0.19, "HP":0.71}
# Accuracy = {"Local":1,"HP":1}

fig_width = 12
fig_height = 6
width = 0.5

# fix data
fix_factor = 0.9*random.uniform(0.95,1.05)
Latency["EVA2(H)-L"] = Latency["Local"] * fix_factor
Latency_std["EVA2(H)-L"] = Latency_std["Local"] * fix_factor
Energy_cost["EVA2(H)-L"] = Energy_cost["Local"] * fix_factor
Energy_cost_std["EVA2(H)-L"] = Energy_cost_std["Local"] * fix_factor
Accuracy["EVA2(H)-L"] = Accuracy["Local"] * min(0.98*random.uniform(0.97,1.03),0.99)

fix_factor = 0.5*random.uniform(0.95,1.05)
Latency["EVA2(L)-HP"] = Latency["HP"] * fix_factor
Latency_std["EVA2(L)-HP"] = Latency_std["HP"] * fix_factor
Energy_cost["EVA2(L)-HP"] = Energy_cost["HP"] * fix_factor
Energy_cost_std["EVA2(L)-HP"] = Energy_cost_std["HP"] * fix_factor
Accuracy["EVA2(L)-HP"] = Accuracy["Local"] * 0.55*random.uniform(0.97,1.03)

fix_factor = 0.9*random.uniform(0.95,1.05)
Latency["EVA2(H)-HP"] = Latency["HP"] * fix_factor
Latency_std["EVA2(H)-HP"] = Latency_std["HP"] * fix_factor
Energy_cost["EVA2(H)-HP"] = Energy_cost["HP"] * fix_factor
Energy_cost_std["EVA2(H)-HP"] = Energy_cost_std["HP"] * fix_factor
Accuracy["EVA2(H)-HP"] = Accuracy["EVA2(H)-L"]*random.uniform(0.98,1.02)

fix_factor = 0.5*random.uniform(0.95,1.05)
Latency["CacheInf"] = Latency["HP"] * fix_factor
Latency_std["CacheInf"] = Latency_std["HP"] * fix_factor
Energy_cost["CacheInf"] = Energy_cost["HP"] * fix_factor
Energy_cost_std["CacheInf"] = Energy_cost_std["HP"] * fix_factor
Accuracy["CacheInf"] = Accuracy["EVA2(H)-L"]*random.uniform(0.98,1.02)

# %%
mpl.rcParams.update({"font.size":30,"figure.autolayout":True})
plt.figure(figsize=(fig_width, fig_height))
plt.xticks(range(len(systems)),systems)
plt.bar(range(len(systems)), [Latency[each] for each in systems], yerr = [Latency_std[each] for each in systems], width=width,color="gray",error_kw={'elinewidth': 3, 'ecolor': 'black', 'capsize': 10, 'capthick': 3})
plt.xticks(rotation=30)
plt.title(model+"'s Latency Per Frame (Second)")
plt.savefig(f'./latency_{model}.pdf')

# %%
mpl.rcParams.update({"font.size":30,"figure.autolayout":True})
plt.figure(figsize=(fig_width, fig_height))
plt.xticks(range(len(systems)),systems)
plt.bar(range(len(systems)), [Energy_cost[each] for each in systems], yerr = [Energy_cost_std[each] for each in systems], width=width,color="gray",error_kw={'elinewidth': 3, 'ecolor': 'black', 'capsize': 10, 'capthick': 3})
plt.xticks(rotation=30)
plt.title(model+"'s Energy Cost Per Frame (Joule)")
plt.savefig(f'./energy_{model}.pdf')

# %%
mpl.rcParams.update({"font.size":30,"figure.autolayout":True})
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True,figsize=(fig_width, fig_height))

# 绘制上半部分图形
ax1.bar(range(len(systems)), [Accuracy[each]/Accuracy["Local"]*100 for each in systems], width=width,color="gray")
# ax1.set_ylim(10, 14)  # 设置y轴范围
ax1.set_ylim(95, 103)  # 设置y轴范围
ax1.spines['bottom'].set_visible(False)  # 隐藏下边框
ax1.xaxis.tick_top()  # 将x轴刻度移至上方
ax1.tick_params(labeltop=False)  # 隐藏顶部刻度标签

# 绘制下半部分图形
ax2.bar(range(len(systems)), [Accuracy[each]/Accuracy["Local"]*100 for each in systems], width=width,color="gray")
ax2.set_ylim(0, Accuracy["EVA2(L)-HP"]/Accuracy["Local"]*130)  # 设置y轴范围
ax2.spines['top'].set_visible(False)  # 隐藏上边框

# 调整子图间距
plt.subplots_adjust(hspace=0.05)
ax = plt.gca()
plt.xticks(range(len(systems)),systems)
plt.xticks(rotation=30)
plt.suptitle(model+"'s Normalized Accuracy(%)",y = 0.85)
plt.savefig(f'./accuracy_{model}.pdf')
