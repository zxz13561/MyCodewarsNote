using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace First_non_repeating_character
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = "sTreSs";
            Console.WriteLine(FirstNonRepeatingLetter(input));
            Console.Read();
        }

        public static string FirstNonRepeatingLetter(string s)
        {
            if (s.Length <= 1)
                return s;

            string s_lower = s.ToLower();
            string ret = s_lower.Select(x => x).Where(x => s_lower.Count(c => c.Equals(x)) == 1).FirstOrDefault().ToString();
            ret = ret != "\0" ? ret : "";
            if (ret == "")
                return ret;
            else
                return s.Contains(ret) ? ret : ret.ToUpper();
        }
    }
}
