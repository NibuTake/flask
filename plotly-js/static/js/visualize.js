$('a#visualize').bind('click', function() {
    $.getJSON($SCRIPT_ROOT + '/_calc_dist', {
      mean: $('input[name="mean"]').val(),
      var: $('input[name="var"]').val()
    }, function(data) {
      // Recieve data from python as json and json.dumped.
      var ids = data.ids;
      var graphs = JSON.parse(data.graphJ);

      // Plot by plotly.
      Plotly.newPlot(ids[0],
                  graphs[0].data,
                  graphs[0].layout || {});
    });
    return false;
  });
