---
declaration: def
origin: cited
lean: TauCeti.DynkinType.scToralDiagramAut
statement: formalized
---

# TauCeti.DynkinType.scToralDiagramAut

The diagram automorphism of the integral toral closure in the full-weight representation.
It descends the lattice automorphism `scModuleDiagramEquiv`, using preservation of weight
components rather than a monomial action on the weight basis.

```lean
TauCeti.DynkinType.scToralDiagramAut {t : TauCeti.DynkinType} (ht : t.Valid)
  {σ : Equiv.Perm (Fin t.rank)} (hσ : σ ∈ t.diagramSymmetry) :
  CategoryTheory.Aut
    (TauCeti.UniversalEnvelopingAlgebra.kostantToralGroupScheme (t.lieBasis ht).rootGenerator
      (t.lieBasis ht).h
      (TauCeti.UniversalEnvelopingAlgebra.representation ℚ (↥(t.lieAlgebra ht)) (t.scModule ht))
      (t.scLattice ht).toAddSubgroup ⋯ ⋯ (t.scWeightBasis ht) (t.scWeight ht))
```

## Depends on

- [The diagram symmetry `θ_σ` of the full-weight module `V_sc(t) = ⨁ᵢ L(ϖᵢ)`](the-diagram-symmetry-of-the-full-weight-module-v.md)

## Proof depends on

- [Cauchy-Schwarz against a majorant](../bilinear-form/cauchy-schwarz-against-a-majorant.md)
- [The rank-one Kostant straightening formula](../../../algebra/part-02/lie/part-02/the-rank-one-kostant-straightening-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.scToralDiagramAut`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/DiagramAutomorphism/ToralClosure.html#TauCeti.DynkinType.scToralDiagramAut).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.scToralDiagramAut`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/DiagramAutomorphism/ToralClosure.html#TauCeti.DynkinType.scToralDiagramAut)
- [Source of `TauCeti.DynkinType.scToralDiagramAut` in TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/DiagramAutomorphism/ToralClosure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/DiagramAutomorphism/ToralClosure.lean#L282)
- [Tau Ceti roadmap status: Chevalley groups and the Chevalley–Demazure group schemes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ChevalleyGroups/STATUS.md)
