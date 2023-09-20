import pytest
import lib
import polars as pl

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
 
if __name__ == "__main__":
    pytest.lib()
