---
declaration: def
origin: cited
lean: TauCeti.Homologous.homotopyEquiv
statement: formalized
---

# Homologous twisting cocycles give homotopy equivalent twisted complexes

for every
differential graded right module `(ℳ, dM)`, the twisted complexes of `mP` and `mQ` are
homotopy equivalent.

```lean
TauCeti.Homologous.homotopyEquiv.{uR, uA, uM, uP} {R : Type uR} {A : Type uA} {M : Type uM}
  [CommRing R] [Ring A] [Algebra R A] [AddCommGroup M] [_root_.Module R M] {P Q : Type uP}
  {ind : P → ℤ} {indQ : Q → ℤ} [Fintype P] [Fintype Q] [_root_.Module Aᵐᵒᵖ M]
  [IsScalarTower R Aᵐᵒᵖ M] [SMulCommClass R Aᵐᵒᵖ M] {𝒜 : ℤ → Submodule R A} [GradedAlgebra 𝒜]
  {d : A →ₗ[R] A} {h : TauCeti.IsDGAlgebra 𝒜 d} {ℳ : ℤ → Submodule R M} [DirectSum.Decomposition ℳ]
  [SetLike.GradedSMul ((TauCeti.InternalGrading.ofDecomposition 𝒜).opposite.piece ℤ) ℳ]
  {dM : M →ₗ[R] M} {mP : TauCeti.TwistingCocycle 𝒜 d P ind}
  {mQ : TauCeti.TwistingCocycle 𝒜 d Q indQ} [DecidableEq P] [DecidableEq Q]
  (H : TauCeti.Homologous h mP mQ) (hM : TauCeti.IsDGRightModule h ℳ dM) :
  HomotopyEquiv (mP.twistedCochainComplex dM hM) (mQ.twistedCochainComplex dM hM)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Homologous.homotopyEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DG/Twisted/Equivalence.html#TauCeti.Homologous.homotopyEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Homologous.homotopyEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DG/Twisted/Equivalence.html#TauCeti.Homologous.homotopyEquiv)
- [Source of `TauCeti.Homologous.homotopyEquiv` in TauCeti/Algebra/Homology/DG/Twisted/Equivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/DG/Twisted/Equivalence.lean#L228)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGFloer/STATUS.md)
