import json

import kfp.dsl as _kfp_dsl
import kfp.components as _kfp_components

from collections import OrderedDict
from kubernetes import client as k8s_client


def func_1():
    import pandas

    import numpy

    print("Hello")


def func_2():
    import pandas

    import numpy

    print("World")


func_1_op = _kfp_components.func_to_container_op(
    func_1, base_image='python:3.6')


func_2_op = _kfp_components.func_to_container_op(
    func_2, base_image='python:3.6')


@_kfp_dsl.pipeline(
    name='default_name',
    description='default_description'
)
func_1_task = func_1_op().after()

func_2_task = func_2_op().after(func_1)

if __name__ == "__main__":
    pipeline_func = auto_generated_pipeline
    pipeline_filename = pipeline_func.__name__ + '.pipeline.tar.gz'
    import kfp.compiler as compiler
    compiler.Compiler().compile(pipeline_func, pipeline_filename)

    # Get or create an experiment and submit a pipeline run
    import kfp
    client = kfp.Client()
    experiment = client.create_experiment('')

    # Submit a pipeline run
    run_name = generate_run_name('default_name')
    run_result = client.run_pipeline(
        experiment.id, run_name, pipeline_filename, {})
