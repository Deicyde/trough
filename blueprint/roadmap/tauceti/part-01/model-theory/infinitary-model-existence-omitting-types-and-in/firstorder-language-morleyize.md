---
declaration: abbrev
origin: cited
lean: FirstOrder.Language.morleyize
statement: formalized
---

# FirstOrder.Language.morleyize

The **Morleyization** of `L` by a family `Φ` of tagged formulas: the function symbols of `L`,
and as `n`-ary relation symbols those of `L` together with one symbol `R_φ` for each member
`⟨n, φ⟩` of `Φ`. No closure property of `Φ` is assumed.

It is not built as a `Language.sum` with a relational language, so that its function symbols are
literally those of `L`. It is an abbreviation, as `Language.sum` is: a structure on the
Morleyization is given by cases on the sum type of relation symbols.

```lean
FirstOrder.Language.morleyize.{u, v} (L : FirstOrder.Language)
  (Φ : Set ((n : ℕ) × L.BoundedFormulaω Empty n)) : FirstOrder.Language
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.morleyize`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/Morleyization.html#FirstOrder.Language.morleyize).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.morleyize`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/Morleyization.html#FirstOrder.Language.morleyize)
- [Source of `FirstOrder.Language.morleyize` in TauCeti/ModelTheory/ModelExistence/Morleyization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/ModelExistence/Morleyization.lean#L73)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
