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

 Date: 07/05/2025 01:10:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tasks
-- ----------------------------
DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks`  (
  `id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `statusText` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `location` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `time` datetime NULL DEFAULT NULL,
  `response_time` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tasks
-- ----------------------------
INSERT INTO `tasks` VALUES ('T001', 'pending', '待处理', '上海市浦东新区陆家嘴', '交通事故，有人员受伤', '2024-01-21 08:45:00', NULL);
INSERT INTO `tasks` VALUES ('T002', 'processing', '进行中', '上海市徐汇区漕河泾', '老人突发脑溢血，需要紧急救护', '2024-01-21 09:00:00', NULL);
INSERT INTO `tasks` VALUES ('T003', 'completed', '已完成', '上海市静安区南京西路', '儿童误食异物，已成功救治', '2024-01-21 07:30:00', 15);
INSERT INTO `tasks` VALUES ('T004', 'pending', '待处理', '上海市杨浦区五角场', '工厂火灾，有人员被困', '2024-01-21 10:00:00', NULL);
INSERT INTO `tasks` VALUES ('T005', 'processing', '进行中', '上海市闵行区莘庄', '孕妇临产，需要紧急送医', '2024-01-21 11:15:00', NULL);
INSERT INTO `tasks` VALUES ('T006', 'completed', '已完成', '上海市虹口区鲁迅公园', '老人摔倒，已送往医院', '2024-01-21 06:45:00', 20);
INSERT INTO `tasks` VALUES ('T011', 'completed', '已完成', '上海市浦东新区陆家嘴', '交通事故，有人员受伤', '2025-04-18 08:45:00', 30);
INSERT INTO `tasks` VALUES ('T012', 'completed', '已完成', '上海市徐汇区漕河泾', '老人突发脑溢血，需要紧急救护', '2025-04-18 09:00:00', 40);
INSERT INTO `tasks` VALUES ('T013', 'completed', '已完成', '上海市静安区南京西路', '儿童误食异物，已成功救治', '2025-04-18 07:30:00', 30);
INSERT INTO `tasks` VALUES ('T014', 'completed', '已完成', '上海市杨浦区五角场', '工厂火灾，有人员被困', '2025-04-18 10:00:00', 30);
INSERT INTO `tasks` VALUES ('T015', 'completed', '已完成', '上海市闵行区莘庄', '孕妇临产，需要紧急送医', '2025-04-18 11:15:00', 30);
INSERT INTO `tasks` VALUES ('T016', 'completed', '已完成', '上海市虹口区鲁迅公园', '老人摔倒，已送往医院', '2025-04-18 06:45:00', 20);
INSERT INTO `tasks` VALUES ('T017', 'completed', '已完成', '上海市浦东新区张江', '心脏骤停，紧急救援', '2025-04-18 14:30:00', 25);
INSERT INTO `tasks` VALUES ('T018', 'completed', '已完成', '上海市黄浦区南京东路', '突发腹痛，怀疑阑尾炎', '2025-04-18 16:45:00', 35);
INSERT INTO `tasks` VALUES ('T019', 'completed', '已完成', '上海市宝山区吴淞', '工伤事故，手部受伤', '2025-04-18 18:00:00', 40);
INSERT INTO `tasks` VALUES ('T020', 'completed', '已完成', '上海市普陀区长寿路', '交通事故，轻微擦伤', '2025-04-18 20:15:00', 20);
INSERT INTO `tasks` VALUES ('T021', 'completed', '已完成', '上海市浦东新区陆家嘴', '交通事故，有人员受伤', '2025-04-19 00:45:00', 30);
INSERT INTO `tasks` VALUES ('T022', 'completed', '已完成', '上海市徐汇区漕河泾', '老人突发脑溢血，需要紧急救护', '2025-04-19 01:00:00', 40);
INSERT INTO `tasks` VALUES ('T023', 'processing', '进行中', '上海市静安区南京西路', '儿童误食异物，紧急救治中', '2025-04-19 01:30:00', NULL);
INSERT INTO `tasks` VALUES ('T024', 'pending', '待处理', '上海市杨浦区五角场', '工厂火灾，有人员被困', '2025-04-19 01:45:00', NULL);

SET FOREIGN_KEY_CHECKS = 1;
