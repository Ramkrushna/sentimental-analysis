var profileFunctions = {

    render_c3_chart: function (data, graphId) {
        var categories = []
        var vals = ['vals']
        data.forEach( function(d, index) {
            categories.push(d.label)
            vals.push(d.value)
        });



        var chart = c3.generate({
            bindto: '#'+graphId,
            data: {
                columns: [ vals ],
                types: {vals : 'bar'}
            },
            axis: {
              y: {
                label: {
                  text: 'Y Label',
                  position: 'outer-middle'
                }
              },
              x: {
                type: 'category',
                categories: categories
              }
            }
        });
    }

};


$('#display-charts').on('click', function(){
    $.ajax({
        dataType: "json",
        type: "GET",
        url: '/charts/',
        success: function(data){
        console.log('test');
            if(data.error) {
                alert(data.error);
            } else {
               profileFunctions.render_c3_chart(data, 'charts-display');
            }
        },
        error: function(jqXHR, textStatus, errorThrown) {
          alert(errorThrown);
       }
    });
});
