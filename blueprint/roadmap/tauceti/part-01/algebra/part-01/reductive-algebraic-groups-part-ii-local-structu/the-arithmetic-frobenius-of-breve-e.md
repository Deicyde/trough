---
declaration: def
origin: cited
lean: TauCeti.MaxUnramifiedCompletion.frobenius
statement: formalized
---

# The arithmetic Frobenius `σ` of `Breve E`

the continuous extension to `Breve E` of the
arithmetic Frobenius of `E^{ur}/E`. It raises every root of every polynomial `X^{q^n} − X` to the
`q`-th power (`frobenius_coe_of_pow_natCard_pow_eq_self`).

```lean
TauCeti.MaxUnramifiedCompletion.frobenius.{u_1} (E : Type u_1) [Field E] [ValuativeRel E]
  [TopologicalSpace E] [IsNonarchimedeanLocalField E] :
  Gal(TauCeti.MaxUnramifiedCompletion.Breve E/E)
```

## Depends on

- [The completed maximal unramified extension `Breve E` of a nonarchimedean local field `E`](the-completed-maximal-unramified-extension-breve.md)
- [TauCeti.algebraicExtensionNormedField](../../../number-theory/part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Proof depends on

- [Dedekind's different theorem, the tame case](../../../number-theory/part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../../number-theory/part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MaxUnramifiedCompletion.frobenius`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Unramified/Completion.html#TauCeti.MaxUnramifiedCompletion.frobenius).

## Sources

- [Tau Ceti documentation: `TauCeti.MaxUnramifiedCompletion.frobenius`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Unramified/Completion.html#TauCeti.MaxUnramifiedCompletion.frobenius)
- [Source of `TauCeti.MaxUnramifiedCompletion.frobenius` in TauCeti/NumberTheory/LocalField/Unramified/Completion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Unramified/Completion.lean#L205)
- [Tau Ceti roadmap status: Reductive algebraic groups, part II — local structure and arithmetic models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroupsPartII/STATUS.md)
