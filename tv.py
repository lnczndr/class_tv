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
        if self.channel <= 120:
            print ("You are now on channel", self.channel)
        else:
            print ("The channel you've entered does not exist.")

    # setting the channel
    def set_channel (self, channel):
        if 0 < channel <= 120:
            self.channel = channel
            print ("The channel is set to", self.channel)
        else:
            print ("The channel is INVALID")

    # getting the volume
    def get_volume (self):
        self.volume = int(input("Enter Volume: "))
        if self.volume >= 7:
            print ("Your volume is now ", self.volume)
        else:
            print ("Your volume must be between 1-7")

    # setting volume
    def set_volume (self, volume):
        if 0 < volume <= 7:
            self.volume = volume
            print ("Your volume is set to ", self.volume)
        else:
            print ("Your volume must be between 1-7")
    
    # making the channel go up
    # making the channel go down
    # increasing the volume (up)
    # decreasing the volume (down)

# output
