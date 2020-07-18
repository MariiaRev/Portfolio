using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Windows.Forms;
using System.Drawing;
using System.Windows.Forms.DataVisualization.Charting;

namespace AntAlgorithm
{
    static class AntAlgo
    {
        public static List<List<int>> GetCitiesCoordinatesFromFile(Label l1)
        {
            String FileTitle = "CitiesCoordinates.txt";
            List<List<int>> CitiesCoordinates = new List<List<int>>();
            try
            {
                using (StreamReader sr = new StreamReader(FileTitle, System.Text.Encoding.Default))
                {
                    string line;
                    int x, y;
                    while ((line = sr.ReadLine()) != null)
                    {
                        x = Convert.ToInt32(line.Split(' ')[0]);
                        y = Convert.ToInt32(line.Split(' ')[1]);
                        CitiesCoordinates.Add(new List<int> { x, y });
                    }
                }
                l1.Text = "File with cities coordinates opened successfully."; 
            }
            catch (Exception)
            {
                l1.Text = "FILE OPEN ERROR";
                l1.Text += "\nCheck the file availability and correctness of the \nentered data.";
                CitiesCoordinates.Clear();
            }
            return CitiesCoordinates;
        }

        static List<List<double>> CountDistancesBetweenCities(List<List<int>> CitiesCoordinates, List<List<double>> CitiesVisibilities)   //function returns distances 
        {                                                                                                                                 //between cities with their visibilities
            List<List<double>> DistancesBetweenCities = new List<List<double>>();

            int count = CitiesCoordinates.Count();
            int X1, Y1, X2, Y2;
            double dist;

            for (int i = 0; i < count; i++)
            {
                DistancesBetweenCities.Add(new List<double>());
                CitiesVisibilities.Add(new List<double>());

                X1 = CitiesCoordinates[i][0];
                Y1 = CitiesCoordinates[i][1];
                for (int j = 0; j < count; j++)
                {
                    if (i == j)                                   //no distance in one city (i=j)
                    {
                        DistancesBetweenCities[i].Add(0);
                        CitiesVisibilities[i].Add(0);
                    }
                    else if (j > i)
                    {
                        X2 = CitiesCoordinates[j][0];
                        Y2 = CitiesCoordinates[j][1];
                        dist = Math.Round(Math.Sqrt(Convert.ToDouble((X1 - X2) * (X1 - X2) + (Y1 - Y2) * (Y1 - Y2))), 4);
                        DistancesBetweenCities[i].Add(dist);
                        CitiesVisibilities[i].Add(Math.Round(1 / dist, 4));
                    }
                    else
                    {
                        DistancesBetweenCities[i].Add(DistancesBetweenCities[j][i]);
                        CitiesVisibilities[i].Add(CitiesVisibilities[j][i]);
                    }
                }
            }
            return DistancesBetweenCities;
        }

        static void init(List<List<double>> list, int n)
        {
            for (int i = 0; i < n; i++)
            {
                list.Add(new List<double>());
                for (int j = 0; j < n; j++)
                {
                    list[i].Add(0);
                }
            }
        }
        static void initCities(List<int> list, int n)
        {
            for (int i = 0; i < n; i++)
            {
                list.Add(i);
            }
        }
   
        static double deltaTauFor1Ant(int Q, double len)            //delta tau for one ant
        {
            return Math.Round(Q / len, 4);
        }

        static double newTau(double p, double tau, double deltaTau)        //uses delta tau for all ants
        {
            return Math.Round((1 - p) * tau + deltaTau, 4);
        }

        static void Pr(List<List<double>> P, List<List<double>> tau, List<List<double>> nu,
            double alpha, double beta, int i, List<int> J)
        {
            double sum = 0;
            double a;

            for (int q = 0; q < J.Count(); q++)
            {
                sum += Math.Pow(tau[i][J[q]], alpha) * Math.Pow(nu[i][J[q]], beta);
            }

            for (int m = 0; m < P.Count(); m++)
            {
                if (J.Contains(m))
                {
                    a = Math.Round((Math.Pow(tau[i][m], alpha) * Math.Pow(nu[i][m], beta)) / sum, 4);
                    P[i][m] = a;
                    P[m][i] = a;
                }
                else
                {
                    P[i][m] = 0;
                    P[m][i] = 0;
                }
            }
        }

        static double L(List<List<double>> distances, List<int> visited)
        {
            double len = 0;
            for (int i = 0; i < visited.Count() - 1; i++)
            {
                len += distances[visited[i]][visited[i + 1]];
            }
            len += distances[visited[visited.Count() - 1]][visited[0]];
            return len;
        }

        static void viewResults(AntInfo solution, Label l1)
        {
            l1.Text = "          Path: ";
            for (int i = 0; i < solution.T.Count(); i++)
                l1.Text += solution.T[i] + " ";
            l1.Text += "\nPath length: " + solution.L;
        }

        public static AntInfo AlgoGo(double alpha, double beta, List<List<int>> CitiesCoordinates, Label SolutionOut)
        {
            int N;
            double tau0 = 1;
            int Q = 10;
            double p = 0.6;

            Random rand = new Random();
            double randNum;
            int chooseCityNum = 0;
            int Tmax = 10;

            List<List<double>> nu = new List<List<double>>();                  // visibilities of cities
            List<List<double>> D = CountDistancesBetweenCities(CitiesCoordinates, nu);    // distances between cities

            AntInfo Solution = new AntInfo(new List<int>(), 1000000);

            if (D.Any())
            {
                N = D.Count();
                List<List<double>> tau = new List<List<double>>();
                List<List<double>> deltaTau = new List<List<double>>();
                List<List<double>> P = new List<List<double>>();
                double maybeBest;
                int indexBest;

                init(tau, N);
                init(deltaTau, N);
                init(P, N);

                for (int i = 0; i < N; i++)
                    for (int j = 0; j < N; j++)
                    {
                        if (i != j)
                        {
                            tau[i][j] = tau0;
                        }
                        else
                            tau[i][j] = 0;

                    }
                for (int t = 0; t < Tmax; t++)
                {
                    List<AntInfo> AllAntsInfo = new List<AntInfo>();

                    for (int k = 0; k < N; k++)                                            // for every ant
                    {
                        List<int> visited = new List<int>();
                        List<int> forVisit = new List<int>();
                        initCities(forVisit, N);

                        visited.Add(k);
                        forVisit.Remove(k);

                        for (int town = 0; town < N - 1; town++)
                        {
                            Pr(P, tau, nu, alpha, beta, visited[visited.Count() - 1], forVisit);

                            randNum = rand.NextDouble();

                            double sum = P[visited[visited.Count() - 1]][0];
                            for (int q = 0; q < N; q++)
                            {
                                if (q + 1 < N && randNum > sum)
                                {
                                    sum += P[visited[visited.Count() - 1]][q + 1];
                                }
                                else
                                {
                                    chooseCityNum = q;
                                    break;
                                }
                            }

                            visited.Add(chooseCityNum);
                            forVisit.Remove(chooseCityNum);
                        }
                        AllAntsInfo.Add(new AntInfo(visited, L(D, visited)));

                        for (int i = 0; i < N; i++)
                            deltaTau[k][i] = deltaTauFor1Ant(Q, AllAntsInfo[k].L);
                    }
                    maybeBest = AllAntsInfo.Min(x => x.L);
                    if (maybeBest < Solution.L)
                    {
                        indexBest = AllAntsInfo.FindIndex(x => x.L == maybeBest);
                        Solution.L = maybeBest;
                        Solution.T = AllAntsInfo[indexBest].T;
                    }

                    for (int k = 0; k < N; k++)
                        for (int j = 0; j < N; j++)
                            tau[k][j] = newTau(p, tau[k][j], deltaTau[k][j]);

                }
                Solution.T.Add(Solution.T[0]);
                viewResults(Solution, SolutionOut);
            }
            return Solution;
        }

        public static void BuildGraphic(Chart chart1, List<List<int>> coordinates, List<int> sequence)
        {

            chart1.Series.Clear();
            ChartArea CA = chart1.ChartAreas[0];
            Series SP = chart1.Series.Add("SPoint");
            SP.ChartType = SeriesChartType.Point;
            SP.BorderWidth = 5;

            Series SL = chart1.Series.Add("SLine");
            SL.ChartType = SeriesChartType.Line;
            SL.Color = Color.DarkOrange;
            SL.BorderWidth = 2;

            Axis ax = new Axis();
            ax.Title = "X";
            chart1.ChartAreas[0].AxisX = ax;
            Axis ay = new Axis();
            ay.Title = "Y";
            chart1.ChartAreas[0].AxisY = ay;
            ay.Interval = 10;

            for (int i=0; i<coordinates.Count()-1; i++)
            {
                int p0 = SL.Points.AddXY(coordinates[i][0], coordinates[i][1]);
                int p1 = SL.Points.AddXY(coordinates[i+1][0], coordinates[i+1][1]);
                SL.Points[p0].Color = Color.Red;
                SL.Points[p1].Color = Color.Red;
            }

            for (int i = 0; i < coordinates.Count() - 1; i++)
            {
                SP.Points.AddXY(coordinates[i][0], coordinates[i][1]);
                SP.Points[i].Label = Convert.ToString(sequence[i]);

                SP.Points[i].MarkerStyle = MarkerStyle.Circle;
                SP.Points[i].Font = new System.Drawing.Font("Maiandra GD", 14f);
                SP.Points[i].Color = Color.Green;
                SP.Points[i].MarkerSize = 10;
            }
        }

        public static List<List<int>> CitiesCoordinatesSequence(List<List<int>> coordinates, AntInfo solution)
        {
            List<List<int>> coordsSequence = new List<List<int>>();

            for (int i = 0; i < coordinates.Count()+1; i++)
                coordsSequence.Add(coordinates[solution.T[i]]);

            return coordsSequence;
        }
    }
}
