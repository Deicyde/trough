---
declaration: theorem
origin: cited
lean: NonUnitalAlgHom.continuous_of_surjective_of_jacobson_eq_bot, NonUnitalAlgHom.continuous_of_surjective_of_nonUnitalJacobson_eq_bot
statement: formalized
proof: formalized
---

# Johnson's theorem

A surjective homomorphism `θ : A → B` of complex Banach algebras, not
assumed continuous, is continuous when `B` is unital with zero Jacobson radical.

```lean
NonUnitalAlgHom.continuous_of_surjective_of_jacobson_eq_bot.{u_1, u_2} {A : Type u_1} {B : Type u_2}
  [NonUnitalNormedRing A] [NormedSpace ℂ A] [IsScalarTower ℂ A A] [SMulCommClass ℂ A A]
  [CompleteSpace A] [NormedRing B] [NormedAlgebra ℂ B] [CompleteSpace B] (θ : A →ₙₐ[ℂ] B)
  (hθ : Function.Surjective ⇑θ) (hB : Ring.jacobson B = ⊥) : Continuous ⇑θ
```

## Depends on

- [TauCeti.nonUnitalJacobson](../../../part-01/banach-algebras/tauceti-nonunitaljacobson.md)

## Proof depends on

- [Gelfand's formula in a nonunital complex Banach algebra](../../../part-01/banach-algebras/gelfands-formula-in-a-nonunital-complex-banach-a.md)
- [LinearMap.continuous_iff_separatingSpace_eq_bot](../../../part-01/banach-algebras/linearmap-continuous-iff-separatingspace-eq-bot.md)
- [LinearMap.separatingSpace](../../../part-01/banach-algebras/linearmap-separatingspace.md)
- [Rickart's scalar-commutant theorem](../../../part-01/one-parameter-semigroups-completely-monotone-and/part-01/rickarts-scalar-commutant-theorem.md)
- [Sinclair's stability lemma](../../../part-01/banach-algebras/sinclairs-stability-lemma.md)

## Lean

Formalized in Tau Ceti as [`NonUnitalAlgHom.continuous_of_surjective_of_jacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Semisimple.html#NonUnitalAlgHom.continuous_of_surjective_of_jacobson_eq_bot).

## Other forms

**Johnson's theorem, nonunital form.** Formalized in Tau Ceti as [`NonUnitalAlgHom.continuous_of_surjective_of_nonUnitalJacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Semisimple.html#NonUnitalAlgHom.continuous_of_surjective_of_nonUnitalJacobson_eq_bot).

```lean
NonUnitalAlgHom.continuous_of_surjective_of_nonUnitalJacobson_eq_bot.{u_1, u_3} {A : Type u_1}
  [NonUnitalNormedRing A] [NormedSpace ℂ A] [IsScalarTower ℂ A A] [SMulCommClass ℂ A A]
  [CompleteSpace A] {B : Type u_3} [NonUnitalNormedRing B] [NormedSpace ℂ B] [IsScalarTower ℂ B B]
  [SMulCommClass ℂ B B] [CompleteSpace B] (θ : A →ₙₐ[ℂ] B) (hθ : Function.Surjective ⇑θ)
  (hB : TauCeti.nonUnitalJacobson ℂ B = ⊥) : Continuous ⇑θ
```

## Sources

- [Tau Ceti documentation: `NonUnitalAlgHom.continuous_of_surjective_of_jacobson_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Semisimple.html#NonUnitalAlgHom.continuous_of_surjective_of_jacobson_eq_bot)
- [Source of `NonUnitalAlgHom.continuous_of_surjective_of_jacobson_eq_bot` in TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Semisimple.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Semisimple.lean#L56)
