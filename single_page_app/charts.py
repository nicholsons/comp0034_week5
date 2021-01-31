import plotly.graph_objects as go


class RecyclingChart:
    """ Creates the figures and statistics to be used in the dashboard"""

    def __init__(self, data):
        self.data = data

    def create_chart(self, area):
        area_data = self.data.process_data_for_area(area)
        eng_data = self.data.recycling_eng
        area = go.Scatter(x=area_data['Year'], y=area_data['Recycling_Rates'],
                          mode='lines',
                          name=area,
                          line=dict(color='firebrick', width=4))
        eng = go.Scatter(x=eng_data['Year'], y=eng_data['Recycling_Rates'], mode='lines',
                         name='England',
                         line=dict(color='lightgrey', dash='dash'))

        # Create the layout
        layout = go.Layout(title="Recycyling", showlegend=True, plot_bgcolor="#ffffff")

        # Create the figure
        figure = go.Figure(layout=layout)

        # Update the figure and add the traces
        figure.add_trace(area)
        figure.add_trace(eng)

        # Update the layout of the axes to look a little closer to the original chart we are copyin
        figure.update_layout(yaxis_title="Percent")
        figure.update_yaxes(title_font=dict(size=14, color='#CDCDCD'),
                            tickfont=dict(color='#CDCDCD', size=12), ticksuffix="%",
                            showgrid=True, gridwidth=1, gridcolor='#CDCDCD',
                            tick0=0.0, dtick=10.0, range=[0, 45])
        figure.update_xaxes(tickangle=90, tickfont=dict(color='#CDCDCD', size=12),
                            showline=True, linewidth=2, linecolor='#CDCDCD')

        return figure
