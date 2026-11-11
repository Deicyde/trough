---
declaration: theorem
origin: cited
lean: TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff
statement: formalized
proof: formalized
---

# TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff

For a finite normalization presentation, ordered automorphisms are finite exactly when
each component has finitely many automorphisms fixing all its special points.

```lean
TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8}
  {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  {H : Type u_3} [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {n : WithTop ℕ∞} {ι : Type u_4}
  {Flag : Type u_5} {X : ι → Type u_6} [(i : ι) → TopologicalSpace (X i)]
  [(i : ι) → ChartedSpace H (X i)] {d : TauCeti.NodalGluing.FlagPairData ι Flag X} {N : Type u_7}
  {R : Type u_8} {m : TauCeti.NodalGluing.Marking d (N ⊕ R)} [∀ (i : ι), ConnectedSpace (X i)]
  [Finite ι] [Finite Flag] :
  Finite ↥(TauCeti.NodalGluing.AuxiliaryAut.ordered I n m) ↔
    ∀ (i : ι), Finite ↥(Diffeomorph.fixingSubgroup (m.specialPoints i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/FiniteAutomorphisms.html#TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/FiniteAutomorphisms.html#TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff)
- [Source of `TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/FiniteAutomorphisms.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Curves/NodalGluing/FiniteAutomorphisms.lean#L124)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
