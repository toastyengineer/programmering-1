// Syntax, runtime and semantic errors

using System;

public class Part3Errors
{
    const double PI_APPROXIMATION = 3.14159;

    public static int f(int x, int y)
    {
      // Returns 3x/2y
      return (3*x)/(2*y);
    }

    public static void g(double z = 1.0)
    {
        // Prints square root of z
        Console.WriteLine(Math.Pow(z, 1.0));
    }

    public static void Main()
    {
        Console.WriteLine(f(2, 5));
        Console.WriteLine(f(2, 0));
        g(4);
        g(PI_APPROXIMATION);
        Console.WriteLine("Skriv en siffra: ");
        string s = Console.ReadLine();
        int k = (int)s[0];
    }
}
