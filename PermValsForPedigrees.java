package BinaryDigits;

import java.lang.Integer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// DATE - 9.26.21 
// PURPOSE - CREATION OF PERMUTATION VALUES MAPPING TO BINARY TABLE
//         - MAP BINARY TABLE TO PEDIGREES CLASS TO BEGIN ADDING THINGS TO THE PEDIGREE FAMILY MEMBER OBJECT/CLASSES
class Binary_Digits {
    // METHOD HOLDING OUR COLUMN NAMES
    private static String[] getColumnNames() 
    {
        String[] permFuncColNames = {"Permutation",
        "Binary Table", "FPP1", "FFP2", "FFP3",
        "TP4", "TP5", "TP6", "TP7", "TP8", "TP9", 
        "LDLC1", "LDLC2", "LDLC3", "LDLC4", "LDLC5", "LDLC6", "LDLC7", "LDLC8", "LDLC9", 
        "TX1", "TX2", "TX3", "TX4", "TX5", "TX6", "TX7", "TX8", "TX9", 
        "CAD1", "CAD2", "CAD3", "CAD4", "CAD5", "CAD6", "CAD7", "CAD8", "CAD9"};
        
//        for (int i = 0; i < permFuncColNames.length; i++)
//        {
//            System.out.print(permFuncColNames[i] + "  |  ");
//        }
        
        return permFuncColNames; 
    }
    
    // METHOD THAT WE GRAB OUR PERMUTATION VALUES FROM
    private static String[] getPermutation(int N)
    {
        String perm[] = new String[N];

        for (int i = 0; i < perm.length; i++ )
        {
        perm[i] = String.format(Integer.toString(i));           
        }
        
        return perm;
    
    }
    
    private static String[] toBinary(int N)
    {
        String[] bin = new String[N];
        
        for (int i = 0; i < bin.length; i++)
        {
            bin[i] = String.format(Integer.toBinaryString(i));
            bin[i] = String.format("%9s", bin[i]).replace(' ', '0');
//            System.out.println(bin[i]);
        }
        
        return bin;
    }
    
    public static void main(String[] args)
    {
        
    // FIRST ROW - FUNCTION HEADERS
        // CALLING METHOD HOLDING COLUMN HEADERS & ASSINGING CONTENTS TO STRING ARRAY
        String[] colNames = getColumnNames();                        
        
    // FIRST COLUMN - PERMUTATION VALUES
        // CALLING METHOD HOLDING PERMUTATION COLUMN VALUES & ASSIGNING CONTENTS TO STRING ARRAY
        String[] permutation = getPermutation(512);
        
    // SECOND COLUMN - BINARY TABLE VALUES
        // CALLING METHOD HOLDING BINARY VALUES & ASSIGNING CONTENTS TO STRING ARRAY
        String[] binary = toBinary(512);

    // PASSING THE STRING ARRAYS TO A 'HOLDING' METHOD, WHICH WE'LL ACCESS 
    // FROM OUR PEDIGREES.JAVA CLASS
        
        // DECLARING ARRAYLIST OBJECT, WHICH WE'LL USE TO ADD OUR STRING ARRAYS TO
        List <String> sendToSetter = new ArrayList <>();
        
        // ADDING STRING ARAYS TO ARRAYLIST
        sendToSetter.add( Arrays.toString( colNames ) );
        sendToSetter.add( Arrays.toString( permutation ) );
        sendToSetter.add( Arrays.toString( binary ) );
        
        // METHOD TO SEND OUR CREATED LIST TO A PLACE THAT'S GRABBABLE FOR OTHER PACKAGES TO GRAB
        PermValsForPedigrees.class.cast(sendToSetter);
    }
}

// CLASS RECEIVING THE LIST CONSISTING OF THE STRING ARRAYS
public class PermValsForPedigrees {

    public static List <String>  sendToPedigrees = new ArrayList <> ();
    
    public class getPermValsForPedigrees {
    
    public void setPermValsForPedigrees(List listexample)
    {        
    sendToPedigrees = listexample;
    }
        
    public List getPermValsForPedigrees()
    {
    return sendToPedigrees;
    }

    }
}