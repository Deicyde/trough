---
declaration: def
origin: cited
lean: TauCeti.dgYonedaIso, TauCeti.dgYonedaCochainEquiv, TauCeti.dgYonedaHomEquiv
statement: formalized
---

# The differential graded Yoneda lemma

the Hom complex out of the free rank-one right
module is the underlying cochain complex of `M`.

```lean
TauCeti.dgYonedaIso.{uR, uA, uM} {R : Type uR} {A : Type uA} {M : Type (max uA uM)} [CommRing R]
  [Ring A] [Algebra R A] [AddCommGroup M] [_root_.Module R M] [_root_.Module Aᵐᵒᵖ M]
  [IsScalarTower R Aᵐᵒᵖ M] {𝒜 : ℤ → Submodule R A} [GradedAlgebra 𝒜] {d : A →ₗ[R] A}
  {h : TauCeti.IsDGAlgebra 𝒜 d} {ℳ : ℤ → Submodule R M}
  [SetLike.GradedSMul ((TauCeti.InternalGrading.ofDecomposition 𝒜).opposite.piece ℤ) ℳ]
  [DirectSum.Decomposition ℳ] {dM : M →ₗ[R] M} (hM : TauCeti.IsDGRightModule h ℳ dM) :
  TauCeti.dgRightModuleHomComplex ⋯ hM ≅ TauCeti.gradedCochainComplex ℳ dM ⋯ ⋯
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.dgYonedaIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DG/Module/Right/Yoneda.html#TauCeti.dgYonedaIso).

## Other forms

**The differential graded Yoneda lemma, degreewise.** Formalized in Tau Ceti as [`TauCeti.dgYonedaCochainEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DG/Module/Right/Yoneda.html#TauCeti.dgYonedaCochainEquiv).

```lean
TauCeti.dgYonedaCochainEquiv.{uR, uA, uM} {R : Type uR} {A : Type uA} {M : Type uM} [CommRing R]
  [Ring A] [Algebra R A] [AddCommGroup M] [_root_.Module R M] [_root_.Module Aᵐᵒᵖ M]
  [IsScalarTower R Aᵐᵒᵖ M] {𝒜 : ℤ → Submodule R A} [GradedAlgebra 𝒜] {ℳ : ℤ → Submodule R M}
  [SetLike.GradedSMul ((TauCeti.InternalGrading.ofDecomposition 𝒜).opposite.piece ℤ) ℳ] (p : ℤ) :
  ↥(TauCeti.dgRightModuleCochains p) ≃ₗ[R] ↥(ℳ p)
```

**The differential graded Yoneda lemma in degree zero.** Formalized in Tau Ceti as [`TauCeti.dgYonedaHomEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DG/Module/Right/Yoneda.html#TauCeti.dgYonedaHomEquiv).

```lean
TauCeti.dgYonedaHomEquiv.{uR, uA, uM} {R : Type uR} {A : Type uA} {M : Type uM} [CommRing R]
  [Ring A] [Algebra R A] [AddCommGroup M] [_root_.Module R M] [_root_.Module Aᵐᵒᵖ M]
  [IsScalarTower R Aᵐᵒᵖ M] {𝒜 : ℤ → Submodule R A} [GradedAlgebra 𝒜] {d : A →ₗ[R] A}
  {h : TauCeti.IsDGAlgebra 𝒜 d} {ℳ : ℤ → Submodule R M}
  [SetLike.GradedSMul ((TauCeti.InternalGrading.ofDecomposition 𝒜).opposite.piece ℤ) ℳ]
  [DirectSum.Decomposition ℳ] {dM : M →ₗ[R] M} (hM : TauCeti.IsDGRightModule h ℳ dM) :
  TauCeti.DGRightModuleHom ⋯ hM ≃ₗ[R] ↥(hM.cyclesDeg 0)
```

## Sources

- [Tau Ceti documentation: `TauCeti.dgYonedaIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DG/Module/Right/Yoneda.html#TauCeti.dgYonedaIso)
- [Source of `TauCeti.dgYonedaIso` in TauCeti/Algebra/Homology/DG/Module/Right/Yoneda.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/DG/Module/Right/Yoneda.lean#L186)
