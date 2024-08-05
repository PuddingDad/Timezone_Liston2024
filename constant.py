timezone_dict = {
    "North America": {
        "United States": {"timezone": "America/New_York", "lat": 37.0902, "lon": -95.7129},
        "Canada": {"timezone": "America/Toronto", "lat": 56.1304, "lon": -106.3468},
        "Mexico": {"timezone": "America/Mexico_City", "lat": 23.6345, "lon": -102.5528},
        "Jamaica": {"timezone": "America/Jamaica", "lat": 18.1096, "lon": -77.2975},
        "Costa Rica": {"timezone": "America/Costa_Rica", "lat": 9.7489, "lon": -83.7534},
        "Bahamas": {"timezone": "America/Nassau", "lat": 25.0343, "lon": -77.3963},
        "Honduras": {"timezone": "America/Tegucigalpa", "lat": 15.2000, "lon": -86.2419},
        "Cuba": {"timezone": "America/Havana", "lat": 21.5218, "lon": -77.7812},
        "Dominican Republic": {"timezone": "America/Santo_Domingo", "lat": 18.7357, "lon": -70.1627}
    },
    "South America": {
        "Brazil": {"timezone": "America/Sao_Paulo", "lat": -14.2350, "lon": -51.9253},
        "Argentina": {"timezone": "America/Argentina/Buenos_Aires", "lat": -38.4161, "lon": -63.6167},
        "Chile": {"timezone": "America/Santiago", "lat": -35.6751, "lon": -71.5430},
        "Colombia": {"timezone": "America/Bogota", "lat": 4.5709, "lon": -74.2973},
        "Peru": {"timezone": "America/Lima", "lat": -9.1900, "lon": -75.0152},
        "Uruguay": {"timezone": "America/Montevideo", "lat": -32.5228, "lon": -55.7658},
        "Ecuador": {"timezone": "America/Guayaquil", "lat": -1.8312, "lon": -78.1834},
        "Bolivia": {"timezone": "America/La_Paz", "lat": -16.2902, "lon": -63.5887},
        "Paraguay": {"timezone": "America/Asuncion", "lat": -23.4425, "lon": -58.4438},
        "Venezuela": {"timezone": "America/Caracas", "lat": 6.4238, "lon": -66.5897}
    },
    "Europe": {
        "United Kingdom": {"timezone": "Europe/London", "lat": 55.3781, "lon": -3.4360},
        "France": {"timezone": "Europe/Paris", "lat": 46.6034, "lon": 1.8883},
        "Germany": {"timezone": "Europe/Berlin", "lat": 51.1657, "lon": 10.4515},
        "Italy": {"timezone": "Europe/Rome", "lat": 41.8719, "lon": 12.5674},
        "Spain": {"timezone": "Europe/Madrid", "lat": 40.4637, "lon": -3.7492},
        "Russia": {"timezone": "Europe/Moscow", "lat": 61.5240, "lon": 105.3188},
        "Turkey": {"timezone": "Europe/Istanbul", "lat": 38.9637, "lon": 35.2433},
        "Greece": {"timezone": "Europe/Athens", "lat": 39.0742, "lon": 21.8243},
        "Poland": {"timezone": "Europe/Warsaw", "lat": 51.9194, "lon": 19.1451},
        "Ukraine": {"timezone": "Europe/Kiev", "lat": 48.3794, "lon": 31.1656}
    },
    "Asia": {
        "India": {"timezone": "Asia/Kolkata", "lat": 20.5937, "lon": 78.9629},
        "Japan": {"timezone": "Asia/Tokyo", "lat": 35.6895, "lon": 139.6917},
        "China": {"timezone": "Asia/Shanghai", "lat": 35.8617, "lon": 104.1954},
        "Saudi Arabia": {"timezone": "Asia/Riyadh", "lat": 23.8859, "lon": 45.0792},
        "South Korea": {"timezone": "Asia/Seoul", "lat": 35.9078, "lon": 127.7669},
        "Indonesia": {"timezone": "Asia/Jakarta", "lat": -0.7893, "lon": 113.9213},
        "Malaysia": {"timezone": "Asia/Kuala_Lumpur", "lat": 4.2105, "lon": 101.9758},
        "Vietnam": {"timezone": "Asia/Ho_Chi_Minh", "lat": 14.0583, "lon": 108.2772},
        "Philippines": {"timezone": "Asia/Manila", "lat": 12.8797, "lon": 121.7740},
        "Thailand": {"timezone": "Asia/Bangkok", "lat": 15.8700, "lon": 100.9925}
    },
    "Oceania": {
        "Australia": {"timezone": "Australia/Sydney", "lat": -25.2744, "lon": 133.7751},
        "New Zealand": {"timezone": "Pacific/Auckland", "lat": -40.9006, "lon": 174.8860},
        "Fiji": {"timezone": "Pacific/Fiji", "lat": -17.7134, "lon": 178.0650},
        "Papua New Guinea": {"timezone": "Pacific/Port_Moresby", "lat": -6.314993, "lon": 143.9555},
        "Samoa": {"timezone": "Pacific/Apia", "lat": -13.7590, "lon": -172.1046},
        "Tonga": {"timezone": "Pacific/Tongatapu", "lat": -21.1790, "lon": -175.1982},
        "Solomon Islands": {"timezone": "Pacific/Guadalcanal", "lat": -9.6457, "lon": 160.1562},
        "Vanuatu": {"timezone": "Pacific/Efate", "lat": -15.3767, "lon": 166.9592},
        "Kiribati": {"timezone": "Pacific/Tarawa", "lat": 1.451817, "lon": 173.0376},
        "New Caledonia": {"timezone": "Pacific/Noumea", "lat": -20.9043, "lon": 165.6180}
    },
  "Africa": {
    "Kenya": {"timezone": "Africa/Nairobi", "lat": -1.2921, "lon": 36.8219},
    "Egypt": {"timezone": "Africa/Cairo", "lat": 26.8206, "lon": 30.8025},
    "Zimbabwe": {"timezone": "Africa/Harare", "lat": -17.8292, "lon": 31.0522},
    "Congo": {"timezone": "Africa/Brazzaville", "lat": -4.2634, "lon": 15.2429},
    "Somalia": {"timezone": "Africa/Mogadishu", "lat": 2.0469, "lon": 45.3182},
    "Ghana": {"timezone": "Africa/Accra", "lat": 5.6037, "lon": -0.1870},
    "Ethiopia": {"timezone": "Africa/Addis_Ababa", "lat": 9.0316, "lon": 38.7612},
    "Sudan": {"timezone": "Africa/Khartoum", "lat": 15.5007, "lon": 32.5599},
    "Uganda": {"timezone": "Africa/Kampala", "lat": 0.3476, "lon": 32.5825},
    "Zambia": {"timezone": "Africa/Lusaka", "lat": -15.3875, "lon": 28.3228},
}
}

tih_api = "https://history.muffinlabs.com/date"
tih_wiki = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all'


country_info= {
    "United States": {
        "capital": "Washington, D.C.",
        "description": "The United States is known for its diverse culture, technology hubs like Silicon Valley, and iconic landmarks such as the Statue of Liberty. It's a leading country in global politics, economy, and military power.",
        "image": "https://cdn.mos.cms.futurecdn.net/XsbvTN6PRi6PZtgEGvRsiE.jpg",  # Replace with the actual URL
        "caption": "Statue of Liberty in New York City, a symbol of freedom and democracy."
    },
    "Canada": {
        "capital": "Ottawa",
        "description": "Canada is famous for its natural beauty, polite people, and landmarks such as Niagara Falls and the CN Tower. It is the second-largest country in the world by land area.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/ab/3Falls_Niagara.jpg",  # Replace with the actual URL
        "caption": "Niagara Falls, one of the most famous waterfalls in the world."
    },
    "Mexico": {
        "capital": "Mexico City",
        "description": "Mexico is known for its rich cultural heritage, vibrant festivals, and landmarks such as Chichen Itza and Cancun. It has a diverse landscape that includes beaches, deserts, and jungles.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Chichen_Itza_3.jpg/640px-Chichen_Itza_3.jpg",  # Replace with the actual URL
        "caption": "Chichen Itza, an ancient Mayan city and UNESCO World Heritage site."
    },
    "Jamaica": {
        "capital": "Kingston",
        "description": "Jamaica is famous for reggae music, beautiful beaches, and a vibrant culture. It is a popular tourist destination known for its resorts and laid-back lifestyle.",
        "image": "https://cdn.sandals.com/beaches/v12/images/resorts/bng/seven-mile-beach/large-beach.jpg",  # Replace with the actual URL
        "caption": "Seven Mile Beach in Negril, known for its white sand and clear waters."
    },
    "Costa Rica": {
        "capital": "San José",
        "description": "Costa Rica is known for its biodiversity, eco-tourism, and beautiful landscapes. It is a leader in environmental sustainability and conservation efforts.",
        "image": "https://volcano.si.edu/gallery/photos/GVP-08129.jpg",  # Replace with the actual URL
        "caption": "Arenal Volcano, an iconic and active volcano in Costa Rica."
    },
    "Bahamas": {
        "capital": "Nassau",
        "description": "The Bahamas is famous for its stunning beaches, clear blue waters, and thriving tourism industry. It's a popular destination for luxury vacations and water sports.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUWH78wpSiJYnJmBx0weRGM9C_1Jtf3rGR_g&s",  # Replace with the actual URL
        "caption": "The pristine beaches of the Bahamas, perfect for relaxation and adventure."
    },
    "Honduras": {
        "capital": "Tegucigalpa",
        "description": "Honduras is known for its rich history, ancient ruins, and natural beauty. It offers a variety of landscapes from beaches to mountains.",
        "image": "https://www.visitcentroamerica.com/wp-content/uploads/2017/09/place-central-america-honduras-ruins-copan-03.jpg",  # Replace with the actual URL
        "caption": "Copán Ruinas, an ancient Mayan archaeological site."
    },
    "Cuba": {
        "capital": "Havana",
        "description": "Cuba is famous for its cigars, classic cars, and vibrant culture. Its capital, Havana, is known for its colonial architecture and historical significance.",
        "image": "https://content.r9cdn.net/rimg/dimg/a3/1d/05f2b4a1-city-11020-1700c4dba73.jpg?crop=true&width=1020&height=498",  # Replace with the actual URL
        "caption": "The colorful streets and classic cars of Havana."
    },
    "Dominican Republic": {
        "capital": "Santo Domingo",
        "description": "The Dominican Republic is known for its beautiful beaches, resorts, and rich cultural heritage. It shares the island of Hispaniola with Haiti.",
        "image": "https://media.tacdn.com/media/attractions-content--1x-1/12/5f/c0/84.jpg",  # Replace with the actual URL
        "caption": "Punta Cana, renowned for its stunning beaches and clear waters."
    },
    "Brazil": {
        "capital": "Brasília",
        "description": "Brazil is famous for its Carnival festival, Amazon rainforest, and vibrant culture. It is the largest country in South America by both area and population.",
        "image": "https://publisher-ncreg.s3.us-east-2.amazonaws.com/pb-ncregister/swp/hv9hms/media/20231122221124_45448c583eabca7ad6be347939c641312d4ce7570209ad29d3345175aea14fec.jpg",  # Replace with the actual URL
        "caption": "Christ the Redeemer statue overlooking Rio de Janeiro."
    },
    "Argentina": {
        "capital": "Buenos Aires",
        "description": "Argentina is known for its tango music, wine, and landmarks such as Patagonia. It has a rich cultural heritage and diverse landscapes.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Perito_Moreno_Glacier_Patagonia_Argentina_Luca_Galuzzi_2005.JPG/1200px-Perito_Moreno_Glacier_Patagonia_Argentina_Luca_Galuzzi_2005.JPG",  # Replace with the actual URL
        "caption": "Perito Moreno Glacier in Patagonia, a stunning natural wonder."
    },
    "Chile": {
        "capital": "Santiago",
        "description": "Chile is famous for its diverse landscapes, wine regions, and Easter Island. It stretches along the western edge of South America, from the Atacama Desert in the north to Patagonia in the south.",
        "image": "https://vajiram-prod.s3.ap-south-1.amazonaws.com/What_are_Moai_statues_65df02ed78.jpg",  # Replace with the actual URL
        "caption": "The Moai statues on Easter Island, a UNESCO World Heritage site."
    },
    "Colombia": {
        "capital": "Bogotá",
        "description": "Colombia is known for its coffee, cultural heritage, and landmarks like Cartagena. It has a diverse landscape that includes mountains, rainforests, and beaches.",
        "image": "https://content.r9cdn.net/rimg/dimg/16/60/a2791cb8-city-26923-164d7878ff3.jpg?width=1366&height=768&xhint=2150&yhint=1306&crop=true",  # Replace with the actual URL
        "caption": "The colorful colonial architecture of Cartagena."
    },
    "Peru": {
        "capital": "Lima",
        "description": "Peru is famous for Machu Picchu, rich history, and diverse cuisine. It has a significant indigenous population and is known for its archaeological sites.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Machu_Picchu%2C_Peru.jpg/1200px-Machu_Picchu%2C_Peru.jpg",  # Replace with the actual URL
        "caption": "Machu Picchu, the ancient Incan city set high in the Andes Mountains."
    },
    "Uruguay": {
        "capital": "Montevideo",
        "description": "Uruguay is known for its beaches, vibrant culture, and historic towns. It is one of the most progressive countries in Latin America.",
        "image": "https://assets.megamediaradios.fm/sites/2/2023/12/9614150292_a7fa6e70af_b-768x576.jpg",  # Replace with the actual URL
        "caption": "Punta del Este, a popular beach resort destination."
    },
    "Ecuador": {
        "capital": "Quito",
        "description": "Ecuador is famous for the Galapagos Islands, diverse landscapes, and rich culture. It is located on the equator, from which it derives its name.",
        "image": "https://www.travelandleisure.com/thmb/WzL019sDotA4SIo4bacRrE4j_N0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/galapagos-islands-ecuador-GALAPA1104-d013219debf14369ab5039a4eafb496e.jpg",  # Replace with the actual URL
        "caption": "The Galapagos Islands, known for their unique wildlife and ecosystems."
    },
    "Bolivia": {
        "capital": "Sucre (constitutional), La Paz (seat of government)",
        "description": "Bolivia is known for its high-altitude cities, salt flats, and rich indigenous culture. It has one of the largest indigenous populations in Latin America.",
        "image": "https://www.gochile.cl/fotos/full/106562-10525555_981197595267185_7783138974584524459_n.jpg",  # Replace with the actual URL
        "caption": "Salar de Uyuni, the world's largest salt flat."
    },
    "Paraguay": {
        "capital": "Asunción",
        "description": "Paraguay is famous for its rich history, cultural festivals, and beautiful landscapes. It is a landlocked country located in the heart of South America.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3d/J38_025_Encarnaci%C3%B3n%2C_Avenida_Costanera_Republica_del_Paraguay.jpg",  # Replace with the actual URL
        "caption": "The historic town of Encarnación, known for its Jesuit missions."
    },
    "Venezuela": {
        "capital": "Caracas",
        "description": "Venezuela is known for its oil reserves, beautiful landscapes, and cultural diversity. It has the world's largest proven oil reserves.",
        "image": "https://cdn.britannica.com/81/155181-050-CE1B56BF/Angel-Falls-waterfall-world-Rio-Churun-Venezuela.jpg",  # Replace with the actual URL
        "caption": "Angel Falls, the world's highest uninterrupted waterfall."
    },
    "United Kingdom": {
        "capital": "London",
        "description": "The United Kingdom is famous for its rich history, landmarks like Big Ben, and vibrant culture. It consists of England, Scotland, Wales, and Northern Ireland.",
        "image": "https://www.londonperfect.com/g/photos/upload/sml_302526596-1498570960-big-ben-westminster.jpg",  # Replace with the actual URL
        "caption": "Big Ben and the Houses of Parliament, iconic symbols of London."
    },
    "France": {
        "capital": "Paris",
        "description": "France is known for its art, cuisine, landmarks like the Eiffel Tower, and romantic culture. It is one of the most visited countries in the world.",
        "image": "https://www.travelandleisure.com/thmb/SPUPzO88ZXq6P4Sm4mC5Xuinoik=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/eiffel-tower-paris-france-EIFFEL0217-6ccc3553e98946f18c893018d5b42bde.jpg",  # Replace with the actual URL
        "caption": "The Eiffel Tower, an iconic symbol of Paris and France."
    },
    "Germany": {
        "capital": "Berlin",
        "description": "Germany is famous for its engineering, beer, and landmarks like the Berlin Wall. It is a leading country in the European Union.",
        "image": "https://media.cntraveler.com/photos/5b914e80d5806340ca438db1/16:9/w_2560,c_limit/BrandenburgGate_2018_GettyImages-549093677.jpg",  # Replace with the actual URL
        "caption": "The Brandenburg Gate, a symbol of German unity and history."
    },
    "Italy": {
        "capital": "Rome",
        "description": "Italy is known for its rich history, cuisine, and landmarks such as the Colosseum. It is the birthplace of the Renaissance and home to numerous UNESCO World Heritage sites.",
        "image": "https://cdn.mos.cms.futurecdn.net/BiNbcY5fXy9Lra47jqHKGK-1200-80.jpg",  # Replace with the actual URL
        "caption": "The Colosseum in Rome, an ancient amphitheater and iconic landmark."
    },
    "Spain": {
        "capital": "Madrid",
        "description": "Spain is famous for its vibrant culture, flamenco music, and landmarks such as the Sagrada Familia. It has a rich history and diverse regions.",
        "image": "https://cdn.britannica.com/15/194815-050-08B5E7D1/Nativity-facade-Sagrada-Familia-cathedral-Barcelona-Spain.jpg",  # Replace with the actual URL
        "caption": "La Sagrada Familia, a masterpiece of architecture in Barcelona."
    },
    "Portugal": {
        "capital": "Lisbon",
        "description": "Portugal is known for its beautiful coastline, historic cities, and Fado music. It has a rich maritime history and is one of the oldest nations in Europe.",
        "image": "https://cdn-imgix.headout.com/media/images/ed1d75795abe9978e68d8da6934e99be-17655-TicketstoBele-mTower---009.jpg?w=744&h=465&crop=faces&auto=compress%2Cformat&fit=min",  # Replace with the actual URL
        "caption": "The historic Belem Tower in Lisbon, a symbol of Portugal's maritime history."
    },
    "Netherlands": {
        "capital": "Amsterdam",
        "description": "The Netherlands is famous for its canals, windmills, and vibrant tulip fields. It is known for its liberal policies and rich cultural heritage.",
        "image": "https://cdn.britannica.com/78/219378-131-A2307D59/Rijksmuseum-Amsterdam.jpg",  # Replace with the actual URL
        "caption": "Amsterdam's iconic canals and historic buildings."
    },
    "Belgium": {
        "capital": "Brussels",
        "description": "Belgium is known for its chocolate, waffles, and medieval towns. It is the headquarters of the European Union and NATO.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHYNGHq83H7Q4Cp1_V-rB4uuxmoJBC-Ix34w&s",  # Replace with the actual URL
        "caption": "The Grand Place in Brussels, a UNESCO World Heritage site."
    },
    "Switzerland": {
        "capital": "Bern",
        "description": "Switzerland is famous for its mountains, chocolate, and neutrality. It is known for its high quality of life and beautiful landscapes.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Matterhorn_from_Domh%C3%BCtte_-_2.jpg/1200px-Matterhorn_from_Domh%C3%BCtte_-_2.jpg",  # Replace with the actual URL
        "caption": "The Matterhorn, one of the most famous mountains in the Swiss Alps."
    },
    "Austria": {
        "capital": "Vienna",
        "description": "Austria is known for its classical music, beautiful landscapes, and rich history. It has a strong cultural heritage and is the birthplace of many famous composers.",
        "image": "https://cdn.shopify.com/s/files/1/1846/2967/articles/schonbrunn-min.jpg?v=1502201578",  # Replace with the actual URL
        "caption": "The historic Schönbrunn Palace in Vienna."
    },
    "Sweden": {
        "capital": "Stockholm",
        "description": "Sweden is famous for its high quality of life, design, and natural beauty. It is known for its progressive policies and vibrant culture.",
        "image": "https://media.tacdn.com/media/attractions-splice-spp-674x446/0b/27/88/f7.jpg",  # Replace with the actual URL
        "caption": "Stockholm's historic Gamla Stan, one of the best-preserved medieval city centers in Europe."
    },
    "Norway": {
        "capital": "Oslo",
        "description": "Norway is known for its stunning fjords, Northern Lights, and high standard of living. It is one of the world's wealthiest countries per capita.",
        "image": "https://res.cloudinary.com/simpleview/image/upload/v1470836048/clients/norway/naeroyfjorden_fjord_norway_2_1_001b9127-14ad-4b3d-99b6-29d8b3aae412.jpg",  # Replace with the actual URL
        "caption": "The breathtaking fjords of Norway, a natural wonder."
    },
    "Denmark": {
        "capital": "Copenhagen",
        "description": "Denmark is famous for its design, high quality of life, and historic architecture. It is known for its progressive social policies and as the home of the Vikings.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKBdbvrmk03OFHua219PS0pkh-bEnND6DAgQ&s",  # Replace with the actual URL
        "caption": "Nyhavn in Copenhagen, known for its colorful houses and historic boats."
    },
    "Finland": {
        "capital": "Helsinki",
        "description": "Finland is known for its education system, saunas, and beautiful natural landscapes. It is one of the happiest countries in the world.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8GrHS20D98ami_6pJmcfHpCB18D_jJCjRAg&s",  # Replace with the actual URL
        "caption": "The Northern Lights, a spectacular natural phenomenon visible in Finland."
    },
    "Iceland": {
        "capital": "Reykjavik",
        "description": "Iceland is famous for its geothermal activity, waterfalls, and glaciers. It is known for its unique landscapes and high quality of life.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhQ-Hw36yDflFHvxevOHGKGPM0PwEKCZvHGA&s",  # Replace with the actual URL
        "caption": "The Blue Lagoon, a geothermal spa and popular tourist destination."
    },
    "Ireland": {
        "capital": "Dublin",
        "description": "Ireland is known for its lush landscapes, rich cultural heritage, and vibrant music scene. It is famous for its literature, traditional music, and historic castles.",
        "image": "https://images.ireland.com/media/Images/destinations/county/Clare/3a78caab4f9b4ef29ef0527da0231b36.jpeg",  # Replace with the actual URL
        "caption": "The Cliffs of Moher, one of Ireland's most famous natural landmarks."
    },
    "Greece": {
        "capital": "Athens",
        "description": "Greece is known for its ancient history, stunning islands, and Mediterranean cuisine. It is the birthplace of democracy and Western philosophy.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-w7i9rN1p8rL7SlwP4YGYt6H4zhsvKJ_2sw&s",  # Replace with the actual URL
        "caption": "The Parthenon in Athens, an iconic symbol of ancient Greece."
    },
    "Turkey": {
        "capital": "Ankara",
        "description": "Turkey is famous for its rich history, diverse culture, and landmarks such as Hagia Sophia. It straddles both Europe and Asia and has a unique blend of Eastern and Western influences.",
        "image": "https://cdn.britannica.com/03/189803-050-871B95C4/Hagia-Sophia-Istanbul.jpg",  # Replace with the actual URL
        "caption": "Hagia Sophia, a historic and architectural marvel in Istanbul."
    },
    "Russia": {
        "capital": "Moscow",
        "description": "Russia is known for its vast size, diverse culture, and historical landmarks. It is the largest country in the world by area and has a rich cultural heritage.",
        "image": "https://gallerybyzantium.com/wp-content/uploads/2019/01/st-basil-cathedral_1.jpg",  # Replace with the actual URL
        "caption": "St. Basil's Cathedral in Moscow, known for its colorful onion domes."
    },
    "Ukraine": {
        "capital": "Kyiv",
        "description": "Ukraine is known for its rich history, vibrant culture, and beautiful landscapes. It is one of the largest countries in Europe by area.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRydckPaNjoY1iWX8WnY7QATkyHCbkLpD5cZg&s",  # Replace with the actual URL
        "caption": "The historic St. Sophia's Cathedral in Kyiv."
    },
    "Poland": {
        "capital": "Warsaw",
        "description": "Poland is famous for its medieval architecture, rich history, and cultural heritage. It has a resilient spirit and is known for its contributions to art, music, and science.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrOtcjE7amnQRqMLdH2DAc0M1Nj69VYpsChA&s",  # Replace with the actual URL
        "caption": "The historic market square in Krakow, a UNESCO World Heritage site."
    },
    "Romania": {
        "capital": "Bucharest",
        "description": "Romania is known for its beautiful landscapes, medieval castles, and rich folklore. It is the home of the legendary Dracula and has a diverse cultural heritage.",
        "image": "https://miro.medium.com/v2/resize:fit:1140/1*nKl07q4rHSTz5IwaFgmwiA.jpeg",  # Replace with the actual URL
        "caption": "Bran Castle, commonly known as Dracula's Castle."
    },
    "Hungary": {
        "capital": "Budapest",
        "description": "Hungary is famous for its thermal baths, vibrant culture, and historical landmarks. It is known for its contributions to music, literature, and science.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6VI0Zi0wt-RmaLWC6W-IetuhokE8xw7cnJg&s",  # Replace with the actual URL
        "caption": "The Hungarian Parliament Building, an architectural gem in Budapest."
    },
    "Czech Republic": {
        "capital": "Prague",
        "description": "The Czech Republic is known for its medieval towns, beer culture, and vibrant arts scene. It has a rich history and is home to many UNESCO World Heritage sites.",
        "image": "https://media1.thrillophilia.com/filestore/vgatnf0y74oxhh8qynnmldtyk6cs_shutterstock_222064795.jpg",  # Replace with the actual URL
        "caption": "The historic Charles Bridge in Prague, a symbol of the city's rich history."
    },
    "Slovakia": {
        "capital": "Bratislava",
        "description": "Slovakia is known for its beautiful landscapes, castles, and vibrant folk traditions. It is a landlocked country in Central Europe with a rich cultural heritage.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPWcrSaC8W3YHnGC-h8ohjxpLSRVyXHOJDDw&s",  # Replace with the actual URL
        "caption": "Bratislava Castle, overlooking the capital city of Slovakia."
    },
    "Bulgaria": {
        "capital": "Sofia",
        "description": "Bulgaria is famous for its rich history, beautiful landscapes, and vibrant culture. It has a diverse range of natural attractions, from mountains to beaches.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQSklDXsfGFEL11wxxsg0OolNWJq3mrjwNmA&s",  # Replace with the actual URL
        "caption": "The Rila Monastery, a UNESCO World Heritage site in Bulgaria."
    },
    "Serbia": {
        "capital": "Belgrade",
        "description": "Serbia is known for its rich cultural heritage, vibrant festivals, and beautiful landscapes. It has a diverse cultural scene and a complex history.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyOti8dreiP5T4cHcH6WcjJrWItb1RkDfhkA&s",  # Replace with the actual URL
        "caption": "The historic Kalemegdan Fortress in Belgrade."
    },
    "Croatia": {
        "capital": "Zagreb",
        "description": "Croatia is famous for its stunning coastline, historic towns, and vibrant culture. It is a popular tourist destination known for its beautiful beaches and crystal-clear waters.",
        "image": "https://assets.vogue.com/photos/597642e77563be3e6b400a90/master/w_2560%2Cc_limit/00-lede-dubrovnik-croatia-travel-guide.jpg",  # Replace with the actual URL
        "caption": "The picturesque town of Dubrovnik, a UNESCO World Heritage site."
    },
    "Slovenia": {
        "capital": "Ljubljana",
        "description": "Slovenia is known for its beautiful landscapes, charming towns, and rich cultural heritage. It is a green and diverse country located in Central Europe.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/84/Lake_Bled_from_the_Mountain.jpg",  # Replace with the actual URL
        "caption": "Lake Bled, known for its picturesque island and medieval castle."
    },
    "Bosnia and Herzegovina": {
        "capital": "Sarajevo",
        "description": "Bosnia and Herzegovina is known for its rich cultural heritage, beautiful landscapes, and historic cities. It has a complex history and a vibrant cultural scene.",
        "image": "https://images.squarespace-cdn.com/content/v1/5db2c1c870cf53160ba6a917/1572209323313-27RYXM0IUTPX09LHV1VN/IMG_0934.jpeg",  # Replace with the actual URL
        "caption": "The historic Stari Most bridge in Mostar."
    },
    "Montenegro": {
        "capital": "Podgorica",
        "description": "Montenegro is famous for its stunning Adriatic coastline, beautiful mountains, and medieval towns. It is a small but diverse country with a rich cultural heritage.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjzWvGx9DqS3YTGaC1Qh5tlfYvg-RMmmUnBQ&s",  # Replace with the actual URL
        "caption": "The Bay of Kotor, known for its breathtaking beauty."
    },
    "North Macedonia": {
        "capital": "Skopje",
        "description": "North Macedonia is known for its rich history, diverse culture, and beautiful landscapes. It is a landlocked country in the Balkans with a unique cultural heritage.",
        "image": "https://images.squarespace-cdn.com/content/v1/545012a9e4b0988576f6b699/611c855e-c4e8-48bb-af2d-05e6be6ed3ad/ohrid-north-macedonia-old-town-lake.jpeg",  # Replace with the actual URL
        "caption": "The historic town of Ohrid, known for its ancient churches and beautiful lake."
    },
    "Albania": {
        "capital": "Tirana",
        "description": "Albania is known for its beautiful beaches, rich history, and vibrant culture. It is a country with a unique blend of Mediterranean and Balkan influences.",
        "image": "https://i0.wp.com/feel-albania.com/wp-content/uploads/2019/10/Berat-City-by-night.jpg?fit=1800%2C1080&ssl=1",  # Replace with the actual URL
        "caption": "The ancient city of Berat, a UNESCO World Heritage site."
    },
    "Kosovo": {
        "capital": "Pristina",
        "description": "Kosovo is known for its rich cultural heritage, vibrant music scene, and beautiful landscapes. It is a young country with a diverse population and a complex history.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Prizren_Fortress_%282021%29.jpg",  # Replace with the actual URL
        "caption": "The historic Prizren Fortress, overlooking the city of Prizren."
    },
    "Armenia": {
        "capital": "Yerevan",
        "description": "Armenia is known for its rich history, ancient churches, and beautiful landscapes. It is one of the oldest Christian nations in the world and has a unique cultural heritage.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlugVxFznQsCit04ZUCC9LIlIo0qG8UWlK3w&s",  # Replace with the actual URL
        "caption": "The ancient monastery of Geghard, a UNESCO World Heritage site."
    },
    "Azerbaijan": {
        "capital": "Baku",
        "description": "Azerbaijan is known for its rich history, diverse culture, and beautiful landscapes. It is a country located at the crossroads of Europe and Asia, with a unique blend of Eastern and Western influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwRaoRxCHZlMR4GpN_BGz7FRFwKqsU0CuUiw&s",  # Replace with the actual URL
        "caption": "The Flame Towers in Baku, a symbol of modern Azerbaijan."
    },
    "Georgia": {
        "capital": "Tbilisi",
        "description": "Georgia is famous for its rich history, beautiful landscapes, and vibrant culture. It is known for its unique cuisine and wine, as well as its hospitality.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG7P78Ahzt3dYFQgHK6Bng0T5Di5OTgcbSBw&s",  # Replace with the actual URL
        "caption": "The historic town of Sighnaghi, known for its wine and stunning views."
    },
    "Kazakhstan": {
        "capital": "Nur-Sultan",
        "description": "Kazakhstan is known for its vast steppes, rich history, and diverse culture. It is the largest landlocked country in the world and has a unique blend of Asian and European influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLmuhlNWGPaI45ld4_hK6mzZ7YnUGhwrNpPw&s",  # Replace with the actual URL
        "caption": "The futuristic cityscape of Nur-Sultan, the capital of Kazakhstan."
    },
    "Uzbekistan": {
        "capital": "Tashkent",
        "description": "Uzbekistan is known for its rich history, beautiful architecture, and vibrant culture. It is located in Central Asia and is famous for its Silk Road cities.",
        "image": "https://res.cloudinary.com/odysseytraveller/image/fetch/f_auto,q_auto,dpr_auto,r_4,w_765,h_535.5,c_limit/https://cdn.odysseytraveller.com/app/uploads/2018/04/Registan-Square-Samarkand-1.jpg",  # Replace with the actual URL
        "caption": "The Registan in Samarkand, a historic and architectural marvel."
    },
    "Turkmenistan": {
        "capital": "Ashgabat",
        "description": "Turkmenistan is known for its rich history, unique culture, and beautiful landscapes. It is a country in Central Asia with a rich cultural heritage and unique traditions.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzMm0Hphb4yzJxhqINy7rke9tgBLPMEivxyg&s",  # Replace with the actual URL
        "caption": "The white marble city of Ashgabat, known for its grand architecture."
    },
    "Kyrgyzstan": {
        "capital": "Bishkek",
        "description": "Kyrgyzstan is known for its stunning mountains, rich culture, and vibrant traditions. It is a country in Central Asia with a strong nomadic heritage.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_NbNLv3GVOlvAi9XZd8buT9s4bjULtz2VTg&s",  # Replace with the actual URL
        "caption": "The picturesque mountains and lakes of Kyrgyzstan."
    },
    "Tajikistan": {
        "capital": "Dushanbe",
        "description": "Tajikistan is famous for its beautiful landscapes, rich history, and vibrant culture. It is a mountainous country in Central Asia with a rich cultural heritage.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6rfWdF9qT6MV945Q9iQsMfmEdnc7csh4bug&s",  # Replace with the actual URL
        "caption": "The Pamir Mountains, known as the 'Roof of the World'."
    },
    "Afghanistan": {
        "capital": "Kabul",
        "description": "Afghanistan is known for its rich history, diverse culture, and beautiful landscapes. It is a country with a complex history and a unique cultural heritage.",
        "image": "URL_https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsEnqW-woXmx6Z1YSr1eDcqkE5Y2sKrnjHeA&sTO_IMAGE",  # Replace with the actual URL
        "caption": "The historic city of Herat, known for its beautiful architecture."
    },
    "Pakistan": {
        "capital": "Islamabad",
        "description": "Pakistan is known for its rich cultural heritage, beautiful landscapes, and vibrant traditions. It is a country with a diverse population and a unique cultural identity.",
        "image": "https://images.pexels.com/photos/12912453/pexels-photo-12912453.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",  # Replace with the actual URL
        "caption": "The Badshahi Mosque in Lahore, a symbol of Pakistan's rich history."
    },
    "India": {
        "capital": "New Delhi",
        "description": "India is famous for its rich cultural heritage, diverse cuisine, and beautiful landscapes. It is the world's largest democracy and has a diverse population with a unique blend of cultures.",
        "image": "https://skift.com/wp-content/uploads/2022/06/GettyImages-1208049833-scaled-e1654782377122.jpg",  # Replace with the actual URL
        "caption": "The Taj Mahal, an iconic symbol of India's rich history and culture."
    },
    "Bangladesh": {
        "capital": "Dhaka",
        "description": "Bangladesh is known for its rich cultural heritage, vibrant traditions, and beautiful landscapes. It is a country in South Asia with a unique cultural identity and a strong sense of community.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsGQ71TfmfUTZJJUqHn7mxmHBwz5T6eyfM1A&s",  # Replace with the actual URL
        "caption": "The Sundarbans, the largest mangrove forest in the world and a UNESCO World Heritage site."
    },
    "Sri Lanka": {
        "capital": "Colombo",
        "description": "Sri Lanka is famous for its rich history, beautiful beaches, and vibrant culture. It is an island nation in South Asia with a unique cultural heritage and a strong sense of community.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Beauty_of_Sigiriya_by_Binuka.jpg",  # Replace with the actual URL
        "caption": "The ancient city of Sigiriya, known for its iconic rock fortress."
    },
    "Nepal": {
        "capital": "Kathmandu",
        "description": "Nepal is known for its stunning mountains, rich culture, and vibrant traditions. It is home to the highest peaks in the world, including Mount Everest.",
        "image": "https://cdn.britannica.com/17/83817-050-67C814CD/Mount-Everest.jpg",  # Replace with the actual URL
        "caption": "Mount Everest, the highest peak in the world, located in the Himalayas."
    },
    "Bhutan": {
        "capital": "Thimphu",
        "description": "Bhutan is known for its stunning landscapes, rich culture, and unique traditions. It is a small Himalayan kingdom with a strong emphasis on happiness and well-being.",
        "image": "https://www.acethehimalaya.com/wp-content/uploads/2023/02/tigers-nest-bhutan.jpg",  # Replace with the actual URL
        "caption": "The Tiger's Nest Monastery, a sacred site perched on a cliffside."
    },
    "Maldives": {
        "capital": "Malé",
        "description": "The Maldives is famous for its stunning beaches, clear blue waters, and vibrant marine life. It is a tropical paradise known for its luxury resorts and beautiful coral reefs.",
        "image": "https://media.cnn.com/api/v1/images/stellar/prod/220707113925-17-maldives-best-overwater-villas-velaa.jpg?c=original",  # Replace with the actual URL
        "caption": "The beautiful overwater bungalows and clear waters of the Maldives."
    },
    "China": {
        "capital": "Beijing",
        "description": "China is known for its rich history, diverse culture, and beautiful landscapes. It is the world's most populous country and has a unique cultural heritage.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtNXXVwsBCDC30yJnztyh4v4816j4VP4o8XQ&s",  # Replace with the actual URL
        "caption": "The Great Wall of China, one of the most iconic landmarks in the world."
    },
    "Japan": {
        "capital": "Tokyo",
        "description": "Japan is famous for its rich cultural heritage, advanced technology, and beautiful landscapes. It is known for its unique blend of traditional and modern influences.",
        "image": "https://res.cloudinary.com/jnto/image/upload/w_750,h_503,fl_lossy,f_auto/v1531981666/fujiguide/SG010_6",  # Replace with the actual URL
        "caption": "Mount Fuji, an iconic symbol of Japan."
    },
    "South Korea": {
        "capital": "Seoul",
        "description": "South Korea is known for its rich cultural heritage, vibrant pop culture, and advanced technology. It is a country with a unique blend of traditional and modern influences.",
        "image": "https://ucarecdn.com/2667d034-3197-4c39-b162-579a4e2e583a/-/crop/1920x1007/0,72/-/resize/1200x630/-/resize/x300/",  # Replace with the actual URL
        "caption": "The Gyeongbokgung Palace in Seoul, a symbol of South Korea's rich history."
    },
    "North Korea": {
        "capital": "Pyongyang",
        "description": "North Korea is known for its strict government, unique culture, and complex history. It is one of the most isolated countries in the world.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAUHTStLbbpAW9l4cI4XoGSUtphsnU6Zcv5g&s",  # Replace with the actual URL
        "caption": "The Juche Tower in Pyongyang, a symbol of North Korean ideology."
    },
    "Mongolia": {
        "capital": "Ulaanbaatar",
        "description": "Mongolia is known for its vast steppes, rich history, and nomadic culture. It is a landlocked country in East Asia with a unique cultural heritage.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUYPyTBnBy_LK1bUgBnzw8WOZ3KNw2mqgtTA&s",  # Replace with the actual URL
        "caption": "The vast steppes of Mongolia, home to a rich nomadic tradition."
    },
    "Vietnam": {
        "capital": "Hanoi",
        "description": "Vietnam is known for its rich history, vibrant culture, and beautiful landscapes. It is a country in Southeast Asia with a unique blend of traditions and modern influences.",
        "image": "https://media.tacdn.com/media/attractions-splice-spp-674x446/12/3f/40/63.jpg",  # Replace with the actual URL
        "caption": "Ha Long Bay, a UNESCO World Heritage site known for its stunning limestone karsts."
    },
    "Thailand": {
        "capital": "Bangkok",
        "description": "Thailand is famous for its beautiful beaches, rich culture, and delicious cuisine. It is a popular tourist destination known for its vibrant cities and stunning landscapes.",
        "image": "https://img.traveltriangle.com/blog/wp-content/uploads/2018/08/cover-image-the-grand-palace.jpg",  # Replace with the actual URL
        "caption": "The Grand Palace in Bangkok, a symbol of Thailand's rich history and culture."
    },
    "Cambodia": {
        "capital": "Phnom Penh",
        "description": "Cambodia is known for its rich history, beautiful temples, and vibrant culture. It is home to the famous Angkor Wat, one of the largest religious monuments in the world.",
        "image": "https://media.tacdn.com/media/attractions-splice-spp-674x446/12/3f/5c/aa.jpg",  # Replace with the actual URL
        "caption": "Angkor Wat, a UNESCO World Heritage site and iconic symbol of Cambodia."
    },
    "Laos": {
        "capital": "Vientiane",
        "description": "Laos is known for its rich culture, beautiful landscapes, and vibrant traditions. It is a landlocked country in Southeast Asia with a unique cultural heritage.",
        "image": "https://media.tacdn.com/media/attractions-splice-spp-674x446/07/b1/f5/33.jpg",  # Replace with the actual URL
        "caption": "The historic city of Luang Prabang, a UNESCO World Heritage site."
    },
    "Myanmar": {
        "capital": "Naypyidaw",
        "description": "Myanmar is known for its rich history, beautiful landscapes, and vibrant culture. It is a country with a diverse population and a unique cultural heritage.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAId8E37gzsZjZPBromhRvuv6Lz8qQWOHrug&s",  # Replace with the actual URL
        "caption": "The ancient city of Bagan, known for its thousands of pagodas and temples."
    },
    "Philippines": {
        "capital": "Manila",
        "description": "The Philippines is famous for its beautiful beaches, rich culture, and vibrant traditions. It is an archipelago with a diverse population and a unique blend of cultures.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLTzS8Iv5Crqv8dRoKZ3Po2B0vb2rGc3QCOw&s",  # Replace with the actual URL
        "caption": "The stunning white sand beaches of Boracay, a popular tourist destination."
    },
    "Malaysia": {
        "capital": "Kuala Lumpur",
        "description": "Malaysia is known for its rich cultural heritage, diverse cuisine, and beautiful landscapes. It is a country with a unique blend of Malay, Chinese, Indian, and indigenous influences.",
        "image": "https://www.retalkasia.com/sites/default/files/styles/article-full/public/pexels-photo-462671.jpeg?itok=9md87QSN",  # Replace with the actual URL
        "caption": "The iconic Petronas Towers in Kuala Lumpur, a symbol of modern Malaysia."
    },
    "Singapore": {
        "capital": "Singapore",
        "description": "Singapore is famous for its modern skyline, clean streets, and vibrant culture. It is a global financial hub and a melting pot of cultures.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhEWRQ1gaTwV8XT7Ads86YKdM0xJmoFLXTgw&s",  # Replace with the actual URL
        "caption": "The Marina Bay Sands, a symbol of Singapore's modernity and innovation."
    },
    "Indonesia": {
        "capital": "Jakarta",
        "description": "Indonesia is known for its rich cultural heritage, diverse landscapes, and vibrant traditions. It is the largest archipelago in the world and has a diverse population.",
        "image": "https://d3hne3c382ip58.cloudfront.net/files/uploads/bookmundi/resized/cmsfeatured/pura-tanah-lot-temple-1529401896-785X440.jpg",  # Replace with the actual URL
        "caption": "The beautiful beaches and temples of Bali, a popular tourist destination."
    },
    "Brunei": {
        "capital": "Bandar Seri Begawan",
        "description": "Brunei is known for its rich cultural heritage, beautiful mosques, and vibrant traditions. It is a small but wealthy country in Southeast Asia with a unique blend of Malay, Chinese, and indigenous influences.",
        "image": "https://f7c7358c.rocketcdn.me/wp-content/uploads/2020/01/SOAS-sunset-690x400.jpg",  # Replace with the actual URL
        "caption": "The Sultan Omar Ali Saifuddien Mosque, a symbol of Brunei's Islamic heritage."
    },
    "East Timor": {
        "capital": "Dili",
        "description": "East Timor is known for its rich cultural heritage, beautiful landscapes, and vibrant traditions. It is a small country in Southeast Asia with a unique blend of Portuguese and indigenous influences.",
        "image": "https://www.intrepidtravel.com/v3/assets/blt0de87ff52d9c34a8/blt0711c8f0e0f4561f/6454482a50fd952be61ae434/Intrepid_Travel-Timor_Leste-Atauro_Akrema_-_Timor-Leste_DK_2013.jpg",  # Replace with the actual URL
        "caption": "The stunning beaches and coral reefs of East Timor, a paradise for divers."
    },
    "Australia": {
        "capital": "Canberra",
        "description": "Australia is famous for its unique wildlife, stunning landscapes, and vibrant culture. It is a vast country with a diverse population and a rich cultural heritage.",
        "image": "https://www.tripsavvy.com/thmb/k39AA6dtCIbao7bsVyy5HDz7AJo=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/OperaHouse-755d893182dc4811b608eb1a99792fd7.jpg",  # Replace with the actual URL
        "caption": "The Sydney Opera House, an iconic symbol of Australia."
    },
    "New Zealand": {
        "capital": "Wellington",
        "description": "New Zealand is known for its stunning landscapes, rich culture, and vibrant traditions. It is a country with a diverse population and a strong Maori heritage.",
        "image": "https://www.theroadtrip.co.nz/wp-content/uploads/2024/04/picturesque-milford-sound.jpg",  # Replace with the actual URL
        "caption": "The breathtaking landscapes of New Zealand, known for its natural beauty."
    },
    "Papua New Guinea": {
        "capital": "Port Moresby",
        "description": "Papua New Guinea is known for its rich cultural heritage, beautiful landscapes, and vibrant traditions. It is a country with a diverse population and a unique blend of Melanesian, Polynesian, and Micronesian influences.",
        "image": "https://coraltriangleadventures.com/wp-content/uploads/2021/04/Kimbe-Island-reef-PNG.jpg",  # Replace with the actual URL
        "caption": "The beautiful coral reefs and diverse marine life of Papua New Guinea."
    },
    "Fiji": {
        "capital": "Suva",
        "description": "Fiji is famous for its beautiful beaches, rich culture, and vibrant traditions. It is an island nation in the South Pacific with a unique blend of indigenous, Indian, and European influences.",
        "image": "https://destinationlesstravel.com/wp-content/uploads/2021/11/Horseshoe-Bay-Matagi-Island-1024x683.jpg.webp",  # Replace with the actual URL
        "caption": "The stunning beaches and crystal-clear waters of Fiji, a popular tourist destination."
    },
    "Samoa": {
        "capital": "Apia",
        "description": "Samoa is known for its rich cultural heritage, beautiful landscapes, and vibrant traditions. It is an island nation in the South Pacific with a unique blend of Polynesian and European influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMJDlegIEAxXiGwh-mq9TvVZYCPqgm-kNAwg&s",  # Replace with the actual URL
        "caption": "The beautiful beaches and lush landscapes of Samoa, known for its natural beauty."
    },
    "Tonga": {
        "capital": "Nuku'alofa",
        "description": "Tonga is known for its rich cultural heritage, beautiful landscapes, and vibrant traditions. It is an island nation in the South Pacific with a unique blend of Polynesian and European influences.",
        "image": "https://i1.wp.com/www.nhfaithfusion.com/wp-content/uploads/2013/12/Tonga-1.jpg?fit=1006%2C655&ssl=1",  # Replace with the actual URL
        "caption": "The beautiful beaches and crystal-clear waters of Tonga, a popular tourist destination."
    },
    "Vanuatu": {
        "capital": "Port Vila",
        "description": "Vanuatu is known for its rich cultural heritage, beautiful landscapes, and vibrant traditions. It is an island nation in the South Pacific with a unique blend of Melanesian and European influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7fGCiyuV20tFHYviDAjDDiAM3Gg2aA1Kgcg&s",  # Replace with the actual URL
        "caption": "The beautiful beaches and coral reefs of Vanuatu, a paradise for divers."
    },
    "Solomon Islands": {
        "capital": "Honiara",
        "description": "The Solomon Islands are known for their rich cultural heritage, beautiful landscapes, and vibrant traditions. It is an island nation in the South Pacific with a unique blend of Melanesian and European influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLh388r9zLu9vEvOzK6antl5PAoBPW30AWTw&s",  # Replace with the actual URL
        "caption": "The beautiful beaches and crystal-clear waters of the Solomon Islands, known for their natural beauty."
    },
    "Micronesia": {
        "capital": "Palikir",
        "description": "Micronesia is known for its rich cultural heritage, beautiful landscapes, and vibrant traditions. It is a region in the western Pacific Ocean with a unique blend of Micronesian and European influences.",
        "image": "https://natureconservancy-h.assetsadobe.com/is/image/content/dam/tnc/nature/en/photos/MicronesiaTaneSinclair-Taylor.jpg?crop=133%2C0%2C2133%2C1600&wid=640&hei=480&scl=3.3333333333333335",  # Replace with the actual URL
        "caption": "The beautiful coral reefs and diverse marine life of Micronesia, a paradise for divers."
    },
    "Palau": {
        "capital": "Ngerulmud",
        "description": "Palau is known for its rich cultural heritage, beautiful landscapes, and vibrant traditions. It is an island nation in the western Pacific Ocean with a unique blend of Micronesian and European influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWfKYv30popXLDQLT-Y4a_Jhv2HQ0Gl-28hA&s",  # Replace with the actual URL
        "caption": "The beautiful coral reefs and diverse marine life of Palau, a paradise for divers."
    },
    "Marshall Islands": {
        "capital": "Majuro",
        "description": "The Marshall Islands are known for their rich cultural heritage, beautiful landscapes, and vibrant traditions. It is an island nation in the central Pacific Ocean with a unique blend of Micronesian and European influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnQ0QT1SVmVUnVNtW78EzgvdIWfdSTgYYdZQ&s",  # Replace with the actual URL
        "caption": "The beautiful beaches and crystal-clear waters of the Marshall Islands, known for their natural beauty."
    },
    "Nauru": {
        "capital": "Yaren",
        "description": "Nauru is known for its rich cultural heritage, beautiful landscapes, and vibrant traditions. It is a small island nation in the central Pacific Ocean with a unique blend of Micronesian and European influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPXVZ9CekjykWK-daZj33FTOap0ERT_w18TA&s",  # Replace with the actual URL
        "caption": "The beautiful beaches and crystal-clear waters of Nauru, known for their natural beauty."
    },
    "Kiribati": {
        "capital": "Tarawa",
        "description": "Kiribati is known for its rich cultural heritage, beautiful landscapes, and vibrant traditions. It is an island nation in the central Pacific Ocean with a unique blend of Micronesian and European influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_-SOElm-UaTTieWpV2-l4XG5Gttv0ZmWU_Q&s",  # Replace with the actual URL
        "caption": "The beautiful beaches and crystal-clear waters of Kiribati, known for their natural beauty."
    },
    "Tuvalu": {
        "capital": "Funafuti",
        "description": "Tuvalu is known for its rich cultural heritage, beautiful landscapes, and vibrant traditions. It is a small island nation in the central Pacific Ocean with a unique blend of Polynesian and European influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfaDsJO06Lc_ogNOiiXpXZ7zQCI_USFYUucQ&s",  # Replace with the actual URL
        "caption": "The beautiful beaches and crystal-clear waters of Tuvalu, known for their natural beauty."
    },
    "Andorra": {
        "capital": "Andorra la Vella",
        "description": "Andorra is known for its beautiful mountain landscapes, rich cultural heritage, and vibrant traditions. It is a small principality in the Pyrenees Mountains between France and Spain.",
        "image": "https://media.istockphoto.com/id/1995243181/photo/mountains-landscape-in-autumn-view-of-arable-fields-in-the-valley-and-mountain-ridge-covered.jpg?s=612x612&w=0&k=20&c=HdaLoqjxF_Wo18038gLHrKhrXJ4NescryhaLXzubAYo=",  # Replace with the actual URL
        "caption": "The picturesque mountain landscapes of Andorra, known for their natural beauty."
    },
    "Monaco": {
        "capital": "Monaco",
        "description": "Monaco is known for its luxury, beautiful coastline, and vibrant culture. It is a small city-state on the French Riviera, famous for its casinos, yacht-lined harbor, and prestigious Grand Prix.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8Bx2H0d3Q6UjmE1wbyITidAzgBFDRx4yOvA&s",  # Replace with the actual URL
        "caption": "The luxurious Monte Carlo Casino, a symbol of Monaco's glamour and wealth."
    },
    "San Marino": {
        "capital": "San Marino",
        "description": "San Marino is known for its rich history, beautiful landscapes, and vibrant traditions. It is one of the world's oldest republics, located on the Italian Peninsula.",
        "image": "https://i.insider.com/5bd8bf8048eb1234850f47c8?width=700",  # Replace with the actual URL
        "caption": "The picturesque medieval city of San Marino, known for its historic architecture."
    },
    "Liechtenstein": {
        "capital": "Vaduz",
        "description": "Liechtenstein is known for its beautiful mountain landscapes, rich cultural heritage, and vibrant traditions. It is a small principality in the Alps between Switzerland and Austria.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzupdJG-pcoIPuleUThhwWzonE_W2rxL5Ekg&s",  # Replace with the actual URL
        "caption": "The picturesque Vaduz Castle, a symbol of Liechtenstein's rich history and culture."
    },
    "Vatican City": {
        "capital": "Vatican City",
        "description": "Vatican City is known for its rich history, beautiful art, and religious significance. It is the smallest independent state in the world, located in the heart of Rome, Italy.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx-YffaeMaRco9q5-tNYGE47MMo2Kh_Lf4SA&s",  # Replace with the actual URL
        "caption": "St. Peter's Basilica, a symbol of Vatican City's religious and cultural importance."
    },
    "Saint Kitts and Nevis": {
        "capital": "Basseterre",
        "description": "Saint Kitts and Nevis is known for its beautiful beaches, rich culture, and vibrant traditions. It is a small island nation in the Caribbean with a unique blend of African, European, and indigenous influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpr4LMO7nuntkQsQE_bHey4Gtcu85Sn9noDw&s",  # Replace with the actual URL
        "caption": "The beautiful beaches and crystal-clear waters of Saint Kitts and Nevis, known for their natural beauty."
    },
    "Antigua and Barbuda": {
        "capital": "Saint John's",
        "description": "Antigua and Barbuda is known for its beautiful beaches, rich culture, and vibrant traditions. It is a small island nation in the Caribbean with a unique blend of African, European, and indigenous influences.",
        "image": "https://media.tacdn.com/media/attractions-content--1x-1/10/5a/8a/90.jpg",  # Replace with the actual URL
        "caption": "The beautiful beaches and crystal-clear waters of Antigua and Barbuda, known for their natural beauty."
    },
    "Saint Lucia": {
        "capital": "Castries",
        "description": "Saint Lucia is known for its beautiful beaches, rich culture, and vibrant traditions. It is a small island nation in the Caribbean with a unique blend of African, European, and indigenous influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRarCOm7BR870sSyVyW6NI6ia9dc3oMue0_0g&s",  # Replace with the actual URL
        "caption": "The stunning Pitons, a UNESCO World Heritage site and symbol of Saint Lucia's natural beauty."
    },
    "Saint Vincent and the Grenadines": {
        "capital": "Kingstown",
        "description": "Saint Vincent and the Grenadines is known for its beautiful beaches, rich culture, and vibrant traditions. It is a small island nation in the Caribbean with a unique blend of African, European, and indigenous influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs-1rSTbo6-reSuj6PXBvVpwKJFV_xoHLLSg&s",  # Replace with the actual URL
        "caption": "The beautiful beaches and crystal-clear waters of Saint Vincent and the Grenadines, known for their natural beauty."
    },
    "Barbados": {
        "capital": "Bridgetown",
        "description": "Barbados is known for its beautiful beaches, rich culture, and vibrant traditions. It is a small island nation in the Caribbean with a unique blend of African, European, and indigenous influences.",
        "image": "https://cdn.prod.website-files.com/5e93226606600f15bcd785e2/6546752296218ef7ce933567_Barbados-Bottom-Bay-2.jpeg",  # Replace with the actual URL
        "caption": "The beautiful beaches and crystal-clear waters of Barbados, known for their natural beauty."
    },
    "Grenada": {
        "capital": "Saint George's",
        "description": "Grenada is known for its beautiful beaches, rich culture, and vibrant traditions. It is a small island nation in the Caribbean with a unique blend of African, European, and indigenous influences.",
        "image": "https://ik.imagekit.io/gondolatravel/uploads/0893_C023_CA_77_44_A8_8_DED_0_A878262683_D_e71725fd58.JPG?tr=w-947,h-373,c-maintain_ratio,f-auto",  # Replace with the actual URL
        "caption": "The beautiful beaches and crystal-clear waters of Grenada, known for their natural beauty."
    },
    "Trinidad and Tobago": {
        "capital": "Port of Spain",
        "description": "Trinidad and Tobago is known for its rich culture, vibrant traditions, and beautiful landscapes. It is a small island nation in the Caribbean with a unique blend of African, Indian, European, and indigenous influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaBF-23VHaJQLKkRwaQGiS5Ey8KWy_cEm5ew&s",  # Replace with the actual URL
        "caption": "The beautiful beaches and vibrant culture of Trinidad and Tobago, known for their natural beauty."
    },
    "Bahamas": {
        "capital": "Nassau",
        "description": "The Bahamas is known for its beautiful beaches, rich culture, and vibrant traditions. It is a small island nation in the Caribbean with a unique blend of African, European, and indigenous influences.",
        "image": "https://images.squarespace-cdn.com/content/v1/6250a8d257a6e83aaad50c8e/07c6f3ac-524f-4771-88b1-7e695dab2e15/Worlds-Most-Crystal-Clear-Blue-Water-Beaches-4",  # Replace with the actual URL
        "caption": "The stunning beaches and crystal-clear waters of the Bahamas, known for their natural beauty."
    },
    "Cuba": {
        "capital": "Havana",
        "description": "Cuba is known for its rich culture, vibrant traditions, and beautiful landscapes. It is a Caribbean island nation with a unique blend of African, European, and indigenous influences.",
        "image": "https://media.architecturaldigest.com/photos/5797b51eb6c434ab487bc0c8/master/pass/GettyImages-148836251.jpg",  # Replace with the actual URL
        "caption": "The vibrant streets and historic architecture of Havana, a symbol of Cuba's rich cultural heritage."
    },
    "Jamaica": {
        "capital": "Kingston",
        "description": "Jamaica is known for its rich culture, vibrant music, and beautiful landscapes. It is a Caribbean island nation with a unique blend of African, European, and indigenous influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNe1KXvgJ7u46zGZIh5qJOg2tM2hqkMqhGAQ&s",  # Replace with the actual URL
        "caption": "The stunning beaches and lush landscapes of Jamaica, known for their natural beauty."
    },
    "Dominican Republic": {
        "capital": "Santo Domingo",
        "description": "The Dominican Republic is known for its beautiful beaches, rich culture, and vibrant traditions. It is a Caribbean island nation with a unique blend of African, European, and indigenous influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1j_t-xkWKjT6QVaNCAPZgLYbUxdYyV_zFUQ&s",  # Replace with the actual URL
        "caption": "The beautiful beaches and crystal-clear waters of the Dominican Republic, known for their natural beauty."
    },
    "Haiti": {
        "capital": "Port-au-Prince",
        "description": "Haiti is known for its rich culture, vibrant traditions, and beautiful landscapes. It is a Caribbean island nation with a unique blend of African, European, and indigenous influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_0vKHQiJGSkh83i4nUfi0NwaxNcsvR05ihw&s",  # Replace with the actual URL
        "caption": "The vibrant culture and stunning landscapes of Haiti, known for their natural beauty."
    },
    "Belize": {
        "capital": "Belmopan",
        "description": "Belize is known for its beautiful beaches, rich culture, and vibrant traditions. It is a small country in Central America with a unique blend of African, European, and indigenous influences.",
        "image": "https://www.hamanasi.com/wp-content/uploads/2023/06/2-lorenzoballarinphoto-20190413_025256_DSC_0264-1024x682.jpg",  # Replace with the actual URL
        "caption": "The stunning coral reefs and crystal-clear waters of Belize, known for their natural beauty."
    },
    "Guatemala": {
        "capital": "Guatemala City",
        "description": "Guatemala is known for its rich culture, vibrant traditions, and beautiful landscapes. It is a country in Central America with a unique blend of Mayan, Spanish, and indigenous influences.",
        "image": "https://cdn.adventure-life.com/50/19/1209426070d54loj/1300x820.webp",  # Replace with the actual URL
        "caption": "The ancient Mayan ruins of Tikal, a UNESCO World Heritage site and symbol of Guatemala's rich history."
    },
    "El Salvador": {
        "capital": "San Salvador",
        "description": "El Salvador is known for its rich culture, vibrant traditions, and beautiful landscapes. It is a country in Central America with a unique blend of indigenous, Spanish, and African influences.",
        "image": "https://nextvacay.com/wp-content/uploads/2023/05/image-85.png.webp",  # Replace with the actual URL
        "caption": "The beautiful beaches and lush landscapes of El Salvador, known for their natural beauty."
    },
    "Honduras": {
        "capital": "Tegucigalpa",
        "description": "Honduras is known for its rich culture, vibrant traditions, and beautiful landscapes. It is a country in Central America with a unique blend of indigenous, Spanish, and African influences.",
        "image": "https://live.staticflickr.com/65535/49999306891_4170a7c916_c.jpg",  # Replace with the actual URL
        "caption": "The ancient Mayan ruins of Copán, a UNESCO World Heritage site and symbol of Honduras' rich history."
    },
    "Nicaragua": {
        "capital": "Managua",
        "description": "Nicaragua is known for its rich culture, vibrant traditions, and beautiful landscapes. It is a country in Central America with a unique blend of indigenous, Spanish, and African influences.",
        "image": "https://roamwildtravel.com/cdn/shop/articles/beach_194365c2-0db0-444a-8937-5b77f4aafbb6.jpg?v=1645342453",  # Replace with the actual URL
        "caption": "The stunning beaches and crystal-clear waters of Nicaragua, known for their natural beauty."
    },
    "Costa Rica": {
        "capital": "San José",
        "description": "Costa Rica is known for its rich culture, vibrant traditions, and beautiful landscapes. It is a country in Central America with a unique blend of indigenous, Spanish, and African influences.",
        "image": "https://i0.wp.com/crie.cr/wp-content/uploads/2023/11/parks-in-Costa-Rica.jpg?fit=1344%2C768&ssl=1",  # Replace with the actual URL
        "caption": "The stunning beaches and lush rainforests of Costa Rica, known for their natural beauty."
    },
    "Panama": {
        "capital": "Panama City",
        "description": "Panama is known for its rich culture, vibrant traditions, and beautiful landscapes. It is a country in Central America with a unique blend of indigenous, Spanish, and African influences.",
        "image": "https://cdn.britannica.com/73/75873-050-D9FF99F9/tugboat-one-ship-locks-Panama-Canal.jpg",  # Replace with the actual URL
        "caption": "The iconic Panama Canal, a symbol of Panama's strategic importance and engineering marvel."
    },
    "Greenland": {
        "capital": "Nuuk",
        "description": "Greenland is known for its vast icy landscapes, rich culture, and unique traditions. It is the world's largest island, located in the Arctic region.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFG68YeYyaZ4aXkeLXnjz1OVOzfLGb7NpRoQ&s",  # Replace with the actual URL
        "caption": "The stunning icy landscapes of Greenland, known for their natural beauty."
    },
    "Iceland": {
        "capital": "Reykjavik",
        "description": "Iceland is known for its stunning landscapes, rich culture, and vibrant traditions. It is a country in the North Atlantic with a unique blend of Nordic and European influences.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR67IH0K2TdbrAicHMBQVMa1DU3HJ1fu5-wHw&s",  # Replace with the actual URL
        "caption": "The breathtaking landscapes of Iceland, known for their natural beauty."
    },
    "South Africa": {
        "capital": "Pretoria",
        "description": "South Africa is known for its diverse culture, beautiful landscapes, and vibrant cities.",
        "image": "https://www.capetown.travel/wp-content/uploads/best-views-of-table-mountain.jpg",  # Replace with the actual URL
        "caption": "A stunning view of Table Mountain in Cape Town, South Africa."
    },
    "Egypt": {
        "capital": "Cairo",
        "description": "Egypt is famous for its ancient civilization and some of the world's most famous monuments.",
        "image": "https://discovery.sndimg.com/content/dam/images/discovery/fullset/2022/10/Curiosity%20pyramids%20of%20giza%20GettyImages-1085205362.jpg.rend.hgtvcom.616.411.suffix/1665772906478.jpeg",  # Replace with the actual URL
        "caption": "The majestic pyramids of Giza in Egypt."
    },
    "Rwanda": {
        "capital": "Kigali",
        "description": "Rwanda is known as the 'Land of a Thousand Hills' and is famous for its mountain gorillas.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh9JgYkygINURHIYywkpg2WXrAzIxaXLc0Xw&s",  # Replace with the actual URL
        "caption": "The beautiful landscape of Rwanda."
    },
    "Kenya": {
        "capital": "Nairobi",
        "description": "Kenya is renowned for its wildlife reserves and diverse landscapes.",
        "image": "https://cdn.britannica.com/61/153461-050-3C2B54D7/Acacia-trees-Taita-Hills-Kenya.jpg",  # Replace with the actual URL
        "caption": "A safari adventure in the Maasai Mara, Kenya."
    },
    "Cameroon": {
        "capital": "Yaoundé",
        "description": "Cameroon is known for its cultural diversity and natural beauty.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQK3dmFYWyJYN1AgPda-qMwYpQnXFa2lzwUaQ&s",  # Replace with the actual URL
        "caption": "The rich cultural heritage of Cameroon."
    },
    "Nigeria": {
        "capital": "Abuja",
        "description": "Nigeria is known for its vibrant culture, music, and film industry.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQMDHC3nJ4kg43a_lXXAmszpb36DQqo00pkg&s",  # Replace with the actual URL
        "caption": "The bustling cityscape of Lagos, Nigeria."
    },
    "Senegal": {
        "capital": "Dakar",
        "description": "Senegal is known for its rich history, music, and vibrant arts scene.",
        "image": "https://cdn.britannica.com/16/152516-050-93DB4049/Goree-Island-Senegal.jpg",  # Replace with the actual URL
        "caption": "The colorful streets of Dakar, Senegal."
    },
    "Morocco": {
        "capital": "Rabat",
        "description": "Morocco is famous for its vibrant markets, rich history, and diverse landscapes.",
        "image": "https://media.gq-magazine.co.uk/photos/5d138f50976fa31476f39436/16:9/w_2560%2Cc_limit/marrakech-gq-9oct18_istock_b.jpg",  # Replace with the actual URL
        "caption": "The iconic architecture of Marrakech, Morocco."
    },
    "Mali": {
        "capital": "Bamako",
        "description": "Mali is known for its music, culture, and historic cities like Timbuktu.",
        "image": "https://cdn.britannica.com/16/178116-050-ADDA20CF/Mosque-Djenne-Mali.jpg",  # Replace with the actual URL
        "caption": "The cultural treasures of Mali."
    }    
}