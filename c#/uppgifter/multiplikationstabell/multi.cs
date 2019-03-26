using System;

public class Multi
{
  public static void Error()
  {
    Console.WriteLine("Invalid option");
    System.Environment.Exit(1);
  }

  public static int Ask(string s)
  {
    Console.WriteLine(s);
    int x = Convert.ToInt32(Console.ReadLine());
    if (x < 1 || x > 99)
    {
      Error();
    }
    return x;
  }

  public static void Main()
  {
    int m = Ask("Enter m (must be positive whole number): ");
    int n = Ask("Enter n (whole number greater than m): ");
    if (m > n)
    {
      Error();
    }
    if (n - m > 4)
    {
      n = m + 4;
    }
    for (;m < n+1; m++)
    {
      for (int i = 1; i < 11; i++)
      // Looping through m to n and 1 to 10
      {
        if (i < 10)
        // Upcoming conditionals are required for correct formatting in output.
        {
          if (m*i < 10)
          {
            Console.Write("  "+(m * i)+",");
          }
          else if (m*i < 100)
          {
            Console.Write(" "+(m * i)+",");
          }
          else
          {
            Console.Write((m * i)+",");
          }
        }
        else
        {
          if ((m * i) % 10 == 0 & m < 10)
          // If the product's remainder is 0 when divided by 10 and m is less than 10:
          // Write a space before the number for accurate display.
          {
            Console.Write(" "+(m * i)+"");
            Console.WriteLine();
          }
          else
          // Otherwise, no space before the number.
          {
            Console.Write((m * i)+"");
            Console.WriteLine();
          }
        }
      }
    }
  }
}
