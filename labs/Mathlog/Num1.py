import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import numpy as np
import re
from functools import reduce

# Настройка русского шрифта
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

class SuperpositionOperator:
    """Класс для работы с суперпозицией операций над множествами"""
    
    def __init__(self):
        self.operations = {}
        self.composed_operations = {}
    
    def define_operation(self, name, expression, variables):
        """
        Определение новой операции через суперпозицию
        name: имя новой операции
        expression: выражение, определяющее операцию
        variables: список переменных (множеств), участвующих в операции
        """
        self.operations[name] = {
            'expression': expression,
            'variables': variables,
            'arity': len(variables)
        }
        print(f"✓ Операция '{name}' определена: {name}({', '.join(variables)}) = {expression}")
    
    def apply_operation(self, name, sets):
        """
        Применение определенной операции к конкретным множествам
        """
        if name not in self.operations:
            raise ValueError(f"Операция '{name}' не определена")
        
        op_info = self.operations[name]
        if len(sets) != op_info['arity']:
            raise ValueError(f"Операция '{name}' требует {op_info['arity']} аргументов, получено {len(sets)}")
        
        # Создаем словарь для подстановки
        substitution = {var: sets[i] for i, var in enumerate(op_info['variables'])}
        
        # Вычисляем выражение
        return self._evaluate_expression(op_info['expression'], substitution)
    
    def compose_operations(self, name, expression, operations_map):
        """
        Суперпозиция операций - создание новой операции из существующих
        operations_map: словарь {переменная_в_новой_операции: (имя_операции, аргументы)}
        """
        # Разбираем выражение и заменяем вложенные операции
        parsed_expr = expression
        
        for var, (op_name, args) in operations_map.items():
            if op_name in self.operations:
                # Создаем вызов операции в текстовом виде
                op_call = f"{op_name}({', '.join(args)})"
                parsed_expr = parsed_expr.replace(var, op_call)
        
        # Определяем все уникальные переменные (множества)
        variables = set()
        for var, (_, args) in operations_map.items():
            variables.update(args)
        variables = sorted(list(variables))
        
        # Сохраняем суперпозицию
        self.composed_operations[name] = {
            'expression': parsed_expr,
            'variables': variables,
            'base_expression': expression,
            'operations_map': operations_map
        }
        
        # Также сохраняем как обычную операцию
        self.operations[name] = {
            'expression': parsed_expr,
            'variables': variables,
            'arity': len(variables),
            'is_composition': True
        }
        
        print(f"✓ Суперпозиция операций '{name}' создана:")
        print(f"  {name}({', '.join(variables)}) = {expression}")
        print(f"  Где: {', '.join([f'{k} = {v[0]}({", ".join(v[1])})' for k, v in operations_map.items()])}")
    
    def _evaluate_expression(self, expression, substitution):
        """
        Вычисление выражения с подстановкой множеств
        """
        expr = expression
        
        # Заменяем символы операций
        expr = expr.replace('∩', '&')
        expr = expr.replace('∪', '|')
        expr = expr.replace('\\', '-')
        expr = expr.replace('△', '^')
        
        # Заменяем вызовы операций
        for op_name, op_info in self.operations.items():
            if op_name in expr:
                # Находим вызовы операций в выражении
                pattern = rf'{op_name}\(([^)]+)\)'
                matches = re.findall(pattern, expr)
                for match in matches:
                    args_names = [arg.strip() for arg in match.split(',')]
                    # Рекурсивно вычисляем аргументы
                    args_values = []
                    for arg_name in args_names:
                        if arg_name in substitution:
                            args_values.append(substitution[arg_name])
                        elif arg_name in self.operations:
                            # Вложенный вызов операции
                            args_values.append(self.apply_operation(arg_name, 
                                [substitution.get(a, a) for a in args_names]))
                        else:
                            raise ValueError(f"Неизвестная переменная или операция: {arg_name}")
                    
                    # Вычисляем операцию
                    result = self.apply_operation(op_name, args_values)
                    # Заменяем вызов на временную переменную
                    temp_var = f"__temp_{op_name}_{len(matches)}__"
                    substitution[temp_var] = result
                    expr = expr.replace(f"{op_name}({match})", temp_var)
        
        # Заменяем переменные
        for var, set_value in substitution.items():
            expr = expr.replace(var, f'set_value_{var}')
            # Сохраняем значение в локальной переменной
            globals()[f'set_value_{var}'] = set_value
        
        # Безопасное вычисление
        try:
            # Создаем безопасное пространство имен
            namespace = {f'set_value_{k}': v for k, v in substitution.items()}
            result = eval(expr, {"__builtins__": {}}, namespace)
            return result
        except Exception as e:
            print(f"Ошибка вычисления: {e}")
            return None
    
    def visualize_superposition(self, expression, base_sets, operations_to_apply=None):
        """
        Визуализация суперпозиции операций
        """
        if operations_to_apply:
            # Применяем последовательность операций
            result = None
            for op_name, args in operations_to_apply:
                if op_name in self.operations:
                    sets = [base_sets[arg] for arg in args]
                    result = self.apply_operation(op_name, sets)
            return result
        else:
            # Вычисляем выражение напрямую
            return self._evaluate_expression(expression, base_sets)

class SetExpressionVisualizer:
    """Класс для визуализации выражений над множествами"""
    
    def __init__(self):
        self.sets = {}
        self.superposition = SuperpositionOperator()
    
    def parse_expression(self, expression, sets):
        """Парсинг и вычисление выражения над множествами"""
        self.sets = sets
        
        expr = expression
        # Заменяем символы операций
        expr = expr.replace('∩', '&')
        expr = expr.replace('∪', '|')
        expr = expr.replace('\\', '-')
        expr = expr.replace('△', '^')
        
        # Заменяем названия множеств
        for set_name in sets:
            expr = expr.replace(set_name, f'sets["{set_name}"]')
        
        try:
            result = eval(expr)
            return result
        except Exception as e:
            print(f"Ошибка в выражении: {e}")
            return None
    
    def get_set_from_input(self, name):
        """Ввод множества с консоли"""
        print(f"\nВведите элементы множества {name} (через пробел):")
        elements = input().split()
        
        try:
            if elements and all(e.replace('-', '').isdigit() for e in elements):
                return set(map(int, elements))
            else:
                return set(elements)
        except:
            return set(elements)
    
    def visualize_expression(self, expression, sets, result_set, title=None):
        """Визуализация выражения на кругах Эйлера"""
        num_sets = len(sets)
        
        if num_sets == 2:
            self._visualize_2sets(expression, sets, result_set, title)
        elif num_sets == 3:
            self._visualize_3sets(expression, sets, result_set, title)
        else:
            print(f"Визуализация для {num_sets} множеств не поддерживается")
    
    def _visualize_2sets(self, expression, sets, result_set, title=None):
        """Визуализация для 2 множеств"""
        set_names = list(sets.keys())
        A, B = sets[set_names[0]], sets[set_names[1]]
        
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        # Исходные множества
        ax1 = axes[0]
        v1 = venn2([A, B], set_labels=(set_names[0], set_names[1]), ax=ax1)
        for text in v1.subset_labels:
            if text: text.set_text('')
        ax1.set_title('Исходные множества', fontsize=12, fontweight='bold')
        
        # Результат
        ax2 = axes[1]
        v2 = venn2([A, B], set_labels=(set_names[0], set_names[1]), ax=ax2)
        for text in v2.subset_labels:
            if text: text.set_text('')
        
        # Определяем области результата
        highlight_regions = []
        regions = {
            '10': A.difference(B),
            '01': B.difference(A),
            '11': A.intersection(B)
        }
        
        for region_id, region_set in regions.items():
            if region_set and any(elem in result_set for elem in region_set):
                highlight_regions.append(region_id)
        
        # Оформление
        for patch in v2.patches:
            patch.set_color('#E0E0E0')
            patch.set_alpha(0.2)
            patch.set_edgecolor('#CCCCCC')
        
        colors = ['#FF4444', '#44FF44', '#4444FF']
        for i, region in enumerate(highlight_regions):
            if v2.get_patch_by_id(region):
                v2.get_patch_by_id(region).set_color(colors[i % len(colors)])
                v2.get_patch_by_id(region).set_alpha(0.8)
                v2.get_patch_by_id(region).set_linewidth(2.5)
        
        for label in v2.set_labels:
            if label:
                label.set_fontsize(12)
                label.set_fontweight('bold')
        
        display_title = title or f'Результат: {result_set}'
        ax2.set_title(display_title, fontsize=11, fontweight='bold')
        
        plt.suptitle(f'Выражение: {expression}\nРезультат: {result_set}', 
                     fontsize=12, fontweight='bold', y=1.05)
        plt.tight_layout()
        plt.show()
    
    def _visualize_3sets(self, expression, sets, result_set, title=None):
        """Визуализация для 3 множеств"""
        set_names = list(sets.keys())
        A, B, C = sets[set_names[0]], sets[set_names[1]], sets[set_names[2]]
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # Исходные множества
        ax1 = axes[0]
        v1 = venn3([A, B, C], set_labels=(set_names[0], set_names[1], set_names[2]), ax=ax1)
        for text in v1.subset_labels:
            if text: text.set_text('')
        ax1.set_title('Исходные множества', fontsize=12, fontweight='bold')
        
        # Результат
        ax2 = axes[1]
        v2 = venn3([A, B, C], set_labels=(set_names[0], set_names[1], set_names[2]), ax=ax2)
        for text in v2.subset_labels:
            if text: text.set_text('')
        
        # Определяем области результата
        regions = {
            '100': A.difference(B.union(C)),
            '010': B.difference(A.union(C)),
            '001': C.difference(A.union(B)),
            '110': A.intersection(B).difference(C),
            '101': A.intersection(C).difference(B),
            '011': B.intersection(C).difference(A),
            '111': A.intersection(B).intersection(C)
        }
        
        highlight_regions = []
        for region_id, region_set in regions.items():
            if region_set and any(elem in result_set for elem in region_set):
                highlight_regions.append(region_id)
        
        # Оформление
        for patch in v2.patches:
            patch.set_color('#E0E0E0')
            patch.set_alpha(0.2)
            patch.set_edgecolor('#CCCCCC')
        
        colors = ['#FF4444', '#44FF44', '#4444FF', '#FFAA44', '#FF44FF', '#44FFFF', '#AA44FF']
        for i, region in enumerate(highlight_regions):
            if v2.get_patch_by_id(region):
                v2.get_patch_by_id(region).set_color(colors[i % len(colors)])
                v2.get_patch_by_id(region).set_alpha(0.8)
                v2.get_patch_by_id(region).set_linewidth(2.5)
        
        for label in v2.set_labels:
            if label:
                label.set_fontsize(12)
                label.set_fontweight('bold')
        
        display_title = title or f'Результат: {result_set}'
        ax2.set_title(display_title, fontsize=11, fontweight='bold')
        
        plt.suptitle(f'Выражение: {expression}\nРезультат: {result_set}', 
                     fontsize=12, fontweight='bold', y=1.05)
        plt.tight_layout()
        plt.show()
    
    def superposition_mode(self):
        """Режим работы с суперпозицией операций"""
        print("\n" + "="*60)
        print("РЕЖИМ СУПЕРПОЗИЦИИ ОПЕРАЦИЙ")
        print("="*60)
        print("\nСуперпозиция позволяет создавать сложные операции из простых")
        
        while True:
            print("\n--- МЕНЮ СУПЕРПОЗИЦИИ ---")
            print("1 - Определить новую базовую операцию")
            print("2 - Создать суперпозицию операций")
            print("3 - Применить операцию к множествам")
            print("4 - Показать все определенные операции")
            print("5 - Пример суперпозиции")
            print("6 - Назад")
            
            choice = input("\nВыберите действие: ").strip()
            
            if choice == '1':
                self._define_operation()
            elif choice == '2':
                self._create_superposition()
            elif choice == '3':
                self._apply_operation()
            elif choice == '4':
                self._show_operations()
            elif choice == '5':
                self._example_superposition()
            elif choice == '6':
                break
            else:
                print("Неверный выбор!")
    
    def _define_operation(self):
        """Определение новой операции"""
        print("\n--- ОПРЕДЕЛЕНИЕ НОВОЙ ОПЕРАЦИИ ---")
        name = input("Имя операции (например, 'sym_diff'): ").strip()
        variables = input("Переменные через пробел (например, 'X Y'): ").strip().split()
        expression = input(f"Выражение для {name}({', '.join(variables)}): ").strip()
        
        self.superposition.define_operation(name, expression, variables)
    
    def _create_superposition(self):
        """Создание суперпозиции операций"""
        print("\n--- СОЗДАНИЕ СУПЕРПОЗИЦИИ ---")
        name = input("Имя новой операции: ").strip()
        expression = input("Выражение для суперпозиции (используйте переменные): ").strip()
        
        print("\nСопоставьте переменные существующим операциям:")
        operations_map = {}
        
        # Находим все переменные в выражении
        import re
        variables = re.findall(r'\b[A-Za-z_][A-Za-z0-9_]*\b', expression)
        variables = [v for v in variables if v not in ['∩', '∪', '\\', '△']]
        
        for var in set(variables):
            print(f"\nДля переменной '{var}':")
            op_name = input(f"  Имя операции (или 'set' если это множество): ").strip()
            if op_name != 'set' and op_name in self.superposition.operations:
                args = input(f"  Аргументы для {op_name} (через пробел): ").strip().split()
                operations_map[var] = (op_name, args)
            else:
                operations_map[var] = ('set', [var])
        
        self.superposition.compose_operations(name, expression, operations_map)
    
    def _apply_operation(self):
        """Применение операции к множествам"""
        print("\n--- ПРИМЕНЕНИЕ ОПЕРАЦИИ ---")
        
        # Показываем доступные операции
        if not self.superposition.operations:
            print("Нет определенных операций. Сначала определите операции.")
            return
        
        print("\nДоступные операции:")
        for op_name, op_info in self.superposition.operations.items():
            print(f"  {op_name}({', '.join(op_info['variables'])})")
        
        op_name = input("\nИмя операции: ").strip()
        
        if op_name not in self.superposition.operations:
            print("Операция не найдена!")
            return
        
        op_info = self.superposition.operations[op_name]
        
        # Ввод множеств
        sets = {}
        for var in op_info['variables']:
            print(f"\nМножество {var}:")
            elements = input("Элементы через пробел: ").strip().split()
            try:
                if elements and all(e.replace('-', '').isdigit() for e in elements):
                    sets[var] = set(map(int, elements))
                else:
                    sets[var] = set(elements)
            except:
                sets[var] = set(elements)
        
        # Применяем операцию
        result = self.superposition.apply_operation(op_name, [sets[var] for var in op_info['variables']])
        
        print(f"\nРезультат {op_name}({', '.join(op_info['variables'])}):")
        print(f"  {result}")
        
        # Визуализация
        if len(op_info['variables']) in [2, 3]:
            self.visualize_expression(
                op_info['expression'], 
                sets, 
                result,
                title=f"Операция {op_name}: {result}"
            )
    
    def _show_operations(self):
        """Показать все определенные операции"""
        print("\n--- ОПРЕДЕЛЕННЫЕ ОПЕРАЦИИ ---")
        
        if not self.superposition.operations:
            print("Нет определенных операций")
            return
        
        for op_name, op_info in self.superposition.operations.items():
            print(f"\n{op_name}({', '.join(op_info['variables'])})")
            print(f"  Выражение: {op_info['expression']}")
            if op_info.get('is_composition'):
                print(f"  (суперпозиция)")
    
    def _example_superposition(self):
        """Пример использования суперпозиции"""
        print("\n--- ПРИМЕР СУПЕРПОЗИЦИИ ---")
        
        # Определяем базовые операции
        print("\n1. Определяем базовые операции:")
        self.superposition.define_operation("intersection", "X ∩ Y", ["X", "Y"])
        self.superposition.define_operation("union", "X ∪ Y", ["X", "Y"])
        self.superposition.define_operation("difference", "X \\ Y", ["X", "Y"])
        
        # Создаем суперпозицию
        print("\n2. Создаем суперпозицию: sym_diff = (X \\ Y) ∪ (Y \\ X)")
        self.superposition.compose_operations(
            "sym_diff",
            "A ∪ B",
            {
                "A": ("difference", ["X", "Y"]),
                "B": ("difference", ["Y", "X"])
            }
        )
        
        # Тестируем на примере
        print("\n3. Тестируем на примере:")
        X = {1, 2, 3, 4}
        Y = {3, 4, 5, 6}
        
        print(f"X = {X}")
        print(f"Y = {Y}")
        
        result = self.superposition.apply_operation("sym_diff", [X, Y])
        print(f"sym_diff(X, Y) = {result}")
        
        # Визуализируем
        sets = {"X": X, "Y": Y}
        self.visualize_expression(
            "(X \\ Y) ∪ (Y \\ X)",
            sets,
            result,
            title="Симметрическая разность через суперпозицию"
        )

# Основная программа
if __name__ == "__main__":
    print("\n" + "="*60)
    print("СУПЕРПОЗИЦИЯ ОПЕРАЦИЙ НАД МНОЖЕСТВАМИ")
    print("="*60)
    print("\nСуперпозиция - это создание новых операций из существующих")
    print("Пример: sym_diff(X,Y) = (X \\ Y) ∪ (Y \\ X)")
    
    visualizer = SetExpressionVisualizer()
    
    while True:
        print("\n" + "="*60)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*60)
        print("1 - Обычный режим (ввод выражений)")
        print("2 - Режим суперпозиции (создание новых операций)")
        print("3 - Пример суперпозиции")
        print("4 - Выход")
        
        choice = input("\nВыберите режим (1-4): ").strip()
        
        if choice == '1':
            # Обычный режим
            print("\n--- ОБЫЧНЫЙ РЕЖИМ ---")
            num_sets = input("Количество множеств (2 или 3): ").strip()
            if num_sets not in ['2', '3']:
                print("Поддерживаются только 2 или 3 множества")
                continue
            
            num_sets = int(num_sets)
            set_names = []
            for i in range(num_sets):
                name = input(f"Название множества {i+1}: ").strip().upper()
                if not name:
                    name = chr(65 + i)
                set_names.append(name)
            
            sets = {}
            for name in set_names:
                sets[name] = visualizer.get_set_from_input(name)
            
            expression = input("\nВведите выражение: ").strip()
            result = visualizer.parse_expression(expression, sets)
            
            if result is not None:
                print(f"\nРезультат: {result}")
                visualizer.visualize_expression(expression, sets, result)
        
        elif choice == '2':
            visualizer.superposition_mode()
        
        elif choice == '3':
            visualizer._example_superposition()
        
        elif choice == '4':
            print("\nДо свидания!")
            break
        else:
            print("Неверный выбор!")