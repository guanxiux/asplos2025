#%%
from matplotlib import pyplot as plt
import matplotlib as mpl

systems = ["Local", "ALL", "EVA2","HP","EVA2+HP","CacheInf"]

# KAPAO
model = "KAPAO"
Latency = {"Local":1, "ALL":1, "EVA2":1,"HP":1,"EVA2+HP":1,"CacheInf":1}
Latency_std = {"Local":0.5, "ALL":0.5, "EVA2":0.5,"HP":0.5,"EVA2+HP":0.5,"CacheInf":0.5}
Energy_cost = {"Local":1, "ALL":1, "EVA2":1,"HP":1,"EVA2+HP":1,"CacheInf":1}
Energy_cost_std = {"Local":0.5, "ALL":0.5, "EVA2":0.5,"HP":0.5,"EVA2+HP":0.5,"CacheInf":0.5}
Accuracy = {"Local":1, "ALL":1, "EVA2":1,"HP":1,"EVA2+HP":1,"CacheInf":1}

# # AGRNav
# model = "AGRNav"
# Latency = {"Local":1, "ALL":1, "EVA2":1,"HP":1,"EVA2+HP":1,"CacheInf":1}
# Latency_std = {"Local":0.5, "ALL":0.5, "EVA2":0.5,"HP":0.5,"EVA2+HP":0.5,"CacheInf":0.5}
# Energy_cost = {"Local":1, "ALL":1, "EVA2":1,"HP":1,"EVA2+HP":1,"CacheInf":1}
# Energy_cost_std = {"Local":0.5, "ALL":0.5, "EVA2":0.5,"HP":0.5,"EVA2+HP":0.5,"CacheInf":0.5}
# Accuracy = {"Local":1, "ALL":1, "EVA2":1,"HP":1,"EVA2+HP":1,"CacheInf":1}

fig_width = 12
fig_height = 6
width = 0.5

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
plt.figure(figsize=(fig_width, fig_height))
plt.xticks(range(len(systems)),systems)
plt.bar(range(len(systems)), [Accuracy[each]/Accuracy["Local"]*100 for each in systems], width=width,color="gray")
plt.xticks(rotation=30)
plt.title(model+"'s Normalized Accuracy(%)")
plt.savefig(f'./accuracy_{model}.pdf')