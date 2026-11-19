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
- [Source of `TauCeti.SNumbers.IsSNumberSequence` in TauCeti/Analysis/Normed/Operator/SNumbers/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/SNumbers/Basic.lean#L50)
- [Tau Ceti roadmap status: s-numbers and entropy numbers of operators between Banach spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SNumbers/STATUS.md)
