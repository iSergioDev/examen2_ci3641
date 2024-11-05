using System;

public class Program
{
    public static void Main()
    {
        Console.WriteLine("Ingrese un número entero:");
        int n;
        if (int.TryParse(Console.ReadLine(), out n) && n > 0)
        {
            int resultado = Count(n);
            Console.WriteLine($"count({n}) = {resultado}");
        }
        else
        {
            Console.WriteLine("Por favor, ingrese un número entero positivo.");
        }
    }

    public static int Count(int n)
    {
        int count = 0;
        while (n != 1)
        {
            if (n % 2 == 0)
                n /= 2;
            else
                n = 3 * n + 1;
            count++;
        }
        return count;
    }
}
