# 分數
PERFECT_PTS = 3
GREAT_PTS = 2
GOOD_PTS = 1

# 扣血
BAD_DMG = 50
MISS_DMG = 80

def nonnegative_input(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            s = int(s)
            if s < 0:
                print('請輸入非負整數！')
                continue
            return s
        except ValueError:
            print('請輸入非負整數！')

def count_score(name: str) -> tuple[int]:
    PERFECT_PTS = nonnegative_input(f'請輸入 {name} 的 PERFECT_PTS 數：')
    GREAT_PTS = nonnegative_input(f'請輸入 {name} 的 GREAT_PTS數：')
    GOOD_PTS = nonnegative_input(f'請輸入 {name} 的 GOOD_PTS 數：')
    BAD_DMG = nonnegative_input(f'請輸入 {name} 的 BAD_DMG 數：')
    MISS_DMG = nonnegative_input(f'請輸入 {name} 的 MISS_DMG 數：')

    score = PERFECT_PTS*PERFECT_PTS + GREAT_PTS*GREAT_PTS + GOOD_PTS*GOOD_PTS
    hp = max(0, 1000 - BAD_DMG*BAD_DMG - MISS_DMG*MISS_DMG)
    combo = int(input(f'請輸入 {name} 的最大 COMBO 數：'))

    return (score, PERFECT_PTS, hp, combo)

def single() -> None:
    PERFECT_PTS = int(input('請輸入您的 PERFECT_PTS 數：'))
    GREAT_PTS = int(input('請輸入您的 GREAT_PTS 數：'))
    GOOD_PTS = int(input('請輸入您的 GOOD_PTS 數：'))
    print (f'好的，系統已計算完成\n您的總分為 {PERFECT_PTS*PERFECT_PTS + GREAT_PTS*GREAT_PTS + GOOD_PTS*GOOD_PTS} 分')

def double() -> None:
    name_a = input('請輸入一號玩家的暱稱:')
    name_b = input('請輸入二號玩家的暱稱:')

    score_a, PERFECT_PTS_a, hp_a, combo_a = count_score(name_a)
    score_b, PERFECT_PTS_b, hp_b, combo_b = count_score(name_b)

    print(f'好的，系統已計算完成\n{name_a} 的分數為：{score_a} 分\n{name_b} 的分數為：{score_b} 分')
    if score_a != score_b:
        print(f'{name_a if score_a > score_b else name_b} 獲勝！')
    else:
        print(f'由於雙方分數一樣，進入同分比較第一階段\n{name_a}的 PERFECT_PTS 數為：{PERFECT_PTS_a}\n{name_b}的 PERFECT_PTS 數為：{PERFECT_PTS_b}')
        if PERFECT_PTS_a != PERFECT_PTS_b:
            print(f'{name_a if PERFECT_PTS_a > PERFECT_PTS_b else name_b} 獲勝！')
        else:
            print(f'由於雙方 PERFECT_PTS 數也一樣，進入同分比較第二階段\n{name_a} 的最大 COMBO 數為 {combo_a}\n{name_b} 的最大 COMBO 數為 {combo_b}')
            if combo_a != combo_b:
                print(f'{name_a if combo_a > combo_b else name_b} 獲勝！')
            else:
                print(f'由於雙方的最大 COMBO 數仍一樣，進入同分比較最後階段\n無陣容的狀態之下\n{name_a} 將會剩下 {hp_a} 點血\n{name_b} 將會剩下 {hp_b} 點血')
                if hp_a != hp_b:
                    print(f'{name_a if hp_a > hp_b else name_b} 獲勝！')
                else:
                    print('雙方平手！')

def main() -> None:
    while True:
        match input('\n請選擇要執行的項目 (A)單人算分 (B)雙人 PK\n或輸入任意其他字來結束程式\n：').upper():
            case 'A':
                single()
            case 'B':
                double()
            case _:
                print('感謝您本次的使用，再見~')
                return

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'發生錯誤：{e}')