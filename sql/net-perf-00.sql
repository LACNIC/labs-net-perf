-- MySQL dump 10.11
--
-- Host: localhost    Database: net-perf
-- ------------------------------------------------------
-- Server version	5.0.77

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
-- Table structure for table `targets`
--

DROP TABLE IF EXISTS `targets`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `targets` (
  `id` int(11) NOT NULL auto_increment,
  `target-handle` varchar(15) NOT NULL,
  `create-datetime` datetime NOT NULL,
  `target-description` varchar(255) default NULL,
  `ipv4` varchar(20) default NULL,
  `ipv6` varchar(60) default NULL,
  `domain` varchar(255) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `target-handle` (`target-handle`),
  KEY `create-datetime` (`create-datetime`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `targets`
--

LOCK TABLES `targets` WRITE;
/*!40000 ALTER TABLE `targets` DISABLE KEYS */;
/*!40000 ALTER TABLE `targets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test-results`
--

DROP TABLE IF EXISTS `test-results`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `test-results` (
  `id` bigint(20) NOT NULL auto_increment COMMENT 'id autonumerico',
  `target-handle` varchar(15) NOT NULL COMMENT 'FK en tabla targets',
  `test-datetime` datetime NOT NULL,
  `status` varchar(10) NOT NULL COMMENT 'OK, FAIL',
  `int01` bigint(20) default NULL,
  `real01` double default NULL,
  `int02` bigint(20) default NULL,
  `real02` double default NULL,
  `int03` bigint(20) default NULL,
  `real03` double default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `target-handle` (`target-handle`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `test-results`
--

LOCK TABLES `test-results` WRITE;
/*!40000 ALTER TABLE `test-results` DISABLE KEYS */;
/*!40000 ALTER TABLE `test-results` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2010-11-08 19:50:32
