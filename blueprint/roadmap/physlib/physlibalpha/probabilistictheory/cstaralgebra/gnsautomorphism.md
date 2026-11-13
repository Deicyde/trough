---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.preGNSAut, ProbabilisticTheory.UnitalPositiveLinearMap.ofPreGNS_preGNSAut, ProbabilisticTheory.UnitalPositiveLinearMap.inner_preGNSAut, ProbabilisticTheory.UnitalPositiveLinearMap.norm_preGNSAut, ProbabilisticTheory.UnitalPositiveLinearMap.preGNSAutCLM, ProbabilisticTheory.UnitalPositiveLinearMap.gnsAut, ProbabilisticTheory.UnitalPositiveLinearMap.gnsAut_coe, ProbabilisticTheory.UnitalPositiveLinearMap.inner_gnsAut
statement: formalized
proof: formalized
---

# Symmetries of an invariant state are unitarily implemented

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.GNSAutomorphism`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean): 18 declarations, 11 with a docstring.

> A ⋆-automorphism preserving a state is implemented by a unitary operator on the GNS space that fixes
> the cyclic vector.

## i. Overview

> Let `ω` be a state on a unital C⋆-algebra `A` and `σ` a ⋆-automorphism of `A` with `ω ∘ σ = ω`.
> Then `[a] ↦ [σ a]` preserves the GNS inner product `⟨a, b⟩ = ω(a⋆ b)`, so it extends to an
> isometry of the GNS space `H_ω`, with inverse the extension of `σ⁻¹`. This unitary operator `U_σ`
> fixes the cyclic vector and intertwines the GNS representation: `U_σ π_ω(a) = π_ω(σ a) U_σ`.
> For a group of such automorphisms, for instance the translations of a lattice and a
> translation-invariant state, this gives a unitary representation of the group on `H_ω`.

## ii. Key results

> - `UnitalPositiveLinearMap.gnsUnitary` : the unitary operator implementing a symmetry.
> - `UnitalPositiveLinearMap.gnsUnitary_cyclicVector` : it fixes the cyclic vector.
> - `UnitalPositiveLinearMap.gnsUnitary_comp_gnsRep` : it intertwines the GNS representation.
> - `UnitalPositiveLinearMap.gnsUnitaryRep` : the unitary representation of a group of symmetries.

## iv. References

> * None.

## A. The isometry on the pre-Hilbert space

**`ProbabilisticTheory.UnitalPositiveLinearMap.preGNSAut`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L64).

> The map `[a] ↦ [σ a]` on the pre-Hilbert space of a state.

```lean
def preGNSAut : ω.toPositiveLinearMap.PreGNS →ₗ[ℂ] ω.toPositiveLinearMap.PreGNS
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.ofPreGNS_preGNSAut`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L71).

```lean
lemma ofPreGNS_preGNSAut (x : ω.toPositiveLinearMap.PreGNS) :
    ω.toPositiveLinearMap.ofPreGNS (preGNSAut ω σ x) = σ (ω.toPositiveLinearMap.ofPreGNS x)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.inner_preGNSAut`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L75).

> A symmetry preserving the state preserves the GNS inner product.

```lean
lemma inner_preGNSAut (hσ : ∀ a, ω (σ a) = ω a) (x y : ω.toPositiveLinearMap.PreGNS) :
    ⟪preGNSAut ω σ x, preGNSAut ω σ y⟫_ℂ = ⟪x, y⟫_ℂ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.norm_preGNSAut`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L81).

```lean
lemma norm_preGNSAut (hσ : ∀ a, ω (σ a) = ω a) (x : ω.toPositiveLinearMap.PreGNS) :
    ‖preGNSAut ω σ x‖ = ‖x‖
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.preGNSAutCLM`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L89).

> The symmetry as a bounded operator on the pre-Hilbert space.

```lean
def preGNSAutCLM (hσ : ∀ a, ω (σ a) = ω a) :
    ω.toPositiveLinearMap.PreGNS →L[ℂ] ω.toPositiveLinearMap.PreGNS
```

## B. The unitary operator

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsAut`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L96).

> The unitary operator on the GNS space implementing a symmetry that preserves the state.

```lean
def gnsAut (hσ : ∀ a, ω (σ a) = ω a) : ω.GNS →L[ℂ] ω.GNS
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsAut_coe`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L99).

```lean
lemma gnsAut_coe (hσ : ∀ a, ω (σ a) = ω a) (x : ω.toPositiveLinearMap.PreGNS) :
    gnsAut hσ (x : ω.GNS) = ((preGNSAut ω σ x : ω.toPositiveLinearMap.PreGNS) : ω.GNS)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.inner_gnsAut`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L104).

> The implementing operator preserves the inner product of the GNS space.

```lean
lemma inner_gnsAut (hσ : ∀ a, ω (σ a) = ω a) (x y : ω.GNS) :
    ⟪gnsAut hσ x, gnsAut hσ y⟫_ℂ = ⟪x, y⟫_ℂ
```

## C. Representations of groups of symmetries

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsAut_mul`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L122).

```lean
lemma gnsAut_mul (g h : Multiplicative G) :
    gnsAut (hα (g * h)) = gnsAut (hα g) * gnsAut (hα h)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsAut_one`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L136).

```lean
lemma gnsAut_one : gnsAut (hα 1) = 1
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.star_gnsAut_mul_gnsAut`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L148).

```lean
lemma star_gnsAut_mul_gnsAut (g : Multiplicative G) :
    star (gnsAut (hα g)) * gnsAut (hα g) = 1
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.star_gnsAut`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L154).

```lean
lemma star_gnsAut (g : Multiplicative G) : star (gnsAut (hα g)) = gnsAut (hα g⁻¹)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsUnitary`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L163).

> **Translations of an invariant state are unitarily implemented**: the unitary operator on the
> GNS space implementing the symmetry `α g`.

```lean
def gnsUnitary (g : Multiplicative G) : unitary (ω.GNS →L[ℂ] ω.GNS)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsUnitaryRep`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L170).

> **The unitary representation of a symmetry group on the GNS space of an invariant state.**

```lean
def gnsUnitaryRep : Multiplicative G →* unitary (ω.GNS →L[ℂ] ω.GNS)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsUnitary_cyclicVector`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L176).

> The implementing unitary fixes the cyclic vector.

```lean
lemma gnsUnitary_cyclicVector (g : Multiplicative G) :
    ((gnsUnitary hα g : unitary (ω.GNS →L[ℂ] ω.GNS)) : ω.GNS →L[ℂ] ω.GNS) ω.gnsCyclicVector =
      ω.gnsCyclicVector
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsUnitary_gnsRep_cyclicVector`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L186).

> The implementing unitary carries `π(a) Ω` to `π(α_g a) Ω`.

```lean
lemma gnsUnitary_gnsRep_cyclicVector (g : Multiplicative G) (a : A) :
    ((gnsUnitary hα g : unitary (ω.GNS →L[ℂ] ω.GNS)) : ω.GNS →L[ℂ] ω.GNS)
        (ω.gnsRep a ω.gnsCyclicVector) = ω.gnsRep (α g a) ω.gnsCyclicVector
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gnsUnitary_comp_gnsRep`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L196).

> The implementing unitaries intertwine the GNS representation with the symmetry:
> `U_g π(a) = π(α_g a) U_g`.

```lean
lemma gnsUnitary_comp_gnsRep (g : Multiplicative G) (a : A) :
    ((gnsUnitary hα g : unitary (ω.GNS →L[ℂ] ω.GNS)) : ω.GNS →L[ℂ] ω.GNS) * ω.gnsRep a =
      ω.gnsRep (α g a) * ((gnsUnitary hα g : unitary (ω.GNS →L[ℂ] ω.GNS)) : ω.GNS →L[ℂ] ω.GNS)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.inner_gnsRep_cyclicVector_gnsUnitary`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean#L221).

> The matrix coefficients of the GNS vectors `π(a) Ω` are the correlation functions of the
> state: `⟪π(a) Ω, U_g π(a) Ω⟫ = ω(a⋆ α_g(a))`.

```lean
lemma inner_gnsRep_cyclicVector_gnsUnitary (g : Multiplicative G) (a : A) :
    ⟪ω.gnsRep a ω.gnsCyclicVector,
      ((gnsUnitary hα g : unitary (ω.GNS →L[ℂ] ω.GNS)) : ω.GNS →L[ℂ] ω.GNS)
        (ω.gnsRep a ω.gnsCyclicVector)⟫_ℂ = ω (star a * α g a)
```

## Depends on

- [The GNS construction](gns.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/GNSAutomorphism.lean)
