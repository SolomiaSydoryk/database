SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema panel_bd
-- -----------------------------------------------------
DROP TABLE IF EXISTS panel_bd.interactive_advertising_panels_has_commercials;
DROP TABLE IF EXISTS panel_bd.supermarket_has_interactive_advertising_panel;
DROP TABLE IF EXISTS panel_bd.supermarket_has_manufacturer;
DROP TABLE IF EXISTS panel_bd.supermarket_has_section;
DROP TABLE IF EXISTS panel_bd.owner_has_supermarket;
DROP TABLE IF EXISTS panel_bd.employee;
DROP TABLE IF EXISTS panel_bd.commercials;
DROP TABLE IF EXISTS panel_bd.owner;
DROP TABLE IF EXISTS panel_bd.supermarket;
DROP TABLE IF EXISTS panel_bd.address;
DROP TABLE IF EXISTS panel_bd.manufacturer;
DROP TABLE IF EXISTS panel_bd.section;
DROP TABLE IF EXISTS panel_bd.interactive_advertising_panel;
DROP TABLE IF EXISTS panel_bd.specifications;

-- -----------------------------------------------------
-- Schema panel_bd
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS panel_bd DEFAULT CHARACTER SET utf8 ;
USE panel_bd ;

-- -----------------------------------------------------
-- Table panel_bd.specifications
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.specifications (
  id INT NOT NULL AUTO_INCREMENT,
  model_year INT NOT NULL,
  screen_resolution_capacity VARCHAR(25) NOT NULL,
  display_type VARCHAR(15) NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table panel_bd.section
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.section (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table panel_bd.interactive_advertising_panel
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.interactive_advertising_panel (
  id INT NOT NULL AUTO_INCREMENT,
  number VARCHAR(20) NOT NULL,
  specifications_id INT NOT NULL,
  section_id INT NOT NULL,
  PRIMARY KEY (id, specifications_id, section_id),
  INDEX fk_interactive_advertising_panel_specifications1_idx (specifications_id ASC) VISIBLE,
  INDEX fk_interactive_advertising_panel_section1_idx (section_id ASC) VISIBLE,
  CONSTRAINT fk_interactive_advertising_panel_specifications1
    FOREIGN KEY (specifications_id)
    REFERENCES panel_bd.specifications (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_interactive_advertising_panel_section1
    FOREIGN KEY (section_id)
    REFERENCES panel_bd.section (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table panel_bd.manufacturer
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.manufacturer (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(30) NOT NULL,
  email VARCHAR(45) NOT NULL,
  phone VARCHAR(13) NOT NULL,
  site VARCHAR(45) NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX name_UNIQUE (name ASC) VISIBLE,
  UNIQUE INDEX email_UNIQUE (email ASC) VISIBLE,
  UNIQUE INDEX phone_UNIQUE (phone ASC) VISIBLE,
  UNIQUE INDEX site_UNIQUE (site ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table panel_bd.address
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.address (
  id INT NOT NULL AUTO_INCREMENT,
  street_name VARCHAR(45) NOT NULL,
  number_of_building INT NOT NULL,
  city VARCHAR(45) NOT NULL,
  region VARCHAR(45) NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table panel_bd.supermarket
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.supermarket (
  id INT NOT NULL AUTO_INCREMENT,
  supermarket_name VARCHAR(40) NOT NULL,
  description_of_supermarket VARCHAR(60) NOT NULL,
  area FLOAT NOT NULL,
  trade_network VARCHAR(45) NOT NULL,
  business_hours VARCHAR(15) NOT NULL,
  average_number_of_visitors INT NOT NULL,
  address_id INT NOT NULL,
  PRIMARY KEY (id, address_id),
  INDEX fk_supermarket_address1_idx (address_id ASC) VISIBLE,
  CONSTRAINT fk_supermarket_address1
    FOREIGN KEY (address_id)
    REFERENCES panel_bd.address (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table panel_bd.owner
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.owner (
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(45) NOT NULL,
  phone VARCHAR(13) NOT NULL,
  name VARCHAR(30) NOT NULL,
  surname VARCHAR(45) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX phone_UNIQUE (phone ASC) VISIBLE,
  UNIQUE INDEX email_UNIQUE (email ASC) VISIBLE
) ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table panel_bd.commercials
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.commercials (
  id INT NOT NULL AUTO_INCREMENT,
  duration VARCHAR(15) NOT NULL,
  manufacturer VARCHAR(30) NOT NULL,
  trademark_in_video VARCHAR(30) NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table panel_bd.interactive_advertising_panels_has_commercials
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.interactive_advertising_panel_has_commercials (
  interactive_advertising_panel_id INT NOT NULL,
  commercials_id INT NOT NULL,
  PRIMARY KEY (interactive_advertising_panel_id, commercials_id),
  INDEX fk_interactive_advertising_panel_has_commercials_commercia_idx (commercials_id ASC) VISIBLE,
  INDEX fk_interactive_advertising_panel_has_commercials_interactiv_idx (interactive_advertising_panel_id ASC) VISIBLE,
  CONSTRAINT fk_interactive_advertising_panel_has_commercials_interactive1
    FOREIGN KEY (interactive_advertising_panel_id)
    REFERENCES panel_bd.interactive_advertising_panel (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_interactive_advertising_panel_has_commercials_commercials1
    FOREIGN KEY (commercials_id)
    REFERENCES panel_bd.commercials (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table panel_bd.employee
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.employee (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  surname VARCHAR(45) NOT NULL,
  phone VARCHAR(13) NOT NULL,
  position VARCHAR(30) NOT NULL,
  supermarket_id INT NOT NULL,
  supermarket_address_id INT NOT NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX phone_UNIQUE (phone ASC) VISIBLE,
  INDEX fk_employee_supermarket1_idx (supermarket_id ASC, supermarket_address_id ASC) VISIBLE,
  CONSTRAINT fk_employee_supermarket1
    FOREIGN KEY (supermarket_id , supermarket_address_id)
    REFERENCES panel_bd.supermarket (id , address_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table panel_bd.supermarket_has_section
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.supermarket_has_section (
  supermarket_id INT NOT NULL,
  supermarket_address_id INT NOT NULL,
  section_id INT NOT NULL,
  PRIMARY KEY (supermarket_id, supermarket_address_id, section_id),
  INDEX fk_supermarket_has_section_section1_idx (section_id ASC) VISIBLE,
  INDEX fk_supermarket_has_section_supermarket1_idx (supermarket_id ASC, supermarket_address_id ASC) VISIBLE,
  CONSTRAINT fk_supermarket_has_section_supermarket1
    FOREIGN KEY (supermarket_id , supermarket_address_id)
    REFERENCES panel_bd.supermarket (id , address_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_supermarket_has_section_section1
    FOREIGN KEY (section_id)
    REFERENCES panel_bd.section (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table panel_bd.owner_has_supermarket
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.owner_has_supermarket (
  owner_id INT NOT NULL,
  supermarket_id INT NOT NULL,
  supermarket_address_id INT NOT NULL,
  PRIMARY KEY (owner_id, supermarket_id, supermarket_address_id),
  INDEX fk_owner_has_supermarket_supermarket1_idx (supermarket_id ASC, supermarket_address_id ASC) VISIBLE,
  INDEX fk_owner_has_supermarket_owner1_idx (owner_id ASC) VISIBLE,
  CONSTRAINT fk_owner_has_supermarket_owner1
    FOREIGN KEY (owner_id)
    REFERENCES panel_bd.owner (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_owner_has_supermarket_supermarket1
    FOREIGN KEY (supermarket_id , supermarket_address_id)
    REFERENCES panel_bd.supermarket (id , address_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table panel_bd.supermarket_has_interactive_advertising_panel
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.supermarket_has_interactive_advertising_panel (
  supermarket_id INT NOT NULL,
  supermarket_address_id INT NOT NULL,
  interactive_advertising_panel_id INT NOT NULL,
  interactive_advertising_panel_specifications_id INT NOT NULL,
  interactive_advertising_panel_section_id INT NOT NULL,
  number_of_panels INT NOT NULL,
  PRIMARY KEY (supermarket_id, supermarket_address_id, interactive_advertising_panel_id, interactive_advertising_panel_specifications_id, interactive_advertising_panel_section_id),
  INDEX fk_supermarket_has_interactive_advertising_panel_interactiv_idx (interactive_advertising_panel_id ASC, interactive_advertising_panel_specifications_id ASC, interactive_advertising_panel_section_id ASC) VISIBLE,
  INDEX fk_supermarket_has_interactive_advertising_panel_supermarket_idx (supermarket_id ASC, supermarket_address_id ASC) VISIBLE,
  CONSTRAINT fk_supermarket_has_interactive_advertising_panel_supermarket1
    FOREIGN KEY (supermarket_id , supermarket_address_id)
    REFERENCES panel_bd.supermarket (id , address_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_supermarket_has_interactive_advertising_panel_interactive_1
    FOREIGN KEY (interactive_advertising_panel_id , interactive_advertising_panel_specifications_id , interactive_advertising_panel_section_id)
    REFERENCES panel_bd.interactive_advertising_panel (id , specifications_id , section_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table panel_bd.panel_has_manufacturer
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS panel_bd.supermarket_has_manufacturer (
  supermarket_id INT NOT NULL,
  supermarket_address_id INT NOT NULL,
  manufacturer_id INT NOT NULL,
  PRIMARY KEY (supermarket_id, supermarket_address_id, manufacturer_id),
  INDEX fk_supermarket_has_manufacturer_manufacturer1_idx (manufacturer_id ASC) VISIBLE,
  INDEX fk_supermarket_has_manufacturer_panel1_idx (supermarket_id ASC, supermarket_address_id ASC) VISIBLE,
  CONSTRAINT fk_supermarket_has_manufacturer_supermarket1
    FOREIGN KEY (supermarket_id , supermarket_address_id)
    REFERENCES panel_bd.supermarket (id , address_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_supermarket_has_manufacturer_manufacturer1
    FOREIGN KEY (manufacturer_id)
    REFERENCES panel_bd.manufacturer (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

ALTER TABLE panel_bd.section
ADD INDEX idx_name (name);

ALTER TABLE panel_bd.address
ADD INDEX idx_street_name (street_name),
ADD INDEX idx_city (city),
ADD INDEX idx_region (region);

ALTER TABLE panel_bd.supermarket
ADD INDEX idx_supermarket_name (supermarket_name),
ADD INDEX idx_trade_network (trade_network);

INSERT INTO panel_bd.specifications (model_year, screen_resolution_capacity, display_type)
VALUES
(2022, '1920x1080', 'LED'),
(2021, '3840x2160', 'OLED'),
(2023, '4096x2160', 'QLED');

INSERT INTO panel_bd.section (name)
VALUES
('Electronics'),
('Clothing'),
('Groceries'),
('Home and Garden'),
('Toys');

INSERT INTO panel_bd.interactive_advertising_panel (number, specifications_id, section_id)
VALUES
('panel001', 1, 1),
('panel002', 2, 2),
('panel003', 3, 3);

INSERT INTO panel_bd.manufacturer (name, email, phone, site)
VALUES
('Samsung', 'contact@samsung.com', '+1234567890', 'www.samsung.com'),
('LG', 'contact@lg.com', '+9876543210', 'www.lg.com'),
('Sony', 'contact@sony.com', '+1122334455', 'www.sony.com');

INSERT INTO panel_bd.address (street_name, number_of_building, city, region)
VALUES
('Horodotska', 1, 'Lviv', 'Lvivska'),
('Lesya Ukrainka', 22, 'Horodok', 'Lvivska'),
('Zelena', 7, 'Sambir', 'Lvivska');

INSERT INTO panel_bd.supermarket (supermarket_name, description_of_supermarket, area, trade_network, business_hours, average_number_of_visitors, address_id)
VALUES
('SuperMart A', 'Large panel with a wide range of products', 2500.5, 'SuperMart', '9:00-21:00', 1500, 1),
('SuperStore B', 'One-stop shop for all your needs', 1800.75, 'SuperStore', '8:00-22:00', 1200, 2),
('MegaMarket C', 'Your shopping destination', 3500.25, 'MegaMart', '10:00-23:00', 2000, 3);

INSERT INTO panel_bd.owner (email, phone, name, surname)
VALUES
('owner1@email.com', '+1112223333', 'Марія', 'Бах'),
('owner2@email.com', '+4445556666', 'Степан', 'Олеськів');

INSERT INTO panel_bd.commercials (duration, manufacturer, trademark_in_video)
VALUES
('30 с', 'Nestle', 'Cini Minis'),
('45 с', 'Jacobs', 'Jacobs Monarch'),
('1 хв', 'Sony', 'Sony Bravia');

INSERT INTO panel_bd.interactive_advertising_panel_has_commercials (interactive_advertising_panel_id, commercials_id)
VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO panel_bd.employee (name, surname, phone, position, supermarket_id, supermarket_address_id)
VALUES
('Misha', 'Swift', '+9998887777', 'Manager', 1, 1),
('Victoria', 'Bresh', '+3332221111', 'Касир', 1, 1),
('Natalia', 'Haho', '+1115559999', 'Консультант', 2, 2),
('Paulo', 'Joas', '+6665554444', 'Manager', 3, 3);

INSERT INTO panel_bd.supermarket_has_section (supermarket_id, supermarket_address_id, section_id)
VALUES
(1, 1, 1),
(1, 1, 2),
(2, 2, 3),
(3, 3, 4);

INSERT INTO panel_bd.owner_has_supermarket (owner_id, supermarket_id, supermarket_address_id)
VALUES
(1, 1, 1),
(2, 2, 2);

INSERT INTO panel_bd.supermarket_has_interactive_advertising_panel (supermarket_id, supermarket_address_id, interactive_advertising_panel_id, interactive_advertising_panel_specifications_id, interactive_advertising_panel_section_id, number_of_panels)
VALUES
(1, 1, 1, 1, 1, 5),
(2, 2, 2, 2, 2, 4),
(3, 3, 3, 3, 3, 6);

INSERT INTO panel_bd.supermarket_has_manufacturer (supermarket_id, supermarket_address_id, manufacturer_id)
VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;