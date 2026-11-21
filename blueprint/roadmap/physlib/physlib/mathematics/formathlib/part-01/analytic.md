---
declaration: module
origin: cited
lean: AnalyticOnNhd.dense_setOf_ne_zero
statement: formalized
proof: formalized
---

# Analyticity and dense non-vanishing sets

The module `Physlib.Mathematics.ForMathlib.Analytic`, [Physlib/Mathematics/ForMathlib/Analytic.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Mathematics/ForMathlib/Analytic.lean): 1 declaration, 1 with a docstring.

> Density of the non-vanishing set of an analytic function.

## i. Overview

> By the identity principle, an analytic function on a connected normed space which vanishes on a
> non-empty open set vanishes everywhere. Hence an analytic function which is non-zero at one point
> is non-zero on a dense set.
>
> Applications include domains in phase space used in proofs of Liouville integrability.

## ii. Key results

> - `AnalyticOnNhd.dense_setOf_ne_zero` : a function analytic on a connected space and non-zero at
>   some point is non-zero on a dense set.

## iv. References

> The density proof uses the identity principle in `Mathlib.Analysis.Analytic.Uniqueness`.

## A. Density of the non-vanishing set

**`AnalyticOnNhd.dense_setOf_ne_zero`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Mathematics/ForMathlib/Analytic.lean#L50).

> A function analytic on a connected space, and non-zero at some point, is non-zero on a dense
> set.

```lean
lemma AnalyticOnNhd.dense_setOf_ne_zero {𝕜 E F : Type*} [NontriviallyNormedField 𝕜]
    [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F] [NormedSpace 𝕜 F]
    [PreconnectedSpace E] {f : E → F} (hf : AnalyticOnNhd 𝕜 f Set.univ) {x₀ : E}
    (hx₀ : f x₀ ≠ 0) : Dense {x | f x ≠ 0}
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/Analytic.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Mathematics/ForMathlib/Analytic.lean)
