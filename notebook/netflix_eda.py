import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({
    'figure.facecolor': '#141414',
    'axes.facecolor':   '#1f1f1f',
    'axes.edgecolor':   '#333333',
    'axes.labelcolor':  '#e5e5e5',
    'xtick.color':      '#b3b3b3',
    'ytick.color':      '#b3b3b3',
    'text.color':       '#e5e5e5',
    'grid.color':       '#2a2a2a',
    'grid.linestyle':   '--',
    'font.family':      'sans-serif',
    'axes.titlesize':   14,
    'axes.titleweight': 'bold',
    'axes.titlepad':    14,
})
NETFLIX_RED  = '#E50914'
ACCENT_GOLD  = '#F5A623'
ACCENT_TEAL  = '#17a2b8'
MUTED        = '#b3b3b3'

df = pd.read_csv('/home/claude/netflix_eda/data/netflix_titles.csv')
df.columns = df.columns.str.strip()
df['date_added']   = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added']   = df['date_added'].dt.year
df['duration_int'] = df['duration'].str.extract(r'(\d+)').astype(float)

print(f"Dataset: {df.shape[0]} titles, {df.shape[1]} columns")
print("\nMissing values:\n", df.isnull().sum())

# Chart 1: Content Type Donut
counts = df['type'].value_counts()
fig, ax = plt.subplots(figsize=(7,7), facecolor='#141414')
wedges, texts, autotexts = ax.pie(
    counts, labels=counts.index, autopct='%1.1f%%',
    colors=[NETFLIX_RED, ACCENT_TEAL], startangle=90, pctdistance=0.75,
    wedgeprops=dict(width=0.55, edgecolor='#141414', linewidth=3))
for t in texts:     t.set_color('#e5e5e5'); t.set_fontsize(13)
for a in autotexts: a.set_color('#ffffff'); a.set_fontsize(12); a.set_fontweight('bold')
ax.set_title('Content Type Distribution', color='#e5e5e5', fontsize=16, fontweight='bold', pad=20)
ax.add_artist(plt.Circle((0,0), 0.40, fc='#141414'))
ax.text(0, 0, f'{counts.sum():,}\nTitles', ha='center', va='center', fontsize=13, color='#e5e5e5', fontweight='bold')
plt.tight_layout()
plt.savefig('/home/claude/netflix_eda/charts/chart1_content_type.png', dpi=150, bbox_inches='tight', facecolor='#141414')
plt.close(); print("Chart 1 done")

# Chart 2: Top 10 Countries
countries = df['country'].dropna().str.split(',').explode().str.strip()
top_countries = countries.value_counts().head(10)
fig, ax = plt.subplots(figsize=(10,6), facecolor='#141414')
bar_colors = [NETFLIX_RED] + ['#444444'] * 9
bars = ax.barh(top_countries.index[::-1], top_countries.values[::-1],
               color=bar_colors[::-1], edgecolor='none', height=0.6)
for bar, val in zip(bars, top_countries.values[::-1]):
    ax.text(bar.get_width() + 15, bar.get_y() + bar.get_height()/2, str(val), va='center', color=MUTED, fontsize=11)
ax.set_xlabel('Number of Titles', color=MUTED)
ax.set_title('Top 10 Countries by Content', color='#e5e5e5', fontsize=16, fontweight='bold')
ax.grid(axis='x', alpha=0.3); ax.spines[['top','right','left','bottom']].set_visible(False)
plt.tight_layout()
plt.savefig('/home/claude/netflix_eda/charts/chart2_top_countries.png', dpi=150, bbox_inches='tight', facecolor='#141414')
plt.close(); print("Chart 2 done")

# Chart 3: Yearly Trend
yearly = df.groupby(['year_added','type']).size().unstack(fill_value=0)
yearly = yearly[(yearly.index >= 2010) & (yearly.index <= 2021)]
fig, ax = plt.subplots(figsize=(11,5), facecolor='#141414')
ax.plot(yearly.index, yearly.get('Movie', 0), color=NETFLIX_RED, marker='o', linewidth=2.5, markersize=6, label='Movies')
ax.plot(yearly.index, yearly.get('TV Show', 0), color=ACCENT_TEAL, marker='s', linewidth=2.5, markersize=6, label='TV Shows')
ax.fill_between(yearly.index, yearly.get('Movie', 0), alpha=0.15, color=NETFLIX_RED)
ax.fill_between(yearly.index, yearly.get('TV Show', 0), alpha=0.15, color=ACCENT_TEAL)
ax.set_title('Content Added to Netflix Per Year', color='#e5e5e5', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', color=MUTED); ax.set_ylabel('Number of Titles', color=MUTED)
ax.legend(facecolor='#1f1f1f', edgecolor='#333', labelcolor='#e5e5e5')
ax.grid(alpha=0.3); ax.spines[['top','right']].set_visible(False)
plt.tight_layout()
plt.savefig('/home/claude/netflix_eda/charts/chart3_yearly_trend.png', dpi=150, bbox_inches='tight', facecolor='#141414')
plt.close(); print("Chart 3 done")

# Chart 4: Top 10 Genres
genres = df['listed_in'].dropna().str.split(',').explode().str.strip()
top_genres = genres.value_counts().head(10)
colors_g = [NETFLIX_RED,'#c40812','#a00710','#ff1f2e','#ff4d58',ACCENT_GOLD,'#d4881c','#b36f10',ACCENT_TEAL,'#0e8499']
fig, ax = plt.subplots(figsize=(10,6), facecolor='#141414')
bars = ax.bar(range(len(top_genres)), top_genres.values, color=colors_g, edgecolor='none', width=0.6)
ax.set_xticks(range(len(top_genres)))
ax.set_xticklabels(top_genres.index, rotation=35, ha='right', fontsize=10)
for bar, val in zip(bars, top_genres.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 15, str(val), ha='center', color=MUTED, fontsize=10)
ax.set_title('Top 10 Genres on Netflix', color='#e5e5e5', fontsize=16, fontweight='bold')
ax.set_ylabel('Number of Titles', color=MUTED)
ax.grid(axis='y', alpha=0.3); ax.spines[['top','right','left','bottom']].set_visible(False)
plt.tight_layout()
plt.savefig('/home/claude/netflix_eda/charts/chart4_top_genres.png', dpi=150, bbox_inches='tight', facecolor='#141414')
plt.close(); print("Chart 4 done")

# Chart 5: Ratings Distribution
ratings_order = ['G','TV-Y','TV-Y7','TV-Y7-FV','PG','TV-G','TV-PG','PG-13','TV-14','R','TV-MA','NR','UR']
rating_counts = df['rating'].value_counts()
rating_counts = rating_counts[[r for r in ratings_order if r in rating_counts.index]]
fig, ax = plt.subplots(figsize=(11,5), facecolor='#141414')
bar_colors = [ACCENT_TEAL if r in ['TV-Y','TV-Y7','G','PG','TV-G','TV-PG','TV-Y7-FV']
              else NETFLIX_RED if r in ['TV-MA','R','NC-17'] else ACCENT_GOLD for r in rating_counts.index]
bars = ax.bar(rating_counts.index, rating_counts.values, color=bar_colors, edgecolor='none', width=0.6)
for bar, val in zip(bars, rating_counts.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10, str(val), ha='center', color=MUTED, fontsize=10)
ax.set_title('Content Rating Distribution', color='#e5e5e5', fontsize=16, fontweight='bold')
ax.set_ylabel('Number of Titles', color=MUTED)
ax.grid(axis='y', alpha=0.3); ax.spines[['top','right','left','bottom']].set_visible(False)
legend_patches = [mpatches.Patch(color=ACCENT_TEAL, label='Kids / Family'),
                  mpatches.Patch(color=ACCENT_GOLD, label='Teen / General'),
                  mpatches.Patch(color=NETFLIX_RED, label='Mature / Adult')]
ax.legend(handles=legend_patches, facecolor='#1f1f1f', edgecolor='#333', labelcolor='#e5e5e5')
plt.tight_layout()
plt.savefig('/home/claude/netflix_eda/charts/chart5_ratings.png', dpi=150, bbox_inches='tight', facecolor='#141414')
plt.close(); print("Chart 5 done")

# Chart 6: Movie Duration Histogram
movies = df[df['type'] == 'Movie']['duration_int'].dropna()
fig, ax = plt.subplots(figsize=(10,5), facecolor='#141414')
ax.hist(movies, bins=40, color=NETFLIX_RED, edgecolor='#141414', alpha=0.9)
ax.axvline(movies.mean(), color=ACCENT_GOLD, linewidth=2, linestyle='--', label=f'Mean: {movies.mean():.0f} min')
ax.axvline(movies.median(), color=ACCENT_TEAL, linewidth=2, linestyle='--', label=f'Median: {movies.median():.0f} min')
ax.set_title('Movie Duration Distribution', color='#e5e5e5', fontsize=16, fontweight='bold')
ax.set_xlabel('Duration (minutes)', color=MUTED); ax.set_ylabel('Number of Movies', color=MUTED)
ax.legend(facecolor='#1f1f1f', edgecolor='#333', labelcolor='#e5e5e5')
ax.grid(alpha=0.3); ax.spines[['top','right']].set_visible(False)
plt.tight_layout()
plt.savefig('/home/claude/netflix_eda/charts/chart6_movie_duration.png', dpi=150, bbox_inches='tight', facecolor='#141414')
plt.close(); print("Chart 6 done")

print("\nAll 6 charts generated successfully!")
