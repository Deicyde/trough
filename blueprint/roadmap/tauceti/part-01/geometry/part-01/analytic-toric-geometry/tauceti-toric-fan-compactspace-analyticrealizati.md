---
declaration: theorem
origin: cited
lean: TauCeti.Toric.Fan.compactSpace_analyticRealization_iff_isComplete
statement: formalized
proof: formalized
---

# TauCeti.Toric.Fan.compactSpace_analyticRealization_iff_isComplete

A nonempty regular fan has compact analytic realization exactly when it is complete. The
nonemptiness hypothesis is necessary: the realization of the empty fan is empty, hence compact,
while the empty fan is not complete. See
`TauCeti.Toric.Fan.compactSpace_analyticRealization_iff_isEmpty_or_isComplete` for the form
without it.

```lean
TauCeti.Toric.Fan.compactSpace_analyticRealization_iff_isComplete.{u} {N V : Type u}
  [AddCommGroup N] [AddCommGroup V] [_root_.Module ℝ V] {i : N →+ V} (Φ : TauCeti.Toric.Fan i)
  (hΦ : Φ.IsRegular) (hΦ0 : Nonempty ↑Φ.cones) :
  CompactSpace ↑(Φ.analyticRealization hΦ) ↔ Φ.IsComplete
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gordan's lemma](../../part-02/other-results/gordans-lemma.md)
- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.Fan.compactSpace_analyticRealization_iff_isComplete`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Compact.html#TauCeti.Toric.Fan.compactSpace_analyticRealization_iff_isComplete).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.Fan.compactSpace_analyticRealization_iff_isComplete`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Compact.html#TauCeti.Toric.Fan.compactSpace_analyticRealization_iff_isComplete)
- [Source of `TauCeti.Toric.Fan.compactSpace_analyticRealization_iff_isComplete` in TauCeti/Geometry/Toric/Analytic/Fan/Compact.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Toric/Analytic/Fan/Compact.lean#L269)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AnalyticToricGeometry/STATUS.md)
