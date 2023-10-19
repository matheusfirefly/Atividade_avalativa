-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 19-Out-2023 às 23:04
-- Versão do servidor: 5.7.11
-- PHP Version: 5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bd_dados`
--
CREATE DATABASE IF NOT EXISTS `bd_dados` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `bd_dados`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tb_xetario`
--

CREATE TABLE `tb_xetario` (
  `cod_ser` int(11) NOT NULL,
  `des_tar` varchar(255) NOT NULL,
  `pes_res` varchar(255) NOT NULL,
  `data_ini` date NOT NULL,
  `data_ter` date NOT NULL,
  `quanti_pro` int(11) NOT NULL,
  `tip` varchar(25) NOT NULL,
  `obs` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `tb_xetario`
--

INSERT INTO `tb_xetario` (`cod_ser`, `des_tar`, `pes_res`, `data_ini`, `data_ter`, `quanti_pro`, `tip`, `obs`) VALUES
(1, 'Reparo de maquina', 'Jorge', '2018-12-03', '2019-02-01', 120, 'Baixa', 'Reparo demorou mais que o esperado'),
(3, 'Reparo de maquina', 'Luiz e Jorge', '2018-12-03', '2019-02-01', 120, 'Baixa', 'Reparo demorou mais que o esperado'),
(4, 'Reparo de maquina', 'Jorge', '2018-12-03', '2019-02-01', 120, 'Baixa', 'Reparo demorou mais que o esperado');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_xetario`
--
ALTER TABLE `tb_xetario`
  ADD PRIMARY KEY (`cod_ser`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_xetario`
--
ALTER TABLE `tb_xetario`
  MODIFY `cod_ser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
