using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Rot13
{
    class Program
    {
        static void Main(string[] args)
        {
            string input_string = "test";
            Console.WriteLine(Rot13(input_string));
            Console.Read();
        }

        public static string Rot13(string message)
        {
            int[] ascii_arr = message.Select(c => Convert.ToInt32(c)).ToArray();
            for(int i = 0; i < ascii_arr.Length; i++)
            {
                int check = ascii_arr[i];
                if (check >= 65 && check <= 90)
                    ascii_arr[i] = check >= 78 ? check - 13 : check + 13;
                else if (check >= 97 && check <= 122)
                    ascii_arr[i] = check >= 110 ? check - 13 : check + 13;
            }

            return String.Join("", ascii_arr.Select(c => Convert.ToChar(c)));
        }
    }
}
