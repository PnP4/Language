// Generated from Language.g4 by ANTLR 4.5.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LanguageParser}.
 */
public interface LanguageListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LanguageParser#init}.
	 * @param ctx the parse tree
	 */
	void enterInit(LanguageParser.InitContext ctx);
	/**
	 * Exit a parse tree produced by {@link LanguageParser#init}.
	 * @param ctx the parse tree
	 */
	void exitInit(LanguageParser.InitContext ctx);
	/**
	 * Enter a parse tree produced by {@link LanguageParser#com}.
	 * @param ctx the parse tree
	 */
	void enterCom(LanguageParser.ComContext ctx);
	/**
	 * Exit a parse tree produced by {@link LanguageParser#com}.
	 * @param ctx the parse tree
	 */
	void exitCom(LanguageParser.ComContext ctx);
	/**
	 * Enter a parse tree produced by {@link LanguageParser#method}.
	 * @param ctx the parse tree
	 */
	void enterMethod(LanguageParser.MethodContext ctx);
	/**
	 * Exit a parse tree produced by {@link LanguageParser#method}.
	 * @param ctx the parse tree
	 */
	void exitMethod(LanguageParser.MethodContext ctx);
	/**
	 * Enter a parse tree produced by {@link LanguageParser#pipe}.
	 * @param ctx the parse tree
	 */
	void enterPipe(LanguageParser.PipeContext ctx);
	/**
	 * Exit a parse tree produced by {@link LanguageParser#pipe}.
	 * @param ctx the parse tree
	 */
	void exitPipe(LanguageParser.PipeContext ctx);
	/**
	 * Enter a parse tree produced by {@link LanguageParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(LanguageParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link LanguageParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(LanguageParser.ParameterContext ctx);
}