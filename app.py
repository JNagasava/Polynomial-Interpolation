import interpolation.control as ctrl 
import interpolation.functions as function
import interpolation.graphs as graph
import interpolation.tables as tbl

import json
import plotly
import io
from flask import Flask, render_template, request, url_for
import csv

app = Flask(__name__)

@app.route("/")
def index():  

  ######################################
  title = 'Interpolation of Runge function'
  f = function.runge
  name_f = 'runge'
  start = -1
  end = 1
  k = 2
  n = 31
  m = 201
  #####################################

  # Generates values of function f (Creates function f)
  V = ctrl.create_V(f, start, end, m)
  base_f = { 'name': name_f, 'values': V, 'mode': 'lines', 'dash': 'solid', 'color': 'green' }

  # Generates dots of from function f
  dots_f = { 'name': f'{name_f}\'s dots', 'values': list(), 'mode': 'markers', 'color': 'gray' }
  for i in range(k, n + 1):
    V = ctrl.create_V(f, start, end, i)
    dots_f['values'].append(V)

  # Initialize 
  linear_system = { 'name': 'linear system', 'values': list(), 'mode': 'lines', 'dash': 'solid', 'color': 'orange' } 
  lagrange = { 'name': 'lagrange', 'values': list(), 'mode': 'lines', 'dash': 'solid', 'color': 'yellow' }
  newton = { 'name': 'newton', 'values': list(), 'mode': 'lines', 'dash': 'solid', 'color': 'blue' }
  cubic_spline = { 'name': 'cubic spline', 'values': list(), 'mode': 'lines', 'dash': 'solid', 'color': 'red' }

  # Make interpolations
  for i in range (k, n + 1):
    
    # Linear System
    linear_system['values'].append(ctrl.interpolation_by_function(f, 'linear_system', start, end, i, m))

    # Lagrange    
    lagrange['values'].append(ctrl.interpolation_by_function(f, 'lagrange', start, end, i, m))

    # Newton    
    newton['values'].append(ctrl.interpolation_by_function(f, 'newton', start, end, i, m))

    # Cubic Spline
    cubic_spline['values'].append(ctrl.interpolation_by_function(f, 'cubic_spline', start, end, i, m))

  # JSON encoder
  k = json.dumps(k, cls=plotly.utils.PlotlyJSONEncoder)
  n = json.dumps(n, cls=plotly.utils.PlotlyJSONEncoder)
  title = json.dumps(title, cls=plotly.utils.PlotlyJSONEncoder)
  base_f = json.dumps(base_f, cls=plotly.utils.PlotlyJSONEncoder)
  dots_f = json.dumps(dots_f, cls=plotly.utils.PlotlyJSONEncoder)
  interpolation_f = json.dumps([linear_system, lagrange, newton, cubic_spline], cls=plotly.utils.PlotlyJSONEncoder)

  return render_template('function.html', k=k, n=n, title=title, base_f=base_f, dots_f=dots_f, interpolation_f=interpolation_f)


if __name__ == "__main__":
    app.run(debug=True)

  
# <_io.TextIOWrapper name='data/runge.csv' mode='r' encoding='UTF-8'>

# <FileStorage: 'runge.csv' ('text/csv')>