from bokeh.plotting import figure,output_file , show

x = [[1,3,2],[2,5,4],[4,6,7,8]]
y = [[10,7,9],[9,4,11,12],[12,13,14,15]]

p = figure()

p.patches(x,y,fill_color=["red","blue","green"])

output_file("patch.html")

show(p)