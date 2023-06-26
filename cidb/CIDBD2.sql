-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Case_Ivestication_DB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Case_Ivestication_DB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Case_Ivestication_DB` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema classroom
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema classroom
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `classroom` DEFAULT CHARACTER SET utf8mb4 ;
USE `Case_Ivestication_DB` ;

-- -----------------------------------------------------
-- Table `Case_Ivestication_DB`.`Personal_Information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Case_Ivestication_DB`.`Personal_Information` (
  `FirstName` VARCHAR(10) NOT NULL,
  `SecondName` VARCHAR(10) NOT NULL,
  `IdBirtCertNo` INT(10) NOT NULL,
  `PhoneNumber` INT(10) NULL,
  `CountyOfResidence` VARCHAR(15) NULL,
  `SubCounty` VARCHAR(15) NULL,
  `Ward` VARCHAR(15) NULL,
  `Village` VARCHAR(20) NULL,
  `YearOfBirth` INT(4) NULL,
  `EmailAddress` VARCHAR(30) NULL,
  `TestStatus` VARCHAR(6) NULL,
  `ReasonForTesting` VARCHAR(15) NULL,
  `Vaccination` VARCHAR(3) NULL,
  `SexAtBirth` VARCHAR(6) NULL,
  PRIMARY KEY (`IdBirtCertNo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Case_Ivestication_DB`.`Clinical_Information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Case_Ivestication_DB`.`Clinical_Information` (
  `PatientId` INT(4) NOT NULL,
  `PatientClinicalCourse` VARCHAR(15) NOT NULL,
  `Ventilation` CHAR(3) NULL,
  `HealthStatus` VARCHAR(11) NULL,
  `PatientSymptoms` VARCHAR(7) NULL,
  `PatientSigns` VARCHAR(6) NULL,
  `Temparature` FLOAT NULL,
  `UnderlyingConditions` VARCHAR(4) NULL,
  `Personal_Information_IdBirtCertNo` INT(10) NOT NULL,
  PRIMARY KEY (`PatientId`, `Personal_Information_IdBirtCertNo`),
  INDEX `fk_Clinical_Information_Personal_Information_idx` (`Personal_Information_IdBirtCertNo` ASC) VISIBLE,
  CONSTRAINT `fk_Clinical_Information_Personal_Information`
    FOREIGN KEY (`Personal_Information_IdBirtCertNo`)
    REFERENCES `Case_Ivestication_DB`.`Personal_Information` (`IdBirtCertNo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Case_Ivestication_DB`.`Labaratory_information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Case_Ivestication_DB`.`Labaratory_information` (
  `SpecimenCollection` INT NOT NULL,
  `DateofSpecimenCollection` DATE NULL,
  `SpecimenType` VARCHAR(50) NULL,
  `DateSpecimenSent ToTheLab` DATE NULL,
  `NumberOfTheConfirmingLab` INT(2) NULL,
  `AssayUsed` VARCHAR(10) NULL,
  `SequensingDoneOrNotl` VARCHAR(3) NULL,
  `PreliminaryLabResults` VARCHAR(45) NULL,
  `DateofResultConfirmation` VARCHAR(8) NULL,
  `Personal_Information_IdBirtCertNo` INT(10) NOT NULL,
  PRIMARY KEY (`Personal_Information_IdBirtCertNo`),
  INDEX `fk_Labaratory_information_Personal_Information1_idx` (`Personal_Information_IdBirtCertNo` ASC) VISIBLE,
  CONSTRAINT `fk_Labaratory_information_Personal_Information1`
    FOREIGN KEY (`Personal_Information_IdBirtCertNo`)
    REFERENCES `Case_Ivestication_DB`.`Personal_Information` (`IdBirtCertNo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Case_Ivestication_DB`.`ExposureandTravelInformation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Case_Ivestication_DB`.`ExposureandTravelInformation` (
  `Occupation` VARCHAR(30) BINARY NULL,
  `Travelled?` VARCHAR(20) NULL,
  `VisitedAnyHealthFacility` VARCHAR(3) NULL,
  `ExposureToARIP` VARCHAR(30) NULL,
  `ExposureToPCC` VARCHAR(20) NULL,
  `VisitedAnyAnimalMarket` VARCHAR(20) NULL,
  `OccupationID` INT(2) NOT NULL,
  `Personal_Information_IdBirtCertNo` INT(10) NOT NULL,
  PRIMARY KEY (`Personal_Information_IdBirtCertNo`),
  CONSTRAINT `fk_ExposureandTravelInformation_Personal_Information1`
    FOREIGN KEY (`Personal_Information_IdBirtCertNo`)
    REFERENCES `Case_Ivestication_DB`.`Personal_Information` (`IdBirtCertNo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `classroom` ;

-- -----------------------------------------------------
-- Table `classroom`.`class`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `classroom`.`class` (
  `ClassID` INT(2) NOT NULL,
  `ClassName` VARCHAR(10) NOT NULL,
  `NoChairs` INT(2) NOT NULL,
  `nameOfTeacher` VARCHAR(20) NOT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
