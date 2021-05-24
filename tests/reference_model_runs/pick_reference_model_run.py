import os

from pick_model_runs_fun import fun_test_reference_run, get_exe_path

this_fp = os.path.dirname(os.path.abspath(__file__))
test_example_dir = os.path.abspath(os.path.join(this_fp, 'SEAWAT', '1_box', 'case1', ''))
test_example_dir = os.path.abspath(os.path.join(this_fp, 'MF2005', 'l1b2k', 'inputref'))
mf5_exe = get_exe_path(exe_name='swtv4')
mf5_exe = get_exe_path(exe_name='mf2005')

# def test_mf5_ref_run_bcf2ss(modelname='bcf2ss'):
#     fun_test_reference_run(modelname, test_example_dir, mf5_exe)
#     pass
#
# def test_mf5_ref_run_str(modelname='str'):
#     fun_test_reference_run(modelname, test_example_dir, mf5_exe)
#     pass

# /Users/bfdestombe/PycharmProjects/flopymetascript/tests/reference_model_runs/SEAWAT/1_box/case1/case1.adv
# /Users/bfdestombe/PycharmProjects/flopymetascript/tests/reference_model_runs/SEAWAT/1_box/case1/case1.nam
fun_test_reference_run('l1b2k', test_example_dir, mf5_exe, test_hds=True, test_cbc=True)
