from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Bar
from plotly.graph_objs import Figure
from plotly.graph_objs import Layout
from django.http import HttpResponse;
import random

def plotly(request):
    demographics = ['WHITE','BLACK','HISPA','ASIAN','UNKWN']
    average_visits = [random.uniform(1.5,6) for x in demographics]
    graph = [Bar(x=demographics,y=average_visits)]
    layout = Layout(title='Average # of Visits by Ethnicity',xaxis=dict(title='Ethnicity'),yaxis=dict(title='Average # of Visits'))
    fig = Figure(data=graph,layout=layout)
    plot_div = plot(fig,output_type='div',show_link=False,link_text="")
    return render(request, "visualizations/plotly.html", context={'plot_div':plot_div})

def ex1(request):
	import dash
	import dash_core_components as dcc
	import dash_html_components as html

	from django_plotly_dash import DjangoDash

	app = DjangoDash('SimpleExample')

	app.layout = html.Div([
	    dcc.RadioItems(
		id='dropdown-color',
		options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
		value='red'
	    ),
	    html.Div(id='output-color'),
	    dcc.RadioItems(
		id='dropdown-size',
		options=[{'label': i, 'value': j} for i, j in [('L','large'), ('M','medium'), ('S','small')]],
		value='medium'
	    ),
	    html.Div(id='output-size')

	])

	@app.callback(
	    dash.dependencies.Output('output-color', 'children'),
	    [dash.dependencies.Input('dropdown-color', 'value')])
	def callback_color(dropdown_value):
	    return "The selected color is %s." % dropdown_value

	@app.callback(
	    dash.dependencies.Output('output-size', 'children'),
	    [dash.dependencies.Input('dropdown-color', 'value'),
	     dash.dependencies.Input('dropdown-size', 'value')])
	def callback_size(dropdown_color, dropdown_size):
	    return "The chosen T-shirt is a %s %s one." %(dropdown_size,
		                                          dropdown_color)
    
	return HttpResponse('Error!');
# Create your views here.
