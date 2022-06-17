using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Valid_Braces
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = "[(])";
            Console.WriteLine(validBraces(input));
            Console.Read();
        }

        public static bool validBraces(String braces)
        {
            char[] arr = braces.ToCharArray();
            List<char> clist = new List<char>();
            foreach (char s in arr)
            {
                if (!left_symbol.ContainsKey(s))
                {
                    if (clist.Count > 0 && clist.Contains(s) && clist.Last() == s)
                        clist.Remove(s);
                    else
                        return false;
                }                   
                else
                    clist.Add(left_symbol[s]);
            }
            return clist.Count == 0;
        }

        public static Dictionary<char, char> left_symbol = new Dictionary<char, char>() {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'}
        };
    }
}
