from bokeh.plotting import figure,output_file , show

x = [1,2,3,4,5]
y = [1,2,3,4,5]

p = figure()

p.line(x,y)

output_file("line.html")

show(p)
