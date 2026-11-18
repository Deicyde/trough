---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.gnsStructureFactor, ProbabilisticTheory.UnitalPositiveLinearMap.integral_gnsStructureFactor, ProbabilisticTheory.UnitalPositiveLinearMap.gnsStructureFactor_univ, ProbabilisticTheory.UnitalPositiveLinearMap.gnsCyclicVector_mem_sector, ProbabilisticTheory.UnitalPositiveLinearMap.projection_one_gnsCyclicVector
statement: formalized
proof: formalized
---

# The momentum decomposition of an invariant state

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.GNSSpectral`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSSpectral.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSSpectral.lean): 6 declarations (1 instance with no name), 5 with a docstring.

> The GNS space of a translation-invariant state decomposes over the momenta, and the momentum
> distribution of a local excitation is its structure factor.

## i. Overview

> For a state `ω` of a C⋆-algebra and an abelian group `G` of ⋆-automorphisms preserving `ω`, the
> unitary representation of `G` on the GNS space is the integral of the characters of `G` against a
> projection-valued measure `P` on the Pontryagin dual of `G`. The cyclic vector `Ω` is invariant, so
> it has momentum zero: `P` gives it to the trivial character. The vector `π(a) Ω` created by an
> observable `a` has momentum distribution `μ_a`, the finite measure with
> `∫ χ(g) dμ_a(χ) = ω(a⋆ α_g(a))`, the structure factor of `a`, and total mass `ω(a⋆ a)`.

## ii. Key results

> - `UnitalPositiveLinearMap.gnsStructureFactor` : the momentum distribution of `π(a) Ω`.
> - `UnitalPositiveLinearMap.integral_gnsStructureFactor` : its Fourier transform is the
>   correlation function of `a`.
> - `UnitalPositiveLinearMap.projection_one_gnsCyclicVector` : the invariant vector has momentum
>   zero.

## iv. References

> * None.

## A. The momentum distribution of a local excitation

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsStructureFactor`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSSpectral.lean#L71).

> The momentum distribution of the excitation `π(a) Ω` created by the observable `a` from the
> invariant state: the distribution of the vector `π(a) Ω` over the characters of the symmetry
> group.

```lean
def gnsStructureFactor (a : A) : Measure (PontryaginDual (Multiplicative G))
```

**An instance with no name**, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSSpectral.lean#L74).

```lean
instance (a : A) : IsFiniteMeasure (gnsStructureFactor hα a)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.integral_gnsStructureFactor`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSSpectral.lean#L79).

> **The Fourier transform of the momentum distribution is the correlation function**:
> `∫ χ(g) dμ_a(χ) = ω(a⋆ α_g(a))`.

```lean
lemma integral_gnsStructureFactor (a : A) (g : Multiplicative G) :
    ∫ χ, ((χ g : Circle) : ℂ) ∂gnsStructureFactor hα a = ω (star a * α g a)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsStructureFactor_univ`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSSpectral.lean#L85).

> The total momentum weight of the excitation `π(a) Ω` is `ω(a⋆ a)`.

```lean
lemma gnsStructureFactor_univ (a : A) :
    (gnsStructureFactor hα a).real Set.univ = (ω (star a * a)).re
```

## B. The invariant vector

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsCyclicVector_mem_sector`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSSpectral.lean#L99).

> The cyclic vector of an invariant state has momentum zero: its spectral measure is carried
> by the trivial character.

```lean
lemma gnsCyclicVector_mem_sector :
    ω.gnsCyclicVector ∈ ProbabilisticTheory.Representation.sector (toEnd (gnsUnitaryRep hα))
      (fun g => (((1 : PontryaginDual (Multiplicative G)) g : Circle) : ℂ))
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.projection_one_gnsCyclicVector`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSSpectral.lean#L110).

> **The vacuum has momentum zero.** For a countable symmetry group the spectral projection of
> the trivial character fixes the cyclic vector.

```lean
lemma projection_one_gnsCyclicVector [Countable G] :
    projection (gnsUnitaryRep hα) {(1 : PontryaginDual (Multiplicative G))} ω.gnsCyclicVector =
      ω.gnsCyclicVector
```

## Depends on

- [Symmetries of an invariant state are unitarily implemented](gnsautomorphism.md)
- [The commutant of a unitary representation of an abelian group](../representation/commutant.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSSpectral.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSSpectral.lean)
