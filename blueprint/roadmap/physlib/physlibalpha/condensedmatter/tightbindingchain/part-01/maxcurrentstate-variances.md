---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.variance_openHamiltonian_maxCurrentState, CondensedMatter.TightBindingChain.variance_position_maxCurrentState, CondensedMatter.TightBindingChain.uncertaintyRatio_sq_eq
statement: formalized
proof: formalized
---

# The variances of the maximal current state

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.MaxCurrentState.Variances`, [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Variances.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Variances.lean): 3 declarations, 3 with a docstring; 5 private, not shown.

## i. Overview

> In the maximal current state of the open chain with `N` sites, write `θ = π / (N + 1)`. The energy
> and position variances are
>
>   `Var H = 4 t² sin² θ (N - 1) / (N + 1)`,
>   `Var X = a² (((N + 1)² + 2) / 12 - 1 / (2 sin² θ))`.
>
> The position variance rests on one sum over the `(N + 1)`-th roots of unity,
> `∑ j < N + 1, (j - (N + 1) / 2)² cos (2 j θ) = (N + 1) / (2 sin² θ)`, obtained by summation by
> parts. Hence `C²` has the closed form
> `2 (N - 1) / ((N + 1) cos² θ) · (((N + 1)² + 2) / 6 · sin² θ - 1)`.

## ii. Key results

> - `variance_openHamiltonian_maxCurrentState` : `Var H = 4 t² sin² θ (N - 1) / (N + 1)`.
> - `variance_position_maxCurrentState` : `Var X = a² (((N + 1)² + 2) / 12 - 1 / (2 sin² θ))`.
> - `uncertaintyRatio_sq_eq` : the closed form of `C²`.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. Sums over the roots of unity

## B. The energy variance

**`CondensedMatter.TightBindingChain.variance_openHamiltonian_maxCurrentState`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Variances.lean#L168).

> The energy variance of the maximal current state, `Var H = 4 t² sin² θ (N - 1) / (N + 1)`.

```lean
lemma variance_openHamiltonian_maxCurrentState :
    variance T.maxCurrentVectorState T.openHamiltonianObservable =
      4 * T.t ^ 2 * Real.sin (Real.pi / (T.N + 1)) ^ 2 * (T.N - 1) / (T.N + 1)
```

## C. The position variance

**`CondensedMatter.TightBindingChain.variance_position_maxCurrentState`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Variances.lean#L188).

> The position variance of the maximal current state,
> `Var X = a² (((N + 1)² + 2) / 12 - 1 / (2 sin² θ))`.

```lean
lemma variance_position_maxCurrentState :
    variance T.maxCurrentVectorState T.positionObservable =
      T.a ^ 2 * (((T.N + 1) ^ 2 + 2) / 12 - 1 / (2 * Real.sin (Real.pi / (T.N + 1)) ^ 2))
```

## D. The closed form of `C`

**`CondensedMatter.TightBindingChain.uncertaintyRatio_sq_eq`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Variances.lean#L231).

> The closed form of `C²` in the maximal current state, with `θ = π / (N + 1)`:
> `C² = 2 (N - 1) / ((N + 1) cos² θ) · (((N + 1)² + 2) / 6 · sin² θ - 1)`.

```lean
lemma uncertaintyRatio_sq_eq (ht : T.t ≠ 0) (hN : 2 ≤ T.N) :
    T.uncertaintyRatio ^ 2 = 2 * (T.N - 1) / ((T.N + 1) * Real.cos (Real.pi / (T.N + 1)) ^ 2) *
      (((T.N + 1) ^ 2 + 2) / 6 * Real.sin (Real.pi / (T.N + 1)) ^ 2 - 1)
```

## Depends on

- [The elemental uncertainty of the open tight binding chain](maxcurrentstate-uncertaintyratio.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Variances.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Variances.lean)
