---
declaration: def
origin: cited
lean: TauCeti.LieModule.Cohomology.cochainComplex
statement: formalized
---

# TauCeti.LieModule.Cohomology.cochainComplex

The Chevalley–Eilenberg cochain complex of `L` with coefficients in `M`, whose degree `n`
term is the module of alternating maps `L [⋀^Fin n]→ₗ[R] M`.

```lean
TauCeti.LieModule.Cohomology.cochainComplex.{u_1, u_2, u_3} (R : Type u_1) [CommRing R]
  (L : Type u_2) [LieRing L] [LieAlgebra R L] (M : Type u_3) [AddCommGroup M] [_root_.Module R M]
  [LieRingModule L M] [LieModule R L M] : CochainComplex (ModuleCat R) ℕ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.LieModule.Cohomology.d_d](tauceti-liemodule-cohomology-d-d.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LieModule.Cohomology.cochainComplex`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.html#TauCeti.LieModule.Cohomology.cochainComplex).

## Sources

- [Tau Ceti documentation: `TauCeti.LieModule.Cohomology.cochainComplex`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.html#TauCeti.LieModule.Cohomology.cochainComplex)
- [Source of `TauCeti.LieModule.Cohomology.cochainComplex` in TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.lean#L281)
- [Tau Ceti roadmap status: Lie algebroids, Lie groupoids and Poisson geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LieGroupoidsPoisson/STATUS.md)
