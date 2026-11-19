---
declaration: theorem
origin: cited
lean: TauCeti.DynkinType.span_range_scWeight_eq_top
statement: formalized
proof: formalized
---

# The weights of the full-weight lattice span the weight lattice

the weights carried by the
weight basis span `Fin t.rank → ℤ` over `ℤ`, since the highest weight vector of the `i`-th summand
lies in the lattice with weight the `i`-th standard basis vector. This is the spanning condition
of `TauCeti.GeneralLinear.isClosedImmersion_weightTorus`.

```lean
TauCeti.DynkinType.span_range_scWeight_eq_top (t : TauCeti.DynkinType) (ht : t.Valid) :
  Submodule.span ℤ (Set.range (t.scWeight ht)) = ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy-Schwarz against a majorant](../bilinear-form/cauchy-schwarz-against-a-majorant.md)
- [The rank-one Kostant straightening formula](../../../algebra/part-02/lie/part-02/the-rank-one-kostant-straightening-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.span_range_scWeight_eq_top`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/SimplyConnectedModule/Lattice.html#TauCeti.DynkinType.span_range_scWeight_eq_top).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.span_range_scWeight_eq_top`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/SimplyConnectedModule/Lattice.html#TauCeti.DynkinType.span_range_scWeight_eq_top)
- [Source of `TauCeti.DynkinType.span_range_scWeight_eq_top` in TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/SimplyConnectedModule/Lattice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/SimplyConnectedModule/Lattice.lean#L262)
- [Tau Ceti roadmap status: Chevalley groups and the Chevalley–Demazure group schemes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ChevalleyGroups/STATUS.md)
