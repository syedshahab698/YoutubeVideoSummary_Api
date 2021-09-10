import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

from main import get_summary_of_video


app = dash.Dash(__name__,
	external_stylesheets=[dbc.themes.SKETCHY]
	)

server = app.server
app.title = 'Youtube Video Summary'

app.layout = html.Div(
	children = [
        
       dbc.Jumbotron( style = { 'background-color':'#5D5C61'},children = [
    dbc.Row( [
        dbc.Col([
        html.H1("Youtube Video Summary", className="display-3", ),
        html.P(
            "Used to summarize a video"
    
            ),], 
        width=4,
        ),
        dbc.Col([
            dbc.Card(
            [
                dbc.CardImg(src="/static/propic.jpg", top=True),
                dbc.CardBody(
                    [
                        html.H4("About me", className="card-title"),
                        html.P(
                            "Junior DataScientist ",
                            className="card-text",
                        ),
                        dbc.Button("Github",href = "https://github.com/syedshahab698", color="primary"),
                    ]
                ),
            ],
            style={"width": "18rem"},
        ),

            ], width=4),

        

        ], justify="center"), 
        


  ] ),

		dbc.Row(
		            dbc.Col(
		            	[html.Label('Enter URL of any youtube video : '),
		                dcc.Input(id="input1", type="text", placeholder="Enter a Youtube video URL",value = '',
						style = { 'width': '60%' , "margin-left":"10px"}
						),],
		                width={"size": 6, "offset": 3},
		            ),
		        ),
		html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Markdown(id='summary-display', children='Summary of the video',
						style = {'margin-bottom':'20%',
                        'textAlign':'left'}),
                    width={"size": 10,  "offset": 1},
                ),
                ]),

	html.Div(className = 'footer',children = [
                
        html.A(children = "Created by Syed Shahab uddin \u2764\uFE0F", href = 'https://github.com/syedshahab698')
        ])
    





	]
	
	)



@app.callback(
 	Output('summary-display', 'children'),
 	Input('input1', 'value')
 	)
def update_summary(url):
    if not url:
        return "Please enter URL of any YouTube video"
    print(url)

    summ = get_summary_of_video(url.strip())
        # print(summ)
        # summ = "Subtitles are disabled for this video"
    
    return summ

if __name__ == "__main__":
	app.run_server(debug=False)


