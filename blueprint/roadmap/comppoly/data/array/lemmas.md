---
catalog: module
lean: Array.eraseDups, Array.isBoolean, Array.toNum, Array.leftpad_toList, Array.rightpad_toList, Array.rightpad_getElem_eq_getD, Array.matchSize, Array.matchSize_toList, Array.getElem?_eq_toList, Array.getD_map_of_lt, Array.foldl_zipIdx_eq_foldl_toList_zipIdx, Array.foldl_zipIdx_eq_foldl_toList_zipIdx_size, Array.mem_foldl_append_of_mem, Array.mem_flatten_map_of_mem, Array.findIdxRev?, Array.findIdxRev?_def, Array.findIdxRev?_maximal, Array.findIdxRev?_eq_none, Array.findIdxRev?_empty_none, Array.findIdxRev?_eq_some, Array.rightpadPowerOfTwo, Array.rightpadPowerOfTwo_size, Array.getLast, Array.getLastD, Array.popWhile_nil_or_last_false
statement: formalized
proof: formalized
---

# Auxiliary lemmas for `Array`

`CompPoly.Data.Array.Lemmas`, in [CompPoly/Data/Array/Lemmas.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean), by Quang Dao, Gregor Mitscha-Baude.

`Array.eraseDups` (definition, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L25))

> Remove duplicates from an array while preserving first occurrences.

```lean
def eraseDups [BEq α] (xs : Array α) : Array α
```

`Array.isBoolean` (definition, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L36))

> Checks if an array of elements from a type `R` is a boolean array, i.e., if every element is
> either `0` or `1`.

```lean
def isBoolean {R : Type _} [Zero R] [One R] (a : Array R) : Prop
```

`Array.toNum` (definition, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L41))

> Interpret an array as the binary representation of a number, sending `0` to `0` and `≠ 0` to
> `1`.

```lean
def toNum {R : Type _} [Zero R] [DecidableEq R] (a : Array R) : ℕ
```

`Array.leftpad_toList` (lemma, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L44))

```lean
lemma leftpad_toList {a : Array α} {n : Nat} {unit : α} :
    a.leftpad n unit = mk (a.toList.leftpad n unit)
```

`Array.rightpad_toList` (lemma, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L49))

```lean
lemma rightpad_toList {a : Array α} {n : Nat} {unit : α} :
    a.rightpad n unit = mk (a.toList.rightpad n unit)
```

`Array.rightpad_getElem_eq_getD` (lemma, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L54))

```lean
lemma rightpad_getElem_eq_getD {a : Array α} {n : Nat} {unit : α} {i : Nat}
    (h : i < (a.rightpad n unit).size) : (a.rightpad n unit)[i] = a.getD i unit
```

`Array.matchSize` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L67))

> `Array` version of `List.matchSize`, which rightpads the arrays to the same length.

```lean
def matchSize (a b : Array α) (unit : α) : Array α × Array α
```

`Array.matchSize_toList` (lemma, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L70))

```lean
lemma matchSize_toList {a b : Array α} {unit : α} :
    matchSize a b unit =
      let (a', b') := List.matchSize a.toList b.toList unit
      (mk a', mk b')
```

`Array.getElem?_eq_toList` (lemma, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L76))

```lean
lemma getElem?_eq_toList {a : Array α} {i : ℕ} : a.toList[i]? = a[i]?
```

`Array.getD_map_of_lt` (theorem, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L81))

> `Array.map` and `getD` agree with indexed access on in-bounds indices.

```lean
theorem getD_map_of_lt {β : Type*} (xs : Array α) (f : α → β)
    (d : β) {i : Nat} (hi : i < xs.size) :
    (xs.map f).getD i d = f xs[i]
```

`Array.foldl_zipIdx_eq_foldl_toList_zipIdx` (theorem, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L87))

```lean
theorem foldl_zipIdx_eq_foldl_toList_zipIdx {β : Type*}
    (f : β → α × Nat → β) (init : β) (a : Array α) :
    a.zipIdx.foldl f init = a.toList.zipIdx.foldl f init
```

`Array.foldl_zipIdx_eq_foldl_toList_zipIdx_size` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L93))

```lean
theorem foldl_zipIdx_eq_foldl_toList_zipIdx_size {β : Type*}
    (f : β → α × Nat → β) (init : β) (a : Array α) :
    Array.foldl f init a.zipIdx 0 a.size = a.toList.zipIdx.foldl f init
```

`Array.mem_foldl_append_of_mem` (theorem, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L99))

```lean
theorem mem_foldl_append_of_mem {β : Type*}
    (xs : Array α) (f : α → Array β) {x : α} {y : β}
    (hx : x ∈ xs.toList) (hy : y ∈ (f x).toList) :
    y ∈ (xs.foldl (fun out x ↦ out ++ f x) #[]).toList
```

`Array.mem_flatten_map_of_mem` (theorem, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L133))

```lean
theorem mem_flatten_map_of_mem {β : Type*}
    (xs : Array α) (f : α → Array β) {x : α} {y : β}
    (hx : x ∈ xs.toList) (hy : y ∈ (f x).toList) :
    y ∈ (xs.map f).flatten
```

`Array.findIdxRev?` (definition, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L149))

> find index from the end of an array

```lean
def findIdxRev? (cond : α → Bool) (as : Array α) : Option (Fin as.size)
```

`Array.findIdxRev?_def` (lemma, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L161))

> if findIdxRev? finds an index, the condition is satisfied on that element

```lean
lemma findIdxRev?_def {cond} {as : Array α} {k : Fin as.size} :
    findIdxRev? cond as = some k → cond as[k]
```

`Array.findIdxRev?_maximal` (lemma, [line 172](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L172))

> if findIdxRev? finds an index, then for every greater index the condition doesn't hold

```lean
lemma findIdxRev?_maximal {cond} {as : Array α} {k : Fin as.size} :
    findIdxRev? cond as = some k → ∀ j : Fin as.size, j > k → ¬ cond as[j]
```

`Array.findIdxRev?_eq_none` (lemma, [line 197](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L197))

> if the condition is false on all elements, then findIdxRev? finds nothing

```lean
lemma findIdxRev?_eq_none {cond} {as : Array α} (h : ∀ i, (hi : i < as.size) → ¬ cond as[i]) :
    findIdxRev? cond as = none
```

`Array.findIdxRev?_empty_none` (lemma, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L214))

```lean
lemma findIdxRev?_empty_none {cond} {as : Array α} (h : as = #[]) :
    findIdxRev? cond as = none
```

`Array.findIdxRev?_eq_some` (lemma, [line 221](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L221))

> if the condition is true on some element, then findIdxRev? finds something

```lean
lemma findIdxRev?_eq_some {cond} {as : Array α} (h : ∃ i, ∃ hi : i < as.size, cond as[i]) :
    ∃ k : Fin as.size, findIdxRev? cond as = some k
```

`Array.rightpadPowerOfTwo` (definition, [line 242](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L242))

> Right-pads an array with `unit` elements until its length is a power of two. Returns the padded
> array and the number of elements added.

```lean
def rightpadPowerOfTwo (unit : α) (a : Array α) : Array α
```

`Array.rightpadPowerOfTwo_size` (lemma, [line 245](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L245))

```lean
lemma rightpadPowerOfTwo_size (unit : α) (a : Array α) :
  (a.rightpadPowerOfTwo unit).size = 2 ^ (Nat.clog 2 a.size)
```

`Array.getLast` (definition, [line 253](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L253))

> Get the last element of an array, assuming the array is non-empty.

```lean
def getLast (a : Array α) (h : a.size > 0) : α
```

`Array.getLastD` (definition, [line 256](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L256))

> Get the last element of an array, or `v₀` if the array is empty.

```lean
def getLastD (a : Array α) (v₀ : α) : α
```

`Array.popWhile_nil_or_last_false` (lemma, [line 258](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean#L258))

```lean
lemma popWhile_nil_or_last_false (p : α → Bool) (as : Array α)
    (h : (as.popWhile p).size > 0) : ¬ (p <| (as.popWhile p).getLast h)
```

## Depends on

- [Auxiliary lemmas for `List`](../list/lemmas.md)

## Sources

- [CompPoly/Data/Array/Lemmas.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Array/Lemmas.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Array.Lemmas.json)
