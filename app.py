import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

from main import get_summary_of_video


app = dash.Dash(__name__,
	external_stylesheets=[dbc.themes.SKETCHY]
	)

app.layout = html.Div(
	children = [
        
       dbc.Jumbotron( style = { 'background-color':'#5D5C61'},children = [
        html.H1("Youtube Video Summary", className="display-3", ),
        html.P(
            "Used to summarize a video"
    
),  ] ),

		dbc.Row(
		            dbc.Col(
		            	[html.Label('Enter URL of any youtube video : '),
		                dcc.Input(id="input1", type="text", placeholder="Enter a Youtube video Url",value = '',
						style = {'margin-left':'20%'}
						),],
		                width={"size": 6, "offset": 3},
		            ),
		        ),
		html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(id='summary-display', children='Summary of the video',
						style = {'margin-left':'20%',
						'margin-right':'20%'}),
                    width={"size": 10,  "offset": 1},
                ),
                ]),

	
    





	]
	
	)



@app.callback(
	Output('summary-display', 'children'),
	Input('input1', 'value')
	)
def update_summary(url):
	print(url)
	try:
		summ = get_summary_of_video(url.strip())
	except:
		summ = "Subtitles are disabled for this video"

	return summ




if __name__ == "__main__":
	app.run_server(debug=True)

