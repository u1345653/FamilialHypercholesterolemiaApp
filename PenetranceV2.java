package penetrancev2;

import java.util.Scanner;
import java.util.*;

/** Script Title: PenetranceV2
 ** Version: 2
 ** Author: Ricky Snyder
 ** Date: 9.8.21
 ** Purpose: Second iteration of code for Penetrance Functions
 ***** Modifications since prior Version:
 **** 1) Enforced Data Integrity on all user input variables via the addition 
 ****     of Boolean 'while' loops and conditional statements: MORE DIFFICULT THAN ANTICIPATED
 **** 2) Streamlined method calls, and therefore the flow between intr-class methods.

**** TODO: 
 **** 1) Weave User Input Variables into all 511 formula permutations (Completed Binary Table in Number.java file)
 **** 2) From there, complete the incorporation of all other permutation combinations... 
 *        3) Genotypes (Columns C56: K56) 
 *        4) Founder (pedigrees 1-3) & Transmission (pedigrees 4-9) Probabilities (Columns L56:T56)
 *        5) LDL-C or Total-C Penetrance (Columns U56:AC56)
 *        6) Tendon Xanthoma Penetrance (Columns AD56:AL56)
 *        7) Penetrance for CAD (Columns AM56:AU56)
 *        8) Weave in the String Likelihood Section (Completed prior in the StrLikelihood.java file); (Column AV57)
 *        9) Complete Family Section (Column AW57)
 *        10) Complete Numerator Parts for Diagnostic Probability (Columns AX57:BF57)
 *   11) After binary table possibilities are complete compute the values stemming from the product sum row (Row 570, Columns AV:BF) for each Numerator Part for Diagnostic Probability
 *   12) Lastly, compute the FH probability, via the persons Numerator Diagnostic Probability (AX570...) and divide it by the String likelihood (AV570)... 
 *   13) THIS VALUE SHOULD GIVE US THE PROBABILITY THAT THE INDIVDUAL THE DATA PERTAINS TO, HAS TRAITS THAT ARE IN LINE WITH FH HYPERCHOLESTEROLEMIA.
 */

public class PenetranceV2 {

    public static List<Object> getInput()
    {
        
//<editor-fold defaultstate="collapsed" desc="User Age Input: Lines 17-28">
Scanner userAgeInput = new Scanner(System.in);
String agePrompt = "Please enter your Age in years: ";
System.out.println(agePrompt);

while( !userAgeInput.hasNextInt() ) {
    String incorrectAge = String.format("Incorrect Entry. Your input, %s",
            userAgeInput.nextLine() + ", is not a viable age. "
                    + "Please try again." );
    System.out.println(incorrectAge);
    
    if ( userAgeInput.hasNextInt() )
        break;
}
int userAge = userAgeInput.nextInt();
//</editor-fold>

//<editor-fold defaultstate="collapsed" desc="User LDL Level Input: Lines 34-45">
Scanner userLDLInput = new Scanner(System.in);
String LDLPrompt = "Please enter your most recent LDL-C level: ";
System.out.println(LDLPrompt);

while ( !userLDLInput.hasNextInt() ) {
    String incorrectLDL = String.format("Incorrect Entry. Your input, %s", userLDLInput.nextLine() + ", is not a viable LDL input. Please try again.");
    System.out.println(incorrectLDL);
    
    if ( userLDLInput.hasNextInt() )
        break;
}
int userLDL = userLDLInput.nextInt();
//</editor-fold>

//<editor-fold defaultstate="collapsed" desc="User Total Cholesterol Input: Lines 45-56">
Scanner userTOTCInput = new Scanner(System.in);
String TOTCPrompt = "Please enter your most recent Total Cholesterol level: ";
System.out.println(TOTCPrompt);

while ( !userTOTCInput.hasNextInt() ) {
    String incorrectTOTC = String.format("Incorrect Entry. Your input, %s", userTOTCInput.nextLine() + ", is not a viable Total Cholesterol input. Please try again.");
    System.out.println(incorrectTOTC);
    
    if ( userTOTCInput.hasNextInt() )
        break;
}
int userTOTC = userTOTCInput.nextInt();
//</editor-fold>

//<editor-fold defaultstate="collapsed" desc="User Clinical Cad Input: Lines 63-102">
int clinCadYes = 1;
int clinCadNo = 0;
String clinicalCadPrompt = "Has anyone you've known been diagnosed with Coronary Artery Disease? Enter '1' for Yes, or '0' for No: ";

Scanner userClinCadInput = new Scanner(System.in);
int userClincalCad = 0;

do
{
    // Print message prompt asking for user input.
    System.out.println(clinicalCadPrompt);
    
    // First, we need to handle non-integer user input.
    while ( !userClinCadInput.hasNextInt() )
    {
        String incorrectClinCad = String.format("Incorrect entry. Your "
                + "input, %s", userClinCadInput.nextLine() + ", is not an "
                        + "integer value. Please enter '1' for "
                        + "'Yes, or '0' for No: ");
        
        System.out.println(incorrectClinCad);
    }
    
    // After confirming input is an integer, we need to assign it to our
    // integer, then test if it is either 1 or 0.
    userClincalCad = userClinCadInput.nextInt();
    
    // We'll want to have a range we're checking for, that will print an
    // error message. Otherwise, it will break the loop assuming it is a 1 or 0.
    if (userClincalCad != clinCadYes && userClincalCad != clinCadNo )
    {
        String incorrectClinCadNum = String.format("Incorrect integer value. Please try again. ");
        System.out.println(incorrectClinCadNum);
    }
    else
        break;
    
}while ( userClincalCad != clinCadYes || userClincalCad != clinCadNo );
//</editor-fold>

//<editor-fold defaultstate="collapsed" desc="User Gender Input: Lines 104-138">
int maleGender = 1;
int femaleGender = 0;
String genderPrompt = "Please indicate your identified gender. Enter '1' for Male or '0' for Female: ";

int userGender = 0;
Scanner userGenderInput = new Scanner(System.in);

do {
    // Print message prompting for user input.
    System.out.println(genderPrompt);
    
    // Handling of non-integer user input.
    while ( !userGenderInput.hasNextInt() )
    {
        String incorrectGenderPrompt = String.format("Incorrect entry. Your input of %s",
                userGenderInput.nextLine() + " is not an integer value. "
                        + "Please try again entering '1' for Male and '0' for Female.");
        System.out.println(incorrectGenderPrompt);
    }
    
    // Assigning integer val to original variable for further validation.
    userGender = userGenderInput.nextInt();
    
    // Now we'll want to ensure that the integer was either 0 or 1.
    if ( userGender != maleGender && userGender != femaleGender )
    {
        String incorrectGenderNum = String.format("Incorrect entry. Please try again.");
        System.out.println(incorrectGenderNum);
    }
    else
        break;
    
}while( userGender != maleGender || userGender != femaleGender );
//</editor-fold>


//<editor-fold defaultstate="collapsed" desc="CAD Age User Input: Lines 142-154">
Scanner userCADOnsetInput = new Scanner(System.in);
String cadOnsetPrompt = "At what age were you diagnosed with Cornary Artery Disease? ";
System.out.println(cadOnsetPrompt);

while ( !userCADOnsetInput.hasNextInt() ) {
    String incorrectCADAge = String.format("Incorrect Entry. Your input, %s", userCADOnsetInput.nextLine() + ", is not an integer value. Please try again.");
    System.out.println(incorrectCADAge);
    
    if ( userCADOnsetInput.hasNextInt() )
        break;
}
int userCadOnset = userCADOnsetInput.nextInt();
//</editor-fold>

//<editor-fold defaultstate="collapsed" desc="Tendon Xanthoma Input: Lines 158-193">
Scanner userTXInput = new Scanner(System.in);
int unkownTXVal = 9;
int yesTXVal = 1;
int noTXVal = 0;
int userTX = 0;

String txPrompt = "Are you aware of Tendon Xanthoma running in your family? Enter '9' if you're not sure, '1' if Yes, '0' if No:  ";

do
{
    // Print message prompting the user to input #'s.
    System.out.println(txPrompt);
    
    // Handling of non-integer user input.
    while ( !userTXInput.hasNextInt() )
    {
        String incorrectTxInput = String.format("Incorrect entry. Your "
                + "input, %s", userTXInput.nextLine() + ", is not "
                        + "an integer value. Please try again.");
        System.out.println(incorrectTxInput);
    }
    
    // Assigning integer val to input. To then check for 9, 1, or 0 being
    // the integer validated.
    userTX = userTXInput.nextInt();
    
    if ( userTX != unkownTXVal && userTX != yesTXVal && userTX != noTXVal )
    {
        String incorrectTxNumInput = String.format("Incorrect entry. "
                + "Please try again.");
        System.out.println(incorrectTxNumInput);
    }
    else
        break;
    
}while( userTX != unkownTXVal || userTX != yesTXVal || userTX != noTXVal );
//</editor-fold>

return Arrays.asList(userAge, userLDL, userTOTC, userClincalCad, userGender, userCadOnset, userTX);
    }

    public static List<Object> getPenMethods(List userInput)
//<editor-fold defaultstate="collapsed" desc="Penetrance Methods List Object">
    {
        int age;
        double ldl, totc, clinicalCad, gender, cadOnset, tx;
        
        age = (int) userInput.get(0);
        ldl = (int) userInput.get(1);
        totc = (int) userInput.get(2);
        clinicalCad = (int) userInput.get(3);
        gender = (int) userInput.get(4);
        cadOnset = (int) userInput.get(5);
        tx = (int) userInput.get(6);
        
        // Calling the CAD penetrance classes/methods (that does and doesn't contribute to FH).
        double cadPenFHVal = cadIsFH(clinicalCad, gender, cadOnset, age);
        double cadPenNotFHVal = cadIsNotFH(clinicalCad, gender, cadOnset, age);
        
        // Calling the Tx Penetrance classes/methods (that does/doesn't contribute to FH).
        double txPenFHVal = txIsFH(ldl, age, tx);
        double txPenNotFHVal = txNotFH(ldl, age, tx);
        
        // Methods generating users expected LDL Means based on users age and FH Contribution
        double ldlMeanValFH = ldlFHMean(age);
        double ldlMeanValNotFH = ldlNotFHMean(age);
        
        // Methods generating users expected FH LDL SD based on users age and FH Contribution
        double ldlSdValFH = ldlSdFH(age);
        double ldlSdValNotFH = ldlSdNotFH(age);
        
        //Method generating users expected FH Total Cholesterol Mean based on users age.
        double totcMeanValFH = totMeanFH(age);
        double totcMeanValNotFH = totMeanNotFH(age);
        
        //Method generating users expected Tot-C Standard deviation, based on users age;
        double totcSdFH = totSdFH(age);
        double totcSdNotFH = totSdNotFH(age);
        
        return Arrays.asList(cadPenFHVal, cadPenNotFHVal, txPenFHVal, txPenNotFHVal,
                ldlMeanValFH, ldlMeanValNotFH, ldlSdValFH, ldlSdValNotFH,
                totcMeanValFH, totcMeanValNotFH, totcSdFH, totcSdNotFH);
    }
//</editor-fold>
    
    public static List<Object> getCholPenVals(List penMethods)
//<editor-fold defaultstate="collapsed" desc="Cholesterol Penetrance Values List Object">
    {
        Random distTest = new Random();
        
        double meanFHLDL, meanNotFHLDL, sdFHLDL, sdNotFhLDL, meanFHTOTC, meanNotFHTOTC, sdFHTOTC, sdNotFHTOTC;
        
        meanFHLDL = (double) penMethods.get(4);
        meanNotFHLDL = (double) penMethods.get(5);
        sdFHLDL = (double) penMethods.get(6);
        sdNotFhLDL = (double) penMethods.get(7);
        meanFHTOTC = (double) penMethods.get(8);
        meanNotFHTOTC = (double) penMethods.get(9);
        sdFHTOTC = (double) penMethods.get(10);
        sdNotFHTOTC = (double) penMethods.get(11);
        
        // Using the Java Random Class to generate the #'s associated with our normal distribution.
        double LDLNotFH = distTest.nextGaussian()*meanNotFHLDL + sdNotFhLDL;
        double LDLFH = distTest.nextGaussian() * meanFHLDL + sdFHLDL;
        double TOTCNotFh = distTest.nextGaussian() * meanNotFHTOTC + sdNotFHTOTC;
        double TOTCFH = distTest.nextGaussian() * meanFHTOTC + sdFHTOTC;
        
        return Arrays.asList(LDLNotFH, LDLFH, TOTCNotFh, TOTCFH);
    }
//</editor-fold>
    
    public static void main(String[] args) 
    {
    List <Object> userInput = getInput();
    System.out.println("User Input Values: " + userInput);
    
    List <Object> penMethods = getPenMethods(userInput); 
    System.out.println("Penetrance Methods: " + penMethods);
    
    List <Object> cholPenVals = getCholPenVals(penMethods);
    System.out.println("Cholesterol Penetrance Values: " + cholPenVals);
    }

    public static double txIsFH(double userLDL, double userAge, double userTX) 
//<editor-fold defaultstate="collapsed" desc="Tendon Xanthoma FH Value">
    {
        double tx = userTX;
        double LDL = userLDL;
        double age = userAge;
        
        double calcVal;
        
        if (tx == 9 || LDL < 100)
            calcVal = 1;
        
        else if (LDL >= 100)
            calcVal = tx * ((.8205 * age-1.8113)/100) * (1-tx) * (1-(0.8205 * age - 1.8113)/100);
        
        else
            calcVal = 1;
        
        return calcVal;
    }
//</editor-fold>
        
    // Method to generate the probability that Tendon Xanthoma doesn't contribute to FH.
    public static double txNotFH(double userLDL, double userAge, double userTX) 
//<editor-fold defaultstate="collapsed" desc="Tendon Xanthoma Non-FH Value">
    {
        double tx = userTX;
        double LDL = userLDL;
        double aqe = userAge;
        
        double calcVal;
        
        if (tx == 9)
            calcVal = 1;
        
        else if (tx == 1)
            calcVal = 0.0001;
        
        else
            calcVal = 1 - 0.0001;
        
        return calcVal;
        
    }
//</editor-fold>

    // Method to generate the probability that CAD contributes to FH.
    public static double cadIsFH(double userClincalCad, double userGender, double userCadOnset, double userAge) 
//<editor-fold defaultstate="collapsed" desc="Coronary Artery Disease FH Value">
    {
        double clinicalCad = userClincalCad;
        double gender = userGender;
        double OnsetAge = userCadOnset;
        double age = userAge;
        
        double cadCalcVal;
        
        if (clinicalCad == 9)
            cadCalcVal = 1;
        
        else if (gender == 0 && clinicalCad == 0)
            cadCalcVal = (0.832/(1+(Math.exp(0.155 * (54.7 - OnsetAge)))));
        
        else if (gender == 0 && clinicalCad != 0)
            cadCalcVal = 1 - (0.832/(1+Math.exp(0.124*(52.9-age))));
        
        else if (gender != 0 && clinicalCad == 0)
            cadCalcVal = (.601/ (1 + Math.exp(0.155 * (54.7-OnsetAge))));
        
        else
            cadCalcVal = 1 - (.601 / (1+Math.exp(.155 * (54.7 - age))));
        
        return cadCalcVal;
    }
//</editor-fold>

    // Method to generate the probability that CAD does not contribute to FH.
    public static double cadIsNotFH(double userClincalCad, double userGender, double userCadOnset, double userAge) 
//<editor-fold defaultstate="collapsed" desc="Coronary Artery Disease Non-FH Value">
    {
        double clinicalCad = userClincalCad;
        double gender = userGender;
        double OnsetAge = userCadOnset;
        double age = userAge;
        
        double cadCalcVal;
        
        if (clinicalCad == 9)
            cadCalcVal = 1;
        
        else if (gender == 1 && clinicalCad == 1)
            cadCalcVal = 0.499/(1+Math.exp(0.142 *(69.6-OnsetAge)));
        
        else if (gender == 1 && clinicalCad != 1)
            cadCalcVal = 1 - (0.499/(1+Math.exp(0.0981*(88.6-age))));
        
        else if (gender != 1 && clinicalCad == 1)
            cadCalcVal = 0.601/(1+Math.exp(0.155*(54.7-OnsetAge)));
        
        else
            cadCalcVal = 1 - (.601/(1+Math.exp(0.155*(54.7-age))));
        
        return cadCalcVal;
    }
//</editor-fold>
        
    private static double ldlFHMean(double userAge) 
//<editor-fold defaultstate="collapsed" desc="LDL FH Mean Value">
    {
        final int under20sMeanFH = 205;
        final int in20sMeanFH = 222;
        final int over20sMeanFH = 222;
        
        double age = userAge;
        double meanVal;
        
        if (age < 20)
            meanVal = under20sMeanFH;
        
        else if (age >= 20 && age <30)
            meanVal = in20sMeanFH;
        
        else
            meanVal = over20sMeanFH;
        
        return meanVal;
        
    }
//</editor-fold>
    
    private static double ldlNotFHMean(double userAge) 
//<editor-fold defaultstate="collapsed" desc="LDL Non-FH Mean Value">
    {
        final int under20sMeanNotFH = 89;
        final int in20sMeanNotFH = 105;
        final int over20sMeanNotFH = 121;
        
        double age = userAge;
        double meanVal;
        
        if (age < 20)
            meanVal = under20sMeanNotFH;
        
        else if (age >= 20 && age <30)
            meanVal = in20sMeanNotFH;
        
        else
            meanVal = over20sMeanNotFH;
        
        return meanVal;
        
    }
//</editor-fold>

    private static double ldlSdFH(double userAge) 
//<editor-fold defaultstate="collapsed" desc="LDL FH Standard Deviation Value">
    {
        final int under20sSdFH = 55;
        final int in20sSdFH = 76;
        final int over20sSdFH = 76;
        
        double age = userAge;
        double sdVal;
        
        if (age < 20)
            sdVal = under20sSdFH;
        
        else if (age >= 20 && age < 30)
            sdVal = in20sSdFH;
        
        else
            sdVal = over20sSdFH;
        
        return sdVal;
    }
//</editor-fold>

    private static double ldlSdNotFH(double userAge) 
//<editor-fold defaultstate="collapsed" desc="LDL Non-FH Standard Deviation Value">
    {
        final int under20sSdNotFH = 26;
        final int in20sSdNotFH = 32;
        final int over20sSdNotFH = 35;
        
        double age = userAge;
        double sdVal;
        
        if (age < 20)
            sdVal = under20sSdNotFH;
        
        else if (age >= 20 && age < 30)
            sdVal = in20sSdNotFH;
        
        else
            sdVal = over20sSdNotFH;
        
        return sdVal;
    }
//</editor-fold>

    private static double totMeanFH(double userAge) 
//<editor-fold defaultstate="collapsed" desc="Total Cholesterol FH Mean value">
    {
        final int under20sMeanFH = 279;
        final int in20sMeanFH = 309;
        final int over20sMeanFH = 316;
        
        double age = userAge;
        double meanVal;
        
        if (age < 20)
            meanVal = under20sMeanFH;
        
        else if (age >= 20 && age < 30)
            meanVal = in20sMeanFH;
        
        else
            meanVal = over20sMeanFH;
        
        return meanVal;
    }
//</editor-fold>

    private static double totMeanNotFH(double userAge) 
//<editor-fold defaultstate="collapsed" desc="Total Cholesterol Non-FH Mean Value">
    {
        final int under20sMeanNotFH = 158;
        final int in20sMeanNotFH = 177;
        final int over20sMeanNotFH = 201;
        
        double age = userAge;
        double meanVal;
        
        if (age < 20)
            meanVal = under20sMeanNotFH;
        
        else if (age >= 20 && age < 30)
            meanVal = in20sMeanNotFH;
        
        else
            meanVal = over20sMeanNotFH;
        
        return meanVal;
    }
//</editor-fold>
    
    private static double totSdFH(double userAge) 
//<editor-fold defaultstate="collapsed" desc="Total Cholesterol FH Standard Deviation Value">
    {
        final int under20sSdFH = 58;
        final int in20sSdFH = 61;
        final int over20sSdFH = 84;
        
        double age = userAge;
        double meanVal;
        
        if (age < 20)
            meanVal = under20sSdFH;
        
        else if (age >= 20 && age < 30)
            meanVal = in20sSdFH;
        
        else
            meanVal = over20sSdFH;
        
        return meanVal;
    }
//</editor-fold>

    private static double totSdNotFH(double userAge) 
//<editor-fold defaultstate="collapsed" desc="Total Cholesterol Non-FH Standard Deviation Value">
    {
        final int under20sSdNotFH = 29;
        final int in20sSdNotFH = 36;
        final int over20sSdNotFH = 41;
        
        double age = userAge;
        double meanVal;
        
        if (age < 20)
            meanVal = under20sSdNotFH;
        
        else if (age >= 20 && age < 30)
            meanVal = in20sSdNotFH;
        
        else
            meanVal = over20sSdNotFH;
        
        return meanVal;
    }
//</editor-fold>
   
    private double nextNextGaussian;
    private boolean haveNextNextGaussian = false;    
}