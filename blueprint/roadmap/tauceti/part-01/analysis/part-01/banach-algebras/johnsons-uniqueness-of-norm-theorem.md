---
declaration: theorem
origin: cited
lean: AlgebraNorm.exists_le_mul_and_le_mul_of_jacobson_eq_bot, RingNorm.exists_le_mul_and_le_mul_of_nonUnitalJacobson_eq_bot
statement: formalized
proof: formalized
---

# Johnson's uniqueness-of-norm theorem

On a unital complex algebra `A` with zero Jacobson
radical, any two algebra norms under which `A` is complete are equivalent.

```lean
AlgebraNorm.exists_le_mul_and_le_mul_of_jacobson_eq_bot.{u_1} {A : Type u_1} [Ring A] [Algebra ℂ A]
  (f g : AlgebraNorm ℂ A) (hf : CompleteSpace A) (hg : CompleteSpace A) (hA : Ring.jacobson A = ⊥) :
  ∃ C₁ C₂, ∃ (_ : 0 < C₁) (_ : 0 < C₂), ∀ (x : A), f x ≤ C₁ * g x ∧ g x ≤ C₂ * f x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Johnson's theorem](johnsons-theorem.md)

## Lean

Formalized in Tau Ceti as [`AlgebraNorm.exists_le_mul_and_le_mul_of_jacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/NormUniqueness.html#AlgebraNorm.exists_le_mul_and_le_mul_of_jacobson_eq_bot).

## Other forms

**Johnson's uniqueness-of-norm theorem.** Formalized in Tau Ceti as [`RingNorm.exists_le_mul_and_le_mul_of_nonUnitalJacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/NormUniqueness.html#RingNorm.exists_le_mul_and_le_mul_of_nonUnitalJacobson_eq_bot).

```lean
RingNorm.exists_le_mul_and_le_mul_of_nonUnitalJacobson_eq_bot.{u_1} {A : Type u_1} [NonUnitalRing A]
  [_root_.Module ℂ A] [IsScalarTower ℂ A A] [SMulCommClass ℂ A A] (f g : RingNorm A)
  (hfs : ∀ (c : ℂ) (x : A), f (c • x) ≤ ‖c‖ * f x) (hgs : ∀ (c : ℂ) (x : A), g (c • x) ≤ ‖c‖ * g x)
  (hf : CompleteSpace A) (hg : CompleteSpace A) (hA : TauCeti.nonUnitalJacobson ℂ A = ⊥) :
  ∃ C₁ C₂, ∃ (_ : 0 < C₁) (_ : 0 < C₂), ∀ (x : A), f x ≤ C₁ * g x ∧ g x ≤ C₂ * f x
```

## Sources

- [Tau Ceti documentation: `AlgebraNorm.exists_le_mul_and_le_mul_of_jacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/NormUniqueness.html#AlgebraNorm.exists_le_mul_and_le_mul_of_jacobson_eq_bot)
- [Source of `AlgebraNorm.exists_le_mul_and_le_mul_of_jacobson_eq_bot` in TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/NormUniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/NormUniqueness.lean#L112)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachAlgebras/STATUS.md)
