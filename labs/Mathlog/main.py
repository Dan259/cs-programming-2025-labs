from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def read_set(prompt):
    while True:
        user_input = input(prompt).strip()
        elements = [x.strip() for x in user_input.replace(';', ',').split(',')]
        if len(elements) != 4:
            print("⚠️ Требуется ровно 4 элемента. Попробуйте ещё раз.")
            continue
        return set(elements)

def show_menu():
    print("\nВыберите операцию:")
    print("1. Объединение (A ∪ B ∪ C)")
    print("2. Пересечение (A ∩ B ∩ C)")
    print("3. Разность (A \\ B)")
    print("4. Симметрическая разность (A △ B)")
    print("5. Выход")

def draw_venn2_highlight(A, B, highlight_region, title):
    # Подсчёт размеров областей
    only_A = len(A - B)
    only_B = len(B - A)
    both = len(A & B)

    # Определяем цвета: выделенная область — оранжевая, остальные — серые
    colors = {
        '10': 'orange' if highlight_region == '10' else 'lightgray',
        '01': 'orange' if highlight_region == '01' else 'lightgray',
        '11': 'orange' if highlight_region == '11' else 'lightgray'
    }

    v = venn2(subsets=(only_A, only_B, both), set_labels=(f"A", f"B"))
    for region, color in colors.items():
        if region in v.patches:
            v.patches[region].set_color(color)
    plt.title(title)
    plt.show()

from matplotlib import pyplot as plt
from matplotlib.patches import Circle
from matplotlib_venn import venn2, venn3

def draw_venn2_mask(A, B, highlight_region, title):
    """
    Рисует диаграмму Венна для двух множеств и выделяет цветом одну область.
    highlight_region: '10' (только A), '01' (только B) или '11' (пересечение)
    """
    # 1. Строим стандартную диаграмму (все области серые)
    only_A = len(A - B)
    only_B = len(B - A)
    both = len(A & B)
    
    v = venn2(subsets=(only_A, only_B, both), set_labels=(f"A", f"B"))
    
    # Делаем все области серыми
    for region in v.patches:
        if region is not None:
            region.set_color('lightgray')
    
    # 2. Определяем координаты и радиус для "маски" (цветного круга)
    # Центры кругов в venn2 фиксированы: (-0.5, 0) и (0.5, 0)
    center_left = (-0.5, 0)
    center_right = (0.5, 0)
    radius = 1.0 # Стандартный радиус в venn2
    
    # 3. Рисуем цветной круг поверх нужной области
    if highlight_region == '10': # Только A
        mask = Circle(center_left, radius, color='orange', alpha=0.4, zorder=1)
    elif highlight_region == '01': # Только B
        mask = Circle(center_right, radius, color='orange', alpha=0.4, zorder=1)
    elif highlight_region == '11': # Пересечение
        # Центр пересечения находится посередине между центрами кругов
        mask = Circle((0, 0), radius, color='orange', alpha=0.4, zorder=1)
    else:
        return # Неверный код региона
    
    plt.gca().add_patch(mask)
    
    plt.title(title)
    plt.show()

def draw_venn3_mask(A, B, C, highlight_regions, title):
    """
    Рисует диаграмму Венна для трёх множеств и выделяет цветом указанные области.
    highlight_regions: список кодов ('100', '010', '111' и т.д.)
    """
    # 1. Строим стандартную диаграмму (все области серые)
    only_A = len(A - (B | C))
    only_B = len(B - (A | C))
    only_C = len(C - (A | B))
    AB_only = len((A & B) - C)
    AC_only = len((A & C) - B)
    BC_only = len((B & C) - A)
    ABC = len(A & B & C)
    
    v = venn3(subsets=(only_A, only_B, only_C, AB_only, AC_only, BC_only, ABC),
              set_labels=(f"A", f"B", "C"))
    
    for region in v.patches:
        if region is not None:
            region.set_color('lightgray')
            
    # 2. Центры кругов в venn3 фиксированы:
    centers = {
        'A': (-0.5, 0),
        'B': (0.5, 0),
        'C': (0, 0.866) # Высота равностороннего треугольника
    }
    radius = 1.0
    
    # 3. Рисуем цветные круги-маски для каждой выделенной области
    for region_code in highlight_regions:
        if region_code == '100': # Только A
            mask = Circle(centers['A'], radius, color='orange', alpha=0.4, zorder=1)
        elif region_code == '010': # Только B
            mask = Circle(centers['B'], radius, color='orange', alpha=0.4, zorder=1)
        elif region_code == '001': # Только C
            mask = Circle(centers['C'], radius, color='orange', alpha=0.4, zorder=1)
        elif region_code == '111': # Пересечение всех трёх
            mask = Circle(centers['C'], radius * 0.65, color='orange', alpha=0.6, zorder=1) # Центр и поменьше радиус
        else:
            continue # Пропускаем сложные случаи (AB_only и т.д.) для простоты или обрабатываем отдельно

        plt.gca().add_patch(mask)
    
    plt.title(title)
    plt.show()

def main():
    print("Введите по 4 элемента для каждого множества (через запятую):")
    A = read_set("Множество A: ")
    B = read_set("Множество B: ")
    C = read_set("Множество C: ")

    while True:
        show_menu()
        choice = input("Ваш выбор: ").strip()

        if choice == '1':
            result = A | B | C
            print(f"A ∪ B ∪ C = {sorted(result)}")
            # Выделяем все области, кроме пустых
            draw_venn3_mask(A, B, C, ['100', '010', '001', '110', '101', '011', '111'], "Объединение A ∪ B ∪ C")

        elif choice == '2':
            result = A & B & C
            print(f"A ∩ B ∩ C = {sorted(result)}")
            draw_venn3_mask(A, B, C, ['111'], "Пересечение A ∩ B ∩ C")

        elif choice == '3':
            print("Выберите пару для разности:")
            print("1. A \\ B")
            print("2. B \\ A")
            pair = input("Ваш выбор: ").strip()
            if pair == '1':
                result = A - B
                print(f"A \\ B = {sorted(result)}")
                draw_venn2_highlight(A, B, '10', "Разность A \\ B")
            elif pair == '2':
                result = B - A
                print(f"B \\ A = {sorted(result)}")
                draw_venn2_highlight(B, A, '01', "Разность B \\ A")
            else:
                print("❌ Неверный выбор.")

        elif choice == '4':
            print("Выберите пару для симметрической разности:")
            print("1. A △ B")
            print("2. B △ A (то же, что 1)")
            pair = input("Ваш выбор: ").strip()
            if pair in ('1', '2'):
                result = A ^ B
                print(f"A △ B = {sorted(result)}")
                draw_venn2_highlight(A, B, ['10', '01'], "Симметрическая разность A △ B")
            else:
                print("❌ Неверный выбор.")

        elif choice == '5':
            print("Завершение работы.")
            break

        else:
            print("❌ Неверный выбор. Попробуйте ещё раз.")

if __name__ == "__main__":
    main()