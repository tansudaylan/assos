import importlib

import assos


def test_import_assos_package():
    assert hasattr(assos, '__file__')


def test_main_module_exposes_core_workflow_symbols():
    main = importlib.import_module('assos.main')
    assert hasattr(main, 'plot_imag')
    assert hasattr(main, 'init')
    assert hasattr(main, 'plot_anim')