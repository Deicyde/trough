---
declaration: theorem
origin: cited
lean: TauCeti.SNumbers.IsSNumberSequence.le_singularValue
statement: formalized
proof: formalized
---

# TauCeti.SNumbers.IsSNumberSequence.le_singularValue

Approximation numbers are the largest s-number sequence, pointwise on every operator.

```lean
TauCeti.SNumbers.IsSNumberSequence.le_singularValue.{u} {𝕜 : Type u} [NontriviallyNormedField 𝕜]
  {s : TauCeti.SNumbers.SNumberFamily 𝕜}
  (hs :
    TauCeti.SNumbers.IsSNumberSequence
      fun {X Y} [NormedAddCommGroup X] [NormedSpace 𝕜 X] [NormedAddCommGroup Y] [NormedSpace 𝕜 Y] =>
      s)
  {X Y : Type u} [NormedAddCommGroup X] [NormedSpace 𝕜 X] [NormedAddCommGroup Y] [NormedSpace 𝕜 Y]
  (T : X →L[𝕜] Y) (n : ℕ) : s T n ≤ T.singularValue n
```

## Depends on

- [TauCeti.SNumbers.IsSNumberSequence](tauceti-snumbers-issnumbersequence.md)
- [TauCeti.SNumbers.SNumberFamily](tauceti-snumbers-snumberfamily.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SNumbers.IsSNumberSequence.le_singularValue`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SNumbers/Approximation.html#TauCeti.SNumbers.IsSNumberSequence.le_singularValue).

## Sources

- [Tau Ceti documentation: `TauCeti.SNumbers.IsSNumberSequence.le_singularValue`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SNumbers/Approximation.html#TauCeti.SNumbers.IsSNumberSequence.le_singularValue)
- [Source of `TauCeti.SNumbers.IsSNumberSequence.le_singularValue` in TauCeti/Analysis/Normed/Operator/SNumbers/Approximation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/SNumbers/Approximation.lean#L66)
- [Tau Ceti roadmap status: s-numbers and entropy numbers of operators between Banach spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SNumbers/STATUS.md)
