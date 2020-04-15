import showarray, generation_carte

carte,coord = generation_carte.crea_grille(10,20)
map_plus_de_ponts = generation_carte.crea_new_pont(carte,0.5,coord)
map = generation_carte.ajout_ponts(map_plus_de_ponts, 0.4, coord)
generation_carte.numero_ile(map,coord)
showarray.showtable(map)    #showarray permet d'afficher la carte
