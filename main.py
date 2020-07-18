# import interpolation.control as ctrl 
# import interpolation.functions as function
# import interpolation.graphs as graph
# import interpolation.tables as tbl

# import plotly.graph_objects as go

import importlib

import tkinter

# def index():  

#     ######################################
#     title = 'Interpolation of Runge function'
#     f = function.runge
#     name_f = 'runge'
#     start = -1
#     end = 1
#     k = 2
#     n = 31
#     m = 301
#     #####################################

#     # Generates values of function f (Creates function f)
#     V = ctrl.create_V(f, start, end, m)
#     base_f = { 'name': name_f, 'values': V, 'mode': 'lines', 'dash': 'solid', 'color': 'green' }

#     # Generates dots of from function f
#     dots_f = { 'name': f'{name_f}\'s dots', 'values': list(), 'mode': 'markers', 'color': 'gray' }
#     for i in range(k, n + 1):
#         V = ctrl.create_V(f, start, end, i)
#         dots_f['values'].append(V)

#     # Initialize 
#     linear_system = { 'name': 'linear system', 'values': list(), 'mode': 'lines', 'dash': 'solid', 'color': 'orange' } 
#     lagrange = { 'name': 'lagrange', 'values': list(), 'mode': 'lines', 'dash': 'solid', 'color': 'yellow' }
#     newton = { 'name': 'newton', 'values': list(), 'mode': 'lines', 'dash': 'solid', 'color': 'blue' }
#     cubic_spline = { 'name': 'cubic spline', 'values': list(), 'mode': 'lines', 'dash': 'solid', 'color': 'red' }

#     # Make interpolations
#     for i in range(k, n + 1):

#         # Linear System
#         linear_system['values'].append(ctrl.interpolation_by_function(f, 'linear_system', start, end, i, m))

#         # Lagrange    
#         lagrange['values'].append(ctrl.interpolation_by_function(f, 'lagrange', start, end, i, m))

#         # Newton    
#         newton['values'].append(ctrl.interpolation_by_function(f, 'newton', start, end, i, m))

#         # Cubic Spline
#         cubic_spline['values'].append(ctrl.interpolation_by_function(f, 'cubic_spline', start, end, i, m))
    
   
#     fig = go.Figure()

#     # Add traces, one for each slider step
#     for step in range(k, n + 1):
#         fig.add_trace(go.Scatter(
#             visible=False,
#             line=dict(color="blue", width=6),
#             name = 'Cubic Splines',
#             x=cubic_spline['values'][step - k]['x'],
#             y=cubic_spline['values'][step - k]['y']))
#         fig.add_trace(go.Scatter(
#             visible=False,
#             line=dict(color="red", width=6),
#             name = 'Lagrange',
#             x=lagrange['values'][step - k]['x'],
#             y=lagrange['values'][step - k]['y']))

#     print(len(fig.data))

#     # Make 1st trace visible
#     fig.data[0].visible = True
#     fig.data[1].visible = True

#     j = 0

#     # Create and add slider
#     steps = []
#     for i in range(n - 1):
#         step = dict(
#             method = 'update',
#             args=[{"visible": [False] * len(fig.data)},
#                   {"title": "n : " + str(i + k)}]  # layout attribute
#         )
#         step["args"][0]['visible'][i + j] = True  # Toggle i'th trace to "visible"
#         step["args"][0]['visible'][i + j +1] = True
#         j+=1
#         steps.append(step)

#     sliders = [dict(steps=steps)]

#     sliders = [dict(
#     active=0,
#     currentvalue={"prefix": "Frequency: "},
#     pad={"t": 50},
#     steps=steps
#     )]

#     fig.update_layout(
#         sliders=sliders
#     )

#     fig.show()



def test():

    test_interface = importlib.import_module('test_interface')
    importlib.reload(test_interface)
    print(test_interface.f(3))


root = tkinter.Tk()
btn = tkinter.Button(root, text='Import', command=test)
btn.pack()
root.mainloop()







# if __name__ == "__main__":
#     index()
