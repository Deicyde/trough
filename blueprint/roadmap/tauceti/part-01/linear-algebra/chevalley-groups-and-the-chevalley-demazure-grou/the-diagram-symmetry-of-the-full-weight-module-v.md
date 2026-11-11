---
declaration: def
origin: cited
lean: TauCeti.DynkinType.scModuleDiagramEquiv
statement: formalized
---

# The diagram symmetry `θ_σ` of the full-weight module `V_sc(t) = ⨁ᵢ L(ϖᵢ)`

the
automorphism mapping the `i`-th summand to the `σ i`-th one by
`TauCeti.DynkinType.fundamentalModuleDiagramEquiv`. It carries the action of each `x` to the
action of its image under the diagram automorphism `TauCeti.DynkinType.diagramLieEquiv`.

```lean
TauCeti.DynkinType.scModuleDiagramEquiv {t : TauCeti.DynkinType} (ht : t.Valid)
  {σ : Equiv.Perm (Fin t.rank)} (hσ : σ ∈ t.diagramSymmetry) : t.scModule ht ≃ₗ[ℚ] t.scModule ht
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.scModuleDiagramEquiv`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/DiagramAutomorphism/Module.html#TauCeti.DynkinType.scModuleDiagramEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.scModuleDiagramEquiv`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/DiagramAutomorphism/Module.html#TauCeti.DynkinType.scModuleDiagramEquiv)
- [Source of `TauCeti.DynkinType.scModuleDiagramEquiv` in TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/DiagramAutomorphism/Module.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/DiagramAutomorphism/Module.lean#L335)
- [Tau Ceti roadmap status: Chevalley groups and the Chevalley–Demazure group schemes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ChevalleyGroups/STATUS.md)
