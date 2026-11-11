---
declaration: theorem
origin: cited
lean: TauCeti.IsNonsingularDirection.isPartiallySemialgebraic
statement: formalized
proof: formalized
---

# Łojasiewicz's Lemma 5

A subset of the cylinder `(ι → ℝ) × (Unit → ℝ)` with bounded heights,
for which the vertical direction is nonsingular, is partially semialgebraic. This applies in
particular to bounded sets, by `Bornology.IsBounded.image_snd`.

```lean
TauCeti.IsNonsingularDirection.isPartiallySemialgebraic {ι : Type} [Fintype ι]
  {s : Set ((ι → ℝ) × (Unit → ℝ))} (hs : TauCeti.IsNonsingularDirection s (0, 1))
  (hb : Bornology.IsBounded (Prod.snd '' s)) : TauCeti.IsPartiallySemialgebraic s
```

## Depends on

- [TauCeti.IsPartiallySemialgebraic](tauceti-ispartiallysemialgebraic.md)

## Proof depends on

- [Real analytic Weierstrass preparation theorem](real-analytic-weierstrass-preparation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsNonsingularDirection.isPartiallySemialgebraic`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic/NonsingularDirection.html#TauCeti.IsNonsingularDirection.isPartiallySemialgebraic).

## Sources

- [Tau Ceti documentation: `TauCeti.IsNonsingularDirection.isPartiallySemialgebraic`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic/NonsingularDirection.html#TauCeti.IsNonsingularDirection.isPartiallySemialgebraic)
- [Source of `TauCeti.IsNonsingularDirection.isPartiallySemialgebraic` in TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic/NonsingularDirection.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic/NonsingularDirection.lean#L165)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
