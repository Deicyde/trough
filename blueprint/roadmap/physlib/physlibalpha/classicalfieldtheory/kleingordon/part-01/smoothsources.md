---
declaration: module
origin: cited
lean: KleinGordon.Spacetime.lineDerivCLM_lineDerivCLM_ofFun, KleinGordon.Spacetime.distributionOperator_ofFun, KleinGordon.Spacetime.ofFun_mem_compactDistributions, KleinGordon.Spacetime.retardedDistribution_ofFun
statement: formalized
proof: formalized
---

# Smooth sources as distributions

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.SmoothSources`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/SmoothSources.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/SmoothSources.lean): 4 declarations, 4 with a docstring.

> The retarded solution of a smooth source and the distributional retarded solution agree.

## i. Overview

> A smooth function is a distribution by integration against test functions. The weak derivative of
> the induced distribution is the induced distribution of the derivative. The Klein–Gordon operator
> on the induced distribution is the induced distribution of the smooth operator. So the retarded
> solution of the distribution induced by a test field is the distribution induced by the smooth
> retarded solution.

## ii. Key results

> - `lineDerivCLM_lineDerivCLM_ofFun` : the second weak derivative.
> - `distributionOperator_ofFun` : the Klein–Gordon operator on the distribution of a smooth field.
> - `ofFun_mem_compactDistributions` : the distribution of a test field has compact support.
> - `retardedDistribution_ofFun` : the retarded solution of the distribution of a test field is the
>   distribution of the smooth retarded solution.

## iv. References

> None.

## A. Weak derivatives

> - `lineDerivCLM_lineDerivCLM_ofFun` : the second weak derivative of a smooth function.

## B. The Klein–Gordon operator

> - `distributionOperator_ofFun` : the Klein–Gordon operator on the distribution of a smooth field.

## C. Compact support

> - `ofFun_mem_compactDistributions` : the distribution of a test field has compact support.

## D. The retarded solution

> - `retardedDistribution_ofFun` : the retarded solution of the distribution of a test field is the
>   distribution of the smooth retarded solution.

**`KleinGordon.Spacetime.lineDerivCLM_lineDerivCLM_ofFun`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/SmoothSources.lean#L74).

> The weak derivative of the second order of a smooth function.

```lean
lemma lineDerivCLM_lineDerivCLM_ofFun {u : SpaceTime d → V} (hu : ContDiff ℝ ∞ u)
    (μ : Fin 1 ⊕ Fin d) :
    Distribution.lineDerivCLM (n := ⊤) (k := ⊤) (Lorentz.Vector.basis μ)
        (Distribution.lineDerivCLM (n := ⊤) (k := ⊤) (Lorentz.Vector.basis μ)
          (Distribution.ofFun (⊤ : Opens (SpaceTime d)) u volume ⊤)) =
      Distribution.ofFun (⊤ : Opens (SpaceTime d))
        (SpaceTime.deriv μ (SpaceTime.deriv μ u)) volume ⊤
```

**`KleinGordon.Spacetime.distributionOperator_ofFun`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/SmoothSources.lean#L89).

> **The Klein–Gordon operator on a smooth field.** The operator on the distribution induced by a
> smooth field is the distribution induced by the smooth operator.

```lean
lemma distributionOperator_ofFun (m : ℝ) (u : smoothFields d V) :
    distributionOperator m (Distribution.ofFun (⊤ : Opens (SpaceTime d)) u.val volume ⊤) =
      Distribution.ofFun (⊤ : Opens (SpaceTime d)) (operator m u).val volume ⊤
```

**`KleinGordon.Spacetime.ofFun_mem_compactDistributions`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/SmoothSources.lean#L123).

> The distribution induced by a test field has compact support.

```lean
lemma ofFun_mem_compactDistributions (f : TestField d V) :
    Distribution.ofFun (⊤ : Opens (SpaceTime d)) (f.val : SpaceTime d → V) volume ⊤ ∈
      compactDistributions (SpaceTime d) V
```

**`KleinGordon.Spacetime.retardedDistribution_ofFun`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/SmoothSources.lean#L133).

> **Smooth sources.** The retarded solution of the distribution induced by a test field is the
> distribution induced by the smooth retarded solution. This is the one Green operator realised on
> test fields, on compactly supported distributions and on smooth fields.

```lean
lemma retardedDistribution_ofFun {F : Type} [NormedAddCommGroup F] [NormedSpace ℂ F]
    [CompleteSpace F] (m : ℝ) (f : TestField d F) :
    Solution.retardedDistribution m ⟨Distribution.ofFun (⊤ : Opens (SpaceTime d))
        (f.val : SpaceTime d → F) volume ⊤, ofFun_mem_compactDistributions f⟩ =
      Distribution.ofFun (⊤ : Opens (SpaceTime d))
        ((Solution.retarded F m f).val : SpaceTime d → F) volume ⊤
```

## Depends on

- [Klein–Gordon fields and causal propagation](solution.md)

## Proof depends on

- [Distributions induced by smooth functions](../../../mathematics/part-02/distribution/offun.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/SmoothSources.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/SmoothSources.lean)
