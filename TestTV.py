# LANA CAZANDRA U. LEGASPI - BSCPE 1-5

# Import the tv
from tv import TV

# Make 2 TV object
# Making the first TV object
tv1 = TV()

# Turn on the TV
tv1.power_on()

# Set a channel
tv1.set_channel (30)

# Get the current channel
current_channel_tv1 = tv1.get_channel

# Set the volume
tv1.set_volume(3)

# Get the current volume
current_volume_tv1 = tv1.get_volume()

# Turn off the TV
tv1.power_off()

# Showing output
print ("TV 1's channel is ", current_channel_tv1, "and volume is ", current_volume_tv1)
print ()

# Make the second TV object
tv2 = TV()

# Repeat the process
# Turn on the second TV
tv2.power_on()

# Set a channel for the second TV
tv2.set_channel(3)

# Get the current channel of the second TV
current_channel_tv2 = tv2.get_channel()

# Set the volume for the second TV
tv2.set_volume(2)

# Get the current volume of the second TV
current_volume_tv2 = tv2.get_volume()

# Turn off the second TV
tv2.power_off()

# Print TV 2's channel and volume level
print("TV 2's channel is", current_channel_tv2, "and volume level is", current_volume_tv2)