---
declaration: theorem
origin: cited
lean: LinearMap.existsUnique_eq_smul_of_isSimpleModule, IsSimpleModule.algebraMap_end_bijective_of_completeSpace
statement: formalized
proof: formalized
---

# Rickart's scalar-commutant theorem

every algebraic endomorphism of a
simple complex Banach module is multiplication by a unique complex scalar.

```lean
LinearMap.existsUnique_eq_smul_of_isSimpleModule.{u_1, u_2} {A : Type u_1} {E : Type u_2}
  [NormedRing A] [NormedAlgebra ℂ A] [CompleteSpace A] [NormedAddCommGroup E] [NormedSpace ℂ E]
  [CompleteSpace E] [_root_.Module A E] [IsScalarTower ℂ A E] [ContinuousSMul A E]
  [IsSimpleModule A E] (f : E →ₗ[A] E) : ∃! c, ∀ (x : E), f x = c • x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.existsUnique_eq_smul_of_isSimpleModule`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Simple.html#LinearMap.existsUnique_eq_smul_of_isSimpleModule).

## Other forms

**Rickart's scalar-commutant theorem.** Formalized in Tau Ceti as [`IsSimpleModule.algebraMap_end_bijective_of_completeSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Simple.html#IsSimpleModule.algebraMap_end_bijective_of_completeSpace).

```lean
IsSimpleModule.algebraMap_end_bijective_of_completeSpace.{u_1, u_2} {A : Type u_1} {E : Type u_2}
  [NormedRing A] [NormedAlgebra ℂ A] [CompleteSpace A] [NormedAddCommGroup E] [NormedSpace ℂ E]
  [CompleteSpace E] [_root_.Module A E] [IsScalarTower ℂ A E] [ContinuousSMul A E]
  [IsSimpleModule A E] : Function.Bijective ⇑(algebraMap ℂ (Module.End A E))
```

## Sources

- [Tau Ceti documentation: `LinearMap.existsUnique_eq_smul_of_isSimpleModule`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Simple.html#LinearMap.existsUnique_eq_smul_of_isSimpleModule)
- [Source of `LinearMap.existsUnique_eq_smul_of_isSimpleModule` in TauCeti/Analysis/Normed/Module/Simple.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/Simple.lean#L97)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachAlgebras/STATUS.md)
