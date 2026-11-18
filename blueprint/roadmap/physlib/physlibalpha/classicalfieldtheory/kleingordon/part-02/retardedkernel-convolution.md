---
declaration: module
origin: cited
lean: KleinGordon.Solution.retarded_eq_kernel, KleinGordon.Solution.actTestFunction_pointReflection_apply, KleinGordon.Solution.retardedDistribution_apply, KleinGordon.Solution.realAdvancedCutoff_compactCutoff_apply, KleinGordon.Solution.retardedDistribution_delta_apply
statement: formalized
proof: formalized
---

# The retarded solution as a convolution with the retarded kernel

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.RetardedKernel.Convolution`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Convolution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Convolution.lean): 5 declarations, 5 with a docstring.

> The retarded solution at `p` is the retarded kernel tested against the reflected and shifted
> source.

## i. Overview

> The retarded kernel `K` is the retarded point source at the origin. The point reflection
> `x ↦ p - x` reverses time. It is therefore a Poincaré transformation that is not orthochronous.
> It maps the retarded point source at the origin to the advanced point source at `p`. The
> advanced point source at `p` is the retarded response evaluated at `p`. This gives
> `(G_R f)(p) = K (x ↦ f (p - x))`.

## ii. Key results

> - `retarded_eq_kernel` : the retarded solution at `p` is the kernel tested against
>   `x ↦ f (p - x)`.

## iv. References

> None.

## A. The point reflection

## B. The convolution form

> - `retarded_eq_kernel` : the retarded solution at `p` is the kernel tested against
>   `x ↦ f (p - x)`.
> - `retardedDistribution_apply` : the retarded solution of a compactly supported distribution is
>   the distribution tested against the cut off advanced solution.
> - `retardedDistribution_delta_apply` : the point source gives the advanced solution at `p`.

**`KleinGordon.Solution.retarded_eq_kernel`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Convolution.lean#L66).

> **The retarded solution as a convolution.** The retarded solution of a real test source at
> `p` is the retarded kernel tested against the source reflected through `p`.

```lean
lemma retarded_eq_kernel (p : SpaceTime d) (f : TestField d ℝ) :
    ((realRetardedGreenOperator m).toLinearMap f).val p =
      retardedPointSource m 0
        (actTestFunction (pointReflection p)⁻¹ (testFieldEquiv ℝ f))
```

**`KleinGordon.Solution.actTestFunction_pointReflection_apply`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Convolution.lean#L79).

> The reflected source takes the value `f (p - x)` at `x`.

```lean
lemma actTestFunction_pointReflection_apply (p x : SpaceTime d) (f : TestField d ℝ) :
    actTestFunction (pointReflection p)⁻¹ (testFieldEquiv ℝ f) x =
      testFieldEquiv ℝ f (p - x)
```

**`KleinGordon.Solution.retardedDistribution_apply`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Convolution.lean#L87).

> **Convolution with a compactly supported distribution by transposition.** The retarded
> solution of `T` tested against `f` is `T` tested against the advanced solution of `f` cut off by
> a function that equals one near the support of `T`.

```lean
lemma retardedDistribution_apply (T : compactDistributions (SpaceTime d) ℝ) (f : TestField d ℝ) :
    retardedDistribution m T (testFieldEquiv ℝ f) =
      T.val (realAdvancedCutoff m (compactCutoff (compactDistributionBound T))
        (testFieldEquiv ℝ f))
```

**`KleinGordon.Solution.realAdvancedCutoff_compactCutoff_apply`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Convolution.lean#L93).

> The cut off advanced solution has the value `χ p * (A f) p`.

```lean
lemma realAdvancedCutoff_compactCutoff_apply (T : compactDistributions (SpaceTime d) ℝ)
    (f : TestField d ℝ) (p : SpaceTime d) :
    realAdvancedCutoff m (compactCutoff (compactDistributionBound T)) (testFieldEquiv ℝ f) p =
      compactCutoff (compactDistributionBound T) p *
        ((realAdvancedGreenOperator m).toLinearMap f).val p
```

**`KleinGordon.Solution.retardedDistribution_delta_apply`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Convolution.lean#L101).

> For the point source the transposed convolution is the advanced solution at `p`.

```lean
lemma retardedDistribution_delta_apply (p : SpaceTime d) (f : TestField d ℝ) :
    retardedDistribution m (deltaCompact p) (testFieldEquiv ℝ f) =
      ((realAdvancedGreenOperator m).toLinearMap f).val p
```

## Depends on

- [Poincaré covariance for distributional sources](covariance-distributions.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Convolution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Convolution.lean)
