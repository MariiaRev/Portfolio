using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AntAlgorithm
{
    public partial class Form1 : Form
    {
        List<List<int>> CitiesCoordinates;
        List<List<int>> coordsSequence;

        public Form1()
        {
            InitializeComponent();
            CitiesCoordinates = AntAlgo.GetCitiesCoordinatesFromFile(FileOpenStatus);
            AntInfo solution;
            if (CitiesCoordinates.Any())
            {
                double a = 1, b = 5;
                textBox1.Text = Convert.ToString(a);
                textBox2.Text = Convert.ToString(b);
                solution = AntAlgo.AlgoGo(a, b, CitiesCoordinates, Solution);
                label2.Text = "SOLUTION";

                coordsSequence = AntAlgo.CitiesCoordinatesSequence(CitiesCoordinates, solution);
                AntAlgo.BuildGraphic(chart1, coordsSequence, solution.T);
            }

            //show recommended parameters alpha beta
            label7.Text = "alpha:\n";
            label7.Text += "  beta:";
            label8.Text = "0,5\n 5";
            label9.Text = "1\n1";
            label10.Text = "1\n2";
            label11.Text = "1\n5";


        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                double a = Convert.ToDouble(textBox1.Text);
                double b = Convert.ToDouble(textBox2.Text);
                AntInfo solution;

                if (CitiesCoordinates.Any())
                {
                    solution = AntAlgo.AlgoGo(a, b, CitiesCoordinates, Solution);
                    label2.Text = "SOLUTION";

                    coordsSequence = AntAlgo.CitiesCoordinatesSequence(CitiesCoordinates, solution);
                    AntAlgo.BuildGraphic(chart1, coordsSequence, solution.T);
                }
            }
            catch(Exception){ }
        }
    }
}
