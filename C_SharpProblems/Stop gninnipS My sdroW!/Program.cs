using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Stop_gninnipS_My_sdroW_
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = "Hey wollef sroirraw";
            Console.WriteLine(SpinWords(input));
            Console.Read();
        }

        public static string SpinWords(string sentence)
        {         
            return string.Join(" ", sentence.Split(' ').Select(w => w.Length >= 5 ? string.Join("", w.Reverse()) : w));
        }
    }
}
