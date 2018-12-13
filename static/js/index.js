d3.json('/data').then(function(data) {
    console.log(data);
    data.forEach(function(d) {
        console.log(d);
        var results = d3.select("#results")
        results.append("hr")
        results.append("div")
            .attr("class", "row")
            .html(
                `<div class="col-6">
                    <div class="card" style="width: 18rem;">
                        <img class="card-img-top" src=${d.Image} alt="Result Image">
                        <div class="card-body">
                            <h2 class="card-text">${d.Name}</h2>
                        </div>
                    </div>
                    </div>
                    <div class="col-6">
                        <div id=${d.Handle} class="200x160px">
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
    

// function customValue(val) {
//     if (val <= -0.051) {
//         return 'negative';
//     } else if (val >= 0.051) {
//         return 'positive';
//     } else if (val >= -0.05 & val <= 0.05) {
//         return 'neutral';
//     }
// }