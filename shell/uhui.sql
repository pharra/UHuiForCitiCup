CREATE DATABASE  IF NOT EXISTS `uhui2` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `uhui2`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: uhui2
-- ------------------------------------------------------
-- Server version	5.7.16-log
CREATE USER 'uhui'@'localhost' IDENTIFIED BY 'uhuiforciti';
GRANT ALL ON uhui2.* TO 'uhui'@'localhost';
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
-- Table structure for table `area`
--

DROP TABLE IF EXISTS `area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `area` (
  `areaID` varchar(128) NOT NULL,
  `X` varchar(45) DEFAULT NULL,
  `Y` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`areaID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area`
--

LOCK TABLES `area` WRITE;
/*!40000 ALTER TABLE `area` DISABLE KEYS */;
INSERT INTO `area` VALUES ('0','0','0');
/*!40000 ALTER TABLE `area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `brand` (
  `brandID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(16) NOT NULL,
  `areaID` varchar(128) DEFAULT '地址未录入',
  PRIMARY KEY (`brandID`),
  UNIQUE KEY `brand_name_uindex` (`name`),
  KEY `area_idx` (`areaID`),
  CONSTRAINT `area` FOREIGN KEY (`areaID`) REFERENCES `area` (`areaID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (1,'KFC','0'),(2,'麦当劳','0'),(3,'必胜客','0'),(4,'星巴克','0'),(5,'小米','0'),(6,'华为','0'),(7,'阿迪达斯','0'),(8,'bose','0'),(9,'Apple','0'),(10,'Levis','0'),(11,'高露洁','0'),(12,'公牛','0'),(13,'YSL','0'),(14,'MAC','0'),(15,'斯伯丁','0'),(16,'小天才','0'),(17,'红星','0'),(18,'小天鹅','0'),(19,'携程','0'),(20,'飞猪','0');
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `catID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(16) NOT NULL,
  PRIMARY KEY (`catID`),
  UNIQUE KEY `category_name_uindex` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'家具家居'),(2,'文娱体育'),(3,'旅行住宿'),(4,'服装服饰'),(5,'生活百货'),(6,'电子产品'),(7,'美妆装饰'),(8,'饮食保健');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companycoupon`
--

DROP TABLE IF EXISTS `companycoupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `companycoupon` (
  `ID` varchar(4) NOT NULL,
  `brandID` int(11) NOT NULL,
  `catID` int(11) NOT NULL,
  `value` decimal(10,2) NOT NULL,
  `product` varchar(16) NOT NULL,
  `discount` varchar(16) NOT NULL,
  `pic` varchar(128) NOT NULL,
  `expiredTime` date NOT NULL,
  `remain` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `brand_idx` (`brandID`),
  KEY `cat_idx` (`catID`),
  CONSTRAINT `brand` FOREIGN KEY (`brandID`) REFERENCES `brand` (`brandID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cat` FOREIGN KEY (`catID`) REFERENCES `category` (`catID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companycoupon`
--

LOCK TABLES `companycoupon` WRITE;
/*!40000 ALTER TABLE `companycoupon` DISABLE KEYS */;
/*!40000 ALTER TABLE `companycoupon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coupon`
--

DROP TABLE IF EXISTS `coupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coupon` (
  `couponID` varchar(16) NOT NULL,
  `userID` varchar(16) NOT NULL,
  `brandID` int(11) NOT NULL,
  `catID` int(11) NOT NULL,
  `listPrice` decimal(10,2) NOT NULL,
  `value` int(11) NOT NULL,
  `product` varchar(16) DEFAULT NULL,
  `discount` varchar(16) NOT NULL,
  `pic` varchar(128) DEFAULT NULL,
  `expiredTime` date NOT NULL,
  `onSale` tinyint(4) DEFAULT '0',
  `expired` tinyint(4) DEFAULT '0',
  `used` tinyint(4) DEFAULT '0',
  `store` tinyint(4) DEFAULT '0',
  `bought` date DEFAULT NULL,
  `sold` date DEFAULT NULL,
  PRIMARY KEY (`couponID`,`userID`),
  KEY `brand___fk` (`brandID`),
  KEY `cat___fk` (`catID`),
  KEY `user__fk_idx` (`userID`),
  KEY `value_idx` (`value`),
  CONSTRAINT `brand___fk` FOREIGN KEY (`brandID`) REFERENCES `brand` (`brandID`) ON UPDATE CASCADE,
  CONSTRAINT `cat___fk` FOREIGN KEY (`catID`) REFERENCES `category` (`catID`) ON UPDATE CASCADE,
  CONSTRAINT `user__fk` FOREIGN KEY (`userID`) REFERENCES `user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `value` FOREIGN KEY (`value`) REFERENCES `valueset` (`VID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coupon`
--

LOCK TABLES `coupon` WRITE;
/*!40000 ALTER TABLE `coupon` DISABLE KEYS */;
INSERT INTO `coupon` VALUES ('1','1505213459xmhr',19,7,1.00,1,'飞猪5元即领即用券','满5元减5元','images/pic/flypig.jpg','2017-09-10',0,0,0,1,'2017-09-12',NULL),('10','1505213791frgi',19,7,1.00,1,'飞猪','满199元减100元','images/pic/flypig.jpg','2017-09-10',1,0,0,0,NULL,NULL),('100','1505213791frgi',19,7,1.00,1,'飞猪','满299元减100元','images/pic/flypig.jpg','2017-09-10',1,0,0,0,NULL,NULL),('101','1505213791frgi',19,7,1.00,1,'飞猪','满10元减10元','images/pic/flypig.jpg','2017-09-10',1,0,0,0,NULL,NULL),('102','1505213791frgi',6,6,1.00,1,'阿迪达斯10元抵用券','满99元减10元','images/pic/adidas.png','2017-09-10',1,0,0,0,NULL,NULL),('103','1505213791frgi',1,8,1.00,1,'麦当劳30元券','满30元减30元','images/pic/m.png','2017-09-10',1,0,0,0,NULL,NULL),('104','1505213791frgi',18,7,1.00,1,'携程','满199元减90元','images/pic/ctrip.jpg','2017-09-10',1,0,0,0,NULL,NULL),('105','1505213791frgi',2,8,1.00,1,'必胜客','满88元减5元','images/pic/pizzahut.jpg','2017-09-10',1,0,0,0,NULL,NULL),('106','1505213791frgi',1,8,1.00,1,'麦当劳98-10','满98元减10元','images/pic/m.png','2017-09-10',1,0,0,0,NULL,NULL),('107','1505213791frgi',18,7,100.00,1,'携程5元抵用券','满49元减5元','images/pic/ctrip.jpg','2017-09-10',0,0,0,0,NULL,'2017-09-12'),('108','1505213791frgi',18,7,1.00,1,'携程满200减20','满200元减20元','images/pic/ctrip.jpg','2017-09-10',1,0,0,0,NULL,NULL),('109','1505213791frgi',5,5,1.00,1,'华为官方旗舰店_52','满20元减20元','images/pic/huawei.png','2017-09-10',0,0,0,0,NULL,'2017-09-12'),('11','1505213791frgi',18,7,1.00,1,'携程30元无门槛券','满30元减30元','images/pic/ctrip.jpg','2017-09-10',1,0,0,0,NULL,NULL),('110','1505213791frgi',1,8,1.00,1,'麦当劳','满30元减30元','images/pic/m.png','2017-09-10',1,0,0,0,NULL,NULL),('111','1505213791frgi',18,7,1.00,1,'携程','满10元减10元','images/pic/ctrip.jpg','2017-09-10',1,0,0,0,NULL,NULL),('112','1505213791frgi',18,7,1.00,1,'携程','满5元减5元','images/pic/ctrip.jpg','2017-09-10',1,0,0,0,NULL,NULL),('113','1505213791frgi',3,8,1.00,1,'星巴克','满100元减100元','images/pic/starbucks.png','2017-09-10',1,0,0,0,NULL,NULL),('114','1505213791frgi',17,4,1.00,1,'小天鹅','满5元减5元','images/pic/littlegoose.jpg','2017-09-10',0,0,0,0,NULL,'2017-09-12'),('115','1505213791frgi',7,5,1.00,1,'bose全场通用','满10元减10元','images/pic/bose.png','2017-09-10',1,0,0,0,NULL,NULL),('116','1505213459xmhr',17,4,1.00,1,'小天鹅','满5元减5元','images/pic/littlegoose.jpg','2017-09-10',NULL,NULL,NULL,1,'2017-09-12',NULL),('117','1505213791frgi',17,4,1.00,1,'小天鹅','满99元减10元','images/pic/littlegoose.jpg','2017-09-10',1,0,0,0,NULL,NULL),('118','1505213791frgi',1,8,20.00,1,'麦当劳满168-20','满168元减20元','images/pic/m.png','2017-09-10',0,0,0,1,NULL,NULL),('119','1505213791frgi',2,8,10.00,1,'必胜客','满100元减10元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('12','1505213791frgi',17,4,5.00,1,'小天鹅5元即领即用券','满5元减5元','images/pic/littlegoose.jpg','2017-09-10',0,0,0,1,NULL,NULL),('120','1505213791frgi',2,8,10.00,1,'必胜客','满99元减10元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('121','1505213791frgi',17,4,30.00,1,'小天鹅30元抵用券','满199元减30元','images/pic/littlegoose.jpg','2017-09-10',0,0,0,1,NULL,NULL),('122','1505213791frgi',4,5,5.00,1,'小米指定商品满30减5元抵用券','满30元减5元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('123','1505213791frgi',16,4,30.00,1,'红星美凯龙满300减30','满300元减30元','images/pic/redstar.jpg','2017-09-10',0,0,0,1,NULL,NULL),('124','1505213791frgi',3,8,350.00,1,'星巴克','满999元减350元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('125','1505213791frgi',4,5,5.00,1,'小米全场通用','满99元减5元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('126','1505213791frgi',3,8,5.00,1,'星巴克99减5','满99元减5元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('127','1505213791frgi',4,5,5.00,1,'小米旗舰店','满79元减5元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('128','1505213791frgi',3,8,5.00,1,'星巴克5元抵用券','满59元减5元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('129','1505213791frgi',9,6,8.00,1,'Levis8元抵用券','满88元减8元','images/pic/levis.png','2017-09-10',0,0,0,1,NULL,NULL),('13','1505213791frgi',16,4,20.00,1,'红星美凯龙无门槛20元抵用券','满20元减20元','images/pic/redstar.jpg','2017-09-10',0,0,0,1,NULL,NULL),('130','1505213791frgi',16,4,5.00,1,'红星美凯龙无门槛5元','满5元减5元','images/pic/redstar.jpg','2017-09-10',0,0,0,1,NULL,NULL),('131','1505213791frgi',4,5,15.00,1,'小米专营店','满98元减15元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('132','1505213791frgi',1,8,20.00,1,'麦当劳','满40元减20元','images/pic/m.png','2017-09-10',0,0,0,1,NULL,NULL),('133','1505213791frgi',16,4,3.00,1,'红星美凯龙','满10元减3元','images/pic/redstar.jpg','2017-09-10',0,0,0,1,NULL,NULL),('134','1505213791frgi',16,4,60.00,1,'红星美凯龙满599-60','满599元减60元','images/pic/redstar.jpg','2017-09-10',0,0,0,1,NULL,NULL),('135','1505213791frgi',7,5,50.00,1,'bose 满499元减50元','满499元减50元','images/pic/bose.png','2017-09-10',0,0,0,1,NULL,NULL),('136','1505213791frgi',16,4,10.00,1,'红星美凯龙','满10元减10元','images/pic/redstar.jpg','2017-09-10',0,0,0,1,NULL,NULL),('137','1505213791frgi',1,8,100.00,1,'麦当劳满799元减100元','满799元减100元','images/pic/m.png','2017-09-10',0,0,0,1,NULL,NULL),('138','1505213791frgi',16,4,10.00,1,'红星美凯龙满69减10元','满69元减10元','images/pic/redstar.jpg','2017-09-10',0,0,0,1,NULL,NULL),('139','1505213791frgi',2,8,5.00,1,'必胜客满59减5抵用券','满59元减5元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('14','1505213791frgi',16,4,5.00,1,'红星美凯龙满68减5元','满68元减5元','images/pic/redstar.jpg','2017-09-10',0,0,0,1,NULL,NULL),('140','1505213791frgi',4,5,10.00,1,'小米官方旗舰店','满35元减10元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('141','1505213791frgi',15,3,10.00,1,'小天才','满11元减10元','images/pic/littlegenius.jpg','2017-09-10',0,0,0,1,NULL,NULL),('142','1505213791frgi',15,3,2.00,1,'小天才','满2.1元减2元','images/pic/littlegenius.jpg','2017-09-10',0,0,0,1,NULL,NULL),('143','1505213791frgi',3,8,20.00,1,'星巴克','满21元减20元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('144','1505213791frgi',2,8,20.00,1,'必胜客','满199元减20元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('145','1505213791frgi',15,3,20.00,1,'小天才','满99元减20元','images/pic/littlegenius.jpg','2017-09-10',0,0,0,1,NULL,NULL),('146','1505213791frgi',2,8,10.00,1,'必胜客','满25元减10元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('147','1505213791frgi',15,3,20.00,1,'小天才','满200元减20元','images/pic/littlegenius.jpg','2017-09-10',0,0,0,1,NULL,NULL),('148','1505213791frgi',5,5,10.00,1,'自营华为10元抵用券','满119元减10元','images/pic/huawei.png','2017-09-10',0,0,0,1,NULL,NULL),('149','1505213791frgi',15,3,10.00,1,'小天才满10减10','满10元减10元','images/pic/littlegenius.jpg','2017-09-10',0,0,0,1,NULL,NULL),('15','1505213791frgi',14,3,10.00,1,'斯伯丁满69减10元抵用券','满69元减10元','images/pic/spalding.jpg','2017-09-10',0,0,0,1,NULL,NULL),('150','1505213791frgi',14,3,10.00,1,'斯伯丁','满99元减10元','images/pic/spalding.jpg','2017-09-10',0,0,0,1,NULL,NULL),('151','1505213791frgi',1,8,20.00,1,'麦当劳','满100元减20元','images/pic/m.png','2017-09-10',0,0,0,1,NULL,NULL),('152','1505213791frgi',5,5,10.00,1,'华为品牌抵用券199元减10元','满199元减10元','images/pic/huawei.png','2017-09-10',0,0,0,1,NULL,NULL),('153','1505213791frgi',14,3,5.00,1,'斯伯丁','满99元减5元','images/pic/spalding.jpg','2017-09-10',0,0,0,1,NULL,NULL),('154','1505213791frgi',3,8,10.00,1,'星巴克89-10','满89元减10元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('155','1505213791frgi',14,3,10.00,1,'斯伯丁','满99元减10元','images/pic/spalding.jpg','2017-09-10',0,0,0,1,NULL,NULL),('156','1505213791frgi',14,3,10.00,1,'斯伯丁','满30元减10元','images/pic/spalding.jpg','2017-09-10',0,0,0,1,NULL,NULL),('157','1505213791frgi',5,5,5.00,1,'华为旗舰店','满15元减5元','images/pic/huawei.png','2017-09-10',0,0,0,1,NULL,NULL),('158','1505213791frgi',14,3,10.00,1,'斯伯丁','满30元减10元','images/pic/spalding.jpg','2017-09-10',0,0,0,1,NULL,NULL),('159','1505213791frgi',3,8,5.00,1,'星巴克全国通用','满15元减5元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('16','1505213791frgi',5,5,20.00,1,'华为官方旗舰店','满20元减20元','images/pic/huawei.png','2017-09-10',0,0,0,1,NULL,NULL),('160','1505213791frgi',14,3,20.00,1,'斯伯丁','满59.8元减20元','images/pic/spalding.jpg','2017-09-10',0,0,0,1,NULL,NULL),('161','1505213791frgi',13,2,30.00,1,'MAC','满99元减30元','images/pic/MAC.jpg','2017-09-10',0,0,0,1,NULL,NULL),('162','1505213791frgi',2,8,10.00,1,'必胜客','满99元减10元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('163','1505213791frgi',13,2,10.00,1,'MAC','满29元减10元','images/pic/MAC.jpg','2017-09-10',0,0,0,1,NULL,NULL),('164','1505213791frgi',2,8,10.00,1,'必胜客','满99元减10元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('165','1505213791frgi',13,2,10.00,1,'MAC','满100元减10元','images/pic/MAC.jpg','2017-09-10',0,0,0,1,NULL,NULL),('166','1505213791frgi',6,6,5.00,1,'阿迪达斯旗舰店','满79元减5元','images/pic/adidas.png','2017-09-10',0,0,0,1,NULL,NULL),('167','1505213791frgi',13,2,5.00,1,'MAC','满38元减5元','images/pic/MAC.jpg','2017-09-10',0,0,0,1,NULL,NULL),('168','1505213791frgi',13,2,40.00,1,'MAC40元抵用券','满199元减40元','images/pic/MAC.jpg','2017-09-10',0,0,0,1,NULL,NULL),('169','1505213791frgi',3,8,80.00,1,'星巴克满299元减80元抵用券','满299元减80元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('17','1505213791frgi',13,2,10.00,1,'MAC10元无门槛券','满10元减10元','images/pic/MAC.jpg','2017-09-10',0,0,0,1,NULL,NULL),('170','1505213791frgi',2,8,5.00,1,'必胜客满20-5','满20元减5元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('171','1505213791frgi',7,5,200.00,1,'bose 满999减200','满999元减200元','images/pic/bose.png','2017-09-10',0,0,0,1,NULL,NULL),('172','1505213791frgi',3,8,10.00,1,'星巴克全国通用','满99元减10元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('173','1505213791frgi',13,2,30.00,1,'MAC','满288元减30元','images/pic/MAC.jpg','2017-09-10',0,0,0,1,NULL,NULL),('174','1505213791frgi',4,5,3.00,1,'自营小米满30-3','满30元减3元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('175','1505213791frgi',4,5,5.00,1,'7月小米49-5','满49元减5元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('176','1505213791frgi',13,2,10.00,1,'MAC','满10元减10元','images/pic/MAC.jpg','2017-09-10',0,0,0,1,NULL,NULL),('177','1505213791frgi',13,2,5.00,1,'MAC','满5.01元减5元','images/pic/MAC.jpg','2017-09-10',0,0,0,1,NULL,NULL),('178','1505213791frgi',12,2,10.00,1,'YSL','满10元减10元','images/pic/YSL.jpg','2017-09-10',0,0,0,1,NULL,NULL),('179','1505213791frgi',5,5,20.00,1,'华为全场通用','满21元减20元','images/pic/huawei.png','2017-09-10',0,0,0,1,NULL,NULL),('18','1505213791frgi',3,8,5.00,1,'星巴克5元抵用券','满38元减5元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('180','1505213791frgi',12,2,20.00,1,'YSL','满159元减20元','images/pic/YSL.jpg','2017-09-10',0,0,0,1,NULL,NULL),('181','1505213791frgi',12,2,20.00,1,'YSL','满199元减20元','images/pic/YSL.jpg','2017-09-10',0,0,0,1,NULL,NULL),('182','1505213791frgi',4,5,20.00,1,'百丽小米专营店','满199元减20元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('183','1505213791frgi',12,2,50.00,1,'YSL','满299元减50元','images/pic/YSL.jpg','2017-09-10',0,0,0,1,NULL,NULL),('184','1505213791frgi',12,2,10.00,1,'YSL满11减10','满11元减10元','images/pic/YSL.jpg','2017-09-10',0,0,0,1,NULL,NULL),('185','1505213791frgi',3,8,10.00,1,'星巴克89-10','满89元减10元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('186','1505213791frgi',2,8,20.00,1,'必胜客','满199元减20元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('187','1505213791frgi',12,2,5.00,1,'YSL','满6元减5元','images/pic/YSL.jpg','2017-09-10',0,0,0,1,NULL,NULL),('188','1505213791frgi',12,2,5.00,1,'YSL','满99元减5元','images/pic/YSL.jpg','2017-09-10',0,0,0,1,NULL,NULL),('189','1505213791frgi',12,2,5.00,1,'YSL','满39元减5元','images/pic/YSL.jpg','2017-09-10',0,0,0,1,NULL,NULL),('190','1505213791frgi',5,5,120.00,1,'华为满1500减120','满1500元减120元','images/pic/huawei.png','2017-09-10',0,0,0,1,NULL,NULL),('191','1505213791frgi',5,5,100.00,1,'华为专卖店','满500元减100元','images/pic/huawei.png','2017-09-10',0,0,0,1,NULL,NULL),('192','1505213791frgi',1,8,50.00,1,'麦当劳','满200元减50元','images/pic/m.png','2017-09-10',0,0,0,1,NULL,NULL),('193','1505213791frgi',6,6,50.00,1,'阿迪达斯旗舰店','满199元减50元','images/pic/adidas.png','2017-09-10',0,0,0,1,NULL,NULL),('194','1505213791frgi',12,2,20.00,1,'YSL','满99元减20元','images/pic/YSL.jpg','2017-09-10',0,0,0,1,NULL,NULL),('195','1505213791frgi',12,2,30.00,1,'YSL','满149元减30元','images/pic/YSL.jpg','2017-09-10',0,0,0,1,NULL,NULL),('196','1505213791frgi',11,1,400.00,1,'公牛','满1600元减400元','images/pic/bull.jpg','2017-09-10',0,0,0,1,NULL,NULL),('197','1505213791frgi',9,6,10.00,1,'Levis全场通用','满50元减10元','images/pic/levis.png','2017-09-10',0,0,0,1,NULL,NULL),('198','1505213791frgi',4,5,5.00,1,'小米专营店','满20元减5元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('199','1505213791frgi',11,1,40.00,1,'公牛','满199元减40元','images/pic/bull.jpg','2017-09-10',0,0,0,1,NULL,NULL),('2','1505213791frgi',1,8,8.00,1,'麦当劳满46元减8元抵用券','满46元减8元','images/pic/m.png','2017-09-10',0,0,0,1,NULL,NULL),('20','1505213791frgi',2,8,5.00,1,'必胜客满49减5','满49元减5元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('200','1505213791frgi',11,1,20.00,1,'公牛','满80元减20元','images/pic/bull.jpg','2017-09-10',0,0,0,1,NULL,NULL),('201','1505213791frgi',11,1,20.00,1,'公牛','满99元减20元','images/pic/bull.jpg','2017-09-10',0,0,0,1,NULL,NULL),('21','1505213791frgi',2,8,5.00,1,'必胜客','满5元减5元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('22','1505213791frgi',11,1,8.00,1,'公牛满46元减8元抵用券','满46元减8元','images/pic/bull.jpg','2017-09-10',0,0,0,1,NULL,NULL),('23','1505213791frgi',11,1,10.00,1,'公牛满69减10','满69元减10元','images/pic/bull.jpg','2017-09-10',0,0,0,1,NULL,NULL),('25','1505213791frgi',11,1,20.00,1,'公牛指定产品无门槛抵用券','满20元减20元','images/pic/bull.jpg','2017-09-10',0,0,0,1,NULL,NULL),('26','1505213791frgi',10,1,10.00,1,'高露洁满99减10元抵用券','满99元减10元','images/pic/colgate.png','2017-09-10',0,0,0,1,NULL,NULL),('27','1505213791frgi',4,5,5.00,1,'小米满49减5元抵用券','满49元减5元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('28','1505213791frgi',7,5,5.00,1,'bose 5元抵用券','满5元减5元','images/pic/bose.png','2017-09-10',0,0,0,1,NULL,NULL),('29','1505213791frgi',10,1,1.00,1,'高露洁1元无门槛抵用券','满1元减1元','images/pic/colgate.png','2017-09-10',0,0,0,1,NULL,NULL),('3','1505213791frgi',4,5,10.00,1,'小米满69减10','满69元减10元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('30','1505213791frgi',2,8,100.00,1,'必胜客','满199元减100元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('31','1505213791frgi',9,6,30.00,1,'Levis部分产品30元无门槛券','满30元减30元','images/pic/levis.png','2017-09-10',0,0,0,1,NULL,NULL),('32','1505213791frgi',3,8,5.00,1,'星巴克5元即领即用券','满5元减5元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('33','1505213791frgi',10,1,20.00,1,'高露洁无门槛20元抵用券','满20元减20元','images/pic/colgate.png','2017-09-10',0,0,0,1,NULL,NULL),('34','1505213791frgi',10,1,5.00,1,'高露洁满68减5元','满68元减5元','images/pic/colgate.png','2017-09-10',0,0,0,1,NULL,NULL),('35','1505213791frgi',1,8,10.00,1,'麦当劳满69减10元抵用券','满69元减10元','images/pic/m.png','2017-09-10',0,0,0,1,NULL,NULL),('36','1505213791frgi',10,1,20.00,1,'高露洁','满20元减20元','images/pic/colgate.png','2017-09-10',0,0,0,1,NULL,NULL),('37','1505213791frgi',9,6,10.00,1,'Levis10元无门槛券','满10元减10元','images/pic/levis.png','2017-09-10',0,0,0,1,NULL,NULL),('38','1505213791frgi',10,1,5.00,1,'高露洁5元抵用券','满38元减5元','images/pic/colgate.png','2017-09-10',0,0,0,1,NULL,NULL),('40','1505213791frgi',5,5,5.00,1,'华为满49减5','满49元减5元','images/pic/huawei.png','2017-09-10',0,0,0,1,NULL,NULL),('41','1505213791frgi',10,1,5.00,1,'高露洁','满5元减5元','images/pic/colgate.png','2017-09-10',0,0,0,1,NULL,NULL),('42','1505213791frgi',7,5,8.00,1,'bose 79减8','满79元减8元','images/pic/bose.png','2017-09-10',0,0,0,1,NULL,NULL),('43','1505213791frgi',10,1,9.00,1,'高露洁满79减9','满79元减9元','images/pic/colgate.png','2017-09-10',0,0,0,1,NULL,NULL),('44','1505213791frgi',8,5,5.00,1,'Apple49-5元','满49元减5元','images/pic/apple.png','2017-09-10',0,0,0,1,NULL,NULL),('45','1505213791frgi',1,8,8.00,1,'麦当劳68减8抵用券','满68元减8元','images/pic/m.png','2017-09-10',0,0,0,1,NULL,NULL),('46','1505213791frgi',10,1,30.00,1,'高露洁满299减30券','满299元减30元','images/pic/colgate.png','2017-09-10',0,0,0,1,NULL,NULL),('47','1505213791frgi',3,8,5.00,1,'星巴克满39减5元抵用券','满39元减5元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('48','1505213791frgi',10,1,5.00,1,'高露洁满49-5元','满49元减5元','images/pic/colgate.png','2017-09-10',0,0,0,1,NULL,NULL),('49','1505213791frgi',10,1,10.00,1,'高露洁满78元减10元','满78元减10元','images/pic/colgate.png','2017-09-10',0,0,0,1,NULL,NULL),('5','1505213791frgi',2,8,20.00,1,'必胜客指定产品无门槛抵用券','满20元减20元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('50','1505213791frgi',5,5,30.00,1,'华为满299减30券','满299元减30元','images/pic/huawei.png','2017-09-10',0,0,0,1,NULL,NULL),('51','1505213791frgi',4,5,10.00,1,'小米满50减10','满50元减10元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('53','1505213791frgi',2,8,10.00,1,'必胜客10元抵用券','满168元减10元','images/pic/pizzahut.jpg','2017-09-10',0,0,0,1,NULL,NULL),('54','1505213791frgi',10,1,10.00,1,'高露洁10元抵用券','满10元减10元','images/pic/colgate.png','2017-09-10',0,0,0,1,NULL,NULL),('57','1505213791frgi',5,5,9.00,1,'铂金及以上会员准时达券','抵扣9元','images/pic/huawei.png','2017-09-10',0,0,0,1,NULL,NULL),('58','1505213791frgi',3,8,30.00,1,'星巴克满99减30抵用券','满99元减30元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('59','1505213791frgi',6,6,5.00,1,'阿迪达斯5元抵用券','满49元减5元','images/pic/adidas.png','2017-09-10',0,0,0,1,NULL,NULL),('60','1505213791frgi',5,5,5.00,1,'华为19-5','满19元减5元','images/pic/huawei.png','2017-09-10',0,0,0,1,NULL,NULL),('61','1505213791frgi',1,8,30.00,1,'麦当劳99-30','满99元减30元','images/pic/m.png','2017-09-10',0,0,0,1,NULL,NULL),('64','1505213791frgi',4,5,5.00,1,'小米5元无门槛','满5元减5元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('66','1505213791frgi',3,8,5.00,1,'星巴克全场','满6元减5元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('69','1505213791frgi',8,5,5.00,1,'Apple59-5','满59元减5元','images/pic/apple.png','2017-09-10',0,0,0,1,NULL,NULL),('7','1505213791frgi',5,5,5.00,1,'华为满49减5元抵用券','满49元减5元','images/pic/huawei.png','2017-09-10',0,0,0,1,NULL,NULL),('72','1505213791frgi',6,6,15.00,1,'阿迪达斯99减15抵用券','满99元减15元','images/pic/adidas.png','2017-09-10',0,0,0,1,NULL,NULL),('73','1505213791frgi',7,5,20.00,1,'bose 199减20券','满199元减20元','images/pic/bose.png','2017-09-10',0,0,0,1,NULL,NULL),('76','1505213791frgi',4,5,5.00,1,'小米官方店','满5元减5元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('78','1505213791frgi',9,6,5.00,1,'Levis5元抵用券','满49元减5元','images/pic/levis.png','2017-09-10',0,0,0,1,NULL,NULL),('79','1505213791frgi',1,8,15.00,1,'麦当劳15元抵用券','满199元减15元','images/pic/m.png','2017-09-10',0,0,0,1,NULL,NULL),('80','1505213791frgi',6,6,10.00,1,'阿迪达斯旗舰店','满25元减10元','images/pic/adidas.png','2017-09-10',0,0,0,1,NULL,NULL),('82','1505213791frgi',3,8,5.00,1,'星巴克星冰乐','满11元减5元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('84','1505213791frgi',6,6,5.00,1,'阿迪达斯旗舰店','满10元减5元','images/pic/adidas.png','2017-09-10',0,0,0,1,NULL,NULL),('85','1505213791frgi',6,6,137.00,1,'阿迪达斯专营','满299元减137元','images/pic/adidas.png','2017-09-10',0,0,0,1,NULL,NULL),('90','1505213791frgi',8,5,5.00,1,'Apple满55-5元','满55元减5元','images/pic/apple.png','2017-09-10',0,0,0,1,NULL,NULL),('92','1505213791frgi',3,8,10.00,1,'星巴克10元无门槛','满10元减10元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('93','1505213791frgi',3,8,5.00,1,'星巴克无门槛5元抵用券','满5元减5元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('94','1505213791frgi',4,5,4.00,1,'小米部分商品立减4元','满4元减4元','images/pic/mi.png','2017-09-10',0,0,0,1,NULL,NULL),('96','1505213791frgi',3,8,5.00,1,'洋河立减5元抵用券','满5元减5元','images/pic/starbucks.png','2017-09-10',0,0,0,1,NULL,NULL),('99','1505213791frgi',6,6,20.00,1,'阿迪达斯299-20券','满299元减20元','images/pic/adidas.png','2017-09-10',0,0,0,1,NULL,NULL),('Coupon object','1505213459xmhr',5,5,100.00,1,'华为官方旗舰店_52','满20元减20元','images/pic/huawei.png','2017-09-10',1,NULL,NULL,0,'2017-09-12',NULL);
/*!40000 ALTER TABLE `coupon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `like`
--

DROP TABLE IF EXISTS `like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `like` (
  `uid` varchar(16) NOT NULL,
  `cid` varchar(16) NOT NULL,
  PRIMARY KEY (`uid`,`cid`),
  KEY `coupon_idx` (`cid`),
  CONSTRAINT `coupon` FOREIGN KEY (`cid`) REFERENCES `coupon` (`couponID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `user` FOREIGN KEY (`uid`) REFERENCES `user` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like`
--

LOCK TABLES `like` WRITE;
/*!40000 ALTER TABLE `like` DISABLE KEYS */;
/*!40000 ALTER TABLE `like` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `limit`
--

DROP TABLE IF EXISTS `limit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `limit` (
  `couponID` varchar(16) NOT NULL,
  `content` varchar(128) NOT NULL,
  PRIMARY KEY (`couponID`,`content`),
  KEY `limit_coupon_couponID_fk` (`couponID`),
  CONSTRAINT `limit_coupon_couponID_fk` FOREIGN KEY (`couponID`) REFERENCES `coupon` (`couponID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `limit`
--

LOCK TABLES `limit` WRITE;
/*!40000 ALTER TABLE `limit` DISABLE KEYS */;
/*!40000 ALTER TABLE `limit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `message` (
  `messageID` varchar(16) NOT NULL,
  `userID` varchar(16) DEFAULT NULL,
  `content` varchar(128) DEFAULT NULL,
  `time` date DEFAULT NULL,
  `messageCat` enum('上架的优惠券被购买','上架的优惠券即将过期','上架的优惠券已过期','关注的优惠券即将过期','关注的优惠券已被购买','关注的优惠券已下架','我的优惠券即将过期','我的优惠券已过期','系统通知') DEFAULT NULL,
  `hasRead` tinyint(1) NOT NULL DEFAULT '0',
  `couponID` varchar(16) NOT NULL,
  `hasSend` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`messageID`),
  KEY `messege_user_ID_fk` (`userID`),
  CONSTRAINT `message_user_ID_fk` FOREIGN KEY (`userID`) REFERENCES `user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES ('1505223125hjqi','1505213459xmhr','关注的优惠券已被购买','2017-09-12','关注的优惠券已被购买',0,'114',0),('1505223216yroy','1505213459xmhr','上架的优惠券被购买','2017-09-12','上架的优惠券被购买',0,'116',0),('1505223350dkhe','1505213459xmhr','上架的优惠券被购买','2017-09-12','上架的优惠券被购买',0,'1',0);
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `ID` varchar(16) NOT NULL,
  `nickname` varchar(32) NOT NULL,
  `phoneNum` varchar(11) DEFAULT NULL,
  `gender` enum('男','女') NOT NULL,
  `avatar` varchar(128) DEFAULT '/static/images/default_avatar.jpg',
  `password` varchar(32) NOT NULL,
  `email` varchar(32) DEFAULT NULL,
  `UCoin` decimal(10,2) NOT NULL DEFAULT '0.00',
  `hasConfirm` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `User_ID_uindex` (`ID`),
  UNIQUE KEY `user_nickname_uindex` (`nickname`),
  UNIQUE KEY `user_phoneNum_uindex` (`phoneNum`),
  UNIQUE KEY `uhuiwebapp_user_email_uindex` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('1504619052wlvw','zww','13711146102','男','images/avatar/default.jpg','9df0cb7d54607109d65e8c5cc81f8d25',NULL,0.00,1),('1505213459xmhr','测试账号1密码123456','13000000000','男','images/avatar/default.jpg','9df0cb7d54607109d65e8c5cc81f8d25',NULL,9999896.00,1),('1505213791frgi','测试账号2密码123','13111111111','男','images/avatar/default.jpg','95ce56719f009d7920f3062cbf028e58',NULL,0.00,1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `valuecalculate`
--

DROP TABLE IF EXISTS `valuecalculate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `valuecalculate` (
  `vid` int(11) NOT NULL,
  `listprice` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`vid`),
  CONSTRAINT `vid` FOREIGN KEY (`vid`) REFERENCES `valueset` (`VID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `valuecalculate`
--

LOCK TABLES `valuecalculate` WRITE;
/*!40000 ALTER TABLE `valuecalculate` DISABLE KEYS */;
INSERT INTO `valuecalculate` VALUES (1,100.00);
/*!40000 ALTER TABLE `valuecalculate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `valueset`
--

DROP TABLE IF EXISTS `valueset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `valueset` (
  `VID` int(11) NOT NULL AUTO_INCREMENT,
  `value` decimal(10,2) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`VID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `valueset`
--

LOCK TABLES `valueset` WRITE;
/*!40000 ALTER TABLE `valueset` DISABLE KEYS */;
INSERT INTO `valueset` VALUES (1,0.00,'测试分组1');
/*!40000 ALTER TABLE `valueset` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-16  1:07:56
