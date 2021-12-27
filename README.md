# P9_matthieu_guimard

## Installer le projet sur son ordinateur

La première étape est de se mettre dans le bon répertoir de votre ordinateur et de cloner le repository

``git clone https://github.com/matthieu0guim/P9_GUIMARD_MATTHIEU.git``

Une fois le code télécharger sur votre machine vous devez créer une environnement virtuel dans lequel vous allez installer toutes les librairies nécessaires au bon fonctionnement du site.

Si vous utilisez l'outil virtualenv il vous faudra rentrer la commande qui suit.
``mkvirtualenv litreview``

Après avoir rentré cette commande vous serez directement mis dans votre environnement virtuel.
Vous pourrez alors installer les librairies avec la commande 
``pip install -r requirements.txt``

Vous devez maintenant aller dans le répertoire contenant le fichier 'manage.py' afin de pouvoir utiliser les commandes de django.

La dernière étape avant de pouvoir travailler sur le projet est de procéder aux migrations pour installer votre base de données.

Pour cela vous devez rentrer la commande:
``python manage.py migrate``

## lancer le serveur

Une fois votre environnement correctement installé il ne vous reste plus qu'à faire tourner le serveur sur votre machine. Vous pourrez alors accéder au site internet avec l'interface utilisateur ou bien aller directement dans la partie administrateur mises à disposition par le framework django.

Pour lancer le serveur, assurez-vous d'être dans le dossier qui contien le fichier 'manage.py'. Rentrez alors la commande suivante:

``python manage.py runserver``

### Créer un profil développeur
Il existe deux manière pour créer un profil développeur et pouvoir gérer le site.

#### Créer un profil directement sur le site.

Après avoir lancé l'environnement virtuel et le serveur en local, le développeur pourra rentrer l'adresse du serveur sur son navigateur et arrivera directement sur la page de connexion. Ici il faudra ensuite appuyer sur le bouton "S'INCRIRE".
Rentrer alors son identifiant et son mot de passe. Pour des raisons de sécurité il n'est pas possible de s'octroyer les droits directements depuis le front.
Une fois votre profil créé, vous pouvez fermer votre serveur et lancer le shell de django avec la commande:


``python manage.py shell``


Une fois dans le shell il faudra importer le model User depuis votre base de données puis le profil que vous venez de créer.
Les lignes de coed qui suivent supposent que vous venez de créer un profil avec le nom d'utilisateur "Développeur"


`` from authentication.models import User ``

`` user = User.objects.get(username="Développeur") ``


Une fois que vous avez créé l'instance de votre profil dans le shell vous pourrez alors vous attribuer le rôle de superuser nécessaire pour accéder à l'admin du site.


``user.is_superuser=True``

``user.save()``


Votre profil est maintenant superuser et vous pouvez accéder à l'admin en rajoutant /admin à la fin de l'url fourni lors du lancement de votre serveur en local.


`` http://127.0.0.1:8000/admin ``

#### Créer votre profil superuser directement en ligne de commande

Une fois que l'environnement virtuel a été lancé il est possible d'utiliser une fonctionnalité du framework django pour créer directement votre profil super unser en ligne de commande.

``python manage.py createsuper``
``Nom d'utilisateur:``
``Adresse électronique:``
``Password:``
``Password (again):``


Lorsque vous rentrez votre mot de passe, celui-ci ne s'affiche pas à l'écran, c'est tout à fait normal. Attention aux typos!!!

Votre profil est maintenant superuser et vous pouvez accéder à l'admin en rajoutant /admin à la fin de l'url fourni lors du lancement de votre serveur en local.

`` http://127.0.0.1:8000/admin ``

## ACtions possibles sur le site

### Créer un profil utilisateur

Pour créer un profil en tant qu'utilisateur il suffit de cliquer sur le bouton ** S'INSCRIRE **  

Vous pourrez alors renseigner votre nom d'utilisateur, en respectant les spécifications indiquées, ainsi que votre mot de passe. 

Une fois les champs complétés il vous suffit de cliquer sur le bouton **S'inscrire ** en bas du cadre pour compléter la création de votre profil.

Vous serez alors redirigé vers la page de flux qui sera vide dans un premier temps.

Nous allons maintenant décrire les différentes actions possibles sur le site.

### Demander une critique de livre

Pour demander un avis concernant un livre qui vous intéresse vous pouvez créer un ticket directement depuis la page d'accueil.

Il vous suffit de cliquer sur le bouton  ** DEMANDER UNE CRITIQUE **. Vous erez alors redirigé vers la page correspondante.

Sur cette page, vous pourrez renseigner le titre de votre livre ainsi qu'une courte description, soit de ce que vous en savez soit pour affiner pour demande. Enfin, si vous l'avez sur votre ordinateur,  vous pourrez également cliquer sur le bouton ** Parcourir ** qui ouvrira l'explorateur de fichier de votre ordinateur. Vous pourrez alors aller chercher votre image et la rajouter à votre demande de critique. Il n'y a pas de taille maximale à ne pas dépasser, par contre à l'affichage l'image sera réduite.

Une fois tous le champs complétés la dernière étape est de cliquer sur le bouton ** Créer le ticket **.

Vous serez alors redirigé vers la page d'accueil et vous verrez votre demande de critique s'afficher dans votre fil d'actualité.


### Répondre à une demande de critique

Lorsque vous parcourez votre page de flux vous pourrez voir des demandandes de critiques provenant des autre utilisateurs du site auxquels vous êtes abonnés. Si la demande de critique est toujours en attente d'une réponse un bouton ** créer une critique ** sera visible en bas à droite du post. Si vous souhaitez y répondre il vous suffit de cliquer sur ce bouton. Vous serez alors redirigé vers la page du site correspondante.
Cette page affiche à l'écran les informations concernant la demande de critique.

Vous pourrez alors renseigner en quelques mots votre avis général sur le livre en question en complétant le champ 'Headline'.
Vous pourrez également attribuer une notre à ce livre en choisissant celle qui vous semble la plus appropriée. 
Enfin il sera possible d'écrire un avis détaillé dans le champ de texte plus grand situé à la fin de la page et qui s'intitule 'Body'.

Une fois que votre critique est complète vous pouvez la publier en cliquant sur le bouton ** créer la critique ** situé en bas de la page.
Après avoir cliqué sur ce bouton vous serez redirigé vers la page de flux où votre critique apparaitra.


### Créer une critique qui n'est pas une réponse à une demande

Il est également possible de spontanément créer une critique sans que celle ci ne soit demandée par un autre utilisateur.
Pour cela,  sur le page de flux de votre compte, vous pouvez cliquer directement sur le bouton ** CRÉER UNE CRITIQUE **. Vous serez alors redirigé vers la page correspondante.
Celle comporte une section correspondant à la demande d'une critique et une autre correspondant à la critique en elle même. Comme décrit précédemment pour la création d'une demande de critique vous devez renseigner le titre du livre en question,  ajouter une description de votre demande et mettre une photo de la couverture du livre.

Dans la section située en dessous vous aurez à disposition les mêmes champs que pour une critique répondant à une demande d'un utilisateur.

Une fois tous les champs complété à votre convenance vous pouvez publier votre critique en cliquant sur le bouton ** créer une critique ** situé en bas de page. Vous serez alors redirigé vers votre fil d'actualité où vous verrez à la fois votre demande de critique ainsi que votre propre réponse à cette demande.

### La page POSTS

Quatre boutons de navigations sont situés en haut à droite du site. Peut importe la page sur laquelle vous êtes, ces boutons sont toujours accessibles. L'un d'entre eux s'intitule ** Posts **. Lorsque vous cliquez dessus, le site vous redirige vers une page où vous pourrez voir l'intégralité de vos posts sur le site. Vous aurez ainsi la possibilité de modifier ou de supprimer vos tickets ainsi que vos critiques.

Pour modifier un ticket ou une critique la démarche est la même. En bas à droite de votre post, vous devez cliquer sur le bouton ** modifier **. Vous serez alors redirigé vers une page identique à celle de création d'une demande à la différence que cette fois-ci les champs sont déjà pré-remplis. Vous pouvez ainsi modifier ces informations. Une fois que vos modifications sont faites il vous sufit de cliquer sur le bouton ** confirmer les modifications ** en bas de page. Vous serez alors redirigé vers votre la page de vos propre posts. 

La suppression d'un post suit la même logique. Il vous faut pour cela cliquer sur le bouton ** supprimer ** situé à droite du bouton de modification. Vous serez alors redirigé vers une page récapitulant votre post pour vous demander la confirmation de votre choix. Si vous êtes certain de vouloir supprimer votre post il vous suffit de cliquer sur le bouton ** je suis certain **. Vous serez alors redirigé vers la page de vos posts. 
Si le post que vous venez de supprimer était une demande de critique et que cette demande avait été répondu, alors la suppression de la demande entraine automatiquement la suppression de la critique qui y était associée.

### La page Abonnement

Parmis les quatre boutons de navigation, se trouve le bouton ** Abonnements **. Cliquer dessus vous redirigera vers une page où vous pourrez gérer vos abonnements aux autres utilisateurs. 

Cette page vous permet de voir tous les utilisateurs auxquels vous êtes abonnés ainsi que les utilisateurs qui sont abonnés à votre compte. 

#### Suivre un nouvel utilisateur

Pour vous abonner à un utilisateur, vous pouvez cliquer sur le bandeau déroulant. Vous verrez alors la liste de tous les utilisateurs du site. Vous pourrez alors cliquer sur l'utilisateur que vous souhaitez suivre. Dans un deuxième temps, vous pourrez cliquer sur le bouton ** Envoyer **. Vous êtes maintenant abonné à un nouvel utilisateur du site et son nom s'ajoute à la liste de vos abonnements.

### Arréter de suivre un utilisateur

La page gérant les abonnements de votre compte liste tous les utilisateurs auxquels vous êtes abonnés. À coté du nom de l'utiliasteur que vous suivez, vous pouvez voir un bouton ** Se désabonner **. Si vous souhaiter arréter de suivre un utilisateur, il faut cliquer sur ce bouton. Vous serez alors redirigé vers une page de confirmation. Si vous êtes sûr de votre action, vous pouvez cliquer sur le bouton ** Confirmer **. Vous serez alors redirigé vers la page des abonnements et l'utilisateur n'apparaît plus dans la liste de vos abonnements.


## Accéder au côté administrateur du site.

Pour pouvoir accéder à cette foncitonnalité, il faut que vous ayez précédemment réalisé les opérations pour obtenir le status de super utilisateur. Si ce n'est pas déjà fait, vous pouvez vous reporter à la description des opération en début de documentation.

Pour accéder au côté administrateur du site, il faut modifer l'url et mettre " /admin " en bout de celui ci:
`` http://127.0.0.1:8000/admin ``

Vous serez alors redirigé vers la page de connection. Les identifiants sont les même que pour la page de connexion du site.

Une fois connecté vous verrez alors les applications développées dans le framework django ainsi que les models créés dans chacune d'entre elles.

En cliquant sur un des modèles, vous serez alors redirigé vers une page affichant toutes les informations contenues dans la table correspondante au sein de la base de données. 

Il sera possible de modifier une entrée de la table, de la supprimer et aussi d'en créer une nouvelle directement sur le coté administrateur.


## Se déconnecter.

### Depuis le site administrateur

Pour se déconnecter alors que l'on est sur l'admin de django, il faut cliquer sur le bouton ** DÉCONNEXION ** localisé tout en haut à droite. Vous serez alors redirigé vers la page de connexion principale du site.

### Depuis le coté utilisateur

Sur le site utilisateur, deux boutons permettent de vous déconnecter. Le premier se situe en haut à gauche au bout de la phrase "Vous êtes connecté en tant que [...]"
Le deuxième bouton se situe en haut à droite au bout des boutons de navigations du site.
  