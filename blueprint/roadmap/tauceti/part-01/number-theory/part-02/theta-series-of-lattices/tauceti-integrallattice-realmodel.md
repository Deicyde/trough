---
declaration: def
origin: cited
lean: TauCeti.IntegralLattice.realModel
statement: formalized
---

# TauCeti.IntegralLattice.realModel

The **real model** of a positive definite integral lattice `M`: the image `1 ⊗ M` of its
carrier in the Euclidean space `ℝ ⊗[ℚ] V`.

```lean
TauCeti.IntegralLattice.realModel.{u_1} {V : Type u_1} [AddCommGroup V] [_root_.Module ℚ V]
  (M : TauCeti.IntegralLattice V) (hM : M.IsPosDef) : Submodule ℤ (M.RealModelSpace hM)
```

## Depends on

- [TauCeti.IntegralLattice](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.realModel`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/RealModel.html#TauCeti.IntegralLattice.realModel).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.realModel`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/RealModel.html#TauCeti.IntegralLattice.realModel)
- [Source of `TauCeti.IntegralLattice.realModel` in TauCeti/Algebra/Module/ZLattice/RealModel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/ZLattice/RealModel.lean#L184)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ThetaSeries/STATUS.md)
