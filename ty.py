import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

level = df["level"].tolist()
attempt = df["attempt"].tolist()

fig = px.line(x=level, y=attempt)
fig.show()