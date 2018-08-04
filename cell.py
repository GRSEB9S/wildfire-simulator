class Cell:
    def __init__(self, status, size, elevation, windDirection, windSpeed, flammability):
        self.status         =  status         # unburned, burning, burned
        self.size           =  size           # side length of cell in meters
        self.elevation      =  elevation      # meters above sea level
        self.windDirection  =  windDirection  # in radians
        self.windSpeed      =  windSpeed      # in mph
        self.flammability   =  flammability   # scale of 0-10, 0 being nonflammable
        
        # More complex variables that may be added later
        #
        # self.fuelSurfaceAreaVolumeRatio  =  fuelSurfaceAreaVolumeRatio
        # self.fuelLoad                    =  fuelLoad
        # self.fuelMoistureContent         =  fuelMoistureContent 
        # self.relativeHumidity            =  relativeHumidity
        # self.temperature                 =  temperature

    '''
    def update(self, status=status, size=size, elevation=elevation, windDirection=windDirection, 
               windSpeed=windSpeed, flammability=flammability):
        self.status                      =  status
        self.size                        =  size
        self.elevation                   =  elevation
        self.windDirection               =  windDirection
        self.windSpeed                   =  windSpeed
        self.flammability                =  flammability
       
        # More complex variables that may be added later
        #
        # self.fuelSurfaceAreaVolumeRatio  =  fuelSurfaceAreaVolumeRatio
        # self.fuelLoad                    =  fuelLoad
        # self.fuelMoistureContent         =  fuelMoistureContent
        # self.relativeHumidity            =  relativeHumidity
        # self.temperature                 =  temperature
    '''

    def printCell(self):
        kBrightRed = '\x1b[38;5;9m'
        kDarkRed = '\x1b[38;5;52m'
        kColorEnd = '\x1b[0m'

        if self.status == 'unburned':
            print('O', end='')
        elif self.status == 'burning':
            print(kBrightRed + '~' + kColorEnd, end='')
        elif self.status == 'burned':
            print(kDarkRed + 'X' + kColorEnd, end='')

