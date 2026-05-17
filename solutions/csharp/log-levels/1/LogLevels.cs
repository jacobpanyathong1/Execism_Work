using System;
using System.Text.RegularExpressions;

static class LogLine
{
    public static string Message(string logLine)
    {    
        string pattern = @"\s+(.+)";

        string messageSent = Regex.Match(logLine, pattern).Value.Trim();

        return messageSent; 
    }

    public static string LogLevel(string logLine)
    {
        string pattern = @"^.*?\p{P}([a-zA-Z]+)\p{P}.*$";

        string messageLog = Regex.Replace(logLine, pattern, "$1").ToLower();
        
        return messageLog;
    }

    public static string Reformat(string logLine)
    {
        string searchPattern1 = @"\s+(.+)";

        string searchPattern2 = @"^.*?\p{P}([a-zA-Z]+)\p{P}.*$";

        string ccString1 = Regex.Match(logLine, searchPattern1).Value.Trim();

        string ccString2 = Regex.Replace(logLine, searchPattern2, "$1").ToLower();
        
        string newString2 = Regex.Replace(ccString2, @"[^a-zA-Z0-9\s]", "").Trim();
        
        string newMessage = $"{ccString1} ({newString2})";
        //Console.WriteLine($"printing: {newMessage}");

        return newMessage;
    }
}
