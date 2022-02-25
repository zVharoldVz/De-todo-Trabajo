
INSERT INTO "auth_user" ( "id","password","date_joined","last_login", "is_superuser", "username", "last_name", "email", "is_staff","is_active","first_name") 
VALUES ( 1,"pbkdf2_sha256$260000$I73Et5pTVLUmV4AQWU5xJn$9Zp3hFY/k6lBxGP9LoDhfglQiiqkBWW7Iam8bnDp4R4=","2022-02-23 01:21:22.382335",1,"harold","osorio cruzado","harold_54430@hotmail.com",1,1,"2022-02-14 02:35:22.608208","harold" )
INSERT INTO "auth_user" ( "id","password","date_joined","last_login", "is_superuser", "username", "last_name", "email", "is_staff","is_active","first_name") 
VALUES ( 2,"pbkdf2_sha256$260000$Npvm7wQ4i3aItPkLu3iR6i$a6ihozICIAGK47hTmM164oqkxJkdgXbS+DrMTz903Zo=","2022-02-15 23:54:40.678198",1,"harold1","osorio cruzado IMPOMAXS","harold_54430@hotmail.com",1,1,"2022-02-15 23:12:12.138980","harold" );
INSERT INTO "auth_user" ( "id","password","date_joined","last_login", "is_superuser", "username", "last_name", "email", "is_staff","is_active","first_name") 
VALUES (3,"pbkdf2_sha256$260000$uOa0Cbgbm8BpNTnhftDKZ9$s0XIJZjx8T6gRxdaM3CmVkNzHt4VVhJBDgbRwbfjX74=","2022-02-17 00:36:46.206999",0,"harold2","","harold_54430@hotmail.com",0,1,"2022-02-17 00:36:08.156063","" );
INSERT INTO "auth_user" ( "id","password","date_joined","last_login", "is_superuser", "username", "last_name", "email", "is_staff","is_active","first_name") 
VALUES ( 4,"pbkdf2_sha256$260000$X5KOLZ2aMFEC9cyEVRd9UE$97vAC5+Qdxaiph4fngZ5jVHP3dwxTsPq7ohNzBw+nQI=","2022-02-17 02:33:01.702682",0,"harold3","","harold_54430@hotmail.com",0,1,"2022-02-17 02:32:54.686601","" );

INSERT INTO "app_tipotrabajo" ( "id", "tipotrabajo") VALUES (1,"Albañil");
INSERT INTO "app_tipotrabajo" ( "id", "tipotrabajo") VALUES (2,"Electricista");
INSERT INTO "app_tipotrabajo" ( "id", "tipotrabajo") VALUES (3,"Camarografo");
INSERT INTO "app_tipotrabajo" ( "id", "tipotrabajo") VALUES (4,"Tecnico");
INSERT INTO "app_tipotrabajo" ( "id", "tipotrabajo") VALUES (5,"Maestro");

INSERT INTO "app_habilidades" ("id", "nombrehabilidad", "descripcion", "nomeroTrabjos", "tipoTrabajo_id", "user_id") VALUES ( 19,"El vídeo proporciona una manera eficaz dfdsfsdfsdf","El vídeo proporciona una manera eficaz para ayudarle a demostrar el punto. Cuando haga clic en Vídeo en línea, puede pegar el código para insertar del vídeo que desea agregar. También puede escribir una palabra clave para buscar en línea el vídeo que mejor se adapte a su documento.
Para otorgar a su documento un aspecto profesional, Word proporciona encabezados, pies de página, páginas de portada y diseños de cuadro de texto que se complementan entre sí. Por ejemplo, puede agregar una portada coincidente, el encabezado y la barra lateral. Haga clic en Insertar y elija los elementos que desee de las distintas galerías.
Los temas y estilos también ayudan a mantener su documento coordinado. Cuando haga clic en Diseño y seleccione un tema nuevo, cambiarán las imágenes, gráficos y gráficos SmartArt para que coincidan con el nuevo tema. Al aplicar los estilos, los títulos cambian para coincidir con el nuevo tema.",0,4,1);
INSERT INTO "app_habilidades" ("id", "nombrehabilidad", "descripcion", "nomeroTrabjos", "tipoTrabajo_id", "user_id") VALUES ( 23,"dfsddsfsd","sdfsd",0,1,1 );
INSERT INTO "app_habilidades" ("id", "nombrehabilidad", "descripcion", "nomeroTrabjos", "tipoTrabajo_id", "user_id") VALUES ( 26,"sdfsdsdasd32423","sdfsd",0,3,1);
INSERT INTO "app_habilidades" ("id", "nombrehabilidad", "descripcion", "nomeroTrabjos", "tipoTrabajo_id", "user_id") VALUES ( 31,"asddfgdf","asddfg",0,1,1 );
INSERT INTO "app_habilidades" ("id", "nombrehabilidad", "descripcion", "nomeroTrabjos", "tipoTrabajo_id", "user_id") VALUES ( 32,"prueba","prueba",0,4,1 );
INSERT INTO "app_habilidades" ("id", "nombrehabilidad", "descripcion", "nomeroTrabjos", "tipoTrabajo_id", "user_id") VALUES ( 33,"asdasd","dfgdfgdfg",0,1,1);
INSERT INTO "app_habilidades" ("id", "nombrehabilidad", "descripcion", "nomeroTrabjos", "tipoTrabajo_id", "user_id") VALUES ( 34,"fdgfg","dsf",0,2,1 );
INSERT INTO "app_habilidades" ("id", "nombrehabilidad", "descripcion", "nomeroTrabjos", "tipoTrabajo_id", "user_id") VALUES ( 35,"haroldfgdgdfgdf","fdgdfgdfgdfg",0,3,1 );
INSERT INTO "app_habilidades" ("id", "nombrehabilidad", "descripcion", "nomeroTrabjos", "tipoTrabajo_id", "user_id") VALUES ( 36,"dfsdfassssssssssssssssssssssssssssssssss","asdasdsadsad",0,2,1 );
INSERT INTO "app_habilidades" ("id", "nombrehabilidad", "descripcion", "nomeroTrabjos", "tipoTrabajo_id", "user_id") VALUES ( 37,"asdasd","dgdgdfgdfg",0,1,1 );

INSERT INTO "app_extradato" ("id", "telefono",  "dni", "Direcion", "user_id")  VALUES ( 9,4345345,777945,"sdfdsfdfgdfgdf",1 );
INSERT INTO "app_extradato" ("id", "telefono",  "dni", "Direcion", "user_id")  VALUES ( 11,7867185737,48493788,"dsfdsfdsf",2 );
INSERT INTO "app_extradato" ("id", "telefono",  "dni", "Direcion", "user_id")  VALUES ( 12,"","","",3 );
INSERT INTO "app_extradato" ("id", "telefono",  "dni", "Direcion", "user_id")  VALUES ( 13,"","","",4 );

INSERT INTO "app_foto_perfil" ( "id", "imagen", "user_id") VALUES ( 2,"DeTodoTrabajo/FotoUser/WhatsApp_Image_2021-12-29_at_3.25.21_PM.jpeg",2);
INSERT INTO "app_foto_perfil" ( "id", "imagen", "user_id") VALUES ( 5,"DeTodoTrabajo/FotoUser/User-Login_NZNpBVn.png",1 );

INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 1,"DeTodoTrabajo/FotoTrabajo/256571053_300738185240371_372236517694667997_n.jpg",33 );
INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 2,"DeTodoTrabajo/FotoTrabajo/260077622_995901021141005_6613930230373901908_n.jpg",33 );
INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 3,"DeTodoTrabajo/FotoTrabajo/260261697_1237340453452883_7657640851203089843_n.jpg",33 );
INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 4,"DeTodoTrabajo/FotoTrabajo/264400710_1915101035338231_206613274263121647_n.jpg",34 );
INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 5,"DeTodoTrabajo/FotoTrabajo/268903854_461111345579095_3850846324374305713_n.jpg",34 );
INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 6,"DeTodoTrabajo/FotoTrabajo/270295632_869939053695946_354383824044102006_n.jpg",34 );
INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 7,"DeTodoTrabajo/FotoTrabajo/WhatsApp_Image_2021-12-10_at_9.41.45_AM.jpeg",35 );
INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 8,"DeTodoTrabajo/FotoTrabajo/WhatsApp_Image_2021-12-29_at_3.25.21_PM.jpeg",35 );
INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 24,"DeTodoTrabajo/FotoTrabajo/260077622_995901021141005_6613930230373901908_n_oNRoJ97.jpg",19 );
INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 25,"DeTodoTrabajo/FotoTrabajo/260261697_1237340453452883_7657640851203089843_n_9vtmtSq.jpg",19 );
INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 26,"DeTodoTrabajo/FotoTrabajo/262544095_312897624173836_3264170854886474489_n.jpg",19 );
INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 27,"DeTodoTrabajo/FotoTrabajo/260077622_995901021141005_6613930230373901908_n_tI7N07f.jpg",36 );
INSERT INTO "app_fototrabajo" ( "id", "fotoTrabajo", "habilidad_id") VALUES ( 28,"DeTodoTrabajo/FotoTrabajo/272818837_4811155785626587_9112371571623836675_n.jpg",37 );