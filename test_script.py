import pytest
import lib
import polars as pl

# Test the read_csv function
# @pytest.mark.parametrize("file_path", ["test_data.csv", "test_data2.csv"])
# def test_read_csv(file_path):
#     lib.read_csv(file_path)
#     # assert isinstance(data, pl.DataFrame)
#     # # You can add more assertions based on your specific requirements

# Test the calculate_statistics function
def test_calculate_statistics():
    # Create a test DataFrame for testing
    test_data = pl.DataFrame({
        'danceability': [0.5, 0.6, 0.7],
        'energy': [0.8, 0.9, 0.6],
        'artist_popularity': [75, 80, 90],
        'loudness': [-5, -4, -3]
    })
    
    lib.calculate_statistics(test_data)
 
