---
declaration: def
origin: cited
lean: Matrix.restrictedFamilyPresentationEquiv
statement: formalized
---

# Matrix.restrictedFamilyPresentationEquiv

The cokernel of the unchanged relation matrix is topologically the restricted series
with coefficients in the presented finite Tate module. The source has its quotient topology.

```lean
Matrix.restrictedFamilyPresentationEquiv.{u_1, u_2, u_3, u_5, u_6} {σ : Type u_1} {ι : Type u_2}
  {κ : Type u_3} [Fintype ι] [Fintype κ] {c : σ → ℝ} [∀ (i : σ), Fact (0 < c i)] {τ : Type u_5}
  {K : Type u_6} [NormedField K] [IsUltrametricDist K] [CompleteSpace K] [Finite τ] {d : τ → ℝ}
  [∀ (j : τ), Fact (0 < d j)] (A : Matrix ι κ ↥(MvPowerSeries.IsRestricted.subring d)) :
  ((ι → ↥(MvPowerSeries.IsRestricted.subring c)) ⧸
      (A.map
            ⇑(algebraMap ↥(MvPowerSeries.IsRestricted.subring d)
                ↥(MvPowerSeries.IsRestricted.subring
                    c))).mulVecLin.range) ≃L[↥(MvPowerSeries.IsRestricted.subring c)]
    TauCeti.MvPowerSeries.IsRestrictedFamily.Gauss c
      ((ι → ↥(MvPowerSeries.IsRestricted.subring d)) ⧸ A.mulVecLin.range)
```

## Depends on

- [TauCeti.MvPowerSeries.IsRestrictedFamily](tauceti-mvpowerseries-isrestrictedfamily.md)

## Proof depends on

- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../../part-02/topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)

## Lean

Formalized in Tau Ceti as [`Matrix.restrictedFamilyPresentationEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Presentation.html#Matrix.restrictedFamilyPresentationEquiv).

## Sources

- [Tau Ceti documentation: `Matrix.restrictedFamilyPresentationEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Presentation.html#Matrix.restrictedFamilyPresentationEquiv)
- [Source of `Matrix.restrictedFamilyPresentationEquiv` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Presentation.lean#L325)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
