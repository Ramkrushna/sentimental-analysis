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
//Q1 
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
                    chartTitle = data.chart_title
                    chartData = data.chartData;
                    renderPieChart(chartData);
                }
            },
            error: function(jqXHR, textStatus, errorThrown)
          {
              alert(errorThrown);
           }
        });
});

//Q2
    $('#display-charts-q2').on('click', function(){

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
                    chartData = data;
                    renderPieChart(chartData);
                }
            },
            error: function(jqXHR, textStatus, errorThrown)
          {
              alert(errorThrown);
           }
        });
});


//Q3
    $('#display-charts-q3').on('click', function(){

    $.ajax({
            dataType: "json",
            type: "GET",
            url: '/q3/',
            success: function(data){
            console.log('test');
                if(data.error) {
                    alert(data.error);
                } else {

                    console.log(data);
                    chartData = data;
                    renderPieChart(chartData);
                }
            },
            error: function(jqXHR, textStatus, errorThrown)
          {
              alert(errorThrown);
           }
        });
});


//Q4
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

                    console.log(data);
                    chartData = data;
                    renderPieChart(chartData);
                }
            },
            error: function(jqXHR, textStatus, errorThrown)
          {
              alert(errorThrown);
           }
        });
});


//Q5
    $('#display-charts-q5').on('click', function(){

    $.ajax({
            dataType: "json",
            type: "GET",
            url: '/q5/',
            success: function(data){
            console.log('test');
                if(data.error) {
                    alert(data.error);
                } else {

                    console.log(data);
                    chartData = data;
                    renderPieChart(chartData);
                }
            },
            error: function(jqXHR, textStatus, errorThrown)
          {
              alert(errorThrown);
           }
        });
});


//Q6
    $('#display-charts-q6').on('click', function(){

    $.ajax({
            dataType: "json",
            type: "GET",
            url: '/q6/',
            success: function(data){
            console.log('test');
                if(data.error) {
                    alert(data.error);
                } else {

                    console.log(data);
                    chartData = data;
                    renderPieChart(chartData);
                }
            },
            error: function(jqXHR, textStatus, errorThrown)
          {
              alert(errorThrown);
           }
        });
});


//Q7
    $('#display-charts-q7').on('click', function(){

    $.ajax({
            dataType: "json",
            type: "GET",
            url: '/q7/',
            success: function(data){
            console.log('test');
                if(data.error) {
                    alert(data.error);
                } else {

                    console.log(data);
                    chartData = data;
                    renderPieChart(chartData);
                }
            },
            error: function(jqXHR, textStatus, errorThrown)
          {
              alert(errorThrown);
           }
        });
});
