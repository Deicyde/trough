---
catalog: module
lean: Batteries.DList.toList_ofList, Batteries.DList.ofList_toList, Batteries.DList.toList_empty, Batteries.DList.toList_singleton, Batteries.DList.toList_append, Batteries.DList.toList_cons, Batteries.DList.toList_push, Batteries.DList.singleton_eq_ofThunk, Batteries.DList.ofThunk_coe
statement: formalized
proof: formalized
---

# Difference list

`Batteries.Data.DList.Lemmas`, in [Batteries/Data/DList/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Lemmas.lean), by Leonardo de Moura.

> This file provides a few results about `DList`.
>
> A difference list is a function that, given a list, returns the original content of the
> difference list prepended to the given list. It is useful to represent elements of a given type
> as `a₁ + ... + aₙ` where `+ : α → α → α` is any operation, without actually computing.
>
> This structure supports `O(1)` `append` and `push` operations on lists, making it
> useful for append-heavy uses such as logging and pretty printing.

`Batteries.DList.toList_ofList` (theorem, [line 29](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Lemmas.lean#L29))

```lean
theorem toList_ofList (l : List α) : DList.toList (DList.ofList l) = l
```

`Batteries.DList.ofList_toList` (theorem, [line 32](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Lemmas.lean#L32))

```lean
theorem ofList_toList (l : DList α) : DList.ofList (DList.toList l) = l
```

`Batteries.DList.toList_empty` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Lemmas.lean#L39))

```lean
theorem toList_empty : toList (@empty α) = []
```

`Batteries.DList.toList_singleton` (theorem, [line 42](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Lemmas.lean#L42))

```lean
theorem toList_singleton (x : α) : toList (singleton x) = [x]
```

`Batteries.DList.toList_append` (theorem, [line 44](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Lemmas.lean#L44))

```lean
theorem toList_append (l₁ l₂ : DList α) : toList (l₁ ++ l₂) = toList l₁ ++ toList l₂
```

`Batteries.DList.toList_cons` (theorem, [line 47](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Lemmas.lean#L47))

```lean
theorem toList_cons (x : α) (l : DList α) : toList (cons x l) = x :: toList l
```

`Batteries.DList.toList_push` (theorem, [line 50](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Lemmas.lean#L50))

```lean
theorem toList_push (x : α) (l : DList α) : toList (push l x) = toList l ++ [x]
```

`Batteries.DList.singleton_eq_ofThunk` (theorem, [line 54](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Lemmas.lean#L54))

```lean
theorem singleton_eq_ofThunk {α : Type _} {a : α} : singleton a = ofThunk [a]
```

`Batteries.DList.ofThunk_coe` (theorem, [line 58](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Lemmas.lean#L58))

```lean
theorem ofThunk_coe {α : Type _} {l : List α} : ofThunk l = ofList l
```

## Depends on

- [DList/Basic](basic.md)

## Sources

- [Batteries/Data/DList/Lemmas.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Lemmas.lean)
