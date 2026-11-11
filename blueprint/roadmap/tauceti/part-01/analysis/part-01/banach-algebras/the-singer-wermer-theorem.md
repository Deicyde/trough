---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.apply_mem_nonUnitalJacobson_of_derivation, ContinuousLinearMap.apply_mem_jacobson_of_derivation
statement: formalized
proof: formalized
---

# The Singer–Wermer theorem

A bounded derivation `D` of a commutative complex Banach
algebra, possibly without unit, takes values in the Jacobson radical.

```lean
ContinuousLinearMap.apply_mem_nonUnitalJacobson_of_derivation.{u_1} {B : Type u_1}
  [NonUnitalNormedCommRing B] [NormedSpace ℂ B] [IsScalarTower ℂ B B] [SMulCommClass ℂ B B]
  [CompleteSpace B] (D : B →L[ℂ] B) (hD : ∀ (x y : B), D (x * y) = x * D y + D x * y) (a : B) :
  D a ∈ TauCeti.nonUnitalJacobson ℂ B
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.apply_mem_nonUnitalJacobson_of_derivation`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/Derivation/SingerWermer.html#ContinuousLinearMap.apply_mem_nonUnitalJacobson_of_derivation).

## Other forms

**The Singer–Wermer theorem, unital form.** Formalized in Tau Ceti as [`ContinuousLinearMap.apply_mem_jacobson_of_derivation`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/Derivation/SingerWermer.html#ContinuousLinearMap.apply_mem_jacobson_of_derivation).

```lean
ContinuousLinearMap.apply_mem_jacobson_of_derivation.{u_2} {A : Type u_2} [NormedCommRing A]
  [NormedAlgebra ℂ A] [CompleteSpace A] (D : A →L[ℂ] A)
  (hD : ∀ (x y : A), D (x * y) = x * D y + D x * y) (a : A) : D a ∈ Ring.jacobson A
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.apply_mem_nonUnitalJacobson_of_derivation`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/Derivation/SingerWermer.html#ContinuousLinearMap.apply_mem_nonUnitalJacobson_of_derivation)
- [Source of `ContinuousLinearMap.apply_mem_nonUnitalJacobson_of_derivation` in TauCeti/Analysis/Normed/Algebra/Derivation/SingerWermer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Algebra/Derivation/SingerWermer.lean#L92)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachAlgebras/STATUS.md)
