---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.hasCompactoidImage_iff_isCompletelyContinuous
statement: formalized
proof: formalized
---

# Compactoid image is complete continuity

**Compactoid image is complete continuity** for maps into an ultrametric Banach space over a
complete nontrivially normed field.

```lean
ContinuousLinearMap.hasCompactoidImage_iff_isCompletelyContinuous.{u_1, u_2, u_3} {K : Type u_1}
  {E : Type u_2} {F : Type u_3} [NontriviallyNormedField K] [CompleteSpace K]
  [SeminormedAddCommGroup E] [NormedSpace K E] [NormedAddCommGroup F] [NormedSpace K F]
  [IsUltrametricDist F] [CompleteSpace F] {u : E →L[K] F} :
  u.HasCompactoidImage ↔ u.IsCompletelyContinuous
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Riesz's lemma, translated form](../../part-03/normed/part-02/rieszs-lemma-translated-form.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.hasCompactoidImage_iff_isCompletelyContinuous`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compactoid/CompletelyContinuous.html#ContinuousLinearMap.hasCompactoidImage_iff_isCompletelyContinuous).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.hasCompactoidImage_iff_isCompletelyContinuous`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compactoid/CompletelyContinuous.html#ContinuousLinearMap.hasCompactoidImage_iff_isCompletelyContinuous)
- [Source of `ContinuousLinearMap.hasCompactoidImage_iff_isCompletelyContinuous` in TauCeti/Analysis/Normed/Operator/Compactoid/CompletelyContinuous.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/Compactoid/CompletelyContinuous.lean#L158)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CompactOperators/STATUS.md)
