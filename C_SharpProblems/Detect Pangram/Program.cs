using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Detect_Pangram
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = "The quick brown fox jumps ver the lazy dg";
            Console.WriteLine(IsPangram(input));
            Console.Read();
        }

        public static bool IsPangram(string str)
        {
            List<char> alphabet = new List<char>() {
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            };

            str = str.ToLower();
            foreach (char c in str.ToCharArray())
            {
                if (alphabet.Contains(c))
                    alphabet.Remove(c);
            }

            return alphabet.Count == 0;
        }
    }
}
