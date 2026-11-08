---
declaration: theorem
origin: cited
lean: LinearMap.continuous_of_derivation_of_nonUnitalJacobson_eq_bot, LinearMap.continuous_of_derivation_of_jacobson_eq_bot
statement: formalized
proof: formalized
---

# Johnson–Sinclair theorem, nonunital form

Let `B` be a complex Banach algebra, not
necessarily unital, with zero Jacobson radical. Every linear map `D : B → B` satisfying the
Leibniz rule `D (x * y) = x * D y + D x * y` is continuous.

```lean
LinearMap.continuous_of_derivation_of_nonUnitalJacobson_eq_bot.{u_1} {B : Type u_1}
  [NonUnitalNormedRing B] [NormedSpace ℂ B] [IsScalarTower ℂ B B] [SMulCommClass ℂ B B]
  [CompleteSpace B] (D : B →ₗ[ℂ] B) (hD : ∀ (x y : B), D (x * y) = x * D y + D x * y)
  (hB : TauCeti.nonUnitalJacobson ℂ B = ⊥) : Continuous ⇑D
```

## Depends on

- [TauCeti.nonUnitalJacobson](../../../part-01/banach-algebras/tauceti-nonunitaljacobson.md)

## Proof depends on

- [LinearMap.continuous_iff_separatingSpace_eq_bot](../../../part-01/banach-algebras/linearmap-continuous-iff-separatingspace-eq-bot.md)
- [LinearMap.separatingSpace](../../../part-01/banach-algebras/linearmap-separatingspace.md)
- [Rickart's scalar-commutant theorem](../part-02/rickarts-scalar-commutant-theorem.md)
- [Sinclair's stability lemma](../../../part-01/banach-algebras/sinclairs-stability-lemma.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.continuous_of_derivation_of_nonUnitalJacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Derivation.html#LinearMap.continuous_of_derivation_of_nonUnitalJacobson_eq_bot).

## Other forms

**Johnson–Sinclair theorem: derivations of semisimple Banach algebras are continuous.** Formalized in Tau Ceti as [`LinearMap.continuous_of_derivation_of_jacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Derivation.html#LinearMap.continuous_of_derivation_of_jacobson_eq_bot).

```lean
LinearMap.continuous_of_derivation_of_jacobson_eq_bot.{u_1} {B : Type u_1} [NormedRing B]
  [NormedAlgebra ℂ B] [CompleteSpace B] (D : B →ₗ[ℂ] B)
  (hD : ∀ (x y : B), D (x * y) = x * D y + D x * y) (hB : Ring.jacobson B = ⊥) : Continuous ⇑D
```

## Sources

- [Tau Ceti documentation: `LinearMap.continuous_of_derivation_of_nonUnitalJacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Derivation.html#LinearMap.continuous_of_derivation_of_nonUnitalJacobson_eq_bot)
- [Source of `LinearMap.continuous_of_derivation_of_nonUnitalJacobson_eq_bot` in TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Derivation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Derivation.lean#L118)
