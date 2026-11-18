---
declaration: module
origin: cited
lean: KleinGordon.Solution.causalKernel, KleinGordon.Solution.smul_zero_of_translation_eq_zero, KleinGordon.Solution.causalKernel_actDist, KleinGordon.Solution.causalKernel_actDist_of_not
statement: formalized
proof: formalized
---

# The causal propagator kernel

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.Covariance.CausalKernel`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/CausalKernel.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/CausalKernel.lean): 4 declarations, 4 with a docstring.

> The causal propagator kernel is invariant under the orthochronous Lorentz group and odd under time
> reversal.

## i. Overview

> The causal propagator kernel is the retarded kernel minus the advanced kernel, both centred at the
> spacetime origin. It solves the homogeneous equation. The covariance of the retarded and advanced
> point sources (`retardedPointSource_actDist`) transfers to it. A Lorentz transformation fixes the
> origin. An orthochronous one fixes the kernel. A time-reversing one swaps the retarded and the
> advanced kernel, so it changes the sign of the causal kernel.
>
> The covariance is proved on the distribution itself. The Fourier transform of the kernel inherits
> it with the induced action on the frequencies.

## ii. Key results

> - `causalKernel` : the retarded kernel minus the advanced kernel at the origin.
> - `causalKernel_actDist` : the kernel is invariant under orthochronous Lorentz transformations.
> - `causalKernel_actDist_of_not` : the kernel changes sign under time reversing ones.

## iv. References

> None.

## A. The kernel

> - `causalKernel` : the retarded kernel minus the advanced kernel at the origin.
> - `causalKernel_actDist` : the kernel is invariant under orthochronous Lorentz transformations.
> - `causalKernel_actDist_of_not` : the kernel changes sign under time reversing ones.

**`KleinGordon.Solution.causalKernel`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/CausalKernel.lean#L60).

> The causal propagator kernel: the retarded kernel minus the advanced kernel at the origin.

```lean
def causalKernel (m : ℝ) : DistributionField d ℝ
```

**`KleinGordon.Solution.smul_zero_of_translation_eq_zero`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/CausalKernel.lean#L64).

> A Poincaré transformation without translation fixes the origin.

```lean
lemma smul_zero_of_translation_eq_zero {g : PoincareGroup d} (h : g.translation = 0) :
    g • (0 : SpaceTime d) = 0
```

**`KleinGordon.Solution.causalKernel_actDist`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/CausalKernel.lean#L70).

> **Lorentz invariance of the causal kernel.** An orthochronous Lorentz transformation leaves
> the causal propagator kernel invariant.

```lean
lemma causalKernel_actDist (m : ℝ) {g : PoincareGroup d} (hg : g.IsOrthochronous)
    (h : g.translation = 0) : actDist g (causalKernel m) = causalKernel m
```

**`KleinGordon.Solution.causalKernel_actDist_of_not`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/CausalKernel.lean#L77).

> A time-reversing Lorentz transformation changes the sign of the causal propagator kernel.

```lean
lemma causalKernel_actDist_of_not (m : ℝ) {g : PoincareGroup d} (hg : ¬ g.IsOrthochronous)
    (h : g.translation = 0) : actDist g (causalKernel m) = -causalKernel m
```

## Depends on

- [Distributional sources](../part-01/distributionsources.md)
- [The Poincaré action on test functions and distributions](../../../relativity/poincare/distributions.md)

## Proof depends on

- [Poincaré covariance for distributional sources](covariance-distributions.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/CausalKernel.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/CausalKernel.lean)
