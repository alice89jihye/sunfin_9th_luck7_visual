import pandas as pd
import streamlit.components.v1 as components
import json

def prepare_data(df):
    traits = ['Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness']
    data = []
    for i, row in df.iterrows():
        for trait in traits:
            if row[trait] > 0:
                data.append({
                    'source': row['Name'],
                    'target': trait,
                    'value': row[trait]
                })
    return data

def show(df: pd.DataFrame):
    # Transform data
    data_json = prepare_data(df)
    
    # HTML and D3.js code
    html_code = f"""
    <!DOCTYPE html>
    <meta charset="utf-8">
    <style>
    body {{
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        width: 100vw;
    }}
    #chart-container {{
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    svg {{
        width: 100%;
        height: auto;
        max-width: 100%;
        max-height: 100%;
    }}
    .arc text {{
        font: 10px sans-serif;
        text-anchor: middle;
    }}
    .ribbon path {{
        fill-opacity: 0.67;
        stroke: #000;
        stroke-width: 0.5px;
    }}
    </style>
    <div id="chart-container">
        <svg></svg>
    </div>
    <script src="https://d3js.org/d3.v6.min.js"></script>
    <script>
    const data = {json.dumps(data_json)};
    let width = 1080;
    let height = 1080;
    let innerRadius = Math.min(width, height) * 0.5 - 20;
    let outerRadius = innerRadius + 6;

    const names = Array.from(new Set(data.flatMap(d => [d.source, d.target])));
    const index = new Map(names.map((name, i) => [name, i]));
    const matrix = Array.from(index, () => new Array(names.length).fill(0));
    for (const {{source, target, value}} of data) matrix[index.get(source)][index.get(target)] += value;

    const chord = d3.chordDirected()
        .padAngle(12 / innerRadius)
        .sortSubgroups(d3.descending)
        .sortChords(d3.descending);

    const arc = d3.arc()
        .innerRadius(innerRadius)
        .outerRadius(outerRadius);

    const ribbon = d3.ribbonArrow()
        .radius(innerRadius - 0.5)
        .padAngle(1 / innerRadius);

    const colors = d3.schemeCategory10;

    const svg = d3.select("svg");

    function updateChartSize() {{
        const container = document.getElementById('chart-container');
        const containerWidth = container.clientWidth;
        const containerHeight = container.clientHeight;

        width = Math.min(containerWidth, containerHeight);
        height = width;
        innerRadius = width * 0.5 - 20;
        outerRadius = innerRadius + 6;

        arc.innerRadius(innerRadius).outerRadius(outerRadius);
        ribbon.radius(innerRadius - 0.5);

        svg.attr("viewBox", [-width / 2, -height / 2, width, height]);

        drawChart();
    }}

    function drawChart() {{
        svg.selectAll("*").remove();

        const chords = chord(matrix);

        svg.append("g")
            .selectAll("path")
            .data(chords.groups)
            .join("path")
            .attr("d", arc)
            .attr("fill", d => colors[d.index])
            .attr("stroke", "#fff");

        svg.append("g")
            .attr("fill-opacity", 0.75)
            .selectAll("path")
            .data(chords)
            .join("path")
            .attr("d", ribbon)
            .attr("fill", d => colors[d.target.index])
            .style("mix-blend-mode", "multiply")
            .append("title")
            .text(d => `${{names[d.source.index]}} - ${{names[d.target.index]}}: ${{d.source.value.toFixed(3)}}`);

        // Add labels
        const labels = svg.append("g")
            .selectAll("g")
            .data(chords.groups)
            .join("g")
            .append("text")
            .attr("dy", ".35em")
            .attr("font-size", `${{width / 100}}px`)
            .attr("transform", d => `rotate(${{(d.startAngle + d.endAngle) * 90 / Math.PI - 90}}) translate(${{outerRadius + 10}}) ${{(d.startAngle + d.endAngle) / 2 > Math.PI ? "rotate(180)" : ""}}`)
            .attr("text-anchor", d => (d.startAngle + d.endAngle) / 2 > Math.PI ? "end" : null)
            .text(d => names[d.index]);

        // Adjust viewBox to fit labels
        const bbox = svg.node().getBBox();
        const padding = 20;
        svg.attr("viewBox", `${{bbox.x - padding}} ${{bbox.y - padding}} ${{bbox.width + padding * 2}} ${{bbox.height + padding * 2}}`);
    }}

    updateChartSize();
    window.addEventListener('resize', updateChartSize);
    </script>
    """
    
    # Render HTML and JS code in Streamlit
    components.html(html_code, height=1000)