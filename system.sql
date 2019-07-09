/*
Navicat MySQL Data Transfer

Source Server         : local-mysql
Source Server Version : 50723
Source Host           : localhost:3306
Source Database       : python_test

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2019-07-09 18:26:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for system_user
-- ----------------------------
DROP TABLE IF EXISTS `system_user`;
CREATE TABLE `system_user` (
  `id` varchar(64) COLLATE utf8_bin NOT NULL,
  `name` varchar(80) COLLATE utf8_bin DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `email` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of system_user
-- ----------------------------
INSERT INTO `system_user` VALUES ('', '3', '3', '3');
INSERT INTO `system_user` VALUES ('6298495c-a233-11e9-b300-005056c00008', '9', '9', '9');
INSERT INTO `system_user` VALUES ('72d015e4-a232-11e9-8370-005056c00008', '6', '6', '6');
INSERT INTO `system_user` VALUES ('a0e19a86-a232-11e9-ac8c-005056c00008', '7', '7', '7');
INSERT INTO `system_user` VALUES ('aadfbd54-a232-11e9-85de-005056c00008', '8', '8', '8');
INSERT INTO `system_user` VALUES ('ca53765c-a233-11e9-85f3-005056c00008', '11', '11', '11');
