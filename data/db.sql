-- MySQL dump 10.13  Distrib 5.6.13, for Win64 (x86_64)
--
-- Host: localhost    Database: haofu
-- ------------------------------------------------------
-- Server version	5.6.13

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
-- Table structure for table `Account`
--

DROP TABLE IF EXISTS `Account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Account` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `LoginId` varchar(45) NOT NULL,
  `Pwd` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Locked` bit(1) NOT NULL DEFAULT b'0',
  `LMT` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `AT` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `DEL` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `LoginId_UNIQUE` (`LoginId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='账户';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Account`
--

LOCK TABLES `Account` WRITE;
/*!40000 ALTER TABLE `Account` DISABLE KEYS */;
/*!40000 ALTER TABLE `Account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Game`
--

DROP TABLE IF EXISTS `Game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Game` (
  `Id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增长Id',
  `Name` varchar(16) NOT NULL COMMENT '名字',
  `Code` varchar(16) NOT NULL COMMENT '编码，SEO使用',
  `LMT` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后修改时间',
  `AT` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '添加时间',
  `DEL` bit(1) NOT NULL COMMENT '删除标志位',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Name_UNIQUE` (`Name`),
  UNIQUE KEY `Code_UNIQUE` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Game`
--

LOCK TABLES `Game` WRITE;
/*!40000 ALTER TABLE `Game` DISABLE KEYS */;
/*!40000 ALTER TABLE `Game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Server`
--

DROP TABLE IF EXISTS `Server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Server` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `GameId` int(11) NOT NULL,
  `Name` varchar(16) NOT NULL,
  `OpenTime` datetime NOT NULL,
  `Feature` varchar(32) NOT NULL,
  `Ratio` varchar(16) NOT NULL,
  `Version` varchar(16) NOT NULL,
  `ISP` varchar(16) NOT NULL,
  `LMT` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `AT` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `DEL` bit(1) NOT NULL,
  `Uri` varchar(500) NOT NULL,
  `Contact` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Server`
--

LOCK TABLES `Server` WRITE;
/*!40000 ALTER TABLE `Server` DISABLE KEYS */;
INSERT INTO `Server` VALUES (1,1,'1','2013-07-30 21:05:09','xx','xxx','xxx','dd','2013-07-30 13:05:09','2013-07-30 13:05:09','\0','',NULL),(2,1,'1','2013-07-30 21:05:31','xx','xxx','xxx','dd','2013-07-30 13:05:31','2013-07-30 13:05:31','\0','',NULL),(3,1,'1','2013-07-30 21:05:33','xx','xxx','xxx','dd','2013-07-30 13:05:33','2013-07-30 13:05:33','\0','',NULL),(4,1,'','2013-07-30 21:22:33','xx','xxx','xxx','dd','2013-07-30 13:22:33','2013-07-30 13:22:33','\0','',NULL);
/*!40000 ALTER TABLE `Server` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-08-21 11:30:40
