using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Categorize_New_Member
{
    class Program
    {
        static void Main(string[] args)
        {
            IEnumerable<string> res = OpenOrSenior(new[] { new[] { 45, 12 }, new[] { 55, 21 }, new[] { 19, 2 }, new[] { 104, 20 } });
            foreach (var s in res)
            {
                Console.Write(s);
            }           
            Console.Read();
        }

        public static IEnumerable<string> OpenOrSenior(int[][] data)
        {
            List<string> re_list = new List<string>();
            foreach (var player in data)
            {
                if (player[0] >= 55 && player[1] >= 7)
                    re_list.Add("Senior");
                else
                    re_list.Add("Open");
            }
            return re_list.AsEnumerable<string>();
        }
    }
}
