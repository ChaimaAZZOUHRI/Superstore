# Superstore
# Rapport de Nettoyage et Transformation des Données  
**Chaima AZZOUHRI**

---

## Résumé

L’objectif de ce projet était de transformer un fichier CSV transactionnel brut en un dataset propre, structuré et prêt pour l’analyse.  

Le fichier initial contenait :
- Des incohérences de types de données  
- Des valeurs manquantes  
- L’absence d’indicateurs métier calculés  

Un pipeline complet a été mis en place selon le cycle de vie de la donnée :

**Ingestion → Nettoyage → Transformation → Analyse exploratoire → Export**

### Principales actions réalisées

- Correction des formats de dates  
- Correction du type du code postal  
- Traitement des valeurs manquantes  
- Création de variables temporelles (Année, Mois, Trimestre)  
- Création d’un indicateur de performance logistique  
- Calcul des principaux indicateurs commerciaux  

Le dataset final (**superstore_clean.csv**) est cohérent, enrichi et prêt pour :
- Intégration dans PostgreSQL  
- Visualisation via dashboard  

---

## 1. Exploration initiale des données

Le dataset contient **9800 lignes** et **18 colonnes**.

### Problèmes identifiés :

- Dates stockées en texte  
- Codes postaux au format float  
- 11 valeurs manquantes dans la colonne `Postal Code`  

### Limitation structurelle importante

Certaines variables financières essentielles étaient absentes :
- `Profit`
- `Quantity`
- `Discount`
- `Cost`

Cette absence empêche :
- Le calcul du profit total  
- Le calcul de la marge réelle  
- L’identification précise des produits à faible rentabilité  
- L’analyse de l’impact des remises  

En conséquence, l’analyse financière a été limitée aux indicateurs basés uniquement sur la variable :

**Sales (chiffre d’affaires)**

---

## 2. Décisions de nettoyage

### Conversion des dates

Les colonnes :
- `Order Date`
- `Ship Date`

Ont été converties en format `datetime` afin de :
- Permettre une analyse temporelle fiable  
- Extraire l’année, le mois et le trimestre  
- Éviter les erreurs d’interprétation  

### Correction du type Postal Code

La colonne `Postal Code` :
- Initialement en `float`
- Convertie en `string`

Raison :
Un code postal est un identifiant et non une valeur numérique.  
Cette conversion évite notamment la perte des zéros initiaux.

### Gestion des valeurs manquantes

Les 11 valeurs manquantes de `Postal Code` ont été remplacées par :

```text
"UNKNOWN"
