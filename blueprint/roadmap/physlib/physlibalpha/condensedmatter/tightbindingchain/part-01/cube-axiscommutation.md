---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.hopping_eq_zero_of_degenerate, CondensedMatter.TightBindingChain.bracket_openHamiltonian_position_eq_zero_iff, CondensedMatter.TightBindingChain.axisBracket_maxCurrentCubeVectorState_ne_zero, CondensedMatter.TightBindingChain.bracket_cubePairs_pair_ne_zero, CondensedMatter.TightBindingChain.variance_mul_variance_cubePairs_pos, CondensedMatter.TightBindingChain.bracket_cubePairs_eq_zero_iff
statement: formalized
proof: formalized
---

# Which observables of the open tight binding cube commute

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.Cube.AxisCommutation`, [PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/AxisCommutation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/AxisCommutation.lean): 6 declarations, 6 with a docstring.

## i. Overview

> The six observables of the cube are the Hamiltonian `H` and the position `X` of each axis
> (`cubePairs`). Two of them on different axes commute (`bracket_cubePairs_of_ne`). Here the
> converse: `H` and `X` of one axis do not commute, since their bracket has a nonzero expectation in
> the maximal current state, and by Robertson's relation the product of their variances is positive
> in that state. So two distinct observables of the cube commute if and only if they lie on
> different axes.

## ii. Key results

> - `bracket_openHamiltonian_position_eq_zero_iff` : on one chain, `⁅H, X⁆ = 0` if and only if
>   `t = 0` or the chain has a single site, so the hypotheses below cannot be dropped.
> - `axisBracket_maxCurrentCubeVectorState_ne_zero` : in the maximal current state, the expectation
>   of `⁅H, X⁆` is nonzero on each axis.
> - `bracket_cubePairs_pair_ne_zero` : `H` and `X` of one axis do not commute.
> - `bracket_cubePairs_eq_zero_iff` : two distinct observables of the cube commute if and only if
>   they lie on different axes.
> - `variance_mul_variance_cubePairs_pos` : in the maximal current state, `Var H · Var X > 0` on
>   each axis.

## iv. References

> * H. P. Robertson, *The uncertainty principle*, Phys. Rev. 34 (1929) 163.

## A. One chain: when `H` and `X` commute

**`CondensedMatter.TightBindingChain.hopping_eq_zero_of_degenerate`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/AxisCommutation.lean#L63).

> Without hopping, or with a single site, the hopping operator is zero.

```lean
lemma hopping_eq_zero_of_degenerate (T : TightBindingChain) (h : T.t = 0 ∨ T.N < 2) :
    T.hopping = 0
```

**`CondensedMatter.TightBindingChain.bracket_openHamiltonian_position_eq_zero_iff`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/AxisCommutation.lean#L78).

> On one chain, the Hamiltonian and the position commute if and only if there is no hopping or
> only one site.

```lean
lemma bracket_openHamiltonian_position_eq_zero_iff (T : TightBindingChain) :
    ⁅T.openHamiltonianObservable, T.positionObservable⁆ = 0 ↔ T.t = 0 ∨ T.N < 2
```

## B. The pair of an axis does not commute

**`CondensedMatter.TightBindingChain.axisBracket_maxCurrentCubeVectorState_ne_zero`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/AxisCommutation.lean#L101).

> In the maximal current state of the cube, the expectation of `⁅H, X⁆` is nonzero on each
> axis.

```lean
lemma axisBracket_maxCurrentCubeVectorState_ne_zero (hx : Tx.t ≠ 0) (hy : Ty.t ≠ 0)
    (hz : Tz.t ≠ 0) (hNx : 2 ≤ Tx.N) (hNy : 2 ≤ Ty.N) (hNz : 2 ≤ Tz.N) (k : Fin 3) :
    Tx.axisBracket Ty Tz (Tx.maxCurrentCubeVectorState Ty Tz) k ≠ 0
```

**`CondensedMatter.TightBindingChain.bracket_cubePairs_pair_ne_zero`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/AxisCommutation.lean#L114).

> The Hamiltonian and the position of one axis of the cube do not commute.

```lean
lemma bracket_cubePairs_pair_ne_zero (hx : Tx.t ≠ 0) (hy : Ty.t ≠ 0) (hz : Tz.t ≠ 0)
    (hNx : 2 ≤ Tx.N) (hNy : 2 ≤ Ty.N) (hNz : 2 ≤ Tz.N) (k : Fin 3) :
    ⁅Tx.cubePairs Ty Tz (0, k), Tx.cubePairs Ty Tz (1, k)⁆ ≠ 0
```

**`CondensedMatter.TightBindingChain.variance_mul_variance_cubePairs_pos`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/AxisCommutation.lean#L121).

> In the maximal current state of the cube, the variances of `H` and `X` of each axis have a
> positive product.

```lean
lemma variance_mul_variance_cubePairs_pos (hx : Tx.t ≠ 0) (hy : Ty.t ≠ 0) (hz : Tz.t ≠ 0)
    (hNx : 2 ≤ Tx.N) (hNy : 2 ≤ Ty.N) (hNz : 2 ≤ Tz.N) (k : Fin 3) :
    0 < variance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.cubePairs Ty Tz (0, k)) *
      variance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.cubePairs Ty Tz (1, k))
```

## C. Commuting and axes

**`CondensedMatter.TightBindingChain.bracket_cubePairs_eq_zero_iff`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/AxisCommutation.lean#L137).

> Two distinct observables of the cube commute if and only if they lie on different axes.

```lean
lemma bracket_cubePairs_eq_zero_iff (hx : Tx.t ≠ 0) (hy : Ty.t ≠ 0) (hz : Tz.t ≠ 0)
    (hNx : 2 ≤ Tx.N) (hNy : 2 ≤ Ty.N) (hNz : 2 ≤ Tz.N) {p q : Fin 2 × Fin 3} (h : p ≠ q) :
    ⁅Tx.cubePairs Ty Tz p, Tx.cubePairs Ty Tz q⁆ = 0 ↔ p.2 ≠ q.2
```

## Depends on

- [The open tight binding cube](cube-basic.md)

## Proof depends on

- [Mandelstam–Tamm and Cramér–Rao in the open tight binding chain](current-mandelstamtamm.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/AxisCommutation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/AxisCommutation.lean)
