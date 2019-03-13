using System;
namespace HelloWorld
{
  class Part2
  {
    public static void Main()
    {
      Console.WriteLine("Utskrift görs med console.writeline()");
      Console.Write("Mata in en sträng med Console.ReadLine()");

      string a = Console.ReadLine();
      Console.WriteLine("Variabeln a har värdet "+a+" och typen "+a.GetType());

      int b = 3;
      Console.WriteLine("Varabeln B har värdet "+b+" och typen "+b.GetType());

      float c = 3.0F;
      Console.WriteLine("Variabeln C har värdet "+c+" och typen "+c.GetType());

      string d = "Hej";
      Console.WriteLine("Variabeln D har värdet "+d+" och typen "+d.GetType());

      int[] e = {-1, 0, 1, 2};
      /*Console.WriteLine("Variabeln E har värdet ("+e[0]+","+e[1]+","+e[2]+","+e[3]+" och typen ")+e.GetType());
      a = "'" + a + "' är strängen du skrev in";*/
      Console.WriteLine("variabeln a har värdet "+a+" och typen "+a.GetType());

      b += 1;
      b -= 2;
      b *= 3;
      b /= 4;
      b %= 2;
      Console.WriteLine("Variabeln B har värdet "+b+" och typen "+b.GetType());

      c = c + 1.0f;
      c = c - 2.0f;
      c = c * 3.0f;
      c = c / 4.0f;
      Console.WriteLine("Variabeln C har värdet "+c+" och typen "+c.GetType());

      b = (int)c; // Statisk typning kräver typkonvertering
      Console.WriteLine("Variabeln B har nu värdet "+b+" och typen "+b.GetType());
      c = (int)b; // Statisk typning kräver typkonvertering
      Console.WriteLine("Variabeln C har nu värdet "+c+" och typen "+c.GetType());
    }
  }
}
