from matplotlib import pyplot as plt

# dummy temperatures
temps = [10, 11, 14, 12, 10, 8, 5, 7, 10, 12, 15, 13, 12, 11, 10]

# list of x-values for plotting
xvals = list(range(len(temps)))

# say our peaks are at indices 2 and 10 (temps of 14 and 15)
peak_idx = [2, 10]

# make a new list of just the peak temp values
peak_temps = [temps[i] for i in peak_idx]

# repeat for x-values
peak_xvals = [xvals[i] for i in peak_idx]

# now we can plot the temps
plt.plot(xvals, temps)

# and add the scatter points for the peak values




xcoords = [0.22058956, 0.33088437, 2.20589566]
for xc in xcoords:
    plt.axvline(x=xc)


plt.scatter(peak_xvals, peak_temps)
plt.show()
