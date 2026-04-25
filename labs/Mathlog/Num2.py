import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import numpy as np

# Настройка русского шрифта
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def visualize_swapped_positions():
    """
    Визуализация исходного выражения: ((A ∩ C) \ E) ∪ E \ ((E ∩ A) ∪ (E ∩ C))
    На графике круги E и C поменяны местами (визуально)
    """
    
    # Создаем тестовые множества (исходное выражение не меняется)
    A = {'a1', 'a2', 'ac1', 'ae1', 'ace1'}
    C = {'c1', 'c2', 'ac1', 'ce1', 'ace1'}  # Множество C
    E = {'e1', 'e2', 'ae1', 'ce1', 'ace1'}  # Множество E
    
    # Вычисляем результат ИСХОДНОГО выражения: ((A ∩ C) \ E) ∪ E \ ((E ∩ A) ∪ (E ∩ C))
    part1 = A.intersection(C).difference(E)  # (A∩C)\E
    part2 = E.difference(E.intersection(A).union(E.intersection(C)))  # E \ ((E∩A)∪(E∩C))
    result = part1.union(part2)
    
    # Создаем фигуру
    fig = plt.figure(figsize=(14, 8))
    
    # Основная визуализация - меняем порядок множеств для визуальной перестановки
    # Вместо (A, C, E) передаем (A, E, C) - это поменяет позиции E и C на графике
    ax1 = fig.add_subplot(1, 2, 1)
    v = venn3([A, E, C], set_labels=('A', 'E', 'C'), ax=ax1)
    
    # Убираем цифры из кругов
    for text in v.subset_labels:
        if text is not None:
            text.set_text('')
    
    # Выделяем ТОЛЬКО результирующие области для ИСХОДНОГО выражения
    # ВНИМАНИЕ: при передаче [A, E, C] области имеют другие id:
    # '110' - теперь это A∩E без C (но нам нужно A∩C без E)
    # '001' - это только C (но нам нужно только E)
    # Поэтому нужно правильно определить области после перестановки
    
    # При порядке [A, E, C]:
    # id '101' соответствует A∩C без E (то что нам нужно для (A∩C)\E)
    # id '010' соответствует только E (то что нам нужно для E \ ((E∩A)∪(E∩C)))
    
    # Область 1: (A∩C)\E - теперь это область '101'
    if v.get_patch_by_id('101'):
        v.get_patch_by_id('101').set_color('#FF4444')
        v.get_patch_by_id('101').set_alpha(0.85)
        v.get_patch_by_id('101').set_edgecolor('darkred')
        v.get_patch_by_id('101').set_linewidth(2.5)
    
    # Область 2: только E - теперь это область '010'
    if v.get_patch_by_id('010'):
        v.get_patch_by_id('010').set_color('#44FF44')
        v.get_patch_by_id('010').set_alpha(0.85)
        v.get_patch_by_id('010').set_edgecolor('darkgreen')
        v.get_patch_by_id('010').set_linewidth(2.5)
    
    # Делаем остальные области прозрачными
    all_patches = ['100', '001', '110', '011', '111']
    for patch_id in all_patches:
        if v.get_patch_by_id(patch_id):
            v.get_patch_by_id(patch_id).set_color('#E0E0E0')
            v.get_patch_by_id(patch_id).set_alpha(0.15)
            v.get_patch_by_id(patch_id).set_edgecolor('#CCCCCC')
            v.get_patch_by_id(patch_id).set_linewidth(0.5)
    
    # Настраиваем подписи множеств
    for label in v.set_labels:
        if label is not None:
            label.set_fontsize(14)
            label.set_fontweight('bold')
    
    ax1.set_title(f'Исходное выражение\n((A∩C)\\E) ∪ E\\((E∩A)∪(E∩C))\nКруги E и C поменяны местами', 
                  fontsize=11, fontweight='bold', pad=20)
    
    # Добавляем легенду
    legend_elements = [
        plt.Rectangle((0,0), 1, 1, facecolor='#FF4444', alpha=0.85, 
                     edgecolor='darkred', linewidth=2, label='(A∩C)\\E'),
        plt.Rectangle((0,0), 1, 1, facecolor='#44FF44', alpha=0.85,
                     edgecolor='darkgreen', linewidth=2, label='Только E (без A и C)'),
        plt.Rectangle((0,0), 1, 1, facecolor='#E0E0E0', alpha=0.15,
                     edgecolor='#CCCCCC', linewidth=0.5, label='Остальные области')
    ]
    ax1.legend(handles=legend_elements, loc='lower left', fontsize=10, 
               framealpha=0.9, bbox_to_anchor=(0, -0.15))
    
    # Правая часть - объяснение
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.axis('off')
    
    explanation = f"""
    ИСХОДНОЕ ВЫРАЖЕНИЕ (НЕ ИЗМЕНЯЕТСЯ):
    ((A ∩ C) \\ E) ∪ E \\ ((E ∩ A) ∪ (E ∩ C))
    
    НА ГРАФИКЕ:
    • Круги E и C поменяны местами
    • Выражение осталось прежним
    
    РЕЗУЛЬТАТ ВКЛЮЧАЕТ:
    
    ▸ Область 1 (КРАСНЫЙ)
      (A ∩ C) \\ E
      • Элементы в пересечении A и C,
        но НЕ в E
    
    ▸ Область 2 (ЗЕЛЕНЫЙ)
      Только E (без A и C)
      • Элементы, принадлежащие
        только множеству E
    
    РЕЗУЛЬТАТ = {result}
    """
    
    ax2.text(0.1, 0.5, explanation, fontsize=11, verticalalignment='center',
             fontfamily='monospace', 
             bbox=dict(boxstyle='round', facecolor='#F0F0F0', alpha=0.9, 
                      edgecolor='#999999', linewidth=1.5))
    
    plt.suptitle('Визуализация исходного выражения с переставленными кругами E и C', 
                 fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.show()
    
    # Вывод результата
    print("\n" + "=" * 60)
    print("ИСХОДНОЕ ВЫРАЖЕНИЕ (НЕ ИЗМЕНЯЕТСЯ):")
    print("=" * 60)
    print(f"\nВыражение: ((A ∩ C) \\ E) ∪ E \\ ((E ∩ A) ∪ (E ∩ C))")
    print(f"\nМножество A = {A}")
    print(f"Множество C = {C}")
    print(f"Множество E = {E}")
    print(f"\n(A ∩ C) \\ E = {part1}")
    print(f"E \\ ((E∩A) ∪ (E∩C)) = {part2}")
    print(f"\nИТОГОВЫЙ РЕЗУЛЬТАТ: {result}")
    print("=" * 60)

def simple_swapped_positions():
    """Простая визуализация с переставленными кругами"""
    
    # Тестовые множества
    A = {'a', 'ac', 'ae', 'ace'}
    C = {'c', 'ac', 'ce', 'ace'}
    E = {'e', 'ae', 'ce', 'ace'}
    
    # Вычисляем исходное выражение
    part1 = A.intersection(C).difference(E)
    part2 = E.difference(E.intersection(A).union(E.intersection(C)))
    result = part1.union(part2)
    
    # Создаем визуализацию с переставленными кругами
    plt.figure(figsize=(10, 8))
    v = venn3([A, E, C], set_labels=('A', 'E', 'C'))  # E и C поменяны местами
    
    # Убираем цифры
    for text in v.subset_labels:
        if text is not None:
            text.set_text('')
    
    # Очищаем все области
    for patch in v.patches:
        patch.set_color('#F0F0F0')
        patch.set_alpha(0.1)
        patch.set_edgecolor('#CCCCCC')
        patch.set_linewidth(0.5)
    
    # Выделяем нужные области (с учетом перестановки)
    # (A∩C)\E - теперь это '101'
    if v.get_patch_by_id('101'):
        v.get_patch_by_id('101').set_color('#FF3333')
        v.get_patch_by_id('101').set_alpha(0.85)
        v.get_patch_by_id('101').set_edgecolor('#990000')
        v.get_patch_by_id('101').set_linewidth(3)
        v.get_patch_by_id('101').set_zorder(10)
    
    # Только E - теперь это '010'
    if v.get_patch_by_id('010'):
        v.get_patch_by_id('010').set_color('#33FF33')
        v.get_patch_by_id('010').set_alpha(0.85)
        v.get_patch_by_id('010').set_edgecolor('#009900')
        v.get_patch_by_id('010').set_linewidth(3)
        v.get_patch_by_id('010').set_zorder(10)
    
    # Настраиваем подписи
    for label in v.set_labels:
        if label is not None:
            label.set_fontsize(14)
            label.set_fontweight('bold')
    
    plt.title(f'Исходное выражение\n((A∩C)\\E) ∪ E\\((E∩A)∪(E∩C))\n\nРезультат: {result}', 
              fontsize=11, fontweight='bold', pad=20)
    
    # Легенда
    legend_elements = [
        plt.Rectangle((0,0), 1, 1, facecolor='#FF3333', alpha=0.85, 
                     edgecolor='#990000', linewidth=2, label='(A∩C) \\ E'),
        plt.Rectangle((0,0), 1, 1, facecolor='#33FF33', alpha=0.85,
                     edgecolor='#009900', linewidth=2, label='Только E (без A и C)')
    ]
    plt.legend(handles=legend_elements, loc='upper right', fontsize=11, 
               framealpha=0.95, fancybox=True, shadow=True)
    
    plt.tight_layout()
    plt.show()

def interactive_swapped_positions():
    """Интерактивный режим с переставленными кругами"""
    
    print("\n" + "=" * 60)
    print("ВВЕДИТЕ ВАШИ МНОЖЕСТВА")
    print("=" * 60)
    print("\nИсходное выражение: ((A ∩ C) \\ E) ∪ E \\ ((E ∩ A) ∪ (E ∩ C))")
    print("На графике круги E и C будут визуально переставлены")
    
    # Ввод элементов
    print("\nВведите элементы через пробел:")
    a_input = input("Множество A: ").split()
    c_input = input("Множество C: ").split()
    e_input = input("Множество E: ").split()
    
    # Преобразуем в множества
    try:
        if a_input and a_input[0].replace('-', '').isdigit():
            A = set(map(int, a_input))
            C = set(map(int, c_input))
            E = set(map(int, e_input))
        else:
            A = set(a_input)
            C = set(c_input)
            E = set(e_input)
    except:
        A = set(a_input)
        C = set(c_input)
        E = set(e_input)
    
    # Вычисляем исходное выражение
    part1 = A.intersection(C).difference(E)
    part2 = E.difference(E.intersection(A).union(E.intersection(C)))
    result = part1.union(part2)
    
    # Визуализация с переставленными кругами
    plt.figure(figsize=(12, 7))
    v = venn3([A, E, C], set_labels=('A', 'E', 'C'))  # E и C поменяны местами
    
    # Убираем цифры
    for text in v.subset_labels:
        if text is not None:
            text.set_text('')
    
    # Выделяем результирующие области (с учетом перестановки)
    if v.get_patch_by_id('101'):  # (A∩C)\E
        v.get_patch_by_id('101').set_color('#FF4444')
        v.get_patch_by_id('101').set_alpha(0.8)
        v.get_patch_by_id('101').set_edgecolor('darkred')
        v.get_patch_by_id('101').set_linewidth(2.5)
    
    if v.get_patch_by_id('010'):  # Только E
        v.get_patch_by_id('010').set_color('#44FF44')
        v.get_patch_by_id('010').set_alpha(0.8)
        v.get_patch_by_id('010').set_edgecolor('darkgreen')
        v.get_patch_by_id('010').set_linewidth(2.5)
    
    # Остальные области
    for patch_id in ['100', '001', '110', '011', '111']:
        if v.get_patch_by_id(patch_id):
            v.get_patch_by_id(patch_id).set_color('#D3D3D3')
            v.get_patch_by_id(patch_id).set_alpha(0.15)
            v.get_patch_by_id(patch_id).set_edgecolor('#AAAAAA')
            v.get_patch_by_id(patch_id).set_linewidth(0.5)
    
    # Настраиваем подписи
    for label in v.set_labels:
        if label is not None:
            label.set_fontsize(13)
            label.set_fontweight('bold')
    
    plt.title(f'Исходное выражение (круги E и C переставлены)\n((A∩C)\\E) ∪ E\\((E∩A)∪(E∩C))\n\nРезультат: {result}', 
              fontsize=11, fontweight='bold')
    
    # Легенда
    legend_elements = [
        plt.Rectangle((0,0), 1, 1, facecolor='#FF4444', alpha=0.8, 
                     edgecolor='darkred', linewidth=2, label=f'(A∩C)\\E = {part1}'),
        plt.Rectangle((0,0), 1, 1, facecolor='#44FF44', alpha=0.8,
                     edgecolor='darkgreen', linewidth=2, label=f'Только E = {part2}')
    ]
    plt.legend(handles=legend_elements, loc='lower left', fontsize=10, 
               framealpha=0.9, bbox_to_anchor=(0, -0.1))
    
    plt.tight_layout()
    plt.show()
    
    # Вывод результатов
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ ВЫЧИСЛЕНИЙ:")
    print("=" * 60)
    print(f"A = {A}")
    print(f"C = {C}")
    print(f"E = {E}")
    print(f"\n(A ∩ C) \\ E = {part1}")
    print(f"E \\ ((E∩A) ∪ (E∩C)) = {part2}")
    print(f"\nИТОГОВЫЙ РЕЗУЛЬТАТ = {result}")
    print("=" * 60)

# Основная программа
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("ВИЗУАЛИЗАЦИЯ ИСХОДНОГО ВЫРАЖЕНИЯ С ПЕРЕСТАВЛЕННЫМИ КРУГАМИ")
    print("=" * 60)
    print("\nИсходное выражение: ((A ∩ C) \\ E) ∪ E \\ ((E ∩ A) ∪ (E ∩ C))")
    print("На графике круги E и C поменяны местами (визуально)")
    print("Выражение НЕ ИЗМЕНЯЕТСЯ!")
    print("\nНа кругах ОТСУТСТВУЮТ цифры, выделены ТОЛЬКО результирующие области!")
    
    while True:
        print("\nВыберите режим:")
        print("1 - Стандартная визуализация (с пояснениями)")
        print("2 - Простая визуализация (минималистичная)")
        print("3 - Ввод своих множеств")
        print("4 - Выход")
        
        choice = input("\nВаш выбор (1-4): ")
        
        if choice == '1':
            visualize_swapped_positions()
        elif choice == '2':
            simple_swapped_positions()
        elif choice == '3':
            interactive_swapped_positions()
        elif choice == '4':
            print("\nДо свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")