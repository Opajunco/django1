/*  FUNCIONAMIENTO:

tenemos que tener una lista ordenada de check inputs con 
un atributo data-checkid cuyo valor sea el orden en el que se encuentran
ahora, lo que hace este script es que si usamos el teclado, cuando presionamos Shift, 
se resalta el último check que se tocó, para que sirva de pivote, desde el cual cuando toquemos otro check
se seleccionen todos los que hay enmedio y su volvemos a tocar de de-seleccionan. en el movil para activar el pivote solo hay que dejarlo presionado
y el funcionamiento el igual. para descativar el pivote se deja presionado otra vez.

si hay un check con el atributo data-parent, y otros con data-child, cuando se pinche el data-parent se seleccionan todos los data-child con el mismo número.
FASII

una vez tengamos la seleccion ya lo iteramos para hacer lo que queramos con el 


 */

var checks = document.querySelectorAll("input[data-checkid]");
//colección de todos los checks con el atributo data-checkid
var seleccion = true;
var bigcheck = -1;
var bigcheckelem;
var curcheck;

var checkYes = true;

var idinicio;
var idfin;

var timeout;

for (var i = 0; i < checks.length; i++) {
  //-----------------Recorremos la colección de checkboxes
  //   checks[i].onkeydown = function () {
  checks[i].addEventListener("keydown", function () {
    //------cuando se presiona(keydown) la tecla shift(keyCode 16), el bigcheck toma el valor del id
    //---- además si el check no estaba seleccionado por lo que sea, se le selecciona
    if (event.keyCode == 16) {
      if (bigcheck == -1) {
        bigcheck = this.getAttribute("data-checkid");
        this.style = "width: 30px;height:30px";
        this.checked = true;
        bigcheckelem = this;
        console.log(
          `keycode: ${event.keyCode} - my id i:  ${bigcheck} 
          y ahora el bigcheck es ${bigcheck}-----yyyyy el checked attribute es ${this.checked}`
        );
      }
    }
  });

  //   checks[i].onkeyup = function () {
  checks[i].addEventListener("keyup", function () {
    if (event.keyCode == 16) {
      bigcheckelem.style = "width: 20px;height:20px";

      bigcheck = -1;
      console.log(
        "my id i:  " + this.id + " y ahora el bigcheck es " + bigcheck
      );
    }
  });

  checks[i].addEventListener("click", function () {
    if (bigcheck >= 0) {
      curcheck = this.getAttribute("data-checkid");
      console.log(
        "current check: " +
          curcheck +
          " - ultima seleccion bigcheck: " +
          bigcheck
      );

      if (curcheck < bigcheck) {
        idinicio = curcheck;
        idfin = bigcheck;
      } else {
        idinicio = bigcheck;
        idfin = curcheck;
      }

      for (var i = idinicio; i <= idfin; i++) {
        checkquetecrio = document.querySelectorAll(
          "[data-checkid='" + i + "']"
        )[0];
        //Así buscamos los elementos por el atributo DATAAAAAAAAAAAAA

        // checkquetecrio = document.querySelectorAll('[data-checkid ='' ]');
        // console.log(checkquetecrio.getAttribute("data-checkid"));

        if (checkYes == true) {
          // console.log(checkquetecrio.checked);
          checkquetecrio.checked = true;

          console.log(checkYes);
        } else {
          checkquetecrio.checked = false;
        }
      }
      if (checkYes == true) {
        checkYes = false;
      } else {
        checkYes = true;
      }
      console.log("checkYes = " + checkYes);
    }
  });






  checks[i].addEventListener("focus", function () {
    checkYes = true;
  });

  //   checks[i].addEventListener('touchstart', tachinin, false);
  //   checks[i].addEventListener('touchend', tachinou, false);
  checks[i].ontouchstart = function () {
    tachinin(this);
  };

  checks[i].ontouchend = function () {
    tachinou();
  };

  checks[i].addEventListener("dbclick", function () {
    alert("double click!");
  });
}

function tachinin(elem) {
  // alert(this.checked)
  // touchStartTimeStamp = e.timeStamp;
  timeout = setTimeout(
    // alert(this.checked)
    function () {
      //   alert(elem.getAttribute("data-checkid"));

      if (elem.getAttribute("data-checkid") == bigcheck) {
        bigcheck = -1;
        elem.style = "width: 20px;height:20px";
      } else {
        if (bigcheck > -1) {
          checkanterior = document.querySelectorAll(
            "[data-checkid='" + bigcheck + "']"
          )[0];
          checkanterior.style = "width: 20px;height:20px";
        }

        bigcheck = elem.getAttribute("data-checkid");
        elem.style = "width: 40px;height:40px";
        //   elem.checked =true;
      }

      //    elem.style="border:2px;background:#ff0000";
      // console.log('Input Value:', textInput.value);
    },
    400
  );
}

function tachinou(e) {
  //   touchEndTimeStamp = e.timeStamp;
  clearTimeout(timeout);
  // alert(touchEndTimeStamp - touchStartTimeStamp); // in miliseconds
}







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
