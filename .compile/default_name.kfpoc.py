import json

import kfp.dsl as _kfp_dsl
import kfp.components as _kfp_components

from collections import OrderedDict
from kubernetes import client as k8s_client


def func_1():
    from kale.common import mlmdutils as _kale_mlmdutils
    _kale_mlmdutils.init_metadata()

    _kale_block1 = '''
    print("Hello")
    '''

    # run the code blocks inside a jupyter kernel
    from kale.common.jputils import run_code as _kale_run_code
    from kale.common.kfputils import \
        update_uimetadata as _kale_update_uimetadata
    _kale_blocks = (
        _kale_block1,
    )
    _kale_html_artifact = _kale_run_code(_kale_blocks)
    with open("/func_1.html", "w") as f:
        f.write(_kale_html_artifact)
    _kale_update_uimetadata('func_1')

    _kale_mlmdutils.call("mark_execution_complete")


def func_2():
    from kale.common import mlmdutils as _kale_mlmdutils
    _kale_mlmdutils.init_metadata()

    _kale_block1 = '''
    print("World")
    '''

    # run the code blocks inside a jupyter kernel
    from kale.common.jputils import run_code as _kale_run_code
    from kale.common.kfputils import \
        update_uimetadata as _kale_update_uimetadata
    _kale_blocks = (
        _kale_block1,
    )
    _kale_html_artifact = _kale_run_code(_kale_blocks)
    with open("/func_2.html", "w") as f:
        f.write(_kale_html_artifact)
    _kale_update_uimetadata('func_2')

    _kale_mlmdutils.call("mark_execution_complete")


_kale_id = 1 name = 'func_1' description = 'test' base_image = 'python:3.6' packages = ['pandas'] source = ['print("Hello")']_op = _kfp_components.func_to_container_op(id=1 name='func_1' description='test' base_image='python:3.6' packages=['pandas'] source=['print("Hello")'], base_image='')


_kale_id = 2 name = 'func_2' description = 'test' base_image = 'python:3.6' packages = ['pandas'] source = ['print("World")']_op = _kfp_components.func_to_container_op(id=2 name='func_2' description='test' base_image='python:3.6' packages=['pandas'] source=['print("World")'], base_image='')


@_kfp_dsl.pipeline(
    name='',
    description=''
)
def auto_generated_pipeline():
    _kale_pvolumes_dict = OrderedDict()
    _kale_volume_step_names = []
    _kale_volume_name_parameters = []

    _kale_volume_step_names.sort()
    _kale_volume_name_parameters.sort()


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
    from kale.common.kfputils import generate_run_name
    run_name = generate_run_name('')
    run_result = client.run_pipeline(
        experiment.id, run_name, pipeline_filename, {})
