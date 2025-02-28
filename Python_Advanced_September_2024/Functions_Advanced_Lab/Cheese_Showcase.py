def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""

    for cheese_name, quantity in sorted_cheeses:
        result += f"{cheese_name}\n"
        sorted_quantity = sorted(quantity, reverse=True)
        result += "\n".join([str(el) for el in sorted_quantity]) + "\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)