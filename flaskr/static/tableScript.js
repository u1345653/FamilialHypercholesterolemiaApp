// function updateTableVal(obj) {
//
// 	var userinputcadstat1 = obj;
// 	var cadstat1 = userinputcadstat1.options[userinputcadstat1.selectedIndex].value;
// 	var tablecadstat1 = document.getElementById("ped1TableCadStat");
//
// 	if (cadstat1 === "1") {
// 		tablecadstat1 = cadstat1;
// 		tablecadstat1.valueOf();
// 	}
// 	else if (cadstat1 === "9") {
// 		tablecadstat1 = cadstat1;
// 	}
// 	else
// 		tablecadstat1 = cadstat1;
// }

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

// function createTable() {
//
// 	// Age Values
// 	var age1 = 0, age2 = 0, age3 = 0, age4 = 0, age5 = 0, age6 = 0, age7 = 0, age8 = 0, age9 = 0;
// 	age1 = parseFloat( document.getElementById("ped1Age").value );
// 	age2 = parseFloat( document.getElementById("ped2Age").value );
// 	age3 = parseFloat( document.getElementById("ped3Age").value );
// 	age4 = parseFloat( document.getElementById("ped4Age").value );
// 	age5 = parseFloat( document.getElementById("ped5Age").value );
// 	age6 = parseFloat( document.getElementById("ped6Age").value );
// 	age7 = parseFloat( document.getElementById("ped7Age").value );
// 	age8 = parseFloat( document.getElementById("ped8Age").value );
// 	age9 = parseFloat( document.getElementById("ped9Age").value );
//
// 	// Gender Values
// 	var gender1 = "", gender2 = "", gender3 = "", gender4 = "", gender5 = "", gender6 = "", gender7 = "", gender8 = "", gender9 = "";
// 	gender1 = document.getElementById("ped1Gender").value;
// 	gender2 = document.getElementById("ped2Gender").value;
// 	gender3 = document.getElementById("ped3Gender").value;
// 	gender4 = document.getElementById("ped4Gender").value;
// 	gender5 = document.getElementById("ped5Gender").value;
// 	gender6 = document.getElementById("ped6Gender").value;
// 	gender7 = document.getElementById("ped7Gender").value;
// 	gender8 = document.getElementById("ped8Gender").value;
// 	gender9 = document.getElementById("ped9Gender").value;
//
// 	// LDL Values
// 	var ldl1 = 0, ldl2 = 0, ldl3 = 0, ldl4 = 0, ldl5 = 0, ldl6 = 0, ldl7 = 0, ldl8 = 0, ldl9 = 0;
// 	ldl1 = parseFloat( document.getElementById("ped1LDLChol").value );
// 	ldl2 = parseFloat( document.getElementById("ped2LDLChol").value );
// 	ldl3 = parseFloat( document.getElementById("ped3LDLChol").value );
// 	ldl4 = parseFloat( document.getElementById("ped4LDLChol").value );
// 	ldl5 = parseFloat( document.getElementById("ped5LDLChol").value );
// 	ldl6 = parseFloat( document.getElementById("ped6LDLChol").value );
// 	ldl7 = parseFloat( document.getElementById("ped7LDLChol").value );
// 	ldl8 = parseFloat( document.getElementById("ped8LDLChol").value );
// 	ldl9 = parseFloat( document.getElementById("ped9LDLChol").value );
//
// 	// TOT-C Values
// 	var totc1 = 0, totc2 = 0, totc3 = 0, totc4 = 0, totc5 = 0, totc6 = 0, totc7 = 0, totc8 = 0, totc9 = 0;
// 	totc1 = parseFloat( document.getElementById("ped1TOTChol").value );
// 	totc2 = parseFloat( document.getElementById("ped2TOTChol").value );
// 	totc3 = parseFloat( document.getElementById("ped3TOTChol").value );
// 	totc4 = parseFloat( document.getElementById("ped4TOTChol").value );
// 	totc5 = parseFloat( document.getElementById("ped5TOTChol").value );
// 	totc6 = parseFloat( document.getElementById("ped6TOTChol").value );
// 	totc7 = parseFloat( document.getElementById("ped7TOTChol").value );
// 	totc8 = parseFloat( document.getElementById("ped8TOTChol").value );
// 	totc9 = parseFloat( document.getElementById("ped9TOTChol").value );
//
// 	// TX Status Values
// 	var tx1 = 0, tx2 = 0, tx3 = 0, tx4 = 0, tx5 = 0, tx6 = 0, tx7 = 0, tx8 = 0, tx9 = 0;
// 	tx1 = parseFloat( document.getElementById("ped1TXStatus").value );
// 	tx2 = parseFloat( document.getElementById("ped2TXStatus").value );
// 	tx3 = parseFloat( document.getElementById("ped3TXStatus").value );
// 	tx4 = parseFloat( document.getElementById("ped4TXStatus").value );
// 	tx5 = parseFloat( document.getElementById("ped5TXStatus").value );
// 	tx6 = parseFloat( document.getElementById("ped6TXStatus").value );
// 	tx7 = parseFloat( document.getElementById("ped7TXStatus").value );
// 	tx8 = parseFloat( document.getElementById("ped8TXStatus").value );
// 	tx9 = parseFloat( document.getElementById("ped9TXStatus").value );
//
// 	// CAD Status Values
// 	var cadstat1 = 0, cadstat2 = 0, cadstat3 = 0, cadstat4 = 0, cadstat5 = 0, cadstat6 = 0, cadstat7 = 0, cadstat8 = 0, cadstat9 = 0;
// 	cadstat1 = parseFloat( document.getElementById("ped1CadStatus").value );
// 	cadstat2 = parseFloat( document.getElementById("ped2CadStatus").value );
// 	cadstat3 = parseFloat( document.getElementById("ped3CadStatus").value );
// 	cadstat4 = parseFloat( document.getElementById("ped4CadStatus").value );
// 	cadstat5 = parseFloat( document.getElementById("ped5CadStatus").value );
// 	cadstat6 = parseFloat( document.getElementById("ped6CadStatus").value );
// 	cadstat7 = parseFloat( document.getElementById("ped7CadStatus").value );
// 	cadstat8 = parseFloat( document.getElementById("ped8CadStatus").value );
// 	cadstat9 = parseFloat( document.getElementById("ped9CadStatus").value );
//
// 	// CAD Age Onset Values
// 	var cadage1 = 0, cadage2 = 0, cadage3 = 0, cadage4 = 0, cadage5 = 0, cadage6 = 0, cadage7 = 0, cadage8 = 0, cadage9 = 0;
// 	cadage1 = parseFloat( document.getElementById("ped1CadAge").value );
// 	cadage2 = parseFloat( document.getElementById("ped2CadAge").value );
// 	cadage3 = parseFloat( document.getElementById("ped3CadAge").value );
// 	cadage4 = parseFloat( document.getElementById("ped4CadAge").value );
// 	cadage5 = parseFloat( document.getElementById("ped5CadAge").value );
// 	cadage6 = parseFloat( document.getElementById("ped6CadAge").value );
// 	cadage7 = parseFloat( document.getElementById("ped7CadAge").value );
// 	cadage8 = parseFloat( document.getElementById("ped8CadAge").value );
// 	cadage9 = parseFloat( document.getElementById("ped9CadAge").value );
//
// 	// DNA DX Status Values
// 	var dna1 = 0, dna2 = 0, dna3 = 0, dna4 = 0, dna5 = 0, dna6 = 0, dna7 = 0, dna8 = 0, dna9 = 0, dnaCalc = 0;
// 	dna1 = parseFloat( document.getElementById("ped1DnaDxStatus").value );
// 	dna2 = parseFloat( document.getElementById("ped2DnaDxStatus").value );
// 	dna3 = parseFloat( document.getElementById("ped3DnaDxStatus").value );
// 	dna4 = parseFloat( document.getElementById("ped4DnaDxStatus").value );
// 	dna5 = parseFloat( document.getElementById("ped5DnaDxStatus").value );
// 	dna6 = parseFloat( document.getElementById("ped6DnaDxStatus").value );
// 	dna7 = parseFloat( document.getElementById("ped7DnaDxStatus").value );
// 	dna8 = parseFloat( document.getElementById("ped8DnaDxStatus").value );
// 	dna9 = parseFloat( document.getElementById("ped9DnaDxStatus").value );
//
// 	// PERSON PROB VALUES
//
// 	if (document.getElementById( "ped1FhProb") != null) {
// 		var personprob1 = parseFloat( document.getElementById("ped1FhProb").item(0).innerHTML.obj.value );
// 	}
// 	if (document.getElementById( "ped2FhProb") != null) {
// 		var personprob2 = parseFloat( document.getElementById("ped2FhProb").item(0).innerHTML.obj.value );
// 	}
// 	if (document.getElementById( "ped3FhProb") != null) {
// 		var personprob3 = parseFloat( document.getElementById("ped3FhProb").item(0).innerHTML.obj.value );
// 	}
// 	if (document.getElementById( "ped4FhProb") != null) {
// 		var personprob4 = parseFloat( document.getElementById("ped4FhProb").item(0).innerHTML.obj.value );
// 	}
// 	if (document.getElementById( "ped5FhProb") != null) {
// 		var personprob5 = parseFloat( document.getElementById("ped5FhProb").item(0).innerHTML.obj.value );
// 	}
// 	if (document.getElementById( "ped6FhProb") != null) {
// 		var personprob6 = parseFloat( document.getElementById("ped6FhProb").item(0).innerHTML.obj.value );
// 	}
// 	if (document.getElementById( "ped7FhProb") != null) {
// 		var personprob7 = parseFloat( document.getElementById("ped7FhProb").item(0).innerHTML.obj.value );
// 	}
// 	if (document.getElementById( "ped8FhProb") != null) {
// 		var personprob8 = parseFloat( document.getElementById("ped8FhProb").item(0).innerHTML.obj.value );
// 	}
// 	if (document.getElementById( "ped9FhProb") != null) {
// 		var personprob9 = parseFloat( document.getElementById("ped9FhProb").item(0).innerHTML.obj.value );
// 	}
//
// 	// personprob1 = parseFloat(document.getElementsByTagName("ped1FhProb").item(0).innerHTML.obj.value );
// 	// personprob2 = parseFloat(document.getElementsByTagName("ped2FhProb").item(0).innerHTML.obj.value );
// 	// personprob3 = parseFloat(document.getElementsByTagName("ped3FhProb").item(0).innerHTML.obj.value );
// 	// personprob4 = parseFloat(document.getElementsByTagName("ped4FhProb").item(0).innerHTML.obj.value );
// 	// personprob5 = parseFloat(document.getElementsByTagName("ped5FhProb").item(0).innerHTML.obj.value );
// 	// personprob6 = parseFloat(document.getElementsByTagName("ped6FhProb").item(0).innerHTML.obj.value );
// 	// personprob7 = parseFloat(document.getElementsByTagName("ped7FhProb").item(0).innerHTML.obj.value );
// 	// personprob8 = parseFloat(document.getElementsByTagName("ped8FhProb").item(0).innerHTML.obj.value );
// 	// personprob9 = parseFloat(document.getElementsByTagName("ped9FhProb").item(0).innerHTML.obj.value );
//
// 	result = document.getElementById('tableHeader');
// 	result.innerHTML = '<h3>Family PhenoType Information: </h3>';
//
// 	var array = [["Person", 'Age', 'Gender', 'LDL Cholesterol', 'TOT-C Cholesterol', 'TX Status', 'CAD Status', 'CAD Onset Age', 'DNA-DX Status', 'FH Probability'],
// 		["1 - Grandmother on Parent 1's Side", age1, gender1, ldl1, totc1, tx1, cadstat1, cadage1, dna1, personprob1],
// 		["2 - Grandfather on Parent 1's Side", age2, gender2, ldl2, totc2, tx2, cadstat2, cadage2, dna2, personprob2],
// 		["3 - Sibling of Parent 1", age3, gender3, ldl3, totc3, tx3, cadstat3, cadage3, dna3, personprob3],
// 		["4 - Second Sibling of Parent 1", age4, gender4, ldl4, totc4, tx4, cadstat4, cadage4, dna4, personprob4],
// 		["5 - Parent 1", age5, gender5, ldl5, totc5, tx5, cadstat5, cadage5, dna5, personprob5],
// 		["6 - Parent 2", age6, gender6, ldl6, totc6, tx6, cadstat6, cadage6, dna6, personprob6],
// 		["7 - Child 1 of Parent 1 & 2", age7, gender7, ldl7, totc7, tx7, cadstat7, cadage7, dna7, personprob7],
// 		["8 - Child 2 of Parent 1 & 2", age8, gender8, ldl8, totc8, tx8, cadstat8, cadage8, dna8, personprob8],
// 		["9 - Child 3 of Parent 1 & 2", age9, gender9, ldl9, totc9, tx9, cadstat9, cadage9, dna9,  personprob9]] ;
//
// 	var tableData = array;
//
// 	var table = document.getElementById('createdTable');
// 	table.setAttribute('id', 'createdTable');
// 	// table.innerHTML = "";
//
//
// 	var row = {};
// 	var cell = {};
//
// 	tableData.forEach( function (rowData) {
// 		row = table.insertRow(-1);
// 		rowData.forEach( function (cellData) {
// 			cell = row.insertCell();
// 			cell.textContent = cellData;
// 		});
// 	});
//
// 	//
// 	//
// 	// var famText = "";
// 	// famText = document.getElementById("familyProb");
// 	// famText.innerHTML = '<br><br><b>Family Pedigree FH Probability: <i>Insert % Prob Here</i></b>'
// }