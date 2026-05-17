using System;

public static class LogAnalysis 
{
    // TODO: define the 'SubstringAfter()' extension method on the `string` type
    public static string SubstringAfter(this string str, string delimiter)
    {
        /*if (str == null) 
            throw new ArgumentNullException(nameof(str));
        
        if (delimiter == null)
            throw new ArgumentNullException(nameof(delimiter));*/

        int index = str.IndexOf(delimiter);
        /*if (index == -1) // delimiter not found
        {
            return "";
        }*/
        return str.Substring(index + delimiter.Length);
    }
    
    // TODO: define the 'SubstringBetween()' extension method on the `string` type

    public static string SubstringBetween(this string str, string delimiter1, string delimiter2)
    {
        int startIndex = str.IndexOf(delimiter1);
        //if (startIndex == -1) return ""; // delimiter1 not found
        
        startIndex += delimiter1.Length; 
        int endIndex = str.IndexOf(delimiter2, startIndex);
        //if (endIndex == -1) return ""; // delimiter2 not found
        
        return str.Substring(startIndex, endIndex - startIndex);
    }

    // TODO: define the 'Message()' extension method on the `string` type

    public static string Message(this string publicLog)
    {
        return publicLog.SubstringAfter(":").Trim();
    }


    // TODO: define the 'LogLevel()' extension method on the `string` type
    public static string LogLevel(this string publicLog)
    {
        return publicLog.SubstringBetween("[","]");
    }
}