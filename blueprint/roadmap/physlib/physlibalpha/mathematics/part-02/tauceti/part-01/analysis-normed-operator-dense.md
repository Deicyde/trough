---
declaration: module
origin: cited
lean: ContinuousLinearMap.norm_sub_apply_le_of_norm_le, ContinuousLinearMap.tendsto_apply_of_dense, ContinuousLinearMap.uniformCauchySeqOn_apply_of_dense
statement: formalized
proof: formalized
---

# Extending bounded-operator convergence from dense subsets

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.Normed.Operator.Dense`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/Normed/Operator/Dense.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Normed/Operator/Dense.lean): 3 declarations, 3 with a docstring.

> This file records two standard density arguments for uniformly bounded families of continuous linear
> maps between seminormed spaces.

## i. Overview

> This file records two standard density arguments for uniformly bounded families of continuous
> linear maps between seminormed spaces. Pointwise convergence on a dense subset extends to
> pointwise convergence everywhere, and uniform Cauchy convergence on a parameter set does likewise.
> Both rest on the same estimate
> `ContinuousLinearMap.norm_sub_apply_le_of_norm_le`, which moves the point at which a
> difference of two uniformly bounded operators is evaluated to a nearby point of the dense subset.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`ContinuousLinearMap.norm_sub_apply_le_of_norm_le`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Normed/Operator/Dense.lean#L54).

> Comparing two continuous linear maps of norm at most `K` at `x` costs at most `2 K ‖x - y‖`
> more than comparing them at `y`. This is the shared estimate of the two density arguments below:
> `y` is chosen in the dense subset, close to the arbitrary vector `x`.

```lean
lemma norm_sub_apply_le_of_norm_le {T S : X →L[𝕜] Y} {K : ℝ}
    (hT : ‖T‖ ≤ K) (hS : ‖S‖ ≤ K)
    (x y : X) : ‖T x - S x‖ ≤ ‖T y - S y‖ + 2 * K * ‖x - y‖
```

**`ContinuousLinearMap.tendsto_apply_of_dense`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Normed/Operator/Dense.lean#L67).

> A uniformly bounded family of continuous linear maps that converges pointwise on a dense
> subset converges pointwise everywhere.

```lean
lemma tendsto_apply_of_dense {ι : Type*} {l : Filter ι} {D : Set X}
    (hD : Dense D) {f : ι → X →L[𝕜] Y} {g : X →L[𝕜] Y} {C : ℝ}
    (hbound : ∀ᶠ i in l, ‖f i‖ ≤ C)
    (htendsto : ∀ x ∈ D, Tendsto (fun i => f i x) l (nhds (g x))) (x : X) :
    Tendsto (fun i => f i x) l (nhds (g x))
```

**`ContinuousLinearMap.uniformCauchySeqOn_apply_of_dense`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Normed/Operator/Dense.lean#L99).

> A uniformly bounded family of continuous linear maps that is uniformly Cauchy on a parameter
> set at every vector in a dense subset is uniformly Cauchy there at every vector.

```lean
lemma uniformCauchySeqOn_apply_of_dense {ι Z : Type*} {p : Filter ι}
    {D : Set X}
    (hD : Dense D) {f : ι → Z → X →L[𝕜] Y} {s : Set Z} {C : ℝ}
    (hbound : ∀ᶠ i in p, ∀ z ∈ s, ‖f i z‖ ≤ C)
    (hcauchy : ∀ x ∈ D, UniformCauchySeqOn (fun i z => f i z x) p s) (x : X) :
    UniformCauchySeqOn (fun i z => f i z x) p s
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/Normed/Operator/Dense.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Normed/Operator/Dense.lean)
