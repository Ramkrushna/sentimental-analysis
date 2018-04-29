 function renderPieChart(chartData){ 
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

//Q2
    $('#display-charts-q2').on('click', function(){
    alert("Working");
    $.ajax({
            dataType: "json",
            type: "GET",
            url: '/q2/',
            success: function(data){
            console.log('test');
                if(data.error) {
                    alert(data.error);
                } else {

                    console.log(data);
                    chartData = data.chartData;
                    chartTitle = data.chartTitle;
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

