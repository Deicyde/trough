---
declaration: theorem
origin: cited
lean: StrongDual.exists_pos_norm_sub_ofReal_smul_le
statement: formalized
proof: formalized
---

# The Bishop–Phelps lemma

Let `0 ≤ k < 1` and `f ≠ 0`. If the real part of `h` is positive
on the open cone `{x | k * ‖f‖ * ‖x‖ < re (f x)}`, then some positive real multiple of `h` lies
within `k * ‖f‖` of `f`.

```lean
StrongDual.exists_pos_norm_sub_ofReal_smul_le.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] (f h : StrongDual 𝕜 E) {k : ℝ} (hk₀ : 0 ≤ k)
  (hk₁ : k < 1) (hf : f ≠ 0)
  (hpos : ∀ (x : E), k * ‖f‖ * ‖x‖ < RCLike.re (f x) → 0 < RCLike.re (h x)) :
  ∃ c, 0 < c ∧ ‖f - ↑c • h‖ ≤ k * ‖f‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`StrongDual.exists_pos_norm_sub_ofReal_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#StrongDual.exists_pos_norm_sub_ofReal_smul_le).

## Sources

- [Tau Ceti documentation: `StrongDual.exists_pos_norm_sub_ofReal_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#StrongDual.exists_pos_norm_sub_ofReal_smul_le)
- [Source of `StrongDual.exists_pos_norm_sub_ofReal_smul_le` in TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.lean#L94)
