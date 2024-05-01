import numpy as np
import pandas as pd
import os


def jitter(df, col, amt=0.5):
    return df[col] + np.random.random(len(df)) * amt - amt / 2


def debug(df, extra=""):
    print(f"{extra} {df.shape=}")
    return df


def limit_n(df, col, n=20, other="Other"):
    top = df[col].value_counts()

    topn = top.index[:n]
    return df[col].where(df[col].isin(topn), other)


def csv(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(current_dir, "data", f"{filename}.csv")
    return pd.read_csv(file)


def modify(fig):
    # Sadly, atm, here you'd have to manually copy/paste after you figure out
    # your own design colors in tailwind.pcss
    primary = "hsl(24, 9.8%, 10%)"  # tailwind.pcss/root:primary
    secondary = "hsl(60, 4.8%, 95.9%)"  # tailwind.pcss/root:secondary
    gl = "hsl(80, 6%, 90%)"  # https://hslpicker.com/#e6e7e4
    m = 0
    pan = "pan"

    fig.update_traces(line_color=primary)

    fig.update_layout(
        paper_bgcolor=secondary,
        plot_bgcolor=secondary,
        margin={"l": m, "r": m, "b": m, "t": m},
        font_color=primary,
        hoverlabel={"bgcolor": secondary},
        dragmode=pan,
        xaxis=dict(gridcolor=gl),
        yaxis=dict(gridcolor=gl),
    )
