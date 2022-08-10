-- Creates second_table in hbtn_0c_0 with default values
CREATE table IF NOT exists second_table(id INT, name VARCHAR(25), score INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES ('1', 'John', '10');
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES ('2', 'Alex', '3');
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES ('3', 'Bob', '14');
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES ('4', 'George', '8');
