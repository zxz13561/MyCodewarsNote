using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PaginationHelper
{
    class Program
    {
        static void Main(string[] args)
        {
        }
    }

    public class PagnationHelper<T>
    {
        private static int itemPP = 0;
        private static int total_page = 0;
        private static int total_items = 0;
        private static int count_remain = 0;
        private static bool haveRemain = false;

        /// <summary>
        /// Constructor, takes in a list of items and the number of items that fit within a single page
        /// </summary>
        /// <param name="collection">A list of items</param>
        /// <param name="itemsPerPage">The number of items that fit within a single page</param>
        public PagnationHelper(IList<T> collection, int itemsPerPage)
        {
            total_items = collection.Count;
            itemPP = itemsPerPage;

            int page_count = total_items / itemPP;
            int remain = total_items % itemPP;

            total_page = remain == 0 ? page_count : page_count + 1;
            haveRemain = remain != 0;

            if (haveRemain)
                count_remain = total_items - itemPP * (total_page - 1);
        }

        /// <summary>
        /// The number of items within the collection
        /// </summary>
        public int ItemCount
        {
            get
            {
                return total_items;
            }
        }

        /// <summary>
        /// The number of pages
        /// </summary>
        public int PageCount
        {
            get
            {
                return total_page;
            }
        }

        /// <summary>
        /// Returns the number of items in the page at the given page index 
        /// </summary>
        /// <param name="pageIndex">The zero-based page index to get the number of items for</param>
        /// <returns>The number of items on the specified page or -1 for pageIndex values that are out of range</returns>
        public int PageItemCount(int pageIndex)
        {
            if (pageIndex > total_page - 1 || pageIndex < 0)
                return -1;

            return total_page - 1 == pageIndex && haveRemain ? count_remain : itemPP;
        }

        /// <summary>
        /// Returns the page index of the page containing the item at the given item index.
        /// </summary>
        /// <param name="itemIndex">The zero-based index of the item to get the pageIndex for</param>
        /// <returns>The zero-based page index of the page containing the item at the given item index or -1 if the item index is out of range</returns>
        public int PageIndex(int itemIndex)
        {
            if (itemIndex > total_items - 1 || itemIndex < 0)
                return -1;

            int t_page = itemIndex / itemPP;
            return itemIndex % itemPP == 0 ? t_page : t_page + 1;
        }
    }
}
