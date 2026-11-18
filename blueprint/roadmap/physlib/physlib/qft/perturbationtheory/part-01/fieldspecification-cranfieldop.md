---
declaration: module
origin: cited
lean: FieldSpecification.fieldOpToCrAnType, FieldSpecification.fieldOpToCreateAnnihilateTypeCongr, FieldSpecification.CrAnFieldOp, FieldSpecification.crAnFieldOpToFieldOp, FieldSpecification.crAnFieldOpToFieldOp_prod, FieldSpecification.crAnFieldOpToCreateAnnihilate, FieldSpecification.crAnStatistics
statement: formalized
proof: formalized
---

# Creation and annihilation states

The module `Physlib.QFT.PerturbationTheory.FieldSpecification.CrAnFieldOp`, [Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean): 9 declarations (2 instances with no name), 8 with a docstring.

> Called `CrAnFieldOp` for short here.
>
> Given a field specification, in addition to defining states
> (see: `Physlib.QFT.PerturbationTheory.FieldSpecification.Basic`),
> we can also define creation and annihilation states.
> These are similar to states but come with an additional specification of whether they correspond to
> creation or annihilation operators.
>
> In particular we have the following creation and annihilation states for each field:
> - Negative asymptotic states - with the implicit specification that it is a creation state.
> - Position states with a creation specification.
> - Position states with an annihilation specification.
> - Positive asymptotic states - with the implicit specification that it is an annihilation state.
>
> In this module in addition to defining `CrAnFieldOp` we also define some maps:
> - The map `crAnFieldOpToFieldOp` takes a `CrAnFieldOp` to its state in `FieldOp`.
> - The map `crAnFieldOpToCreateAnnihilate` takes a `CrAnFieldOp` to its corresponding
> `CreateAnnihilate` value.
> - The map `crAnStatistics` takes a `CrAnFieldOp` to its corresponding `FieldStatistic`
> (bosonic or fermionic).

**`FieldSpecification.fieldOpToCrAnType`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean#L44).

> To each field operator the specification of the type of creation and annihilation parts.
> For asymptotic states there is only one allowed part, whilst for position
> field operator there is two.

```lean
def fieldOpToCrAnType : 𝓕.FieldOp → Type
```

**An instance with no name**, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean#L50).

> The instance of a finite type on `𝓕.fieldOpToCreateAnnihilateType i`.

```lean
instance : ∀ i, Fintype (𝓕.fieldOpToCrAnType i)
```

**An instance with no name**, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean#L57).

> The instance of a decidable equality on `𝓕.fieldOpToCreateAnnihilateType i`.

```lean
instance : ∀ i, DecidableEq (𝓕.fieldOpToCrAnType i)
```

**`FieldSpecification.fieldOpToCreateAnnihilateTypeCongr`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean#L65).

> The equivalence between `𝓕.fieldOpToCreateAnnihilateType i` and
> `𝓕.fieldOpToCreateAnnihilateType j` from an equality `i = j`.

```lean
def fieldOpToCreateAnnihilateTypeCongr : {i j : 𝓕.FieldOp} → i = j →
    𝓕.fieldOpToCrAnType i ≃ 𝓕.fieldOpToCrAnType j
```

**`FieldSpecification.CrAnFieldOp`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean#L98).

> For a field specification `𝓕`, the (sigma) type `𝓕.CrAnFieldOp`
> corresponds to the type of creation and annihilation parts of field operators.
> It formally defined to consist of the following elements:
> - For each incoming asymptotic field operator `φ` in `𝓕.FieldOp` an element
>   written as `⟨φ, ()⟩` in `𝓕.CrAnFieldOp`, corresponding to the creation part of `φ`.
>   Here `φ` has no annihilation part. (Here `()` is the unique element of `Unit`.)
> - For each position field operator `φ` in `𝓕.FieldOp` an element of `𝓕.CrAnFieldOp`
>   written as `⟨φ, .create⟩`, corresponding to the creation part of `φ`.
> - For each position field operator `φ` in `𝓕.FieldOp` an element of `𝓕.CrAnFieldOp`
>   written as `⟨φ, .annihilate⟩`, corresponding to the annihilation part of `φ`.
> - For each outgoing asymptotic field operator `φ` in `𝓕.FieldOp` an element
>   written as `⟨φ, ()⟩` in `𝓕.CrAnFieldOp`, corresponding to the annihilation part of `φ`.
>   Here `φ` has no creation part. (Here `()` is the unique element of `Unit`.)
>
> As an example, if `f` corresponds to a Weyl-fermion field, it would contribute
>   the following elements to `𝓕.CrAnFieldOp`
> - For each spin `s`, an element corresponding to an incoming asymptotic operator: `a(p, s)`.
> - For each each Lorentz
>   index `a`, an element corresponding to the creation part of a position operator:
>
>   `∑ s, ∫ d³p/(…) (xₐ (p,s) a(p, s) e ^ (-i p x))`.
> - For each each Lorentz
>   index `a`,an element corresponding to annihilation part of a position operator:
>
>   `∑ s, ∫ d³p/(…) (yₐ(p,s) a†(p, s) e ^ (-i p x))`.
> - For each spin `s`, element corresponding to an outgoing asymptotic operator: `a†(p, s)`.

```lean
def CrAnFieldOp : Type
```

**`FieldSpecification.crAnFieldOpToFieldOp`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean#L101).

> The map from creation and annihilation field operator to their underlying states.

```lean
def crAnFieldOpToFieldOp : 𝓕.CrAnFieldOp → 𝓕.FieldOp
```

**`FieldSpecification.crAnFieldOpToFieldOp_prod`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean#L104).

```lean
lemma crAnFieldOpToFieldOp_prod (s : 𝓕.FieldOp) (t : 𝓕.fieldOpToCrAnType s) :
    𝓕.crAnFieldOpToFieldOp ⟨s, t⟩ = s
```

**`FieldSpecification.crAnFieldOpToCreateAnnihilate`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean#L114).

> For a field specification `𝓕`, `𝓕.crAnFieldOpToCreateAnnihilate` is the map from
>   `𝓕.CrAnFieldOp` to `CreateAnnihilate` taking `φ` to `create` if
> - `φ` corresponds to an incoming asymptotic field operator or the creation part of a position based
>   field operator.
>
> otherwise it takes `φ` to `annihilate`.

```lean
def crAnFieldOpToCreateAnnihilate : 𝓕.CrAnFieldOp → CreateAnnihilate
```

**`FieldSpecification.crAnStatistics`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean#L129).

> For a field specification `𝓕`, and an element `φ` in `𝓕.CrAnFieldOp`, the field
> statistic `crAnStatistics φ` is defined to be the statistic associated with the field `𝓕.Field`
> (or the `𝓕.FieldOp`) underlying `φ`.
>
> The following notation is used in relation to `crAnStatistics`:
> - For `φ` an element of `𝓕.CrAnFieldOp`, `𝓕 |>ₛ φ` is `crAnStatistics φ`.
> - For `φs` a list of `𝓕.CrAnFieldOp`, `𝓕 |>ₛ φs` is the product of `crAnStatistics φ` over
>   the list `φs`.

```lean
def crAnStatistics : 𝓕.CrAnFieldOp → FieldStatistic
```

## Depends on

- [Creation and annihilation parts of fields](createannihilate.md)
- [Field specification](fieldspecification-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnFieldOp.lean)
