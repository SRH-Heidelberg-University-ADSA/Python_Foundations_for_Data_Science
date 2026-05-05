# Complexity Analysis of a Dynamic List in Python                                                                                    
                                                                                                                                       
  A dynamic list in Python (the built-in `list`) is implemented as a **dynamic array** under the hood.                                 
                                                                                                                                       
  ---                                                                                                                                  
                  
  ## Core Operations                                                                                                                   
                  
  | Operation        | Average Case      | Worst Case | Notes                  |                                                       
  |------------------|-------------------|------------|------------------------|
  | `list[i]`        | O(1)              | O(1)       | Direct memory offset   |                                                       
  | `list.append(x)` | **O(1) amortized**| O(n)       | Occasional resize      |                                                       
  | `list.pop()`     | O(1)              | O(1)       | Remove from end        |                                                       
  | `list.insert(i)` | O(n)              | O(n)       | Shifts elements right  |                                                       
  | `list.pop(i)`    | O(n)              | O(n)       | Shifts elements left   |                                                       
  | `list.remove(x)` | O(n)              | O(n)       | Search + shift         |                                                       
  | `x in list`      | O(n)              | O(n)       | Linear scan            |                                                       
  | `len(list)`      | O(1)              | O(1)       | Stored as a field      |                                                       
  | `list[a:b]`      | O(k)              | O(k)       | k = slice length       |                                                       
                                                                                                                                       
  ---                                                                                                                                  
                                                                                                                                       
  ## Why `append` is O(1) Amortized                                                                                                    
   
  Python doesn't allocate one slot at a time — it **over-allocates** by roughly 1.125×                                                 
  when it needs to grow:
                                                                                                                                       
  capacity: 0 → 4 → 8 → 16 → 25 → 35 → 46 ...                                                                                          
                                                                                                                                       
  So most appends just place an element in an existing slot — O(1).                                                                    
  Occasionally the array is full and Python must:                                                                                      
                                                                                                                                       
  1. Allocate a new larger block                                                                                                       
  2. Copy all n elements over → O(n)                                                                                                   
                                                                                                                                       
  **Amortized analysis** — spread the copy cost across all the appends that led to it:                                                 
                                                                                                                                       
  n appends trigger ~log(n) resizes                                                                                                    
  total copy work = n/2 + n/4 + n/8 + ... = n   (geometric series)
                                                                                                                                       
  cost per append = n total work / n appends = O(1)                                                                                    
                                                                                                                                       
  So each append costs **O(1) on average** even though individual resizes cost O(n).                                                   
                                                                                                                                       
  ---
                                                                                                                                       
  ## Why Insert/Pop in the Middle is O(n)                                                                                              
   
  Elements are stored **contiguously in memory**. Inserting at index `i` requires                                                      
  shifting everything after it one position to the right:
                                                                                                                                       
  Before: [A, B, C, D, E]                                                                                                              
  Insert X at index 1:                                                                                                                 
           shift →  →  →                                                                                                               
  After:  [A, X, B, C, D, E]                                                                                                           
                                                                                                                                       
  In the worst case (insert at index 0), you shift all n elements → O(n).                                                              
                                                                                                                                       
  ---             
                                                                                                                                       
  ## Why `list[i]` is O(1) — Pointer Array                                                                                             
   
  Python lists don't store the actual objects directly.                                                                                
  They store a contiguous array of **fixed-size pointers** (memory addresses),
  each 8 bytes on a 64-bit system.                                                                                                     
                                                                                                                                       
  list = ["hello", 42, 3.14, True]                                                                                                     
                                                                                                                                       
  Memory layout:                                                                                                                       
  ┌──────────┬──────────┬──────────┬──────────┐
  │ 0x7f3a1  │ 0x7f9b2  │ 0x7fc43  │ 0x7fd54  │                                                                                        
  └──────────┴──────────┴──────────┴──────────┘                                                                                        
       │           │          │          │                                                                                             
       ▼           ▼          ▼          ▼                                                                                             
    "hello"       42        3.14       True                                                                                            
                                                                                                                                       
  Since every pointer is the same size (8 bytes), finding index `i` is just arithmetic:                                                
                                                                                                                                       
  address of list[i] = base_address + (i × 8)                                                                                          
                                                                                                                                       
  It doesn't matter that `"hello"` is 100 bytes and `42` is 28 bytes —                                                                 
  the list only stores pointers, so indexing is always one arithmetic operation → O(1).                                                
                                                                                                                                       
  ---                                                                                                                                  
                                                                                                                                       
  ## How Python Knows the Size of Each Object                                                                                          
   
  When Python follows a pointer to an object, it finds a **PyObject** —                                                                
  a C struct that always starts with a fixed header:
                                                                                                                                       
  PyObject header (every object has this):                                                                                             
  ┌─────────────────┬─────────────────┬──────────────┐                                                                                 
  │  ob_refcount    │    ob_type      │   ob_data... │                                                                                 
  │  (8 bytes)      │   (8 bytes)     │  (variable)  │                                                                                 
  └─────────────────┴─────────────────┴──────────────┘                                                                                 
                                                                                                                                       
  - `ob_type` points to the type object (e.g. `int`, `str`, `float`)                                                                   
  - The type object knows the memory layout and size of the object                                                                     
                                                                                                                                       
  ### Fixed-size types (int, float, bool)                                                                                              
                                                                                                                                       
  The type defines the size — Python reads `ob_type → tp_basicsize` bytes:                                                             
                  
  PyLongObject (small int):
  ┌──────────────┬───────────┬───────────┐
  │  ob_refcount │  ob_type  │  ob_digit │
  │   (8 bytes)  │  (8 bytes)│  (4 bytes)│
  └──────────────┴───────────┴───────────┘
                                                                                                                                       
  ### Variable-size types (str, list, bytes)                                                                                           
                                                                                                                                       
  These have an extra `ob_size` field in the header storing the length:                                                                
                                                                                                                                       
  PyUnicodeObject ("hello"):                                                                                                           
  ┌──────────────┬───────────┬───────────┬──────────────────┐
  │  ob_refcount │  ob_type  │  ob_size  │  characters...   │                                                                          
  │   (8 bytes)  │  (8 bytes)│  (8 bytes)│  h e l l o       │                                                                          
  └──────────────┴───────────┴───────────┴──────────────────┘                                                                          
                                  │                                                                                                    
                                  └──→ 5                                                                                               
                                                                                                                                       
  This is why `len("hello")` is O(1) — Python just reads `ob_size` from the header.                                                    
                                                                                                                                       
  ---                                                                                                                                  
                                                                                                                                       
  ## Space Complexity                                                                                                                  
   
  | | Complexity |                                                                                                                     
  |---|---|       
  | Storage      | O(n)                              |                                                                                 
  | Over-allocation headroom | O(n) (constant factor ~1.125×) |                                                                        
                                                                                                                                       
  The over-allocation wastes at most ~12.5% extra memory —                                                                             
  a small price for amortized O(1) appends.                                                                                            
                                                                                                                                       
  ---             
                                                                                                                                       
  ## Practical Takeaway                                                                                                                
   
  ```python                                                                                                                            
  # Fast ✓        
  lst.append(x)       # O(1) amortized — add to end                                                                                    
  lst.pop()           # O(1) — remove from end                                                                                         
  lst[i]              # O(1) — random access                                                                                           
                                                                                                                                       
  # Slow ✗                                                                                                                             
  lst.insert(0, x)    # O(n) — avoid for large lists                                                                                   
  lst.pop(0)          # O(n) — use collections.deque instead                                                                           
  x in lst            # O(n) — use a set for membership tests                                                                          
                                                                                                                                       
  If you need fast inserts/removals at both ends, use collections.deque                                                                
  which gives O(1) for appendleft and popleft.                                                                                         
  If you need fast membership testing, use a set.