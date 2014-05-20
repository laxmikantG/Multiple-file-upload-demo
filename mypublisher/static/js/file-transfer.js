var handleFiles = function(files, droplist, flag){
	var numFiles = files.length;
	show_list_message(numFiles);
	var items ="";
	for (var i = 0; i < numFiles; i++) {
		  var file = files[i];
		  items += '<li class="list-group-item">'+file.name+' <span class="badge" title="delete" onclick="remove_selected(this, '+i+', \''+file.name+'\');">X</span>\
		  <input type="hidden" name="deleted_'+i+'" id="deleted_'+i+'"  value=""></li>'
	}
	$("#"+droplist).html(items);
	$("#upload-files").unbind("click");
	$("#upload-files").bind("click", function(){
		uplaodFilesToServer(files);
		$(this).attr("disabled", "disabled");
	});
}

var remove_selected = function(listitem ,filenum, filename){
	$("#deleted_"+filenum).val(filename);
	$(listitem).closest("li").hide();
	var count = $(".list-group-item:visible").length;
	show_list_message(count);
	if(count == "0")$(".list-group-item").remove();
}

function uplaodFilesToServer(blobFiles) {
    var fd = new FormData();
	for (var i = 0; i < blobFiles.length; i++)
	{
		file = blobFiles[i];
		fd.append(file.name, file);
	}
    $.ajax({
       url: $("form").attr("action"),
       type: "POST",
       data: fd,
       processData: false,
       contentType: false,
       beforeSend: function(xhr, settings) {
           if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
        	   var csrftoken = getCookie('csrftoken');
               xhr.setRequestHeader("X-CSRFToken", csrftoken);
           }
       },
       success: function(response) {
    	   	$("#uploadmsg").addClass("show");
    	   	$("#uploadmsg").removeClass("hide");
    	   	$("#message").text(response.message);
    	   	clean_area();
       },
       error: function(xhr, status, errorMessage) {
           console.log(errorMessage); // Optional
       }
    });
}  

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
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
		$("#message").text("");
		$("#uploadmsg").addClass("hide");
	   	$("#uploadmsg").removeClass("show");
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
	  var numFiles = files.length;
	  handleFiles(files, "list-dnd-files", 1);
}
clean_area = function(){
	var count = "0";
	show_list_message(count);
	if(count == "0")$(".list-group-item").remove();
	$("#upload-files").removeAttr("disabled");
}

$(function(){
	select_upload_choice();
	handle_drag_and_drop()
});


