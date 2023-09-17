from path_optim import optimize_path


def test_no_path():
    assert optimize_path("") == ""


def test_go_N_when_told_N():
    assert optimize_path("N") == "N"


def test_N_and_S_should_cancel_each_other():
    assert optimize_path("NS") == ""
    assert optimize_path("SN") == ""


def test_E_and_W_should_cancel_each_other():
    assert optimize_path("EW") == ""
    assert optimize_path("WE") == ""


def test_NWE_should_be_N():
    assert optimize_path("NWE") == "N"


def test_NESWWS_should_be_WS():
    assert optimize_path("NESWWS") == "WS" # loop from the point of origin


def test_NESWSW_should_be_WS():
    assert optimize_path("NESWSW") == "SW"


def test_path_tracer_given_N_gives_steps_00_01(): # loop anywhere in the path
    assert optimize_path("ENWNNESESWSE") == "EE"
    assert optimize_path("ENEENNWS") == "ENEENNWS"
    
