/******************************
* Author: Andres Juarez
* Date: 13-10-2012
******************************/
//Boton Guardar Juegos
$(document).bind("ready",function(){
	$(".btn_aceptar").bind("click",submitGame);
	$(".btn_aceptar_on").bind("click",submitGame);
})

function submitGame(e){
	//alert("Entro");
	if (e){
		e.preventDefault();
	}
        var gameId = this.id.split("_") ;
        
        var local= $("#marcadora_"+gameId[1]).val();
        var visitor = $("#marcadorb_"+gameId[1]).val();
        //alert("El Id del game: "+gameId[1]+" marcadora "+local+" marcadorb_ "+visitor);
        var ruta = "/juegos/1/"+gameId[1]+"/"+local+"/"+visitor;
        var datos = "1/"+gameId[1]+"/"+local+"/"+visitor;
        $.ajax({
                url: "/juegos/",
                type: 'GET',
                async: true,
                data: "1/"+gameId[1]+"/"+local+"/"+visitor,
                success: function(response){
                	//var win = window.open();
                	//win.document.write(response);
                	window.open(ruta, "_self");

                   //alert(response);
                   // $("#marcadora_"+gameId[2]).attr("readonly", "true");
                   //$("#marcadorb_"+gameId[2]).attr("readonly", "true");
                },
                error: function (result) {
                    alert('ERROR ' + result.status + ' ' + result.statusText);}
            });
	
	//$(this.parentNode).contents().find(".btn_aceptar").show();
}



// tab predicciones
$(function() {
    $('.mod_predic').each(function() {
        $(this).click(function(e) {
            var i = $(this).attr('open_id');
			$('.mod_predic').removeClass("mod_predic_focus");
            $('.mod_predic_open').hide(100);
            $('.mod_predic').show(100);
			$('#pre-tab'+i).addClass("mod_predic_focus");
			$(this).hide(100);
            $('#pre'+i).show(100);
			$("#pre-tab"+i+" .marcador1").val($("#pre-tab"+i+" .count1").val());
			$("#pre-tab"+i+" .marcador2").val($("#pre-tab"+i+" .count2").val());
        });
    });
	 $(".btn_cerrar").click(function(e) {
		 	var i = $(this).attr('open_id');
            $('#pre-tab'+i).show(100);
            $('.mod_predic_open').hide(100);
			$('.mod_predic').removeClass("mod_predic_focus");
        });

		$('ul.item_partic:even').addClass('ddt2');
		$('ul.item_partic:odd').addClass('ddt1');
		$('.desta').removeClass("ddt2");
		$('.desta').addClass("user_act");
});

//mostrar velos 
function mostrarMensaje(mensaje){
    if(mensaje != null)
        $("#txt_mensaje").html(mensaje);
    else
        $("#txt_mensaje").html("Tus invitaciones <br/>fueron enviadas correctamente");
        
    $("#share_msj").fadeIn("slow");
}

// verificando que rellene los marcadores para habilitar aceptar
$(function(){
      $('.marcador1, .marcador2').keyup(function(){ 
            var i = $(this).attr('open_id');
            var validated = "";
			var marc1= $("#pre"+i+" .marcador1").val();
			var marc2= $("#pre"+i+" .marcador2").val();
			
            if(marc1>=0 && marc2>=0 && marc2!="" && marc1!="") { validated = true; } else { validated = false; }
 
            if(validated==true) { 
				$("#pre"+i+" .btn_aceptar").addClass("btn_aceptar_on");
				$(".btn_aceptar_on").bind("click",submitGame);
				$("#pre"+i+" .btn_aceptar").removeClass("btn_aceptar");
				$("#pre"+i+" .btn_aceptar_on").removeAttr("disabled");
				var validated = "";
			}else {
				$("#pre"+i+" .btn_aceptar_on").addClass("btn_aceptar");
				$("#pre"+i+" .btn_aceptar").removeClass("btn_aceptar_on");
				$("#pre"+i+" .btn_aceptar").addAttr("disabled");
			}
      });
});

$(document).ready(function(e) {
		
		// cebra de resultados
		$('.item_partic').mouseover( function() { $(this).addClass("ddt3"); });
		$('.item_partic').mouseout( function() { $(this).removeClass("ddt3"); });
		
		$('li.mod_predic:even').addClass('ddt1');
		$('li.mod_predic:odd').addClass('ddt1');
		
		$(".mod_predic").mouseover( function() { $(this).addClass("ddt3"); });
		$('.mod_predic').mouseout( function() { $(this).removeClass("ddt3"); });
		
		
		$('#str_nombre, #str_apellido, #str_correo, #int_numero, #str_twitter, #str_cedula').click(
		function() {
			if (this.value == this.defaultValue) {
					this.value = '';
			}
		}
		);
		$('#str_nombre, #str_apellido, #str_correo, #int_numero, #str_twitter, #str_cedula').blur(
		function() {
			if (this.value == '') {
				this.value = this.defaultValue;
			}
		}
		);	
	
		jQuery.validator.addMethod("notEqual", function(value, element, param) {
			  return this.optional(element) || value != param;
		}, "");

	 	$('#registro').validate( {
		  		submitHandler: function(form) {
					$("div.error_form").hide();
					location.href='juegos_semana.html';
				},
			  errorLabelContainer: $("div.error_form"),
			  rules: {
						str_nombre: {
						  required: true,
						  notEqual: "[Nombre]"
						},
						str_correo: {
						  required: true,
						  email: true,
						  notEqual: "[correo@xyz.com]"
						},
						int_codigo: {
						  required: true,
						  notEqual: "0000"
						},
						int_numero: {
						  maxlength: 7,
						  required: true,
						  digits: true,
						  notEqual: "[0000000]"

						},
						str_apellido: {
						  required: true,
						  notEqual: "[Apellido]"
						},
						str_cedula: {
						  minlength: 7,
						  required: true,
						  digits: true,
						  notEqual: "[00000000]"
						},
						int_fecha_dia: {
						  minlength: 1,
						  required: true
						},
						int_fecha_mes: {
						  required: true
						},
						int_fecha_ano: {
						  required: true
						}
			  },
			  messages: {
						str_nombre: {
							required: '<strong>ERROR:</strong> Ingresa tu nombre <br>'
						},
						str_correo: {
							required: '<strong>ERROR:</strong> Ingresa un email <br>',
							email: '<strong>ERROR:</strong> Ingresa un email valido <br>'
						},
						int_codigo: {
							required: '<strong>ERROR:</strong> Selecciona un codigo de area <br>'
						},
						int_numero: {
						  maxlength: "<strong>ERROR:</strong> Verifica numero <br>",
						  required: "<strong>ERROR:</strong> Ingresa tu numero <br>",
						  digits: "<strong>ERROR:</strong> Solo puedes ingresar numeros en tu telefono <br>"
						},
						str_apellido: {
						  required: "<strong>ERROR:</strong> Ingresa un apellido <br>"
						},
						str_cedula: {
						  required: "<strong>ERROR:</strong> Ingresa tu cedula <br>",
						  digits: "<strong>ERROR:</strong> Solo puedes ingresar numeros en tu cedula <br>"
						},
						int_fecha_dia: {
						  required: "<strong>ERROR:</strong> Selecciona una fecha.<br>"
						},
						int_fecha_mes: {
						  required: "<strong>ERROR:</strong> Selecciona un mes.<br>"
						},
						int_fecha_ano: {
						  required: "<strong>ERROR:</strong> Selecciona un año.<br>"
						}
			  },
        highlight: function(label) {
            $(label).closest('.control-group').addClass('error_form_txt');
        },
        success: function(label) {
   			 label.closest('.control-group').removeClass('error_form_txt').addClass('success');
        }
	 });
	
	$(".btn_borrar").click(function() {
		$("#registro")[0].reset();
	});
	
	$(".btn_no").click(function() {
		$(".error_edad").fadeIn(100);
	});
	
});
