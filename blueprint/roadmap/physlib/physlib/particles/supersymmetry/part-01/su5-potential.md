---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.PotentialTerm, SuperSymmetry.SU5.PotentialTerm.toFieldLabel, SuperSymmetry.SU5.PotentialTerm.InSuperPotential, SuperSymmetry.SU5.PotentialTerm.no_conjugate_in_toFieldLabel_of_inSuperPotential, SuperSymmetry.SU5.PotentialTerm.degree, SuperSymmetry.SU5.PotentialTerm.degree_le_four, SuperSymmetry.SU5.PotentialTerm.RParity, SuperSymmetry.SU5.PotentialTerm.violates_RParity_iff_mem
statement: formalized
proof: formalized
---

# Potential of the SU(5) + U(1) GUT

The module `Physlib.Particles.SuperSymmetry.SU5.Potential`, [Physlib/Particles/SuperSymmetry/SU5/Potential.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/Potential.lean): 10 declarations (1 instance with no name), 7 with a docstring.

## i. Overview

> In this module we will write down some of the potential terms appearing in
> an `SU(5)` SUSY GUT model, with matter in the 5-bar and 10d representations.
>
> A future iteration of this file will include all terms,
> and derive them from symmetry properties.
>
> The terms of the super-potential we will consider are:
> `W ⊃ μ 5Hu 5̄Hd + 𝛽ᵢ 5̄Mⁱ5Hu + 𝜆ᵢⱼₖ 5̄Mⁱ 5̄Mʲ 10ᵏ + W¹ᵢⱼₖₗ 10ⁱ 10ʲ 10ᵏ 5̄Mˡ`
> `+ W²ᵢⱼₖ 10ⁱ 10ʲ 10ᵏ 5̄Hd + W³ᵢⱼ 5̄Mⁱ 5̄Mʲ 5Hu 5Hu + W⁴ᵢ 5̄Mⁱ 5̄Hd 5Hu 5Hu`
>
> The terms of the Kahler potential are:
> `K ⊃ K¹ᵢⱼₖ 10ⁱ 10ʲ 5Mᵏ + K²ᵢ 5̄Hu 5̄Hd 10ⁱ`

## ii. Key results

> - `PotentialTerm` : The inductive type indexing the potential terms.
> - `violateRParity` : The finite set of terms which violate R-parity.
>   `β`, `λ`, `W²`, `W⁴`, `K¹`, `K²`
> - `causeProtonDecay` : The finite set of terms which contribute to proton decay.
>   `W¹`, `W²`, `K¹`, `λ`

## iv. References

> * The main reference for the terms, and notation used in this module is: arXiv:0912.0853 A previous
>   version of this code was replaced in PR#569. [ref: arxiv\_0912\_0853]

## A. The definition of `PotentialTerm`

> We define an inductive type with a term for each of the potential terms we are interested in,
> present in both the super-potential and Kahler potential.

**`SuperSymmetry.SU5.PotentialTerm`**, an inductive, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/Potential.lean#L70).

> Relevant terms part of the superpotential and Kahler potential of the `SU(5)` SUSY GUT.

```lean
inductive PotentialTerm
  /-- The term `μ 5Hu 5̄Hd` appearing in the super-potential. -/
  | μ : PotentialTerm
  /-- The term `𝛽ᵢ 5̄Mⁱ5Hu` appearing in the super-potential. -/
  | β : PotentialTerm
  /-- The term `𝜆ᵢⱼₖ 5̄Mⁱ 5̄Mʲ 10ᵏ` appearing in the super-potential. -/
  | Λ : PotentialTerm
  /-- The term `W¹ᵢⱼₖₗ 10ⁱ 10ʲ 10ᵏ 5̄Mˡ` appearing in the super-potential. -/
  | W1 : PotentialTerm
  /-- The term `W²ᵢⱼₖ 10ⁱ 10ʲ 10ᵏ 5̄Hd` appearing in the super-potential. -/
  | W2 : PotentialTerm
  /-- The term `W³ᵢⱼ 5̄Mⁱ 5̄Mʲ 5Hu 5Hu` appearing in the super-potential. -/
  | W3 : PotentialTerm
  /-- The term `W⁴ᵢ 5̄Mⁱ 5̄Hd 5Hu 5Hu` appearing in the super-potential. -/
  | W4 : PotentialTerm
  /-- The term `K¹ᵢⱼₖ 10ⁱ 10ʲ 5Mᵏ` appearing in the Kahler potential. -/
  | K1 : PotentialTerm
  /-- The term `K²ᵢ 5̄Hu 5̄Hd 10ⁱ` appearing in the Kahler potential. -/
  | K2 : PotentialTerm
  /-- The term `λᵗᵢⱼ 10ⁱ 10ʲ 5Hu` appearing in the super-potential. -/
  | topYukawa : PotentialTerm
  /-- The term `λᵇᵢⱼ 10ⁱ 5̄Mʲ 5̄Hd` appearing in the super-potential. -/
  | bottomYukawa : PotentialTerm
```

## B. Relation to field labels

> We map each term in the potential to the list of `FieldLabel`s which it contains.
> This allows us to define various properties of the potential term in a safe way, based
> solely on the field content.

**`SuperSymmetry.SU5.PotentialTerm.toFieldLabel`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/Potential.lean#L108).

> The fields contained within a given term of the potential.

```lean
def toFieldLabel : PotentialTerm → List FieldLabel
```

## C. Presence in the super-potential

> We define a predicate which is true on those terms which are members of the super-potential.
> We will also prove that this predicate is decidable.

**`SuperSymmetry.SU5.PotentialTerm.InSuperPotential`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/Potential.lean#L132).

> The proposition which is true on those terms which are members of the
> super potential.

```lean
def InSuperPotential : PotentialTerm → Prop
```

**An instance with no name**, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/Potential.lean#L145).

```lean
instance : (T : PotentialTerm) → Decidable (InSuperPotential T)
```

### C.1. In super potential implies no conjugate fields

> Been in the super potential implies that the term contains no conjugate fields.

**`SuperSymmetry.SU5.PotentialTerm.no_conjugate_in_toFieldLabel_of_inSuperPotential`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/Potential.lean#L167).

> The terms within the super-potential contain no conjugate fields.

```lean
lemma no_conjugate_in_toFieldLabel_of_inSuperPotential {T : PotentialTerm}
    (h : T.InSuperPotential) : FieldLabel.fiveMatter ∉ T.toFieldLabel ∧
    FieldLabel.fiveHd ∉ T.toFieldLabel ∧ FieldLabel.fiveBarHu ∉ T.toFieldLabel
```

## D. Degree of the potential term

> We define the degree of a term in the potential to be the number of fields it contains.
> The degree of all terms present is less than or equal to four.

**`SuperSymmetry.SU5.PotentialTerm.degree`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/Potential.lean#L183).

> The degree of a term in the potential.

```lean
def degree (T : PotentialTerm) : ℕ
```

**`SuperSymmetry.SU5.PotentialTerm.degree_le_four`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/Potential.lean#L185).

```lean
lemma degree_le_four (T : PotentialTerm) : T.degree ≤ 4
```

## E. R-parity of the potential terms

> Based on the R-parity of the underlying fields, we define the R-parity of each term
> in the potential. We show that those terms which violate R-parity are exactly those
> which are `β`, `Λ`, `W2`, `W4`, `K1`, or `K2`.

**`SuperSymmetry.SU5.PotentialTerm.RParity`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/Potential.lean#L199).

> The R-parity of a term in the potential.

```lean
def RParity (T : PotentialTerm) : Fin 2
```

**`SuperSymmetry.SU5.PotentialTerm.violates_RParity_iff_mem`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/Potential.lean#L203).

```lean
lemma violates_RParity_iff_mem {T : PotentialTerm} :
    T.RParity = 1 ↔ T ∈ ({β, Λ, W2, W4, K1, K2} : Finset PotentialTerm)
```

## F. Terms which violate proton decay

> We write down the finite set of terms which contribute to proton decay.
> We do not at this point prove this result.

**`SuperSymmetry.SU5.PotentialTerm.causeProtonDecay`**, a def, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/Potential.lean#L224).

> The finite set of terms in the superpotential and Kahler potential which are involved in
>   proton decay.
> - `W¹ᵢⱼₖₗ 10ⁱ 10ʲ 10ᵏ 5̄Mˡ`
> - `𝜆ᵢⱼₖ 5̄Mⁱ 5̄Mʲ 10ᵏ`
> - `W²ᵢⱼₖ 10ⁱ 10ʲ 10ᵏ 5̄Hd`
> - `K¹ᵢⱼₖ 10ⁱ 10ʲ 5Mᵏ`

```lean
def causeProtonDecay : Finset PotentialTerm
```

## Depends on

- [The field labels](su5-fieldlabels.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/Potential.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/Potential.lean)
