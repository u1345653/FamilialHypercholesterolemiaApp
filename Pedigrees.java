package Pedigrees;

// DATE: 9.25.21
// PURPOSE: CREATE PEDIGREE CLASS IDENTIFYING EACH PEDIGREE OF 9-PEDIGREE FAMILY
// NEXT STEPS: READ IN THE BINARY TABLE AND CREATE CORRESPONDING LOGIC FOR THE FH VALUES

class Pedigrees 
{
    /* LETS FIRST IDENTIFY WHAT ALL FAMILY PEDIGREES HAVE IN OUR ALGORITHM.... 
    THESE ARE THE COLUMNS IN THE AGGREGATE FUNCTION SECTION
    NOTE - THIS DOESN'T YET ACCOUNT FOR COLUMNS AV, STRING LIKELIHOOD OR 
    FAMILY (AV & AW). ONLY THE THINGS THAT WE KNOW EACH FAMILY MEMBER 
    IN THE PEDIGREE TO HAVE. THOSE ITEMS REPRESENT THINGS THROUGHOUT 
    THE ENTIRE PEDIGREE TREE */
    
    private int PEDIGREEID; // VALUES 1-9, REPRESENTING THE MEMBERS OF PEDIGREE
    int GENOTYPE; // COLUMNS C - K
    double PROBABILITIES; // COLUMNS L - T
    double CHOLPENETRANCE; // COLUMNS U - AC
    double TXPENETRANCE; // COLUMNS AD - AL
    double CADPENETRANCE; // COLUMNS AM - AU
    double NUMDIAGPROB; // COLUMNS AX - BF
        
    public void setPedID(int id)
    {
        PEDIGREEID = id;
    }
    
    public int getPedID()
    {
        return PEDIGREEID;
    }
    
}

class TestPedigree{
    // TESTING OUR FAMILY PEDIGREES
    
    public static void main(String args[])
    {

    // CREATING ALL OF OUR PEDIGREE OBJECTS
    Pedigrees[] pedigree = new Pedigrees[10];
    
    // ASSIGNING CREATED PEDIGREE OBJECTS EACH AN ID, 1-9;
        for (int i = 1; i < pedigree.length; i++)
        {
            pedigree[i] = new Pedigrees();
            pedigree[i].setPedID(i);
        // System.out.println("Pedgree " + i + " | Pedigree ID: " + pedigree[i].getPedID());
        }
    
    }
    
}