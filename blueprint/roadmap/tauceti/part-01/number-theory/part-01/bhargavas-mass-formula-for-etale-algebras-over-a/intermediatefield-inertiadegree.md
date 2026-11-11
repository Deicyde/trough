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
- [Source of `IntermediateField.inertiaDegree` in TauCeti/NumberTheory/LocalField/Unramified/IntermediateField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Unramified/IntermediateField.lean#L48)
- [Tau Ceti roadmap status: Bhargava's mass formula for étale algebras over a local field](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EtaleMassFormula/STATUS.md)
