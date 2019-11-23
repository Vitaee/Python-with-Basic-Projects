def place_tiles(room_length, room_width , tile_dim):
    placement = []
    
    num_of_tiles_per_row = int(room_length / tile_dim)
    num_of_tiles_per_col = int(room_width / tile_dim)
    prev_tile = None
    
    for c in range(num_of_tiles_per_col):
        cur_row_tiles = []
        
        
        for r in range(num_of_tiles_per_row):
            if prev_tile and prev_tile == "b":
                cur_row_tiles.append("w")
                prev_tile = "w"
                
            else:
                cur_row_tiles.append("b")
                prev_tile = "b"
        placement.append(cur_row_tiles)
        prev_tile = cur_row_tiles[0]
    return placement    

#for jupyterlab placement(4,4,1)
#or you can try print(place(4,4,1))
    