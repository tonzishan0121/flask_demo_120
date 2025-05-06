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

 Date: 07/05/2025 01:09:58
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ambulances
-- ----------------------------
DROP TABLE IF EXISTS `ambulances`;
CREATE TABLE `ambulances`  (
  `ambulance_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `license_plate` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `statusText` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `driver_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `driver_phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `last_update_time` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`ambulance_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of ambulances
-- ----------------------------
INSERT INTO `ambulances` VALUES ('AMB001', '沪A12345', 'online', '救护车在线，随时待命', '张三', '13800138000', '2024-01-21 08:00:00');
INSERT INTO `ambulances` VALUES ('AMB002', '沪B67890', 'processing', '救护车正在执行任务', '李四', '13900139000', '2024-01-21 08:15:00');
INSERT INTO `ambulances` VALUES ('AMB003', '沪C54321', 'offline', '救护车离线，维护中', '王五', '13700137000', '2024-01-21 07:30:00');
INSERT INTO `ambulances` VALUES ('AMB004', '沪D98765', 'online', '救护车在线，随时待命', '赵六', '13600136000', '2024-01-21 08:20:00');
INSERT INTO `ambulances` VALUES ('AMB005', '沪E13579', 'processing', '救护车正在执行任务', '孙七', '13500135000', '2024-01-21 08:30:00');
INSERT INTO `ambulances` VALUES ('AMB006', '沪F24680', 'offline', '救护车离线，休息中', '周八', '13400134000', '2024-01-21 07:45:00');

SET FOREIGN_KEY_CHECKS = 1;
