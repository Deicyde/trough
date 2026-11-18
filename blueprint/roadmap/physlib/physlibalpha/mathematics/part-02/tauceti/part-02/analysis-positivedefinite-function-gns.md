---
declaration: module
origin: cited
lean: TauCeti.IsPositiveDefiniteSub.gnsSpace, TauCeti.IsPositiveDefiniteSub.gnsVector, TauCeti.IsPositiveDefiniteSub.inner_gnsVector, TauCeti.IsPositiveDefiniteSub.norm_gnsVector_sub_sq, TauCeti.IsPositiveDefiniteSub.gnsVector_dense, TauCeti.IsPositiveDefiniteSub.gnsTranslation, TauCeti.IsPositiveDefiniteSub.gnsTranslation_gnsVector, TauCeti.IsPositiveDefiniteSub.gnsTranslation_zero
statement: formalized
proof: formalized
---

# The GNS translation representation of a positive-definite function

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.PositiveDefinite.Function.GNS`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean): 16 declarations, 16 with a docstring; 2 private, not shown.

> A positive-definite function on an additive commutative group has a canonical Hilbert space,
> obtained from its translation-invariant positive-definite kernel.

## i. Overview

> A positive-definite function on an additive commutative group has a canonical Hilbert space,
> obtained from its translation-invariant positive-definite kernel. Translation of the kernel
> vectors extends uniquely to a unitary operator. These operators form a group representation,
> and the original function is a matrix coefficient of its vector at zero.
>
> The translation action is part of the GNS/Kolmogorov decomposition of a positive-definite
> function. Its later use in LCA Bochner theory requires spectral measures and Pontryagin duality.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * W. Rudin, *Fourier Analysis on Groups* (1962), Chapter 1.

## A. Development

**`TauCeti.IsPositiveDefiniteSub.gnsSpace`**, an abbrev, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L56).

> The canonical Hilbert space of the translation-invariant kernel `K(a,b) = F(a-b)`.

```lean
abbrev gnsSpace
```

**`TauCeti.IsPositiveDefiniteSub.gnsVector`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L59).

> The vector in the GNS space corresponding to a group element.

```lean
def gnsVector (a : G) : hF.gnsSpace
```

**`TauCeti.IsPositiveDefiniteSub.inner_gnsVector`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L63).

> The inner product of two GNS vectors is the original positive-definite kernel.

```lean
lemma inner_gnsVector (a b : G) : ⟪hF.gnsVector a, hF.gnsVector b⟫_ℂ = F (a - b)
```

**`TauCeti.IsPositiveDefiniteSub.norm_gnsVector_sub_sq`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L68).

> Squared distances between GNS vectors are controlled by the real part of the function.

```lean
lemma norm_gnsVector_sub_sq (a b : G) :
    ‖hF.gnsVector a - hF.gnsVector b‖ ^ 2 =
      2 * ((F 0).re - (F (a - b)).re)
```

**`TauCeti.IsPositiveDefiniteSub.gnsVector_dense`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L79).

> The GNS vectors span a dense subspace.

```lean
lemma gnsVector_dense :
    (Submodule.span ℂ (Set.range hF.gnsVector)).topologicalClosure = ⊤
```

**`TauCeti.IsPositiveDefiniteSub.gnsTranslation`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L97).

> Translation by `g` is a unitary operator on the canonical GNS Hilbert space. Its action on
> the dense family of kernel vectors is `v(a) ↦ v(g+a)`.

```lean
def gnsTranslation (g : G) : hF.gnsSpace ≃ₗᵢ[ℂ] hF.gnsSpace
```

**`TauCeti.IsPositiveDefiniteSub.gnsTranslation_gnsVector`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L106).

> Translation acts on the canonical GNS vectors by addition.

```lean
lemma gnsTranslation_gnsVector (g a : G) :
    hF.gnsTranslation g (hF.gnsVector a) = hF.gnsVector (g + a)
```

**`TauCeti.IsPositiveDefiniteSub.gnsTranslation_zero`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L113).

> The translation at zero is the identity operator.

```lean
lemma gnsTranslation_zero : hF.gnsTranslation 0 = LinearIsometryEquiv.refl ℂ hF.gnsSpace
```

**`TauCeti.IsPositiveDefiniteSub.gnsTranslation_add`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L124).

> GNS translations compose according to the group law.

```lean
lemma gnsTranslation_add (g k : G) :
    hF.gnsTranslation (g + k) = (hF.gnsTranslation k).trans (hF.gnsTranslation g)
```

**`TauCeti.IsPositiveDefiniteSub.gnsRepresentation`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L145).

> The GNS representation as a homomorphism from the multiplicative copy of `G` to the
> unitary operators on its canonical Hilbert space.

```lean
def gnsRepresentation : Multiplicative G →* (hF.gnsSpace ≃ₗᵢ[ℂ] hF.gnsSpace)
```

**`TauCeti.IsPositiveDefiniteSub.gnsRepresentation_ofAdd`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L153).

> The representation operator at `g` is translation by `g`.

```lean
lemma gnsRepresentation_ofAdd (g : G) :
    hF.gnsRepresentation (Multiplicative.ofAdd g) = hF.gnsTranslation g
```

**`TauCeti.IsPositiveDefiniteSub.gnsRepresentation_gnsVector`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L158).

> The representation translates each GNS vector.

```lean
lemma gnsRepresentation_gnsVector (g a : G) :
    hF.gnsRepresentation (Multiplicative.ofAdd g) (hF.gnsVector a) =
      hF.gnsVector (g + a)
```

**`TauCeti.IsPositiveDefiniteSub.eq_inner_gnsRepresentation`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L165).

> A positive-definite function is a matrix coefficient of its canonical unitary
> representation.

```lean
lemma eq_inner_gnsRepresentation (g : G) :
    F g = ⟪hF.gnsRepresentation (Multiplicative.ofAdd g) (hF.gnsVector 0),
      hF.gnsVector 0⟫_ℂ
```

**`TauCeti.IsPositiveDefiniteSub.continuous_gnsVector`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L172).

> Continuity of a positive-definite function at zero makes its canonical feature map
> continuous. This is the regularity needed for a strongly continuous representation.

```lean
lemma continuous_gnsVector [TopologicalSpace G] [IsTopologicalAddGroup G]
    (hcont : ContinuousAt F 0) : Continuous hF.gnsVector
```

**`TauCeti.IsPositiveDefiniteSub.continuous_gnsTranslation_apply`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L204).

> The GNS translation representation is strongly continuous: every vector has a continuous
> orbit.

```lean
lemma continuous_gnsTranslation_apply [TopologicalSpace G] [IsTopologicalAddGroup G]
    (hcont : ContinuousAt F 0) (x : hF.gnsSpace) :
    Continuous (fun g : G => hF.gnsTranslation g x)
```

**`TauCeti.IsPositiveDefiniteSub.continuous_gnsRepresentation_apply`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean#L248).

> The canonical unitary representation has continuous orbits.

```lean
lemma continuous_gnsRepresentation_apply [TopologicalSpace G] [IsTopologicalAddGroup G]
    (hcont : ContinuousAt F 0) (x : hF.gnsSpace) :
    Continuous (fun g : Multiplicative G => hF.gnsRepresentation g x)
```

## Depends on

- [Positive-definite functions on an additive commutative group](../part-01/analysis-positivedefinite-addgroup.md)
- [Kolmogorov decomposition of a positive-definite kernel](analysis-positivedefinite-kernel-kolmogorov.md)

## Proof depends on

- [Extending bounded-operator convergence from dense subsets](../part-01/analysis-normed-operator-dense.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/GNS.lean)
