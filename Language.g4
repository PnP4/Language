grammar Language;
init : com;
com : method pipe com | method;
method : METHOD | METHOD parameter;
METHOD : [a-z]+;
pipe : SINPIP;
parameter : PARAMETER | PARAMETER PARAMETER | PARAMETER IP;
PARAMETER : PARAMETERSIGN[a-z]+;
ip : IP;
IP : PARAMETERSIGN[0-9]+;
parametersign : PARAMETERSIGN;
PARAMETERSIGN : [-];
SINPIP : [|];
WS : [ \t\r\n]+ -> skip ;