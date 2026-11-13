---
declaration: module
origin: cited
lean: Distribution.compactDistributions, Distribution.compactDistributionBound, Distribution.compactDistributionBound_vanishes, Distribution.multiplyDistribution, Distribution.multiplyDistribution_apply, Distribution.multiplyDistribution_eq_self, Distribution.compactCutoffRadius, Distribution.compactCutoffBump
statement: formalized
proof: formalized
---

# Compactly supported distributions and cutoffs

The module `PhyslibAlpha.Mathematics.Distribution.CompactSupport`, [PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean): 10 declarations, 10 with a docstring.

## i. Overview

> A compactly supported distribution is unchanged by a cutoff that equals one near its support.

## ii. Key results

> - `compactDistributions` : Compactly supported native distributions, defined by annihilation outside
>   a compact bound.
> - `compactDistributionBound` : A chosen compact support bound for a native compact distributional
>   source.
> - `multiplyDistribution` : Smooth multiplication of a distribution is the transpose of native test
>   multiplication.
> - `compactCutoffRadius` : A positive radius containing a compact set in its open ball.
> - `compactCutoffBump` : The canonical support-bound cutoff is a smooth compact bump.
> - `compactCutoff` : A native compact test cutoff equal to one in a neighborhood of the compact set.

## iv. References

> None.

## A. Compact distributional sources

> - `compactDistributions` : Compactly supported native distributions, defined by annihilation outside
>   a compact bound.
> - `compactDistributionBound` : A chosen compact support bound for a native compact distributional
>   source.
>
> Lemmas: `compactDistributionBound_vanishes`.

## B. Localization of native distributions

> - `multiplyDistribution` : Smooth multiplication of a distribution is the transpose of native test
>   multiplication.
> - `compactCutoffRadius` : A positive radius containing a compact set in its open ball.
> - `compactCutoffBump` : The canonical support-bound cutoff is a smooth compact bump.
> - `compactCutoff` : A native compact test cutoff equal to one in a neighborhood of the compact set.
>
> Lemmas: `multiplyDistribution_apply`, `multiplyDistribution_eq_self`, `compactCutoff_one_near`.

**`Distribution.compactDistributions`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean#L75).

> Compactly supported native distributions, defined by annihilation outside a compact bound.

```lean
def compactDistributions (E V : Type*) [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup V] [NormedSpace ℝ V] :
    Submodule ℝ (Distribution (⊤ : Opens E) V ⊤)
```

**`Distribution.compactDistributionBound`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean#L95).

> A chosen compact support bound for a native compact distributional source.

```lean
def compactDistributionBound (T : compactDistributions E V) : Compacts E
```

**`Distribution.compactDistributionBound_vanishes`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean#L99).

> The chosen compact bound has the source's native test annihilation property.

```lean
lemma compactDistributionBound_vanishes (T : compactDistributions E V) :
    Distribution.IsVanishingOn T.val (compactDistributionBound T : Set E)ᶜ
```

**`Distribution.multiplyDistribution`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean#L104).

> Smooth multiplication of a distribution is the transpose of native test multiplication.

```lean
def multiplyDistribution (w : E → ℝ) (hw : ContDiff ℝ ∞ w) :
    Distribution (⊤ : Opens E) V ⊤ →L[ℝ] Distribution (⊤ : Opens E) V ⊤
```

**`Distribution.multiplyDistribution_apply`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean#L109).

> Multiplication of native distributions is defined by moving the weight onto the test.

```lean
lemma multiplyDistribution_apply (w : E → ℝ) (hw : ContDiff ℝ ∞ w)
    (T : Distribution (⊤ : Opens E) V ⊤) (φ : _root_.TestFunction (⊤ : Opens E) ℝ ⊤) :
    multiplyDistribution w hw T φ = T (smoothWeightTest w hw φ)
```

**`Distribution.multiplyDistribution_eq_self`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean#L114).

> A weight equal to one near a compact support bound leaves the source unchanged.

```lean
lemma multiplyDistribution_eq_self (w : E → ℝ) (hw : ContDiff ℝ ∞ w)
    (T : Distribution (⊤ : Opens E) V ⊤) (K : Set E)
    (hT : Distribution.IsVanishingOn T Kᶜ)
    (hnear : ∀ p ∈ K, w =ᶠ[𝓝 p] (1 : E → ℝ)) : multiplyDistribution w hw T = T
```

**`Distribution.compactCutoffRadius`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean#L135).

> A positive radius containing a compact set in its open ball.

```lean
def compactCutoffRadius (K : Compacts E) : ℝ
```

**`Distribution.compactCutoffBump`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean#L139).

> The canonical support-bound cutoff is a smooth compact bump.

```lean
def compactCutoffBump (K : Compacts E) : ContDiffBump (0 : E)
```

**`Distribution.compactCutoff`**, a def, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean#L146).

> A native compact test cutoff equal to one in a neighborhood of the compact set.

```lean
def compactCutoff [FiniteDimensional ℝ E] (K : Compacts E) :
    _root_.TestFunction (⊤ : Opens E) ℝ ⊤
```

**`Distribution.compactCutoff_one_near`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean#L152).

> The support-bound cutoff equals one as a germ at every point in its compact bound.

```lean
lemma compactCutoff_one_near [FiniteDimensional ℝ E] (K : Compacts E) {p : E} (hp : p ∈ K) :
    (compactCutoff K : E → ℝ) =ᶠ[𝓝 p] (1 : E → ℝ)
```

## Depends on

- [Operations on test functions](testfunction.md)

## Sources

- [PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/CompactSupport.lean)
