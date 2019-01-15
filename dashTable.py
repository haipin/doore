import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
'''
def generate_table(dataframe, max_rows=10):
	Theader = [html.Tr([html.Th(col) for col in dataframe.columns])]

	#Tbody = []
	temp_tr = []
	for i in range(min(len(dataframe), max_rows)):
		temp_td = []
		for col in dataframe.columns:
			temp_td.append(dataframe.iloc[i][col])
		temp_tr.append(temp_td)

#	Tbody = [html.Tr([html.Td([dataframe.iloc[i][col] for col in dataframe.columns]) for i in range(min(len(dataframe), max_rows))])]

	return html.Table([Theader] + [temp_tr])

'''
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[html.H1(children="US Agriculture Exports (2011)"), generate_table(df)])

if __name__ == '__main__':
	app.run_server(port=8010)