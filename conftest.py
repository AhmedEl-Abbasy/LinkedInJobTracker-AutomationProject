import pytest
import structure as st

@pytest.fixture(scope="session",autouse=True)
def setup_teardown():
    st.init_withRealBrowser()
    yield 
    st.finish()
    