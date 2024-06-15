
#include <iostream> // fonctions pour la sortie et l'entrée standard + la sortie d'erreur : iostream pour Input/Output stream

#include <fstream> //fonction pour lire et écrire dans un fichier

using namespace std;



int main()
{
	
	cout << "salut\n"; //cout : C - out      cout est un objet qui représente la sortie standard
						//on peut l'utiliser via l'opérateur "<<" pour afficher tout type de variable classique du C++
						//on peu enchainer plusieurs utilisation de "<<"
	cout << 1 << " == " << 2 << " = " << (1 == 2) << endl; //endl pour end line est le caractère de fin de ligne dans notre cas il peut varier selon le compilateur et le système

	const int size = 1'000'000;//il est possible d'écrire de grand chiffre en mettant des ' entre plusieurs suites de chiffres

	char data[size] = "Salut"; //on initialise un tableau de char d'une taille de size


	cout.write(data, size); //lors d'écriture de données brut dans le terminal (et oui ça peut servir) la fonction cout.write permert d'écrire dans le terminal les size octet présent en ram à l'adresse data
	//on constate ici que data est initialisée avec des 0 qui n'apparaissent pas dans le terminal
	//vérifions cette théorie
	cout << endl; 
	for (int i = 0; i < 50; i++)
	{
		char e = data[i];	//on accède à l'élément numero i de data
		int value = (int)e;		//on convertie le char en int : on nomme cela un cast pour caster on fait   (type)value
		cout << "data[" << i << "] = " << value << endl;
	}
	
	//toute cette logique ce retrouve avec la sortie d'erreur
	cerr << "ceci est un erreur !\n";// Quelle différence entre cout et cerr ? les deux apparaissent dans le terminal
									//il est possible de rediriger une des sorties vers un fichier par exemple mais on peut vouloir les erreur
									//ex : j'ai un programme qui fait cout une liste géométrique plus de 1G de valeurs, 
									// si je veux m'assurer que tout se déroule bien mais les 1G de valeurs me rendent avengle je redirige vers un fichier la sortie standard 
									// et je ne garde que les messages d'erreur plus importants 
									// ou inversement je ne veux pas laisser l'utilisateur lambda voir mes messages d'erreur je redirige les erreurs vers un fichier log 



	//l'entrée standard : C -in
	int x = 0;
	cout << "x = ";
	cin >> x;//l'objet cin s'utilise avec l'opérateur ">>" qui affecte une valeur à la variable passer en argument ici x ; 
			//l'opérateur ">>" s'occupe tout seul de la conversion quand celle-ci est possible ici il va convertir en entier
			//l'opérateur ">>" lit l'entrée standard jusqu'au prochain retour à la ligne
	cout << endl << "x = " << x << endl;
	cout << "taper votre pseudo >>";
	cin.read(data, 10);//comme pour cout.write on a cin.read
	cout << data << endl;;



	//Les fichiers fonctionnent relativement pareil à ceci près qu'il faut les ouvrir ou le créer


	ofstream fileOut = ofstream("text.txt");//ofstream pour out stream on ouvre le fichier text.txt en mode écriture, si il existe déjà, on le supprime purement et simplement
	fileOut << x <<endl << data <<endl;
	//l'usage de <<endl ou de <<'\n' ou encore de <<"\n" est nécessaire si on veut le lire par la suite
	
	fileOut.close();//on ferme le fichier pour permettre sa lecture 


	ifstream fileIn = ifstream("text.txt");//on ouvre le fichier en mode lecture, si il n'existe pas : ERREUR
	int y;
	char name[20];
	fileIn >> y >>name;//l'opérateur ">>" lit le fichier jusqu'au prochain saut de ligne d'ou l'utilité de <<endl
	cout << "y = " << y << endl
		<< name << endl;
	fileIn.close();//ion ferme le fichier par réflexe et par économie de mémoire


	cout << "Fin" << endl;
	return 0;
}