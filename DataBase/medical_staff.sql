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

 Date: 07/05/2025 01:10:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for medical_staff
-- ----------------------------
DROP TABLE IF EXISTS `medical_staff`;
CREATE TABLE `medical_staff`  (
  `staff_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `role` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `statusText` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `ambulance_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `last_update_time` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`staff_id`) USING BTREE,
  INDEX `ambulance_id`(`ambulance_id` ASC) USING BTREE,
  CONSTRAINT `medical_staff_ibfk_1` FOREIGN KEY (`ambulance_id`) REFERENCES `ambulances` (`ambulance_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of medical_staff
-- ----------------------------
INSERT INTO `medical_staff` VALUES ('MS001', '张医生', '医生', 'on_duty', '当班中', '13800138001', 'AMB001', '2024-01-21 08:00:00');
INSERT INTO `medical_staff` VALUES ('MS002', '李护士', '护士', 'standby', '待命中', '13900139001', 'AMB001', '2024-01-21 08:05:00');
INSERT INTO `medical_staff` VALUES ('MS003', '王医生', '医生', 'on_duty', '当班中', '13700137001', 'AMB002', '2024-01-21 08:10:00');
INSERT INTO `medical_staff` VALUES ('MS004', '赵护士', '护士', 'standby', '待命中', '13600136001', 'AMB002', '2024-01-21 08:15:00');
INSERT INTO `medical_staff` VALUES ('MS005', '孙医生', '医生', 'off_duty', '未值班', '13500135001', NULL, '2024-01-21 07:30:00');
INSERT INTO `medical_staff` VALUES ('MS006', '周护士', '护士', 'off_duty', '未值班', '13400134001', NULL, '2024-01-21 07:45:00');
INSERT INTO `medical_staff` VALUES ('MS007', '吴医生', '医生', 'on_duty', '当班中', '13300133001', 'AMB004', '2024-01-21 08:20:00');
INSERT INTO `medical_staff` VALUES ('MS008', '郑护士', '护士', 'standby', '待命中', '13200132001', 'AMB004', '2024-01-21 08:25:00');

SET FOREIGN_KEY_CHECKS = 1;
