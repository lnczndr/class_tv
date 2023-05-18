# LANA CAZANDRA U. LEGASPI - BSCPE 1-5
# CLASS TV

# creating class "tv"
class TV:
    # defining methods for:
    def __init__ (self, power, channel, volume):
        self.power = power
        self.channel = channel
        self.volume = volume

    # turning on the tv
    def power_on(self):
        self.power = True
        print ("The TV is ON.")

    # turning off the tv
    def power_off(self):
        self.power = False
        print ("The TV is OFF.")

    # getting channel
    def get_channel (self):
        self.channel = int(input("Enter channel: "))
        if channel < 120:
            print ("You are now on channel", self.channel)
        else:
            print ("The channel you've entered does not exist.")

    # setting the channel
    # getting the volume
    # setting volume
    # making the channel go up
    # making the channel go down
    # increasing the volume (up)
    # decreasing the volume (down)

# output
