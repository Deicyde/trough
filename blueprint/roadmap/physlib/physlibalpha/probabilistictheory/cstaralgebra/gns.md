---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.GNS, ProbabilisticTheory.UnitalPositiveLinearMap.gnsRep, ProbabilisticTheory.UnitalPositiveLinearMap.gnsCyclicVector, ProbabilisticTheory.UnitalPositiveLinearMap.gnsRep_gnsCyclicVector, ProbabilisticTheory.UnitalPositiveLinearMap.norm_gnsCyclicVector, ProbabilisticTheory.UnitalPositiveLinearMap.inner_gnsCyclicVector_gnsRep_gnsCyclicVector, ProbabilisticTheory.UnitalPositiveLinearMap.denseRange_gnsRep_gnsCyclicVector, ProbabilisticTheory.UnitalPositiveLinearMap.IsFaithful
statement: formalized
proof: formalized
---

# The GNS construction

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.GNS`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean): 9 declarations, 9 with a docstring.

> Every state on a C⋆-algebra is the vector state of a cyclic unit vector in its GNS representation.

## i. Overview

> Every state `ω` on a C⋆-algebra is a vector state of a representation. Mathlib's GNS construction
> gives the Hilbert space `H_ω` and the representation `π_ω`. The image `Ω_ω` of `1` in `H_ω` is a
> cyclic unit vector with `ω(a) = ⟪Ω_ω, π_ω(a) Ω_ω⟫`, and a faithful state gives a faithful
> representation.

## ii. Key results

> - `UnitalPositiveLinearMap.gnsRep` : the GNS representation of a state.
> - `UnitalPositiveLinearMap.gnsCyclicVector` : the cyclic vector `Ω_ω`.
> - `UnitalPositiveLinearMap.inner_gnsCyclicVector_gnsRep_gnsCyclicVector` : `ω(a) = ⟪Ω\_ω, π\_ω(a)
>   Ω\_ω⟫`.
> - `UnitalPositiveLinearMap.denseRange_gnsRep_gnsCyclicVector` : `Ω_ω` is cyclic.
> - `UnitalPositiveLinearMap.injective_gnsRep_of_isFaithful` : faithful states give faithful
>   representations.

## iv. References

> * None.

## A. The GNS representation

**`ProbabilisticTheory.UnitalPositiveLinearMap.GNS`**, an abbrev, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean#L66).

> The GNS Hilbert space `H_ω` carried by a state `ω` on a unital C⋆-algebra: the Hilbert space
> completion of `A` with respect to the (semi-)inner product `⟨x, y⟩ := ω(x⋆y)`.

```lean
noncomputable abbrev GNS
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsRep`**, an abbrev, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean#L70).

> The GNS representation `π_ω : A → B(H_ω)` carried by a state `ω`: the unital
> `⋆`-homomorphism into the bounded operators on `ω.GNS` induced by left multiplication.

```lean
noncomputable abbrev gnsRep : A →⋆ₐ[ℂ] (ω.GNS →L[ℂ] ω.GNS)
```

## B. The cyclic vector

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsCyclicVector`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean#L79).

> The GNS cyclic vector `Ω_ω ∈ H_ω`: the image of `1 : A` under `A → ω.GNS`.

```lean
noncomputable def gnsCyclicVector : ω.GNS
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsRep_gnsCyclicVector`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean#L84).

> `π_ω(a) Ω_ω` is, concretely, the image of `a` itself under `A → ω.GNS` — since
> `π_ω(a) Ω_ω = π_ω(a) · (\text{image of } 1) = \text{image of } (a \cdot 1) = \text{image of } a`.

```lean
lemma gnsRep_gnsCyclicVector (a : A) :
    ω.gnsRep a ω.gnsCyclicVector =
      ((ω.toPositiveLinearMap.toPreGNS a : ω.toPositiveLinearMap.PreGNS) : ω.GNS)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.norm_gnsCyclicVector`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean#L97).

> `Ω_ω` has unit norm: `‖Ω_ω‖² = ω(1⋆1) = ω(1) = 1`.

```lean
lemma norm_gnsCyclicVector : ‖ω.gnsCyclicVector‖ = 1
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.inner_gnsCyclicVector_gnsRep_gnsCyclicVector`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean#L109).

> The defining identity of the GNS construction: `ω` is recovered as the vector state of `π_ω`
> at the cyclic vector `Ω_ω`.

```lean
lemma inner_gnsCyclicVector_gnsRep_gnsCyclicVector (a : A) :
    ⟪ω.gnsCyclicVector, ω.gnsRep a ω.gnsCyclicVector⟫_ℂ = ω a
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.denseRange_gnsRep_gnsCyclicVector`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean#L118).

> `Ω_ω` is cyclic: the orbit `π_ω(A) Ω_ω` is dense in `H_ω`, so every vector in `H_ω` is a limit
> of vectors reachable from `Ω_ω` by applying elements of `A`.

```lean
lemma denseRange_gnsRep_gnsCyclicVector :
    DenseRange (fun a : A => ω.gnsRep a ω.gnsCyclicVector)
```

## C. Faithful states

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsFaithful`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean#L144).

> A state is **faithful** when only `0` gives `x⋆x` weight `0` — the standard notion of a
> faithful state on a C⋆-algebra, and the hypothesis under which the GNS representation `π_ω`
> becomes injective.

```lean
def IsFaithful (ω : 𝓢[ℂ, A]) : Prop
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.injective_gnsRep_of_isFaithful`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean#L147).

> The GNS representation of a faithful state is faithful.

```lean
lemma injective_gnsRep_of_isFaithful (h : ω.IsFaithful) : Function.Injective ω.gnsRep
```

## Depends on

- [Channels](../channel/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNS.lean)
