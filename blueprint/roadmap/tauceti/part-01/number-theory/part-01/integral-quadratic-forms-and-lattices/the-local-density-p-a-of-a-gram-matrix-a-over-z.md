---
declaration: def
origin: cited
lean: Matrix.localDensity
statement: formalized
---

# The local density `α_p(A)` of a Gram matrix `A` over `ℤ_p`

the limit as `r → ∞` of the
normalized counts `#{X ∈ Mₙ(ℤ/pʳ) : Xᵀ A X = A} / p ^ (r * n.choose 2)`. For symmetric `A` with
nonzero determinant the normalized counts are constant from `r = 2 v_p(2 det A) + 1` on
(`Matrix.localDensityCount_div_pow_of_det_ne_zero`), so the limit exists; for other `A` this is
a junk value.

```lean
Matrix.localDensity.{u_1} {n : Type u_1} [Fintype n] [DecidableEq n] {p : ℕ} [Fact (Nat.Prime p)]
  (A : Matrix n n ℤ_[p]) : ℚ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.localDensity`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/LocalDensity/Basic.html#Matrix.localDensity).

## Sources

- [Tau Ceti documentation: `Matrix.localDensity`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/LocalDensity/Basic.html#Matrix.localDensity)
- [Source of `Matrix.localDensity` in TauCeti/NumberTheory/IntegralLattice/LocalDensity/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/IntegralLattice/LocalDensity/Basic.lean#L545)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/IntegralLattices/STATUS.md)
