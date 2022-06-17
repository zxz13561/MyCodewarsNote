using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Find_the_missing_letter
{
    class Program
    {
        static void Main(string[] args)
        {
            char[] input = { 'O', 'Q', 'R', 'S' };
            Console.WriteLine(FindMissingLetter(input));
            Console.Read();
        }

        public static char FindMissingLetter(char[] array)
        {
            string all_alphabet = Char.IsUpper(array[0]) ? "ABCDEFGHIJKLMNOPQRSTUVWXYZ":"abcdefghijklmnopqrstuvwxyz";
            int start = all_alphabet.IndexOf(array[0]);
            int end = all_alphabet.IndexOf(array.Last());

            var correct_arr = all_alphabet
                .Skip(start)
                .Take(end - start + 1)
                .Select(c => c)
                .ToArray();

            return correct_arr.Select(c => c).Where(c => !array.Contains(c)).FirstOrDefault();
        }
    }
}
