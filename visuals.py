# ...new file...
"""visuals.py
Compact plotting helpers for the COVID notebook.
Usage:
    from visuals import load_data_from_url, plot_stacked_bar, plot_choropleth_plotly
    df = load_data_from_url()
    plot_stacked_bar(df, search='Netherlands')

The functions use plotly if available for interactive maps and matplotlib for a simple stacked bar.
"""
from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt

# try to import plotly (optional)
try:
    import plotly.express as px
    _HAS_PLOTLY = True
except Exception:
    _HAS_PLOTLY = False

# default data URL (same as the notebook)
DEFAULT_URL = (
    'https://opendata.arcgis.com/datasets/bbb2e4f589ba40d692fab712ae37b9ac_1.csv'
)


def load_data_from_url(url: str = DEFAULT_URL) -> pd.DataFrame:
    """Load CSV from URL and normalize column names. Returns a DataFrame.
    Columns normalized: strip BOM, whitespace. Ensures Confirmed and Deaths exist and are numeric.
    """
    r = pd.read_csv(url, dtype=str)
    # strip BOM and whitespace
    r.columns = [c.lstrip('\ufeff').strip() for c in r.columns]

    # Ensure numeric columns
    for col in ['Confirmed', 'Deaths']:
        if col not in r.columns:
            r[col] = 0
        r[col] = pd.to_numeric(r[col], errors='coerce').fillna(0)

    # If Recovered missing, compute as Confirmed - Deaths (non-negative)
    if 'Recovered' not in r.columns:
        r['Recovered'] = (r['Confirmed'] - r['Deaths']).clip(lower=0).astype(int)
    else:
        r['Recovered'] = pd.to_numeric(r['Recovered'], errors='coerce').fillna(
            (r['Confirmed'] - r['Deaths']).clip(lower=0)
        )

    # Keep Lat/Long if present
    for c in ['Lat', 'Long_', 'Latitude', 'Longitude']:
        if c in r.columns and 'Lat' not in r.columns:
            r.rename(columns={c: 'Lat'}, inplace=True)
        if c in r.columns and 'Long_' not in r.columns:
            r.rename(columns={c: 'Long_'}, inplace=True)

    return r


def filter_by_country(df: pd.DataFrame, query: Optional[str]) -> pd.DataFrame:
    """Return rows matching query in Country_Region (case-insensitive substring). If query is falsy, return df.
    """
    if not query:
        return df
    col = 'Country_Region'
    if col not in df.columns:
        # try common alternatives
        if 'Country/Region' in df.columns:
            col = 'Country/Region'
        else:
            raise KeyError('No country column found')

    qlow = str(query).lower().strip()
    mask = df[col].astype(str).str.lower().str.contains(qlow, na=False)
    return df[mask]


def plot_stacked_bar(df: pd.DataFrame, search: Optional[str] = None, region_col: str = 'Country_Region', top_n: int = 20, figsize=(12, 6)):
    """Plot a stacked bar (Confirmed, Recovered, Deaths) for the filtered dataset.
    If search is provided, filters rows by country substring match first.
    """
    sub = filter_by_country(df, search)
    # Aggregate
    agg = sub.groupby(region_col, as_index=True).agg({'Confirmed': 'sum', 'Recovered': 'sum', 'Deaths': 'sum'})
    if agg.empty:
        raise ValueError(f"No rows match '{search}' in column '{region_col}'")

    plot_df = agg.sort_values('Deaths', ascending=False).head(top_n)
    ax = plot_df.plot(kind='bar', stacked=True, figsize=figsize, color=['#6baed6', '#74c476', '#de2d26'])
    ax.set_title(f"COVID - Confirmed / Recovered / Deaths{' (filtered)' if search else ''}")
    ax.set_xlabel('Country / Region')
    ax.set_ylabel('Counts')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def plot_choropleth_plotly(df: pd.DataFrame, metric: str = 'Deaths', title: Optional[str] = None):
    """Create a simple world choropleth using plotly.express with country names (locationmode='country names').
    The function aggregates by country name.
    """
    if not _HAS_PLOTLY:
        raise RuntimeError('plotly is required for choropleth. Install plotly with `pip install plotly`')

    if 'Country_Region' not in df.columns:
        raise KeyError('Country_Region column not found')

    agg = df.groupby('Country_Region', as_index=False).agg({metric: 'sum'})
    title = title or f'COVID - {metric} by Country'

    fig = px.choropleth(
        agg,
        locations='Country_Region',
        locationmode='country names',
        color=metric,
        hover_name='Country_Region',
        color_continuous_scale='Reds',
        title=title,
    )
    fig.update_layout(coloraxis_colorbar=dict(title=metric))
    fig.show()


def plot_bubble_map(df: pd.DataFrame, metric: str = 'Confirmed', size_max: int = 40):
    """Create a bubble map from Lat/Long using plotly.express. Aggregates by country and uses mean coordinates.
    Requires 'Lat' and 'Long_' columns to be present.
    """
    if not _HAS_PLOTLY:
        raise RuntimeError('plotly is required for bubble map. Install plotly with `pip install plotly`')

    if 'Lat' not in df.columns or 'Long_' not in df.columns:
        raise KeyError('Lat and Long_ columns required for bubble map')

    agg = df.groupby('Country_Region', as_index=False).agg({
        metric: 'sum',
        'Lat': 'mean',
        'Long_': 'mean'
    }).dropna(subset=['Lat', 'Long_'])

    fig = px.scatter_geo(
        agg,
        lat='Lat',
        lon='Long_',
        size=metric,
        hover_name='Country_Region',
        projection='natural earth',
        size_max=size_max,
        title=f'COVID - {metric} Bubble Map',
    )
    fig.show()


def plot_time_series(df: pd.DataFrame, country: str, date_col: str = 'Last_Update'):
    """Plot a simple time series of cumulative Confirmed, Recovered, Deaths for a country.
    The function expects a column with dates (string or datetime). It groups by date after parsing.
    """
    if not _HAS_PLOTLY:
        raise RuntimeError('plotly is required for time series. Install plotly with `pip install plotly`')

    if 'Country_Region' not in df.columns:
        raise KeyError('Country_Region column not found')

    sub = df[df['Country_Region'].astype(str).str.lower() == country.lower()]
    if sub.empty:
        raise ValueError(f"No data for country '{country}'")

    if date_col not in sub.columns:
        raise KeyError(f"Date column '{date_col}' not found")

    sub = sub.copy()
    sub[date_col] = pd.to_datetime(sub[date_col], errors='coerce')
    sub = sub.dropna(subset=[date_col])
    ts = sub.groupby(date_col).agg({'Confirmed': 'sum', 'Recovered': 'sum', 'Deaths': 'sum'}).sort_index()

    fig = px.line(ts.reset_index(), x=date_col, y=['Confirmed', 'Recovered', 'Deaths'], title=f'{country} - cumulative counts')
    fig.update_traces(mode='lines+markers')
    fig.show()


if __name__ == '__main__':
    # demo: load data and show three visuals (stacked bar, choropleth, bubble map)
    try:
        print('Loading data...')
        df = load_data_from_url()
        print('Data loaded, rows:', len(df))

        print('\nShowing stacked bar (top countries by deaths)...')
        try:
            plot_stacked_bar(df, search=None, top_n=10)
        except Exception as e:
            print('Stacked bar failed:', e)

        if _HAS_PLOTLY:
            try:
                print('\nShowing choropleth (Deaths)...')
                plot_choropleth_plotly(df, metric='Deaths')
            except Exception as e:
                print('Choropleth failed:', e)

            try:
                print('\nShowing bubble map (Confirmed)...')
                plot_bubble_map(df, metric='Confirmed')
            except Exception as e:
                print('Bubble map failed:', e)
        else:
            print('\nPlotly not installed - skip interactive maps. Install with: pip install plotly')
    except Exception as e:
        print('Demo failed:', e)

