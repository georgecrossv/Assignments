import org.springframework.util.StopWatch;


//import org.apache.commons.io.FileUtils;
import java.io.IOException;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import java.util.HashMap;
import java.util.Map;

import java.nio.charset.StandardCharsets;
public class Reader {

public static void main(String[] args) throws IOException 
{

	int linenumber = 0;
	Path textWithNamesFile = Paths.get("C:\\Users\\georg_ozhdqy2\\Documents\\Names\\TextWithNames.txt");
	Path namesFile = Paths.get("C:\\Users\\georg_ozhdqy2\\Documents\\Names\\Names.txt");
	Map<String, String> results = new HashMap<String, String>();
	// Start the stop watch
	
	long startTime = System.nanoTime();

	List<String> textLines = Files.readAllLines(textWithNamesFile, StandardCharsets.UTF_8);
	// Load the names file into memory

	List<String> names = Files.readAllLines(namesFile, StandardCharsets.UTF_8);
	
	// find the names in the text
	for(String name : names)
	{
		// setting linenumber to 0
		linenumber = 0;
		// create a dictionary entry
		results.put(name, "");  // adds an entry to the dictionary
		
		// find the lines that contain the name
		
		for(String line : textLines)
		{
			if(line.indexOf(name) >= 0)
			{
				
				results.put(name, results.get(name) + ", " + Integer.toString(linenumber));
			}
			linenumber++;
		}
		System.out.println("name: " + name + "; #: " + results.get(name));
	}
		
			
			
			
	long elapsedTime = System.nanoTime() - startTime;
	System.out.println("Total time elapsed: " + elapsedTime + "ms");
}
}
