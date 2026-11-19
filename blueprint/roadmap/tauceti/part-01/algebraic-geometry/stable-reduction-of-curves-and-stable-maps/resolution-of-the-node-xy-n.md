---
declaration: theorem
origin: cited
lean: TauCeti.NodeAlgebra.exists_resolution
statement: formalized
proof: formalized
---

# Resolution of the node `xy = πⁿ`

Let `π` be a uniformizer of a discrete valuation ring
`R`. For every `n` there is a proper morphism `f : Y ⟶ Spec R[x, y] ⧸ (xy - πⁿ)` such that

* `f` is an isomorphism over the open `D(x) ∪ D(y)`, the complement of `V(x, y)`; for `n ≥ 1`
  this closed subset is the single point `(π, x, y)`, the node of the special fibre;
* `Y` is a regular scheme;
* `Y` is at worst nodal of relative dimension one over `Spec R`.

```lean
TauCeti.NodeAlgebra.exists_resolution.{u} {R : Type u} [CommRing R] {π : R} [IsDomain R]
  [IsDiscreteValuationRing R] (hπ : Irreducible π) (n : ℕ) :
  ∃ Y f,
    AlgebraicGeometry.IsProper f ∧
      CategoryTheory.IsIso
          (f ∣_ ⨆ i, PrimeSpectrum.basicOpen (TauCeti.NodeAlgebra.coord (π ^ n) i)) ∧
        TauCeti.AlgebraicGeometry.IsRegular Y ∧
          TauCeti.AlgebraicGeometry.AtWorstNodalOfRelativeDimensionOne
            (CategoryTheory.CategoryStruct.comp f
              (AlgebraicGeometry.Spec.map
                (CommRingCat.ofHom (algebraMap R (TauCeti.NodeAlgebra R (π ^ n))))))
```

## Depends on

- [TauCeti.AlgebraicGeometry.AtWorstNodalOfRelativeDimensionOne](tauceti-algebraicgeometry-atworstnodalofrelative.md)

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NodeAlgebra.exists_resolution`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/Node/Resolution.html#TauCeti.NodeAlgebra.exists_resolution).

## Sources

- [Tau Ceti documentation: `TauCeti.NodeAlgebra.exists_resolution`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/Node/Resolution.html#TauCeti.NodeAlgebra.exists_resolution)
- [Source of `TauCeti.NodeAlgebra.exists_resolution` in TauCeti/AlgebraicGeometry/Curves/Node/Resolution.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Curves/Node/Resolution.lean#L163)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StableReduction/STATUS.md)
