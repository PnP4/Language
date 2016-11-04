
import java.io.File;
import java.io.BufferedReader;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

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
        BufferedReader reader = null;
        File file = new File("DNS.txt");
        String[] text = null;
        try {
            reader = new BufferedReader(new FileReader(file));


            while ((text = reader.readLine().split(" ")) != null) {
                if (text[0].equals(value)) {
                    result = true;
                    break;
                }
            }

            if (result == true) {
                System.out.println("Method :" + value);
                appendToXml(text);
            } else {
                System.out.println("Method Not Found");
                System.exit(1);
            }

        }catch (Exception e){
            System.out.println(e);
        }
    }

    public void appendToXml(String[] methodDetails) throws Exception {

        DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
        Document document = documentBuilder.parse("server.xml");
        Element root = document.getDocumentElement();

        Element newServer = document.createElement("methods");
        Element newMethod = document.createElement("method");
        Element name = document.createElement("name");
        Element ip = document.createElement("ip");
        name.appendChild(document.createTextNode(methodDetails[0]));
        ip.appendChild(document.createTextNode(methodDetails[1]));
        root.appendChild(newMethod);
        newMethod.appendChild(name);
        newMethod.appendChild(ip);

        DOMSource source = new DOMSource(document);
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        StreamResult result = new StreamResult("server.xml");
        transformer.transform(source, result);

    }
}