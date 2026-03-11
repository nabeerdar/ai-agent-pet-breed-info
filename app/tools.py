import numexpr as ne


def calculate(expression):

    try:
        result = ne.evaluate(expression)
        return str(result)
    except Exception:
        return "Invalid expression"