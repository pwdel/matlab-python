import matplotlib
import matplotlib.pyplot as plt

# https://matplotlib.org/users/annotations_intro.html

fig, ax = plt.subplots(nrows=2,ncols=1,sharex=True)

# set the overall title
ax[0].set_title('Temperature Over Time in House - Clipped Off >100dF & <30dF')

# plot out on the top chart ax0
ax[0].plot(validtimeroom0, validtemproom0, label='Upstairs Bedroom')
ax[0].plot(validtimeroom1, validtemproom1, label='First Floor')
# plot out on the bottom chart ax1
ax[1].plot(validtimeroom3, validtemproom3,'g',label='Attic')
ax[1].plot(validtimeroom6, validtemproom6,'r',label='Basement')

# automatically get handle labels
h1, l1 = ax[0].get_legend_handles_labels()
h2, l2 = ax[1].get_legend_handles_labels()
# place legends on chart
ax[0].legend(h1, l1)
ax[1].legend(h2, l2)

# Set common labels with absolute positioning on chart
fig.text(0.5, 0.05, 'linux time', ha='center', va='center')
fig.text(0.05, 0.5, 'degrees F', ha='center', va='center', rotation='vertical')

plt.show()
