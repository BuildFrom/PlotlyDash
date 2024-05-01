import pandas as pd
import numpy as np
import plotly.express as px
from dash import dcc
pd.options.plotting.backend = 'plotly'
from app.notebooks.helpers import modify, csv

def tweak_alta():
    df = csv('snow-alta-1990-2017')
    df = (df
          .assign(DATE=pd.to_datetime(df.DATE).dt.tz_localize('America/Denver'))
          .loc[:,['DATE', 'STATION', 'NAME', 'LATITUDE', 'LONGITUDE',
                  'PRCP', 'SNOW', 'SNWD', 'TMIN', 'TMAX', 'TOBS']]
          .assign(MONTH=lambda df_: df_.DATE.dt.month,
                  YEAR=lambda df_: df_.DATE.dt.year,
                  SEASON=lambda df_: np.select([df_.MONTH < 5,
                                                  df_.MONTH > 10],
                                                  [(df_.YEAR - 1).astype(str) + '-' + 
                                                  (df_.YEAR).astype(str) + ' Season',
                                                  (df_.YEAR).astype(str) + '-' + 
                                                  (df_.YEAR + 1).astype(str) + ' Season'],
                                                  default='Off Season'))
    )

    fig = (df
           .query('SEASON.str.contains("2010-2011")')
           .plot(x='DATE', y='SNWD')
    )

    modify(fig)
    return dcc.Graph(figure=fig)