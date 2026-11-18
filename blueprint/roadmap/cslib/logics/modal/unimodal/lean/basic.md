---
catalog: module
lean: Cslib.Logic.Modal.Model.unimodalOfPredicates, Cslib.Logic.Modal.Model.unimodalOfContainers, Cslib.Logic.Modal.Satisfies.unimodalOfPredicates_preserves_iff, Cslib.Logic.Modal.Satisfies.unimodalOfPredicates_preserves_reflTransGen
statement: formalized
proof: formalized
---

# Basic Modal Logic for Lean

`Cslib.Logics.Modal.Unimodal.Lean.Basic`, in [Cslib/Logics/Modal/Unimodal/Lean/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/Basic.lean), by Fabrizio Montesi.

`Cslib.Logic.Modal.Model.unimodalOfPredicates` (abbreviation, [line 23](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/Basic.lean#L23))

> Builds a unimodal predicate model from a binary relation.

```lean
abbrev Model.unimodalOfPredicates (r : α → α → Prop) : Model α τ (α → Prop)
```

`Cslib.Logic.Modal.Model.unimodalOfContainers` (abbreviation, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/Basic.lean#L27))

> Builds a unimodal container model from a binary relation.

```lean
abbrev Model.unimodalOfContainers [Membership α β] (r : α → α → Prop) : Model α τ β
```

`Cslib.Logic.Modal.Satisfies.unimodalOfPredicates_preserves_iff` (theorem, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/Basic.lean#L34))

> Under `Model.unimodalOfPredicates r`, `P → □P` is an axiom iff `r` preserves `P`.

```lean
theorem Satisfies.unimodalOfPredicates_preserves_iff {P : α → Prop} (r : α → α → Prop) :
    (∀ a, ⇓Modal[Model.unimodalOfPredicates (τ := τ) r,a ⊨ P → □P]) ↔ Preserves r P
```

`Cslib.Logic.Modal.Satisfies.unimodalOfPredicates_preserves_reflTransGen` (theorem, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/Basic.lean#L50))

> Invariants are preserved by the reflexive and transitive closure of the accessibility relation.

```lean
theorem Satisfies.unimodalOfPredicates_preserves_reflTransGen
    {r : α → α → Prop} {P : α → Prop}
    (h : ∀ a, ⇓Modal[unimodalOfPredicates (τ := τ) r,a ⊨ P → □P]) :
    ∀ a, ⇓Modal[unimodalOfPredicates (τ := τ) (Relation.ReflTransGen r),a ⊨ P → □P]
```

## Depends on

- [Modal Logic for Lean](../../lean/basic.md)
- [Basic Modal Logic](../basic.md)

## Proof depends on

- [Relations: preservation of properties](../../../../foundations/relation/preserves.md)

## Sources

- [Cslib/Logics/Modal/Unimodal/Lean/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/Basic.lean)
