---
declaration: theorem
origin: cited
lean: Matrix.abv_det_le_prod_of_le, Matrix.abv_det_le_prod_of_le'
statement: formalized
proof: formalized
---

# Ultrametric Hadamard bound, row form

For a nonarchimedean absolute value `abv`, if row `i`
of `A` is bounded entrywise in `abv` by `b i`, then `abv A.det ≤ ∏ i, b i`.

```lean
Matrix.abv_det_le_prod_of_le.{u_1, u_2, u_3} {R : Type u_1} {S : Type u_2} [CommRing R]
  [Nontrivial R] [CommRing S] [LinearOrder S] [IsStrictOrderedRing S] {n : Type u_3} [Fintype n]
  [DecidableEq n] (A : Matrix n n R) {abv : AbsoluteValue R S} (habv : IsNonarchimedean ⇑abv)
  {b : n → S} (hA : ∀ (i j : n), abv (A i j) ≤ b i) : abv A.det ≤ ∏ i, b i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.abv_det_le_prod_of_le`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.html#Matrix.abv_det_le_prod_of_le).

## Other forms

**Ultrametric Hadamard bound, column form.** Formalized in Tau Ceti as [`Matrix.abv_det_le_prod_of_le'`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.html#Matrix.abv_det_le_prod_of_le').

```lean
Matrix.abv_det_le_prod_of_le'.{u_1, u_2, u_3} {R : Type u_1} {S : Type u_2} [CommRing R]
  [Nontrivial R] [CommRing S] [LinearOrder S] [IsStrictOrderedRing S] {n : Type u_3} [Fintype n]
  [DecidableEq n] (A : Matrix n n R) {abv : AbsoluteValue R S} (habv : IsNonarchimedean ⇑abv)
  {b : n → S} (hA : ∀ (i j : n), abv (A i j) ≤ b j) : abv A.det ≤ ∏ j, b j
```

## Sources

- [Tau Ceti documentation: `Matrix.abv_det_le_prod_of_le`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.html#Matrix.abv_det_le_prod_of_le)
- [Source of `Matrix.abv_det_le_prod_of_le` in TauCeti/LinearAlgebra/Matrix/AbsoluteValue.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.lean#L97)
