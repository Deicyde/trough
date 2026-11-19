---
declaration: structure
origin: cited
lean: TauCeti.SNumbers.IsStrictSNumberSequence
statement: formalized
---

# TauCeti.SNumbers.IsStrictSNumberSequence

A strict s-number sequence is normalized on the identity of every normed space at
all indices strictly below its cardinal dimension, including infinite dimension
(Ullrich 2024, Remark 1).

```lean
TauCeti.SNumbers.IsStrictSNumberSequence.{u} {𝕜 : Type u} [NontriviallyNormedField 𝕜]
  (s : TauCeti.SNumbers.SNumberFamily 𝕜) : Prop
```

## Depends on

- [TauCeti.SNumbers.IsSNumberSequence](tauceti-snumbers-issnumbersequence.md)
- [TauCeti.SNumbers.SNumberFamily](tauceti-snumbers-snumberfamily.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SNumbers.IsStrictSNumberSequence`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SNumbers/Basic.html#TauCeti.SNumbers.IsStrictSNumberSequence).

## Sources

- [Tau Ceti documentation: `TauCeti.SNumbers.IsStrictSNumberSequence`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SNumbers/Basic.html#TauCeti.SNumbers.IsStrictSNumberSequence)
- [Source of `TauCeti.SNumbers.IsStrictSNumberSequence` in TauCeti/Analysis/Normed/Operator/SNumbers/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/SNumbers/Basic.lean#L76)
- [Tau Ceti roadmap status: s-numbers and entropy numbers of operators between Banach spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SNumbers/STATUS.md)
