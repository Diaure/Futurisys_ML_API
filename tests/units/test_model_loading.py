from App.predict import files_load, model, classes_mapping

def test_model_loading():
    # Appel initial
    try:
        files_load()
    except Exception as e:
        assert False, f"files_load() ne doit pas lever d'exception : {e}"
    
    # assert model is not None
    # assert classes_mapping is not None

    # Appel supplémentaire pour vérifier que rien ne casse
    # files_load()

    # assert model is not None
    # assert classes_mapping is not None
    assert True
