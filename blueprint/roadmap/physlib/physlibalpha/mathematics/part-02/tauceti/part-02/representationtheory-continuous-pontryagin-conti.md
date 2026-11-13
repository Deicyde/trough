---
declaration: module
origin: cited
lean: ContRepresentation.integratedCharacterSet, ContRepresentation.mem_integratedCharacterSet_iff, ContRepresentation.isOpen_integratedCharacterSet, ContRepresentation.integratedCharacterToPontryaginDual, ContRepresentation.integratedCharacterToPontryaginDual_spec, ContRepresentation.coe_integratedCharacterToPontryaginDual_apply_eq_div, ContRepresentation.continuous_integratedCharacterToPontryaginDual
statement: formalized
proof: formalized
---

# Continuity of the integrated-character parameter

The module `PhyslibAlpha.Mathematics.TauCeti.RepresentationTheory.Continuous.Pontryagin.Continuity`, [PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Continuity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Continuity.lean): 7 declarations, 7 with a docstring.

> Let `π` be a strongly continuous unitary representation of an abelian topological group equipped
> with a regular invariant measure, and let `A` be a complete star subalgebra containing all
> integrated operators.

## i. Overview

> Let `π` be a strongly continuous unitary representation of an abelian topological group equipped
> with a regular invariant measure, and let `A` be a complete star subalgebra containing all
> integrated operators.
> A character of `A` that is nonzero on some integrated operator determines a continuous group
> character by `ContRepresentation.existsUnique_pontryaginDual_of_integratedOperatorL1`.
>
> This file packages the characters on which that construction is defined and proves that the
> resulting map to the Pontryagin dual is continuous.  Near a character `ω`, choose an integrated
> operator `π(f)` on which `ω` is nonzero.  The detected group character then has the local formula
>
> `χ(g) = ω(π(g)π(f)) / ω(π(f))`.
>
> The numerator is jointly continuous in `ω` and `g`: norm continuity of translated integrated
> operators combines with weak-* continuity of evaluation and the uniform norm bound on characters
> of a Banach algebra.  The denominator remains nonzero in a neighbourhood of `ω`, so the displayed
> quotient proves the required local continuity.  This continuity is the input needed to push a
> character-space spectral measure to the Pontryagin dual.

## ii. Key results

> * `ContRepresentation.integratedCharacterSet`: algebra characters that do not annihilate every
>   integrated operator.
> * `ContRepresentation.integratedCharacterToPontryaginDual`: the group character detected by an
>   integrated-algebra character.
> * `ContRepresentation.continuous_integratedCharacterToPontryaginDual`: continuity of this
>   assignment.

## iv. References

> * G. B. Folland, *A Course in Abstract Harmonic Analysis*, second edition, §§3.2 and 4.4.
> * The local-quotient continuity proof generalizes Tau Ceti's earlier formalization in
>   `TauCeti.StronglyContinuousSpectral.continuousOn_dual`
>   (`TauCeti.Analysis.Fourier.Pontryagin.StronglyContinuous`), which was stated for the
>   integrated algebra of a unitary representation with respect to a Haar measure.

## A. Development

**`ContRepresentation.integratedCharacterSet`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Continuity.lean#L85).

> The characters of an algebra containing the integrated form which do not annihilate every
> integrated operator.  When `π` is unitary, these are exactly the algebra characters from which
> the representation detects a point of the Pontryagin dual.

```lean
def integratedCharacterSet : Set (characterSpace ℂ A)
```

**`ContRepresentation.mem_integratedCharacterSet_iff`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Continuity.lean#L91).

> Membership in the integrated-character set means nonvanishing on some integrated operator.

```lean
lemma mem_integratedCharacterSet_iff (ω : characterSpace ℂ A) :
    ω ∈ π.integratedCharacterSet hcont hbdd A hA ↔
      ∃ f : G →₁[μ] ℂ, ω ⟨π.integratedOperatorL1 hcont hbdd μ f, hA f⟩ ≠ 0
```

**`ContRepresentation.isOpen_integratedCharacterSet`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Continuity.lean#L98).

> The integrated-character set is open in the character space.

```lean
lemma isOpen_integratedCharacterSet :
    IsOpen (π.integratedCharacterSet hcont hbdd A hA)
```

**`ContRepresentation.integratedCharacterToPontryaginDual`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Continuity.lean#L112).

> The continuous group character detected by an algebra character that does not annihilate the
> integrated form.

```lean
noncomputable def integratedCharacterToPontryaginDual
    (ω : π.integratedCharacterSet hcont hbdd A hA) : PontryaginDual (Multiplicative G)
```

**`ContRepresentation.integratedCharacterToPontryaginDual_spec`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Continuity.lean#L120).

> The defining multiplier identity for the group character detected by an integrated
> character.

```lean
lemma integratedCharacterToPontryaginDual_spec
    (ω : π.integratedCharacterSet hcont hbdd A hA) (g : G) (f : G →₁[μ] ℂ) :
    ω.1
        ⟨π.integratedOperatorL1 hcont hbdd μ
          (Lp.compMeasurePreserving (fun t => -g + t)
            (measurePreserving_add_left μ (-g)) f), hA _⟩ =
      (π.integratedCharacterToPontryaginDual hcont hbdd A hA hπ ω (.ofAdd g) : ℂ) *
        ω.1 ⟨π.integratedOperatorL1 hcont hbdd μ f, hA f⟩
```

**`ContRepresentation.coe_integratedCharacterToPontryaginDual_apply_eq_div`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Continuity.lean#L133).

> Local quotient formula for the group character detected by an integrated character.

```lean
lemma coe_integratedCharacterToPontryaginDual_apply_eq_div
    (ω : π.integratedCharacterSet hcont hbdd A hA) (g : G) (f : G →₁[μ] ℂ)
    (hf : ω.1 ⟨π.integratedOperatorL1 hcont hbdd μ f, hA f⟩ ≠ 0) :
    (π.integratedCharacterToPontryaginDual hcont hbdd A hA hπ ω (.ofAdd g) : ℂ) =
      ω.1 ⟨π.integratedOperatorL1 hcont hbdd μ
        (Lp.compMeasurePreserving (fun t => -g + t)
          (measurePreserving_add_left μ (-g)) f), hA _⟩ /
        ω.1 ⟨π.integratedOperatorL1 hcont hbdd μ f, hA f⟩
```

**`ContRepresentation.continuous_integratedCharacterToPontryaginDual`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Continuity.lean#L146).

> The group character detected by a nonvanishing integrated character depends continuously on
> the algebra character.

```lean
lemma continuous_integratedCharacterToPontryaginDual :
    Continuous (π.integratedCharacterToPontryaginDual hcont hbdd A hA hπ)
```

## Depends on

- [The integrated form of a strongly continuous representation](representationtheory-continuous-integrated-basic.md)

## Proof depends on

- [Group characters detected by integrated operators](representationtheory-continuous-pontryagin-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Continuity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Continuity.lean)
