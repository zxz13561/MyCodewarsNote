using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Last_digit_of_a_large_number
{
    class Program
    {
        static void Main(string[] args)
        {
            int n1 = 0946723;
            int n2 = 52651;
            Console.WriteLine(GetLastDigit(n1, n2));
            Console.Read();
        }

        public static int GetLastDigit(int n1, int n2)
        {
            if (n2 == 0)
                return 1;

            int n1_last = int.Parse(n1.ToString().Last().ToString());
            int start_i = n2 > 9 ? 2 : 1;
            int n2_last = int.Parse(n2.ToString().Substring(n2.ToString().Length - start_i));
            switch (n1_last)
            {
                case int n when (n == 2 || n == 8):
                    int[] odd_arr = n == 2 ? new int[]{ 6, 2, 4, 8 } : new int[] { 6, 8, 4, 2 };
                    return odd_arr[n2_last % 4];

                case int n when (n == 3 || n == 7):
                    int[] even_arr = n == 3 ? new int[] { 1, 3, 9, 7 } : new int[] { 1, 7, 9, 3 };
                    return even_arr[n2_last % 4];

                case 4:
                    return n2_last % 2 == 0 ? 4 : 6;

                case 9:
                    return (n2_last % 2) * 9;

                default:
                    return n1_last;
            }
        }
    }
}
