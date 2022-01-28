-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 17, 2019 at 02:40 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clinic`
--

-- --------------------------------------------------------

--
-- Table structure for table `dawki`
--

CREATE TABLE `dawki` (
  `idd` int(11) NOT NULL,
  `ile` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `dawki`

--
-- Table structure for table `dawki_i_leki`
--

CREATE TABLE `dawki_i_leki` (
  `iddl` int(11) NOT NULL,
  `idd` int(11) NOT NULL,
  `idl` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `doktorzy`
--

CREATE TABLE `doktorzy` (
  `idd` int(11) NOT NULL,
  `imie` varchar(20) NOT NULL,
  `nazwisko` varchar(35) NOT NULL,
  `pesel` varchar(11) NOT NULL,
  `telefon` varchar(9) NOT NULL,
  `gabinet` int(3) UNSIGNED NOT NULL,
  `godziny` enum('poranne','popoludniowe','wieczorowe') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `dok_i_spec`
--

CREATE TABLE `dok_i_spec` (
  `idd` int(11) NOT NULL,
  `ids` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Table structure for table `leki`
--

CREATE TABLE `leki` (
  `idl` int(11) NOT NULL,
  `nazwa` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `leki`
--
-- --------------------------------------------------------

--
-- Table structure for table `pacjenci`
--

CREATE TABLE `pacjenci` (
  `idp` int(11) NOT NULL,
  `imie` varchar(20) NOT NULL,
  `nazwisko` varchar(35) NOT NULL,
  `pesel` varchar(11) NOT NULL,
  `plec` enum('Kobieta','Mężczyzna') NOT NULL,
  `data_urodzenia` date NOT NULL,
  `adres` varchar(60) NOT NULL,
  `telefon` varchar(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pacjenci`

--
-- Table structure for table `specjalizacje`
--

CREATE TABLE `specjalizacje` (
  `ids` int(11) NOT NULL,
  `nazwa` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `specjalizacje`

-- --------------------------------------------------------

--
-- Table structure for table `wizyty`
--

CREATE TABLE `wizyty` (
  `idw` int(11) NOT NULL,
  `data` datetime NOT NULL,
  `opis` varchar(512) NOT NULL,
  `idd` int(11) NOT NULL,
  `idp` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `wizyty`

--
-- Table structure for table `wiz_i_dawki_i_leki`
--

CREATE TABLE `wiz_i_dawki_i_leki` (
  `idw` int(11) NOT NULL,
  `iddl` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `wiz_i_dawki_i_leki`
--
-- Indexes for dumped tables
--

--
-- Indexes for table `dawki`
--
ALTER TABLE `dawki`
  ADD PRIMARY KEY (`idd`),
  ADD UNIQUE KEY `idrecepty_UNIQUE` (`idd`);

--
-- Indexes for table `dawki_i_leki`
--
ALTER TABLE `dawki_i_leki`
  ADD PRIMARY KEY (`iddl`,`idd`,`idl`),
  ADD UNIQUE KEY `iddl_UNIQUE` (`iddl`),
  ADD KEY `fk_recepta_has_leki_leki1_idx` (`idl`),
  ADD KEY `fk_recepta_has_leki_recepta1_idx` (`idd`);

--
-- Indexes for table `doktorzy`
--
ALTER TABLE `doktorzy`
  ADD PRIMARY KEY (`idd`),
  ADD UNIQUE KEY `idlekarz_UNIQUE` (`idd`),
  ADD UNIQUE KEY `pesel_UNIQUE` (`pesel`),
  ADD UNIQUE KEY `gabinet_UNIQUE` (`gabinet`);

--
-- Indexes for table `dok_i_spec`
--
ALTER TABLE `dok_i_spec`
  ADD PRIMARY KEY (`idd`,`ids`),
  ADD KEY `fk_lekarz_has_specjalizacja_specjalizacja1_idx` (`ids`),
  ADD KEY `fk_lekarz_has_specjalizacja_lekarz1_idx` (`idd`);

--
-- Indexes for table `leki`
--
ALTER TABLE `leki`
  ADD PRIMARY KEY (`idl`),
  ADD UNIQUE KEY `idleki_UNIQUE` (`idl`),
  ADD UNIQUE KEY `nazwa_UNIQUE` (`nazwa`);

--
-- Indexes for table `pacjenci`
--
ALTER TABLE `pacjenci`
  ADD PRIMARY KEY (`idp`),
  ADD UNIQUE KEY `idpacjent_UNIQUE` (`idp`),
  ADD UNIQUE KEY `pesel_UNIQUE` (`pesel`);

--
-- Indexes for table `specjalizacje`
--
ALTER TABLE `specjalizacje`
  ADD PRIMARY KEY (`ids`),
  ADD UNIQUE KEY `idSpecjalizacja_UNIQUE` (`ids`),
  ADD UNIQUE KEY `nazwa_UNIQUE` (`nazwa`);

--
-- Indexes for table `wizyty`
--
ALTER TABLE `wizyty`
  ADD PRIMARY KEY (`idw`),
  ADD UNIQUE KEY `idwizyty_UNIQUE` (`idw`),
  ADD KEY `fk_wizyty_lekarz1_idx` (`idd`),
  ADD KEY `fk_wizyty_pacjent1_idx` (`idp`);

--
-- Indexes for table `wiz_i_dawki_i_leki`
--
ALTER TABLE `wiz_i_dawki_i_leki`
  ADD PRIMARY KEY (`idw`,`iddl`),
  ADD KEY `fk_wizyty_has_dawki_i_leki_dawki_i_leki1_idx` (`iddl`),
  ADD KEY `fk_wizyty_has_dawki_i_leki_wizyty1_idx` (`idw`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dawki`
--
ALTER TABLE `dawki`
  MODIFY `idd` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `dawki_i_leki`
--
ALTER TABLE `dawki_i_leki`
  MODIFY `iddl` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `doktorzy`
--
ALTER TABLE `doktorzy`
  MODIFY `idd` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `leki`
--
ALTER TABLE `leki`
  MODIFY `idl` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `pacjenci`
--
ALTER TABLE `pacjenci`
  MODIFY `idp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `specjalizacje`
--
ALTER TABLE `specjalizacje`
  MODIFY `ids` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `wizyty`
--
ALTER TABLE `wizyty`
  MODIFY `idw` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `dawki_i_leki`
--
ALTER TABLE `dawki_i_leki`
  ADD CONSTRAINT `fk_recepta_has_leki_leki1` FOREIGN KEY (`idl`) REFERENCES `leki` (`idl`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_recepta_has_leki_recepta1` FOREIGN KEY (`idd`) REFERENCES `dawki` (`idd`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `dok_i_spec`
--
ALTER TABLE `dok_i_spec`
  ADD CONSTRAINT `fk_lekarz_has_specjalizacja_lekarz1` FOREIGN KEY (`idd`) REFERENCES `doktorzy` (`idd`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_lekarz_has_specjalizacja_specjalizacja1` FOREIGN KEY (`ids`) REFERENCES `specjalizacje` (`ids`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `wizyty`
--
ALTER TABLE `wizyty`
  ADD CONSTRAINT `fk_wizyty_lekarz1` FOREIGN KEY (`idd`) REFERENCES `doktorzy` (`idd`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_wizyty_pacjent1` FOREIGN KEY (`idp`) REFERENCES `pacjenci` (`idp`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `wiz_i_dawki_i_leki`
--
ALTER TABLE `wiz_i_dawki_i_leki`
  ADD CONSTRAINT `fk_wizyty_has_dawki_i_leki_dawki_i_leki1` FOREIGN KEY (`iddl`) REFERENCES `dawki_i_leki` (`iddl`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_wizyty_has_dawki_i_leki_wizyty1` FOREIGN KEY (`idw`) REFERENCES `wizyty` (`idw`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
