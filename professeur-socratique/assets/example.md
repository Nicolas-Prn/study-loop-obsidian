### Classification Supervisée

La **Classification Supervisée** est la tâche d'apprentissage automatique la plus courante. Elle consiste à apprendre une fonction de prédiction à partir d'exemples **étiquetés**.

#### Principe

Contrairement à l'apprentissage non supervisé où l'algorithme est livré à lui-même face aux données, ici, l'algorithme dispose d'un "professeur" (le superviseur) qui lui fournit les réponses correctes pour un ensemble d'exemples d'entraînement.

- **Données :** On utilise un [[Jeu de Données (Dataset) | jeu de données]] $D_n$ composé de paires $(x_i, y_i)$ (voir [[Données en Classification Supervisée (Formalisme)]]).
    
- **Objectif :** Trouver la fonction $\hat{f}$ qui associe correctement une entrée $x$ à sa classe $y$ (voir [[Approximation de Fonction (Machine Learning)]]).
    

#### Types de Classification

Selon la nature de la sortie $y$ (l'ensemble $\mathcal{Y}$), on distingue :

1. **Classification Binaire :**
    
    - Il n'y a que **2 classes** possibles.
        
    - $\mathcal{Y} = \{0, 1\}$ ou $\{-1, +1\}$.
        
    - _Exemple :_ Le cas du Saumon vs Bar (voir graphique slide 7) ou Détection de spam (Oui/Non).
        
2. **Classification Multi-classes :**
    
    - Il y a **plus de 2 classes** ($K$ classes).
        
    - $\mathcal{Y} = \{c_1, c_2, ..., c_K\}$.
        
    - _Exemple :_ Reconnaissance de chiffres manuscrits (0 à 9), voir slide 16.
        

#### Différence avec la Régression

La différence fondamentale réside dans la nature de la variable de sortie $y$ :

- **Classification :** $y$ est une étiquette **discrète** (une catégorie, une classe).
    
- **Régression :** $y$ est une valeur **continue** (un nombre réel).
    

> [!note] Illustration visuelle
> 
> Voir le graphique du slide 19 qui compare visuellement la sortie discrète (Classification) et la sortie continue (Régression).
> ![[Pasted image 20251221133447.png]]

#### Exemple concret :
- [[Exemple Reconnaissance de Chiffres Manuscrits]]

---
Seconde note d'exemple :
---
### Le Raisonnement du Classifieur Bayes Naïf

Dans le cadre de la [[Ressources/Classification Supervisée|Classification Supervisée]], et plus spécifiquement du [[Ressources/Formalisme Probabiliste (Machine Learning)|Formalisme Probabiliste]], notre objectif est d'estimer la probabilité qu'une donnée observée $X$ appartienne à une classe $Y_k$.

Soit un vecteur de caractéristiques $X = \{X_1, X_2, ..., X_p\}$ (voir [[Ressources/Données en Classification Supervisée (Formalisme)|Données en Classification Supervisée]]). Nous cherchons à calculer la probabilité **a posteriori** :

$$\mathbb{P}(Y_k | X)$$

#### 1. Le Mur de la Réalité (Problème d'estimation directe)

Si l'on tentait de calculer $\mathbb{P}(Y_k | X)$ directement par simple statistique sur le [[Ressources/Jeu de Données (Dataset)|Jeu de Données]], on se heurterait à la **[[Ressources/Malédiction de la dimensionnalité|Malédiction de la dimensionnalité]]**.

- Pour estimer cette probabilité sans biais, il faudrait avoir observé la **combinaison exacte** de tous les attributs simultanément dans l'ensemble d'apprentissage.
    
- Comme le volume de l'espace des possibles explose exponentiellement avec le nombre d'attributs $p$, la plupart des combinaisons n'existent pas dans les données (données éparses). Le calcul statistique est impossible (division par zéro ou échantillon non représentatif). *En bref, on a pas assez d'infos pour faire une statistique sur $\mathbb{P}(Y_k | X)$.*
    

#### 2. L'Inversion du problème (Théorème de Bayes)

Pour contourner ce manque de données, on utilise la règle fondamentale du [[Ressources/Classifieur de Bayes (Machine Learning)|Classifieur de Bayes]] pour "retourner" le problème conditionnel : 
>[!note] Note
>C'est une première étape, ce qui nous intéresse est ce que cela va ensuite nous permettre de faire ! Voir paragraphe : [[Le Raisonnement du Classifieur Bayes Naïf#3. La Solution "Naïve" (Indépendance Conditionnelle)|la solution naïve]]

$$\underbrace{\mathbb{P}(Y=y|X=x)}_{\text{A posteriori}} = \frac{\overbrace{\mathbb{P}(X=x|Y=y)}^{\text{Vraisemblance}} \times \overbrace{\mathbb{P}(Y=y)}^{\text{A priori}}}{\underbrace{\mathbb{P}(X=x)}_{\text{Évidence}}}$$

- **L'intérêt :** Il est plus stable statistiquement de modéliser la distribution des attributs pour une classe donnée (la _Vraisemblance_) que l'inverse.
    
- **Le problème persistant :** Le terme de vraisemblance $\mathbb{P}(X=x|Y=y)$ reste une probabilité jointe complexe $\mathbb{P}(X_1, ..., X_p | Y_k)$ qui nécessite toujours d'observer la combinaison complète.
    

#### 3. La Solution "Naïve" (Indépendance Conditionnelle)

C'est ici qu'intervient ==l'hypothèse simplificatrice majeure==. On suppose **naïvement** que tous les attributs sont **indépendants les uns des autres conditionnellement à la classe**.

Cela permet de factoriser la probabilité jointe en un produit de probabilités marginales (voir [[Ressources/Concept de probabilité|Concept de probabilité]]) :

$$\mathbb{P}(X|Y_k) \approx \prod_{j=1}^{p} \mathbb{P}(X_{j}|Y_k)$$

**Impact sur le [[Ressources/Dilemme Biais-Variance (Bias-Variance Tradeoff)|Dilemme Biais-Variance]] :**

- **Augmentation du Biais :** L'hypothèse d'indépendance est souvent fausse dans la réalité (ex: corrélations entre attributs), ce qui éloigne le modèle de la [[Ressources/Vraie Fonction vs Modèle Appris (f vs f_chapeau)|Vraie Fonction]].
    
- **Réduction drastique de la Variance :** Comme on estime chaque paramètre $\mathbb{P}(X_{j}|Y_k)$ séparément, l'estimation est très stable même avec peu de données. Cela rend le modèle très résistant au [[Ressources/Sur-apprentissage (Overfitting)|Sur-apprentissage]].
    

#### 4. La Règle de Décision Finale (MAP)

Pour classer une nouvelle donnée $X_i$, on cherche la classe $Y_k$ qui maximise la probabilité a posteriori. Le terme d'évidence $\mathbb{P}(X_i)$ étant constant pour toutes les classes, on l'ignore.

La règle de décision (Maximum A Posteriori) devient :

$$y(X_i) = \arg \max_{k} \left( \mathbb{P}(Y_k) \times \prod_{j=1}^{p} \mathbb{P}(X_{ij}|Y_k) \right)$$

Les performances de ce classifieur peuvent ensuite être évaluées via la [[Ressources/Matrice de Confusion (Machine Learning)|Matrice de Confusion]] ou le [[Ressources/Exactitude et Taux d'Erreur (Machine Learning)|Taux d'Erreur]].
***
>[!tip] La suite ?
>Maintenant, il va falloir décider de comment on estime nos fameux $\mathbb{P}(X_{ij}|Y_k)$...
>Pour cela, voir : [[Méthodes d'Estimation pour Bayes Naïf (Types d'Attributs)]].