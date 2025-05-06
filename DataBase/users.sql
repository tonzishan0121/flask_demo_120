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

 Date: 07/05/2025 01:10:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nickname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `password_hash` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `role` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `created_at` datetime NULL DEFAULT NULL,
  `last_login` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`email`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('admin@admin.com', 'admin', 'scrypt:32768:8:1$9jPTcWiERPRU4eVL$f295a0791841bfd16d397ccb82bdd5b4d67e1d5eccbb0679d82c65c0e998079e173f6697ff5e3d483f14ab73518f13b5cd24ac268d5d3e9519ca5481752f8460', 'admin', '2025-04-01 23:14:00', '2025-05-04 19:05:53');
INSERT INTO `users` VALUES ('doctor@example.com', 'Dr. Smith', 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 'doctor', '2024-01-20 10:00:00', '2024-01-21 08:30:00');
INSERT INTO `users` VALUES ('doctor2@example.com', 'Dr. Johnson', '7b392998628275539cf7c5bcf9884e769e0bc72a22bb48083ff0d4908cb0d2d9', 'doctor', '2024-01-20 10:45:00', '2024-01-21 09:00:00');
INSERT INTO `users` VALUES ('user1@example.com', 'UserOne', '89e01536ac207279409d4de1e5253e01f4a1769e696db0d6062ca9b8f56767c8', 'user', '2024-01-20 10:15:00', '2024-01-21 08:45:00');
INSERT INTO `users` VALUES ('user2@example.com', 'UserTwo', 'fbb4a8a163ffa958b4f02bf9cabb30cfefb40de803f2c4c346a9d39b3be1b544', 'user', '2024-01-20 10:30:00', '2024-01-21 08:50:00');
INSERT INTO `users` VALUES ('user3@example.com', 'UserThree', '0a0a3549131c438fe4751181e099a4c1f98e2b64e66278dd500c7758344b9d47', 'user', '2024-01-20 11:00:00', '2024-01-21 09:15:00');

SET FOREIGN_KEY_CHECKS = 1;
