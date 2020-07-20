import interpolation.control as ctrl 
import interpolation.graphs as graph
import interpolation.tables as tbl

import json
import plotly
import io
from flask import Flask, render_template, request, url_for
import csv
import math
import importlib

app = Flask(__name__)

def make_function():

    try:  
        function = importlib.import_module('function')
        importlib.reload(function)

        title = function.title
        f = function.f
        name_f = function.name_f
        start = function.start
        end = function.end
        k = function.k
        n = function.n
        m = function.m

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
        linear_spline = { 'name': 'linear spline', 'values': list(), 'mode': 'lines', 'dash': 'solid', 'color': 'black' }
        cubic_spline = { 'name': 'cubic spline', 'values': list(), 'mode': 'lines', 'dash': 'solid', 'color': 'red' }

        # Make interpolations
        for i in range (k, n + 1):
          
          # Linear System
          linear_system['values'].append(ctrl.interpolation_by_function(f, 'linear_system', start, end, i, m))

          # Lagrange    
          lagrange['values'].append(ctrl.interpolation_by_function(f, 'lagrange', start, end, i, m))

          # Newton    
          newton['values'].append(ctrl.interpolation_by_function(f, 'newton', start, end, i, m))

          # Linear Spline
          linear_spline['values'].append(ctrl.interpolation_by_function(f, 'linear_spline', start, end, i, m))

          # Cubic Spline
          cubic_spline['values'].append(ctrl.interpolation_by_function(f, 'cubic_spline', start, end, i, m))

        # JSON encoder
        k = json.dumps(k, cls=plotly.utils.PlotlyJSONEncoder)
        n = json.dumps(n, cls=plotly.utils.PlotlyJSONEncoder)
        title = json.dumps(title, cls=plotly.utils.PlotlyJSONEncoder)
        base_f = json.dumps(base_f, cls=plotly.utils.PlotlyJSONEncoder)
        dots_f = json.dumps(dots_f, cls=plotly.utils.PlotlyJSONEncoder)
        interpolation_f = json.dumps([linear_system, lagrange, newton, linear_spline, cubic_spline], cls=plotly.utils.PlotlyJSONEncoder)

        return render_template('function.html', k=k, n=n, title=title, base_f=base_f, dots_f=dots_f, interpolation_f=interpolation_f)

    # Error
    except:
      return render_template('error.html')

@app.route("/")
def index():  
  return make_function()

@app.route('/csvfile', methods=['POST'])
def upload_file():

    if request.method == 'POST':
        try:
            f = request.files['fileupload']
            # CSV and Interpolations
            stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
            V = tbl.load_csv(stream)
            linear_system_V = ctrl.interpolation_by_values(V, 'linear_system', 201)
            lagrange_V = ctrl.interpolation_by_values(V, 'lagrange', 201)
            newton_V = ctrl.interpolation_by_values(V, 'newton', 201)
            linear_spline_V = ctrl.interpolation_by_values(V, 'linear_spline', 201)
            cubic_spline_V = ctrl.interpolation_by_values(V, 'cubic_spline', 201)

            # Initialize
            dots_f = json.dumps({ 'name': f'dots', 'values': V, 'mode': 'markers', 'color': 'gray' }, cls=plotly.utils.PlotlyJSONEncoder)
            linear_system = { 'name': 'linear system', 'values': linear_system_V, 'mode': 'lines', 'dash': 'solid', 'color': 'orange' } 
            lagrange = { 'name': 'lagrange', 'values': lagrange_V, 'mode': 'lines', 'dash': 'solid', 'color': 'yellow' }
            newton = { 'name': 'newton', 'values': newton_V, 'mode': 'lines', 'dash': 'solid', 'color': 'blue' }
            linear_spline = { 'name': 'linear spline', 'values': linear_spline_V, 'mode': 'lines', 'dash': 'solid', 'color': 'black' }
            cubic_spline = { 'name': 'cubic spline', 'values': cubic_spline_V, 'mode': 'lines', 'dash': 'solid', 'color': 'red' }
            interpolation_f = json.dumps([linear_system, lagrange, newton, linear_spline, cubic_spline], cls=plotly.utils.PlotlyJSONEncoder)

            # Layout
            xlabel = json.dumps(list(V.keys())[0], cls=plotly.utils.PlotlyJSONEncoder)
            ylabel = json.dumps(list(V.keys())[1], cls=plotly.utils.PlotlyJSONEncoder)
            title = json.dumps(f.filename.replace('.csv', ''), cls=plotly.utils.PlotlyJSONEncoder)
            
            return render_template('file.html', title=title, xlabel=xlabel, ylabel=ylabel, dots_f=dots_f, interpolation_f=interpolation_f)

    # Error
        except:
          return render_template('error.html')

    return render_template('error.html')

if __name__ == "__main__":
  import random, threading, webbrowser
  port = 5000 + random.randint(0, 999)
  url = f"http://127.0.0.1:{port}"
  threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
  app.run(port=port, debug=False)
