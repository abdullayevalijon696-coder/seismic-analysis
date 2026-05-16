"""
Seismic Earthquake Analysis Tools
Author: Alijon Abdullayev
"""

from obspy import read, UTCDateTime
from obspy.geodetics import locations2degrees
import numpy as np

class SeismicAnalyzer:
    def __init__(self, data_file):
        """Load seismic data"""
        self.stream = read(data_file)
    
    def calculate_distance(self, lat1, lon1, lat2, lon2):
        """Calculate epicentral distance"""
        distance = locations2degrees(lat1, lon1, lat2, lon2)
        return distance * 111.19
    
    def pick_waves(self, trace, threshold=0.5):
        """Simple P-wave picking"""
        data = trace.data
        max_idx = np.argmax(np.abs(data))
        return max_idx
    
    def gutenberg_richter(self, magnitudes):
        """Calculate G-R relationship"""
        m = np.array(magnitudes)
        log_n = np.log10(len(m))
        return log_n, m
    
    def plot_waveform(self):
        """Plot seismogram"""
        self.stream.plot()

# Example usage:
# analyzer = SeismicAnalyzer('data.mseed')
# distance = analyzer.calculate_distance(38.5, 67.5, 39.0, 68.0)
# analyzer.plot_waveform() 
