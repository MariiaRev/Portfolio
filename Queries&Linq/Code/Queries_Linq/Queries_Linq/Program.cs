using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace Queries_Linq
{
    class Program
    {
        static void Main(string[] args)
        {
            /*Console.OutputEncoding = System.Text.Encoding.Unicode;
            Console.InputEncoding = System.Text.Encoding.Unicode;*/
            XDocument cars = XDocument.Load("cars.xml", LoadOptions.None);
            //Console.WriteLine(cars);

            IEnumerable<XElement> elements = cars.Descendants("car");
            do
            {
                Console.WriteLine();
                Console.WriteLine("                  ---------------------------------");
                Console.WriteLine("1. Данi автомобiлей з певною маркою.");
                Console.WriteLine("2. Моделi автомобiлей з певним роком випуску.");
                Console.WriteLine("3. Кiлькiсть автомобiлей з цiною вiд \"цiна1\" до \"цiна2\".");
                Console.WriteLine("4. Марка та модель автомобiлей з витратами палива меньше, нiж ...");
                Console.WriteLine("5. Середня цiна автомобiля певної марки.");
                Console.WriteLine("6. Усi автомобiлi, згрупованi за кодом магазину.");
                Console.WriteLine("7. Марка i модель автомобiля з вказаними телефоном та назвою магазину.");
                Console.WriteLine("                  ---------------------------------");
                Console.WriteLine();
                Console.Write("Обрати запит: ");
                var choice = Convert.ToInt32(Console.ReadLine());
                switch (choice)
                {
                    case 1:
                        functions.GetCarsByMake(elements);
                        break;
                    case 2:
                        functions.GetCarModelsWithIssueYear(elements);
                        break;

                    case 3:
                        {
                            functions.GetCarsWithPricesBetween(elements);
                        }; break;

                    case 4:
                        {
                            functions.GetCarsWithFuelConsLess(elements);
                        }; break;
                    case 5:
                        {
                            functions.GetAveragePriceByMake(elements);
                        }; break;
                    case 6:
                        {
                            functions.GetCarsGroupByShopId(elements);
                        }; break;
                    case 7:
                        {
                            functions.GetMakeModelCarsWithTitlePhoneShop(elements);
                        }; break;
                    default:
                        Console.WriteLine("Немає такого запиту");
                        break;
                }
                Console.WriteLine("Для виходу натиснiсть ESC.");
                Console.WriteLine("Для продовження натиснiсть будь-яку iншу клавiшу\n");
            } while (Console.ReadKey().Key != ConsoleKey.Escape);
        }
    }
}
