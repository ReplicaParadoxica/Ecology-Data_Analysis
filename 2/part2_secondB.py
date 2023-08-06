import pandas as pd
import plotly.express as px
import json

with open("countries_telegrams.json", "r") as file:
    data = json.load(file)

country_telegrams_dict = dict(zip(data["countries"], data["telegrams_count"]))

df = pd.DataFrame(list(country_telegrams_dict.items()),
                  columns=["Country", "Telegrams Count"])

fig = px.choropleth(df,
                    locations="Country",
                    locationmode="country names",
                    color="Telegrams Count",
                    hover_name="Country",
                    hover_data={"Telegrams Count": True},
                    color_continuous_scale="Viridis",
                    projection="natural earth",
                    title="Number of Telegrams Sent by Country"
                    )

fig.show()
