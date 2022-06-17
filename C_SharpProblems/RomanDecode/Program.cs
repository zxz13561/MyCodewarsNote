using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RomanDecode
{
    class Program
    {
        static void Main(string[] args)
        {
            string code = "MDCLXVI";
            Console.WriteLine(Solution(code));
            Console.Read();
        }

        public static int Solution(string roman)
        {
            char[] codes = roman.ToCharArray();
            int result = 0;
            string check_speical = "";
            foreach (char code in codes)
            {
                check_speical += code;
                result += RomanCode[code];

                if (check_speical.Length == 2)
                {
                    if (SpecialCode.ContainsKey(check_speical))
                    {
                        result -= SpecialCode[check_speical];
                        check_speical = "";
                    }
                    else
                    {
                        check_speical = check_speical.Remove(0, 1);
                    }
                }
            }
            return result;
        }

        static Dictionary<char, int> RomanCode = new Dictionary<char, int>()
        {
            { 'I', 1 },
            { 'V', 5 },
            { 'X', 10 },
            { 'L', 50 },
            { 'C', 100 },
            { 'D', 500 },
            { 'M', 1000 }
        };

        static Dictionary<string, int> SpecialCode = new Dictionary<string, int>()
        {
            { "IV", 2 },
            { "IX", 2 },
            { "XL", 20 },
            { "XC", 20 },
            { "CD", 200 },
            { "CM", 200 }
        };
    }
}
