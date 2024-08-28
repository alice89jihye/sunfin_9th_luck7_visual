import pandas as pd
import streamlit.components.v1 as components

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
    <svg></svg>
    <script src="https://d3js.org/d3.v6.min.js"></script>
    <script>
    const data = {data_json};
    const width = 1080;
    const height = 1080;
    const innerRadius = Math.min(width, height) * 0.5 - 20;
    const outerRadius = innerRadius + 6;

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

    const svg = d3.select("svg")
        .attr("viewBox", [-width / 2, -height / 2, width, height]);

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
    svg.append("g")
        .selectAll("g")
        .data(chords.groups)
        .join("g")
        .append("text")
        .attr("dy", ".35em")
        .attr("transform", d => `rotate(${{(d.startAngle + d.endAngle) * 90 / Math.PI - 90}}) translate(${{outerRadius + 10}}) ${{(d.startAngle + d.endAngle) / 2 > Math.PI ? "rotate(180)" : ""}}`)
        .attr("text-anchor", d => (d.startAngle + d.endAngle) / 2 > Math.PI ? "end" : null)
        .text(d => names[d.index]);
    </script>
    """
    
    # Render HTML and JS code in Streamlit
    components.html(html_code, height=800)



