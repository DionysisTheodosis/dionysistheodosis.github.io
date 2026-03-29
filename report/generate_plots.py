import matplotlib.pyplot as plt
import numpy as np

# Data for Pie Chart (Figure 3)
labels = ['Crash reporters', 'Analytics', 'Ads', 'Identification', 'Marketing']
sizes = [3, 20, 22, 1, 2]  # Total 48 instances
colors = ['#1f2f5c', '#a6a6a6', '#00b050', '#c00000', '#ed7d31']

fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(sizes, labels=None, colors=colors, autopct='%1.0f%%', startangle=90, pctdistance=0.85)

# Styling the text on the pie slices
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

# Make legend
ax.legend(wedges, labels, title="Categories", loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3, frameon=False, fontsize=12)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.tight_layout()
plt.savefig('figure_3.png', dpi=300, bbox_inches='tight')
plt.close()

# Data for Stacked Bar Chart (Figure 2) - 100% representation
apps = ['Calculator', 'Calendar', 'QR & Barcode', 'ZArchiver', 'Translate', 'Speedtest', 'Gboard', 'SHAREit', 'Authenticator', 'RAR', 'CCleaner', 'Turbo VPN']
# We'll map the categories exactly as the original image:
categories = ['Crash reporters', 'Analytics', 'Customer support', 'Identification', 'Ads', 'Location', 'Marketing']

# Raw data counts per app
data = {
    'Calculator': [0, 0, 0, 0, 0, 0, 0],
    'Calendar':   [0, 0, 0, 0, 0, 0, 0],
    'QR & Barcode': [0, 1, 0, 0, 2, 0, 0],  # FB Ads, AdMob (2 Ads), Firebase (1 Analytics)
    'ZArchiver':  [0, 0, 0, 0, 0, 0, 0],
    'Translate':  [0, 0, 0, 0, 0, 0, 0],
    'Speedtest':  [1, 5, 0, 0, 4, 0, 0],  # Crashlytics(1), An(Firebase,GA,Tag,Amplify,ComScore)=5, Ads(AdMob,IAB,Prebid,AmazonAd)=4
    'Gboard':     [0, 0, 0, 0, 0, 0, 0],
    'SHAREit':    [0, 4, 0, 1, 8, 0, 1],  # An(FB,Firebase,IAB,OpenTele)=4, ID(FBLog)=1, Mkt(AppMonet)=1?, Ads(AdMob,Mintegral,Pangle,Tapjoy,Yandex,myTarget,myTracker(an?),Adjust(an?))
    'Authenticator':[0, 0, 0, 0, 0, 0, 0],
    'RAR':        [0, 0, 0, 0, 0, 0, 0],
    'CCleaner':   [1, 3, 0, 0, 6, 0, 0],
    'Turbo VPN':  [1, 3, 0, 0, 7, 0, 0],
}

# Converting to 100% stacked
percentages = {cat: [] for cat in categories}

# Filter out apps with 0 trackers for the plot so it doesn't look empty/broken
active_apps = []
active_data = []

for app in apps:
    total = sum(data[app])
    if total > 0:
        active_apps.append(app)
        active_data.append([count/total * 100 for count in data[app]])

if not active_apps:
    print("No trackers to plot for bar chart")
else:
    # Transpose data for stacking
    plot_data = np.array(active_data).T

    fig, ax = plt.subplots(figsize=(10, 6))

    bottom = np.zeros(len(active_apps))
    colors_bar = ['#3e536f', '#a6a6a6', '#4f81bd', '#c00000', '#00b050', '#ffc000', '#ed7d31']

    for i, cat in enumerate(categories):
        ax.bar(active_apps, plot_data[i], bottom=bottom, label=cat, color=colors_bar[i], width=0.5)
        bottom += plot_data[i]

    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0f}%'.format(y)))
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=4, frameon=False, fontsize=10)

    # Rotate x labels
    plt.xticks(rotation=90)

    plt.tight_layout()
    plt.savefig('figure_2.png', dpi=300, bbox_inches='tight')
    plt.close()

print("Plots generated: figure_2.png and figure_3.png")
