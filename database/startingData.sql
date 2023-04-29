INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('aturing', 'b93727798b520dc10d145b53909c061f082ff14cd5f8cb4ab24c3b71bfa57d7e12e1296029be74c06a0d91ba32756f9fc978047fbe7232be67f94dfc1de9ced9', 'alan@enigma.com', 'Alan', 'Turing');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('dritchie', '67aff785bd17ac24448d491926ff7aadd8fa75e51a2f7a9bfc31889bad0adcd2989061a27ccd9eff9e5e31f2bc14b5c193727e116dc8dc48259acb3919171cd4', 'dennis@unix.com', 'Dennis', 'Ritchie');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com', 'Leslie', 'Lamport');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com', 'Barbara', 'Liskov');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('The Dark Side of the Moon', '1973 Pink Floyd Album', 25.99, 60, 'static/images/The_Dark_Side_of_the_Moon.jpg', 'Rock');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('...And Justice for All', '1988 Metallica Album', 39.99, 10, 'static/images/justiceforall.jpeg', 'Rock');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('In Utero', '1993 Nirvana Album', 39.99, 5, 'static/images/in-utero.jpg', 'Rock');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Hotel California', '1976 Eagles Album', 35.99, 10, 'static/images/Hotelcalifornia.jpg', 'Rock');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('OK Computer', '1997 Radiohead Album', 19.99, 20, 'static/images/OKCOMPUTER.jpeg', 'Rock');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Synchronicity', '1983 The Police Album', 35.99, 15, 'static/images/synchronicity.jpg', 'Rock');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Freudian', '2017 Daniel Caeasar Album', 29.99, 10, 'static/images/freudian.jpg', 'R&B');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('channel ORANGE', '2012 Frank Ocean Album', 49.99, 5, 'static/images/channelorange.jpeg', 'R&B');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Apollo XXI', '2019 Steve Lacy Album', 39.99, 30, 'static/images/Aollo-XXI.jpeg', 'R&B');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Ivory', '2022 Omar Apollo ', 29.99, 10, 'static/images/ivroy.jpeg', 'R&B');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Candydrip', '2022 Lucky Daye Album', 19.99, 10, 'static/images/candydrip.jpeg', 'R&B');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('If Orange Was A Place', '2021 Tems Album', 25.99, 10, 'static/images/orange-was-a-place.jpeg', 'R&B');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('The Melodic Blue', '2021 Baby Keem Album', 35.99, 10, 'static/images/the-melodic-blue.jpeg', 'Rap');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Nothing Was The Same', '2013 Drake Album', 40.99, 30, 'static/images/nothingwasthesame.jpeg', 'Rap');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('TESTING', '2018 A$AP Rocky Album', 39.99, 10, 'static/images/testing.jpeg', 'Rap');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('CALL ME IF YOU GET LOST', '2021 Tyler, The Creator Album', 45.99, 10, 'static/images/callmeifyougetlost.jpg', 'Rap');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('HEROS & VILLAINS', '2022 Metro Boomin Album', 25.99, 10, 'static/images/heros&villains.jpeg', 'Rap');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Madvillainy', '2004 MF DOOM', 35.99, 10, 'static/images/madvillainy.jpeg', 'Rap');

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `cost`)
VALUES ('1', 'aturing', '1', 10, 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `cost`)
VALUES ('2', 'dritchie', '2', 10, 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `cost`)
VALUES ('3', 'llamport', '3', 10, 5.50);
