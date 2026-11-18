---
catalog: module
lean: Batteries.DList, Batteries.DList.ofList, Batteries.DList.empty, Batteries.DList.toList, Batteries.DList.toList_mk, Batteries.DList.singleton, Batteries.DList.cons, Batteries.DList.append, Batteries.DList.push, Batteries.DList.ofThunk, Batteries.DList.join
statement: formalized
proof: formalized
---

# DList/Basic

`Batteries.Data.DList.Basic`, in [Batteries/Data/DList/Basic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean), by Leonardo de Moura.

`Batteries.DList` (structure, [line 17](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean#L17))

> A difference List is a Function that, given a List, returns the original
> contents of the difference List prepended to the given List.
> This structure supports `O(1)` `append` and `push` operations on lists, making it
> useful for append-heavy uses such as logging and pretty printing.

```lean
structure DList (α : Type u) where
  /-- "Run" a `DList` by appending it on the right by a `List α` to get another `List α`. -/
  apply     : List α → List α
  /-- The `apply` function of a `DList` is completely determined by the list `apply []`. -/
  invariant : ∀ l, apply l = apply [] ++ l
```

`Batteries.DList.ofList` (definition, [line 30](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean#L30))

> `O(1)` (`apply` is `O(|l|)`). Convert a `List α` into a `DList α`.

```lean
def ofList (l : List α) : DList α
```

`Batteries.DList.empty` (definition, [line 34](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean#L34))

> `O(1)` (`apply` is `O(1)`). Return an empty `DList α`.

```lean
def empty : DList α
```

`Batteries.DList.toList` (definition, [line 42](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean#L42))

> `O(apply())`. Convert a `DList α` into a `List α` by running the `apply` function.

```lean
def toList : DList α → List α
```

`Batteries.DList.toList_mk` (theorem, [line 45](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean#L45))

```lean
theorem toList_mk : toList ⟨f, h⟩ = f []
```

`Batteries.DList.singleton` (definition, [line 48](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean#L48))

> `O(1)` (`apply` is `O(1)`). A `DList α` corresponding to the list `[a]`.

```lean
def singleton (a : α) : DList α
```

`Batteries.DList.cons` (definition, [line 53](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean#L53))

> `O(1)` (`apply` is `O(1)`). Prepend `a` on a `DList α`.

```lean
def cons : α → DList α → DList α
```

`Batteries.DList.append` (definition, [line 60](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean#L60))

> `O(1)` (`apply` is `O(1)`). Append two `DList α`.

```lean
def append : DList α → DList α → DList α
```

`Batteries.DList.push` (definition, [line 70](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean#L70))

> `O(1)` (`apply` is `O(1)`). Append an element at the end of a `DList α`.

```lean
def push : DList α → α → DList α
```

`Batteries.DList.ofThunk` (definition, [line 83](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean#L83))

> Convert a lazily-evaluated `List` to a `DList`

```lean
def ofThunk (l : Thunk (List α)) : DList α
```

`Batteries.DList.join` (definition, [line 88](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean#L88))

> Concatenates a list of difference lists to form a single difference list. Similar to
> `List.join`.

```lean
def join {α : Type _} : List (DList α) → DList α
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/DList/Basic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/DList/Basic.lean)
