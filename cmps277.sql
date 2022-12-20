-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:8889
-- Generation Time: May 03, 2021 at 12:47 PM
-- Server version: 8.0.18
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cmps277`
--

-- --------------------------------------------------------

--
-- Table structure for table `civilian`
--

DROP TABLE IF EXISTS `civilian`;
CREATE TABLE IF NOT EXISTS `civilian` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `PatientID` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `PatientID` (`PatientID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `district`
--

DROP TABLE IF EXISTS `district`;
CREATE TABLE IF NOT EXISTS `district` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `GovID` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `GovID` (`GovID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `district`
--

INSERT INTO `district` (`ID`, `Name`, `GovID`) VALUES
(1, 'Hamra', 1);

-- --------------------------------------------------------

--
-- Table structure for table `governate`
--

DROP TABLE IF EXISTS `governate`;
CREATE TABLE IF NOT EXISTS `governate` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `governate`
--

INSERT INTO `governate` (`ID`, `Name`) VALUES
(1, 'Beirut');

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

DROP TABLE IF EXISTS `hospital`;
CREATE TABLE IF NOT EXISTS `hospital` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Phone` int(8) NOT NULL,
  `Capacity` int(11) NOT NULL,
  `DistrictID` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `DistrictID` (`DistrictID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hospital`
--

INSERT INTO `hospital` (`ID`, `Name`, `Phone`, `Capacity`, `DistrictID`) VALUES
(1, 'AUBMC', 3500000, 19000, 1);

-- --------------------------------------------------------

--
-- Table structure for table `medical`
--

DROP TABLE IF EXISTS `medical`;
CREATE TABLE IF NOT EXISTS `medical` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Is_Doctor` tinyint(1) NOT NULL,
  `Is_Vaccinator` tinyint(1) NOT NULL,
  `PatientID` int(11) NOT NULL,
  `HospID` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `PatientID` (`PatientID`),
  KEY `HospID` (`HospID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `medicalrecord`
--

DROP TABLE IF EXISTS `medicalrecord`;
CREATE TABLE IF NOT EXISTS `medicalrecord` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Is_Pregnant` tinyint(1) NOT NULL,
  `Has_BloodPressure` tinyint(1) NOT NULL,
  `Has_Diabetes` tinyint(1) NOT NULL,
  `Has_Cancer` tinyint(1) NOT NULL,
  `Has_RespiratoryD` tinyint(1) NOT NULL,
  `Has_HeartD` tinyint(1) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `medicalrecord`
--

INSERT INTO `medicalrecord` (`ID`, `Is_Pregnant`, `Has_BloodPressure`, `Has_Diabetes`, `Has_Cancer`, `Has_RespiratoryD`, `Has_HeartD`) VALUES
(1, 0, 1, 1, 0, 0, 0),
(2, 0, 1, 1, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `nationalpersonnel`
--

DROP TABLE IF EXISTS `nationalpersonnel`;
CREATE TABLE IF NOT EXISTS `nationalpersonnel` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `PatientID` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `PatientID` (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
CREATE TABLE IF NOT EXISTS `patient` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Fname` varchar(30) NOT NULL,
  `Lname` varchar(30) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `Phone` int(8) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `CovidPositive` tinyint(1) NOT NULL DEFAULT '0',
  `MedRecID` int(11) NOT NULL,
  `DistID` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `MedRecID` (`MedRecID`),
  KEY `DistID` (`DistID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`ID`, `Fname`, `Lname`, `Gender`, `Phone`, `Email`, `CovidPositive`, `MedRecID`, `DistID`) VALUES
(2, 'Christopher', 'Farah', 'Female', 99, 'c', 0, 1, 1),
(6, 'Ali', 'Aloush', 'Male', 9, 'c', 0, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `vaccine`
--

DROP TABLE IF EXISTS `vaccine`;
CREATE TABLE IF NOT EXISTS `vaccine` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DateTaken` date NOT NULL,
  `HospID` int(11) NOT NULL,
  `PatientID` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `HospID` (`HospID`),
  KEY `PatientID` (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `civilian`
--
ALTER TABLE `civilian`
  ADD CONSTRAINT `civilian_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `patient` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `district`
--
ALTER TABLE `district`
  ADD CONSTRAINT `district_ibfk_1` FOREIGN KEY (`GovID`) REFERENCES `governate` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `hospital`
--
ALTER TABLE `hospital`
  ADD CONSTRAINT `hospital_ibfk_1` FOREIGN KEY (`DistrictID`) REFERENCES `district` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `medical`
--
ALTER TABLE `medical`
  ADD CONSTRAINT `medical_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `patient` (`ID`),
  ADD CONSTRAINT `medical_ibfk_2` FOREIGN KEY (`HospID`) REFERENCES `hospital` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `nationalpersonnel`
--
ALTER TABLE `nationalpersonnel`
  ADD CONSTRAINT `nationalpersonnel_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `patient` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `patient`
--
ALTER TABLE `patient`
  ADD CONSTRAINT `patient_ibfk_1` FOREIGN KEY (`MedRecID`) REFERENCES `medicalrecord` (`ID`),
  ADD CONSTRAINT `patient_ibfk_2` FOREIGN KEY (`DistID`) REFERENCES `district` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `vaccine`
--
ALTER TABLE `vaccine`
  ADD CONSTRAINT `vaccine_ibfk_1` FOREIGN KEY (`HospID`) REFERENCES `hospital` (`ID`),
  ADD CONSTRAINT `vaccine_ibfk_2` FOREIGN KEY (`PatientID`) REFERENCES `patient` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
