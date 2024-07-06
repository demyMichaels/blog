import plotly.graph_objs as go
import plotly.io as pio

# Define the data
categories = [
    'Price', 'Relationship management', 'Account executives', 'Corporate dealers',
    'Ease of use', 'Security', 'Accuracy', 'Speed', 'Market commentary', 'Confirmation', 'Tracking'
]

before_values = [1, 2, 4, 4, 3, 2, 3, 2, 1, 2, 1]
after_values = [4, 3, 4, 3, 4, 4, 4, 4, 4, 4, 4]

# Create traces with improved styling
trace_before = go.Scatter(
    x=categories,
    y=before_values,
    mode='lines+markers',
    name='EFS and Other Traditional Competitors’ “Before” Strategy',
    line=dict(dash='dash', color='gray'),
    marker=dict(color='gray')
)

trace_after = go.Scatter(
    x=categories,
    y=after_values,
    mode='lines+markers',
    name='EFS’s “After” Strategy',
    line=dict(color='limegreen'),
    marker=dict(color='limegreen')
)

# Layout with gradient background
layout = go.Layout(
    title='EFS: Before and After',
    yaxis=dict(title='High', range=[0, 5], tickvals=[1, 2, 3, 4]),
    xaxis=dict(title='Low'),
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background for the paper
    plot_bgcolor='rgba(255,255,255,0.9)',   # Light gray background for the plot
    font=dict(color='black'),
    title_font=dict(size=24, color='black', family="Arial, sans-serif"),
    xaxis_tickangle=-45,
    hovermode='x unified'
)

# Create the figure
fig = go.Figure(data=[trace_before, trace_after], layout=layout)

# Update layout for hover interactions
fig.update_traces(
    hoverinfo="x+y+name",
    line=dict(width=2),
    marker=dict(size=8)
)

fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Arial"
    ),
    legend=dict(
        x=0.5,
        y=-0.2,
        xanchor='center',
        orientation='h'
    )
)

# Save the figure as an interactive HTML file
output_file = 'blue_ocean_strategy.html'
fig.write_html(output_file)

print(f"Interactive chart saved to {output_file}")
