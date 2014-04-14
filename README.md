SCR_peak_detection
==================

The algorithm detects peaks given a specified threshold
+	function [Peaks, minindex]=peakdet(SCR,threshold, x)
+	 the function peakdet,detect peaks in a SCR data
+	[PEAKS, MINIDEX] = PEAKDET(SCR, THRESHOLD) finds
+	the local maxima and minima ("peaks and valleys") in the smooth SCR signal.
+	PEAKS and MININDEX contains indices in SCR, and column 2 
+	the values of the SCR.
+	
+	With [PEAKS, MINTINDEX] = PEAKDET(SCR, THRESHOLD, X) the indices
+	 in PEAKS and MININDEX  are replaced with X- values
+	
+	A datapoint is considered a peak if it has the maximal value
+	and was preceded (to the left) by a value lower by threshod.
