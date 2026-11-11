---
declaration: theorem
origin: cited
lean: TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff_forall_specialPoints_nonempty_of_complexTorus
statement: formalized
proof: formalized
---

# Stability of elliptic curves

If every normalization component is biholomorphic to a
one-dimensional complex torus, the marked nodal curve has finitely many automorphisms fixing
every label exactly when every component carries a special point.

```lean
TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff_forall_specialPoints_nonempty_of_complexTorus.{u_1,
    u_2, u_3, u_4, u_5, u_6, u_7}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℂ E H} {n : WithTop ℕ∞} {ι : Type u_3} {Flag : Type u_4} {X : ι → Type u_5}
  [(i : ι) → TopologicalSpace (X i)] [(i : ι) → ChartedSpace H (X i)]
  {d : TauCeti.NodalGluing.FlagPairData ι Flag X} {N : Type u_6} {R : Type u_7}
  {m : TauCeti.NodalGluing.Marking d (N ⊕ R)} [Finite ι] [Finite Flag] {L : ι → Submodule ℤ ℂ}
  [∀ (i : ι), DiscreteTopology ↥(L i)] [∀ (i : ι), IsZLattice ℝ (L i)]
  (e :
    (i : ι) →
      Diffeomorph I (modelWithCornersSelf ℂ ℂ) (X i) (AddAction.orbitRel.Quotient ↥(L i) ℂ) n)
  (hn : n ≠ 0) :
  Finite ↥(TauCeti.NodalGluing.AuxiliaryAut.ordered I n m) ↔ ∀ (i : ι), (m.specialPoints i).Nonempty
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff](tauceti-nodalgluing-auxiliaryaut-finite-ordered.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff_forall_specialPoints_nonempty_of_complexTorus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/FiniteAutomorphisms.html#TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff_forall_specialPoints_nonempty_of_complexTorus).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff_forall_specialPoints_nonempty_of_complexTorus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/FiniteAutomorphisms.html#TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff_forall_specialPoints_nonempty_of_complexTorus)
- [Source of `TauCeti.NodalGluing.AuxiliaryAut.finite_ordered_iff_forall_specialPoints_nonempty_of_complexTorus` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/FiniteAutomorphisms.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Curves/NodalGluing/FiniteAutomorphisms.lean#L186)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
