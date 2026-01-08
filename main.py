PERFECT = 3
GREAT = 2
GOOD = 1
BAD = 50
MISS = 80

def count_score(name: str) -> tuple[int]:
    perfect = int(input(f'請輸入 {name} 的 PERFECT 數：'))
    great = int(input(f'請輸入 {name} 的 GREAT數：'))
    good = int(input(f'請輸入 {name} 的 GOOD 數：'))
    bad = int(input(f'請輸入 {name} 的 BAD 數：'))
    miss = int(input(f'請輸入 {name} 的 MISS 數：'))

    score = perfect*PERFECT + great*GREAT + good*GOOD
    hp = max(0, 1000 - bad*BAD - miss*MISS)
    combo = int(input(f'請輸入 {name} 的最大 COMBO 數：'))

    return (score, perfect, hp, combo)

def single() -> None:
    perfect = int(input('請輸入您的 PERFECT 數：'))
    great = int(input('請輸入您的 GREAT 數：'))
    good = int(input('請輸入您的 GOOD 數：'))
    print (f'好的，系統已計算完成\n您的總分為 {perfect*PERFECT + great*GREAT + good*GOOD} 分')

def double() -> None:
    name_a = input('請輸入一號玩家的暱稱:')
    name_b = input('請輸入二號玩家的暱稱:')

    score_a, perfect_a, hp_a, combo_a = count_score(name_a)
    score_b, perfect_b, hp_b, combo_b = count_score(name_b)

    print(f'好的，系統已計算完成\n{name_a} 的分數為：{score_a} 分\n{name_b} 的分數為：{score_b} 分')
    if score_a != score_b:
        print(f'{name_a if score_a > score_b else name_b} 獲勝！')
    else:
        print(f'由於雙方分數一樣，進入同分比較第一階段\n{name_a}的 PERFECT 數為：{perfect_a}\n{name_b}的 PERFECT 數為：{perfect_b}')
        if perfect_a != perfect_b:
            print(f'{name_a if perfect_a > perfect_b else name_b} 獲勝！')
        else:
            print(f'由於雙方 PERFECT 數也一樣，進入同分比較第二階段\n{name_a} 的最大 COMBO 數為 {combo_a}\n{name_b} 的最大 COMBO 數為 {combo_b}')
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