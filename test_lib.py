import pytest
import lib
import polars as pl
import os


sample_csv_content = """
danceability,energy,artist_popularity,loudness
0.7,0.8,90,5.5
0.6,0.7,85,4.8
0.8,0.9,92,6.2
"""
# Define test cases for calculate_statistics function
def test_calculate_statistics():
    # Create a sample CSV file for testing
    sample_data = pl.DataFrame({
        'danceability': [0.1, 0.1, 0.1],
        'energy': [0.8, 0.7, 0.9],
        'artist_popularity': [80, 70, 90],
        'loudness': [-5, -6, -4]
    })
    lib.calculate_statistics(sample_data)


    # Verify the expected output
    # assert result['mean']['danceability'] == 0.1
    # assert result['median']['danceability'] == 0.1

# Define test cases for visualize_data function
def test_visualize_data():
    # Create a sample CSV file for testing
    sample_data = pl.DataFrame({
        'danceability': [0.7, 0.6, 0.8],
        'energy': [0.8, 0.7, 0.9],
        'artist_popularity': [80, 70, 90],
        'loudness': [-5, -6, -4]
    })
    # sample_data.write_csv('test_data.csv')


    # Test the visualize_data function
    lib.visualize_data(sample_data,"./")

    # You can add assertions here to check the expected behavior

# Define test cases for calculate_correlation function


# Clean up the test file by removing the sample data file
def teardown():
    if os.path.exists('test_data.csv'):
        os.remove('test_data.csv')

# Run the tests
if __name__ == "__main__":
    pytest.lib()
