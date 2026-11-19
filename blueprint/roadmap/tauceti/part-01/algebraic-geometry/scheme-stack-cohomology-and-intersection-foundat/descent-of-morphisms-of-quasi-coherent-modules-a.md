---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.Descent.qcohPseudofunctor_isPrestack_fpqcTopology
statement: formalized
proof: formalized
---

# Descent of morphisms of quasi-coherent modules along fpqc coverings

The pseudofunctor
`T ↦ QCoh(T)` is a prestack for the fpqc topology: for an fpqc covering of `S`, morphisms of
quasi-coherent modules on `S` are the families of morphisms between their pullbacks to the members
of the covering which agree on the overlaps.

```lean
TauCeti.AlgebraicGeometry.Descent.qcohPseudofunctor_isPrestack_fpqcTopology.{u} :
  CategoryTheory.Pseudofunctor.IsPrestack TauCeti.AlgebraicGeometry.Descent.qcohPseudofunctor
    AlgebraicGeometry.Scheme.fpqcTopology
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.Descent.qcohPseudofunctor_isPrestack_fpqcTopology`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Descent/QuasicoherentSheaf/Prestack.html#TauCeti.AlgebraicGeometry.Descent.qcohPseudofunctor_isPrestack_fpqcTopology).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.Descent.qcohPseudofunctor_isPrestack_fpqcTopology`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Descent/QuasicoherentSheaf/Prestack.html#TauCeti.AlgebraicGeometry.Descent.qcohPseudofunctor_isPrestack_fpqcTopology)
- [Source of `TauCeti.AlgebraicGeometry.Descent.qcohPseudofunctor_isPrestack_fpqcTopology` in TauCeti/AlgebraicGeometry/Descent/QuasicoherentSheaf/Prestack.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Descent/QuasicoherentSheaf/Prestack.lean#L300)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
