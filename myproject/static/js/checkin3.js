/*
Requisitos de funcionamiento
Debe haber una serie de divs en filas, llamaremos divrows
dentro de cada divrow debe haber un checkbox encerrado en otro div circular. 
Es decir, al menos cadaa fila debe tener la siguiente estructura: divrow 
(con los datos que queremos extraer, aunque hay que decidir aún si es mejor que estén en el checkbox),
 dentro un div circular que contenga el checkbox,y dentro el checkbox.

esos divrows pueden estar organizados en bloques, encabezados por otro div con el nombre del bloque e igualmente 
un checkbox. En este caso no es estrictamente necesario que esté metido en un div circular.
a estos divs los llamaremos divblocks.

únicamente los checkbox dentro de los divrows deben tener el atributo data-checkid cuyos valores deberán
estar ordenados en orden creciente.

cuando se usen bloques divblocks los checkbox de estos divblock deben tener un atributo "data-checkparent" y 
los checkbox de los divrows deben tener un atributo "data-checkchild" cuyo valor debe coincidir con el valor de 
su coprrespondiente "data-checkparent"

*/



// _DEV_ Implementar la selecci´n multiple en moviles, ontouch (ver checkin.js)

//checkin3 deberá funcionar igual que gmail. 
// más sencillo de checkin2


// 

var checks = document.querySelectorAll("input[data-checkid]");
//colección de todos los checks con el atributo data-checkid

var ShiftPressed = false; //true si tenemos presionada la tecla Shift

var curcheck; //currentcheck  (id)
// var curcheckelem;//lo mismo que el currentcheck pero directamente el objeto

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

const cargadivs = async () => {
  // function cargadivs () {

  checks = document.querySelectorAll("input[data-checkid]");

  for (var i = 0; i < checks.length; i++) {

    checks[i].addEventListener("click", function () {

      if (ShiftPressed == false) {  //si no tenemos Shift presionado 

        curpivote = this.getAttribute("data-checkid"); // el current check = atributo data-checkid
        console.log("check clicado " + this.getAttribute("data-checkid"));
        // checkpivote = this;

        //para saber cual es el pivote actual
        if (checkpivote) { checkpivote.parentElement.style = "background: rgba(0,0,0,0" }
        checkpivote = this;
        checkpivote.parentElement.style = "background: rgba(0,0,0,0.5)"

        if (this.checked == true) { this.parentElement.parentElement.style = "background: rgba(0,0,0,0.3)" }
        else { this.parentElement.parentElement.style = "background: rgba(0,0,0,0)" }

      };


      if (ShiftPressed == true) {  //si tenemos Shift presionado 

        curcheck = this.getAttribute("data-checkid");
        if (!curpivote) { curpivote = curcheck };


        // console.log("curcheckelem.checked = " + curcheckelem)


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
          if (this.checked == false) {
            checkquetecrio.checked = false;
            checkquetecrio.parentElement.parentElement.style = "background: rgba(0,0,0,0)"
          } else {

            checkquetecrio.checked = true;
            checkquetecrio.parentElement.parentElement.style = "background: rgba(0,0,0,0.3)"
          }


        };
        curpivote = curcheck;

        if (checkpivote) { checkpivote.parentElement.style = "background: rgba(0,0,0,0)" }
        checkpivote = this;
        checkpivote.parentElement.style = "background: rgba(0,0,0,0.5)"

      };
    });




    // 
    checks[i].addEventListener("change", function () {
      console.log(this);
      console.log(`el check numero ${this.getAttribute("data-checkid")} ha cambiado`)
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
        // hijitos[j].checked = estado;
        shadowrow (estado, hijitos[j]);

        console.log(hijitos[j]);
      }
    };
  }



}

// boolcheck verdadero si queremos que esté check y falso si no
function shadowrow(boolcheck, checkobject) {
  if (boolcheck == false) {
    checkobject.checked = false;
    checkobject.parentElement.parentElement.style = "background: rgba(0,0,0,0)"
  } else {
  
    checkobject.checked = true;
    checkobject.parentElement.parentElement.style = "background: rgba(0,0,0,0.3)"
  }

}










// PARA OBTENER LOS RESULTADOSSSS

document.getElementById("btnResult").onclick = function () {

  console.log(checks.length);
  var seleccionados = [];
  for (i = 0; i < checks.length; i++) {
    console.log(checks[i]);
    console.log(checks[i].checked);
    console.log(checks[i].value);
    if (checks[i].checked) {
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



