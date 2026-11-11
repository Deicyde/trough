---
declaration: theorem
origin: cited
lean: Matrix.exists_ne_zero_mulVec_eq_zero_norm_le
statement: formalized
proof: formalized
---

# Bombieri and Vaaler's Siegel lemma over `ℤ`, in the sup norm

Let `A` be a `p × n` integer
matrix with linearly independent rows and `p < n`, and let `g` be the greatest common divisor of
its maximal minors. Then `A x = 0` has a nonzero integral solution `x` with
`‖x‖ ≤ (√det (A Aᵀ) / g) ^ (1 / (n - p))`, where `‖x‖ = max_i |x i|`.

```lean
Matrix.exists_ne_zero_mulVec_eq_zero_norm_le.{u_1} {ι : Type u_1} [Fintype ι] {p : ℕ}
  {A : Matrix (Fin p) ι ℤ} (hA : LinearIndependent ℚ (A.map Int.cast).row)
  (hp : p < Fintype.card ι) :
  ∃ x,
    x ≠ 0 ∧
      A.mulVec x = 0 ∧ ‖x‖ ≤ (√↑(A * A.transpose).det / ↑A.minorGcd) ^ (↑(Fintype.card ι) - ↑p)⁻¹
```

## Depends on

- [Matrix.minorGcd](matrix-minorgcd.md)

## Proof depends on

- [Bombieri and Vaaler's Theorem 2 over `ℤ`, in the sup norm](bombieri-and-vaalers-theorem-2-over-z-in-the-sup.md)

## Lean

Formalized in Tau Ceti as [`Matrix.exists_ne_zero_mulVec_eq_zero_norm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/SiegelsLemma.html#Matrix.exists_ne_zero_mulVec_eq_zero_norm_le).

## Sources

- [Tau Ceti documentation: `Matrix.exists_ne_zero_mulVec_eq_zero_norm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/SiegelsLemma.html#Matrix.exists_ne_zero_mulVec_eq_zero_norm_le)
- [Source of `Matrix.exists_ne_zero_mulVec_eq_zero_norm_le` in TauCeti/NumberTheory/Height/Arakelov/SiegelsLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Height/Arakelov/SiegelsLemma.lean#L83)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HeightsAndUnits/STATUS.md)
