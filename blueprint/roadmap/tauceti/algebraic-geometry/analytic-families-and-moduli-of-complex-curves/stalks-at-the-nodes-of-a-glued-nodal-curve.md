---
declaration: theorem
origin: cited
lean: TauCeti.NodalGluing.quotientStalkToNode_bijective
statement: formalized
proof: formalized
---

# Stalks at the nodes of a glued nodal curve

At the node of a flag pair, the restrictions
to the two branches identify the stalk of the glued curve with the branch-pair node ring.

```lean
TauCeti.NodalGluing.quotientStalkToNode_bijective.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {H : Type u_2} [TopologicalSpace H]
  (I : ModelWithCorners ℂ E H) {ι : Type} {Flag : Type u_3} {X : ι → Type}
  [(i : ι) → TopologicalSpace (X i)] [(i : ι) → ChartedSpace H (X i)]
  (d : TauCeti.NodalGluing.FlagPairData ι Flag X) [Finite Flag] [∀ (i : ι), T2Space (X i)]
  (f : Flag) :
  Function.Bijective
    ⇑(TauCeti.holomorphicStructureSheaf.quotientStalkToNode I (TauCeti.NodalGluing.gluedRelSetoid d)
        (TauCeti.NodalGluing.fstPoint d f) (TauCeti.NodalGluing.sndPoint d f) ⋯)
```

## Depends on

- [TauCeti.holomorphicStructureSheaf.quotientSheaf](tauceti-holomorphicstructuresheaf-quotientsheaf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.quotientStalkToNode_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/StructureSheaf.html#TauCeti.NodalGluing.quotientStalkToNode_bijective).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.quotientStalkToNode_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/StructureSheaf.html#TauCeti.NodalGluing.quotientStalkToNode_bijective)
- [Source of `TauCeti.NodalGluing.quotientStalkToNode_bijective` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/StructureSheaf.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/NodalGluing/StructureSheaf.lean#L63)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
