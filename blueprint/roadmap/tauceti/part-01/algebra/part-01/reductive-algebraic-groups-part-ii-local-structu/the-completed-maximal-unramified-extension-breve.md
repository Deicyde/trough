---
declaration: abbrev
origin: cited
lean: TauCeti.MaxUnramifiedCompletion.Breve
statement: formalized
---

# The completed maximal unramified extension `Breve E` of a nonarchimedean local field `E`

the uniform completion of `E^{ur}` for its spectral norm. It is a complete valued field
(`UniformSpace.Completion.valuativeRel`, `UniformSpace.Completion.isValuativeTopology`) and an
algebra over `E` and over `E^{ur}`, the latter embedding densely
(`UniformSpace.Completion.denseRange_coe`).

```lean
TauCeti.MaxUnramifiedCompletion.Breve.{u_1} (E : Type u_1) [Field E] [ValuativeRel E]
  [TopologicalSpace E] [IsNonarchimedeanLocalField E] : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](../../../number-theory/part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MaxUnramifiedCompletion.Breve`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Unramified/Completion.html#TauCeti.MaxUnramifiedCompletion.Breve).

## Sources

- [Tau Ceti documentation: `TauCeti.MaxUnramifiedCompletion.Breve`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Unramified/Completion.html#TauCeti.MaxUnramifiedCompletion.Breve)
- [Source of `TauCeti.MaxUnramifiedCompletion.Breve` in TauCeti/NumberTheory/LocalField/Unramified/Completion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Unramified/Completion.lean#L131)
- [Tau Ceti roadmap status: Reductive algebraic groups, part II — local structure and arithmetic models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroupsPartII/STATUS.md)
