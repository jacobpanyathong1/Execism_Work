class Lasagna
{
    // TODO: define the 'ExpectedMinutesInOven()' method
    public int ExpectedMinutesInOven()
    {
        return 40;
    }

    // TODO: define the 'RemainingMinutesInOven()' method
    public int RemainingMinutesInOven(int minutes)
    {
        int minutesLeft = ExpectedMinutesInOven() - minutes;
        return minutesLeft;
    }


    // TODO: define the 'PreparationTimeInMinutes()' method
    public int PreparationTimeInMinutes(int numofLayers)
    {
        int timetoPrepare = 2 * numofLayers;
        return timetoPrepare;
    }
    // TODO: define the 'ElapsedTimeInMinutes()' method
    public int ElapsedTimeInMinutes (int numofLayers,int cookTime)
    {
        int mealTime = PreparationTimeInMinutes(numofLayers) + cookTime;
        return mealTime;
    }
}
// submitting again with .net8 to check debug
//Passed Test