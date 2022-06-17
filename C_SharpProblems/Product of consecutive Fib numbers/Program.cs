using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Product_of_consecutive_Fib_numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            ulong[] r = new ulong[] { 55, 89, 1 };
            ulong[] f_r = productFib(4895);
            Console.WriteLine(r == f_r);
            Console.Read();
        }

        public static ulong[] productFib(ulong prod)
        {
            switch (prod)
            {
                case 0:
                    return new ulong[] { 0, 1, 1 };
                case 1:
                    return new ulong[] { 1, 1, 1 };
                case 2:
                    return new ulong[] { 1, 2, 1 };
                default:
                    break;
            }

            ulong fib1 = 2;
            ulong fib2 = 3;
            ulong temp = 0;
            ulong mult = 0;

            while (prod > mult)
            {
                mult = fib1 * fib2;
                if (prod == mult)
                    return new ulong[] { fib1, fib2, 1 };
                else if (prod < mult)
                    return new ulong[] { fib1, fib2, 0 };

                temp = fib1;
                fib1 = fib2;
                fib2 = temp + fib1;
            }
            return new ulong[] { 0, 0, 0 };
        }
    }
}
