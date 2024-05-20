-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2024 at 09:25 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

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
-- Table structure for table `account_role`
--

CREATE TABLE `account_role` (
  `ACCOUNT_ROLE_ID` int(11) NOT NULL,
  `ACCOUNT_ID` int(11) DEFAULT NULL,
  `ROLE_ID` int(11) DEFAULT NULL,
  `GRANTER_ACCOUNT` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `account_role`
--

INSERT INTO `account_role` (`ACCOUNT_ROLE_ID`, `ACCOUNT_ID`, `ROLE_ID`, `GRANTER_ACCOUNT`) VALUES
(1, 1, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `account_session`
--

CREATE TABLE `account_session` (
  `ACCOUNT_SESSION_ID` int(11) NOT NULL,
  `ACCOUNT_ID` int(11) NOT NULL,
  `SESSION_KEY` varchar(255) NOT NULL,
  `IP_ADDRESS` varchar(255) NOT NULL,
  `DATETIME_CREATED` datetime NOT NULL,
  `DATETIME_LAST_REQUEST` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `activity`
--

CREATE TABLE `activity` (
  `ACTIVITY_ID` int(11) NOT NULL,
  `SEMESTER_ID` int(11) DEFAULT NULL,
  `CODE` varchar(10) DEFAULT NULL,
  `LABEL` varchar(100) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
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

INSERT INTO `activity` (`ACTIVITY_ID`, `SEMESTER_ID`, `CODE`, `LABEL`, `DESCRIPTION`, `LOCATION`, `COLLEGE_ID`, `ACTIVITY_START_DATE`, `ACTIVITY_END_DATE`, `ACTIVITY_STATUS`, `APPROVED_BY`, `APPROVED_DATE`, `DISAPPROVED_BY`, `DISAPPROVED_DATE`, `DISAPPROVED_REASON`, `DISAPROVED_DATETIME`, `DATETIME_CREATED`, `DATETIME_UPDATED`, `STATUSCODE`) VALUES
(202401, 232402, '001', 'Intramurals', 'Yearly Intramural Event', 'Banke(Main)', 0, '2024-05-01', '2024-05-10', 'active', NULL, NULL, NULL, NULL, NULL, NULL, '2024-05-18 02:48:30', '2024-05-18 02:48:30', 1),
(202402, NULL, 'SNACK_PA', 'SNACK Partylist', NULL, 'Boni', NULL, '2001-01-01', '2001-02-02', 'active', 1, NULL, NULL, NULL, NULL, NULL, '2024-05-18 14:08:48', NULL, NULL),
(202403, NULL, NULL, '1', NULL, 'Boni', NULL, '2001-10-20', '2002-12-21', 'active', 1, NULL, NULL, NULL, NULL, NULL, '2024-05-18 14:22:43', NULL, NULL),
(202404, NULL, NULL, 'College Week', NULL, 'Main', NULL, '2024-10-20', '2024-10-25', 'active', 1, NULL, NULL, NULL, NULL, NULL, '2024-05-18 14:22:43', NULL, NULL),
(202405, NULL, NULL, 'USG', NULL, 'Boni', NULL, '2004-01-20', '2005-01-21', 'active', 1, NULL, NULL, NULL, NULL, NULL, '2024-05-18 16:10:27', NULL, NULL),
(202406, NULL, NULL, 'CCS Night', NULL, 'Boni', NULL, '2024-05-20', '2024-05-28', 'active', 1, NULL, NULL, NULL, NULL, NULL, '2024-05-18 16:10:27', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `ATTENDANCE_ID` int(11) NOT NULL,
  `ACTIVITY_ID` int(11) DEFAULT NULL,
  `ACTIVITY_CODE` varchar(255) DEFAULT NULL,
  `CARD_ID` varchar(255) DEFAULT NULL,
  `STUDENT_ID` int(11) DEFAULT NULL,
  `EMPLOYEE_ID` int(11) DEFAULT NULL,
  `STUDENT_NUMBER` varchar(255) DEFAULT NULL,
  `TRANSACTION_TYPE_ID` int(11) DEFAULT NULL,
  `USER_ID` int(11) DEFAULT NULL,
  `IP_ADDRESS` varchar(255) DEFAULT NULL,
  `DATETIME_CREATED` datetime DEFAULT NULL,
  `DATE_CREATED` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `event_log`
--

CREATE TABLE `event_log` (
  `EVENT_LOG_ID` int(11) NOT NULL,
  `ACCOUNT_ID` int(11) DEFAULT NULL,
  `EVENT_DESCRIPTION` varchar(255) DEFAULT NULL,
  `IP_ADDRESS` varchar(255) DEFAULT NULL,
  `DATETIME_ADDED` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `ROLE_ID` int(11) NOT NULL,
  `LABEL` varchar(255) NOT NULL,
  `DESCRIPTION` varchar(255) NOT NULL,
  `DATETIME_CREATED` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`ROLE_ID`, `LABEL`, `DESCRIPTION`, `DATETIME_CREATED`) VALUES
(1, 'ADMIN', 'Administrator', '2024-05-17 16:23:19'),
(2, 'OSA', 'Office of Student Affairs', '2024-05-17 16:23:19');

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
-- Table structure for table `transaction_type`
--

CREATE TABLE `transaction_type` (
  `TRANSACTION_TYPE_ID` int(11) NOT NULL,
  `LABEL` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

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
-- Indexes for table `account_role`
--
ALTER TABLE `account_role`
  ADD PRIMARY KEY (`ACCOUNT_ROLE_ID`),
  ADD UNIQUE KEY `ROLE_ID` (`ROLE_ID`),
  ADD KEY `ACCOUNT_ID` (`ACCOUNT_ID`);

--
-- Indexes for table `account_session`
--
ALTER TABLE `account_session`
  ADD PRIMARY KEY (`ACCOUNT_SESSION_ID`);

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
  ADD PRIMARY KEY (`ATTENDANCE_ID`);

--
-- Indexes for table `event_log`
--
ALTER TABLE `event_log`
  ADD PRIMARY KEY (`EVENT_LOG_ID`),
  ADD KEY `ACCOUNT_ID` (`ACCOUNT_ID`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`ROLE_ID`);

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
-- Indexes for table `transaction_type`
--
ALTER TABLE `transaction_type`
  ADD PRIMARY KEY (`TRANSACTION_TYPE_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `ACCOUNT_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `account_session`
--
ALTER TABLE `account_session`
  MODIFY `ACCOUNT_SESSION_ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `activity`
--
ALTER TABLE `activity`
  MODIFY `ACTIVITY_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=202407;

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `ATTENDANCE_ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `ROLE_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
-- Constraints for table `account_role`
--
ALTER TABLE `account_role`
  ADD CONSTRAINT `ACCOUNT_ROLE_IBFK_1` FOREIGN KEY (`ACCOUNT_ID`) REFERENCES `account` (`ACCOUNT_ID`);

--
-- Constraints for table `activity`
--
ALTER TABLE `activity`
  ADD CONSTRAINT `ACTIVITY_IBFK_1` FOREIGN KEY (`APPROVED_BY`) REFERENCES `account` (`ACCOUNT_ID`),
  ADD CONSTRAINT `ACTIVITY_IBFK_2` FOREIGN KEY (`DISAPPROVED_BY`) REFERENCES `account` (`ACCOUNT_ID`),
  ADD CONSTRAINT `ACTIVITY_IBFK_3` FOREIGN KEY (`STATUSCODE`) REFERENCES `statuscode` (`STATUSCODE_ID`);

--
-- Constraints for table `event_log`
--
ALTER TABLE `event_log`
  ADD CONSTRAINT `EVENT_LOG_IBFK_1` FOREIGN KEY (`ACCOUNT_ID`) REFERENCES `account` (`ACCOUNT_ID`);

--
-- Constraints for table `statuscode`
--
ALTER TABLE `statuscode`
  ADD CONSTRAINT `STATUSCODE_IBFK_1` FOREIGN KEY (`STATUSCODE_GROUP_ID`) REFERENCES `statuscode_group` (`STATUS_GROUP_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
