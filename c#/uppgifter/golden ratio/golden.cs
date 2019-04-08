using System;
using System.IO;
using System.Collections.Generic;

public class Golden
{
  public const int MAX = 100;
  public const decimal GOLDENRATIO = 1.61803398874989484820458683436563811m;

  public static decimal Fibonacci(int n)
  {
    decimal a = 0;
    decimal b = 1;
    for (int i = 0; i < n; i++)
    {
      decimal temp = a;
      a = b;
      b = temp + b;
    }
    return a;
  }
  public static void Main()
  {
    List<decimal> a = new List<decimal>();
    for (int i = 0; i < MAX; i++)
    {
      a.Add(Fibonacci(i));
    }
    for (int i = 0; i < MAX; i++)
    {
      if (i-1 > 0)
      {
        decimal ratio = a[i] / a[i-1];
        if (ratio == GOLDENRATIO)
        {
          Console.WriteLine("\nMatch at index: "+i+" ["+a[i-1]+", "+a[i]+"]");
          Console.WriteLine("Value of Golden Ratio estimated to be: "+ratio+"\n");
          Environment.Exit(0);
        }
      }
    }
  }
}
