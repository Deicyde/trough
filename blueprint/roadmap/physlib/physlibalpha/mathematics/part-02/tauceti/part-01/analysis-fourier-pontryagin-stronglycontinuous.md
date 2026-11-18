---
declaration: module
origin: cited
lean: ContRepresentation.exists_pontryaginMeasureTransform_eq_inner
statement: formalized
proof: formalized
---

# Matrix coefficients of strongly continuous unitary representations

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.Fourier.Pontryagin.StronglyContinuous`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/StronglyContinuous.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/StronglyContinuous.lean): 1 declaration, 1 with a docstring; 16 private, not shown.

> Let `π` be a strongly continuous unitary representation of a locally compact abelian group `G` on a
> complex Hilbert space `H`, and let `ξ ∈ H`.

## i. Overview

> Let `π` be a strongly continuous unitary representation of a locally compact abelian group `G`
> on a complex Hilbert space `H`, and let `ξ ∈ H`. The
> diagonal matrix coefficient `g ↦ ⟪ξ, π(g) ξ⟫` is the Fourier–Stieltjes transform of a finite
> inner regular positive measure on the Pontryagin dual of `G`. This is the cyclic form of the
> Stone–Naimark–Ambrose–Godement spectral theorem.
>
> The operators `π(g)` are only strongly continuous, so the spectral measure is built from the
> integrated operators `π(f)`, `f ∈ L¹(G)`, taken with respect to a Haar measure. They generate a
> unital commutative C⋆-algebra `A`, and the vector functional `a ↦ ⟪ξ, a ξ⟫` is integration
> against a finite measure `ν` on the character space of `A`. A character `ω` that does not vanish
> on every integrated operator determines a continuous group character `χ_ω` with
> `ω(π(g) π(f)) = χ_ω(g) ω(π(f))`; this assignment is continuous on the open set of such
> characters, and the image of `ν` under it is the required measure. The characters annihilating
> every integrated operator do not contribute: since `π(f) ξ` approximates `ξ`, the identity
> `∫ |ω(π(f)) - 1|² dν = ‖π(f) ξ - ξ‖²` forces their measure to be zero.
> Compact approximation inside the open set of non-annihilating characters then proves that the
> pushforward measure is inner regular.
>
> No second countability of `G` and no separability of `H` is needed: the integrated form is defined
> for the Haar measure through its inner regularity for compact sets.

## ii. Key results

> * `ContRepresentation.exists_pontryaginMeasureTransform_eq_inner`: a diagonal matrix coefficient
>   of a strongly continuous unitary representation of a locally compact abelian group is the
>   Fourier–Stieltjes transform of a finite inner regular measure on the dual group.

## iv. References

> * G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press (2016), §§3.2,
>   4.4 and Theorem 4.44.

## A. Development

**`ContRepresentation.exists_pontryaginMeasureTransform_eq_inner`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/StronglyContinuous.lean#L295).

> **Spectral theorem for strongly continuous unitary representations**, cyclic form. For a
> strongly continuous unitary representation `π` of a locally compact abelian group `G` on a
> Hilbert space `H` and a vector `ξ`, the matrix coefficient `g ↦ ⟪ξ, π(g) ξ⟫` is the
> Fourier–Stieltjes transform of a finite inner regular measure on the Pontryagin dual of `G`.

```lean
lemma ContRepresentation.exists_pontryaginMeasureTransform_eq_inner
    (π : ContRepresentation ℂ (Multiplicative G) H)
    (hcont : ∀ v, Continuous fun g : G ↦ π (.ofAdd g) v)
    (hπ : ContRepresentation.IsUnitary π) (ξ : H) :
    ∃ μ : FiniteMeasure (PontryaginDual (Multiplicative G)),
      μ.toMeasure.InnerRegular ∧ ∀ g, μ.pontryaginMeasureTransform g = ⟪ξ, π (.ofAdd g) ξ⟫_ℂ
```

## Depends on

- [Fourier–Stieltjes transform of measures on a Pontryagin dual](analysis-fourier-pontryagin-measure.md)
- [Unitary continuous representations](../part-02/representationtheory-continuous-unitary-basic.md)

## Proof depends on

- [Positive functionals on commutative C⋆-algebras are measures on the character space](analysis-cstaralgebra-characterspacemeasure.md)
- [Inner regularity under almost everywhere continuous maps](../part-02/measuretheory-measure-regular.md)
- [The algebra of an integrated representation](../part-02/representationtheory-continuous-integrated-algeb.md)
- [Continuity of the integrated-character parameter](../part-02/representationtheory-continuous-pontryagin-conti.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/StronglyContinuous.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/StronglyContinuous.lean)
