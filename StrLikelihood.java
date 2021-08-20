package strlikelihood;
import java.util.Scanner;

//<editor-fold defaultstate="collapsed" desc="Notes">
/*
* String likelihood is the product of an individuals:
* 1) Founder Prior Probabilities (L57-T57)
* 2) LCL-C or Total-C Penetrance (U57-AC57)
* 3) Tendon Xanthoma Penetrance (AD57:AL57)
* 4) Penetrance for CAD (AM57:AU57)

* String Likelihood feeds into the numeric parts for diagnostic probability (AX-BF);
* Diagnostic Probability is the product of the founder or transmission prob and the String Likelihood.
* Product Sums represent the sum of an individuals possibilities (columns AV-BF) for Diagnostic probability. 
* FH Probability is the product sum for a given individual (AX-BF) divided by string likelihood product sum (AV570)

*/
//</editor-fold>


//<editor-fold defaultstate="collapsed" desc="TODO">
/* TODO:
* 1 - Create Logic for String Likelihood
* 2 - Create Logic for Diagnostic Probability
* 3 - Create Logic for Product Sum
* 4 - Create Logic for FH Probability
* 5 - Account for all 511 Permutations when final calculation is made
* 6 - Revisit and complete earlier coding modules.
*/
//</editor-fold>

public class StrLikelihood {

    public static void main(String[] args) 
    {
    //int age;
    double ldlOrTotalC, txp, clinicalcad, founderprob, stringVal, numDiagProb;
    
    String prompt = "Please enter ";
    String ldlOrTotalCPrompt = "LDL-C or Total-C:";
    String txpprompt ="Tanden Xanthoma:";
    String clinicalcadprompt = "Clinical Coronary Artery Disease Diagnosis:";
    String founderprobprompt = "Known Founder Probabilities:";
    
    // Creating Scanner Object for User Input
    Scanner input = new Scanner(System.in);
    
    // Assigning user input value to ldlOrTotalC variable.
    System.out.print(prompt + ldlOrTotalCPrompt);
    ldlOrTotalC = input.nextDouble();
    
    // Assigning user input value to Tanden Xanthoma variable.
    System.out.print(prompt + txpprompt);
    txp = input.nextDouble();
    
    // Assigning user input value to Clinical Coronary Artery Disease variable.
    System.out.print(prompt + clinicalcadprompt);
    clinicalcad = input.nextDouble();
    
    // Assigning user input value to founder probability variable.
    System.out.print(prompt + founderprobprompt);
    founderprob = input.nextDouble();    

    /* Passing all user defined/ instantiated variables through our stringLikelihood 
    // method, which will return the results of the product of all 4 variables. 
     The value of that calculation will then be assigned to the 'results' variable. */
    stringVal = stringLikelihood(ldlOrTotalC, txp, clinicalcad, founderprob);
     
    System.out.println("String Likelihood Value: " + stringVal);
    
    /* The value ot the stringLikelihood caclulation will then be passed through 
      as an agrument to the numeratorDiagnosticProbability method. */
    numDiagProb = numeratorDiagnosticProbability(stringVal); 
    
    System.out.println("Numerator Part for Diagnostic Probability: " + numDiagProb);
    }

//<editor-fold defaultstate="collapsed" desc="String Likelihood Method Description">
    /*
    stringLikelihood method receives 4 arguments, then calculates the value of
    stringlikelihood, which then gets returned into our Main class.
    */
//</editor-fold>
    
    private static double stringLikelihood(double cholesterol, double tendonXan, double corArtDisease, double transmisProb) 
    {
        double likelihood;
        likelihood = (cholesterol * tendonXan * corArtDisease * transmisProb);
        return likelihood;
    }
    
//<editor-fold defaultstate="collapsed" desc="Numerator Diagnostic Probability Method Description">
    /*
    numeratorDiagnosticProbability method with receives the stringLikelihood
    value as an argument, to then calculate the numerator value associated
    with a given individual. Value is then returned to the main method.
    */
//</editor-fold>
    
    private static double numeratorDiagnosticProbability(double prob)
    {
        double probability;
        final int FH = 1, NOTFH = 0;
        int genoTypeVal;
        
        Scanner input = new Scanner(System.in);
        
        System.out.print("Please enter 1 for known FH, or 0 for not known FH: ");
        genoTypeVal = input.nextInt();
        
        if (genoTypeVal == NOTFH)
        {
            probability = genoTypeVal * prob;
        }
        
        else 
        {
            genoTypeVal = FH;
            probability = genoTypeVal * prob;
        }
        
        return probability;

}
    
}
