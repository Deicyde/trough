---
declaration: theorem
origin: cited
lean: YoungDiagram.injOn_zpow_cellContent_of_prod_geom_sum_ne_zero
statement: formalized
proof: formalized
---

# Split semisimplicity separates the Jucys–Murphy eigenvalues

Over a commutative ring
without zero divisors, if the unit `Q` is not `1` and the product `∏_{d=1}^{n} [d]_Q` of the
`Q`-integers `[d]_Q = 1 + Q + ⋯ + Q ^ (d - 1)` is nonzero, then on every Young diagram of size
less than `n` the powers `Q ^ content c` of distinct addable cells are distinct.

```lean
YoungDiagram.injOn_zpow_cellContent_of_prod_geom_sum_ne_zero.{u_1} {μ : YoungDiagram} {R : Type u_1}
  [CommRing R] [NoZeroDivisors R] {Q : Rˣ} {n : ℕ} (hQ : ↑Q ≠ 1)
  (hprod : ∏ d ∈ Finset.Icc 1 n, ∑ i ∈ Finset.range d, ↑Q ^ i ≠ 0) (hμ : μ.card < n) :
  Set.InjOn (fun c => ↑(Q ^ YoungDiagram.cellContent c)) {c | μ.IsAddable c}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`YoungDiagram.injOn_zpow_cellContent_of_prod_geom_sum_ne_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/ContentSeparation.html#YoungDiagram.injOn_zpow_cellContent_of_prod_geom_sum_ne_zero).

## Sources

- [Tau Ceti documentation: `YoungDiagram.injOn_zpow_cellContent_of_prod_geom_sum_ne_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/ContentSeparation.html#YoungDiagram.injOn_zpow_cellContent_of_prod_geom_sum_ne_zero)
- [Source of `YoungDiagram.injOn_zpow_cellContent_of_prod_geom_sum_ne_zero` in TauCeti/Algebra/TypeAHeckeAlgebra/ContentSeparation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/TypeAHeckeAlgebra/ContentSeparation.lean#L38)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
