---
declaration: theorem
origin: cited
lean: IntermediateField.inf_maximalUnramifiedExtension
statement: formalized
proof: formalized
---

# IntermediateField.inf_maximalUnramifiedExtension

The unramified part of a finite subextension is the canonical unramified extension of
its residue degree. No normality hypothesis on `L/K` is required.

```lean
IntermediateField.inf_maximalUnramifiedExtension.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] (L : IntermediateField K (SeparableClosure K))
  [Module.Finite K ↥L] :
  L ⊓ TauCeti.maximalUnramifiedExtension K (SeparableClosure K) =
    TauCeti.unramifiedExtension K (SeparableClosure K) L.inertiaDegree
```

## Depends on

- [IntermediateField.inertiaDegree](intermediatefield-inertiadegree.md)

## Proof depends on

- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`IntermediateField.inf_maximalUnramifiedExtension`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Unramified/IntermediateField.html#IntermediateField.inf_maximalUnramifiedExtension).

## Sources

- [Tau Ceti documentation: `IntermediateField.inf_maximalUnramifiedExtension`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Unramified/IntermediateField.html#IntermediateField.inf_maximalUnramifiedExtension)
- [Source of `IntermediateField.inf_maximalUnramifiedExtension` in TauCeti/NumberTheory/LocalField/Unramified/IntermediateField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Unramified/IntermediateField.lean#L141)
- [Tau Ceti roadmap status: Bhargava's mass formula for étale algebras over a local field](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EtaleMassFormula/STATUS.md)
