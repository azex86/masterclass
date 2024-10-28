
#include <iostream> // fonctions pour la sortie et l'entr�e standard + la sortie d'erreur : iostream pour Input/Output stream

#include <fstream> //fonction pour lire et �crire dans un fichier

using namespace std;



int main()
{
	
	cout << "salut\n"; //cout : C - out      cout est un objet qui repr�sente la sortie standard
						//on peut l'utiliser via l'op�rateur "<<" pour afficher tout type de variable classique du C++
						//on peu enchainer plusieurs utilisation de "<<"
	cout << 1 << " == " << 2 << " = " << (1 == 2) << endl; //endl pour end line est le caract�re de fin de ligne dans notre cas il peut varier selon le compilateur et le syst�me

	const int size = 1'000'000;//il est possible d'�crire de grand chiffre en mettant des ' entre plusieurs suites de chiffres

	char data[size] = "Salut"; //on initialise un tableau de char d'une taille de size


	cout.write(data, size); //lors d'�criture de donn�es brut dans le terminal (et oui �a peut servir) la fonction cout.write permert d'�crire dans le terminal les size octet pr�sent en ram � l'adresse data
	//on constate ici que data est initialis�e avec des 0 qui n'apparaissent pas dans le terminal
	//v�rifions cette th�orie
	cout << endl; 
	for (int i = 0; i < 50; i++)
	{
		char e = data[i];	//on acc�de � l'�l�ment numero i de data
		int value = (int)e;		//on convertie le char en int : on nomme cela un cast pour caster on fait   (type)value
		cout << "data[" << i << "] = " << value << endl;
	}
	
	//toute cette logique ce retrouve avec la sortie d'erreur
	cerr << "ceci est un erreur !\n";// Quelle diff�rence entre cout et cerr ? les deux apparaissent dans le terminal
									//il est possible de rediriger une des sorties vers un fichier par exemple mais on peut vouloir les erreur
									//ex : j'ai un programme qui fait cout une liste g�om�trique plus de 1G de valeurs, 
									// si je veux m'assurer que tout se d�roule bien mais les 1G de valeurs me rendent avengle je redirige vers un fichier la sortie standard 
									// et je ne garde que les messages d'erreur plus importants 
									// ou inversement je ne veux pas laisser l'utilisateur lambda voir mes messages d'erreur je redirige les erreurs vers un fichier log 



	//l'entr�e standard : C -in
	int x = 0;
	cout << "x = ";
	cin >> x;//l'objet cin s'utilise avec l'op�rateur ">>" qui affecte une valeur � la variable passer en argument ici x ; 
			//l'op�rateur ">>" s'occupe tout seul de la conversion quand celle-ci est possible ici il va convertir en entier
			//l'op�rateur ">>" lit l'entr�e standard jusqu'au prochain retour � la ligne
	cout << endl << "x = " << x << endl;
	cout << "taper votre pseudo >>";
	cin.read(data, 10);//comme pour cout.write on a cin.read
	cout << data << endl;;



	//Les fichiers fonctionnent relativement pareil � ceci pr�s qu'il faut les ouvrir ou le cr�er


	ofstream fileOut = ofstream("text.txt");//ofstream pour out stream on ouvre le fichier text.txt en mode �criture, si il existe d�j�, on le supprime purement et simplement
	fileOut << x <<endl << data <<endl;
	//l'usage de <<endl ou de <<'\n' ou encore de <<"\n" est n�cessaire si on veut le lire par la suite
	
	fileOut.close();//on ferme le fichier pour permettre sa lecture 


	ifstream fileIn = ifstream("text.txt");//on ouvre le fichier en mode lecture, si il n'existe pas : ERREUR
	int y;
	char name[20];
	fileIn >> y >>name;//l'op�rateur ">>" lit le fichier jusqu'au prochain saut de ligne d'ou l'utilit� de <<endl
	cout << "y = " << y << endl
		<< name << endl;
	fileIn.close();//on ferme le fichier par r�flexe et par �conomie de m�moire


	cout << "Fin" << endl;
	return 0;
}