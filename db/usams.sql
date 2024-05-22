-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 22, 2024 at 03:01 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `usams`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `ACCOUNT_ID` int(11) NOT NULL,
  `USERNAME` varchar(255) NOT NULL,
  `PASSWORD` varchar(255) NOT NULL,
  `LASTNAME` varchar(255) DEFAULT NULL,
  `FIRSTNAME` varchar(255) DEFAULT NULL,
  `MIDDLENAME` varchar(255) DEFAULT NULL,
  `DATETIME_CREATED` datetime DEFAULT current_timestamp(),
  `STATUSCODE` int(11) DEFAULT NULL,
  `EMP_ACCOUNT` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`ACCOUNT_ID`, `USERNAME`, `PASSWORD`, `LASTNAME`, `FIRSTNAME`, `MIDDLENAME`, `DATETIME_CREATED`, `STATUSCODE`, `EMP_ACCOUNT`) VALUES
(1, 'admin', 'admin123', 'Doe', 'John', 'Dan', '2024-05-17 22:22:47', 1, 1001),
(2, 'osad', 'osad123', 'Dan', 'Jane', 'Doe', '2024-05-17 22:25:31', 1, 1002),
(6, 'jane', '123', NULL, NULL, NULL, NULL, NULL, NULL),
(7, 'mocah', '123', 'Doe', 'MIcah', NULL, NULL, NULL, NULL),
(8, 'mocah', '123', 'Doe', 'MIcah', NULL, NULL, NULL, NULL),
(9, 'ralph', '12345', 'Enrique', 'Ralph', NULL, NULL, NULL, NULL),
(10, 'ralph', '12345', 'Enrique', 'Ralph', NULL, NULL, NULL, NULL),
(11, 'ralph', '12345', 'Enrique', 'Ralph', NULL, NULL, NULL, NULL),
(12, 'ralph', '12345', 'Enrique', 'Ralph', NULL, NULL, NULL, NULL),
(13, 'ralph', '12345', 'Enrique', 'Ralph', NULL, NULL, NULL, NULL),
(14, 'ralph', '12345', 'Enrique', 'Ralph', NULL, NULL, NULL, NULL),
(15, 'ralph', '12345', 'Enrique', 'Ralph', NULL, NULL, NULL, NULL),
(16, 'ralph', '12345', 'Enrique', 'Ralph', NULL, NULL, NULL, NULL),
(17, 'vardox', '123', 'Marinay', 'Fred', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `activity`
--

CREATE TABLE `activity` (
  `ACTIVITY_ID` int(11) NOT NULL,
  `SEMESTER_ID` int(11) DEFAULT NULL,
  `CODE` varchar(10) DEFAULT NULL,
  `LABEL` varchar(255) DEFAULT NULL,
  `DEPARTMENT` varchar(255) DEFAULT NULL,
  `LOCATION` varchar(100) DEFAULT NULL,
  `COLLEGE_ID` int(11) DEFAULT NULL,
  `ACTIVITY_START_DATE` date DEFAULT NULL,
  `ACTIVITY_END_DATE` date DEFAULT NULL,
  `ACTIVITY_STATUS` enum('active','inactive') DEFAULT NULL,
  `APPROVED_BY` int(11) DEFAULT NULL,
  `APPROVED_DATE` date DEFAULT NULL,
  `DISAPPROVED_BY` int(11) DEFAULT NULL,
  `DISAPPROVED_DATE` date DEFAULT NULL,
  `DISAPPROVED_REASON` varchar(255) DEFAULT NULL,
  `DISAPROVED_DATETIME` datetime DEFAULT NULL,
  `DATETIME_CREATED` datetime DEFAULT NULL,
  `DATETIME_UPDATED` datetime DEFAULT NULL,
  `STATUSCODE` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `activity`
--

INSERT INTO `activity` (`ACTIVITY_ID`, `SEMESTER_ID`, `CODE`, `LABEL`, `DEPARTMENT`, `LOCATION`, `COLLEGE_ID`, `ACTIVITY_START_DATE`, `ACTIVITY_END_DATE`, `ACTIVITY_STATUS`, `APPROVED_BY`, `APPROVED_DATE`, `DISAPPROVED_BY`, `DISAPPROVED_DATE`, `DISAPPROVED_REASON`, `DISAPROVED_DATETIME`, `DATETIME_CREATED`, `DATETIME_UPDATED`, `STATUSCODE`) VALUES
(3, NULL, NULL, 'Intramurals', 'USG', 'Annex', NULL, '2024-05-22', '2024-05-23', 'inactive', 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, NULL, NULL, 'Day2', 'CCS', 'Main', NULL, '2024-05-10', '2024-05-24', 'inactive', 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `ATTENDANCE_ID` int(11) NOT NULL,
  `ACTIVITY_ID` int(255) DEFAULT NULL,
  `STUDENT_NUMBER` int(255) DEFAULT NULL,
  `DATETIME_CREATED` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`ATTENDANCE_ID`, `ACTIVITY_ID`, `STUDENT_NUMBER`, `DATETIME_CREATED`) VALUES
(1, 3, 2001, '2024-05-22 06:03:06'),
(2, 3, 2002, '2024-05-22 07:38:00'),
(3, 3, 2003, '2024-05-22 07:38:01'),
(4, 3, 2004, '2024-05-22 07:38:02'),
(5, 3, 2005, '2024-05-22 07:38:03'),
(6, 3, 2006, '2024-05-22 07:38:04'),
(7, 4, 2001, '2024-05-22 07:40:55'),
(8, 4, 2002, '2024-05-22 07:40:56'),
(9, 4, 2003, '2024-05-22 07:40:56'),
(10, 4, 2004, '2024-05-22 07:40:57'),
(11, 4, 2005, '2024-05-22 07:40:58'),
(12, 4, 2006, '2024-05-22 07:40:58');

-- --------------------------------------------------------

--
-- Table structure for table `statuscode`
--

CREATE TABLE `statuscode` (
  `STATUSCODE_ID` int(11) NOT NULL,
  `LABEL` varchar(255) NOT NULL,
  `STATUSCODE_GROUP_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `statuscode`
--

INSERT INTO `statuscode` (`STATUSCODE_ID`, `LABEL`, `STATUSCODE_GROUP_ID`) VALUES
(1, 'ACTIVATED', 1),
(2, 'DEACTIVATED', 2);

-- --------------------------------------------------------

--
-- Table structure for table `statuscode_group`
--

CREATE TABLE `statuscode_group` (
  `STATUS_GROUP_ID` int(11) NOT NULL,
  `TABLE_NAME` varchar(255) NOT NULL,
  `RANGE_START` varchar(255) NOT NULL,
  `RANGE_END` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `statuscode_group`
--

INSERT INTO `statuscode_group` (`STATUS_GROUP_ID`, `TABLE_NAME`, `RANGE_START`, `RANGE_END`) VALUES
(1, 'ON', '', ''),
(2, 'OFF', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `STUDENT_NUMBER` int(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `middlename` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`STUDENT_NUMBER`, `lastname`, `firstname`, `middlename`) VALUES
(2001, 'ORIG', 'AL GABRIEL', NULL),
(2002, 'MARINAY', 'WILFREDO', NULL),
(2003, 'ESPINOSA', 'PRINCESS MICAH', NULL),
(2004, 'TAN', 'KYLE', NULL),
(2005, 'DOE', 'JOHN', NULL),
(2006, 'DELA CRUZ', 'JANE', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`ACCOUNT_ID`),
  ADD KEY `ACCOUNT_IBFK1` (`STATUSCODE`);

--
-- Indexes for table `activity`
--
ALTER TABLE `activity`
  ADD PRIMARY KEY (`ACTIVITY_ID`),
  ADD KEY `APPROVED_BY` (`APPROVED_BY`),
  ADD KEY `DISAPPROVED_BY` (`DISAPPROVED_BY`),
  ADD KEY `STATUSCODE` (`STATUSCODE`);

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`ATTENDANCE_ID`),
  ADD KEY `ATT_FK_ACT_ID` (`ACTIVITY_ID`),
  ADD KEY `STD_FK_NUM` (`STUDENT_NUMBER`);

--
-- Indexes for table `statuscode`
--
ALTER TABLE `statuscode`
  ADD PRIMARY KEY (`STATUSCODE_ID`),
  ADD KEY `STATUSCODE_GROUP_ID` (`STATUSCODE_GROUP_ID`);

--
-- Indexes for table `statuscode_group`
--
ALTER TABLE `statuscode_group`
  ADD PRIMARY KEY (`STATUS_GROUP_ID`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`STUDENT_NUMBER`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `ACCOUNT_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `activity`
--
ALTER TABLE `activity`
  MODIFY `ACTIVITY_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=202407;

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `ATTENDANCE_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `statuscode`
--
ALTER TABLE `statuscode`
  MODIFY `STATUSCODE_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `statuscode_group`
--
ALTER TABLE `statuscode_group`
  MODIFY `STATUS_GROUP_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `ACCOUNT_IBFK1` FOREIGN KEY (`STATUSCODE`) REFERENCES `statuscode` (`STATUSCODE_ID`);

--
-- Constraints for table `activity`
--
ALTER TABLE `activity`
  ADD CONSTRAINT `ACTIVITY_IBFK_1` FOREIGN KEY (`APPROVED_BY`) REFERENCES `account` (`ACCOUNT_ID`),
  ADD CONSTRAINT `ACTIVITY_IBFK_2` FOREIGN KEY (`DISAPPROVED_BY`) REFERENCES `account` (`ACCOUNT_ID`),
  ADD CONSTRAINT `ACTIVITY_IBFK_3` FOREIGN KEY (`STATUSCODE`) REFERENCES `statuscode` (`STATUSCODE_ID`);

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `ATT_FK_ACT_ID` FOREIGN KEY (`ACTIVITY_ID`) REFERENCES `activity` (`ACTIVITY_ID`),
  ADD CONSTRAINT `STD_FK_NUM` FOREIGN KEY (`STUDENT_NUMBER`) REFERENCES `students` (`student_number`);

--
-- Constraints for table `statuscode`
--
ALTER TABLE `statuscode`
  ADD CONSTRAINT `STATUSCODE_IBFK_1` FOREIGN KEY (`STATUSCODE_GROUP_ID`) REFERENCES `statuscode_group` (`STATUS_GROUP_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
