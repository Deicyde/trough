---
declaration: theorem
origin: cited
lean: IsSimpleModule.algebraMap_end_bijective_of_completeSpace, LinearMap.existsUnique_eq_smul_of_isSimpleModule
statement: formalized
proof: formalized
---

# Rickart's scalar-commutant theorem

the scalar map from the complex numbers
to the algebraic endomorphism ring of a simple Banach module is bijective.

```lean
IsSimpleModule.algebraMap_end_bijective_of_completeSpace.{u_1, u_2} {A : Type u_1} {E : Type u_2}
  [NormedRing A] [NormedAlgebra ℂ A] [CompleteSpace A] [NormedAddCommGroup E] [NormedSpace ℂ E]
  [CompleteSpace E] [_root_.Module A E] [IsScalarTower ℂ A E] [ContinuousSMul A E]
  [IsSimpleModule A E] : Function.Bijective ⇑(algebraMap ℂ (Module.End A E))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsSimpleModule.algebraMap_end_bijective_of_completeSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Simple.html#IsSimpleModule.algebraMap_end_bijective_of_completeSpace).

## Other forms

**Rickart's scalar-commutant theorem.** Formalized in Tau Ceti as [`LinearMap.existsUnique_eq_smul_of_isSimpleModule`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Simple.html#LinearMap.existsUnique_eq_smul_of_isSimpleModule).

```lean
LinearMap.existsUnique_eq_smul_of_isSimpleModule.{u_1, u_2} {A : Type u_1} {E : Type u_2}
  [NormedRing A] [NormedAlgebra ℂ A] [CompleteSpace A] [NormedAddCommGroup E] [NormedSpace ℂ E]
  [CompleteSpace E] [_root_.Module A E] [IsScalarTower ℂ A E] [ContinuousSMul A E]
  [IsSimpleModule A E] (f : E →ₗ[A] E) : ∃! c, ∀ (x : E), f x = c • x
```

## Sources

- [Tau Ceti documentation: `IsSimpleModule.algebraMap_end_bijective_of_completeSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Simple.html#IsSimpleModule.algebraMap_end_bijective_of_completeSpace)
- [Source of `IsSimpleModule.algebraMap_end_bijective_of_completeSpace` in TauCeti/Analysis/Normed/Module/Simple.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/Simple.lean#L132)
