---
declaration: def
origin: cited
lean: TauCeti.NodalGluing.AuxiliaryMarkedCurve.partitionedAuxiliaryIsomorphismGroupoid
statement: formalized
---

# The groupoid of curves with partitioned auxiliary marks

For a colouring `κ : R → Cl` of
the auxiliary labels, this is the subgroupoid of the groupoid of curves with unordered auxiliary
marks consisting of the colour-preserving arrows `(π, f)`, those whose permutation `π` lies in
`∏_c S(κ ⁻¹' {c})`.  It is wide (`isWide_partitionedAuxiliaryIsomorphismGroupoid`): it has the
same objects, but in general fewer arrows between them.

```lean
TauCeti.NodalGluing.AuxiliaryMarkedCurve.partitionedAuxiliaryIsomorphismGroupoid.{u, v, w, u_1, u_2,
    u_3, u_13, u_14, u_15}
  {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  {H : Type u_3} [TopologicalSpace H] (I : ModelWithCorners 𝕜 E H) (n : WithTop ℕ∞) (N : Type u_13)
  {R : Type u_14} {Cl : Type u_15} (κ : R → Cl) :
  CategoryTheory.Subgroupoid (TauCeti.NodalGluing.AuxiliaryMarkedCurve I n N R)
```

## Depends on

- [An isomorphism of nodal curves presented by flag-pair data](an-isomorphism-of-nodal-curves-presented-by-flag.md)
- [The groupoid of curves with unordered auxiliary marks](the-groupoid-of-curves-with-unordered-auxiliary.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.AuxiliaryMarkedCurve.partitionedAuxiliaryIsomorphismGroupoid`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/PartitionedAuxiliaryMarks.html#TauCeti.NodalGluing.AuxiliaryMarkedCurve.partitionedAuxiliaryIsomorphismGroupoid).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.AuxiliaryMarkedCurve.partitionedAuxiliaryIsomorphismGroupoid`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/PartitionedAuxiliaryMarks.html#TauCeti.NodalGluing.AuxiliaryMarkedCurve.partitionedAuxiliaryIsomorphismGroupoid)
- [Source of `TauCeti.NodalGluing.AuxiliaryMarkedCurve.partitionedAuxiliaryIsomorphismGroupoid` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/PartitionedAuxiliaryMarks.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/NodalGluing/PartitionedAuxiliaryMarks.lean#L190)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
