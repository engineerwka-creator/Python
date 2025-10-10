import playground

def test_connector():
    assert playground.get_number_of_pin("Phoenix") == 12
    assert playground.get_number_of_pin("d_sub") == 9