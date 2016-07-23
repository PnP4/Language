
import java.io.File;
import java.io.BufferedReader;
import java.io.*;

import javax.xml.transform.*;
import javax.xml.transform.stream.*;
import javax.xml.transform.dom.*;
import org.w3c.dom.*;
import javax.xml.parsers.*;

public class Check extends LanguageBaseListener{



    @Override
    public void enterMethod(LanguageParser.MethodContext ctx) {
        String value = ctx.METHOD().getText();
        boolean result = false;
        try {

            System.out.println("Method :" + value);

        }catch (Exception e){
            System.out.println(e);
        }
    }

}