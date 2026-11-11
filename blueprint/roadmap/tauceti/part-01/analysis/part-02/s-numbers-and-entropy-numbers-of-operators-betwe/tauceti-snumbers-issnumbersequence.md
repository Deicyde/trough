---
declaration: structure
origin: cited
lean: TauCeti.SNumbers.IsSNumberSequence
statement: formalized
---

# TauCeti.SNumbers.IsSNumberSequence

Pietsch's five s-number axioms, with zero-based indexing and Euclidean normalization.
The norm and monotonicity clauses together constitute the first axiom.

```lean
TauCeti.SNumbers.IsSNumberSequence.{u} {𝕜 : Type u} [NontriviallyNormedField 𝕜]
  (s : TauCeti.SNumbers.SNumberFamily 𝕜) : Prop
```

## Depends on

- [TauCeti.SNumbers.SNumberFamily](tauceti-snumbers-snumberfamily.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SNumbers.IsSNumberSequence`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SNumbers/Basic.html#TauCeti.SNumbers.IsSNumberSequence).

## Sources

- [Tau Ceti documentation: `TauCeti.SNumbers.IsSNumberSequence`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SNumbers/Basic.html#TauCeti.SNumbers.IsSNumberSequence)
- [Source of `TauCeti.SNumbers.IsSNumberSequence` in TauCeti/Analysis/Normed/Operator/SNumbers/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/SNumbers/Basic.lean#L50)
- [Tau Ceti roadmap status: s-numbers and entropy numbers of operators between Banach spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SNumbers/STATUS.md)
