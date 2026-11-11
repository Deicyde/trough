---
declaration: theorem
origin: cited
lean: LinearMap.continuous_of_derivation_of_jacobson_eq_bot, LinearMap.continuous_of_derivation_of_nonUnitalJacobson_eq_bot
statement: formalized
proof: formalized
---

# Johnson–Sinclair theorem: derivations of semisimple Banach algebras are continuous

Let
`B` be a unital complex Banach algebra with zero Jacobson radical. Every linear map `D : B → B`
satisfying the Leibniz rule `D (x * y) = x * D y + D x * y` is continuous.

```lean
LinearMap.continuous_of_derivation_of_jacobson_eq_bot.{u_1} {B : Type u_1} [NormedRing B]
  [NormedAlgebra ℂ B] [CompleteSpace B] (D : B →ₗ[ℂ] B)
  (hD : ∀ (x y : B), D (x * y) = x * D y + D x * y) (hB : Ring.jacobson B = ⊥) : Continuous ⇑D
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rickart's scalar-commutant theorem](rickarts-scalar-commutant-theorem.md)
- [Sinclair's stability lemma](../../part-03/normed/part-02/sinclairs-stability-lemma.md)
- [Submodule.IsSeparatingIdeal](submodule-isseparatingideal.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.continuous_of_derivation_of_jacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Derivation.html#LinearMap.continuous_of_derivation_of_jacobson_eq_bot).

## Other forms

**Johnson–Sinclair theorem, nonunital form.** Formalized in Tau Ceti as [`LinearMap.continuous_of_derivation_of_nonUnitalJacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Derivation.html#LinearMap.continuous_of_derivation_of_nonUnitalJacobson_eq_bot).

```lean
LinearMap.continuous_of_derivation_of_nonUnitalJacobson_eq_bot.{u_1} {B : Type u_1}
  [NonUnitalNormedRing B] [NormedSpace ℂ B] [IsScalarTower ℂ B B] [SMulCommClass ℂ B B]
  [CompleteSpace B] (D : B →ₗ[ℂ] B) (hD : ∀ (x y : B), D (x * y) = x * D y + D x * y)
  (hB : TauCeti.nonUnitalJacobson ℂ B = ⊥) : Continuous ⇑D
```

## Sources

- [Tau Ceti documentation: `LinearMap.continuous_of_derivation_of_jacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Derivation.html#LinearMap.continuous_of_derivation_of_jacobson_eq_bot)
- [Source of `LinearMap.continuous_of_derivation_of_jacobson_eq_bot` in TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Derivation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Derivation.lean#L100)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachAlgebras/STATUS.md)
