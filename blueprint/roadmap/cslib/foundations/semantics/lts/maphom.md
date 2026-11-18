---
catalog: module
lean: Cslib.LTS.mapHom, Cslib.LTS.mapHom_tr, Cslib.LTS.mapHom_mTr, Cslib.LTS.mapLabel, Cslib.LTS.mapLabel_tr, Cslib.LTS.mapLabel_mTr
statement: formalized
proof: formalized
---

# Label homomorphism map for LTS

`Cslib.Foundations.Semantics.LTS.MapHom`, in [Cslib/Foundations/Semantics/LTS/MapHom.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/MapHom.lean), by Fabrizio Montesi, Ching-Tsun Chou.

`Cslib.LTS.mapHom` (definition, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/MapHom.lean#L32))

> Given a language homomorphism `f` from `Label₂` to `Label₁` and an LTS `lts` that
> uses `Label₁`, `lts.mapHom f` is an LTS with the same state space but uses `Label₂`, whose
> step on a single label `μ` is the composition of the steps taken by `lts` on the sequence of
> labels `f [μ]`.  Note that `f [μ]` can be empty or consists of many labels.

```lean
def mapHom (lts : LTS State Label₁) (f : Hom Label₂ Label₁) : LTS State Label₂
```

`Cslib.LTS.mapHom_tr` (theorem, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/MapHom.lean#L38))

```lean
theorem mapHom_tr {lts : LTS State Label₁} {μ : Label₂} :
    (lts.mapHom f).Tr s μ s' ↔ lts.MTr s (f [μ]) s'
```

`Cslib.LTS.mapHom_mTr` (theorem, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/MapHom.lean#L44))

> This theorem says basically that `lts.mapHom f` is well-defined because `f` is
> a language homomorphism.

```lean
theorem mapHom_mTr {lts : LTS State Label₁} {μs : List Label₂} :
    (lts.mapHom f).MTr s μs s' ↔ lts.MTr s (f μs) s'
```

`Cslib.LTS.mapLabel` (definition, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/MapHom.lean#L58))

> This is the special case of `LTS.mapHom` when the language homomorphism maps
> single labels to single labels.

```lean
def mapLabel (lts : LTS State Label₁) (f : Label₂ → Label₁) : LTS State Label₂
```

`Cslib.LTS.mapLabel_tr` (theorem, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/MapHom.lean#L62))

```lean
theorem mapLabel_tr {lts : LTS State Label₁} :
    (lts.mapLabel f).Tr s μ s' ↔ lts.Tr s (f μ) s'
```

`Cslib.LTS.mapLabel_mTr` (theorem, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/MapHom.lean#L69))

```lean
theorem mapLabel_mTr {lts : LTS State Label₁} {f : Label₂ → Label₁} :
    (lts.mapLabel f).MTr s μs s' ↔ lts.MTr s (μs.map f) s'
```

## Depends on

- [Language homomorphism](../../../computability/languages/languagehom.md)
- [Labelled Transition System (LTS)](basic.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/MapHom.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/MapHom.lean)
