

Console.Clear();
Console.WriteLine("Input a nunber of multiplication table");
int n = Convert.ToInt32(Console.ReadLine());

Console.WriteLine();
Console.WriteLine();


for (int i = 1; i < n + 1; i++)
{

    for (int j = 1; j < n + 1; j++)
    {

        Console.Write(i * j);
        Console.Write("\t");

    }

    Console.WriteLine();


}
