using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Equal_Sides_Of_An_Array
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = { 1, 2, 3, 4, 3, 2, 1 };
            Console.Write(FindEvenIndex(arr));
            Console.Read();
        }

        public static int FindEvenIndex(int[] arr)
        {
            
            for(int i = 0; i < arr.Length; i++)
            {
                var l_arr = new ArraySegment<int>(arr, 0, i).Sum();
                var r_arr = new ArraySegment<int>(arr, i + 1, arr.Length - 1 - i).Sum();
                
                if (l_arr == r_arr)
                {
                    return i;
                }
            }
            return -1;
        }
    }
}
