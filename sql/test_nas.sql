-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: usmp
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

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
-- Dumping data for table `test_nas`
--

LOCK TABLES `test_nas` WRITE;
/*!40000 ALTER TABLE `test_nas` DISABLE KEYS */;
INSERT INTO `test_nas` VALUES (29,'NSHFS01','NSAHFS01','451741000122','146.248.255.51/52','146.248.255.50','146.248.75.121  KHQSNFS','研4','C-27','PH环境清算NFS存储','NETAPP FAS8080','测试环境','7*24','方式7',''),(30,'NSHFS01','NSBHFS02','451741000121','146.248.255.53/54','146.248.255.50','','研4','C-27','PH环境清算NFS存储','NETAPP FAS8080','测试环境','7*24','方式7',''),(31,'NSMVM01','NSMBVM01\n（原NSYBVM01）','451540000109','146.240.104.74','146.240.104.71','','研4','B-3','老云PM集群、老云NFS\n新云MAPP201, MDMZ201','NETAPP FAS8040','测试环境','7*24','方式7',''),(32,'NSMVM02','NSMAVM02','451724000053','145.240.125.202','146.240.125.201','148.1.167.12    MAPP202\n148.1.166.12    MDMZ202\n146.1.167.12    NEWPMNFS\n','研4','B-4','新云MAPP202、MDMZ202、\n新云PM Glance镜像','NETAPP FAS8040','测试环境','','方式7',''),(33,'NSMVM02','NSMBVM02','451724000054','145.240.125.204','146.240.125.201','','研4','B-4','新云NFS、LAPPTMP','NETAPP FAS8040','测试环境','','方式7',''),(34,'NSTVM02','NSTAVM02\n（原NSYAVM02）','451705000208','147.242.1.202','147.242.1.201','146.1.168.11   MANILA \n148.1.168.11   TAPP202 \n','研4','A-22','新云TAPP202、NFS、架构室容器平台(剩余1个RG未使用)','NETAPP FAS8040','测试环境','7*24','方式7',''),(35,'NSTVM02','NSTBVM02\n（原NSYBVM02）','451705000207','147.242.1.203','147.242.1.201','','研4','A-22','冷备','NETAPP FAS8040','测试环境','','方式7',''),(36,'NSTVM03','NSTAVM03\n（原NSYAVM03）','451704000210','146.33.7.12','146.33.7.11','146.34.7.12    PIT_NFS\n146.34.7.11    PIT_VM_KF\n148.1.168.12   TAPP201','研4','A-20','老云PIT原客服楼集群、NFS、LAPPTMP','NETAPP FAS8080','测试环境','7*24','方式7',''),(37,'NSTVM03','NSTAVM03\n（原NSYAVM03）','451704000212','146.33.7.13','146.33.7.11','','研4','A-20','新云TAPP201','NETAPP FAS8080','测试环境','7*24','方式7',''),(38,'NSTVM11','NSTAVM11','451804000088','147.242.22.10','147.242.22.10','148.1.176.11   TAPP203','研4','A-16','新云TAPP203','NETAPP FAS8200','测试环境','','方式7',''),(39,'NSTVM11','NSTBVM11','451804000087','147.242.22.10','147.242.22.10','148.1.176.12   TAPP204','研4','A-16','冷备','NETAPP FAS8200','测试环境','','方式7',''),(40,'NSTVM12','NSTAVM12','451804000086','147.242.22.10','147.242.22.10','146.65.161.11  TTRU201_NFS','研4','A-17','新云TAPP204、托管TTRU01\n托管NFS','NETAPP FAS8200','测试环境','','方式7',''),(41,'NSTVM12','NSTBVM12','451804000085','147.242.22.10','147.242.22.10','148.65.161.11  TTRU201_VM','研4','A-17','冷备','NETAPP FAS8200','测试环境','','方式7',''),(42,'NSTVM13','NSTAVM13','451852000025','147.242.22.26','147.242.22.25','148.1.177.11  TAPP205     ','研4','C15','新云TAPP205','NETAPP FAS8200','测试环境','7*24','方式7',''),(43,'NSTVM13','NSTBVM13','451852000026','147.242.22.28','147.242.22.25','','研4','C15','新云TAPP205','NETAPP FAS8200','测试环境','7*24','方式7',''),(44,'NSTVM14','NSTAVM14','451852000027','147.242.22.31','147.242.22.30','148.1.177.12  TAPP206','研4','C19','新云TAPP206','NETAPP FAS8200','测试环境','7*24','方式7',''),(45,'NSTVM14','NSTBVM14','451852000028','147.242.22.33','147.242.22.30','','研4','C19','新云TAPP206','NETAPP FAS8200','测试环境','7*24','方式7',''),(46,'NSTVM15','NSTAVM15','451821000047','40.1.3.12','40.1.3.11','','研4','A33','UAT测试','NETAPP FAS8200','测试环境','7*24','方式7',''),(47,'NSTVM15','NSTBVM15','451821000048','40.1.3.14','40.1.3.11','','研4','A33','UAT测试','NETAPP FAS8200','测试环境','7*24','方式7',''),(48,'NSTVM16','NSTAVM16','451840000142','40.2.3.12','40.2.3.11','57.0.193.11','研4','A30','UAT二期测试','NETAPP FAS8200','测试环境','7*24','',''),(49,'NSTVM16','NSTBVM16','451840000141','40.2.3.14','40.2.3.11','57.0.194.11','研4','A30','UAT二期测试','NETAPP FAS8200','测试环境','7*24','',''),(50,'NSTSW01','NSTSW01','60911200547','147.242.22.21','147.242.22.21','','研4','A-16','NAS交换机','NETAPP CN1610','测试环境','','',''),(51,'NSTSW02','NSTSW02','60911200343','147.242.22.22','147.242.22.22','','研4','A-17','NAS交换机','NETAPP CN1610','测试环境','','',''),(52,'NSTSW03','NSTSW03','60911200365.0','无','无','','研4','A-22','NAS交换机','NETAPP CN1610','测试环境','','',''),(53,'NSTSW04','NSTSW04','60911200392.0','无','无','','研4','A-22','NAS交换机','NETAPP CN1610','测试环境','','',''),(54,'V3250-01','V3250-01','451433000071','145.0.37.225','145.0.37.225','','研2','X4-6','测试NFS','NETAPP V3250','测试环境','7*24','方式7',''),(55,'V3250-02','V3250-02','451433000070','145.0.37.226','145.0.37.226','','研2','X4-6','测试NFS','NETAPP V3250','测试环境','7*24','方式7',''),(84,'NSHFS01','NSAHFS01','451741000122','146.248.255.51/52','146.248.255.50','146.248.75.121  KHQSNFS','研4','C-27','PH环境清算NFS存储','NETAPP FAS8080','测试环境','7*24','方式7',''),(85,'NSHFS01','NSBHFS02','451741000121','146.248.255.53/54','146.248.255.50','','研4','C-27','PH环境清算NFS存储','NETAPP FAS8080','测试环境','7*24','方式7',''),(86,'NSMVM01','NSMBVM01\n（原NSYBVM01）','451540000109','146.240.104.74','146.240.104.71','','研4','B-3','老云PM集群、老云NFS\n新云MAPP201, MDMZ201','NETAPP FAS8040','测试环境','7*24','方式7',''),(87,'NSMVM02','NSMAVM02','451724000053','145.240.125.202','146.240.125.201','148.1.167.12    MAPP202\n148.1.166.12    MDMZ202\n146.1.167.12    NEWPMNFS\n','研4','B-4','新云MAPP202、MDMZ202、\n新云PM Glance镜像','NETAPP FAS8040','测试环境','','方式7',''),(88,'NSMVM02','NSMBVM02','451724000054','145.240.125.204','146.240.125.201','','研4','B-4','新云NFS、LAPPTMP','NETAPP FAS8040','测试环境','','方式7',''),(89,'NSTVM02','NSTAVM02\n（原NSYAVM02）','451705000208','147.242.1.202','147.242.1.201','146.1.168.11   MANILA \n148.1.168.11   TAPP202 \n','研4','A-22','新云TAPP202、NFS、架构室容器平台(剩余1个RG未使用)','NETAPP FAS8040','测试环境','7*24','方式7',''),(90,'NSTVM02','NSTBVM02\n（原NSYBVM02）','451705000207','147.242.1.203','147.242.1.201','','研4','A-22','冷备','NETAPP FAS8040','测试环境','','方式7',''),(91,'NSTVM03','NSTAVM03\n（原NSYAVM03）','451704000210','146.33.7.12','146.33.7.11','146.34.7.12    PIT_NFS\n146.34.7.11    PIT_VM_KF\n148.1.168.12   TAPP201','研4','A-20','老云PIT原客服楼集群、NFS、LAPPTMP','NETAPP FAS8080','测试环境','7*24','方式7',''),(92,'NSTVM03','NSTAVM03\n（原NSYAVM03）','451704000212','146.33.7.13','146.33.7.11','','研4','A-20','新云TAPP201','NETAPP FAS8080','测试环境','7*24','方式7',''),(93,'NSTVM11','NSTAVM11','451804000088','147.242.22.10','147.242.22.10','148.1.176.11   TAPP203','研4','A-16','新云TAPP203','NETAPP FAS8200','测试环境','','方式7',''),(94,'NSTVM11','NSTBVM11','451804000087','147.242.22.10','147.242.22.10','148.1.176.12   TAPP204','研4','A-16','冷备','NETAPP FAS8200','测试环境','','方式7',''),(95,'NSTVM12','NSTAVM12','451804000086','147.242.22.10','147.242.22.10','146.65.161.11  TTRU201_NFS','研4','A-17','新云TAPP204、托管TTRU01\n托管NFS','NETAPP FAS8200','测试环境','','方式7',''),(96,'NSTVM12','NSTBVM12','451804000085','147.242.22.10','147.242.22.10','148.65.161.11  TTRU201_VM','研4','A-17','冷备','NETAPP FAS8200','测试环境','','方式7',''),(97,'NSTVM13','NSTAVM13','451852000025','147.242.22.26','147.242.22.25','148.1.177.11  TAPP205     ','研4','C15','新云TAPP205','NETAPP FAS8200','测试环境','7*24','方式7',''),(98,'NSTVM13','NSTBVM13','451852000026','147.242.22.28','147.242.22.25','','研4','C15','新云TAPP205','NETAPP FAS8200','测试环境','7*24','方式7',''),(99,'NSTVM14','NSTAVM14','451852000027','147.242.22.31','147.242.22.30','148.1.177.12  TAPP206','研4','C19','新云TAPP206','NETAPP FAS8200','测试环境','7*24','方式7',''),(100,'NSTVM14','NSTBVM14','451852000028','147.242.22.33','147.242.22.30','','研4','C19','新云TAPP206','NETAPP FAS8200','测试环境','7*24','方式7',''),(101,'NSTVM15','NSTAVM15','451821000047','40.1.3.12','40.1.3.11','','研4','A33','UAT测试','NETAPP FAS8200','测试环境','7*24','方式7',''),(102,'NSTVM15','NSTBVM15','451821000048','40.1.3.14','40.1.3.11','','研4','A33','UAT测试','NETAPP FAS8200','测试环境','7*24','方式7',''),(103,'NSTVM16','NSTAVM16','451840000142','40.2.3.12','40.2.3.11','57.0.193.11','研4','A30','UAT二期测试','NETAPP FAS8200','测试环境','7*24','',''),(104,'NSTVM16','NSTBVM16','451840000141','40.2.3.14','40.2.3.11','57.0.194.11','研4','A30','UAT二期测试','NETAPP FAS8200','测试环境','7*24','',''),(105,'NSTSW01','NSTSW01','60911200547','147.242.22.21','147.242.22.21','','研4','A-16','NAS交换机','NETAPP CN1610','测试环境','','',''),(106,'NSTSW02','NSTSW02','60911200343','147.242.22.22','147.242.22.22','','研4','A-17','NAS交换机','NETAPP CN1610','测试环境','','',''),(107,'NSTSW03','NSTSW03','60911200365.0','无','无','','研4','A-22','NAS交换机','NETAPP CN1610','测试环境','','',''),(108,'NSTSW04','NSTSW04','60911200392.0','无','无','','研4','A-22','NAS交换机','NETAPP CN1610','测试环境','','',''),(109,'V3250-01','V3250-01','451433000071','145.0.37.225','145.0.37.225','','研2','X4-6','测试NFS','NETAPP V3250','测试环境','7*24','方式7',''),(110,'V3250-02','V3250-02','451433000070','145.0.37.226','145.0.37.226','','研2','X4-6','测试NFS','NETAPP V3250','测试环境','7*24','方式7',''),(111,'NSHFS01','NSAHFS01','451741000122','146.248.255.51/52','146.248.255.50','146.248.75.121  KHQSNFS','研4','C-27','PH环境清算NFS存储','NETAPP FAS8080','测试环境','7*24','方式7',''),(112,'NSHFS01','NSBHFS02','451741000121','146.248.255.53/54','146.248.255.50','','研4','C-27','PH环境清算NFS存储','NETAPP FAS8080','测试环境','7*24','方式7',''),(113,'NSMVM01','NSMAVM01\n（原NSYAVM01）','451540000108','146.240.104.73','146.240.104.71','148.1.167.11     MAPP201  \n148.1.166.11     MDMZ201  \n146.240.120.200  SVM_NFS\n146.240.120.196  SVM_PD\n146.240.120.197  SVM_PM\n146.240.120.195  SVM_PT\n','研4','B-3','老云PIT、PD集群、','NETAPP FAS8040','测试环境','7*24','方式7',''),(114,'NSMVM01','NSMBVM01\n（原NSYBVM01）','451540000109','146.240.104.74','146.240.104.71','','研4','B-3','老云PM集群、老云NFS\n新云MAPP201, MDMZ201','NETAPP FAS8040','测试环境','7*24','方式7',''),(115,'NSMVM02','NSMAVM02','451724000053','145.240.125.202','146.240.125.201','148.1.167.12    MAPP202\n148.1.166.12    MDMZ202\n146.1.167.12    NEWPMNFS\n','研4','B-4','新云MAPP202、MDMZ202、\n新云PM Glance镜像','NETAPP FAS8040','测试环境','','方式7',''),(116,'NSMVM02','NSMBVM02','451724000054','145.240.125.204','146.240.125.201','','研4','B-4','新云NFS、LAPPTMP','NETAPP FAS8040','测试环境','','方式7',''),(117,'NSTVM02','NSTAVM02\n（原NSYAVM02）','451705000208','147.242.1.202','147.242.1.201','146.1.168.11   MANILA \n148.1.168.11   TAPP202 \n','研4','A-22','新云TAPP202、NFS、架构室容器平台(剩余1个RG未使用)','NETAPP FAS8040','测试环境','7*24','方式7',''),(118,'NSTVM02','NSTBVM02\n（原NSYBVM02）','451705000207','147.242.1.203','147.242.1.201','','研4','A-22','冷备','NETAPP FAS8040','测试环境','','方式7',''),(119,'NSTVM03','NSTAVM03\n（原NSYAVM03）','451704000210','146.33.7.12','146.33.7.11','146.34.7.12    PIT_NFS\n146.34.7.11    PIT_VM_KF\n148.1.168.12   TAPP201','研4','A-20','老云PIT原客服楼集群、NFS、LAPPTMP','NETAPP FAS8080','测试环境','7*24','方式7',''),(120,'NSTVM03','NSTAVM03\n（原NSYAVM03）','451704000212','146.33.7.13','146.33.7.11','','研4','A-20','新云TAPP201','NETAPP FAS8080','测试环境','7*24','方式7',''),(121,'NSTVM11','NSTAVM11','451804000088','147.242.22.10','147.242.22.10','148.1.176.11   TAPP203','研4','A-16','新云TAPP203','NETAPP FAS8200','测试环境','','方式7',''),(122,'NSTVM11','NSTBVM11','451804000087','147.242.22.10','147.242.22.10','148.1.176.12   TAPP204','研4','A-16','冷备','NETAPP FAS8200','测试环境','','方式7',''),(123,'NSTVM12','NSTAVM12','451804000086','147.242.22.10','147.242.22.10','146.65.161.11  TTRU201_NFS','研4','A-17','新云TAPP204、托管TTRU01\n托管NFS','NETAPP FAS8200','测试环境','','方式7',''),(124,'NSTVM12','NSTBVM12','451804000085','147.242.22.10','147.242.22.10','148.65.161.11  TTRU201_VM','研4','A-17','冷备','NETAPP FAS8200','测试环境','','方式7',''),(125,'NSTVM13','NSTAVM13','451852000025','147.242.22.26','147.242.22.25','148.1.177.11  TAPP205     ','研4','C15','新云TAPP205','NETAPP FAS8200','测试环境','7*24','方式7',''),(126,'NSTVM13','NSTBVM13','451852000026','147.242.22.28','147.242.22.25','','研4','C15','新云TAPP205','NETAPP FAS8200','测试环境','7*24','方式7',''),(127,'NSTVM14','NSTAVM14','451852000027','147.242.22.31','147.242.22.30','148.1.177.12  TAPP206','研4','C19','新云TAPP206','NETAPP FAS8200','测试环境','7*24','方式7',''),(128,'NSTVM14','NSTBVM14','451852000028','147.242.22.33','147.242.22.30','','研4','C19','新云TAPP206','NETAPP FAS8200','测试环境','7*24','方式7',''),(129,'NSTVM15','NSTAVM15','451821000047','40.1.3.12','40.1.3.11','','研4','A33','UAT测试','NETAPP FAS8200','测试环境','7*24','方式7',''),(130,'NSTVM15','NSTBVM15','451821000048','40.1.3.14','40.1.3.11','','研4','A33','UAT测试','NETAPP FAS8200','测试环境','7*24','方式7',''),(131,'NSTVM16','NSTAVM16','451840000142','40.2.3.12','40.2.3.11','57.0.193.11','研4','A30','UAT二期测试','NETAPP FAS8200','测试环境','7*24','',''),(132,'NSTVM16','NSTBVM16','451840000141','40.2.3.14','40.2.3.11','57.0.194.11','研4','A30','UAT二期测试','NETAPP FAS8200','测试环境','7*24','',''),(133,'NSTSW01','NSTSW01','60911200547','147.242.22.21','147.242.22.21','','研4','A-16','NAS交换机','NETAPP CN1610','测试环境','','',''),(134,'NSTSW02','NSTSW02','60911200343','147.242.22.22','147.242.22.22','','研4','A-17','NAS交换机','NETAPP CN1610','测试环境','','',''),(135,'NSTSW03','NSTSW03','60911200365.0','无','无','','研4','A-22','NAS交换机','NETAPP CN1610','测试环境','','',''),(136,'NSTSW04','NSTSW04','60911200392.0','无','无','','研4','A-22','NAS交换机','NETAPP CN1610','测试环境','','',''),(137,'V3250-01','V3250-01','451433000071','145.0.37.225','145.0.37.225','','研2','X4-6','测试NFS','NETAPP V3250','测试环境','7*24','方式7',''),(138,'V3250-02','V3250-02','451433000070','145.0.37.226','145.0.37.226','','研2','X4-6','测试NFS','NETAPP V3250','测试环境','7*24','方式7','');
/*!40000 ALTER TABLE `test_nas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-18 11:13:42
