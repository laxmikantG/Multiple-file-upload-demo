/**
 * Project :- IGP:Modules
*/


var files = new Array();
var filesArray = new Array()
function drop(event)
{	
       
	var dt = event.dataTransfer;
	files = dt.files;
            if(files.length > 0)
            { 
                 $('.button-row-igp > button').removeAttr('disabled');
 
                }else{
			$('.button-row-igp > button').attr('disabled','disabled')
            }
	var p,file,	fileInfo,li;
	fileInfo = document.getElementById("filelist");
	for (var i = 0; i < files.length; i++) 
	{	
		file = files[i];
		p = document.createElement("UL");
		li = document.createElement("li");
		li.id = i;
		file_name=file.name;
		li.innerHTML += file.name+"<a class='remove-igp' href='javascript:void(0);' onClick='removeFile(" + i + ",\""+ file_name +"\")'>Remove</a>"+"\n";
		p.appendChild(li);
		fileInfo.appendChild(p);
	}
	$('#file').removeClass('filesHover');
	$('#file h1').hide();
}

function removeFile(identifier,file){
	var removing_File;
	removing_File = document.createElement("INPUT");
	removing_File.setAttribute("type","hidden");
	removing_File.setAttribute("name","Remove");
	removing_File.setAttribute("value",file);
	var childElem=document.getElementById(identifier);
	childElem.parentNode.setAttribute("class", "removed");
	childElem.parentNode.appendChild(removing_File);
	childElem.parentNode.removeChild(childElem);
}


function Upload(Url)
{
	$('.button-row-igp > button').attr('disabled','disabled')
    var url = Url;
	var fd = new FormData();
	var file;	
	fd.append("formdata", $("form[name='cssoperations']").serialize());
	for (var i = 0; i < files.length; i++)
	{
		file = files[i];
		fd.append("name"+i, file.name);
		fd.append("data"+i, file);
		console.log("file", file.name);
		var xhr = new XMLHttpRequest();

		xhr.onreadystatechange=function()
		{
			if (xhr.readyState==4 && xhr.status==200)
			{
				var url = xhr.responseText; 
				var dwnurl = "location.href=\'" + url +"\'" ;
				var btn = '<div class="link" onclick='+dwnurl+'>click here to Download zip file</div>';
				$('#filelist').html(btn);
			}
		}
	}
	xhr.open('POST', url);
	xhr.send(fd);
}

function hover(event){
	$('#file').addClass('filesHover');
}

toogleElm = function(elm)
	{
		if($(elm).hasClass('hide-igp'))
		{
			$(elm).removeClass('hide-igp')
			$(elm).addClass('show-igp')
		}else if($(elm).hasClass('show-igp'))
		{
			$(elm).addClass('hide-igp')
			$(elm).removeClass('show-igp')
		}
	}
