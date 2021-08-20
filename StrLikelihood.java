package strlikelihood;
import java.util.Scanner;

/*
 * String likelihood is the product of an individuals: 
 * 1) Founder Prior Probabilities (L57-T57)
 * 2) LCL-C or Total-C Penetrance (U57-AC57)
 * 3) Tendon Xanthoma Penetrance (AD57:AL57)
 * 4) Penetrance for CAD (AM57:AU57)

 * String Likelihood feeds into the numeric parts for diagnostic probability (AX-BF)
 * String Likelihood needs to be a double value
*/
public class StrLikelihood {

    public static void main(String[] args) 
    {
    int age;
    double ldlOrTotalC, txp, clinicalcad, founderprob, results;
    
    String prompt = "Please enter ";
    String ldlOrTotalCPrompt = "LDL-C or Total-C:";
    String txpprompt ="Tanden Xanthoma:";
    String clinicalcadprompt = "Clinical Coronary Artery Disease Diagnosis:";
    String founderprobprompt = "Known Founder Probabilities:";
    
    Scanner input = new Scanner(System.in);
    
    System.out.print(prompt + ldlOrTotalCPrompt);
    ldlOrTotalC = input.nextDouble();
    
    System.out.print(prompt + txpprompt);
    txp = input.nextDouble();
    
    System.out.print(prompt + clinicalcadprompt);
    clinicalcad = input.nextDouble();
    
    System.out.print(prompt + founderprobprompt);
    founderprob = input.nextDouble();    

    results = stringLikelihood(ldlOrTotalC, txp, clinicalcad, founderprob);
    
    System.out.println("String Likelihood Value: " + results);
    
    }

    private static double stringLikelihood(double cholesterol, double tendonXan, double corArtDisease, double transmisProb) 
    {
        double likelihood;
        likelihood = (cholesterol * tendonXan * corArtDisease * transmisProb);
        return likelihood;
    }
    
}
