/**
 * Lists and exceptions
 */

using System;
using System.IO;
using System.Collections.Generic;

public class Part5
{
    /**
     * Prints a list
     */
    public static void PrintList(List<int> listIn, int start=0, int stop=0)
    {
        int count = listIn.Count;
        if (count > 0)
        {
            if (stop == 0)
                stop = count-1;
            start = Math.Abs(count+start) % count;
            stop = Math.Abs(count+stop) % count;
        }
        else
        {
            start = 0;
            stop = 0;
        }
        Console.Write("[");
        for (int i=start; i < stop; i++)
        {
            Console.Write(listIn[i]);
            if (i < (stop-1))
                Console.Write(", ");
        }
        Console.WriteLine("]");
    }
    
    /**
     * Does the lists part
     */
    public static void DoLists()
    {
        // En tom lista
        List<int> a = new List<int>();
        PrintList(a);
        
        // En lista med tre element
        List<int> b = new List<int>() {-1, 0, 1};
        PrintList(b);

        // Lägg till ett element
        b.Add(2);
        PrintList(b);
        
        // Ta bort ett element
        b.Remove(0);
        PrintList(b);
        
        // Skriv ut första elementet som en slice
        PrintList(b, 0, 1);
        
        // Skriv ut första och andra elementet som en slice
        PrintList(b, 0, 2);
        
        // Skriv ut sista elementet som en slice
        PrintList(b, -2, -1);
    }

    /**
     * Handles division by zero
     */
    private static int Div(int b, int c)
    {
        int a = 0;
        try
        {
            a = b/c;
        }
        catch (DivideByZeroException)
        {
            Console.WriteLine("Division med noll!");
        }
        return a;
    }

    /**
     * Opens and read a file
     */
    private static string ReadFile(string fileName)
    {
        string s = "";
        try
        {
            using (StreamReader f = new StreamReader(fileName))
            {
                s = f.ReadToEnd();
            }
        }
        catch (FileNotFoundException)
        {
            Console.Write("Hittar inte filen '{0}'!", fileName);
        }
        return s;
    }
    
    /**
     * Does the exceptions part
     */    
    public static void DoExceptions()
    {
        // Division med ett är OK
        Console.WriteLine("Div(1, 1) = {0}", Div(1, 1));
        
        // Division med noll hanteras
        Console.WriteLine("Div(1, 0) = {0}", Div(1, 0));
        
        // Filen finns inte
        Console.WriteLine(ReadFile("not_there.txt"));
    }

    /**
     * Main application
     */    
    public static void Main()
    {
        DoLists();
        DoExceptions();
    }
}
