

def prices(index):
    price = [
        35.00, 53.00, 61.00, 53.00, 53.00, 18.00, 62.00, 45.00, 63.00, 90.00, 99.00,
        195.00, 90.00, 126.00, 63.00, 108.00, 124.00, 124.00, 214.00, 214.00, 22.50, 288.00,
        22.50, 162.00, 270.00, 162.00, 300.00, 450.00, 270.00, 153.00, 135.00, 90.00, 140.00,
        195.00, 106.00, 200.00, 126.00, 180.00, 360.00, 900.00, 72.00, 41.00, 82.00, 22.50,
        60.00, 124.00, 22.50, 54.50, 118.00,

        35.00, 45.00, 18.00, 61.00, 53.00, 53.00, 62.00, 50.00, 63.00, 90.00, 99.00,
        195.00, 63.00, 117.00, 63.00, 108.00, 63.00, 108.00, 45.00, 90.00, 63.00, 99.00, 90.00,
        45.00, 90.00, 288.00, 144.00, 22.50, 22.50, 90.00, 140.00, 106.00, 200.00, 195.00,
        180.00, 215.00, 215.00,

        18.00, 27.00, 45.00, 80.00, 90.00, 432.00, 54.00, 108.00, 180.00, 45.00, 108.00, 162.00,
        324.00, 9.00, 9.00, 9.00, 31.50, 27.00, 45.00, 90.00, 9.00, 18.00, 27.00, 45.00, 54.00,
        90.00, 99.00, 207.00, 198.00, 270.00, 45.00, 90.00, 180.00, 324.00, 432.00, 27.00, 13.50,
        27.00, 13.50, 27.00, 13.50, 430.00, 45.00, 45.00,

        32.00, 54.00, 95.00, 140.00, 203.00, 360.00, 50.00, 63.00, 108.00, 88.00,

        # soya
        81.00, 70.00, 70.00, 66.00, 57.00, 26.10, 31.50, 81.00, 176.00, 140.00, 22.50, 93.00,
        66.00, 152.00, 94.00, 21.00, 53.25, 123.00, 228.00, 9.00, 90.00, 645.00, 48.00, 55.00,

        # Bic
        58.50, 90.00, 54.00, 90.00, 44.00, 44.00, 53.00, 150.00, 85.00, 150.00, 250.00, 9.00,

        # Cherish
        18.00, 18.00, 90.00, 90.00, 62.00, 115.00, 204.00,

        # Cake
        310.00, 460.00, 155.00, 155.00, 207.00, 207.00, 327.00, 327.00, 149.00, 173.00,

        # Kandos
        9.00, 18.00, 27.00, 45.00, 90.00, 108.00, 126.00, 270.00, 27.00, 45.00, 90.00, 410.00, 245.00, 245.00, 435.00,
        420.00, 480.00, 170.00, 170.00, 26.80, 490.00,

        # Hemas
        128.00, 124.00, 13.25, 65.00, 45.00, 49.00, 49.00, 45.50, 80.00, 113.00, 150.00, 135.00, 80.00, 137.00, 135.00,
        9.10, 82.00, 153.00, 42.50, 600.00, 60.00, 61.00, 68.00, 4.50, 4.50, 44.00, 44.00,

        # Sapumal
        6.00, 180.00, 480.00, 790.00, 900.00, 825.00, 50.00, 95.00, 95.00, 31.50, 36.00, 81.00

    ]
    return price[index]


def companies():
    return ["mbm", "cbl", "chocolates", "siddhalepa", "soya", "bic", "cherish", "Cake", "kandos", "hemas", "sapumal"]


def products(type="", product_name=""):
    print(type)
    products = [
        "Gold  Marie  75g ", " Nice  100g ", " Choco cream  100g ", " Custard cream 100g ", "Ginger  bisc  80g  ",
        " Light  Marie   75g  ", " Wafers  vanilla  90g ", " Smart Cream Cracker  85g  ", " Smart Cream Cracker 125g  ",
        " Smart Cream Cracker 190g ", " Smart Cream Cracker 230g ", " Smart Cream Cracker 490g ", " Bran Cracker 140g ",
        " Bran Cracker 210g  ", " Lemon puff   100g ", " Lemon puff     200g ", " Wafers  vanilla  225g",
        " Wafers  Choate  225g ", " Wafers  vanilla   400g ", " Wafers Choate  400g ", " Chick  Bite   30g ",
        " Chick  Bite  tin ", " Kirsco  Bite   30g ", " Kirsco  box  ", " Kirsco   tin ", " Cheese  bit  box  ",
        " Cheese  bit    tin  ", " Gift  tin ", " Gift assortment ", " Family  assortment ", " Tea  time ", " Mari  230g ",
        " Mari 330g ", " Nice  400g ", " Chocolate  Cream 230g  ", " Chocolate  Cream  400g  ", " Ginger    230g ",
        " Ginger  330g ", " Maliben  milk  400g  ", " Maliben  milk  1kg  ", " Yahaposa   200g ", " Kahata Tea 50g ",
        " Kahata Tea 100g ", " Maliben  Tea 20g ", " Maliben tea  50g", " Maliben  100g ", " Watawale  Tea 20g ",
        " Watawale  tea 50g ", " Watawale  tea 100g",

        "Tikiri  Marie 75g", " Choate  Marie  75g", " Light  Marie 75g ", " Choate  Cream  100g", " Nice  100g",
        " Ginger  bisc  80g", " Wafers  vanilla  90g ", " S  Cream  Cracker  85g", " S Cream  Cracker  125g",
        " S Cream Cracker  190g ", " S Cream Cracker  230g", " S  Cream Cracker 490 g", " Cheese Cracker  100g",
        " Cheese   Cracker  200g", "  Lemon  puff  100g", " Lemon  puff 200g", " Choate  puff  100g",
        " Choate puff  2 00g ", " Milk short  85 g ", " Milk   short  100 g ", " Hawaiñ  cookies 100g",
        " Hawain   cookies  200g ", " Tiffin 125g ", " Come  50g  ", " Come  100g ", " Gift assortment ", " Tea  time ",
        " Cheese  button 30g  ", " Onions  30g", " Tikiri Marie  230g ", " Tikiri Marie  330g ", " Choate Cream 230g ",
        " Choate Cream 400g ", " Nice 400g  ", " Ginger 400g ", " Wafers  vanilla  400g ", " Wafers  Choate  400g",

        "Choco  fingers  18g ", " Chco    fingers  27g  ", " Chco   fingers  45g  ", " Chco  fingers   80g  ",
        " Chco  fingers  100g ", " Chunkey   choc  60g ", "Chunkey  choc  20g  box ", " Chunkey   choc  120g ",
        " Chunkey  choc  200g", " Choc  mo    40g  ", " Choc  mo     100g ", " Chit chat  6g bag ", " Chit chat 10g  box ",
        " Popit     8g", "   Chco  nut  8g ", " Pebbles  8g  ", " Pebbles  tube 25g ", " Chco  nut  26g ", " Chco nut 45g ",
        " Chco  nut  90g  ", " Milk  chocolate  12g", " Milk  chocolate  18g", " Milk  chocolate  27g ",
        " Milk  chocolate  45g", "  Ritzbury  crispies", "    Milk  chocolate  90g", "   Milk  chocolate 100g",
        " Ravello  100g ", " Milk  chocolate  170g ", " Cashews 170g", "  Bubbles  40g   ", " Bubbles  90g ",
        " Bubbles  180g  ", " Bubbles 4.5g box  ", " Uno  box", " Rave  26g ", " Rave  13g ", " Champ 26g ", "Champ 13g ",
        " Tropica  26g  ", " Tropica  13g ", " Wafer  stick  box ", " Wafer stick 50g ", "Choc  shock  30g ",

        "Sidhlapa     2.5g ", " Sidhlapa    5 g  ", " Sidhlapa  10g  ", " Sidhlapa   15g  ", " Sidhlaps   25g  ",
        " Sidhlaps   30g ", "    Supirivike  40g ", " Supirivike  70g ", " Supirivike  110g ", " Asamodgum ",

        "Sera coconut milk (90) ", " Soya meat (prawns) ", " Soya meat(cuttle fish)", " Soya meat(chiken)",
        " Soya   meat (curry) ", " Soya meat(budget)", "  Samaposha  100g", "  Samaposha  200g  ", "  Samaposha   500g ",
        " Sisara 1k  ", " Hiru table solte  ", " Vinger  A/F  750ml  ", " Vinger  A/F  375ml  ", " Vinger  coconut  750ml ",
        " Vinger  covonut    375ml", "   Gango  20g ", " Kist necta  200ml ", " Kist  necta  500ml", " Kist  necta 1000ml",
        " Kist  tomato source", " Ninja  coil (12h) ", " Samahan box  ", " Niwaran  90 paspanguwa", " Kothu me",

        "Bic  Razer  (2) ", " Bic  Razer (3) ", " Gillete Razer  (2) ", " Gillete Razer (3) ", "Batteries (AA) ",
        " Batteries(AAA)  ", " Denta toothbrush ", " S/bag  ", " C/Bag ", "  5*7 Grocery bag ", " 7*10Groceru bag ",
        " Atlas pen",

        "Ch Peeps  60g ", " Ve  Peeps  60g ", " Shorties   260g ", " Peeps  260g  ", " Wafers  90g   ", "  Wafers  225g ",
        " Wafers  400g",

        "Okay  box", "  Rollo  box", "  Ch Swiss  roll  200g ", " Ve Swiss  roll  200g ", " Ch Layer  cake 310g  ",
        " Ve Layer  cake  310g ", "Ch Layer cake 460g ", " Ve Layer  cake 460g", " Butter  sponge cake  ",
        " Butter  raisins cake",

        "Kandos  Milk chocolate  9g ", " Kandos  Milk  chocolate  18g", " Kandos  Milk  chocolate  27g ",
        " Kandos  Milk  chocolate  45g ", " Kandos  Milk  chocolate  90g  ", " Kandos  Milk chocolate 100g",
        "  Kandos  cashew  bar", " Kandos  cashew large ", "  Chco  nut  27g", "  Chco  nut  45g  ", " Chco  nut  90g ",
        " Delta  toffee  pak ", " Mylady  toffee pak ", " Tamarind  pak  ", " Mylade  bottles (5)  ", "  Jujubes (2) ",
        " Uswatha  lollipop  (10) ", " Kaju  bottle  (5) ", " Milk toffee  bottle (5)", "  Choco blobs  30g ",
        " Jelly bottle (10)",

        "Eva  DT ", " Eva normal", "  Eva sachets  ", " Paper   servite   ", " C/diapers  ( s) ", " C/diapers (m)  ",
        " C/diapers  ( L )", "   Clogard Tooth paste 40g ", " Clogard tooth paste 70g  ", " Clogard tooth paste 120g ",
        " Clogard tooth paste 160g", " Cheramy  clone ", "Cheramy cream ( s )", " Cheramy cream  ( m )",
        " Kumarika  oil    ( m )", " Diva powder 60g  ", "  Diva powder 550g", "  Diva powder 1kg ", " Diva soap ",
        " Isuru Blue Soap", " Velvet soap", " baby  cheramy soap", " Baby  cheramy soap (125g)", " Dandex shampo   ",
        " Gold hair jel ", " Clogard   brush ", " Clogard juner brush",

        "Wax matches  ", " Sapumal (20)  ", " Sapumal (50) ", "Sapumal  (80) ", " Amritha ", " Ceylon seven ",
        " Sambarani ", " Kivi  shoe polish tin ", "  Kivi  shoe polish liquod ", " Jumbo p nut  ", " Jumbo p nut(chilly)",
        " Jumbo p nut 40g "

    ]
    if type == companies()[0]:
        print('ok1')
        return products[:49]
    elif type == companies()[1]:
        return products[49:86]
    elif type == companies()[2]:
        return products[86:130]
    elif type == companies()[3]:
        return products[130:140]
    elif type == companies()[4]:
        return products[140:164]
    elif type == companies()[5]:
        return products[164:176]
    elif type == companies()[6]:
        return products[176:183]
    elif type == companies()[7]:
        return products[183:193]
    elif type == companies()[8]:
        return products[193:214]
    elif type == companies()[9]:
        return products[214:241]
    elif type == companies()[10]:
        return products[241:]
    else:
        index = 0
        for name in products:
            if name == product_name:
                return index
            index += 1


def customers():
    return [
        '1.Dayasiri Stores-Ekala ',
        '1. Vineetha Grocery-Ekala ',
        '1. Pubudu Grocery-Ekala ',
        '1. Lakshman Grocery-Makewita ',
        '1. Basnayake Grocery-Makewita ',
        '1. Jayantha Grocery-Makewita ',
        '1. Jayakodi Grocery-Makewita ',
        '1. Sugath Grocery-Makewita ',
        '1. Sampath Stores-makewita ',
        '1. Co-operative shop-Makewita ',
        '1. Laksiri Stores-Udugampola ',
        '1. Akarawita Stores-Akarawita ',
        '1. Sampath Stores-Akarawita ',
        '1. Senani Grocery-Akarawita ',
        '1. Shelton Bookshop-Karawita ',
        '1. Wanigasooriya Grocery-Makewita ',
        '1. Sonali Stores-Ekala ',
        '1. Lasindu Grocery-Makewita ',
        '1. Wimala Grocery-Makewita',
        '2.Lal Stores-Mabola ',
        '2. Manel Grocery-Hendala ',
        '2. Indika Stores-Elakanda ',
        '2. Jayamaha Grocery-Weliamuna ',
        '2. Lalani Grocery-Weliamuna ',
        '2.Sarath Grocery-Elakanda ',
        '2. Asela Grocery-Elakanda ',
        '2. Nehara Grocery-Elakanda ',
        '2. Havi Grocery-Elakanda ',
        '2. Nihal Grocery-Nayakakanda ',
        '2. Renuka Grocery-Nayakakanda ',
        '2. Jayakodi Stores-Kelawarapitiya ',
        '2. Jude Grocery-Kelawarapitiya ',
        '2. Sujeewa Grocery-Kelawarapitiya ',
        '2. Shiroma Stores-Kelawarapitiya ',
        '2. Priyanthi Grocery-Kelawarapitiya',
        '3.A.J. Grocery-Wanawasala ',
        '3. Mahinda Grocery-Wanawasala ',
        '3. Jony Grocery-Wanawasala ',
        '3. P$S Stores-Thorana Junction ',
        '3. Bakmeewewa Coolspot-Thorana Junction ',
        '3. Samanala Grocery-Thorana Junction ',
        '3. Anura Pharmacy-Thorana Junction ',
        '3. Pathirana Grocery-Kelaniya ',
        '3. Nishantha Stores-Kelaniya ',
        '3. Tharanga Bakery-Dalugama ',
        '3. Muditha Grocery-Dalugama ',
        '3. Jeewana Grocery-Wewalduuwa ',
        '3. Lahiru Grocery-Wewalduuwa ',
        '3. Samanthi Grocery-Hunupitiya ',
        '3. Madu Grocery-Hunupitiya',
        '4.Angel Bookshop-Enderamulla ',
        '4. Suranga Grocery-Enderamulla ',
        '4. Arosha Grocery-Enderamulla ',
        '4. Asela Grocery-Enderamulla ',
        '4. Sarath Gas Centre-Enderamulla ',
        '4. Lakshman Grocery-Horape ',
        '4. Pasindu Grocery-Horape ',
        '4. Adithya Grocery-Delpe Junction ',
        '4. Sanduni-Delpe Junction ',
        '4. Saman Grocery-Delpe Junction ',
        '4. New Pharmacy-Delpe Junction ',
        '4. Naleen Gas Centre-Delpe Junction ',
        '4. Rajitha Grocery-Delpe Junction ',
        '4. Piyasiri Gas Centre-Delpe Junction ',
        '4. Ananda Grocery-Delpe Junction ',
        '4.  Kalyani Grocery-Enderamulla',
        '5.Kaveesha Grocery-Gongithota ',
        '5. Rohana Stores-Gongithota ',
        '5. Indika Grocery-Gongithota ',
        '5. Pathum Grocery-Paranakanda  ',
        '5. Kanishka Grocery-Paranakanda ',
        '5. Siripala Grocery-Paranakanda ',
        '5. Perera Grocery-Paranakanda ',
        '5. Sagara Stores-Paranakanda ',
        '5. Savindi Grocery-Paranakanda ',
        '5.Channa Grocery-Gongithota ',
        '5. Ruwan Oil Centre-Gongithota ',
        '5. Ramani Dias Grocery-Gongithota ',
        '5. Vimal Stores-Gongithota ',
        '5. Jayasinghe Grocery- Gongithota ',
        '5. Sugath Grocery- Gongithota ',
        '5. Mathara Stores- Gongithota ',
        '5. Thisera Coolspot- Gongithota ',
        '5. Vijesiri Grocery- Gongithota ',
        '5. Kanthi Stores-Gongithota ',
        '5. Sanda Grocery- Gongithota ',
        '5.Premasiri Grocery- Gongithota]'
    ]
