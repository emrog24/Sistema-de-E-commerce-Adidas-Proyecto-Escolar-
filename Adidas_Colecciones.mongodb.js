// Coleccion de Productos
use ("Adidas")
db.A_productos.insertMany([
  {
    "nombre_producto": "Tenis Samba OG",
    "descripcion": "Un ícono de adidas Originals que trasciende décadas. Originalmente diseñados para canchas de fútbol sala.",
    "precio_mxn": 2399.00,
    "categoria": "Originals",
    "url_imagen_principal": "https://assets.adidas.com/images/w_1880,f_auto,q_auto/f9ce5733049f4ca8a93aa8bf011858bd_9366/B75806_09_standard.jpg",
    "tags_busqueda": ["samba", "retro", "clasico", "blanco", "terraza"]
  },
  {
    "nombre_producto": "Tenis Superstar",
    "descripcion": "Los legendarios tenis de la punta de concha. Un símbolo de la cultura hip-hop y el estilo urbano.",
    "precio_mxn": 2499.00,
    "categoria": "Originals",
    "url_imagen_principal": "https://assets.adidas.com/images/w_1880,f_auto,q_auto/815f971f57d840b191f3ab2f017d240c_9366/FU7714_09_standard.jpg",
    "tags_busqueda": ["superstar", "clasico", "punta de concha", "blanco", "urbano"]
  },
  {
    "nombre_producto": "Tenis Ultraboost Light",
    "descripcion": "Tenis de running con el retorno de energía de BOOST. La versión más ligera hasta la fecha.",
    "precio_mxn": 4299.00,
    "categoria": "Running",
    "url_imagen_principal": "https://assets.adidas.com/images/w_940,f_auto,q_auto/c4b1b34cd9b14b81bbdaaf7b00a219c2_9366/GZ5159_09_standard.jpg",
    "tags_busqueda": ["running", "boost", "confort", "maraton", "ligero"]
  },
  {
    "nombre_producto": "Tenis Gazelle",
    "descripcion": "Una reedición fiel de los Gazelle de 1991, con los mismos materiales y colores.",
    "precio_mxn": 2299.00,
    "categoria": "Originals",
    "url_imagen_principal": "https://assets.adidas.com/images/w_1880,f_auto,q_auto/f11bb7c3cdf84ba4b999266e14726711_9366/IF3817_09_standard.jpg",
    "tags_busqueda": ["gazelle", "retro", "suede", "clasico", "gamuza"]
  },
  {
    "nombre_producto": "Jersey Local 23/24 Real Madrid",
    "descripcion": "Jersey oficial del Real Madrid para la temporada 23/24, con tecnología AEROREADY.",
    "precio_mxn": 2199.00,
    "categoria": "Football",
    "url_imagen_principal": "https://assets.adidas.com/images/w_1880,f_auto,q_auto/f952f4fc563e4cf8b22dafbb008fe903_9366/IB0011_01_laydown.jpg",
    "tags_busqueda": ["futbol", "real madrid", "jersey", "blanco", "laliga"]
  },
  {
    "nombre_producto": "Pants Tiro 23",
    "descripcion": "Pants de entrenamiento cónicos, perfectos para el calentamiento o el uso diario.",
    "precio_mxn": 1299.00,
    "categoria": "Sportswear",
    "url_imagen_principal": "https://assets.adidas.com/images/w_600,f_auto,q_auto/c09719a595b844a6b3c9aefa00b72810_9366/Tiro_23_League_Pants_Black_HS7232_01_laydown.jpg",
    "tags_busqueda": ["pants", "tiro", "futbol", "entrenamiento", "negro"]
  },
  {
    "nombre_producto": "Tenis Adizero Adios Pro 3",
    "descripcion": "Diseñados para la velocidad en maratones. Con varillas de carbono ENERGYRODS 2.0.",
    "precio_mxn": 5999.00,
    "categoria": "Running",
    "url_imagen_principal": "https://assets.adidas.com/images/w_940,f_auto,q_auto/ef072339d62c48acb18dae9900cebbfa_9366/GY8411_09_standard.jpg",
    "tags_busqueda": ["running", "competencia", "carbono", "maraton", "adizero"]
  },
  {
    "nombre_producto": "Sudadera con Gorro Essentials",
    "descripcion": "Un básico de fondo de armario. Sudadera cómoda de felpa francesa.",
    "precio_mxn": 1399.00,
    "categoria": "Sportswear",
    "url_imagen_principal": "https://assets.adidas.com/images/w_600,f_auto,q_auto/637b6c3bdcb74822a5fbacfc015bf06a_9366/Sudadera_con_Gorro_Adicolor_Essentials_Trifolio_Negro_H34652_01_laydown.jpg",
    "tags_busqueda": ["sudadera", "hoodie", "basico", "confort", "gris"]
  },
  {
    "nombre_producto": "Playera Team Mercedes-AMG Petronas F1 24",
    "descripcion": "Vístete como el equipo. Playera oficial del equipo Mercedes-AMG Petronas F1 para la temporada 2024, con logos de patrocinadores.",
    "precio_mxn": 1999.00,
    "categoria": "Motorsport",
    "url_imagen_principal": "https://assets.adidas.com/images/w_1880,f_auto,q_auto/efbfed3fc7db4272a42b8c85f814f5c7_9366/JW5363_01_laydown.jpg",
    "tags_busqueda": ["f1", "mercedes", "motorsport", "hamilton", "russell", "playera"]
  },
  {
    "nombre_producto": "Tenis Adidas x Mercedes F1 Ultraboost",
    "descripcion": "Edición especial de Ultraboost. Combina el confort de BOOST con el diseño de alta tecnología y los colores de Mercedes F1.",
    "precio_mxn": 4999.00,
    "categoria": "Motorsport",
    "url_imagen_principal": "https://assets.adidas.com/images/w_1880,f_auto,q_auto/db62528bea244fe1a7b565254ab20c99_9366/JQ3272_09_standard.jpg",
    "tags_busqueda": ["f1", "mercedes", "ultraboost", "edicion especial", "motorsport", "tenis"]
  },
  {
    "nombre_producto": "Gorra Team Mercedes-AMG Petronas F1 24",
    "descripcion": "Gorra oficial del equipo Mercedes F1. Muestra tu apoyo con el logo del equipo bordado y la estrella de Mercedes.",
    "precio_mxn": 1299.00,
    "categoria": "Motorsport",
    "url_imagen_principal": "https://www.tradeinn.com/f/14158/141580276/adidas-gorra-mercedes-amg-petronas-f1-team.webp",
    "tags_busqueda": ["f1", "mercedes", "gorra", "cap", "motorsport", "hamilton", "russell"]
  },
  {
    "nombre_producto": "Tenis Adidas x Bad Bunny Forum 'First Cafe'",
    "descripcion": "El inicio de la colaboración. Un rediseño del clásico Forum con detalles únicos como la doble lengüeta, el broche de correa y el logo 'El Ojo'.",
    "precio_mxn": 5499.00,
    "categoria": "Originals",
    "url_imagen_principal": "https://modozapatillas.com/upload/productos/galeria/normal/adidas-forum-the-first-cafe-x-bad-bunny-modelo-102m-ec6add58983ece9b953f7a3dc04248f2.jpg",
    "tags_busqueda": ["bad bunny", "forum", "cafe", "colaboracion", "el ojo", "urbano", "benito"]
  },
  {
    "nombre_producto": "Tenis Adidas x Bad Bunny Response CL 'Paso Fino'",
    "descripcion": "Inspirados en el estilo western y el senderismo. Presentan una malla 'derretida' sobre las franjas de Adidas y un look robusto.",
    "precio_mxn": 4199.00,
    "categoria": "Originals",
    "url_imagen_principal": "https://sneakerbardetroit.com/wp-content/uploads/2023/09/Bad-Bunny-adidas-Response-CL-Ecru-Tint-ID0780-Release-Info-2-1068x983.jpeg",
    "tags_busqueda": ["bad bunny", "response cl", "colaboracion", "paso fino", "urbano", "benito"]
  },
  {
    "nombre_producto": "Tenis Adidas x Bad Bunny Campus 'Brown'",
    "descripcion": "Una versión del Campus con proporciones exageradas, doble lengüeta y un cuello acolchado. Inspirado en el skate de los 2000.",
    "precio_mxn": 3999.00,
    "categoria": "Originals",
    "url_imagen_principal": "https://sneakernews.com/wp-content/uploads/2023/07/bad-bunny-adidas-campus-brown-ID2529-release-date-5.jpg",
    "tags_busqueda": ["bad bunny", "campus", "brown", "colaboracion", "skate", "urbano", "benito"]
  },
  {
    "nombre_producto": "Tenis Forum Low",
    "descripcion": "El ícono del básquetbol de los 80 regresa a las calles. Con su distintiva tira en X.",
    "precio_mxn": 2599.00,
    "categoria": "Originals",
    "url_imagen_principal": "https://assets.adidas.com/images/w_600,f_auto,q_auto/4a90c9d7ac2341f09516af2a00d61370_9366/Tenis_Forum_Low_Cinza_HQ1506_09_standard.jpg",
    "tags_busqueda": ["forum", "retro", "basketball", "blanco", "clasico"]
  },
  {
    "nombre_producto": "Shorts Woven Training",
    "descripcion": "Shorts ligeros y elásticos diseñados para el movimiento en el gimnasio.",
    "precio_mxn": 899.00,
    "categoria": "Training",
    "url_imagen_principal": "https://assets.adidas.com/images/w_1880,f_auto,q_auto/cd428faafcc54b0a8ea4af4f0155af9b_9366/IC6976_01_laydown.jpg",
    "tags_busqueda": ["shorts", "training", "gimnasio", "ligero", "negro"]
  },
  {
    "nombre_producto": "Tenis Supernova 3",
    "descripcion": "Tenis de running para el entrenamiento diario, con equilibrio entre Bounce y BOOST.",
    "precio_mxn": 2799.00,
    "categoria": "Running",
    "url_imagen_principal": "https://images.tcdn.com.br/img/img_prod/817109/tenis_de_corrida_supernova_3_masculino_27019_2_49be21d1befdd26be78bcaf797879718.jpg",
    "tags_busqueda": ["running", "diario", "confort", "boost", "entrenamiento"]
  },
  {
    "nombre_producto": "Tachos X Crazyfast.1",
    "descripcion": "Diseñados para una velocidad extrema. Ligeros y con gran agarre.",
    "precio_mxn": 5499.00,
    "categoria": "Football",
    "url_imagen_principal": "https://niveks.com/wp-content/uploads/2023/12/CrazyfastCana.jpeg",
    "tags_busqueda": ["futbol", "tachos", "x", "velocidad", "ligero"]
  },
  {
    "nombre_producto": "Chamarra Rompevientos Adicolor",
    "descripcion": "Chamarra clásica con el icónico Trifolio. Hecha de materiales reciclados.",
    "precio_mxn": 1899.00,
    "categoria": "Originals",
    "url_imagen_principal": "https://assets.adidas.com/images/w_600,f_auto,q_auto/92734009497e47fc8832ac84002a029f_9366/Rompevientos_Adicolor_Classics_Negro_GN2780_01_laydown.jpg",
    "tags_busqueda": ["chamarra", "adicolor", "trifolio", "clasico", "rompevientos"]
  },
  {
    "nombre_producto": "Jersey Visitante 23/24 Selección Mexicana",
    "descripcion": "Jersey de visitante de la Selección Nacional de México, inspirado en el arte prehispánico.",
    "precio_mxn": 1999.00,
    "categoria": "Football",
    "url_imagen_principal": "https://dpjye2wk9gi5z.cloudfront.net/wcsstore/ExtendedSitesCatalogAssetStore/images/catalog/zoom/3018317-0105V1.jpg",
    "tags_busqueda": ["futbol", "mexico", "jersey", "seleccion", "verde"]
  }
]);

// Coleccion de Inventario
use("Adidas")
// de Inicio se crearan 4 variantes por producto, en la cual se cambiara la talla y/o el color
db.A_inventario.insertMany([
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf68"), "sku": "B75806-8.5", "talla_us": "8.5", "color": "Cloud White / Core Black", "cantidad_stock": 20 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf68"), "sku": "B75806-9.0", "talla_us": "9.0", "color": "Cloud White / Core Black", "cantidad_stock": 40 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf68"), "sku": "B75806-9.5", "talla_us": "9.5", "color": "Cloud White / Core Black", "cantidad_stock": 55 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf68"), "sku": "B75806-10.0", "talla_us": "10.0", "color": "Cloud White / Core Black", "cantidad_stock": 30 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf69"), "sku": "FU7714-8.0", "talla_us": "8.0", "color": "Cloud White / Core Black", "cantidad_stock": 25 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf69"), "sku": "FU7714-8.5", "talla_us": "8.5", "color": "Cloud White / Core Black", "cantidad_stock": 60 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf69"), "sku": "FU7714-9.0", "talla_us": "9.0", "color": "Cloud White / Core Black", "cantidad_stock": 70 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf69"), "sku": "FU7714-9.5", "talla_us": "9.5", "color": "Cloud White / Core Black", "cantidad_stock": 40 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6a"), "sku": "GZ5159-9.0", "talla_us": "9.0", "color": "Core Black / Core Black", "cantidad_stock": 30 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6a"), "sku": "GZ5159-9.5", "talla_us": "9.5", "color": "Core Black / Core Black", "cantidad_stock": 40 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6a"), "sku": "GZ5159-10.0", "talla_us": "10.0", "color": "Core Black / Core Black", "cantidad_stock": 25 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6a"), "sku": "GZ5159-10.5", "talla_us": "10.5", "color": "Core Black / Core Black", "cantidad_stock": 15 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6b"), "sku": "IF3817-8.0", "talla_us": "8.0", "color": "Core Black / White", "cantidad_stock": 45 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6b"), "sku": "IF3817-8.5", "talla_us": "8.5", "color": "Core Black / White", "cantidad_stock": 35 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6b"), "sku": "IF3817-9.0", "talla_us": "9.0", "color": "Core Black / White", "cantidad_stock": 30 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6b"), "sku": "IF3817-9.5", "talla_us": "9.5", "color": "Core Black / White", "cantidad_stock": 20 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6c"), "sku": "IB0011-S", "talla_us": "S", "color": "White", "cantidad_stock": 60 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6c"), "sku": "IB0011-M", "talla_us": "M", "color": "White", "cantidad_stock": 80 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6c"), "sku": "IB0011-L", "talla_us": "L", "color": "White", "cantidad_stock": 50 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6c"), "sku": "IB0011-XL", "talla_us": "XL", "color": "White", "cantidad_stock": 30 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6d"), "sku": "HS7232-S", "talla_us": "S", "color": "Black / White", "cantidad_stock": 80 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6d"), "sku": "HS7232-M", "talla_us": "M", "color": "Black / White", "cantidad_stock": 100 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6d"), "sku": "HS7232-L", "talla_us": "L", "color": "Black / White", "cantidad_stock": 70 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6d"), "sku": "HS7232-XL", "talla_us": "XL", "color": "Black / White", "cantidad_stock": 40 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6e"), "sku": "GY8411-9.0", "talla_us": "9.0", "color": "Wonder Blue / Cyber Spike", "cantidad_stock": 22 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6e"), "sku": "GY8411-9.5", "talla_us": "9.5", "color": "Wonder Blue / Cyber Spike", "cantidad_stock": 12 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6e"), "sku": "GY8411-10.0", "talla_us": "10.0", "color": "Wonder Blue / Cyber Spike", "cantidad_stock": 15 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6e"), "sku": "GY8411-10.5", "talla_us": "10.5", "color": "Wonder Blue / Cyber Spike", "cantidad_stock": 10 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6f"), "sku": "H34652-S", "talla_us": "S", "color": "Negro", "cantidad_stock": 60 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6f"), "sku": "H34652-M", "talla_us": "M", "color": "Negro", "cantidad_stock": 85 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6f"), "sku": "H34652-L", "talla_us": "L", "color": "Negro", "cantidad_stock": 75 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf6f"), "sku": "H34652-XL", "talla_us": "XL", "color": "Negro", "cantidad_stock": 50 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf70"), "sku": "JW5363-S", "talla_us": "S", "color": "Black", "cantidad_stock": 50 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf70"), "sku": "JW5363-M", "talla_us": "M", "color": "Black", "cantidad_stock": 60 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf70"), "sku": "JW5363-L", "talla_us": "L", "color": "Black", "cantidad_stock": 40 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf70"), "sku": "JW5363-XL", "talla_us": "XL", "color": "Black", "cantidad_stock": 20 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf71"), "sku": "JQ3272-8.5", "talla_us": "8.5", "color": "Core Black / Silver", "cantidad_stock": 15 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf71"), "sku": "JQ3272-9.0", "talla_us": "9.0", "color": "Core Black / Silver", "cantidad_stock": 25 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf71"), "sku": "JQ3272-9.5", "talla_us": "9.5", "color": "Core Black / Silver", "cantidad_stock": 20 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf71"), "sku": "JQ3272-10.0", "talla_us": "10.0", "color": "Core Black / Silver", "cantidad_stock": 10 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf72"), "sku": "HT9911-BLK", "talla_us": "Unitalla", "color": "Black", "cantidad_stock": 90 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf72"), "sku": "HT9911-WHT", "talla_us": "Unitalla", "color": "White", "cantidad_stock": 50 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf72"), "sku": "HT9911-GRN", "talla_us": "Unitalla", "color": "Petronas Green", "cantidad_stock": 30 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf72"), "sku": "HT9911-GRY", "talla_us": "Unitalla", "color": "Grey", "cantidad_stock": 45 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf73"), "sku": "GW0264-8.5", "talla_us": "8.5", "color": "Cardboard / Supplier Colour", "cantidad_stock": 12 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf73"), "sku": "GW0264-9.0", "talla_us": "9.0", "color": "Cardboard / Supplier Colour", "cantidad_stock": 10 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf73"), "sku": "GW0264-9.5", "talla_us": "9.5", "color": "Cardboard / Supplier Colour", "cantidad_stock": 5 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf73"), "sku": "GW0264-10.0", "talla_us": "10.0", "color": "Cardboard / Supplier Colour", "cantidad_stock": 7 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf74"), "sku": "ID0780-9.0", "talla_us": "9.0", "color": "Ecru Tint / Sand", "cantidad_stock": 25 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf74"), "sku": "ID0780-9.5", "talla_us": "9.5", "color": "Ecru Tint / Sand", "cantidad_stock": 30 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf74"), "sku": "ID0780-10.0", "talla_us": "10.0", "color": "Ecru Tint / Sand", "cantidad_stock": 20 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf74"), "sku": "ID0780-10.5", "talla_us": "10.5", "color": "Ecru Tint / Sand", "cantidad_stock": 15 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf75"), "sku": "ID2529-8.5", "talla_us": "8.5", "color": "Brown / Sand", "cantidad_stock": 18 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf75"), "sku": "ID2529-9.0", "talla_us": "9.0", "color": "Brown / Sand", "cantidad_stock": 22 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf75"), "sku": "ID2529-9.5", "talla_us": "9.5", "color": "Brown / Sand", "cantidad_stock": 20 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf75"), "sku": "ID2529-10.0", "talla_us": "10.0", "color": "Brown / Sand", "cantidad_stock": 10 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf76"), "sku": "HQ1506-8.0", "talla_us": "8.0", "color": "Grey / White", "cantidad_stock": 30 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf76"), "sku": "HQ1506-8.5", "talla_us": "8.5", "color": "Grey / White", "cantidad_stock": 40 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf76"), "sku": "HQ1506-9.0", "talla_us": "9.0", "color": "Grey / White", "cantidad_stock": 35 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf76"), "sku": "HQ1506-9.5", "talla_us": "9.5", "color": "Grey / White", "cantidad_stock": 20 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf77"), "sku": "IC6976-S", "talla_us": "S", "color": "Black", "cantidad_stock": 50 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf77"), "sku": "IC6976-M", "talla_us": "M", "color": "Black", "cantidad_stock": 60 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf77"), "sku": "IC6976-L", "talla_us": "L", "color": "Black", "cantidad_stock": 55 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf77"), "sku": "IC6976-XL", "talla_us": "XL", "color": "Black", "cantidad_stock": 30 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf78"), "sku": "HP5938-9.0", "talla_us": "9.0", "color": "Cloud White / Core Black", "cantidad_stock": 35 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf78"), "sku": "HP5938-9.5", "talla_us": "9.5", "color": "Cloud White / Core Black", "cantidad_stock": 45 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf78"), "sku": "HP5938-10.0", "talla_us": "10.0", "color": "Cloud White / Core Black", "cantidad_stock": 40 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf78"), "sku": "HP5938-10.5", "talla_us": "10.5", "color": "Cloud White / Core Black", "cantidad_stock": 25 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf79"), "sku": "GY7390-8.5", "talla_us": "8.5", "color": "Solar Red / Cloud White", "cantidad_stock": 20 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf79"), "sku": "GY7390-9.0", "talla_us": "9.0", "color": "Solar Red / Cloud White", "cantidad_stock": 22 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf79"), "sku": "GY7390-9.5", "talla_us": "9.5", "color": "Solar Red / Cloud White", "cantidad_stock": 15 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf79"), "sku": "GY7390-10.0", "talla_us": "10.0", "color": "Solar Red / Cloud White", "cantidad_stock": 10 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf7a"), "sku": "GN2780-S", "talla_us": "S", "color": "Black", "cantidad_stock": 40 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf7a"), "sku": "GN2780-M", "talla_us": "M", "color": "Black", "cantidad_stock": 50 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf7a"), "sku": "GN2780-L", "talla_us": "L", "color": "Black", "cantidad_stock": 45 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf7a"), "sku": "GN2780-XL", "talla_us": "XL", "color": "Black", "cantidad_stock": 25 },
  
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf7b"), "sku": "IP5485-S", "talla_us": "S", "color": "Green / Red", "cantidad_stock": 70 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf7b"), "sku": "IP5485-M", "talla_us": "M", "color": "Green / Red", "cantidad_stock": 90 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf7b"), "sku": "IP5485-L", "talla_us": "L", "color": "Green / Red", "cantidad_stock": 80 },
  { "producto_id": ObjectId("6916bcd56c3ce9ed24f9cf7b"), "sku": "IP5485-XL", "talla_us": "XL", "color": "Green / Red", "cantidad_stock": 40 }
]);

// Coleccion de Usuarios
use("Adidas")
db.A_usuarios.insertMany([
  
  //5 Administradores
  {
    "nombre_completo": "Rodrigo Fernandez Rojas",
    "email": "rodrigofr@adidas.mx",
    "password": "FERNANDEZ1234",
    "rol": "admin",
    "numero_empleado": "A001",
    "fecha_nacimiento": ISODate("1990-05-15T00:00:00Z"),
    "direcciones": []
  },
  {
    "nombre_completo": "Angel Marino Balderas Landaverde",
    "email": "angelmbl@adidas.mx",
    "password": "BALDERAS1234",
    "rol": "admin",
    "numero_empleado": "A002",
    "fecha_nacimiento": ISODate("1988-10-20T00:00:00Z"),
    "direcciones": []
  },
  {
    "nombre_completo": "Juan Pablo Bautista Guerrero",
    "email": "juanpbg@adidas.mx",
    "password": "BAUTISTA1234",
    "rol": "admin",
    "numero_empleado": "A003",
    "fecha_nacimiento": ISODate("1995-02-01T00:00:00Z"),
    "direcciones": []
  },
  {
    "nombre_completo": "Jesus Emanuel Diaz Rodriguez",
    "email": "jesusedr@adidas.mx",
    "password": "DIAZ1234",
    "rol": "admin",
    "numero_empleado": "A004",
    "fecha_nacimiento": ISODate("1998-07-30T00:00:00Z"),
    "direcciones": []
  },
  {
    "nombre_completo": "Carlo Giovanni Cetina Camacho",
    "email": "carlogcc@adidas.mx",
    "password": "CETINA1234",
    "rol": "admin",
    "numero_empleado": "A005",
    "fecha_nacimiento": ISODate("1992-12-12T00:00:00Z"),
    "direcciones": []
  },

  //15 Clientes
  {
    "nombre_completo": "Ana Garcia Lopez",
    "email": "ana.garcia@gmail.com",
    "password": "cliente_password_123",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("1999-03-10T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Av. Siempre Viva 123", "ciudad": "Querétaro", "codigo_postal": "76100" }
    ]
  },
  {
    "nombre_completo": "Miguel Hernandez Martinez",
    "email": "miguel.hdz@hotmail.com",
    "password": "migue1990",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("1990-11-05T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Calle 5 de Mayo 45", "ciudad": "Guadalajara", "codigo_postal": "44100" }
    ]
  },
  {
    "nombre_completo": "Sofia Torres Diaz",
    "email": "sofia.torres@yahoo.com",
    "password": "sofi_pass_secure",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("2001-08-22T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Av. Reforma 222", "ciudad": "CDMX", "codigo_postal": "06600" }
    ]
  },
  {
    "nombre_completo": "David Jimenez Cruz",
    "email": "david.jimenez@gmail.com",
    "password": "davidj_123",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("1985-04-14T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Privada Luna 8", "ciudad": "Monterrey", "codigo_postal": "64000" }
    ]
  },
  {
    "nombre_completo": "Valeria Ruiz Sanchez",
    "email": "vale_ruiz@gmail.com",
    "password": "valeria123",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("2003-01-30T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Constituyentes 101", "ciudad": "Querétaro", "codigo_postal": "76000" }
    ]
  },
  {
    "nombre_completo": "Fernando Morales Gomez",
    "email": "fer.morales@hotmail.com",
    "password": "fermorales_pass",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("1992-06-18T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Av. de la Luz 200", "ciudad": "Querétaro", "codigo_postal": "76116" }
    ]
  },
  {
    "nombre_completo": "Camila Ortiz Perez",
    "email": "cami.ortiz@gmail.com",
    "password": "camila_ortiz_99",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("1999-10-02T00:00:00Z"),
    "direcciones": [
      { "alias": "Oficina", "calle": "Insurgentes Sur 1000", "ciudad": "CDMX", "codigo_postal": "03100" }
    ]
  },
  {
    "nombre_completo": "Javier Mendoza Flores",
    "email": "javi_mendoza@yahoo.com",
    "password": "javi1985",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("1985-12-01T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Calle Sol 12", "ciudad": "Mérida", "codigo_postal": "97000" }
    ]
  },
  {
    "nombre_completo": "Daniela Castro Ramos",
    "email": "dany.castro@gmail.com",
    "password": "dany_castro_pass",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("1994-03-25T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Av. Patria 500", "ciudad": "Guadalajara", "codigo_postal": "45110" }
    ]
  },
  {
    "nombre_completo": "Diego Alvarez Silva",
    "email": "diego.alvarez@hotmail.com",
    "password": "diego_alva_2025",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("2000-07-07T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Zaragoza 15", "ciudad": "Puebla", "codigo_postal": "72000" }
    ]
  },
  {
    "nombre_completo": "Lucia Herrera Guzman",
    "email": "lucia.herrera@gmail.com",
    "password": "lucia_guzman",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("1997-09-12T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Prol. Bernardo Quintana 10", "ciudad": "Querétaro", "codigo_postal": "76150" }
    ]
  },
  {
    "nombre_completo": "Mateo Leon Vega",
    "email": "mateo.leon@yahoo.com",
    "password": "mateo_leon_v",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("1993-11-19T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Av. Tecnológico 100", "ciudad": "Monterrey", "codigo_postal": "64849" }
    ]
  },
  {
    "nombre_completo": "Isabella Vargas Mora",
    "email": "isa.vargas@gmail.com",
    "password": "isa_vargas_m",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("2002-02-28T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Calle 10, No. 300", "ciudad": "Tijuana", "codigo_postal": "22000" }
    ]
  },
  {
    "nombre_completo": "Santiago Reyes Romero",
    "email": "santi.reyes@hotmail.com",
    "password": "santiago_reyes_01",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("2000-08-17T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Av. de los Arcos 21", "ciudad": "Querétaro", "codigo_postal": "76020" }
    ]
  },
  {
    "nombre_completo": "Regina Dominguez Salas",
    "email": "regina.dominguez@gmail.com",
    "password": "regina_dom_salas",
    "rol": "cliente",
    "fecha_nacimiento": ISODate("1996-05-24T00:00:00Z"),
    "direcciones": [
      { "alias": "Casa", "calle": "Av. Chapultepec 50", "ciudad": "CDMX", "codigo_postal": "06700" }
    ]
  }
]);


// Colección de órdenes de compra
use("Adidas");
db.A_ordenes.insertMany([
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b0d"), 
    "fecha_pedido": ISODate("2025-10-01T10:30:00Z"),
    "estado": "Entregado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f64"), 
        "sku": "B75806-9.5",
        "nombre_producto": "Tenis Samba OG",
        "cantidad": 1,
        "precio_unitario": 2399.00
      }
    ],
    "total_pedido": 2399.00,
    "direccion_envio": { "alias": "Casa", "calle": "Av. Siempre Viva 123", "ciudad": "Querétaro", "codigo_postal": "76100" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b0e"), 
    "fecha_pedido": ISODate("2025-10-03T14:15:00Z"),
    "estado": "Enviado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f7a"), 
        "sku": "IB0011-M",
        "nombre_producto": "Jersey Local 23/24 Real Madrid",
        "cantidad": 1,
        "precio_unitario": 2199.00
      },
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f8a"), 
        "sku": "HT9911-BLK",
        "nombre_producto": "Gorra Team Mercedes-AMG Petronas F1 24",
        "cantidad": 1,
        "precio_unitario": 1299.00
      }
    ],
    "total_pedido": 3498.00,
    "direccion_envio": { "alias": "Casa", "calle": "Calle 5 de Mayo 45", "ciudad": "Guadalajara", "codigo_postal": "44100" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b0f"),
    "fecha_pedido": ISODate("2025-10-05T11:00:00Z"),
    "estado": "Pagado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f6a"), 
        "sku": "GZ5159-10.0",
        "nombre_producto": "Tenis Ultraboost Light",
        "cantidad": 1,
        "precio_unitario": 4299.00
      }
    ],
    "total_pedido": 4299.00,
    "direccion_envio": { "alias": "Casa", "calle": "Av. Reforma 222", "ciudad": "CDMX", "codigo_postal": "06600" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b10"), 
    "fecha_pedido": ISODate("2025-10-06T20:00:00Z"),
    "estado": "Entregado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f92"), 
        "sku": "GW0264-9.0",
        "nombre_producto": "Tenis Adidas x Bad Bunny Forum 'First Cafe'",
        "cantidad": 1,
        "precio_unitario": 5499.00
      }
    ],
    "total_pedido": 5499.00,
    "direccion_envio": { "alias": "Casa", "calle": "Privada Luna 8", "ciudad": "Monterrey", "codigo_postal": "64000" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b11"), 
    "fecha_pedido": ISODate("2025-10-10T09:00:00Z"),
    "estado": "Pagado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f76"), 
        "sku": "HS7232-M",
        "nombre_producto": "Pants Tiro 23",
        "cantidad": 1,
        "precio_unitario": 1299.00
      }
    ],
    "total_pedido": 1299.00,
    "direccion_envio": { "alias": "Casa", "calle": "Constituyentes 101", "ciudad": "Querétaro", "codigo_postal": "76000" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b0d"), 
    "fecha_pedido": ISODate("2025-10-11T13:00:00Z"),
    "estado": "Enviado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f6b"), 
        "sku": "IF3817-8.0",
        "nombre_producto": "Tenis Gazelle",
        "cantidad": 1,
        "precio_unitario": 2299.00
      }
    ],
    "total_pedido": 2299.00,
    "direccion_envio": { "alias": "Casa", "calle": "Av. Siempre Viva 123", "ciudad": "Querétaro", "codigo_postal": "76100" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b12"), 
    "fecha_pedido": ISODate("2025-10-12T15:20:00Z"),
    "estado": "Entregado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f72"), 
        "sku": "GY8411-9.5",
        "nombre_producto": "Tenis Adizero Adios Pro 3",
        "cantidad": 1,
        "precio_unitario": 5999.00
      }
    ],
    "total_pedido": 5999.00,
    "direccion_envio": { "alias": "Casa", "calle": "Av. de la Luz 200", "ciudad": "Querétaro", "codigo_postal": "76116" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b13"), 
    "fecha_pedido": ISODate("2025-10-14T18:00:00Z"),
    "estado": "Pagado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f96"), 
        "sku": "ID0780-9.5",
        "nombre_producto": "Tenis Adidas x Bad Bunny Response CL 'Paso Fino'",
        "cantidad": 1,
        "precio_unitario": 4199.00
      },
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145fa2"), 
        "sku": "IC6976-M",
        "nombre_producto": "Shorts Woven Training",
        "cantidad": 1,
        "precio_unitario": 899.00
      }
    ],
    "total_pedido": 5098.00,
    "direccion_envio": { "alias": "Oficina", "calle": "Insurgentes Sur 1000", "ciudad": "CDMX", "codigo_postal": "03100" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b14"), 
    "fecha_pedido": ISODate("2025-10-15T12:00:00Z"),
    "estado": "Cancelado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f69"), 
        "sku": "FU7714-9.0",
        "nombre_producto": "Tenis Superstar",
        "cantidad": 1,
        "precio_unitario": 2499.00
      }
    ],
    "total_pedido": 2499.00,
    "direccion_envio": { "alias": "Casa", "calle": "Calle Sol 12", "ciudad": "Mérida", "codigo_postal": "97000" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b15"), 
    "fecha_pedido": ISODate("2025-10-16T17:45:00Z"),
    "estado": "Entregado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f9a"), 
        "sku": "ID2529-9.5",
        "nombre_producto": "Tenis Adidas x Bad Bunny Campus 'Brown'",
        "cantidad": 1,
        "precio_unitario": 3999.00
      }
    ],
    "total_pedido": 3999.00,
    "direccion_envio": { "alias": "Casa", "calle": "Av. Patria 500", "ciudad": "Guadalajara", "codigo_postal": "45110" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b16"), 
    "fecha_pedido": ISODate("2025-10-18T08:00:00Z"),
    "estado": "Pagado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145fa6"), 
        "sku": "HP5938-9.5",
        "nombre_producto": "Tenis Supernova 3",
        "cantidad": 1,
        "precio_unitario": 2799.00
      }
    ],
    "total_pedido": 2799.00,
    "direccion_envio": { "alias": "Casa", "calle": "Zaragoza 15", "ciudad": "Puebla", "codigo_postal": "72000" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b17"), 
    "fecha_pedido": ISODate("2025-10-20T19:30:00Z"),
    "estado": "Enviado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145fad"), 
        "sku": "GY7390-9.0",
        "nombre_producto": "Tachos X Crazyfast.1",
        "cantidad": 1,
        "precio_unitario": 5499.00
      }
    ],
    "total_pedido": 5499.00,
    "direccion_envio": { "alias": "Casa", "calle": "Prol. Bernardo Quintana 10", "ciudad": "Querétaro", "codigo_postal": "76150" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b18"), 
    "estado": "Pagado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145fb0"), 
        "sku": "GN2780-S",
        "nombre_producto": "Chamarra Rompevientos Adicolor",
        "cantidad": 1,
        "precio_unitario": 1899.00
      },
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145fb5"), 
        "sku": "IP5485-L",
        "nombre_producto": "Jersey Visitante 23/24 Selección Mexicana",
        "cantidad": 1,
        "precio_unitario": 1999.00
      }
    ],
    "total_pedido": 3898.00,
    "direccion_envio": { "alias": "Casa", "calle": "Av. Tecnológico 100", "ciudad": "Monterrey", "codigo_postal": "64849" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b19"), 
    "fecha_pedido": ISODate("2025-10-23T10:10:00Z"),
    "estado": "Entregado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f86"), 
        "sku": "JQ3272-9.0",
        "nombre_producto": "Tenis Adidas x Mercedes F1 Ultraboost",
        "cantidad": 1,
        "precio_unitario": 4999.00
      }
    ],
    "total_pedido": 4999.00,
    "direccion_envio": { "alias": "Casa", "calle": "Calle 10, No. 300", "ciudad": "Tijuana", "codigo_postal": "22000" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b1a"), 
    "fecha_pedido": ISODate("2025-10-25T14:00:00Z"),
    "estado": "Pagado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f66"), 
        "sku": "FU7714-8.5",
        "nombre_producto": "Tenis Superstar",
        "cantidad": 1,
        "precio_unitario": 2499.00
      }
    ],
    "total_pedido": 2499.00,
    "direccion_envio": { "alias": "Casa", "calle": "Av. de los Arcos 21", "ciudad": "Querétaro", "codigo_postal": "76020" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b1b"), 
    "fecha_pedido": ISODate("2025-10-26T16:00:00Z"),
    "estado": "Pagado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f6e"), 
        "sku": "IF3817-9.0",
        "nombre_producto": "Tenis Gazelle",
        "cantidad": 1,
        "precio_unitario": 2299.00
      }
    ],
    "total_pedido": 2299.00,
    "direccion_envio": { "alias": "Casa", "calle": "Av. Chapultepec 50", "ciudad": "CDMX", "codigo_postal": "06700" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b10"), 
    "fecha_pedido": ISODate("2025-10-28T18:30:00Z"),
    "estado": "Entregado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f62"), 
        "sku": "B75806-8.5",
        "nombre_producto": "Tenis Samba OG",
        "cantidad": 1,
        "precio_unitario": 2399.00
      },
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f76"),
        "sku": "HS7232-M",
        "nombre_producto": "Pants Tiro 23",
        "cantidad": 1,
        "precio_unitario": 1299.00
      },
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f8b"), 
        "sku": "HT9911-WHT",
        "nombre_producto": "Gorra Team Mercedes-AMG Petronas F1 24",
        "cantidad": 1,
        "precio_unitario": 1299.00
      }
    ],
    "total_pedido": 4997.00,
    "direccion_envio": { "alias": "Casa", "calle": "Privada Luna 8", "ciudad": "Monterrey", "codigo_postal": "64000" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b0f"), 
    "fecha_pedido": ISODate("2025-11-01T12:00:00Z"),
    "estado": "Pagado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f93"), 
        "sku": "GW0264-9.5",
        "nombre_producto": "Tenis Adidas x Bad Bunny Forum 'First Cafe'",
        "cantidad": 1,
        "precio_unitario": 5499.00
      }
    ],
    "total_pedido": 5499.00,
    "direccion_envio": { "alias": "Casa", "calle": "Av. Reforma 222", "ciudad": "CDMX", "codigo_postal": "06600" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b0d"), 
    "fecha_pedido": ISODate("2025-11-02T15:00:00Z"),
    "estado": "Pagado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145fb6"), 
        "sku": "IP5485-XL",
        "nombre_producto": "Jersey Visitante 23/24 Selección Mexicana",
        "cantidad": 1,
        "precio_unitario": 1999.00
      }
    ],
    "total_pedido": 1999.00,
    "direccion_envio": { "alias": "Casa", "calle": "Av. Siempre Viva 123", "ciudad": "Querétaro", "codigo_postal": "76100" }
  },
  {
    "usuario_id": ObjectId("6916c307ed53083f56ab6b0e"), 
    "fecha_pedido": ISODate("2025-11-03T17:00:00Z"),
    "estado": "Enviado",
    "items_comprados": [
      {
        "inventario_id": ObjectId("6916bfdcb5650c737e145f87"), 
        "sku": "JQ3272-9.5",
        "nombre_producto": "Tenis Adidas x Mercedes F1 Ultraboost",
        "cantidad": 1,
        "precio_unitario": 4999.00
      }
    ],
    "total_pedido": 4999.00,
    "direccion_envio": { "alias": "Casa", "calle": "Calle 5 de Mayo 45", "ciudad": "Guadalajara", "codigo_postal": "44100" }
  }
]);


// Actualizar todos los usuarios que no tienen el campo "estado" para agregarlo con el valor "activo"
use("Adidas")
db.A_usuarios.updateMany(
  { "estado": { "$exists": false } }, 
  { "$set": { "estado": "activo" } }  
);