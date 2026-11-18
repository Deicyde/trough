---
catalog: module
lean: Set.Saturates, Set.saturates_compl, Set.saturates_eq_biUnion
statement: formalized
proof: formalized
---

# Saturation

`Cslib.Foundations.Data.Set.Saturation`, in [Cslib/Foundations/Data/Set/Saturation.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Set/Saturation.lean), by Ching-Tsun Chou.

`Set.Saturates` (definition, [line 25](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Set/Saturation.lean#L25))

> `f : ι → Set α` saturates `s : Set α` iff `f i` is a subset of `s`
> whenever `f i` and `s` has any intersection at all.

```lean
def Saturates (f : ι → Set α) (s : Set α) : Prop
```

`Set.saturates_compl` (theorem, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Set/Saturation.lean#L32))

> If `f` saturates `s`, then `f` saturates its complement `sᶜ` as well.

```lean
theorem saturates_compl (hs : Saturates f s) : Saturates f sᶜ
```

`Set.saturates_eq_biUnion` (theorem, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Set/Saturation.lean#L38))

> If `f` is a cover and saturates `s`, then `s` is the union of all `f i` that intersects `s`.

```lean
theorem saturates_eq_biUnion (hs : Saturates f s) (hc : ⋃ i, f i = univ) :
    s = ⋃ i ∈ {i | (f i ∩ s).Nonempty}, f i
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/Set/Saturation.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Set/Saturation.lean)
