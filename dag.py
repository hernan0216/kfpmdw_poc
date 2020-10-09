"""
Dag should be the representation of a kubeflow pipeline
"""
import argparse
import autopep8
import os
import pdb
import re
from typing import List, Union
import secrets
# from kale import Pipeline
from pydantic import BaseModel
from uuid import UUID
import kfputils
from component import Component
from edge import Edge
from jinja2 import Environment, PackageLoader, FileSystemLoader


FN_TEMPLATE = "function_template.jinja2"
PIPELINE_TEMPLATE = "pipeline_template.jinja2"

class Dag(BaseModel):  # should adopt nx.Digraph or Pipeline kale model
    """DAG representing a kubeflow pipeline."""

    name: str = "default_name"
    description: str = "default_description"
    components: List[Component] = []
    edges: List[Edge] = []

    @property
    def steps_names(self):
        return [component.name for component in self.components]

    def deploy(self):
        # experiment = POST kubeflow.compile(kwf_sdk_template, namespace) -->> http://kubelow/pipelines
        raise NotImplementedError


    def compile(self):
        """Convert Dag to KFP DSL.

        Returns path to DSL script.
        """
        # log.info("Compiling Dag into KFP DSL code")
        dsl_source = self.generate_dsl()
        return self._save_compiled_code(dsl_source)

    def generate_dsl(self):
        """Generate a Python KFP DSL executable starting from the pipeline.

        Returns (str): A Python executable script
        """
        # List of lightweight components generated code
        lightweight_components = [
            self.generate_lightweight_component(step)
            for step in self.components
        ]
        pdb.set_trace()
        pipeline_code = self.generate_pipeline(lightweight_components)
        return pipeline_code

    def generate_lightweight_component(self, step: Component):
        """Generate Python code using the function template."""
        step_source_raw = step.source

        def _encode_source(s):
            # Encode line by line a multiline string
            return "\n".join([line.encode("unicode_escape").decode("utf-8")
                              for line in s.splitlines()])

        # Since the code will be wrapped in triple quotes inside the template,
        # we need to escape triple quotes as they will not be escaped by
        # encode("unicode_escape").
        step.source = [re.sub(r"'''", "\\'\\'\\'", _encode_source(s))
                       for s in step_source_raw]

        template = self._get_templating_env().get_template(FN_TEMPLATE)
        fn_code = template.render(step=step)
        # fix code style using pep8 guidelines
        return autopep8.fix_code(fn_code)

    def generate_pipeline(self, lightweight_components):
        """Generate Python code using the pipeline template."""
        template = self._get_templating_env().get_template(PIPELINE_TEMPLATE)
        pipeline_code = template.render(
            pipeline=self,
            lightweight_components=lightweight_components
        )
        # fix code style using pep8 guidelines
        return autopep8.fix_code(pipeline_code)

    def _get_templating_env(self):
        loader = FileSystemLoader(searchpath="./")
        template_env = Environment(loader=loader)
        # add custom filters
        return template_env

    def _save_compiled_code(self, dsl_source, path: str = None) -> str:
        if not path:
            # save the generated file in a hidden local directory
            path = os.path.join(os.getcwd(), ".compile")
            os.makedirs(path, exist_ok=True)
        filename = "{}.kfpoc.py".format(self.name)
        output_path = os.path.abspath(os.path.join(path, filename))
        with open(output_path, "w") as f:
            f.write(dsl_source)
        return output_path

    def pipeline_dependencies_tasks(self, Component):
        # TODO: implemente dependency using nx.Digraph.
        return 'func_1' if Component.name == "func_2" else ""

#    def _run_compiled_code(self, script_path: str):
#        _name = self.pipeline.config.pipeline_name
#        pipeline_yaml_path = kfputils.compile_pipeline(script_path, _name)
#        kfputils.upload_pipeline(pipeline_yaml_path, _name)
#        run_name = kfputils.generate_run_name(_name)
#        kfputils.run_pipeline(
#            run_name=run_name,
#            experiment_name=self.pipeline.config.experiment_name,
#            pipeline_package_path=pipeline_yaml_path
#        )      raise NotImplementedError
