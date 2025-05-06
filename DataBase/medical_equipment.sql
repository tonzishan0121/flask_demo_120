/*
 Navicat Premium Data Transfer

 Source Server         : link120
 Source Server Type    : MySQL
 Source Server Version : 80036 (8.0.36)
 Source Host           : localhost:3306
 Source Schema         : rescue_120_db

 Target Server Type    : MySQL
 Target Server Version : 80036 (8.0.36)
 File Encoding         : 65001

 Date: 07/05/2025 01:10:06
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for medical_equipment
-- ----------------------------
DROP TABLE IF EXISTS `medical_equipment`;
CREATE TABLE `medical_equipment`  (
  `equipment_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `statusText` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `ambulance_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `last_update_time` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`equipment_id`) USING BTREE,
  INDEX `ambulance_id`(`ambulance_id` ASC) USING BTREE,
  CONSTRAINT `medical_equipment_ibfk_1` FOREIGN KEY (`ambulance_id`) REFERENCES `ambulances` (`ambulance_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of medical_equipment
-- ----------------------------
INSERT INTO `medical_equipment` VALUES ('EQ001', '除颤器', 'available', '设备可用', 'AMB001', '2024-01-21 08:00:00');
INSERT INTO `medical_equipment` VALUES ('EQ002', '心电监护仪', 'available', '设备可用', 'AMB001', '2024-01-21 08:05:00');
INSERT INTO `medical_equipment` VALUES ('EQ003', '呼吸机', 'unavailable', '设备正在维护', 'AMB002', '2024-01-21 08:10:00');
INSERT INTO `medical_equipment` VALUES ('EQ004', '输液泵', 'available', '设备可用', 'AMB002', '2024-01-21 08:15:00');
INSERT INTO `medical_equipment` VALUES ('EQ005', '除颤器', 'available', '设备可用', 'AMB003', '2024-01-21 08:20:00');
INSERT INTO `medical_equipment` VALUES ('EQ006', '心电监护仪', 'unavailable', '设备正在维护', 'AMB003', '2024-01-21 08:25:00');
INSERT INTO `medical_equipment` VALUES ('EQ007', '呼吸机', 'available', '设备可用', 'AMB004', '2024-01-21 08:30:00');
INSERT INTO `medical_equipment` VALUES ('EQ008', '输液泵', 'available', '设备可用', 'AMB004', '2024-01-21 08:35:00');

SET FOREIGN_KEY_CHECKS = 1;
