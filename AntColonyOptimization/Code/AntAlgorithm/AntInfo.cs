using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AntAlgorithm
{
    public class AntInfo
    {
        public List<int> T { get; set; }            // cities sequence            
        public double L { get; set; }               // length of the path traveled  

        public AntInfo()
        {
            T = new List<int>();
            L = 0;
        }
        public AntInfo(List<int> t, double l)
        {
            T = t;
            L = l;
        }
    }
}

