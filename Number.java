package binary;

// Algorithm is the Negative Base Calculation. Basically, we just pick 

import java.io.*;
import java.util.*;

public class Number {

    private int base;
    private String value = "512";
    private Map<Character, Integer>
            hexatoDec;
    private Map<Integer, Character>
            dectoHex;
    
    public Number (String value, int base)
    {
        this.value = value;
        this.base = base;
        hexatoDec = new HashMap<>();
        dectoHex = new HashMap<>();
        
        for (int i = 0; i < 6; i++)
        {
            dectoHex.put(10 + i, (char)('A' + i));
            hexatoDec.put((char)('A' + i), 10 + i);
        }
    }
    
    public Number (String value)
    {
        this.base = 10;
        this.value = value;
    }
    
    public String toDecimal()
    {
        int sum = 0;
        int pow = 0;
        
        String tempVal = this.value;
        
        for (int i = tempVal.length() - 1; i >= 0; i--) {
            int val = tempVal.charAt(i) - '0';
            if (this.base == 16
                    && hexatoDec.containsKey(
                    tempVal.charAt(i))) {
                    val = hexatoDec.get(tempVal.charAt(i));
            }
        sum += (val) *  (Math.pow(this.base, pow++));
        }
        
        return String.valueOf(sum);
    }
    
    public String toBase(int targetBase)
    {
        String val = this.value;
        
        if (this.base != 10)
            val = toDecimal();
        int temp = Integer.parseInt(val);
        StringBuilder str = new StringBuilder();
        
        while (temp != 0) {
            int tempValue = temp % targetBase;
            if (targetBase == 16
                    && dectoHex.containsKey(tempValue)) {
                str.insert(0, dectoHex.get(tempValue));
            }
            else {
                str.insert(0, tempValue);
            }
            temp /= targetBase;
        }
        return str.toString();
    }
    

   
    public static void main(String[] args) 
    {
    
        Number n1 = new Number("511", 10);
        System.out.println("Decimal : " + n1.toDecimal());
//        System.out.println("Octal : " + n1.toBase(8));
        System.out.println("Binary : " + n1.toBase(2));
    
    }

}