import matplotlib.pyplot as plt
import numpy as np


def plot(categories, values, title, subtitle, barcolor, step):
    plt.style.use('seaborn-ticks')
    fig, ax = plt.subplots(dpi=100)
    bars = ax.barh(categories, values, color=barcolor, edgecolor='black')
    
    i = 0
    for bar in bars:
        xval = bar.get_width()
        y = bar.get_y()
        height = bar.get_height()
        bbox_props = dict(boxstyle="square,pad=0.20")
        ax.text(xval - 0.5, bar.get_y()  + bar.get_height()/2, f'{round(xval, 1)}', ha='right', va='center', color='white', fontdict={'fontsize': 8, 'weight' : 'bold'})
        i += 1

    ax.set_title(title, fontdict={'fontsize': 16})
    ax.set_xlabel(subtitle, fontdict={'fontsize': 12})
    ax.set_facecolor('mistyrose')
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    ax.set_xticks(np.arange(0, max(values)+50, step))
    ax.set_xticklabels([str(int(x)) for x in ax.get_xticks()])

    ax.tick_params(axis='y', colors='white', pad=8, labelsize=7.5)
    for label in ax.get_yticklabels():
        label.set_bbox(dict(facecolor='black', edgecolor='black'))

    # Show the plot
    plt.show()

filename = 'data.txt'
result = {}

with open(filename, 'r') as file:
    for line in file:
        parts = line.strip().split(' - ')
        username = parts[0]
        values = list(map(int, parts[1:]))

        if (len(values) == 0):
            break
        result[username] = {
            'total': values[0],
            '< 200': values[1],
            '< 300': values[2],
            '< 400': values[3],
            '< 500': values[4],
            '< 600': values[5],
            '>= 600': values[6]
        }

categorias = ['total', '< 200', '< 300', '< 400', '< 500', '< 600', '>= 600']
titles = ['(-∞, +∞)', '[100, 200)', '[200, 300)', '[300, 400)', '[400, 500)', '[500, 600)' , '[600, +∞)']
colors =['lightcoral', 'gray', 'green', 'darkcyan', 'blue', 'purple', 'red']

index = 0
for categ in categorias:    
    tab = []
    for username, stats in result.items():
        tab.append({'username' : username, 'pts' : stats[categ]})

    tab = sorted(tab, key=lambda x: x['pts'], reverse=True)
    
    handles = []
    pts = []
    cnt = 0
    last = 25
    for item in tab:
        if (cnt == last):
            break
        handles.append(item['username'])
        pts.append(item['pts'])
        cnt += 1
    while (tab[cnt]['pts'] == tab[last-1]['pts']):
        handles.append(item['username'])
        pts.append(item['pts'])
        cnt += 1

    handles.reverse()
    pts.reverse()

    title = f"Top {len(handles)} Atcoder Brazil 2023 - Tasks in {titles[index]}"
    subtitle = f"Tasks solved with score in {titles[index]}"
    color = colors[index]
    step = 100
    if (max(pts) <= 350):
        step = 50
    plot(handles, pts, title, subtitle, color, step)
    index += 1
