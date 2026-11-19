---
declaration: theorem
origin: cited
lean: Matrix.condNegSemidef_iff_forall_posSemidef_cexp_neg_mul, Matrix.CondNegSemidef.posSemidef_cexp_neg_mul
statement: formalized
proof: formalized
---

# Schoenberg's theorem

A complex kernel `ψ` is conditionally negative semidefinite if and
only if `(a, b) ↦ exp (-t ψ(a, b))` is positive semidefinite for every `t > 0`.

```lean
Matrix.condNegSemidef_iff_forall_posSemidef_cexp_neg_mul.{u_1} {n : Type u_1} {ψ : Matrix n n ℂ} :
  ψ.CondNegSemidef ↔
    ∀ (t : ℝ), 0 < t → (Matrix.of fun a b => Complex.exp (-(↑t * ψ a b))).PosSemidef
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.condNegSemidef_iff_forall_posSemidef_cexp_neg_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/PositiveDefinite/Kernel/Schoenberg.html#Matrix.condNegSemidef_iff_forall_posSemidef_cexp_neg_mul).

## Other forms

**Schoenberg's theorem, forward direction.** Formalized in Tau Ceti as [`Matrix.CondNegSemidef.posSemidef_cexp_neg_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/PositiveDefinite/Kernel/Schoenberg.html#Matrix.CondNegSemidef.posSemidef_cexp_neg_mul).

```lean
Matrix.CondNegSemidef.posSemidef_cexp_neg_mul.{u_1} {n : Type u_1} {ψ : Matrix n n ℂ}
  (hψ : ψ.CondNegSemidef) {t : ℝ} (ht : 0 ≤ t) :
  (Matrix.of fun a b => Complex.exp (-(↑t * ψ a b))).PosSemidef
```

## Sources

- [Tau Ceti documentation: `Matrix.condNegSemidef_iff_forall_posSemidef_cexp_neg_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/PositiveDefinite/Kernel/Schoenberg.html#Matrix.condNegSemidef_iff_forall_posSemidef_cexp_neg_mul)
- [Source of `Matrix.condNegSemidef_iff_forall_posSemidef_cexp_neg_mul` in TauCeti/Analysis/PositiveDefinite/Kernel/Schoenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PositiveDefinite/Kernel/Schoenberg.lean#L87)
