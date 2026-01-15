# 世界計畫計分計算機
## 環境
- Python 3.10+
- （可選）Ruff

## 計分規則
計分比照**排位**的計分模式，具體規則如下：

- 隊伍：不可使用強化判定隊伍，且血量以無隊伍計算（不補血）
- 計分方式
  - PERFECT 算 3 分、GREAT 算 2 分、GOOD 算 1 分、BAD／MISS 算 0 分
  - 若雙方同分，則依序比較
    1. PERFECT 數
    2. 最大 COMBO 數
    3. 剩餘血量（初始 1000 血，BAD 扣 50 血、MISS 扣 80 血）

## 參考資料
- [世界計畫官網計分規則（jp）](https://pjsekai.sega.jp/news/article/index.html?hash=a4be0d5d5effe4a9737f9767f973628c0d98e5f3)
- [世界計畫 Bilibili 官方帳號計分規則（zh-cn）](https://www.bilibili.com/opus/641606270870093929)