# Superstore
## Rapport de Nettoyage et Transformation des Données  
**Chaima AZZOUHRI**

---

## Résumé

L’objectif de ce projet était de transformer un fichier CSV transactionnel brut en un dataset propre, structuré et prêt pour l’analyse. Le fichier initial contenait des incohérences de types de données, des valeurs manquantes et ne comportait pas d’indicateurs métier calculés.

Un pipeline complet a été mis en place selon le cycle de vie de la donnée :  
**Ingestion → Nettoyage → Transformation → Analyse exploratoire → Export.**

Les principales actions réalisées incluent : correction des formats de dates, correction du type du code postal, traitement des valeurs manquantes, création de variables temporelles (Année, Mois, Trimestre), création d’un indicateur de performance logistique, et calcul des principaux indicateurs commerciaux.

Le dataset final (**superstore_clean.csv**) est cohérent, enrichi et prêt pour intégration dans PostgreSQL et visualisation via dashboard.

---

## 1. Exploration initiale des données

Le dataset contient **9800 lignes** et **18 colonnes**. Les problèmes identifiés étaient : dates stockées en texte, codes postaux au format float, **11 valeurs manquantes** dans la colonne **Postal Code**.

Il a été constaté également que certaines variables financières essentielles à une analyse complète de la rentabilité étaient absentes, notamment les variables **Profit, Quantity, Discount** ainsi que le **Cost**. Cette absence empêche le calcul du profit total, de la marge réelle, l’identification précise des produits à faible rentabilité, ainsi que l’analyse de l’impact des remises sur les ventes.

En conséquence, l’analyse financière réalisée dans ce projet a été limitée aux indicateurs basés uniquement sur la variable **Sales (chiffre d’affaires)**, qui constitue la seule mesure financière disponible dans le dataset.

---

## 2. Décisions de nettoyage

Les colonnes **Order Date** et **Ship Date**, initialement enregistrées au format texte, ont été converties en format **datetime** afin de permettre une analyse temporelle fiable (extraction de l’année, du mois et du trimestre) et d’éviter toute erreur d’interprétation du format des dates.

La colonne **Postal Code**, qui était de type **float**, a été convertie en **string** car un code postal est un identifiant et non une valeur numérique ; cette conversion permet notamment d’éviter la perte des zéros initiaux.

Enfin, les **11 valeurs manquantes** observées dans la colonne **Postal Code** ont été remplacées par la valeur **"UNKNOWN"** afin de conserver l’intégralité des lignes du dataset tout en signalant explicitement l’absence d’information.

---

## 3. Feature Engineering

Des variables temporelles (**Order Year, Order Month, Order Quarter**) ont été créées.  
Le **Delivery Delay** a été calculé comme la différence entre **Ship Date** et **Order Date**.

---

## 4. Analyse des variables

Une analyse exploratoire des variables **Sales** et **Delivery Delay** a été réalisée à l’aide de statistiques descriptives (**minimum, maximum, moyenne, écart-type**) ainsi que de visualisations graphiques (**histogrammes**).

Cette analyse n’a pas révélé de valeurs négatives, incohérentes ou impossibles.

Concernant la variable **Delivery Delay**, les délais observés sont compris entre **0 et 7 jours**, ce qui correspond à une plage réaliste pour un processus logistique standard.

Pour la variable **Sales**, certaines valeurs élevées ont été observées ; toutefois, elles ont été interprétées comme des transactions importantes légitimes (par exemple, commandes en grande quantité ou produits à prix élevé) et non comme des erreurs de saisie. En l’absence d’indications contraires, aucune correction ou suppression de ces valeurs n’a été jugée nécessaire.

---

## 5. Indicateurs calculés (KPIs)

Les indicateurs commerciaux calculés incluent :  
- **Chiffre d’affaires total**  
- **Ventes par catégorie**  
- **Ventes par région**  
- **Ventes par segment**  
- **Top 10 produits**  
- **Croissance mensuelle des ventes**

Les indicateurs liés au **Profit** n’ont pas pu être calculés en raison de l’absence de cette variable dans le dataset.

---

## 6. Préparation finale du dataset

Le dataset a été vérifié pour assurer sa cohérence globale et exporté sous le nom **superstore_clean.csv**, prêt pour intégration SQL et développement d’un dashboard.

---

## Conclusion

Ce projet a permis de transformer des données transactionnelles brutes en un dataset analytique fiable et structuré.
