




var checks = document.querySelectorAll("input[data-checkid]");
//colección de todos los checks con el atributo data-checkid

var ShiftPressed = false; //true si tenemos presionada la tecla Shift

var curcheck; //currentcheck  (id)
var curcheckelem;//lo mismo que el currentcheck pero directamente el objeto

var curpivote; //currentpivote  (id)
var checkpivote; //el checkpivote (lo mismo pero directamente el objeto)


var idinicio;
var idfin;


var checkYes = false;



window.addEventListener("keydown", function (event) {
    if (event.key == 'Shift') {
        ShiftPressed = true;
        console.log(event.key + " " + ShiftPressed);
    }
});

window.addEventListener("keyup", function (event) {
    if (event.key == 'Shift') {
        ShiftPressed = false;
        console.log(event.key + " " + ShiftPressed);

    }
});



// con este código ya tenemos ShiftPressed = true solo cuando estamos pulsando Shift



for (var i = 0; i < checks.length; i++) {

    checks[i].addEventListener("click", function () {

        if (ShiftPressed == false) {  //si no tenemos Shift presionado 
            if (checkpivote) { checkpivote.style = "width: 20px;height:20px" }
            curpivote = this.getAttribute("data-checkid"); // el current check = atributo data-checkid
            console.log("check clicado");
            checkpivote = this;
            checkpivote.style = "width: 40px;height:40px"

        };


        if (ShiftPressed == true) {  //si tenemos Shift presionado 
            curcheck = this.getAttribute("data-checkid");
            curcheckelem = this;
            console.log("curcheckelem.checked = " + curcheckelem)


            if (curcheck < curpivote) {
                idinicio = curcheck;
                idfin = curpivote;
            } else {
                idinicio = curpivote;
                idfin = curcheck;
            };

            for (var i = idinicio; i <= idfin; i++) {
                checkquetecrio = document.querySelectorAll(
                    "[data-checkid='" + i + "']"
                )[0];
                //Así buscamos los elementos por el atributo DATAAAAAAAAAAAAA

                // checkquetecrio = document.querySelectorAll('[data-checkid ='' ]');
                // console.log(checkquetecrio.getAttribute("data-checkid"));
                if (curcheckelem.checked == false) { checkquetecrio.checked = false; } else { checkquetecrio.checked = true; }

            };

        };
    });


// 
    checks[i].addEventListener("change", function () {
      console.log (this);
      console.log (`el check numero ${this.getAttribute("data-checkid")} ha cambiado`)
    });



};




//SELECCION POR BLOQUES

parentchecks = document.querySelectorAll("input[data-checkparent]");
for (i = 0; i < parentchecks.length; i++) {
  parentchecks[i].onchange = function () {
    estado = this.checked;
    padresitonumber = this.getAttribute("data-checkparent");
    console.log(padresitonumber + " - " + estado);

    hijitos = document.querySelectorAll(
      "[data-checkchild='" + padresitonumber + "']"
    );
    for (j = 0; j < hijitos.length; j++) {
      hijitos[j].checked = estado;
      console.log(hijitos[j]);
    }
  };
}











// PARA OBTENER LOS RESULTADOSSSS

document.getElementById("btnResult").onclick = function () {
  
    console.log(checks.length);
    var seleccionados =[];
      for (i = 0; i < checks.length; i++) {
      console.log(checks[i]);
      console.log(checks[i].checked);
      console.log(checks[i].value);
      if (checks[i].checked){
        //aquí tenemos que relacionar el check con el objeto que queramos cambiar
        // en principio el value del check podría ser el id de esa fila
        // asi que podríamos hacer nuestra consulta sql mediante AJAX y una vez 
        // terminado el bucle refrescamos la pantalla. como esto depende del resto
        // de los elementos sería más aconsejable que estuviera en un script de la
        // pagina que contiene la tabla.
        
        seleccionados.push(checks[i].value)
      }       
    }
    alert('valores seleccionados: ' + seleccionados.toString());
    // alert('en objeto json: ' + JSON.stringify(seleccionados));
  };



