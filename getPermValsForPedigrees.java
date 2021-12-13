package BinaryDigits;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// DATE - 9.26.21 - 
// PURPOSE: PERMUTATION 'IN-BETWEEN-CLASS' ALLOCATING THE BINARY & PERMUTATION VALUES TO BE TRANSPOSED INTO THE PEDIGREES CLASS.... NEEDS TO BE REVISETED

public class getPermValsForPedigrees {
    
    public static List getPermValsForPedigrees() {
        
    List <String> intakePermutationData = new ArrayList <> ();

        for (int x = 0; x < intakePermutationData.size(); ++x)
        {
        intakePermutationData.set(x, PermValsForPedigrees.sendToPedigrees.get(x));
        System.out.println(intakePermutationData);
        }
        return intakePermutationData;
    }
    
    public static void main(String args[])
    {    
        List <Object> getPermVals = getPermValsForPedigrees();
                
        for (int i = 0; i < getPermVals.size(); ++i)
        {
         getPermVals = (List<Object>) getPermValsForPedigrees.getPermValsForPedigrees().get(i);
        }
        
        System.out.println( Arrays.asList( getPermVals ) );
        
    }
}