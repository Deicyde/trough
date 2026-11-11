---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.atWorstNodalOfRelativeDimensionOne_iff_flat_and_fiberToSpecResidueField
statement: formalized
proof: formalized
---

# The fibrewise criterion for nodal curves

A morphism is at worst nodal of relative
dimension one exactly when it is flat and locally of finite presentation and each of its fibres
`f.fiber y ⟶ Spec κ(y)` over a residue field is at worst nodal.

```lean
TauCeti.AlgebraicGeometry.atWorstNodalOfRelativeDimensionOne_iff_flat_and_fiberToSpecResidueField.{u}
  {X Y : AlgebraicGeometry.Scheme} (f : X ⟶ Y) :
  TauCeti.AlgebraicGeometry.AtWorstNodalOfRelativeDimensionOne f ↔
    AlgebraicGeometry.Flat f ∧
      AlgebraicGeometry.LocallyOfFinitePresentation f ∧
        ∀ (y : ↥Y),
          TauCeti.AlgebraicGeometry.AtWorstNodalOfRelativeDimensionOne
            (AlgebraicGeometry.Scheme.Hom.fiberToSpecResidueField f y)
```

## Depends on

- [TauCeti.AlgebraicGeometry.AtWorstNodalOfRelativeDimensionOne](tauceti-algebraicgeometry-atworstnodalofrelative.md)

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.atWorstNodalOfRelativeDimensionOne_iff_flat_and_fiberToSpecResidueField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/Node/Fiber.html#TauCeti.AlgebraicGeometry.atWorstNodalOfRelativeDimensionOne_iff_flat_and_fiberToSpecResidueField).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.atWorstNodalOfRelativeDimensionOne_iff_flat_and_fiberToSpecResidueField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/Node/Fiber.html#TauCeti.AlgebraicGeometry.atWorstNodalOfRelativeDimensionOne_iff_flat_and_fiberToSpecResidueField)
- [Source of `TauCeti.AlgebraicGeometry.atWorstNodalOfRelativeDimensionOne_iff_flat_and_fiberToSpecResidueField` in TauCeti/AlgebraicGeometry/Curves/Node/Fiber.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Curves/Node/Fiber.lean#L157)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StableReduction/STATUS.md)
