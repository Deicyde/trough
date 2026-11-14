---
declaration: module
origin: cited
lean: FieldSpecification.createFilter, FieldSpecification.createFilter_cons_create, FieldSpecification.createFilter_cons_annihilate, FieldSpecification.createFilter_append, FieldSpecification.createFilter_singleton_create, FieldSpecification.createFilter_singleton_annihilate, FieldSpecification.annihilateFilter, FieldSpecification.annihilateFilter_cons_create
statement: formalized
proof: formalized
---

# Filters of lists of CrAnFieldOp

The module `Physlib.QFT.PerturbationTheory.FieldSpecification.Filters`, [Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean): 12 declarations, 2 with a docstring.

**`FieldSpecification.createFilter`**, a def, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean#L24).

> Given a list of creation and annihilation states, the filtered list only containing
> the creation states. As a schematic example, for the list:
> - `[φ1c, φ1a, φ2c, φ2a]` this will return `[φ1c, φ2c]`.

```lean
def createFilter (φs : List 𝓕.CrAnFieldOp) : List 𝓕.CrAnFieldOp
```

**`FieldSpecification.createFilter_cons_create`**, a lemma, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean#L27).

```lean
lemma createFilter_cons_create {φ : 𝓕.CrAnFieldOp}
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.create) (φs : List 𝓕.CrAnFieldOp) :
    createFilter (φ :: φs) = φ :: createFilter φs
```

**`FieldSpecification.createFilter_cons_annihilate`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean#L34).

```lean
lemma createFilter_cons_annihilate {φ : 𝓕.CrAnFieldOp}
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.annihilate) (φs : List 𝓕.CrAnFieldOp) :
    createFilter (φ :: φs) = createFilter φs
```

**`FieldSpecification.createFilter_append`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean#L41).

```lean
lemma createFilter_append (φs φs' : List 𝓕.CrAnFieldOp) :
    createFilter (φs ++ φs') = createFilter φs ++ createFilter φs'
```

**`FieldSpecification.createFilter_singleton_create`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean#L46).

```lean
lemma createFilter_singleton_create (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.create) :
    createFilter [φ] = [φ]
```

**`FieldSpecification.createFilter_singleton_annihilate`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean#L51).

```lean
lemma createFilter_singleton_annihilate (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.annihilate) : createFilter [φ] = []
```

**`FieldSpecification.annihilateFilter`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean#L60).

> Given a list of creation and annihilation states, the filtered list only containing
> the annihilation states.
> As a schematic example, for the list:
> - `[φ1c, φ1a, φ2c, φ2a]` this will return `[φ1a, φ2a]`.

```lean
def annihilateFilter (φs : List 𝓕.CrAnFieldOp) : List 𝓕.CrAnFieldOp
```

**`FieldSpecification.annihilateFilter_cons_create`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean#L63).

```lean
lemma annihilateFilter_cons_create {φ : 𝓕.CrAnFieldOp}
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.create) (φs : List 𝓕.CrAnFieldOp) :
    annihilateFilter (φ :: φs) = annihilateFilter φs
```

**`FieldSpecification.annihilateFilter_cons_annihilate`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean#L70).

```lean
lemma annihilateFilter_cons_annihilate {φ : 𝓕.CrAnFieldOp}
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.annihilate) (φs : List 𝓕.CrAnFieldOp) :
    annihilateFilter (φ :: φs) = φ :: annihilateFilter φs
```

**`FieldSpecification.annihilateFilter_append`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean#L77).

```lean
lemma annihilateFilter_append (φs φs' : List 𝓕.CrAnFieldOp) :
    annihilateFilter (φs ++ φs') = annihilateFilter φs ++ annihilateFilter φs'
```

**`FieldSpecification.annihilateFilter_singleton_create`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean#L82).

```lean
lemma annihilateFilter_singleton_create (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.create) :
    annihilateFilter [φ] = []
```

**`FieldSpecification.annihilateFilter_singleton_annihilate`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean#L87).

```lean
lemma annihilateFilter_singleton_annihilate (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.annihilate) :
    annihilateFilter [φ] = [φ]
```

## Depends on

- [Creation and annihilation states](fieldspecification-cranfieldop.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Filters.lean)
