# Function to convert a Python function to a Component
# Can be used as a decorator and various options can be set as arguments
# add_op = create_component_from_func(
#   func=add,
#   base_image='python:3.7', # Optional: component is created as a k8s pod, and the image of the pod can be set
#   output_component_file='add.component.yaml', # Optional: component can also be compiled to yaml for easy management and reuse
#   packages_to_install=['pandas==0.24'], # Optional: if there are dependency packages not in the base image but required by the python code, they can be added during component creation
# )

from kfp.components import create_component_from_func

"""
kfp.components.create_component_from_func:
Function to convert a Python function to a Component
Can be used as a decorator and various options can be set as arguments
add_op = create_component_from_func(
    func=add,
    base_image='python:3.7', # Optional: component is created as a k8s pod, and the image of the pod can be set
    output_component_file='add.component.yaml', # Optional: component can also be compiled to yaml for easy management and reuse
    packages_to_install=['pandas==0.24'], # Optional: if there are dependency packages not in the base image but required by the python code, they can be added during component creation
)
"""

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

# After declaring Python functions, use kfp.components.create_component_from_func
# to convert them to ContainerOp type (component)
add_op = create_component_from_func(add)
subtract_op = create_component_from_func(subtract)
multiply_op = create_component_from_func(multiply)

from kfp.dsl import pipeline

@pipeline(name="add example")
def my_pipeline(value_1: int, value_2: int):
    task_1 = add_op(value_1, value_2)
    task_2 = subtract_op(value_1, value_2)
    # If you want to pass data between components,
    # connect output -> input and it will be connected in the DAG
    # Check the dependency part of the dag section in the compiled pipeline.yaml
    # Check the graph of the uploaded pipeline
    task_3 = multiply_op(task_1.output, task_2.output)
