from bokeh.plotting import figure,output_file , show

x = [1,2,3,4,5]
y = [1,2,3,4,5]

p = figure()

p.vbar(x,top=y , bottom=0 , width=0.5 )

output_file("bar.html")

show(p)