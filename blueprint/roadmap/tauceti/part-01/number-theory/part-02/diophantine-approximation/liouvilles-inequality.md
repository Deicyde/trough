---
declaration: theorem
origin: cited
lean: Polynomial.inv_le_norm_ratCast_sub, IsAlgebraic.inv_le_norm_ratCast_sub, IsAlgebraic.exists_pos_le_norm_aeval_mul_supNorm_pow
statement: formalized
proof: formalized
---

# Liouville's inequality

Let `f ∈ ℤ[X]` have degree `d` and a complex root `α`. Every
rational number `ξ` with `f(ξ) ≠ 0` satisfies `|ξ - α| ≥ (2 ^ (d - 1) M(f) H(ξ) ^ d)⁻¹`, where
`M(f)` is the Mahler measure of `f` and `H(ξ)` the height of `ξ`.

```lean
Polynomial.inv_le_norm_ratCast_sub (f : Polynomial ℤ) {α : ℂ}
  (hα : (Polynomial.map (Int.castRingHom ℂ) f).IsRoot α) {ξ : ℚ} (hξ : (Polynomial.aeval ξ) f ≠ 0) :
  (2 ^ (f.natDegree - 1) * (Polynomial.map (Int.castRingHom ℂ) f).mahlerMeasure *
        Height.mulHeight₁ ξ ^ f.natDegree)⁻¹ ≤
    ‖↑ξ - α‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.inv_le_norm_ratCast_sub`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Liouville.html#Polynomial.inv_le_norm_ratCast_sub).

## Other forms

**Liouville's inequality for an algebraic number.** Formalized in Tau Ceti as [`IsAlgebraic.inv_le_norm_ratCast_sub`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Liouville.html#IsAlgebraic.inv_le_norm_ratCast_sub).

```lean
IsAlgebraic.inv_le_norm_ratCast_sub {α : ℂ} (hα : IsAlgebraic ℚ α) {ξ : ℚ} (hξ : ↑ξ ≠ α) :
  (2 ^ ((minpoly ℚ α).natDegree - 1) *
          (Polynomial.map (Int.castRingHom ℂ) (TauCeti.primitiveMinpoly α)).mahlerMeasure *
        Height.mulHeight₁ ξ ^ (minpoly ℚ α).natDegree)⁻¹ ≤
    ‖↑ξ - α‖
```

**Liouville's inequality for the value of an integer polynomial.** Formalized in Tau Ceti as [`IsAlgebraic.exists_pos_le_norm_aeval_mul_supNorm_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.html#IsAlgebraic.exists_pos_le_norm_aeval_mul_supNorm_pow).

```lean
IsAlgebraic.exists_pos_le_norm_aeval_mul_supNorm_pow {ξ : ℂ} (hξ : IsAlgebraic ℚ ξ) (n : ℕ) :
  ∃ c > 0,
    ∀ (P : Polynomial ℤ),
      P.natDegree ≤ n →
        (Polynomial.aeval ξ) P ≠ 0 →
          c ≤ ‖(Polynomial.aeval ξ) P‖ * P.supNorm ^ ((minpoly ℚ ξ).natDegree - 1)
```

## Sources

- [Tau Ceti documentation: `Polynomial.inv_le_norm_ratCast_sub`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Liouville.html#Polynomial.inv_le_norm_ratCast_sub)
- [Source of `Polynomial.inv_le_norm_ratCast_sub` in TauCeti/NumberTheory/DiophantineApproximation/Liouville.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/DiophantineApproximation/Liouville.lean#L44)
