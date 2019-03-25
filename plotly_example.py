import plotly.offline as ptly
import plotly.graph_objs as go
data=[]
trace1 = go.Bar(x=['first','second','third'],
                y=[20,40,30]
    )       
data.append(trace1)
trace2 = go.Bar(x=['first','second','third'],
                y=[30,60,40]
    )       
data.append(trace2)
layout = go.Layout(font=dict(family='Courier New, monospace', size=18, color='#3D3D3D'), 
                   title='example'
    )           
fig = go.Figure(data=data, layout=layout)
ptly.plot(fig, filename = 'example.html')
