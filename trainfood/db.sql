/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - train
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`train` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `train`;

/*Table structure for table `assign` */

DROP TABLE IF EXISTS `assign`;

CREATE TABLE `assign` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `oid` int(11) DEFAULT NULL,
  `status` varchar(300) DEFAULT NULL,
  `date` varchar(700) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `assign` */

/*Table structure for table `delivery` */

DROP TABLE IF EXISTS `delivery`;

CREATE TABLE `delivery` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(63) DEFAULT NULL,
  `place` varchar(300) DEFAULT NULL,
  `post` varchar(88) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(300) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  `rid` int(11) DEFAULT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `delivery` */

insert  into `delivery`(`did`,`name`,`place`,`post`,`pin`,`phone`,`email`,`lid`,`rid`) values 
(1,'akash','kkk','kozhikode',670654,9089789654,'as@gmail.com',7,2);

/*Table structure for table `details` */

DROP TABLE IF EXISTS `details`;

CREATE TABLE `details` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `oid` int(11) NOT NULL,
  `trainno` int(11) NOT NULL,
  `seatno` int(255) NOT NULL,
  `trainname` varchar(500) NOT NULL,
  `station` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;

/*Data for the table `details` */

insert  into `details`(`did`,`oid`,`trainno`,`seatno`,`trainname`,`station`) values 
(3,21,12,12,'nethrw',''),
(4,1,0,0,'gv','gg'),
(5,1,3,2,'2','as'),
(6,4,2,45,'qqq','wusus'),
(7,1,22,22,'u','sjsjs'),
(8,4,12,12,'janashadabthi','Kozhikode '),
(9,5,12,23,'dud','ssd'),
(10,5,12,13,'as','st'),
(11,4,12345,12,'kochi','kochi '),
(12,9,12,23,'aaaa','bbbbb'),
(13,9,12,23,'jana','kozhikode'),
(14,10,23,34,'ooooo','kkkk'),
(15,10,12,23,'ganga','kochi '),
(16,10,13456,133,'aaaaaaa','kochi'),
(17,11,12,23,'aasdd','gh'),
(18,11,231,23,'parasu','calicut '),
(19,12,123,23,'ok','aada '),
(20,12,987,234,'van','kochi'),
(21,13,12,23,'janashadabdi','kzkd'),
(22,13,14321,12,'Amrutha','Kozhikode '),
(23,13,1234,12,'amrutha','kozhikode'),
(24,13,1344,23,'Amrutha ','Kozhikode '),
(25,13,1432,13,'Amrutha ','Kozhikode '),
(26,13,34,567890,'hoe','kzkd'),
(27,13,34,567890,'hoe','kzkd'),
(28,13,34,567890,'hoe','kzkd'),
(29,13,34,567890,'hoe','kzkd'),
(30,13,34,567890,'hoe','kzkd'),
(31,13,34,567890,'hoe','kzkd'),
(32,13,34,567890,'hoe','kzkd'),
(33,13,34,567890,'hoe','kzkd'),
(34,13,34,567890,'hoe','kzkd'),
(35,13,34,567890,'hoe','kzkd'),
(36,13,34,567890,'hoe','kzkd'),
(37,13,34,567890,'hoe','kzkd'),
(38,13,0,0,'ss','se'),
(39,13,0,0,'ss','se'),
(40,13,0,0,'ss','se'),
(41,13,0,0,'ss','se'),
(42,13,23,44,'vt','jj'),
(43,13,23,44,'vt','jj');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `feedback` varchar(500) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`rid`,`uid`,`feedback`,`date`) values 
(1,2,9,'helo','2023-04-24'),
(2,2,9,'helo','2023-04-24'),
(3,2,9,'helo','2023-04-24'),
(4,2,9,'helo','2023-04-24'),
(5,16,9,'oooo','2023-04-27');

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `locationid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `latitude` varchar(30) NOT NULL,
  `longitude` varchar(30) NOT NULL,
  PRIMARY KEY (`locationid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`locationid`,`lid`,`latitude`,`longitude`) values 
(1,9,'11.2577662','75.784518'),
(2,7,'11.2577678','75.7845285'),
(3,10,'11.25834055','75.77963007'),
(4,18,'11.2577972','75.7845429');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(500) NOT NULL,
  `password` varchar(500) NOT NULL,
  `type` varchar(500) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(2,'rest','1234','restaurant'),
(3,'train','567','delivery'),
(4,'train','567','train service'),
(5,'sneha','pm','train service'),
(6,'paru','paru','train service'),
(7,'del','123','delivery'),
(8,'res','123','Rejected'),
(9,'gg','gg','user'),
(10,'asd ','asdl','user'),
(11,'asdfo','asdfrt','delivery'),
(14,'asd','sdfghjkl','pending'),
(16,'asd','sdfghjkl','restaurant'),
(17,'par','123','restaurant'),
(18,'aswin ','123','user');

/*Table structure for table `menu` */

DROP TABLE IF EXISTS `menu`;

CREATE TABLE `menu` (
  `menuid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `items` varchar(500) NOT NULL,
  `details` varchar(500) NOT NULL,
  `image` varchar(600) NOT NULL,
  `date` date NOT NULL,
  `type` varchar(30) DEFAULT NULL,
  `price` varchar(30) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  PRIMARY KEY (`menuid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `menu` */

insert  into `menu`(`menuid`,`rid`,`items`,`details`,`image`,`date`,`type`,`price`,`qty`) values 
(3,2,'kjhj','mmjkj','IMG-20230330-WA0030.jpg','2023-04-06','veg','122',61),
(4,2,'biriyani','rgtyu','IMG-20230330-WA0030.jpg','2023-03-31','non-veg','123',4),
(5,2,'rice','hiiiiii','download.jpeg','2023-04-13','veg','60',60);

/*Table structure for table `order` */

DROP TABLE IF EXISTS `order`;

CREATE TABLE `order` (
  `orderid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `total` varchar(40) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`orderid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `order` */

insert  into `order`(`orderid`,`userid`,`total`,`status`) values 
(1,9,'4026','cart');

/*Table structure for table `orderitem` */

DROP TABLE IF EXISTS `orderitem`;

CREATE TABLE `orderitem` (
  `itemid` int(11) NOT NULL AUTO_INCREMENT,
  `orderid` int(11) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`itemid`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `orderitem` */

insert  into `orderitem`(`itemid`,`orderid`,`pid`,`quantity`,`date`,`status`) values 
(16,14,4,1,'2023-04-27','cart'),
(17,14,3,8,'2023-04-27','cart'),
(18,1,3,45,'2023-04-27','cart');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) DEFAULT NULL,
  `amount` bigint(20) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`id`,`rid`,`amount`,`date`) values 
(1,2,100,'2023-02-07'),
(2,16,500,'2023-03-06'),
(3,19,42,'2023-03-06'),
(4,20,1000,'2023-03-21'),
(5,21,200,'2023-03-21'),
(6,21,123,'2023-04-21'),
(7,1,123,'2023-04-21'),
(8,4,122,'2023-04-21'),
(9,5,122,'2023-04-24'),
(10,9,60,'2023-04-26'),
(11,10,122,'2023-04-26'),
(12,11,123,'2023-04-27'),
(13,13,123,'2023-04-27');

/*Table structure for table `restaurant` */

DROP TABLE IF EXISTS `restaurant`;

CREATE TABLE `restaurant` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `place` varchar(500) NOT NULL,
  `post` varchar(500) NOT NULL,
  `pin` int(255) NOT NULL,
  `latitude` varchar(500) NOT NULL,
  `longitude` varchar(500) NOT NULL,
  `mobileno` bigint(255) NOT NULL,
  `email` varchar(30) NOT NULL,
  `image` varchar(400) NOT NULL,
  `lid` int(255) NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `restaurant` */

insert  into `restaurant`(`rid`,`name`,`place`,`post`,`pin`,`latitude`,`longitude`,`mobileno`,`email`,`image`,`lid`) values 
(1,'abcd','fghjkd','fghj',456789,'11.257787','75.7845422',5678,'zx','IMG-20230330-WA0030.jpg',2),
(2,'amruthz mess','jjkj','jhj',678,'67','678',5678,'fghjk@gmail.com','j.jpeg',16),
(3,'paraqon','kozhikode','mndy',670644,'11.12.67','112.89.89.9',9667677878,'ss@gmai.com','j.jpeg',17);

/*Table structure for table `service` */

DROP TABLE IF EXISTS `service`;

CREATE TABLE `service` (
  `serviceid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `fname` varchar(500) NOT NULL,
  `lname` varchar(500) NOT NULL,
  `trainno` int(11) NOT NULL,
  `place` varchar(500) NOT NULL,
  `post` varchar(500) NOT NULL,
  `pin` int(11) NOT NULL,
  `phone` bigint(11) NOT NULL,
  `email` varchar(500) NOT NULL,
  PRIMARY KEY (`serviceid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `service` */

insert  into `service`(`serviceid`,`lid`,`fname`,`lname`,`trainno`,`place`,`post`,`pin`,`phone`,`email`) values 
(2,5,'sneha','pc',0,'plkd','679503',2147483647,967566767,'1123'),
(3,6,'paruu','p',0,'mezhathur','mezhathur',679534,907434665,'paru@gmail.com');

/*Table structure for table `station` */

DROP TABLE IF EXISTS `station`;

CREATE TABLE `station` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `place` varchar(500) NOT NULL,
  `post` varchar(500) NOT NULL,
  `pin` int(255) NOT NULL,
  `mobileno` bigint(255) NOT NULL,
  `latitude` varchar(30) NOT NULL,
  `longitude` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `station` */

insert  into `station`(`sid`,`name`,`place`,`post`,`pin`,`mobileno`,`latitude`,`longitude`,`email`) values 
(1,'palakkad','plk','olavakode',679503,8921997904,'11.2577899','75.784537','pldstation5@gmail.com'),
(2,'kozhikode','kochi','hhhh',123456,990989887,'12.23.45.9','76.56.89.0','asdf');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `Fname` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  `mobileno` bigint(11) NOT NULL,
  `lid` int(11) NOT NULL,
  `lname` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`userid`,`Fname`,`email`,`mobileno`,`lid`,`lname`) values 
(1,'akhila','gcgf',45678,9,'vvbh'),
(2,'asw ','aa@gmail.com',9446389833,10,'ass '),
(3,'aswin ','as@gmail.com',9445678778,18,'kk ');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
