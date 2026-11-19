---
catalog: module
lean: ByteArray.getElem_eq_data_getElem, ByteArray.uset_eq_set, ByteArray.data_mkEmpty, ByteArray.get_push_eq, ByteArray.get_push_lt, ByteArray.size_set, ByteArray.get_set_eq, ByteArray.get_set_ne, ByteArray.set_set, ByteArray.data_copySlice, ByteArray.get_append_left, ByteArray.get_append_right, ByteArray.get_extract_aux, ByteArray.get_extract, ByteArray.ofFn, ByteArray.ofFn_zero, ByteArray.ofFn_succ, ByteArray.data_ofFn, ByteArray.size_ofFn, ByteArray.get_ofFn, ByteArray.getElem_ofFn, ByteArray.mapMUnsafe, ByteArray.mapM, ByteArray.map
statement: formalized
proof: formalized
---

# ByteArray

`Batteries.Data.ByteArray`, in [Batteries/Data/ByteArray.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean), by François G. Dorais.

`ByteArray.getElem_eq_data_getElem` (theorem, [line 17](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L17))

```lean
theorem getElem_eq_data_getElem (a : ByteArray) (h : i < a.size) : a[i] = a.data[i]
```

> ### uget/uset

`ByteArray.uset_eq_set` (theorem, [line 21](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L21))

```lean
theorem uset_eq_set (a : ByteArray) {i : USize} (h : i.toNat < a.size) (v : UInt8) :
    a.uset i v h = a.set i.toNat v
```

> ### empty

`ByteArray.data_mkEmpty` (theorem, [line 26](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L26))

```lean
theorem data_mkEmpty (cap) : (emptyWithCapacity cap).data = #[]
```

> ### push

`ByteArray.get_push_eq` (theorem, [line 30](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L30))

```lean
theorem get_push_eq (a : ByteArray) (x : UInt8) : (a.push x)[a.size] = x
```

`ByteArray.get_push_lt` (theorem, [line 33](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L33))

```lean
theorem get_push_lt (a : ByteArray) (x : UInt8) (i : Nat) (h : i < a.size) :
    (a.push x)[i]'(size_push .. ▸ Nat.lt_succ_of_lt h) = a[i]
```

> ### set

`ByteArray.size_set` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L39))

```lean
theorem size_set (a : ByteArray) (i : Fin a.size) (v : UInt8) :
    (a.set i v).size = a.size
```

`ByteArray.get_set_eq` (theorem, [line 43](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L43))

```lean
theorem get_set_eq (a : ByteArray) (i : Fin a.size) (v : UInt8) : (a.set i v)[i.val] = v
```

`ByteArray.get_set_ne` (theorem, [line 46](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L46))

```lean
theorem get_set_ne (a : ByteArray) (i : Fin a.size) (v : UInt8) (hj : j < a.size) (h : i.val ≠ j) :
    (a.set i v)[j]'(a.size_set .. ▸ hj) = a[j]
```

`ByteArray.set_set` (theorem, [line 50](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L50))

```lean
theorem set_set (a : ByteArray) (i : Fin a.size) (v v' : UInt8) :
    (a.set i v).set i v' = a.set i v'
```

> ### copySlice

`ByteArray.data_copySlice` (theorem, [line 56](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L56))

```lean
theorem data_copySlice (a i b j len exact) :
  (copySlice a i b j len exact).data = b.data.extract 0 j ++ a.data.extract i (i + len)
    ++ b.data.extract (j + min len (a.data.size - i)) b.data.size
```

> ### append

`ByteArray.get_append_left` (theorem, [line 62](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L62))

```lean
theorem get_append_left {a b : ByteArray} (hlt : i < a.size)
    (h : i < (a ++ b).size := size_append .. ▸ Nat.lt_of_lt_of_le hlt (Nat.le_add_right ..)) :
    (a ++ b)[i] = a[i]
```

`ByteArray.get_append_right` (theorem, [line 67](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L67))

```lean
theorem get_append_right {a b : ByteArray} (hle : a.size ≤ i) (h : i < (a ++ b).size)
    (h' : i - a.size < b.size := Nat.sub_lt_left_of_lt_add hle (size_append .. ▸ h)) :
    (a ++ b)[i] = b[i - a.size]
```

> ### extract

`ByteArray.get_extract_aux` (theorem, [line 74](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L74))

```lean
theorem get_extract_aux {a : ByteArray} {start stop} (h : i < (a.extract start stop).size) :
    start + i < a.size
```

`ByteArray.get_extract` (theorem, [line 79](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L79))

```lean
theorem get_extract {a : ByteArray} {start stop} (h : i < (a.extract start stop).size) :
    (a.extract start stop)[i] = a[start+i]'(get_extract_aux h)
```

> ### ofFn

`ByteArray.ofFn` (definition, [line 86](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L86))

> - `ofFn f` with `f : Fin n → UInt8` returns the byte array whose `i`th element is `f i`. -

```lean
def ofFn (f : Fin n → UInt8) : ByteArray
```

`ByteArray.ofFn_zero` (theorem, [line 89](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L89))

```lean
theorem ofFn_zero (f : Fin 0 → UInt8) : ofFn f = empty
```

`ByteArray.ofFn_succ` (theorem, [line 91](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L91))

```lean
theorem ofFn_succ (f : Fin (n+1) → UInt8) :
    ofFn f = (ofFn fun i => f i.castSucc).push (f (Fin.last n))
```

`ByteArray.data_ofFn` (theorem, [line 95](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L95))

```lean
theorem data_ofFn (f : Fin n → UInt8) : (ofFn f).data = .ofFn f
```

`ByteArray.size_ofFn` (theorem, [line 100](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L100))

```lean
theorem size_ofFn (f : Fin n → UInt8) : (ofFn f).size = n
```

`ByteArray.get_ofFn` (theorem, [line 103](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L103))

```lean
theorem get_ofFn (f : Fin n → UInt8) (i : Fin (ofFn f).size) :
    (ofFn f).get i = f (i.cast (size_ofFn f))
```

`ByteArray.getElem_ofFn` (theorem, [line 107](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L107))

```lean
theorem getElem_ofFn (f : Fin n → UInt8) (i) (h : i < (ofFn f).size) :
    (ofFn f)[i] = f ⟨i, size_ofFn f ▸ h⟩
```

> ### map/mapM

`ByteArray.mapMUnsafe` (definition, [line 119](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L119))

> Unsafe optimized implementation of `mapM`.
>
> This function is unsafe because it relies on the implementation limit that the size of an array is
> always less than `USize.size`.

```lean
unsafe def mapMUnsafe [Monad m] (a : ByteArray) (f : UInt8 → m UInt8) : m ByteArray
```

`ByteArray.mapM` (definition, [line 134](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L134))

> `mapM f a` applies the monadic function `f` to each element of the array.

```lean
def mapM [Monad m] (a : ByteArray) (f : UInt8 → m UInt8) : m ByteArray
```

`ByteArray.map` (definition, [line 142](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean#L142))

> `map f a` applies the function `f` to each element of the array.

```lean
def map (a : ByteArray) (f : UInt8 → UInt8) : ByteArray
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/ByteArray.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/ByteArray.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Data.ByteArray.json)
