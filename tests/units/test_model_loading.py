from App.predict import files_load, model, classes_mapping

def test_model_loading():
    # Appel initial
    try:
        files_load()
    except Exception as e:
        assert False, f"files_load() ne doit pas lever d'exception : {e}"
 
    assert True
