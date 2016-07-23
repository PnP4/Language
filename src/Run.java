import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.File;
import java.util.*;
import javax.xml.transform.*;
import javax.xml.transform.stream.*;
import javax.xml.transform.dom.*;
import org.w3c.dom.*;
import javax.xml.parsers.*;

public class Run {
    public static void main(String[] args) throws Exception{
        ANTLRInputStream input = new ANTLRInputStream(System.in);
// create a lexer that feeds off of input CharStream
        LanguageLexer lexer = new LanguageLexer(input);
// create a buffer of tokens pulled from the lexer
        CommonTokenStream tokens = new CommonTokenStream(lexer);
// create a parser that feeds off the tokens buffer
        LanguageParser parser = new LanguageParser(tokens);
        ParseTree tree = parser.init(); // begin parsing at init rule

        ParseTreeWalker walker = new ParseTreeWalker();
        walker.walk(new Check(), tree);
        System.out.println();
    }
}