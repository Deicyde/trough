---
declaration: theorem
origin: cited
lean: TauCeti.one_add_norm_add_sq_rpow_le_mul, TauCeti.one_add_norm_sq_rpow_le_mul_sub, TauCeti.one_add_norm_sq_rpow_mul_rpow_le_mul_sub_left, TauCeti.one_add_norm_sq_rpow_mul_rpow_le_mul_sub_right, TauCeti.one_add_norm_add_sq_rpow_le
statement: formalized
proof: formalized
---

# Peetre's inequality (`TauCeti.one_add_norm_add_sq_rpow_le_mul`)

For every real `s`, the Japanese bracket `⟨x⟩ = (1 + ‖x‖ ^ 2) ^ (1/2)`
satisfies `⟨x + y⟩ ^ s ≤ 2 ^ (|s| / 2) ⟨x⟩ ^ s ⟨y⟩ ^ |s|`.

```lean
TauCeti.one_add_norm_add_sq_rpow_le_mul.{u_1} {E : Type u_1} [SeminormedAddGroup E] (s : ℝ)
  (x y : E) :
  (1 + ‖x + y‖ ^ 2) ^ (s / 2) ≤ 2 ^ (|s| / 2) * (1 + ‖x‖ ^ 2) ^ (s / 2) * (1 + ‖y‖ ^ 2) ^ (|s| / 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.one_add_norm_add_sq_rpow_le_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JapaneseBracket/Peetre.html#TauCeti.one_add_norm_add_sq_rpow_le_mul).

## Other forms

**Peetre's inequality.** Formalized in Tau Ceti as [`TauCeti.one_add_norm_sq_rpow_le_mul_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JapaneseBracket/Peetre.html#TauCeti.one_add_norm_sq_rpow_le_mul_sub).

```lean
TauCeti.one_add_norm_sq_rpow_le_mul_sub.{u_1} {E : Type u_1} [SeminormedAddCommGroup E] (s : ℝ)
  (x y : E) :
  (1 + ‖x‖ ^ 2) ^ (s / 2) ≤ 2 ^ (|s| / 2) * (1 + ‖x - y‖ ^ 2) ^ (|s| / 2) * (1 + ‖y‖ ^ 2) ^ (s / 2)
```

**Peetre's inequality for a pair of weights, with the decay in `x`.** Formalized in Tau Ceti as [`TauCeti.one_add_norm_sq_rpow_mul_rpow_le_mul_sub_left`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JapaneseBracket/Peetre.html#TauCeti.one_add_norm_sq_rpow_mul_rpow_le_mul_sub_left).

```lean
TauCeti.one_add_norm_sq_rpow_mul_rpow_le_mul_sub_left.{u_1} {E : Type u_1}
  [SeminormedAddCommGroup E] (r s : ℝ) (x y : E) :
  (1 + ‖x‖ ^ 2) ^ (r / 2) * (1 + ‖y‖ ^ 2) ^ (-s / 2) ≤
    2 ^ (|s| / 2) * (1 + ‖x - y‖ ^ 2) ^ (|s| / 2) * (1 + ‖x‖ ^ 2) ^ ((r - s) / 2)
```

**Peetre's inequality for a pair of weights, with the decay in `y`.** Formalized in Tau Ceti as [`TauCeti.one_add_norm_sq_rpow_mul_rpow_le_mul_sub_right`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JapaneseBracket/Peetre.html#TauCeti.one_add_norm_sq_rpow_mul_rpow_le_mul_sub_right).

```lean
TauCeti.one_add_norm_sq_rpow_mul_rpow_le_mul_sub_right.{u_1} {E : Type u_1}
  [SeminormedAddCommGroup E] (r s : ℝ) (x y : E) :
  (1 + ‖x‖ ^ 2) ^ (r / 2) * (1 + ‖y‖ ^ 2) ^ (-s / 2) ≤
    2 ^ (|r| / 2) * (1 + ‖x - y‖ ^ 2) ^ (|r| / 2) * (1 + ‖y‖ ^ 2) ^ ((r - s) / 2)
```

**Peetre's inequality, subadditive form.** Formalized in Tau Ceti as [`TauCeti.one_add_norm_add_sq_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JapaneseBracket/Peetre.html#TauCeti.one_add_norm_add_sq_rpow_le).

```lean
TauCeti.one_add_norm_add_sq_rpow_le.{u_1} {E : Type u_1} [SeminormedAddGroup E] {s : ℝ} (hs : 0 ≤ s)
  (x y : E) :
  (1 + ‖x + y‖ ^ 2) ^ (s / 2) ≤ 2 ^ s * ((1 + ‖x‖ ^ 2) ^ (s / 2) + (1 + ‖y‖ ^ 2) ^ (s / 2))
```

## Sources

- [Tau Ceti documentation: `TauCeti.one_add_norm_add_sq_rpow_le_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JapaneseBracket/Peetre.html#TauCeti.one_add_norm_add_sq_rpow_le_mul)
- [Source of `TauCeti.one_add_norm_add_sq_rpow_le_mul` in TauCeti/Analysis/SpecialFunctions/JapaneseBracket/Peetre.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/JapaneseBracket/Peetre.lean#L89)
