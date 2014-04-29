var handleFiles = function(files){
	var numFiles = files.length;
	show_list_message(numFiles);
	var items ="";
	for (var i = 0, numFiles; i < numFiles; i++) {
		  var file = files[i];
		  items += '<li class="list-group-item">'+file.name+' <span class="badge" title="delete" onclick="remove_selected(this, '+i+', \''+file.name+'\');">X</span>\
		  <input type="hidden" name="deleted_'+i+'" id="deleted_'+i+'"  value=""></li>'
	}
	$("#list-browse-files").html(items);
}

var remove_selected = function(listitem ,filenum, filename){
	$("#deleted_"+filenum).val(filename);
	$(listitem).closest("li").hide();
	var count = $(".list-group-item:visible").length;
	show_list_message(count);
	if(count == "0")$(".list-group-item").remove();
}

var show_list_message = function(numFiles){
	if(numFiles != 0)
		var text = numFiles.toString()+" file(s) selected.";
	else
		var text = "No file selected.";
	$(".browse_count").text(text);
};
select_upload_choice = function(){
	$("input[name='upload_method']").click(function(){
		var val = $(this).val();
		if(val == 1){
			$("#list-browse-files").show();
			$("#list-dnd-files").hide();
			$("#dnd_method").hide();
			$("#browse_method").show();
		}else{
			$("#list-browse-files").hide();
			$("#list-dnd-files").show();
			$("#browse_method").hide();
			$("#dnd_method").show();
		}
	});
}


handle_drag_and_drop = function(){
	var dropbox;
	dropbox = document.getElementById("dropbox");
	dropbox.addEventListener("dragenter", dragenter, false);
	dropbox.addEventListener("dragover", dragover, false);
	dropbox.addEventListener("drop", drop, false);
}

function dragenter(e){
	  e.stopPropagation();
	  e.preventDefault();
}

function dragover(e){
	  e.stopPropagation();
	  e.preventDefault();
}

function drop(e) {
	  e.stopPropagation();
	  e.preventDefault();

	  var dt = e.dataTransfer;
	  var files = dt.files;

	  handleFiles(files);
	}
$(function(){
	select_upload_choice();
});


