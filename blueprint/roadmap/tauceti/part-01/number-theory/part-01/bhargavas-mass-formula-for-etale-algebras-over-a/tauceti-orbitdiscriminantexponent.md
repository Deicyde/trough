---
declaration: def
origin: cited
lean: TauCeti.orbitDiscriminantExponent
statement: formalized
---

# TauCeti.orbitDiscriminantExponent

The sum of the discriminant exponents of the fixed fields of point stabilizers, one per
orbit. An infinite fixed field contributes zero; infinitely many nonzero summands give a total
of zero.

```lean
TauCeti.orbitDiscriminantExponent.{u_1, u_4} (K : Type u_1) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] (X : Type u_4)
  [MulAction Gal(SeparableClosure K/K) X] : ℕ
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.orbitDiscriminantExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/EtaleMassFormula/OrbitWeight.html#TauCeti.orbitDiscriminantExponent).

## Sources

- [Tau Ceti documentation: `TauCeti.orbitDiscriminantExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/EtaleMassFormula/OrbitWeight.html#TauCeti.orbitDiscriminantExponent)
- [Source of `TauCeti.orbitDiscriminantExponent` in TauCeti/NumberTheory/LocalField/EtaleMassFormula/OrbitWeight.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/EtaleMassFormula/OrbitWeight.lean#L86)
- [Tau Ceti roadmap status: Bhargava's mass formula for étale algebras over a local field](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleMassFormula/STATUS.md)
