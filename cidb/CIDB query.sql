-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema case_ivestication_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema case_ivestication_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `case_ivestication_db` DEFAULT CHARACTER SET utf8mb3 ;
USE `case_ivestication_db` ;

-- -----------------------------------------------------
-- Table `case_ivestication_db`.`personal_information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `case_ivestication_db`.`personal_information` (
  `FirstName` VARCHAR(10) NOT NULL,
  `SecondName` VARCHAR(10) NOT NULL,
  `IdBirtCertNo` INT NOT NULL,
  `PhoneNumber` INT NULL DEFAULT NULL,
  `CountyOfResidence` VARCHAR(15) NULL DEFAULT NULL,
  `SubCounty` VARCHAR(15) NULL DEFAULT NULL,
  `Ward` VARCHAR(15) NULL DEFAULT NULL,
  `Village` VARCHAR(20) NULL DEFAULT NULL,
  `YearOfBirth` INT NULL DEFAULT NULL,
  `EmailAddress` VARCHAR(30) NULL DEFAULT NULL,
  `TestStatus` VARCHAR(6) NULL DEFAULT NULL,
  `ReasonForTesting` VARCHAR(15) NULL DEFAULT NULL,
  `Vaccination` VARCHAR(3) NULL DEFAULT NULL,
  `SexAtBirth` VARCHAR(6) NULL DEFAULT NULL,
  PRIMARY KEY (`IdBirtCertNo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `case_ivestication_db`.`clinical_information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `case_ivestication_db`.`clinical_information` (
  `PatientId` INT NOT NULL,
  `PatientClinicalCourse` VARCHAR(15) NOT NULL,
  `Ventilation` CHAR(3) NULL DEFAULT NULL,
  `HealthStatus` VARCHAR(11) NULL DEFAULT NULL,
  `PatientSymptoms` VARCHAR(7) NULL DEFAULT NULL,
  `PatientSigns` VARCHAR(6) NULL DEFAULT NULL,
  `Temparature` FLOAT NULL DEFAULT NULL,
  `UnderlyingConditions` VARCHAR(4) NULL DEFAULT NULL,
  `Personal_Information_IdBirtCertNo` INT NOT NULL,
  PRIMARY KEY (`PatientId`, `Personal_Information_IdBirtCertNo`),
  INDEX `fk_Clinical_Information_Personal_Information_idx` (`Personal_Information_IdBirtCertNo` ASC) VISIBLE,
  CONSTRAINT `fk_Clinical_Information_Personal_Information`
    FOREIGN KEY (`Personal_Information_IdBirtCertNo`)
    REFERENCES `case_ivestication_db`.`personal_information` (`IdBirtCertNo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `case_ivestication_db`.`exposureandtravelinformation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `case_ivestication_db`.`exposureandtravelinformation` (
  `Occupation` VARCHAR(30) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `Travelled?` VARCHAR(20) NULL DEFAULT NULL,
  `VisitedAnyHealthFacility` VARCHAR(3) NULL DEFAULT NULL,
  `ExposureToARIP` VARCHAR(30) NULL DEFAULT NULL,
  `ExposureToPCC` VARCHAR(20) NULL DEFAULT NULL,
  `VisitedAnyAnimalMarket` VARCHAR(20) NULL DEFAULT NULL,
  `OccupationID` INT NOT NULL,
  `Personal_Information_IdBirtCertNo` INT NOT NULL,
  PRIMARY KEY (`Personal_Information_IdBirtCertNo`),
  CONSTRAINT `fk_ExposureandTravelInformation_Personal_Information1`
    FOREIGN KEY (`Personal_Information_IdBirtCertNo`)
    REFERENCES `case_ivestication_db`.`personal_information` (`IdBirtCertNo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `case_ivestication_db`.`labaratory_information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `case_ivestication_db`.`labaratory_information` (
  `SpecimenCollection` INT NOT NULL,
  `DateofSpecimenCollection` DATE NULL DEFAULT NULL,
  `SpecimenType` VARCHAR(50) NULL DEFAULT NULL,
  `DateSpecimenSent ToTheLab` DATE NULL DEFAULT NULL,
  `NumberOfTheConfirmingLab` INT NULL DEFAULT NULL,
  `AssayUsed` VARCHAR(10) NULL DEFAULT NULL,
  `SequensingDoneOrNotl` VARCHAR(3) NULL DEFAULT NULL,
  `PreliminaryLabResults` VARCHAR(45) NULL DEFAULT NULL,
  `DateofResultConfirmation` VARCHAR(8) NULL DEFAULT NULL,
  `Personal_Information_IdBirtCertNo` INT NOT NULL,
  PRIMARY KEY (`Personal_Information_IdBirtCertNo`),
  INDEX `fk_Labaratory_information_Personal_Information1_idx` (`Personal_Information_IdBirtCertNo` ASC) VISIBLE,
  CONSTRAINT `fk_Labaratory_information_Personal_Information1`
    FOREIGN KEY (`Personal_Information_IdBirtCertNo`)
    REFERENCES `case_ivestication_db`.`personal_information` (`IdBirtCertNo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
