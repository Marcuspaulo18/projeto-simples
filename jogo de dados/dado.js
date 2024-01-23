var dadocomp=[];
var dadojog=[];
function dado(){
    var totcomp=0;
    var totjog=0;
    for(var i=0;i<3;i++){
dadocomp[i]= Math.floor(Math.random()*6)+1; 
totcomp+=dadocomp[i];
dadojog[i]= Math.floor(Math.random()*6)+1; 
totjog+=dadojog[i];
            }
document.getElementById("comp").innerHTML=
"<img src='dado"+dadocomp[0]+".png'>"+
"<img src='dado"+dadocomp[1]+".png'>"+
"<img src='dado"+dadocomp[2]+".png'>";
document.getElementById("jog").innerHTML=
"<img src='dado"+dadojog[0]+".png'>"+
"<img src='dado"+dadojog[1]+".png'>"+
"<img src='dado"+dadojog[2]+".png'>";
var mensagem="";
if(totcomp>totjog){
    mensagem="o computador lhe venceu por("+totcomp+"a"+totjog+")";
}
else if(totcomp<totjog){
    mensagem="o jogador venceu por("+totcomp+"a"+totjog+")";
}
else{
    mensagem="ambos empataram por("+totcomp+"a"+totjog+")";
}
document.getElementById("resultado").innerHTML= mensagem;
}