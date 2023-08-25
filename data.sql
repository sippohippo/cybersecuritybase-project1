
/* NOTE! CHANGE THE ADDRESS OF THE IMAGE-FILES. CTRL-F, Users/sippo and replace all with your location */

/* inserting test images */
insert into images values (1, 'img1', TRUE, pg_read_binary_file('/Users/sippo/cybersecuritybase-project1/test_images/Fake1.jpg')::bytea);
insert into images values (2, 'img2', TRUE, pg_read_binary_file('/Users/sippo/cybersecuritybase-project1/test_images/Fake2.jpg')::bytea);
insert into images values (3, 'img3', TRUE, pg_read_binary_file('/Users/sippo/cybersecuritybase-project1/test_images/Fake3.jpg')::bytea);
insert into images values (4, 'img4', FALSE, pg_read_binary_file('/Users/sippo/cybersecuritybase-project1/test_images/Real1.jpg')::bytea);
insert into images values (5, 'img5', FALSE, pg_read_binary_file('/Users/sippo/cybersecuritybase-project1/test_images/Real2.jpg')::bytea);
insert into images values (6, 'img6', FALSE, pg_read_binary_file('/Users/sippo/cybersecuritybase-project1/test_images/Real3.jpg')::bytea);

/* inserting posts */
insert into posts values (1, 'bot', 'Daniel Batista', '@danielbatista', 'Barbie, an iconic figure that has inspired generations, is more than just a doll. With over 200 careers, Barbie has encouraged kids to dream big and break boundaries.', 1);
insert into posts values (2, 'bot', 'Ralp Raynor', '@ralphraynor412', 'From conference rooms to coffee shops, this journey reminded me that hard work and determination truly pave the way for success! #BusinessVenture', 2);
insert into posts values (3, 'bot', 'Eugene Pohlman', '@Pohlman', 'Remember, success is not built on one big achievement, but on the small steps we take every day towards our goals. Keep pushing forward, even when it feels like progress is slow.', 3);
insert into posts values (4, 'human', 'Phil Madden', '@philmadden', 'Happinesss comes from WHAT we do. Fulfillment comes from WHY we do it.', 4);
insert into posts values (5, 'human', 'William Bennett', '@williamb', 'When things do not work out as we wish, it may be that we have not been 100% clear in our request.', 5);
insert into posts values (6, 'human', 'Matthew Gibson', '@MatthewGibson', 'Do not discount yourself no matter what you are doing. Everyone has a unique perspective that they can bring to the world.', 6);

/* inserting admin account */

insert into users values (1000, 'admin', 'admin', TRUE, TRUE);
