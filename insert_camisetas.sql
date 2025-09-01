-- SQL para insertar camisetas de prueba
INSERT INTO mi_primer_app_camiseta (
    equipo, temporada, tipo, talla, precio, precio_oferta, stock, activa, 
    imagen, descripcion, fecha_creacion, fecha_actualizacion
) VALUES 
(
    'Selección Argentina', '1986 World Cup', 'local', 'M', 89.99, 79.99, 15, 1,
    'camisetas/argentina_1986.jpg', 'Camiseta retro de Argentina Mundial 1986 - Diego Maradona',
    datetime('now'), datetime('now')
),
(
    'Real Madrid CF', '1998-2000', 'local', 'L', 94.99, 84.99, 12, 1,
    'camisetas/real_madrid_1998.jpg', 'Camiseta histórica Real Madrid era Galácticos',
    datetime('now'), datetime('now')
),
(
    'FC Barcelona', '1992-1995', 'local', 'L', 99.99, 89.99, 8, 1,
    'camisetas/barcelona_1992.jpg', 'Camiseta FC Barcelona Dream Team de Cruyff',
    datetime('now'), datetime('now')
);
