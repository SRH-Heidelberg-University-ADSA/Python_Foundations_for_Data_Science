# Python List vs Set vs Tuple — Complete Comparison

| Feature | List | Set | Tuple |
|---------|------|-----|-------|
| **Ordered** | Yes | No | Yes |
| **Mutable** | Yes | Yes | No |
| **Duplicates** | Allowed | Not allowed | Allowed |
| **Index access** | Yes | No | Yes |
| **Hashable** | No | No | Yes (if elements are) |
| **Syntax** | `[1, 2, 3]` | `{1, 2, 3}` | `(1, 2, 3)` |
| **Empty** | `[]` | `set()` | `()` |
| **Backed by** | Dynamic array | Hash table | Static array |
| **Memory** | Medium | High (sparse) | Low (compact) |
| **Iteration** | O(n) | O(n) | O(n) |
| **Index access** | O(1) | N/A | O(1) |
| **Search `x in`** | O(n) | O(1) avg | O(n) |
| **Add element** | O(1) amortized | O(1) avg | N/A |
| **Remove element** | O(n) | O(1) avg | N/A |
| **Set math** | O(n²) manual | O(n) built-in | N/A |
| **Use as dict key** | No | No | Yes |
| **Best for** | Ordered mutable collection | Fast lookup / deduplication | Fixed immutable record |

---

## When to use each:

```
Need order + mutability?          → List
Need fast lookup + uniqueness?    → Set
Need fixed record + hashable?     → Tuple
```
