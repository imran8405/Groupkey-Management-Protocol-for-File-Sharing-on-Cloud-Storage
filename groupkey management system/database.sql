/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - system
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`system` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `system`;

/*Table structure for table `addgroup` */

DROP TABLE IF EXISTS `addgroup`;

CREATE TABLE `addgroup` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `groupname` varchar(200) DEFAULT NULL,
  `grouptype` varchar(200) DEFAULT NULL,
  `groupdescription` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `addgroup` */

/*Table structure for table `filesa` */

DROP TABLE IF EXISTS `filesa`;

CREATE TABLE `filesa` (
  `no` int(200) NOT NULL AUTO_INCREMENT,
  `filename` varchar(200) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `file` longblob,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`no`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `filesa` */

insert  into `filesa`(`no`,`filename`,`message`,`file`,`email`) values (1,'q',NULL,'d���}w�qe�Y�19�R�ً�H�Q�` #?','malleswar@gmail.com'),(2,'mine',NULL,'\r�Xq��߉U�p�4k�la<n\rC\"\'�p','malleswar@gmail.com'),(3,'1234','hello','d���}w�qe�Y�19�R�ً�H�Q�` #?','nani@gmail.com'),(4,'mine','hello','\r�Xq��߉U�p�4k�la<n\rC\"\'�p','nani@gmail.com'),(5,'new song',NULL,'٘$zP�s�?3���1���/�A\\~�um���vw[�a3�ط�eUN���� �1�tS��c������\r���Ċ���e�y����(�;�;[/�94�ԝ�T��(�\Z6���	4|\\l���lZ��4�u����5�k/7��ү�A�Y�ePԮwvH9B���0�3k\nz��h�X$��l�K�Qז�p�WC��)o�8�H�A$)�\'��2���oP}��;�\\�}�dϢ���$8���wD��fMX�p�R^�>D��T�ZP���\0Q��p�\0�Qb���B�V�����\nz��޽����?;E�{ec�_p�cT�\'�k�̬��䳮I���8��;{�D�#�O�H(�.D�_','nani@gmail.com'),(6,'123',NULL,'٘$zP�s�?3���1���/�A\\~�um���vw[�a3�ط�eUN���� �1�tS��c������\r���Ċ���e�y����(�;�;[/�94�ԝ�T��(�\Z6���	4|\\l���lZ��4�u����5�k/7��ү�A�Y�ePԮwvH9B���0�3k\nz��h�X$��l�K�Qז�p�WC��)o�8�H�A$)�\'��2���oP}��;�\\�}�dϢ���$8���wD��fMX�p�R^�>D��T�ZP���\0Q��p�\0�Qb���B�V�����\nz��޽����?;E�{ec�_p�cT�\'�k�̬��䳮I���8��;{�D�#�O�H(�.D�_','nani@gmail.com');

/*Table structure for table `groups` */

DROP TABLE IF EXISTS `groups`;

CREATE TABLE `groups` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `groupname` varchar(100) DEFAULT NULL,
  `grouptype` varchar(100) DEFAULT NULL,
  `groupdescription` varchar(100) DEFAULT NULL,
  `members` int(200) DEFAULT NULL,
  `file` longblob,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `groups` */

insert  into `groups`(`id`,`groupname`,`grouptype`,`groupdescription`,`members`,`file`,`email`) values (1,'Group B','def','usefull',3,'d���}w�qe�Y�19�R�ً�H�Q�` #?','nani@gmail.com');

/*Table structure for table `ureg` */

DROP TABLE IF EXISTS `ureg`;

CREATE TABLE `ureg` (
  `slno` int(200) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `number` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`slno`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `ureg` */

insert  into `ureg`(`slno`,`name`,`email`,`number`,`password`,`status`) values (1,'malleswar','malleswar@gmail.com','8684256458','malli','Accepted'),(2,'nani','nani@gmail.com','7674025684','nani','Accepted');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
