using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Binary_Addition
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write(AddBinary(5, 9));
            Console.Read();
        }

        public static string AddBinary(int a, int b)
        {
            return Convert.ToString(a + b, 2);
        }
    }
}
