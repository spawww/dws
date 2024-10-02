% rebase('templates/base.tpl', title=title)
<p class="titolo"><img class="large" src="static/images/logo.png" alt="logo"> {{title}}</p>
% for elemento in listaFile:
 <a href="{{elemento['percorsoFile']}}">{{elemento['nomeFile']}}</a>
 <br>
 {{elemento['dataModifica']}} {{elemento['dimensione']}} 
 <br>
 <img src="static/images/separatore.png" alt="--------">
 <a href="{{elemento['percorsoFile']}}" download><img src="static/images/scarica.png" alt="scarica"></a> <br><br>
% end
% numFiles = len(listaFile)
<p class="finepagina">{{ numFiles }} files {{ size }}.</p>
