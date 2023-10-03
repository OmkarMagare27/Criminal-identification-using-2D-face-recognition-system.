-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.5.19


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema db_accident
--

CREATE DATABASE IF NOT EXISTS db_accident;
USE db_accident;

--
-- Definition of table `tbl_criminal_record`
--

DROP TABLE IF EXISTS `tbl_criminal_record`;
CREATE TABLE `tbl_criminal_record` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `crime_details` varchar(45) NOT NULL,
  `adh_` varchar(45) NOT NULL,
  `em_` varchar(45) NOT NULL,
  `crime_code` varchar(45) NOT NULL DEFAULT 'green',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_criminal_record`
--

/*!40000 ALTER TABLE `tbl_criminal_record` DISABLE KEYS */;
INSERT INTO `tbl_criminal_record` (`id`,`name`,`mobile`,`address`,`crime_details`,`adh_`,`em_`,`crime_code`) VALUES 
 (2,'k','k','k','k','k','k','Red'),
 (3,'k','k','k','k','k','k','Red'),
 (4,'k','k','k','k','k','k','Red'),
 (5,'k','k','k','k','k','k','Red'),
 (6,'k','k','k','k','k','k','Red'),
 (7,'k','k','k','k','k','k','Red'),
 (8,'k','k','k','k','k','k','Red'),
 (9,'k','k','k','k','k','k','Red'),
 (10,'k','k','k','k','k','k','Red'),
 (11,'k','k','k','k','k','k','Red'),
 (12,'k','k','k','k','k','k','Red'),
 (13,'k','k','k','k','k','k','Red'),
 (14,'k','k','k','k','k','k','Red'),
 (15,'k','k','k','k','k','k','Red'),
 (16,'k','k','k','k','k','k','Red'),
 (17,'k','k','k','k','k','k','Red'),
 (18,'k','k','k','k','k','k','Red'),
 (19,'k','k','k','k','k','k','Red'),
 (20,'k','k','k','k','k','k','Red'),
 (21,'k','k','k','k','k','k','Red'),
 (22,'k','k','k','k','k','k','Red'),
 (23,'ok','ok','ok','o','ko','k','Red'),
 (24,'ok','ok','ok','o','ko','k','Red'),
 (25,'ok','ok','ok','o','ko','k','Red'),
 (26,'ok','ok','ok','o','ko','k','Red'),
 (27,'ok','ok','ok','o','ko','k','Red'),
 (28,'ok','ok','ok','o','ko','k','Red'),
 (29,'ok','ok','ok','o','ko','k','Red'),
 (30,'ok','ok','ok','o','ko','k','Red'),
 (31,'ok','ok','ok','o','ko','k','Red'),
 (32,'ok','ok','ok','o','ko','k','Red'),
 (33,'ok','ok','ok','o','ko','k','Red'),
 (34,'ok','ok','ok','o','ko','k','Red'),
 (35,'ok','ok','ok','o','ko','k','Red'),
 (36,'ok','ok','ok','o','ko','k','Red'),
 (37,'ok','ok','ok','o','ko','k','Red'),
 (38,'ok','ok','ok','o','ko','k','Red'),
 (39,'ok','ok','ok','o','ko','k','Red'),
 (40,'ok','ok','ok','o','ko','k','Red'),
 (41,'ok','ok','ok','o','ko','k','Red'),
 (42,'ok','ok','ok','o','ko','k','Red'),
 (43,'ok','ok','ok','o','ko','k','Red');
/*!40000 ALTER TABLE `tbl_criminal_record` ENABLE KEYS */;


--
-- Definition of table `tbl_hospitals`
--

DROP TABLE IF EXISTS `tbl_hospitals`;
CREATE TABLE `tbl_hospitals` (
  `h_id` int(45) unsigned NOT NULL AUTO_INCREMENT,
  `hname` varchar(45) NOT NULL,
  `addr` varchar(45) NOT NULL,
  `lat_2` varchar(45) NOT NULL,
  `long_2` varchar(45) NOT NULL,
  `email2` varchar(45) NOT NULL,
  `mobile2` varchar(45) NOT NULL,
  PRIMARY KEY (`h_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_hospitals`
--

/*!40000 ALTER TABLE `tbl_hospitals` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_hospitals` ENABLE KEYS */;


--
-- Definition of table `tbl_police`
--

DROP TABLE IF EXISTS `tbl_police`;
CREATE TABLE `tbl_police` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `head_name` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `lat_` varchar(45) NOT NULL,
  `long_` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_police`
--

/*!40000 ALTER TABLE `tbl_police` DISABLE KEYS */;
INSERT INTO `tbl_police` (`id`,`head_name`,`address`,`lat_`,`long_`,`email`,`mobile`) VALUES 
 (2,'pramod','pune','18.4454','73.151454','n@gmail.com','7350706868');
/*!40000 ALTER TABLE `tbl_police` ENABLE KEYS */;


--
-- Definition of table `tbl_tain_data`
--

DROP TABLE IF EXISTS `tbl_tain_data`;
CREATE TABLE `tbl_tain_data` (
  `id` int(10) unsigned NOT NULL,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_tain_data`
--

/*!40000 ALTER TABLE `tbl_tain_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_tain_data` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
