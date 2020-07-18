using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace Queries_Linq
{
    class functions
    {
        public static void GetCarsByMake(IEnumerable<XElement> cars)
        {
            Console.Write("Введiть марку авто: ");
            string carMake = Convert.ToString(Console.ReadLine());
            var queryRes = from c in cars
                           where (string)c.Element("make") == carMake
                           select new
                           {
                               id = (string)c.Element("carId"),
                               model = (string)c.Element("model"),
                               issueYear = (int)c.Element("issueYear"),
                               price = (int)c.Element("price"),
                               fuelCons = (int)c.Element("fuelConsumption")
                           };
            if (queryRes.Count() == 0)
            {
                Console.WriteLine("\nНемає автомобiлей обраної марки.");
            }
            else
            {
                Console.WriteLine();
                Console.WriteLine("                       Автомобiлi марки " + carMake);
                Console.WriteLine();
                var count = 0;
                Console.WriteLine("{6,-3}{0,-3}{1,-5}{2,-25}{3,-10}{4,7}{5,20}",
                    "№", "id", "model", "issue year", "price", "fuel consumption", " ");
                Console.WriteLine("  ------------------------------------------------------------------------");
                foreach (var car in queryRes)
                {
                    count += 1;
                    Console.WriteLine("{6,-3}{0,-3}{1,-5}{2,-25}{3,-10}{4,7}{5,20}",
                        count, car.id, car.model, car.issueYear, car.price, car.fuelCons, " ");
                }
                Console.WriteLine();
            }
        }
        public static void GetCarModelsWithIssueYear(IEnumerable<XElement> cars)
        {
            Console.Write("Введiть рiк випуску: ");
            string year = Convert.ToString(Console.ReadLine());
            var queryRes = from c in cars
                           where (string)c.Element("issueYear") == year
                           select new
                           {
                               id = (string)c.Element("carId"),
                               make = (string)c.Element("make"),
                               model = (string)c.Element("model"),
                               price = (int)c.Element("price"),
                               fuelCons = (int)c.Element("fuelConsumption")
                           };
            if (queryRes.Count() == 0)
            {
                Console.WriteLine("\nНемає автомобiлей обраного року випуску.");
            }
            else
            {
                Console.WriteLine();
                Console.WriteLine("                       Моделi автомобiлей з роком випуску " + year);
                Console.WriteLine();
                var count = 0;
                Console.WriteLine("{6,-3}{0,-3}{1,-5}{2,-10}{3,-25}{4,7}{5,20}",
                    "№", "id", "make", "model", "price", "fuel consumption", " ");
                Console.WriteLine("  ------------------------------------------------------------------------");
                foreach (var car in queryRes)
                {
                    count += 1;
                    Console.WriteLine("{6,-3}{0,-3}{1,-5}{2,-10}{3,-25}{4,7}{5,20}",
                        count, car.id, car.make, car.model, car.price, car.fuelCons, " ");
                }
                Console.WriteLine();
            }
        }
        public static void GetCarsWithPricesBetween(IEnumerable<XElement> cars)
        {
            Console.Write("Введiть цiну1: ");
            int price1 = Convert.ToInt32(Console.ReadLine());
            Console.Write("Введiть цiну2: ");
            int price2 = Convert.ToInt32(Console.ReadLine());
            var queryRes = from c in cars
                           where (int)c.Element("price") >= price1 && (int)c.Element("price") <= price2
                           select new
                           {
                               id = (string)c.Element("carId"),
                               make = (string)c.Element("make"),
                               model = (string)c.Element("model"),
                               issueYear = (int)c.Element("issueYear"),
                               fuelCons = (int)c.Element("fuelConsumption"),
                               price = (int)c.Element("price")
                           };
            if (queryRes.Count() == 0)
            {
                Console.WriteLine("\nНемає автомобiлей обраного дiапазону цiн.");
            }
            else
            {
                Console.WriteLine();
                Console.WriteLine("                Автомобiлi з цiнами мiж " + price1 + " та " + price2 + "$");
                Console.WriteLine();
                var count = 0;
                Console.WriteLine("{6,-3}{0,-3}{1,-5}{2,-10}{3,-25}{4,12}{5,10}{7,8}",
                    "№", "id", "Марка", "Модель", "Рiк випуску", "Паливо", " ", "Цiна");
                Console.WriteLine("  ---------------------------------------------------------------------------");
                foreach (var car in queryRes)
                {
                    count += 1;
                    Console.WriteLine("{6,-3}{0,-3}{1,-5}{2,-10}{3,-25}{4,12}{5,10}{7,8}",
                        count, car.id, car.make, car.model, car.issueYear, car.fuelCons, " ", car.price);
                }
                Console.WriteLine();
            }
        }
        public static void GetCarsWithFuelConsLess(IEnumerable<XElement> cars)
        {
            Console.Write("Введiть втрати палива (л/100км): ");
            int fualCons_user = Convert.ToInt32(Console.ReadLine());
            var queryRes = from c in cars
                           where (int)c.Element("fuelConsumption") < fualCons_user
                           select new
                           {
                               make = (string)c.Element("make"),
                               model = (string)c.Element("model"),
                               fuelCons = (int)c.Element("fuelConsumption")
                           };
            if (queryRes.Count() == 0)
            {
                Console.WriteLine("\nНемає автомобiлей з витратами палива меньше ", fualCons_user);
            }
            else
            {
                Console.WriteLine();
                Console.WriteLine("                Автомобiлi з з витратами палива < " + fualCons_user);
                Console.WriteLine();
                var count = 0;
                Console.WriteLine("{4,-3}{0,-3}{1,-10}{2,-25}{3,10}",
                    "№", "Марка", "Модель", "Паливо", " ");
                Console.WriteLine("  ---------------------------------------------------------------------------");
                foreach (var car in queryRes)
                {
                    count += 1;
                    Console.WriteLine("{4,-3}{0,-3}{1,-10}{2,-25}{3,10}",
                        count, car.make, car.model, car.fuelCons, " ");
                }
                Console.WriteLine();
            }
        }
        public static void GetAveragePriceByMake(IEnumerable<XElement> cars)
        {
            Console.Write("Введiть марку автомобiля: ");
            string make_user = Convert.ToString(Console.ReadLine());

            var queryRes = from c in cars
                           where (string)c.Element("make") == make_user
                           select (int)c.Element("price");
            if (queryRes.Count() == 0)
            {
                Console.WriteLine("\nНемає заданої марки.");
            }
            else
            {
                var avgPrice = queryRes.Sum() / queryRes.Count();
                Console.WriteLine();
                Console.WriteLine("\tСередня цiна автомобiлей марки {0}: {1} $", make_user, avgPrice);
                Console.WriteLine();
            }
        }
        public static void GetCarsGroupByShopId(IEnumerable<XElement> cars)
        {
            var queryRes = from c in cars
                           group c by (string)c.Element("shopId");
            queryRes = queryRes.OrderBy(c => c.Key);
            if (queryRes.Count() == 0)
            {
                Console.WriteLine("\nНемає автомобiлей/магазинiв в xml-документi.");
            }
            else
            {
                Console.WriteLine();
                Console.WriteLine("                Автомобiлi зрупованi за кодами магазинiв");
                Console.WriteLine();
                var count = 0;
                Console.WriteLine("{6,-3}{0,-3}{1,-10}{2,-25}{3,12}{4,10}{5,12}",
                    "№", "Марка", "Модель", "Рiк випуску", "Паливо", "Цiна", " ");
                Console.WriteLine("  ---------------------------------------------------------------------------");
                foreach (var shop in queryRes)
                {
                    foreach (var car in shop)
                    {
                        string make = (string)car.Element("make");
                        string model = (string)car.Element("model");
                        int issueYear = (int)car.Element("issueYear");
                        int fuelCons = (int)car.Element("fuelConsumption");
                        int price = (int)car.Element("price");
                        count += 1;
                        Console.WriteLine("{6,-3}{0,-3}{1,-10}{2,-25}{3,12}{4,10}{5,12}",
                            count, make, model, issueYear, fuelCons, price, " ");
                    }
                    Console.WriteLine();
                }
            }
        }
        public static void GetMakeModelCarsWithTitlePhoneShop(IEnumerable<XElement> cars)
        {
            XDocument Shops = XDocument.Load("shops.xml", LoadOptions.None);
            IEnumerable<XElement> shops = Shops.Descendants("shop");
            var queryRes = from c in cars
                           join sh in shops
                           on (string)c.Element("shopId") equals (string)sh.Element("shopId")
                           select new
                           {
                               id = (string)c.Element("carId"),
                               make = (string)c.Element("make"),
                               model = (string)c.Element("model"),
                               title = (string)sh.Element("name"),
                               tel = (string)sh.Element("telephone"),
                           };
            if (queryRes.Count() == 0)
            {
                Console.WriteLine("\nНемає автомобiлей обраного дiапазону цiн.");
            }
            else
            {
                Console.WriteLine();
                Console.WriteLine("                Марки та моделi автомобiлей з назвами та телефонами магазинiв");
                Console.WriteLine();
                var count = 0;
                Console.WriteLine("{6,-3}{0,-3}{1,-5}{2,-10}{3,-25}{4,15}{5,15}",
                    "№", "id", "Марка", "Модель", "Назва магазину", "Телефон", " ");
                Console.WriteLine("  ---------------------------------------------------------------------------");
                foreach (var car in queryRes)
                {
                    count += 1;
                    Console.WriteLine("{6,-3}{0,-3}{1,-5}{2,-10}{3,-25}{4,15}{5,15}",
                        count, car.id, car.make, car.model, car.title, car.tel, " ");
                }
                Console.WriteLine();
            }
        }
    }
}
