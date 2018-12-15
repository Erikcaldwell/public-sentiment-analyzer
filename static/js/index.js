d3.json('/data').then(function(data) {
    console.log(data);
    data.forEach(function(d) {
        console.log(d);
        var results = d3.select("#results")
        results.append("hr")
        results.append("div")
        .attr("class", "row justify-content-center")
        .html(
            `<div class="col-4">
                <div class="card text-center" style="width: 160px;">
                    <img class="card-img-top" src=${d.Image} alt="${d.Name} Image">
                    <div class="card-body">
                        <h5 class="card-text">
                        ${d.Name}
                        </h5>
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div id=${d.Handle} class="250x200px">
                </div>
            </div>`
            );

        var g = new JustGage({
            id: d.Handle,
            value: d.Score.toFixed(3),
            min: -1,
            max: 1,
            title: d.Handle,
            formatNumber: true,
            relativeGaugeSize: true,
            pointer: true,
            customSectors: [{
                // negative scores (red)
                color : "#ff0000",
                lo : -1,
                hi : -0.051
                },
                // neutral scores (yellow)
                {
                color : "#ffff00",
                lo : -0.05,
                hi : 0.05
                },
                // positive scores (green)
                {        
                color : "#00ff00",
                lo : 0.05,
                hi : 1
            }],
        });
    })
});