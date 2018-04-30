 function renderPieChart(chartData){
        alert(chartData); 
        var chart = c3.generate({
        data: {
        // iris data from R
        columns: chartData,
        type : 'pie',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
        }
        });

        chart.load({
        columns: chartData
        });
    }

function renderBarChart(chartData) {
    alert(chartData);
    var chart = c3.generate({
    data: {
        columns: chartData,
        type: 'bar'
    },
    bar: {
        width: {
            ratio: 0.4 // this makes bar width 50% of length between ticks
        }
        // or
        //width: 100 // this makes bar width 100px
    }
    });
}

// Show chart for Q1
    $('#display-charts-q1').on('click', function(){
    $.ajax({
            dataType: "json",
            type: "GET",
            url: '/q1/',
            success: function(data){
            console.log('test');
                if(data.error) {
                    alert(data.error);
                } else {

                    console.log(data);
                    chartData = data.chartData;
                    chartTitle = data.chartTitle;
                    jQuery('#chartTitle div').html('');
                    $('<div class=divText>' + chartTitle + '</div>').appendTo('#chartTitle');
                    renderPieChart(chartData);
                }
            },
            error: function(jqXHR, textStatus, errorThrown)
          {
              alert(errorThrown);
           }
        });
});

// Show chart for Q4
    $('#display-charts-q4').on('click', function(){
    $.ajax({
            dataType: "json",
            type: "GET",
            url: '/q4/',
            success: function(data){
            console.log('test');
                if(data.error) {
                    alert(data.error);
                } else {
                    alert(data.chartData);
                    console.log(data);
                    chartData = data.chartData;
                    chartTitle = data.chartTitle;
                    jQuery('#chartTitle div').html('');
                    $('<div class=divText>' + chartTitle + '</div>').appendTo('#chartTitle');
                    renderBarChart(chartData);
                }
            },
            error: function(jqXHR, textStatus, errorThrown)
          {
              alert(errorThrown);
           }
        });
});
