---
declaration: def
origin: cited
lean: ContinuousAlgHom.quotientKerEquivOfSurjective
statement: formalized
---

# The continuous first isomorphism theorem for Banach algebras

a continuous surjective
algebra homomorphism `f : A → B` induces an isomorphism of topological algebras
`A ⧸ ker f ≃ B`. Its inverse is continuous by the open mapping theorem; it need not be an
isometry.

```lean
ContinuousAlgHom.quotientKerEquivOfSurjective.{u_1, u_2, u_3} {𝕜 : Type u_1} {A : Type u_2}
  {B : Type u_3} [NontriviallyNormedField 𝕜] [NormedRing A] [NormedAlgebra 𝕜 A] [CompleteSpace A]
  [NormedRing B] [NormedAlgebra 𝕜 B] [CompleteSpace B] (f : A →A[𝕜] B)
  (hf : Function.Surjective ⇑f) : (A ⧸ RingHom.ker f) ≃A[𝕜] B
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousAlgHom.quotientKerEquivOfSurjective`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Ring/Quotient.html#ContinuousAlgHom.quotientKerEquivOfSurjective).

## Sources

- [Tau Ceti documentation: `ContinuousAlgHom.quotientKerEquivOfSurjective`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Ring/Quotient.html#ContinuousAlgHom.quotientKerEquivOfSurjective)
- [Source of `ContinuousAlgHom.quotientKerEquivOfSurjective` in TauCeti/Analysis/Normed/Ring/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Ring/Quotient.lean#L178)
