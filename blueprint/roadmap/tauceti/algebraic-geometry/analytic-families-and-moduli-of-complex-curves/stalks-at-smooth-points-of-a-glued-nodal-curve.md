---
declaration: theorem
origin: cited
lean: TauCeti.NodalGluing.quotientStalkBranch_bijective
statement: formalized
proof: formalized
---

# Stalks at smooth points of a glued nodal curve

Away from the flag points, restriction
to the normalization identifies the stalks of the glued curve with the holomorphic stalks of the
normalization.

```lean
TauCeti.NodalGluing.quotientStalkBranch_bijective.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {H : Type u_2} [TopologicalSpace H]
  (I : ModelWithCorners ℂ E H) {ι : Type} {Flag : Type u_3} {X : ι → Type}
  [(i : ι) → TopologicalSpace (X i)] [(i : ι) → ChartedSpace H (X i)]
  (d : TauCeti.NodalGluing.FlagPairData ι Flag X) [Finite Flag] [∀ (i : ι), T1Space (X i)]
  {x : (i : ι) × X i} (hx : x ∉ TauCeti.NodalGluing.flagPointSet d) :
  Function.Bijective
    ⇑(TauCeti.holomorphicStructureSheaf.quotientStalkBranch I (TauCeti.NodalGluing.gluedRelSetoid d)
        ⟦x⟧ x ⋯)
```

## Depends on

- [TauCeti.holomorphicStructureSheaf.quotientSheaf](tauceti-holomorphicstructuresheaf-quotientsheaf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.quotientStalkBranch_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/StructureSheaf.html#TauCeti.NodalGluing.quotientStalkBranch_bijective).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.quotientStalkBranch_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/StructureSheaf.html#TauCeti.NodalGluing.quotientStalkBranch_bijective)
- [Source of `TauCeti.NodalGluing.quotientStalkBranch_bijective` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/StructureSheaf.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/NodalGluing/StructureSheaf.lean#L52)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
