import kfp.compiler
from kfp.components import create_component_from_func

def add(value_1: int, value_2: int) -> int:
    """
    Addition
    """
    ret = value_1 + value_2
    return ret

def subtract(value_1: int, value_2: int) -> int:
    """
    Subtraction
    """
    ret = value_1 - value_2
    return ret

def multiply(value_1: int, value_2: int) -> int:
    """
    Multiplication
    """
    ret = value_1 * value_2
    return ret

add_op = create_component_from_func(add)
subtract_op = create_component_from_func(subtract)
multiply_op = create_component_from_func(multiply)

from kfp.dsl import pipeline

@pipeline(name="add example")
def my_pipeline(value_1: int, value_2: int):
    task_1 = add_op(value_1, value_2)
    task_2 = subtract_op(value_1, value_2)
    task_3 = multiply_op(task_1.output, task_2.output)

if __name__ == "__main__":
    kfp.compiler.Compiler().compile(my_pipeline, "./add_pipeline_2.yaml")
