---
declaration: module
origin: cited
lean: Distribution.ofFun_continuous_add, Distribution.ofFun_finset_sum, Distribution.lineDerivCLM_ofFun, Distribution.isVanishingOn_ofFun
statement: formalized
proof: formalized
---

# Distributions induced by smooth functions

The module `PhyslibAlpha.Mathematics.Distribution.OfFun`, [PhyslibAlpha/Mathematics/Distribution/OfFun.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/OfFun.lean): 4 declarations, 2 with a docstring.

> The distribution of a continuous function is additive in the function. The weak derivative of the
> distribution of a smooth function is the distribution of its derivative.

## i. Overview

> A locally integrable function `u` defines the distribution `φ ↦ ∫ φ • u`. Continuous functions are
> locally integrable. So the map `u ↦ ofFun u` is additive on continuous functions and commutes with
> finite sums. Integration by parts for compactly supported test functions shows that the weak line
> derivative of `ofFun u` is `ofFun` of the line derivative of a smooth `u`. A function vanishing
> outside a set induces a distribution vanishing outside it.

## ii. Key results

> - `Distribution.ofFun_continuous_add` : additivity on continuous functions.
> - `Distribution.ofFun_finset_sum` : finite sums.
> - `Distribution.lineDerivCLM_ofFun` : the weak derivative of the distribution of a smooth function.
> - `Distribution.isVanishingOn_ofFun` : vanishing outside a set.

## iv. References

> None.

## A. Linearity

> - `Distribution.ofFun_continuous_add` : additivity on continuous functions.
> - `Distribution.ofFun_finset_sum` : finite sums.

## B. Weak derivatives

> - `Distribution.lineDerivCLM_ofFun` : the weak derivative of the distribution of a smooth function.

## C. Support

> - `Distribution.isVanishingOn_ofFun` : vanishing outside a set.

**`Distribution.ofFun_continuous_add`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/OfFun.lean#L69).

```lean
lemma ofFun_continuous_add {u w : E → V} (hu : Continuous u) (hw : Continuous w) :
    ofFun (⊤ : Opens E) (u + w) μ ⊤ =
      ofFun (⊤ : Opens E) u μ ⊤ +
        ofFun (⊤ : Opens E) w μ ⊤
```

**`Distribution.ofFun_finset_sum`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/OfFun.lean#L76).

```lean
lemma ofFun_finset_sum {ι : Type*} (S : Finset ι) {g : ι → E → V}
    (hg : ∀ i, Continuous (g i)) :
    ofFun (⊤ : Opens E) (∑ i ∈ S, g i) μ ⊤ =
      ∑ i ∈ S, ofFun (⊤ : Opens E) (g i) μ ⊤
```

**`Distribution.lineDerivCLM_ofFun`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/OfFun.lean#L92).

> The weak derivative of the distribution induced by a smooth function is the distribution
> induced by its derivative.

```lean
lemma lineDerivCLM_ofFun {u : E → V} (hu : ContDiff ℝ ∞ u) (v : E) :
    lineDerivCLM (n := ⊤) (k := ⊤) v
        (ofFun (⊤ : Opens E) u μ ⊤) =
      ofFun (⊤ : Opens E) (fun x => fderiv ℝ u x v) μ ⊤
```

**`Distribution.isVanishingOn_ofFun`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/OfFun.lean#L130).

> A distribution induced by a function that vanishes outside a set vanishes outside it.

```lean
lemma isVanishingOn_ofFun {u : E → V} {K : Set (E)}
    (hK : ∀ x, x ∉ K → u x = 0) :
    IsVanishingOn (ofFun (⊤ : Opens E) u μ ⊤) Kᶜ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Distribution/OfFun.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/OfFun.lean)
