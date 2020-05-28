import interpolation.control as ctrl 
import interpolation.functions as function
import interpolation.graphs as graph
import interpolation.tables as tbl

start = -1
end = 1
n = 7
m = 1001

f = function.cube

# Runge
runge = graph.create_graph(ctrl.create_V(f, start, end, m), 'r', 'runge')

# Linear System
V = ctrl.interpolation_by_function(f, 'linear_system', start, end, n, m)
linear_system = graph.create_graph(V, 'b', 'linear system')

# Lagrange
V = ctrl.interpolation_by_function(f, 'lagrange', start, end, n, m)
lagrange = graph.create_graph(V, 'y', 'lagrange')

# Newton
V = ctrl.interpolation_by_function(f, 'newton', start, end, n, m)
newton = graph.create_graph(V, 'y', 'newton')

# Cubic Spline
V = ctrl.interpolation_by_function(f, 'cubic_spline', start, end, n, m)
cubic_spline = graph.create_graph(V, 'k', 'cubic spline')

graph.plot_graph([runge, linear_system, lagrange, newton, cubic_spline], title='Runge', xlabel='x', ylabel='y')