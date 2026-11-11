---
declaration: theorem
origin: cited
lean: NonUnitalAlgHom.continuous_of_nonUnitalJacobson_eq_bot, NonUnitalAlgHom.continuous_of_jacobson_eq_bot
statement: formalized
proof: formalized
---

# Šilov's theorem

Every homomorphism from a complex Banach algebra into a commutative
semisimple complex Banach algebra is continuous. Neither algebra needs a unit.

```lean
NonUnitalAlgHom.continuous_of_nonUnitalJacobson_eq_bot.{u_1, u_2} {A : Type u_1} {B : Type u_2}
  [NonUnitalNormedRing A] [NormedSpace ℂ A] [CompleteSpace A] [NonUnitalNormedCommRing B]
  [NormedSpace ℂ B] [IsScalarTower ℂ B B] [SMulCommClass ℂ B B] [CompleteSpace B] (θ : A →ₙₐ[ℂ] B)
  (hB : TauCeti.nonUnitalJacobson ℂ B = ⊥) : Continuous ⇑θ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NonUnitalAlgHom.continuous_of_nonUnitalJacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/AutomaticContinuity/Commutative.html#NonUnitalAlgHom.continuous_of_nonUnitalJacobson_eq_bot).

## Other forms

**Šilov's theorem for a unital target.** Formalized in Tau Ceti as [`NonUnitalAlgHom.continuous_of_jacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/AutomaticContinuity/Commutative.html#NonUnitalAlgHom.continuous_of_jacobson_eq_bot).

```lean
NonUnitalAlgHom.continuous_of_jacobson_eq_bot.{u_1, u_2} {A : Type u_1} {B : Type u_2}
  [NonUnitalNormedRing A] [NormedSpace ℂ A] [CompleteSpace A] [NormedCommRing B] [NormedAlgebra ℂ B]
  [CompleteSpace B] (θ : A →ₙₐ[ℂ] B) (hB : Ring.jacobson B = ⊥) : Continuous ⇑θ
```

## Sources

- [Tau Ceti documentation: `NonUnitalAlgHom.continuous_of_nonUnitalJacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/AutomaticContinuity/Commutative.html#NonUnitalAlgHom.continuous_of_nonUnitalJacobson_eq_bot)
- [Source of `NonUnitalAlgHom.continuous_of_nonUnitalJacobson_eq_bot` in TauCeti/Analysis/Normed/Algebra/AutomaticContinuity/Commutative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Algebra/AutomaticContinuity/Commutative.lean#L70)
