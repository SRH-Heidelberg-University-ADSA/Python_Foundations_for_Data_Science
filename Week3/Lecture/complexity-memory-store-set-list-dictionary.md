# How Sets Are Stored in Memory

  How an element lands in a bucket:                                                                                                    
                                                                                                                                       
  s.add(42) # only hashable objects can be added into a set (mutable objects can change so are
  not hashable hence a list cannot go into a set)
                                                                                                                                       
  1. compute hash(42) = 42                                                                                                             
  2. bucket_index = 42 % table_size = 42 % 10 = 2                                                                                      
  3. go to slot 2                                                                                                                      
  4. store hash + pointer there                                                                                                        
                                                                                                                                       
         index:  0      1      2           3      4                                                                                    
                ┌────┬─────┬───────────┬──────┬──────┐                                                                                 
                │None│ None│ hash=42   │ None │ None │                                                                                 
                │    │     │ ptr=0x7f3a│      │      │                                                                                 
                └────┴─────┴───────────┴──────┴──────┘                                                                                 
                                ↓                                                                                                      
                           heap: int(42)                                                                                               
                                                                                                                                       
  ---                                                                                                                                  
  Simple analogy:                                                                                                                      
                                                                                                                                       
  Think of it like a post office:
                                                                                                                                       
  Hash table  = row of post boxes
  Bucket      = one individual post box                                                                                                
  hash(x)     = tells you which box number to go to                                                                                    
  Pointer     = the letter inside pointing to where the package is  


# How an Element Lands in a Dict Bucket                                                                                                
                                                                                                                                       
  d = {42: "forty two"}                                                                                                                
                                                                                                                                       
  ---                                                                                                                                  
  Step by step:                                                                                                                        
                                                                                                                                       
  1. compute hash(42) = 42
  2. bucket_index = 42 % table_size = 42 % 10 = 2                                                                                      
  3. go to slot 2                                                                                                                      
  4. store hash + pointer to key + pointer to value there                                                                              
                                                                                                                                       
  ---                                                                                                                                  
  Bucket layout:                                                                                                                       
                                                                                                                                       
         index:  0      1           2                    3      4
                ┌────┬─────┬─────────────────────┬──────┬──────┐                                                                       
                │None│ None│ hash=42             │ None │ None │                                                                       
                │    │     │ key_ptr=0x7f3a      │      │      │                                                                       
                │    │     │ val_ptr=0x7f4b      │      │      │                                                                       
                └────┴─────┴─────────────────────┴──────┴──────┘                                                                       
                                ↓           ↓                                                                                          
                           heap:int(42)    heap:str("forty two")                                                                       
                                                                                                                                       
  ---                                                                                                                                  
  Compared to set:                                                                                                                     
                                                                                                                                       
  Set bucket at index 2:
  ┌─────────────────────┐                                                                                                              
  │ hash:    42         │                                                                                                              
  │ key_ptr: 0x7f3a     │  ← points to int(42) on heap                                                                                 
  └─────────────────────┘                                                                                                              
                                                                                                                                       
  Dict bucket at index 2:                                                                                                              
  ┌─────────────────────┐                                                                                                              
  │ hash:    42         │                                                                                                              
  │ key_ptr: 0x7f3a     │  ← points to int(42) on heap                                                                                 
  │ val_ptr: 0x7f4b     │  ← points to str("forty two") on heap                                                                        
  └─────────────────────┘                                                                                                              
                                                                                                                                       
  ---                                                                                                                                  
  Looking up a value:                                                                                                                  
                                                                                                                                       
  d[42]           
                                                                                                                                       
  1. hash(42) = 42                                                                                                                     
  2. bucket_index = 42 % 10 = 2                                                                                                        
  3. go to slot 2                                                                                                                      
  4. compare stored hash == hash(42)?   ✓                                                                                              
  5. compare stored key == 42?          ✓                                                                                              
  6. follow val_ptr → "forty two"                                                                                                      
                                                                                                                                       
  ---                                                                                                                                  
  Summary:                                                                                                                             
                  
  Set    → bucket holds hash + key_ptr
  Dict   → bucket holds hash + key_ptr + val_ptr                                                                                       
   
  Both   → actual objects always live on the heap                                                                                      
                  
  ▎ The only difference is the extra val_ptr in the dict bucket. Everything else — hashing, indexing, collision resolution — is        
  ▎ identical.

# How Lists Are Stored in Memory                                                                                                       
                                                                                                                                       
  lst = [10, 20, 30]                                                                                                                   
                                                                                                                                       
  ---                                                                                                                                  
  Lists are much simpler — just a contiguous array of pointers:                                                                        
                                                                                                                                       
  1. no hashing
  2. no buckets                                                                                                                        
  3. just store pointers in order, one after another                                                                                   
                                                                                                                                       
  ---                                                                                                                                  
  Memory layout:                                                                                                                       
                                                                                                                                       
         index:  0           1           2
                ┌───────────┬───────────┬───────────┐                                                                                  
                │ ptr:0x7f3a│ ptr:0x7f4b│ ptr:0x7f5c│                                                                                  
                └───────────┴───────────┴───────────┘                                                                                  
                      ↓           ↓           ↓                                                                                        
                 heap:int(10) heap:int(20) heap:int(30)                                                                                
                                                                                                                                       
  ---                                                                                                                                  
  Compared to set and dict:                                                                                                            
                                                                                                                                       
  List bucket at index 0:
  
  ┌─────────────────────┐                                                                                                              
  │ ptr: 0x7f3a         │  ← just a pointer, no hash needed                                                                            
  └─────────────────────┘                                                                                                              
                                                                                                                                       
  Set bucket at index 2:                                                                                                               
  ┌─────────────────────┐                                                                                                              
  │ hash:    42         │  ← needs hash                                                                                                
  │ key_ptr: 0x7f3a     │                                                                                                              
  └─────────────────────┘                                                                                                              
                                                                                                                                       
  Dict bucket at index 2:                                                                                                              
  ┌─────────────────────┐                                                                                                              
  │ hash:    42         │  ← needs hash                                                                                                
  │ key_ptr: 0x7f3a     │  ← needs key                                                                                                 
  │ val_ptr: 0x7f4b     │  ← needs value                                                                                               
  └─────────────────────┘                                                                                                              
                                                                                                                                       
  ---                                                                                                                                  
  How index access works:                                                                                                              
                                                                                                                                       
  lst[2]
                                                                                                                                       
  1. no hashing needed                                                                                                                 
  2. go directly to index 2                                                                                                            
  3. follow ptr → int(30)                                                                                                              
                                                                                                                                       
  One step — always O(1).                                                                                                              
                                                                                                                                       
  ---                                                                                                                                  
  Post office analogy:
                                                                                                                                       
  List:
  Post boxes are numbered 0, 1, 2...                                                                                                   
  You already know the box number (index)                                                                                              
  Open the box → get pointer → find package on heap                                                                                    
  No calculation needed                                                                                                                
                                                                                                                                       
  Set/Dict:                                                                                                                            
  You don't know the box number                                                                                                        
  hash(key) tells you which box to go to                                                                                               
  Open the box → get pointer → find package on heap                                                                                    
  Requires hash calculation first                                                                                                      
                                                                                                                                       
  ---                                                                                                                                  
  Why lists are more memory efficient than sets:                                                                                       
                                                                                                                                       
  List slot:   [ ptr ]                    ← 1 thing per slot
  Set bucket:  [ hash | ptr ]             ← 2 things per slot                                                                          
  Dict bucket: [ hash | key_ptr | val_ptr]← 3 things per slot                                                                          
                                                                                                                                       
  Also:                                                                                                                                
  List  → dense, no empty slots                                                                                                        
  Set   → sparse, ⅓ of buckets empty (load factor ⅔)                                                                                   
  Dict  → sparse, ⅓ of buckets empty (load factor ⅔)                                                                                   
                                                                                                                                       
  ---                                                                                                                                  
  Full comparison:                                                                                                                     
                                                                                                                                       
  List  → contiguous array of pointers, indexed directly
  Set   → sparse array of (hash + pointer), indexed by hash                                                                            
  Dict  → sparse array of (hash + key pointer + value pointer), indexed by hash 