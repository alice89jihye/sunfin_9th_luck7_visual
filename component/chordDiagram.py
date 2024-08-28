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
    
    # Calculate trait percentages
    traits = ['Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness']
    trait_totals = {trait: sum(item['value'] for item in data_json if item['target'] == trait) for trait in traits}
    total = sum(trait_totals.values())
    trait_percentages = {trait: (value / total) * 100 for trait, value in trait_totals.items()}
    
    # HTML and D3.js code
    html_code = f"""
    <!DOCTYPE html>
    <meta charset="utf-8">
    <style>
    body {{
        margin: 0;
        padding: 0;
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }}
    #chart-container {{
        width: 100%;
        height: 80%;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    svg {{
        width: 100%;
        height: 100%;
        max-width: 80vw;
        max-height: 80vw;
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
    #legend {{
        width: 100%;
        padding: 20px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }}
    .legend-item {{
        display: flex;
        align-items: center;
        margin-bottom: 10px;
        font-size: 16px;
        width: 100%;
    }}
    .legend-color {{
        width: 20px;
        height: 20px;
        margin-right: 10px;
        flex-shrink: 0;
    }}
    .legend-label {{
        flex-grow: 1;
        margin-right: 10px;
    }}
    .legend-percentage {{
        font-weight: bold;
    }}
    </style>
    <div id="chart-container">
        <svg></svg>
    </div>
    <div id="legend"></div>
    <script src="https://d3js.org/d3.v6.min.js"></script>
    <script>
    const data = {json.dumps(data_json)};
    const traitPercentages = {json.dumps(trait_percentages)};
    
    function drawChart() {{
        const container = document.getElementById('chart-container');
        const width = container.clientWidth;
        const height = container.clientHeight;
        const size = Math.min(width, height);
        const innerRadius = size * 0.4;
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
            .attr("viewBox", [-size / 2, -size / 2, size, size]);

        svg.selectAll("*").remove();  // Clear previous content

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
            .attr("font-size", `${{size / 100}}px`)
            .attr("transform", d => `rotate(${{(d.startAngle + d.endAngle) * 90 / Math.PI - 90}}) translate(${{outerRadius + 10}}) ${{(d.startAngle + d.endAngle) / 2 > Math.PI ? "rotate(180)" : ""}}`)
            .attr("text-anchor", d => (d.startAngle + d.endAngle) / 2 > Math.PI ? "end" : null)
            .text(d => names[d.index]);

       // Create legend
        const legend = d3.select("#legend");
        legend.selectAll("*").remove();  // Clear previous content

        const traits = ['Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness'];

        legend.selectAll(".legend-item")
            .data(traits)
            .join("div")
            .attr("class", "legend-item")
            .html((d, i) => `
                <div class="legend-color" style="background-color: ${{colors[i]}};"></div>
                <span class="legend-label">${{d}}</span>
                <span class="legend-percentage">${{traitPercentages[d].toFixed(1)}}%</span>
            `);
    }}

    drawChart();
    window.addEventListener('resize', drawChart);
    </script>
    """
    
    # Render HTML and JS code in Streamlit
    components.html(html_code, height=900, width=800)