
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
        BufferedReader reader = null;
        File file = new File("DNS.txt");
        String text = null;
        try {
            reader = new BufferedReader(new FileReader(file));


            while ((text = reader.readLine()) != null) {
                if (text.equals(value)) {
                    result = true;
                    break;
                }
            }

            if (result == true) {
                System.out.println("Method :" + value);
                appendToXml(value);
            } else {
                System.out.println("Method Not Found");
                System.exit(1);
            }

        }catch (Exception e){
            System.out.println(e);
        }
    }

    public void appendToXml(String methodName) throws Exception {

        DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
        Document document = documentBuilder.parse("server.xml");
        Element root = document.getDocumentElement();

        Element newServer = document.createElement("servers");
        Element name = document.createElement("name");
        name.appendChild(document.createTextNode(methodName));
        root.appendChild(name);

        DOMSource source = new DOMSource(document);
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        StreamResult result = new StreamResult("server.xml");
        transformer.transform(source, result);

    }
}