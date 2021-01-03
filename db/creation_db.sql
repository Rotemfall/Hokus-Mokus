CREATE schema `group1`; 
CREATE TABLE `group1`.`customers`(
  `email_address` varchar(30) NOT NULL,
  `password` varchar(40) NOT NULL,
  `user_name` VARCHAR(25) NOT NULL,
  `first_name` varchar(10) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `country` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `street` varchar(50) NOT NULL,
  `number` smallint NOT NULL,
  `zip_code` varchar(7) NOT NULL,
  `phone_number` varchar(10) NOT NULL,
  `role` varchar(20) NULL DEFAULT('customer'),
  PRIMARY KEY (`email_address`),
  UNIQUE INDEX(`user_name`)
);

CREATE TABLE `group1`.`products`(
`sku` integer NOT NULL,
`name` nvarchar(50) NOT NULL,
`price` smallint NOT NULL,
`description` nvarchar(550) NOT NULL,
`category_code` tinyint NOT NULL,
`img` VARCHAR(50) NOT NULL,
PRIMARY KEY (`sku`)
);
 
CREATE TABLE `group1`.`orders`(
`id` integer AUTO_INCREMENT NOT NULL,
`date_of_order` DATE NOT NULL,
`email_address` varchar(30) NOT NULL,
PRIMARY KEY(`id`),
KEY `email_address` (`email_address`),
CONSTRAINT `email_address` FOREIGN KEY (`email_address`) REFERENCES `customers` (`email_address`) ON DELETE CASCADE
);
 
CREATE TABLE `group1`.`reviews`(
`id` int AUTO_INCREMENT NOT NULL,
`date` DATE NOT NULL,
`rank` tinyint NOT NULL,
`content` nvarchar(250) NULL,
`user_name` VARCHAR(25) NOT NULL,
`sku` integer NOT NULL,
PRIMARY KEY(`id`),
FOREIGN KEY(`user_name`) REFERENCES `group1`.`customers`(`user_name`) ON DELETE CASCADE,
FOREIGN KEY(`sku`) REFERENCES `group1`.`products`(`sku`)
);
 
CREATE TABLE `group1`.`credit_cards`(
`credit_card_number` nchar(16) NOT NULL,
`expiration_date` varchar(5) NOT NULL,
`cvv` varchar(3) NOT NULL,
`email_address` varchar(30) NOT NULL,
FOREIGN KEY(`email_address`) REFERENCES `customers`(`email_address`) ON DELETE CASCADE,
PRIMARY KEY(`credit_card_number`)
);
 
CREATE TABLE `group1`.`contact_us`(
`id` int AUTO_INCREMENT NOT NULL,
`sent_date` date NOT NULL,
`subject` nvarchar(120) NOT NULL,
`content` text(559) NOT NULL,
`status` nvarchar(20) NOT NULL,
`email_address` varchar(30) NOT NULL,
PRIMARY KEY(`id`)
);
 
CREATE TABLE `group1`.`categories`(
`category_code` tinyint AUTO_INCREMENT NOT NULL,
`category_name` varchar(30) NOT NULL,
`img` VARCHAR(50) NOT NULL,
PRIMARY KEY(`category_code`)
);
 
CREATE TABLE `group1`.`include`(
`order_id` integer NOT NULL,
`sku` integer NOT NULL,
`quantity` tinyint NOT NULL,
PRIMARY KEY(`order_id`, `sku`),
FOREIGN KEY(`order_id`) REFERENCES `orders`(`id`) ON DELETE CASCADE,
FOREIGN KEY(`sku`) REFERENCES `products`(`sku`)
);

INSERT INTO `group1`.`customers`
(`email_address`,
`password`,
`user_name`,
`first_name`,
`last_name`,
`country`,
`city`,
`street`,
`number`,
`zip_code`,
`phone_number`)
VALUES
('john@gmail.com', '0987654321','snow123', 'john', 'snow', 'uk', 'london', 'oxford', 100, '8749485', '0584534234'),
('mike2g@gmail.com', 'm12345i678','Bmike', 'mike', 'cohen', 'germany', 'bon', 'main', 890, '9845678', '052300734'),
('roni_99@gmail.com', 'roni2020noam', 'roniponi', 'roni', 'bateman', 'italy', 'rome', 'pizza', 13234, '8709043', '059003454'),
('nicktheking@gmail.com', 'n1i2k3e40909', 'nick876', 'nick', 'lopez', 'france', 'paris', 'macron', 890, '9589085', '058315734'),
('romi_lev3@gmail.com', 'romi87romi5', 'rominiq', 'romi', 'levi', 'israel', 'tel aviv', 'gordon', 13, '7843546', '057234201');

 INSERT INTO `group1`.`customers`
 (`email_address`,
`password`,
`user_name`,
`first_name`,
`last_name`,
`country`,
`city`,
`street`,
`number`,
`zip_code`,
`phone_number`,
`role`)
 VALUES
 ('admin@gmail.com', 'admin', 'admin', 'ori', 'levi', 'israel', 'tel aviv', 'toval', 11, '1435546', '0541234567', 'admin'),
 ('anna@gmail.com', '4321', 'anna4', 'anna', 'bloom', 'israel', 'ramat gan', 'herzel', 39, '6978600', '0523421090', 'dba'),
 ('gil@gmail.com', 'gil33', 'gilfadid', 'gil', 'fadida', 'israel', 'tel aviv', 'yarkon', 102, '7654321', '0549807721', 'content manager');

INSERT INTO `group1`.`categories`
(`category_code`,
`category_name`,
`img`)
VALUES
(1, 'Spells Defence', 'img/cat_1.jpg'),
(2, 'Spyware', 'img/cat_2.jpg'),
(3, 'Muggle Magic', 'img/cat_3.jpg'),
(4, 'Games', 'img/cat_4.jpg');

INSERT INTO `group1`.`products`
(`SKU`,
`name`,
`price`,
`description`,
`category_code`,
`img`) 
VALUES
(602456888, 'Reusable Hangman', 10, 'magical toy version of the traditionally pen-and-paper game hangman', 1, 'img/reusable_hangman.jpg'),
(3267939,'Extendable Ears', 15, 'They are long, flesh-coloured pieces of string which one can insert in one\'s ear, then shove the other end under (for example) a door, and one will hear the conversation or other noise as clear as if it was mere feet away, unless, that is, the door has been Imperturbed (with Imperturbable Charm)', 3, 'img/extendable_ear.jpg'),
(6882018,'Shield Hat',20,  'Shield Hats are magical objects that are enchanted with a Shield Charm and when worn, shield the wearer from many light to moderate curses, jinxes, and other unfriendly spells.', 2, 'img/shield_hat.jpg'),
(28902838, 'Peruvian Instant Darkness Powder', 35, 'his darkness powder creates darkness when used, allowing the user to escape. As its name indicates, it was originally invented by the wizarding community in Peru, which is the place from which the Weasley twins imported the powder. The darkness produced is resistant to many Light-creation spells.', 3, 'img/Peruvian_Instant_Darkness_Powder.jpg'),
(47721029, 'Decoy Detonator', 15, 'Decoy Detonators are black horn-like magical objects designed to create a diversion. After being dropped, the decoy runs a fair distance away, makes a noise like a loud bang, and releases clouds of black smoke, diverting attention from the user.', 3, 'img/decoy_detonator.jpg'),
(53497897, 'Magical Moustache Miracle Stubble Grow', 10, 'Magical Moustache Miracle Stubble Grow was a collection of fake facial hair products that was part of the Muggle Magic magic trick line by Weasleys', 4, 'img/magical_moustache.gif');


INSERT INTO `group1`.`orders` 
(`date_of_order`,
`email_address`)
VALUES
('2020-02-04', 'romi_lev3@gmail.com'),
('2020-02-04', 'mike2g@gmail.com'),
('2019-06-09', 'nicktheking@gmail.com'),
('2019-06-12', 'john@gmail.com'),
('2020-05-06', 'roni_99@gmail.com');

INSERT INTO `group1`.`reviews`
(`date`,
`rank`,
`content`,
`user_name`,
`sku`)
VALUES
('2020-05-02', 5, 'My son was happy to get this product, the quality of it is more than expected:)', 'roniponi', 3267939),
('2019-03-01', 5, 'Good product, I got the delivery very fast!', 'rominiq', 3267939),
('2019-01-29', 4, 'I bought this as a present to my friend for his birthday, the delivery was ok. I am pleased from the service that I got', 'rominiq', 28902838),
('2019-06-21', 5, 'I loved this product!! I was so surprised to get it after one day post order! recommended','roniponi', 602456888),
('2019-05-01', 4, 'The product quality is great, unfortunately the delivery has arrived when no one was at home so the product was next to the front door of my house', 'snow123', 28902838);

INSERT INTO `group1`.`credit_cards`
(`credit_card_number`,
`expiration_date`,
`cvv`,
`email_address`)
VALUES
(4580231109890023, '09/25', 123, 'romi_lev3@gmail.com'),
(2007489724531765, '02/22', 431, 'nicktheking@gmail.com'),
(1287350707297542, '04/20', 119, 'john@gmail.com'),
(2221343057284956, '03/23', 767, 'mike2g@gmail.com'),
(0089694367123597, '05/24', 098, 'roni_99@gmail.com');

INSERT INTO `group1`.`contact_us`
(`sent_date`,
`subject`,
`content`,
`status`,
`email_address`) 
VALUES
('2019-06-20', 'My order didn’t ARRIVE!!!!!', 'WHERE MY ORDER?!!', 'done', 'john@gmail.com'),
('2019-06-20', 'Sorry!', 'My order has just arrived sorry', 'done', 'john@gmail.com'),
('2020-02-10', 'My order', 'My order has just arrived without any present bag to rape it… can somebody can call me and make sure to sent me the bag today? 052300734', 'done', 'mike2g@gmail.com'),
('2019-06-17', 'Website', 'Hello I have just made an order on your website but in the middle of the process my computer crashed so I wanted to check if my order (no. 81234) got into the system or should I make a new one? I will appreciate your resspound. Lior', 'done', 'nicktheking@gmail.com'),
('2020-05-20', 'My delivery', 'My order has just arrived and I notice that I got 2 of the game that I ordered, I am guessing that there is a misunderstanding.', 'waiting', 'roni_99@gmail.com');

INSERT INTO `group1`.`include`
(`order_id`,
`sku`,
`quantity`) 
VALUES
(1, 3267939, 2),
(1, 28902838, 3),
(2, 28902838, 1),
(3, 3267939, 2),
(4, 28902838, 2),
(5,602456888 , 1);