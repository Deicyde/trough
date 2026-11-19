---
declaration: theorem
origin: cited
lean: TauCeti.exists_posDef_eq_sum_smul_sqrt_sqrt_mul_mul_sqrt
statement: formalized
proof: formalized
---

# Existence of a positive-definite solution of the Bures–Wasserstein fixed-point equation

Let `C j` be positive semidefinite matrices and `w j ≥ 0` weights. If some `C j₀` with `w j₀ ≠ 0`
is positive definite, then there is a positive-definite matrix `S` with
`S = ∑ j, w j • √(√S * C j * √S)`.

```lean
TauCeti.exists_posDef_eq_sum_smul_sqrt_sqrt_mul_mul_sqrt.{u_1, u_2, u_3} {n : Type u_1}
  {𝕜 : Type u_2} [RCLike 𝕜] [Fintype n] {J : Type u_3} [Fintype J] {C : J → Matrix n n 𝕜}
  (w : J → NNReal) (hC : ∀ (j : J), (C j).PosSemidef) {j₀ : J} (hj₀ : w j₀ ≠ 0)
  (hCj₀ : (C j₀).PosDef) :
  ∃ S, S.PosDef ∧ S = ∑ j, ↑(w j) • CFC.sqrt (CFC.sqrt S * C j * CFC.sqrt S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brouwer's fixed-point theorem](../../algebraic-topology/singular/brouwers-fixed-point-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_posDef_eq_sum_smul_sqrt_sqrt_mul_mul_sqrt`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/BuresFixedPoint.html#TauCeti.exists_posDef_eq_sum_smul_sqrt_sqrt_mul_mul_sqrt).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_posDef_eq_sum_smul_sqrt_sqrt_mul_mul_sqrt`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/BuresFixedPoint.html#TauCeti.exists_posDef_eq_sum_smul_sqrt_sqrt_mul_mul_sqrt)
- [Source of `TauCeti.exists_posDef_eq_sum_smul_sqrt_sqrt_mul_mul_sqrt` in TauCeti/Analysis/Matrix/BuresFixedPoint.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Matrix/BuresFixedPoint.lean#L144)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OptimalTransport/STATUS.md)
