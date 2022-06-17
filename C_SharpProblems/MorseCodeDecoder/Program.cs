using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MorseCodeDecoder
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = ".";
            Console.WriteLine(Decode(input));

            Console.Read();
        }

        public static string Decode(string morseCode)
        {
            string[] subs = morseCode.Split(' ');
            string res = "";
            int count_space = 0;
            foreach (string s in subs)
            {
                if (s == "" && count_space < 1)
                {
                    count_space++;
                }
                else if(s == "" && count_space == 1)
                {
                    res += " ";
                    count_space = 0;
                }
                else
                {
                    res += code_dic[s];
                    count_space = 0;
                }                               
            }
            res.TrimStart(' ');
            res.TrimEnd(' ');
            return res;
        }

        public static Dictionary<string, string> code_dic = new Dictionary<string, string>()
        {
            {".-", "A" },
            {"-...","B"},
            {"-.-.","C"},
            {"-.." ,"D"},
            {"."   ,"E"},
            {"..-.","F"},
            {"--." ,"G"},
            {"....","H"},
            {".."  ,"I"},
            {".---","J"},
            {"-.-" ,"K"},
            {".-..","L"},
            {"--"  ,"M"},
            {"-."  ,"N"},
            {"---" ,"O"},
            {".--.","P"},
            {"--.-","Q"},
            {".-." ,"R"},
            {"..." ,"S"},
            {"-"   ,"T"},
            {"..-","U"},
            {"...-","V"},
            {".--","W"},
            {"-..-","X"},
            {"-.--","Y"},
            {"--..","Z"},
            {"...---...", "SOS"}
        };
    }
}
