-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: flask_blog
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts` (
  `serial` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `phone_num` varchar(100) DEFAULT NULL,
  `msg` varchar(100) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  KEY `serial` (`serial`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts`
--

LOCK TABLES `contacts` WRITE;
/*!40000 ALTER TABLE `contacts` DISABLE KEYS */;
INSERT INTO `contacts` VALUES (11,'name','07877989951','message','2021-01-16 12:28:30','harshitsh173@gmail.com'),(11,'name','07877989951','lkjkl','2021-01-16 12:29:58','harshitsh173@gmail.com'),(11,'Harshit','9829651493','This is my message','2021-01-16 16:28:50','harshitsh117@gmail.com'),(11,'Stocks','flask-post','None','2021-01-26 14:52:56','An article about stock'),(12,'dlkflkd','9898999998','iiii','2021-01-21 15:33:06','harshitsh18@mmm.com'),(11,'Harhist','07877989951','klj','2021-01-29 18:57:51','harshitsh173@gmail.com');
/*!40000 ALTER TABLE `contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `sno` int(100) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `subheading` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `content` varchar(1000) DEFAULT NULL,
  `img_file` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`),
  UNIQUE KEY `slug` (`slug`),
  KEY `serialnumber` (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,'Article 1','flask-post','An article about stock','Harshit','2020-12-18','Stock (also capital stock) of a corporation is all of the shares into which ownership of the corporation is diffvided.[1] In American English, the shares are collectively known as \"stock\".[1] A single share of the stock represents fractional ownership of the corporation in proportion to the total number of shares. This typically entitles the stockholder to that fraction of the company\'s earnings, proceeds from liquidation of assets (after discharge of all senior claims such as secured and unsecured debt),[2] or voting power, often dividing these up in proportion to the amount of money each stockholder has invested. Not all stock is necessarily equal, as certain classes of stock may be issued for example without voting rights, with enhanced voting rights, or with a certain priority to receive profits or liquidation proceeds before or after other classes of shareholders.','post-bg.jpg'),(2,'Article 2','flask-post1','subheading of article 2','Author 2','2020-12-30','  Lorem ipsum dolor, sit amet consectetur adipisicing elit. Saepe deserunt assumenda facilis obcaecati dolorem odit asperiores expedita quo voluptatibus nobis! Deserunt in dolorem eos repudiandae. Nam minima cum explicabo cumque?',NULL),(3,'Article 3','flask-post2','subheading of article 3','Autohr 3','2020-11-24','  Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam eos ducimus reiciendis praesentium, ipsam quod? Odio ab explicabo mollitia optio culpa obcaecati!',NULL),(4,'Article 4','lkk','lkkl','kljkl','2021-01-28','klkl','Ubuntu-18-04-default-background.jpg');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-08 13:29:59
