grammar Language;
init : com;
com : method pipe com | method;
method : METHOD;
METHOD : [a-z]+;
pipe : SINPIP;
SINPIP : [|];
WS : [ \t\r\n]+ -> skip ;
