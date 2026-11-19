---
declaration: def
origin: cited
lean: IntermediateField.inertiaDegree
statement: formalized
---

# IntermediateField.inertiaDegree

The residue degree of a subextension of `SeparableClosure K`, using the canonical
local-field structures when the extension is finite, and zero otherwise.

```lean
IntermediateField.inertiaDegree.{u_1} {K : Type u_1} [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] (L : IntermediateField K (SeparableClosure K)) : ℕ
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`IntermediateField.inertiaDegree`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Unramified/IntermediateField.html#IntermediateField.inertiaDegree).

## Sources

- [Tau Ceti documentation: `IntermediateField.inertiaDegree`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Unramified/IntermediateField.html#IntermediateField.inertiaDegree)
- [Source of `IntermediateField.inertiaDegree` in TauCeti/NumberTheory/LocalField/Unramified/IntermediateField.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/Unramified/IntermediateField.lean#L51)
- [Tau Ceti roadmap status: Bhargava's mass formula for étale algebras over a local field](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleMassFormula/STATUS.md)
