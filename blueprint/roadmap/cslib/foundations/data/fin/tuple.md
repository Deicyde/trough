---
catalog: module
lean: Fin.castAdd_ne_natAdd, Fin.comp_append, Fin.append_update_left, Fin.append_update_right
statement: formalized
proof: formalized
---

# Appending tuples

`Cslib.Foundations.Data.Fin.Tuple`, in [Cslib/Foundations/Data/Fin/Tuple.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Fin/Tuple.lean), by Christian Reitwiessner.

> Lemmas about `Fin.append` not (yet) in Mathlib: the two parts of an appended tuple never overlap
> and appending commutes with post-composition and with updating an entry on either side.

`Fin.castAdd_ne_natAdd` (theorem, [line 26](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Fin/Tuple.lean#L26))

> The two parts of `Fin.append` never overlap.

```lean
theorem castAdd_ne_natAdd (i : Fin m) (j : Fin n) : castAdd n i ≠ natAdd m j
```

`Fin.comp_append` (theorem, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Fin/Tuple.lean#L30))

> Post-composition commutes with `Fin.append`.

```lean
theorem comp_append (f : α → β) (a : Fin m → α) (b : Fin n → α) :
    f ∘ append a b = append (f ∘ a) (f ∘ b)
```

`Fin.append_update_left` (theorem, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Fin/Tuple.lean#L36))

> Updating an entry of the left tuple is updating the appended tuple at `castAdd`.

```lean
theorem append_update_left (a : Fin m → α) (b : Fin n → α) (i : Fin m) (x : α) :
    append (Function.update a i x) b = Function.update (append a b) (castAdd n i) x
```

`Fin.append_update_right` (theorem, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Fin/Tuple.lean#L44))

> Updating an entry of the right tuple is updating the appended tuple at `natAdd`.

```lean
theorem append_update_right (a : Fin m → α) (b : Fin n → α) (i : Fin n) (x : α) :
    append a (Function.update b i x) = Function.update (append a b) (natAdd m i) x
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/Fin/Tuple.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Fin/Tuple.lean)
