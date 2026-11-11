---
declaration: def
origin: cited
lean: ZLattice.ratModel
statement: formalized
---

# ZLattice.ratModel

The **rational model** of an integral full lattice `L`: the integral lattice in `ℚ ⊗[ℤ] L`
obtained by rationalizing the integer-valued inner product of `L`.

```lean
ZLattice.ratModel.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  {L : Submodule ℤ E} [FiniteDimensional ℝ E] [DiscreteTopology ↥L] [IsZLattice ℝ L]
  (hL : ZLattice.IsIntegral L) : TauCeti.IntegralLattice (TensorProduct ℤ ℚ ↥L)
```

## Depends on

- [TauCeti.IntegralLattice](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.ratModel`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/RationalModel.html#ZLattice.ratModel).

## Sources

- [Tau Ceti documentation: `ZLattice.ratModel`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/RationalModel.html#ZLattice.ratModel)
- [Source of `ZLattice.ratModel` in TauCeti/Algebra/Module/ZLattice/RationalModel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/ZLattice/RationalModel.lean#L118)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ThetaSeries/STATUS.md)
