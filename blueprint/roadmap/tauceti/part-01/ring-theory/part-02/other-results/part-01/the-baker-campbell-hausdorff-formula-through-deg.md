---
declaration: theorem
origin: cited
lean: Ideal.log_exp_mul_exp_of_pow_three_eq_bot
statement: formalized
proof: formalized
---

# The Baker–Campbell–Hausdorff formula through degree two

for elements of a left ideal
with vanishing cube, `log (exp x * exp y) = x + y + ½ ⁅x, y⁆`.

```lean
Ideal.log_exp_mul_exp_of_pow_three_eq_bot.{u_1} {A : Type u_1} [Ring A] [Algebra ℚ A] (I : Ideal A)
  (hI : I ^ 3 = ⊥) {x y : A} (hx : x ∈ I) (hy : y ∈ I) :
  IsNilpotent.log (IsNilpotent.exp x * IsNilpotent.exp y) = x + y + (1 / 2) • ⁅x, y⁆
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Ideal.log_exp_mul_exp_of_pow_three_eq_bot`](https://taucetiproject.org/docs/TauCeti/RingTheory/Nilpotent/BCH.html#Ideal.log_exp_mul_exp_of_pow_three_eq_bot).

## Sources

- [Tau Ceti documentation: `Ideal.log_exp_mul_exp_of_pow_three_eq_bot`](https://taucetiproject.org/docs/TauCeti/RingTheory/Nilpotent/BCH.html#Ideal.log_exp_mul_exp_of_pow_three_eq_bot)
- [Source of `Ideal.log_exp_mul_exp_of_pow_three_eq_bot` in TauCeti/RingTheory/Nilpotent/BCH.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Nilpotent/BCH.lean#L129)
