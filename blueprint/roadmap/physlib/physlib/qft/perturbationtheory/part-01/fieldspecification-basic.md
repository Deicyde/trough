---
declaration: module
origin: cited
lean: FieldSpecification, FieldSpecification.FieldOp, FieldSpecification.statesIsPosition, FieldSpecification.fieldOpToField, FieldSpecification.fieldOpStatistic
statement: formalized
proof: formalized
---

# Field specification

The module `Physlib.QFT.PerturbationTheory.FieldSpecification.Basic`, [Physlib/QFT/PerturbationTheory/FieldSpecification/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Basic.lean): 5 declarations, 5 with a docstring.

> In this module is the definition of a field specification.
> A field specification is a structure consisting of a type of fields and a
> the field statistics of each field.
>
> From each field we can create three different types of `FieldOp`.
> - Negative asymptotic states.
> - Position states.
> - Positive asymptotic states.
>
> These states carry the same field statistic as the field they are derived from.

## References

> * https://particle.physics.ucdavis.edu/modernsusy/slides/slideimages/spinorfeynrules.pdf.
>   [ref: ucdavis\_spinorfeynrules]

**`FieldSpecification`**, a structure, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Basic.lean#L59).

> The structure `FieldSpecification` is defined to have the following content:
>   - A type `Field` whose elements are the constituent fields of the theory.
>   - For every field `f` in `Field`, a type `PositionLabel f` whose elements label the different
>     position operators associated with the field `f`. For example,
>     - For `f` a *real-scalar field*, `PositionLabel f` will have a unique element.
>     - For `f` a *complex-scalar field*, `PositionLabel f` will have two elements, one for the field
>       operator and one for its conjugate.
>     - For `f` a *Dirac fermion*, `PositionLabel f` will have eight elements, one for each Lorentz
>       index of the field and its conjugate.
>     - For `f` a *Weyl fermion*, `PositionLabel f` will have four elements, one for each Lorentz
>       index of the field and its conjugate.
>   - For every field `f` in `Field`, a type `AsymptoticLabel f` whose elements label the different
>     types of incoming asymptotic field operators associated with the
>     field `f` (this also matches the types of outgoing asymptotic field operators).
>     For example,
>     - For `f` a *real-scalar field*, `AsymptoticLabel f` will have a unique element.
>     - For `f` a *complex-scalar field*, `AsymptoticLabel f` will have two elements, one for the
>       field operator and one for its conjugate.
>     - For `f` a *Dirac fermion*, `AsymptoticLabel f` will have four elements, two for each spin.
>     - For `f` a *Weyl fermion*, `AsymptoticLabel f` will have two elements, one for each spin.
>   - For each field `f` in `Field`, a field statistic `statistic f` which classifies `f` as either
>     `bosonic` or `fermionic`.

```lean
structure FieldSpecification where
  /-- A type whose elements are the constituent fields of the theory. -/
  Field : Type
  /-- For every field `f` in `Field`, the type `PositionLabel f` has elements that label the
    different position operators associated with the field `f`. -/
  PositionLabel : Field → Type
  /-- For every field `f` in `Field`, the type `AsymptoticLabel f` has elements that label
    the different asymptotic based field operators associated with the field `f`. -/
  AsymptoticLabel : Field → Type
  /-- For every field `f` in `Field`, the field statistic `statistic f` classifies `f` as either
    `bosonic` or `fermionic`. -/
  statistic : Field → FieldStatistic
```

**`FieldSpecification.FieldOp`**, an inductive, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Basic.lean#L101).

> For a field specification `𝓕`, the inductive type `𝓕.FieldOp` is defined
>   to contain the following elements:
> - For every `f` in `𝓕.Field`, element of `e` of `AsymptoticLabel f` and `3`-momentum `p`, an
>   element labelled `inAsymp f e p` corresponding to an incoming asymptotic field operator
>   of the field `f`, of label `e` (e.g. specifying the spin), and momentum `p`.
> - For every `f` in `𝓕.Field`, element of `e` of `PositionLabel f` and space-time position `x`, an
>   element labelled `position f e x` corresponding to a position field operator of the field `f`,
>   of label `e` (e.g. specifying the Lorentz index), and position `x`.
> - For every `f` in `𝓕.Field`, element of `e` of `AsymptoticLabel f` and `3`-momentum `p`, an
>   element labelled `outAsymp f e p` corresponding to an outgoing asymptotic field operator of the
>   field `f`, of label `e` (e.g. specifying the spin), and momentum `p`.
>
> As an example, if `f` corresponds to a Weyl-fermion field, then
> - For `inAsymp f e p`, `e` would correspond to a spin `s`, and `inAsymp f e p` would, once
>   represented in the operator algebra,
>   be proportional to the creation operator `a(p, s)`.
> - `position f e x`, `e` would correspond to a Lorentz index `a`, and `position f e x` would,
>   once represented in the operator algebra, be proportional to the operator
>
>   `∑ s, ∫ d³p/(…) (xₐ(p,s) a(p, s) e ^ (-i p x) + yₐ(p,s) a†(p, s) e ^ (-i p x))`.
>
> - `outAsymp f e p`, `e` would correspond to a spin `s`, and `outAsymp f e p` would,
>   once represented in the operator algebra, be proportional to the
>   annihilation operator `a†(p, s)`.

```lean
inductive FieldOp (𝓕 : FieldSpecification) where
  | inAsymp : (Σ f, 𝓕.AsymptoticLabel f) × (Momentum 3) → 𝓕.FieldOp
  | position : (Σ f, 𝓕.PositionLabel f) × SpaceTime → 𝓕.FieldOp
  | outAsymp : (Σ f, 𝓕.AsymptoticLabel f) × (Momentum 3) → 𝓕.FieldOp
```

**`FieldSpecification.statesIsPosition`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Basic.lean#L107).

> The bool on `FieldOp` which is true only for position field operator.

```lean
def statesIsPosition : 𝓕.FieldOp → Bool
```

**`FieldSpecification.fieldOpToField`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Basic.lean#L113).

> For a field specification `𝓕`, `𝓕.fieldOpToField` is defined to take field operators
> to their underlying field.

```lean
def fieldOpToField : 𝓕.FieldOp → 𝓕.Field
```

**`FieldSpecification.fieldOpStatistic`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Basic.lean#L128).

> For a field specification `𝓕`, and an element `φ` of `𝓕.FieldOp`.
>   The field statistic `fieldOpStatistic φ` is defined to be the statistic associated with
>   the field underlying `φ`.
>
>   The following notation is used in relation to `fieldOpStatistic`:
> - For `φ` an element of `𝓕.FieldOp`, `𝓕 |>ₛ φ` is `fieldOpStatistic φ`.
> - For `φs` a list of `𝓕.FieldOp`, `𝓕 |>ₛ φs` is the product of `fieldOpStatistic φ` over
>   the list `φs`.
> - For a function `f : Fin n → 𝓕.FieldOp` and a finite set `a` of `Fin n`, `𝓕 |>ₛ ⟨f, a⟩` is the
>   product of `fieldOpStatistic (f i)` for all `i ∈ a`.

```lean
def fieldOpStatistic : 𝓕.FieldOp → FieldStatistic
```

## Depends on

- [Field statistics](fieldstatistics-basic.md)
- [Spacetime](../../../spaceandtime/spacetime/basic.md)
- [Momentum](../../../units/withdim/momentum.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldSpecification/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/Basic.lean)
