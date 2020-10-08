def test():
    from kale.common import mlmdutils as _kale_mlmdutils
    _kale_mlmdutils.init_metadata()

    from kale.common import podutils as _kale_podutils
    _kale_mlmdutils.call("link_input_rok_artifacts")
    _kale_podutils.snapshot_pipeline_step(
        "test",
        "test",
        "/path/to/nb",
        before=True)

    _rok_snapshot_task = _kale_podutils.snapshot_pipeline_step(
        "test",
        "test",
        "/path/to/nb",
        before=False)
    _kale_mlmdutils.call("submit_output_rok_artifact", _rok_snapshot_task)

    _kale_mlmdutils.call("mark_execution_complete")