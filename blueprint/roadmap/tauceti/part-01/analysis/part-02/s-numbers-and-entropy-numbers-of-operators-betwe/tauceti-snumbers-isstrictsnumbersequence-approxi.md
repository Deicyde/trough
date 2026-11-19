---
declaration: theorem
origin: cited
lean: TauCeti.SNumbers.isStrictSNumberSequence_approximation
statement: formalized
proof: formalized
---

# TauCeti.SNumbers.isStrictSNumberSequence_approximation

Approximation numbers are strict: every identity is normalized below the dimension.
No completeness assumption on the field or the space is needed.

```lean
TauCeti.SNumbers.isStrictSNumberSequence_approximation.{u} {𝕜 : Type u}
  [NontriviallyNormedField 𝕜] :
  TauCeti.SNumbers.IsStrictSNumberSequence
    fun {X Y} [NormedAddCommGroup X] [NormedSpace 𝕜 X] [NormedAddCommGroup Y] [NormedSpace 𝕜 Y] =>
    TauCeti.SNumbers.approximation
```

## Depends on

- [TauCeti.SNumbers.IsStrictSNumberSequence](tauceti-snumbers-isstrictsnumbersequence.md)
- [TauCeti.SNumbers.SNumberFamily](tauceti-snumbers-snumberfamily.md)

## Proof depends on

- [TauCeti.SNumbers.IsStrictSNumberSequence.of_normalize_of_lt_rank](tauceti-snumbers-isstrictsnumbersequence-of-norm.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SNumbers.isStrictSNumberSequence_approximation`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SNumbers/Approximation.html#TauCeti.SNumbers.isStrictSNumberSequence_approximation).

## Sources

- [Tau Ceti documentation: `TauCeti.SNumbers.isStrictSNumberSequence_approximation`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SNumbers/Approximation.html#TauCeti.SNumbers.isStrictSNumberSequence_approximation)
- [Source of `TauCeti.SNumbers.isStrictSNumberSequence_approximation` in TauCeti/Analysis/Normed/Operator/SNumbers/Approximation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/SNumbers/Approximation.lean#L52)
- [Tau Ceti roadmap status: s-numbers and entropy numbers of operators between Banach spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SNumbers/STATUS.md)
