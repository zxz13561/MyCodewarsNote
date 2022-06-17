using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simple_Pig_Latin
{
    class Program
    {
        static void Main(string[] args)
        {
            string input_s = "Hello world !";
            Console.WriteLine(PigIt(input_s));
            Console.Read();
        }

        public static string PigIt(string str)
        {
            return String.Join(" ", str.Split(' ').Select(s => s.Length > 1 ? s.Substring(1) + s[0] + "ay" : s));
        }
    }
}
