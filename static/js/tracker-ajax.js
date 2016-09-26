$('.complete_button').click(function(){
	var task_id;
	task_id = $(this).attr("data-taskid");
	$.get('/tracker/task/complete/', {task_id: task_id}, function(data){
		$('#item-status').html(data);
		$('.complete_button').hide();
	});
});

$('#delete_button').click(function(){
	var task_id;
	task_id = $(this).attr("data-taskid");
    var deleteUrl = '/tracker/task/' + task_id + '/delete/';
	$.post(deleteUrl, {}, function(data){
		$('#item-status').html(data);
	});
});


