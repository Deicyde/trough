---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.exists_split_singularLocus
statement: formalized
proof: formalized
---

# AlgebraicGeometry.Scheme.exists_split_singularLocus

All nodes of a proper nodal curve split over one finite separable field extension.
For any chosen base change of the curve, its singular subscheme is the spectrum of a
product of copies of the extended field, as a scheme over that field. This includes the
smooth case, in which the node set is empty.

```lean
AlgebraicGeometry.Scheme.exists_split_singularLocus.{u} {K : Type u} [Field K]
  (X : AlgebraicGeometry.Scheme) [X.Over (AlgebraicGeometry.Spec ↧K)]
  [AlgebraicGeometry.IsProper (X ↘ AlgebraicGeometry.Spec ↧K)]
  (hnodal :
    TauCeti.AlgebraicGeometry.AtWorstNodalOfRelativeDimensionOne (X ↘ AlgebraicGeometry.Spec ↧K)) :
  ∃ L x x_1,
    ∃ (_ : Module.Finite K L) (_ : Algebra.IsSeparable K L),
      ∃ n,
        ∀ (X' : AlgebraicGeometry.Scheme) (x_4 : X'.Over (AlgebraicGeometry.Spec ↧L)) (g : X' ⟶ X)
          (H :
            CategoryTheory.IsPullback g (X' ↘ AlgebraicGeometry.Spec ↧L)
              (X ↘ AlgebraicGeometry.Spec ↧K) (AlgebraicGeometry.Spec.algebraMap K L)),
          Nonempty
            (CategoryTheory.Over.mk
                (CategoryTheory.CategoryStruct.comp
                  (AlgebraicGeometry.Scheme.singularLocus L X').subschemeι
                  (X' ↘ AlgebraicGeometry.Spec ↧L)) ≅
              CategoryTheory.Over.mk (AlgebraicGeometry.Spec.algebraMap L (Fin n → L)))
```

## Depends on

- [TauCeti.AlgebraicGeometry.AtWorstNodalOfRelativeDimensionOne](tauceti-algebraicgeometry-atworstnodalofrelative.md)

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.exists_split_singularLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/Node/Splitting.html#AlgebraicGeometry.Scheme.exists_split_singularLocus).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.exists_split_singularLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/Node/Splitting.html#AlgebraicGeometry.Scheme.exists_split_singularLocus)
- [Source of `AlgebraicGeometry.Scheme.exists_split_singularLocus` in TauCeti/AlgebraicGeometry/Curves/Node/Splitting.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/Node/Splitting.lean#L37)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StableReduction/STATUS.md)
