package penetrance;

import java.util.*;


public class PenetetranceWithOutLDLTOTC {
  
    public static List<Object> getInput()
    {
    Scanner input = new Scanner(System.in);
    
    String agePrompt = "Please enter your Age in years: ";
    System.out.println(agePrompt);
    double userAge = input.nextDouble();     
    
    String LDLPrompt = "Please enter your most recent LDL-C level: ";
    System.out.println(LDLPrompt);
    double userLDL = input.nextDouble();
    
    String TOTCPrompt = "Please enter your most recent Total Cholesterol level: ";
    System.out.println(TOTCPrompt);
    double userTOTC = input.nextDouble();
    
    String clinicalCadPrompt = "Has anyone you've known been diagnosed with Coronary Artery Disease? ";
    System.out.println(clinicalCadPrompt);
    double userClincalCad = input.nextDouble();
    
    String genderPrompt = "Indicate your identified gender (0 - Male; 1 - Female):   ";
    System.out.println(genderPrompt);
    double userGender = input.nextDouble();
        
    String cadOnsetPrompt = "At what age were you diagnosed with Cornary Artery Disease? ";
    System.out.println(cadOnsetPrompt);
    double userCadOnset = input.nextDouble();
    
    String txPrompt = "Tendon Xanthoma Value (9 = Unknown, 1 = Definite Yes, 0 = Definite No):   ";
    System.out.println(txPrompt);
    double userTX = input.nextDouble();
     
    return Arrays.asList(userAge, userLDL, userTOTC, userClincalCad, userGender, userCadOnset, userTX);
    }
    
    public static List<Object> getPenMethods(List userInput)
    {
    double age, ldl, totc, clinicalCad, gender, cadOnset, tx;
    
    age = (double) userInput.get(0);
    ldl = (double) userInput.get(1);
    totc = (double) userInput.get(2);
    clinicalCad = (double) userInput.get(3);
    gender = (double) userInput.get(4);
    cadOnset = (double) userInput.get(5);
    tx = (double) userInput.get(6);  
    
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
    
    public static List<Object> getCholPenVals(List penMethods)
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
    
    public static void main(String[] args) 
    {
    List <Object> userInput = getInput();
    System.out.println("User Input Values: " + userInput);
    
    List <Object> penMethods = getPenMethods(userInput); 
    System.out.println("Penetrance Methods: " + penMethods);
    
    List <Object> cholPenVals = getCholPenVals(penMethods);
    System.out.println("Cholesterol Penetrance Values: " + cholPenVals);

//    // Printing all of our Penetrance Vals
////        System.out.print("LDL FH Penetrance Val: " + ldlPenVal);
////        System.out.print("LDL Not FH Penetrance Val: " + ldlNotPenVal);
//    System.out.println("Tendon Xanthoma FH Penetrance Val:  " + txPenFHVal);
//    System.out.println("Tendon Xanthoma Not FH Penetrance Val:  " + txPenNotFHVal);
//    System.out.println("CAD FH Penetrance Val:  " + cadPenFHVal);
//    System.out.println("CAD Not FH Penetrance Val:  " + cadPenNotFHVal);
    }

    // Method to generate the probability that Tendon Xanthoma contributes to FH.
    public static double txIsFH(double userLDL, double userAge, double userTX) 
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
        
    // Method to generate the probability that Tendon Xanthoma doesn't contribute to FH.
    public static double txNotFH(double userLDL, double userAge, double userTX) 
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

    // Method to generate the probability that CAD contributes to FH.
    public static double cadIsFH(double userClincalCad, double userGender, double userCadOnset, double userAge) 
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

    // Method to generate the probability that CAD does not contribute to FH.
    public static double cadIsNotFH(double userClincalCad, double userGender, double userCadOnset, double userAge) 
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
        
    private static double ldlFHMean(double userAge) 
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
    private static double ldlNotFHMean(double userAge) 
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

    private static double ldlSdFH(double userAge) 
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

    private static double ldlSdNotFH(double userAge) 
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

    private static double totMeanFH(double userAge) 
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

    private static double totMeanNotFH(double userAge) 
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
    
    private static double totSdFH(double userAge) 
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

    private static double totSdNotFH(double userAge) 
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
    
    
    private double nextNextGaussian;
    private boolean haveNextNextGaussian = false;
    
        } 