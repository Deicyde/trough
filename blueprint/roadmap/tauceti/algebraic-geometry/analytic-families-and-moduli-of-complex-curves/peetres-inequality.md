---
declaration: theorem
origin: cited
lean: TauCeti.CircleSobolev.weight_add_le, TauCeti.one_add_norm_add_sq_rpow_le_mul, TauCeti.one_add_norm_sq_rpow_le_mul_sub, TauCeti.one_add_norm_add_sq_rpow_le
statement: formalized
proof: formalized
---

# Peetre's inequality

`(1 + |m + n|) ^ s ≤ (1 + |m|) ^ |s| (1 + |n|) ^ s` for every real
`s`. Shifting frequencies by `m` therefore changes the weights of every order `s` by at most the
factor `(1 + |m|) ^ |s|`.

```lean
TauCeti.CircleSobolev.weight_add_le (s : ℝ) (m n : ℤ) :
  TauCeti.CircleSobolev.weight s (m + n) ≤
    TauCeti.CircleSobolev.weight |s| m * TauCeti.CircleSobolev.weight s n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.weight_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Basic.html#TauCeti.CircleSobolev.weight_add_le).

## Other forms

**Peetre's inequality.** Formalized in Tau Ceti as [`TauCeti.one_add_norm_add_sq_rpow_le_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JapaneseBracket/Peetre.html#TauCeti.one_add_norm_add_sq_rpow_le_mul).

```lean
TauCeti.one_add_norm_add_sq_rpow_le_mul.{u_1} {E : Type u_1} [SeminormedAddGroup E] (s : ℝ)
  (x y : E) :
  (1 + ‖x + y‖ ^ 2) ^ (s / 2) ≤ 2 ^ (|s| / 2) * (1 + ‖x‖ ^ 2) ^ (s / 2) * (1 + ‖y‖ ^ 2) ^ (|s| / 2)
```

**Peetre's inequality, in the form `⟨x⟩ ^ s ≤ 2 ^ (|s| / 2) ⟨x - y⟩ ^ |s| ⟨y⟩ ^ s` for every real `s`.** Formalized in Tau Ceti as [`TauCeti.one_add_norm_sq_rpow_le_mul_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JapaneseBracket/Peetre.html#TauCeti.one_add_norm_sq_rpow_le_mul_sub).

```lean
TauCeti.one_add_norm_sq_rpow_le_mul_sub.{u_1} {E : Type u_1} [SeminormedAddCommGroup E] (s : ℝ)
  (x y : E) :
  (1 + ‖x‖ ^ 2) ^ (s / 2) ≤ 2 ^ (|s| / 2) * (1 + ‖x - y‖ ^ 2) ^ (|s| / 2) * (1 + ‖y‖ ^ 2) ^ (s / 2)
```

**Peetre's inequality, subadditive form.** Formalized in Tau Ceti as [`TauCeti.one_add_norm_add_sq_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JapaneseBracket/Peetre.html#TauCeti.one_add_norm_add_sq_rpow_le).

```lean
TauCeti.one_add_norm_add_sq_rpow_le.{u_1} {E : Type u_1} [SeminormedAddGroup E] {s : ℝ} (hs : 0 ≤ s)
  (x y : E) :
  (1 + ‖x + y‖ ^ 2) ^ (s / 2) ≤ 2 ^ s * ((1 + ‖x‖ ^ 2) ^ (s / 2) + (1 + ‖y‖ ^ 2) ^ (s / 2))
```

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.weight_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Basic.html#TauCeti.CircleSobolev.weight_add_le)
- [Source of `TauCeti.CircleSobolev.weight_add_le` in TauCeti/Analysis/Sobolev/Circle/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Circle/Basic.lean#L139)
