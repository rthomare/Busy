$(function() {
    $('input').change(function() {
      $('#console-event').html('Toggle: ' + $(this).prop('checked'))
        person_id = $(this).attr('data-person-id');
        route = $(this).prop('checked') ? "/not_busy/" : "/busy/";
        $.ajax({
            type: "POST",
            url: "/" + person_id + route,
            data: {
                "busy_image": $(this).attr('data-busy-image'),
                "not_busy_image": $(this).attr('data-not-busy-image')
            },
            success: function() {
                location.reload();
            },
            dataType: "html"
        });
    });
  });