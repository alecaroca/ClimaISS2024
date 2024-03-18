
var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
  // This function will display the specified tab of the form...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  //... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Siguiente";
  }
  //... and run a function that will display the correct step indicator:
  fixStepIndicator(n)
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form...
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    if((!document.querySelector('input[name="pregunta1"]:checked')) || (!document.querySelector('input[name="pregunta2"]:checked'))||
    (!document.querySelector('input[name="pregunta3"]:checked')) || (!document.querySelector('input[name="pregunta4"]:checked'))||
    (!document.querySelector('input[name="pregunta5"]:checked')) || (!document.querySelector('input[name="pregunta6"]:checked'))||
    (!document.querySelector('input[name="pregunta7"]:checked')) || (!document.querySelector('input[name="pregunta8"]:checked'))||
    (!document.querySelector('input[name="pregunta9"]:checked')) || (!document.querySelector('input[name="pregunta10"]:checked'))||
    (!document.querySelector('input[name="pregunta11"]:checked')) || (!document.querySelector('input[name="pregunta12"]:checked'))||
    (!document.querySelector('input[name="pregunta13"]:checked')) || (!document.querySelector('input[name="pregunta14"]:checked'))||
    (!document.querySelector('input[name="pregunta15"]:checked')) || (!document.querySelector('input[name="pregunta16"]:checked'))||
    (!document.querySelector('input[name="pregunta17"]:checked')) || (!document.querySelector('input[name="pregunta18"]:checked'))||
    (!document.querySelector('input[name="pregunta19"]:checked')) || (!document.querySelector('input[name="pregunta20"]:checked'))||
    (!document.querySelector('input[name="pregunta21"]:checked')) || (!document.querySelector('input[name="pregunta22"]:checked'))||
    (!document.querySelector('input[name="pregunta23"]:checked')) || (!document.querySelector('input[name="pregunta24"]:checked'))){
     
      alert("Hubo un error en tu encuesta, es posible que falten datos, porfavor vuelve a realizar la encuesta")
      location.href ="http://www.climaiss.cl";
      event.preventDefault(e);
    }
    else{
      document.getElementById("regForm").submit();
      return false;
    }

  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false
      valid = false;
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid; // return the valid status
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class on the current step:
  x[n].className += " active";
}
