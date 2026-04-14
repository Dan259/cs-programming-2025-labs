import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Функции для отрисовки ---

def draw_venn2(A, B, highlight_region, title):
    """
    Корректно рисует диаграмму Венна для двух множеств.
    highlight_region: '10' (только A), '01' (только B) или '11' (пересечение).
    """
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_aspect('equal')
    ax.axis('off')

    # Центры кругов и радиус
    center_left = (-0.5, 0)
    center_right = (0.5, 0)
    radius = 1.0

    # Вычисляем размеры областей
    only_A = len(A - B)
    only_B = len(B - A)
    both = len(A & B)

    regions = {
        '10': only_A,
        '01': only_B,
        '11': both
    }

    # 1. Рисуем серые круги (фон)
    circle_left = patches.Circle(center_left, radius,
                                facecolor='lightgray', edgecolor='black', linewidth=1, zorder=0)
    circle_right = patches.Circle(center_right, radius,
                                 facecolor='lightgray', edgecolor='black', linewidth=1, zorder=0)
    
    ax.add_patch(circle_left)
    ax.add_patch(circle_right)

    # 2. Рисуем цветную маску поверх нужной области
    if highlight_region == '10' and regions['10'] > 0:
        # Только A: левый круг
        mask = patches.Circle(center_left, radius,
                             facecolor='orange', edgecolor='black', linewidth=1, zorder=1, alpha=0.7)
        ax.add_patch(mask)
        
    elif highlight_region == '01' and regions['01'] > 0:
        # Только B: правый круг
        mask = patches.Circle(center_right, radius,
                             facecolor='orange', edgecolor='black', linewidth=1, zorder=1, alpha=0.7)
        ax.add_patch(mask)
        
    elif highlight_region == '11' and regions['11'] > 0:
        # Пересечение: рисуем клинья (секторы) в обоих кругах
        # Углы пересечения для двух кругов на одной горизонтали
        start_angle = 270  # -90 градусов (вниз)
        end_angle = 90     # +90 градусов (вверх)
        
        wedge_left = patches.Wedge(center_left, radius, start_angle, end_angle,
                                  facecolor='orange', edgecolor='black', linewidth=1, zorder=2, alpha=0.7)
        wedge_right = patches.Wedge(center_right, radius, start_angle, end_angle,
                                   facecolor='orange', edgecolor='black', linewidth=1, zorder=2, alpha=0.7)
        
        ax.add_patch(wedge_left)
        ax.add_patch(wedge_right)

    # 3. Подписываем количество элементов
    def add_text(x, y, text):
        ax.text(x, y, text, ha='center', va='center', fontsize=9)

    add_text(center_left[0] - 0.7, center_left[1], f"Only A\n{regions['10']}")
    add_text(center_right[0] + 0.7, center_right[1], f"Only B\n{regions['01']}")
    
    # Центр пересечения
    cx = (center_left[0] + center_right[0]) / 2
    cy = center_left[1]
    add_text(cx, cy + 0.25, f"Both\n{regions['11']}")

    plt.title(title)
    plt.tight_layout()
    plt.show()


def draw_venn3(A, B, C, highlight_regions, title):
    """
    Корректно рисует диаграмму Венна для трёх множеств.
    highlight_regions: список кодов ('100', '010', '111' и т.д.).
    """
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    # Центры кругов (равносторонний треугольник)
    centers = {
        'A': (-0.5, 0),
        'B': (0.5, 0),
        'C': (0, 0.866) 
    }
    radius = 1.0

    # Вычисляем размеры областей
    only_A = len(A - (B | C))
    only_B = len(B - (A | C))
    only_C = len(C - (A | B))
    AB_only = len((A & B) - C)
    AC_only = len((A & C) - B)
    BC_only = len((B & C) - A)
    ABC = len(A & B & C)

    regions = {
        '100': only_A,
        '010': only_B,
        '001': only_C,
        '110': AB_only,
        '101': AC_only,
        '011': BC_only,
        '111': ABC
    }

     # 1. Рисуем серые круги (фон)
    for name in ['A', 'B', 'C']:
        circle = patches.Circle(centers[name], radius,
                               facecolor='lightgray', edgecolor='black', linewidth=1, zorder=0)
        ax.add_patch(circle)

     # 2. Рисуем цветные маски для пересечений (если они выделены)
     # Используем Wedge для пересечений и Circle для центра.
     
     # Пересечение A и B (без C)
    if '110' in highlight_regions and regions['110'] > 0:
        wedge = patches.Wedge(centers['A'], radius, 270, 90,
                            facecolor='orange', edgecolor='black', linewidth=1,
                            zorder=5, alpha=0.8)
        ax.add_patch(wedge)
        wedge = patches.Wedge(centers['B'], radius, 270, 90,
                            facecolor='orange', edgecolor='black', linewidth=1,
                            zorder=5, alpha=0.8)
        ax.add_patch(wedge)
        
    # Пересечение A и C (без B)
    if '101' in highlight_regions and regions['101'] > 0:
        wedge = patches.Wedge(centers['A'], radius, 330, 210,
                            facecolor='orange', edgecolor='black', linewidth=1,
                            zorder=5, alpha=0.8)
        ax.add_patch(wedge)
        wedge = patches.Wedge(centers['C'], radius, 330, 210,
                            facecolor='orange', edgecolor='black', linewidth=1,
                            zorder=5, alpha=0.8)
        ax.add_patch(wedge)
         
     # Пересечение B и C (без A)
    if '011' in highlight_regions and regions['011'] > 0:
        wedge = patches.Wedge(centers['B'], radius, 330, 210,
                            facecolor='orange', edgecolor='black', linewidth=1,
                            zorder=5, alpha=0.8)
        ax.add_patch(wedge)
        wedge = patches.Wedge(centers['C'], radius, 330, 210,
                            facecolor='orange', edgecolor='black', linewidth=1,
                            zorder=5, alpha=0.8)
        ax.add_patch(wedge)
         
     # Центр (пересечение всех трёх)
    if '111' in highlight_regions and regions['111'] > 0:
        cx = sum([centers['A'][0], centers['B'][0], centers['C'][0]]) / 3
        cy = sum([centers['A'][1], centers['B'][1], centers['C'][1]]) / 3
        mask_radius = radius * 0.45 
        circle = patches.Circle((cx, cy), mask_radius,
                            facecolor='orange', edgecolor='black', linewidth=1,
                            zorder=6)
        ax.add_patch(circle)
         
     # Только A / Только B / Только C
    if '100' in highlight_regions and regions['100'] > 0:
        mask = patches.Circle(centers['A'], radius,
                            facecolor='orange', edgecolor=None, zorder=4, alpha=0.4)
        ax.add_patch(mask)
    if '010' in highlight_regions and regions['010'] > 0:
        mask = patches.Circle(centers['B'], radius,
                            facecolor='orange', edgecolor=None, zorder=4, alpha=0.4)
        ax.add_patch(mask)
    if '001' in highlight_regions and regions['001'] > 0:
        mask = patches.Circle(centers['C'], radius,
                            facecolor='orange', edgecolor=None, zorder=4, alpha=0.4)
        ax.add_patch(mask)


     # 3. Подписываем количество элементов в каждой области
    def add_text(x, y, text):
        ax.text(x, y, text, ha='center', va='center', fontsize=9)
     
    add_text(centers['A'][0] - radius*0.75, centers['A'][1], f"Only A\n{regions['100']}")
    add_text(centers['B'][0] + radius*0.75, centers['B'][1], f"Only B\n{regions['010']}")
    add_text(centers['C'][0], centers['C'][1] + radius*0.45, f"Only C\n{regions['001']}")
    
    add_text( (centers['A'][0]+centers['B'][0])/2 , centers['A'][1] - radius*0.35 , f"A&B\n{regions['110']}")
    add_text( centers['C'][0] , centers['C'][1] - radius*  f"A&C\n{regions['101']}")
    add_text( centers['C'][0] + radius*  centers['C'][1] - radius*  f"B&C\n{regions['011']}")
    
    add_text( centers['C'][0], centers['C'][1] - radius*  f"A&B&C\n{regions['111']}")

    plt.title(title)
    plt.tight_layout()
    plt.show()


# --- Функции для ввода данных и интерфейса ---

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
    print("   Для ДВУХ множеств:")
    print("3. Разность (A \\ B)")
    print("4. Симметрическая разность (A △ B)")
    
    print("\n   Для ТРЁХ множеств:")
    print("   Операции над A ∪ B ∪ C:")
    print("   Операции над A ∩ B ∩ C:")
    
def main():
    print("Введите по 4 элемента для каждого множества (через запятую):")
    
    A = read_set("Множество A: ")
    
    print("\n--- Операции с двумя множествами ---")
    
    B_two = read_set("Множество B: ")
    
    while True:
        show_menu()
        
        choice_2set = input("\nВаш выбор операции с двумя множествами (3/4) или Enter для перехода к трём: ").strip()
        
        if choice_2set == '3':
            print("\nВыберите пару для разности:")
            print("3a. A \\ B")
            print("3b. B \\ A")
            pair_3 = input("Ваш выбор: ").strip()
            
            if pair_3 == 'a':
                result = A - B_two
                print(f"A \\ B = {sorted(result)}")
                draw_venn2(A, B_two, '10', "Разность A \\ B")
            elif pair_3 == 'b':
                result = B_two - A
                print(f"B \\ A = {sorted(result)}")
                draw_venn2(B_two, A, '10', "Разность B \\ A")
            else:
                print("❌ Неверный выбор.")
                
        elif choice_2set == '4':
            result = A ^ B_two
            print(f"A △ B = {sorted(result)}")
            draw_venn2(A, B_two, ['10','01'], "Симметрическая разность A △ B")
            
        elif choice_2set == '':
            break
        else:
            print("❌ Неверный выбор.")
            print("\n--- Операции с тремя множествами ---")
            C_three = read_set("Множество C: ")
             
            while True:
                show_menu()
                choice_3set = input("\nВаш выбор операции с тремя множествами (Enter для выхода): ").strip()
                
                if choice_3set == '':
                    print("Завершение работы.")
                    return
                    
                elif choice_3set == 'union':
                    result = A | B_two | C_three
                    print(f"A ∪ B ∪ C = {sorted(result)}")
                    draw_venn3(A,B_two,C_three,{'A_only','B_only','C_only','AB_only','AC_only','BC_only','ABC'}, "Объединение")
                    
                elif choice_3set == 'intersection':
                    result = A & B_two & C_three
                    print(f"A ∩ B ∩ C = {sorted(result)}")
                    draw_venn3(A,B_two,C_three,{'ABC'}, "Пересечение")
                    
                else:
                    print("❌ Неверный выбор.")


if __name__ == "__main__":
   main()