# P9_matthieu_guimard

## Installer le projet sur son ordinateur

La première étape est de se mettre dans le bon répertoir de votre ordinateur et de cloner le repository

<git clone https://github.com/matthieu0guim/P9_GUIMARD_MATTHIEU.git>

Une fois le code télécharger sur votre machine vous devez créer une environnement virtuel dans lequel vous allez installer toutes les librairies nécessaires au bon fonctionnement du site.

Si vous utilisez l'outil virtualenv il vous faudra rentrer la commande qui suit.
<mkvirtualenv litreview>

Après avoir rentré cette commande vous serez directement mis dans votre environnement virtuel.
Vous pourrez alors installer les librairies avec la commande 
<pip install -r requirements.txt>

Vous devez maintenant aller dans le répertoire contenant le fichier 'manage.py' afin de pouvoir utiliser les commandes de django.

La dernière étape avant de pouvoir travailler sur le projet est de procéder aux migrations pour installer votre base de données.

Pour cela vous devez rentrer la commande:
<python manage.py migrate>


## Créer un profil développeur
Il existe deux manière pour créer un profil développeur et pouvoir gérer le site.

### Créer un profil directement sur le site.

Après avoir lancé l'environnement virtuel et le serveur en local, le développeur pourra rentrer l'adresse du serveur sur son navigateur et arrivera directement sur la page de connexion. Ici il faudra ensuite appuyer sur le bouton "S'INCRIRE".
Rentrer alors son identifiant et son mot de passe. Pour des raisons de sécurité il n'est pas possible de s'octroyer les droits directements depuis le front.
Une fois votre profil créé, vous pouvez fermer votre serveur et lancer le shell de django avec la commande:

>
> python manage.py shell
>

Une fois dans le shell il faudra importer le model User depuis votre base de données puis le profil que vous venez de créer.
Les lignes de coed qui suivent supposent que vous venez de créer un profil avec le nom d'utilisateur "Développeur"

>
> from authentication.models import User
> 
> user = User.objects.get(username="Développeur")
>

Une fois que vous avez créé l'instance de votre profil dans le shell vous pourrez alors vous attribuer le rôle de superuser nécessaire pour accéder à l'admin du site.

>
>user.is_superuser=True
>
>user.save()
>

Votre profil est maintenant superuser et vous pouvez accéder à l'admin en rajoutant /admin à la fin de l'url fourni lors du lancement de votre serveur en local.


>http://127.0.0.1:8000/admin

### Créer votre profil superuser directement en ligne de commande

Une fois que l'environnement virtuel a été lancé il est possible d'utiliser une fonctionnalité du framework django pour créer directement votre profil super unser en ligne de commande.

> python manage.py createsuper
> Nom d'utilisateur:
> Adresse électronique:
> Password:
> Password (again):
>

Lorsque vous rentrez votre mot de passe, celui-ci ne s'affiche pas à l'écran, c'est tout à fait normal. Attention aux typos!!!

Votre profil est maintenant superuser et vous pouvez accéder à l'admin en rajoutant /admin à la fin de l'url fourni lors du lancement de votre serveur en local.


>http://127.0.0.1:8000/admin
