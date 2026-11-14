---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.covariance_maxCurrentState, CondensedMatter.TightBindingChain.variance_mul_variance_maxCurrentState, CondensedMatter.TightBindingChain.uncertaintyRatio, CondensedMatter.TightBindingChain.bound_ne_zero, CondensedMatter.TightBindingChain.one_le_uncertaintyRatio, CondensedMatter.TightBindingChain.uncertaintyRatio_eq_one_iff, CondensedMatter.TightBindingChain.one_lt_uncertaintyRatio, CondensedMatter.TightBindingChain.robertson_schrodinger_uncertaintyRatio
statement: formalized
proof: formalized
---

# The elemental uncertainty of the open tight binding chain

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.MaxCurrentState.UncertaintyRatio`, [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/UncertaintyRatio.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/UncertaintyRatio.lean): 8 declarations, 8 with a docstring.

## i. Overview

> In the maximal current state of the open chain the energy and position fluctuations are
> uncorrelated, so the uncertainty relation closes as an identity: the variance product is the
> squared bracket `(a t cos (π / (N + 1)))²` plus the centered Gram defect. The uncertainty ratio
> `C = √(Var H · Var X) / |a t cos (π / (N + 1))|` is therefore at least one, and equals one exactly
> for `N = 2` and `N = 3`. From four sites on it is strictly larger than one.

## ii. Key results

> - `covariance_maxCurrentState` : `Cov(H, X) = 0` in the maximal current state.
> - `variance_mul_variance_maxCurrentState` : `Var H · Var X = (a t cos (π / (N + 1)))² + defect`.
> - `uncertaintyRatio` : `C = √(Var H · Var X) / |a t cos (π / (N + 1))|`.
> - `one_le_uncertaintyRatio`, `uncertaintyRatio_eq_one_iff`, `one_lt_uncertaintyRatio`.
> - `robertson_schrodinger_uncertaintyRatio` : everything at once.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. No correlation

**`CondensedMatter.TightBindingChain.covariance_maxCurrentState`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/UncertaintyRatio.lean#L55).

> The energy and position fluctuations of the maximal current state are uncorrelated.

```lean
lemma covariance_maxCurrentState :
    covariance T.maxCurrentVectorState T.openHamiltonianObservable T.positionObservable = 0
```

**`CondensedMatter.TightBindingChain.variance_mul_variance_maxCurrentState`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/UncertaintyRatio.lean#L79).

> The uncertainty identity of the maximal current state:
> `Var H · Var X = (a t cos (π / (N + 1)))² + defect`.

```lean
lemma variance_mul_variance_maxCurrentState :
    variance T.maxCurrentVectorState T.openHamiltonianObservable *
        variance T.maxCurrentVectorState T.positionObservable =
      (T.a * T.t * Real.cos (Real.pi / (T.N + 1))) ^ 2 +
        centeredGramDefect T.maxCurrentVectorState T.openHamiltonianObservable
          T.positionObservable
```

## B. The uncertainty ratio `C`

**`CondensedMatter.TightBindingChain.uncertaintyRatio`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/UncertaintyRatio.lean#L98).

> The uncertainty ratio `C = √(Var H · Var X) / |a t cos (π / (N + 1))|` of the maximal current
> state: the uncertainty product over its Robertson bound.

```lean
noncomputable def uncertaintyRatio : ℝ
```

**`CondensedMatter.TightBindingChain.bound_ne_zero`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/UncertaintyRatio.lean#L104).

> The bound `a t cos (π / (N + 1))` is nonzero for `t ≠ 0` and `N ≥ 2`.

```lean
lemma bound_ne_zero (ht : T.t ≠ 0) (hN : 2 ≤ T.N) :
    T.a * T.t * Real.cos (Real.pi / (T.N + 1)) ≠ 0
```

**`CondensedMatter.TightBindingChain.one_le_uncertaintyRatio`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/UncertaintyRatio.lean#L113).

> `C` is at least one.

```lean
lemma one_le_uncertaintyRatio (ht : T.t ≠ 0) (hN : 2 ≤ T.N) : 1 ≤ T.uncertaintyRatio
```

**`CondensedMatter.TightBindingChain.uncertaintyRatio_eq_one_iff`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/UncertaintyRatio.lean#L119).

> `C` equals one exactly for `N = 2` and `N = 3`.

```lean
lemma uncertaintyRatio_eq_one_iff (ht : T.t ≠ 0) (hN : 2 ≤ T.N) :
    T.uncertaintyRatio = 1 ↔ T.N = 2 ∨ T.N = 3
```

**`CondensedMatter.TightBindingChain.one_lt_uncertaintyRatio`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/UncertaintyRatio.lean#L127).

> From four sites on, `C` is strictly larger than one.

```lean
lemma one_lt_uncertaintyRatio (ht : T.t ≠ 0) (hN : 4 ≤ T.N) : 1 < T.uncertaintyRatio
```

**`CondensedMatter.TightBindingChain.robertson_schrodinger_uncertaintyRatio`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/UncertaintyRatio.lean#L134).

> The Robertson–Schrödinger relation through the uncertainty ratio. In the maximal
> current state, `Var H · Var X = (a t cos (π / (N + 1)))² + defect`, `C` is at least one, and
> it equals one exactly for `N = 2` and `N = 3`.

```lean
lemma robertson_schrodinger_uncertaintyRatio (ht : T.t ≠ 0)
    (hN : 2 ≤ T.N) :
    variance T.maxCurrentVectorState T.openHamiltonianObservable *
        variance T.maxCurrentVectorState T.positionObservable =
      (T.a * T.t * Real.cos (Real.pi / (T.N + 1))) ^ 2 +
        centeredGramDefect T.maxCurrentVectorState T.openHamiltonianObservable
          T.positionObservable ∧
      1 ≤ T.uncertaintyRatio ∧ (T.uncertaintyRatio = 1 ↔ T.N = 2 ∨ T.N = 3)
```

## Depends on

- [The maximal current state of the open tight binding chain](maxcurrentstate-basic.md)
- [Uncertainty relations](../../../probabilistictheory/cstaralgebra/uncertainty.md)

## Proof depends on

- [Saturation of the uncertainty relation in the maximal current state](maxcurrentstate-saturation.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/UncertaintyRatio.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/UncertaintyRatio.lean)
