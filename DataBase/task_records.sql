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

 Date: 07/05/2025 01:10:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for task_records
-- ----------------------------
DROP TABLE IF EXISTS `task_records`;
CREATE TABLE `task_records`  (
  `record_id` int NOT NULL AUTO_INCREMENT,
  `task_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `ambulance_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `equipment_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `doctor_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `start_time` datetime NULL DEFAULT NULL,
  `end_time` datetime NULL DEFAULT NULL,
  `duration` int NULL DEFAULT NULL,
  `task_status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `task_statusText` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`record_id`) USING BTREE,
  INDEX `task_id`(`task_id` ASC) USING BTREE,
  INDEX `ambulance_id`(`ambulance_id` ASC) USING BTREE,
  INDEX `equipment_id`(`equipment_id` ASC) USING BTREE,
  INDEX `doctor_id`(`doctor_id` ASC) USING BTREE,
  CONSTRAINT `task_records_ibfk_1` FOREIGN KEY (`task_id`) REFERENCES `tasks` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `task_records_ibfk_2` FOREIGN KEY (`ambulance_id`) REFERENCES `ambulances` (`ambulance_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `task_records_ibfk_3` FOREIGN KEY (`equipment_id`) REFERENCES `medical_equipment` (`equipment_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `task_records_ibfk_4` FOREIGN KEY (`doctor_id`) REFERENCES `medical_staff` (`staff_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of task_records
-- ----------------------------
INSERT INTO `task_records` VALUES (1, 'T001', 'AMB001', 'EQ001', 'MS001', '2024-01-21 08:45:00', '2024-01-21 09:15:00', 30, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (2, 'T002', 'AMB002', 'EQ004', 'MS003', '2024-01-21 09:00:00', '2024-01-21 09:40:00', 40, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (3, 'T003', 'AMB003', 'EQ005', 'MS005', '2024-01-21 07:30:00', '2024-01-21 08:00:00', 30, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (4, 'T004', 'AMB004', 'EQ007', 'MS007', '2024-01-21 10:00:00', '2024-01-21 10:30:00', 30, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (5, 'T005', 'AMB005', 'EQ002', 'MS002', '2024-01-21 11:15:00', '2024-01-21 11:45:00', 30, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (6, 'T006', 'AMB006', 'EQ006', 'MS004', '2024-01-21 06:45:00', '2024-01-21 07:15:00', 30, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (7, 'T011', 'AMB001', 'EQ001', 'MS001', '2025-04-18 08:45:00', '2025-04-18 09:15:00', 30, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (8, 'T012', 'AMB002', 'EQ004', 'MS003', '2025-04-18 09:00:00', '2025-04-18 09:40:00', 40, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (9, 'T013', 'AMB003', 'EQ005', 'MS005', '2025-04-18 07:30:00', '2025-04-18 08:00:00', 30, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (10, 'T014', 'AMB004', 'EQ007', 'MS007', '2025-04-18 10:00:00', '2025-04-18 10:30:00', 30, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (11, 'T015', 'AMB005', 'EQ002', 'MS002', '2025-04-18 11:15:00', '2025-04-18 11:45:00', 30, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (12, 'T016', 'AMB006', 'EQ006', 'MS004', '2025-04-18 06:45:00', '2025-04-18 07:15:00', 30, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (13, 'T017', 'AMB001', 'EQ001', 'MS001', '2025-04-18 14:30:00', '2025-04-18 14:55:00', 25, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (14, 'T018', 'AMB002', 'EQ004', 'MS003', '2025-04-18 16:45:00', '2025-04-18 17:20:00', 35, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (15, 'T019', 'AMB003', 'EQ005', 'MS005', '2025-04-18 18:00:00', '2025-04-18 18:40:00', 40, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (16, 'T020', 'AMB004', 'EQ007', 'MS007', '2025-04-18 20:15:00', '2025-04-18 20:35:00', 20, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (17, 'T021', 'AMB005', 'EQ002', 'MS002', '2025-04-19 00:45:00', '2025-04-19 01:15:00', 30, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (18, 'T022', 'AMB006', 'EQ006', 'MS004', '2025-04-19 01:00:00', '2025-04-19 01:40:00', 40, 'completed', '任务已完成');
INSERT INTO `task_records` VALUES (19, 'T023', 'AMB001', 'EQ001', 'MS001', '2025-04-19 01:30:00', NULL, NULL, 'ongoing', '任务正在进行中');
INSERT INTO `task_records` VALUES (20, 'T024', 'AMB002', 'EQ004', 'MS003', '2025-04-19 01:45:00', NULL, NULL, 'pending', '任务待处理');

SET FOREIGN_KEY_CHECKS = 1;
