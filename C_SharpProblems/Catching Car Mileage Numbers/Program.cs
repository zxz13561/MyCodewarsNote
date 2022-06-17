using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Catching_Car_Mileage_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int input_num = 32101;
            List<int> input_list = new List<int>() { 1337, 256 };

            Console.WriteLine(IsInteresting(input_num, input_list));
            Console.Read();
        }

        public static int IsInteresting(int number, List<int> awesomePhrases)
        {
            if (number < 100) 
                return number >= 98 ? 1 : 0;
           
            bool isFirst = true;
            int end = number + 2;
            while (number <= end)
            {
                int[] num_arr = number.ToString().Select(c => Convert.ToInt32(c) - 48).ToArray();
                bool isZeros = num_arr.Count(c => c == 0) == num_arr.Length - 1;
                bool allSame = num_arr.Count(c => c == num_arr[0]) == num_arr.Length;
                bool inList = awesomePhrases.Contains(number);

                string head = String.Join("", num_arr.Take(num_arr.Length / 2).Select(n => n.ToString()));
                string tail = String.Join("", num_arr.Reverse().Take(num_arr.Length / 2).Select(n => n.ToString()));
                bool isPail = head == tail;
                bool isSeqInc = num_arr[1] - num_arr[0] == 1;
                bool isSeqDec = num_arr[1] - num_arr[0] == -1;

                int pre_n = num_arr[1];
                foreach(int n in num_arr.Skip(2))
                {
                    if (isSeqInc && n != 0)
                        isSeqInc = n - pre_n == 1;
                    else if (isSeqInc && n == 0)
                        isSeqInc = pre_n == 9;
                    else if (isSeqDec)
                        isSeqDec = n - pre_n == -1;
                    else
                        break;

                    pre_n = n;
                }

                if ((isSeqInc || isSeqDec) && num_arr.Contains(0) && Array.IndexOf(num_arr, 0) != num_arr.Length - 1)
                {
                    isSeqInc = false;
                    isSeqDec = false;
                }                   

                if (isZeros || allSame || inList || isSeqInc || isSeqDec || isPail)
                    return isFirst ? 2 : 1;
                else
                    isFirst = false;

                number++;
            }

            return 0;
        }
    }
}
