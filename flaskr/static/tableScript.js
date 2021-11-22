function change(obj) {

	var selectBox = obj;
	var selectedPegigree = selectBox.options[selectBox.selectedIndex].value;
	var ped1Form = document.getElementById("ped1Attributes");
	var ped2Form = document.getElementById("ped2Attributes");
	var ped3Form = document.getElementById("ped3Attributes");
	var ped4Form = document.getElementById("ped4Attributes");
	var ped5Form = document.getElementById("ped5Attributes");
	var ped6Form = document.getElementById("ped6Attributes");
	var ped7Form = document.getElementById("ped7Attributes");
	var ped8Form = document.getElementById("ped8Attributes");
	var ped9Form = document.getElementById("ped9Attributes");

	if (selectedPegigree === 'pedigree1') {
		ped1Form.style.display = "block";
		ped2Form.style.display = "none";
		ped3Form.style.display = "none";
		ped4Form.style.display = "none";
		ped5Form.style.display = "none";
		ped6Form.style.display = "none";
		ped7Form.style.display = "none";
		ped8Form.style.display = "none";
		ped9Form.style.display = "none";
	}	else if (selectedPegigree === 'pedigree2') {
		ped2Form.style.display = "block";
		ped1Form.style.display = "none";
		ped3Form.style.display = "none";
		ped4Form.style.display = "none";
		ped5Form.style.display = "none";
		ped6Form.style.display = "none";
		ped7Form.style.display = "none";
		ped8Form.style.display = "none";
		ped9Form.style.display = "none";
	} else if (selectedPegigree === 'pedigree3') {
		ped3Form.style.display = "block";
		ped2Form.style.display = "none";
		ped1Form.style.display = "none";
		ped4Form.style.display = "none";
		ped5Form.style.display = "none";
		ped6Form.style.display = "none";
		ped7Form.style.display = "none";
		ped8Form.style.display = "none";
		ped9Form.style.display = "none";
	} else if (selectedPegigree === 'pedigree4') {
		ped4Form.style.display = "block";
		ped2Form.style.display = "none";
		ped1Form.style.display = "none";
		ped3Form.style.display = "none";
		ped5Form.style.display = "none";
		ped6Form.style.display = "none";
		ped7Form.style.display = "none";
		ped8Form.style.display = "none";
		ped9Form.style.display = "none";
	} else if (selectedPegigree === 'pedigree5') {
		ped5Form.style.display = "block";
		ped2Form.style.display = "none";
		ped1Form.style.display = "none";
		ped3Form.style.display = "none";
		ped4Form.style.display = "none";
		ped6Form.style.display = "none";
		ped7Form.style.display = "none";
		ped8Form.style.display = "none";
		ped9Form.style.display = "none";
	} else if (selectedPegigree === 'pedigree6') {
		ped6Form.style.display = "block";
		ped2Form.style.display = "none";
		ped1Form.style.display = "none";
		ped3Form.style.display = "none";
		ped4Form.style.display = "none";
		ped5Form.style.display = "none";
		ped7Form.style.display = "none";
		ped8Form.style.display = "none";
		ped9Form.style.display = "none";
	} else if (selectedPegigree === 'pedigree7') {
		ped7Form.style.display = "block";
		ped2Form.style.display = "none";
		ped1Form.style.display = "none";
		ped3Form.style.display = "none";
		ped4Form.style.display = "none";
		ped5Form.style.display = "none";
		ped6Form.style.display = "none";
		ped8Form.style.display = "none";
		ped9Form.style.display = "none";
	} else if (selectedPegigree === 'pedigree8') {
		ped8Form.style.display = "block";
		ped2Form.style.display = "none";
		ped1Form.style.display = "none";
		ped3Form.style.display = "none";
		ped4Form.style.display = "none";
		ped5Form.style.display = "none";
		ped6Form.style.display = "none";
		ped7Form.style.display = "none";
		ped9Form.style.display = "none";
	} else if (selectedPegigree === 'pedigree9') {
		ped9Form.style.display = "block";
		ped2Form.style.display = "none";
		ped1Form.style.display = "none";
		ped3Form.style.display = "none";
		ped4Form.style.display = "none";
		ped5Form.style.display = "none";
		ped6Form.style.display = "none";
		ped7Form.style.display = "none";
		ped8Form.style.display = "none";
	}
}