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
- [Source of `TauCeti.IsNonsingularDirection.isPartiallySemialgebraic` in TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic/NonsingularDirection.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic/NonsingularDirection.lean#L165)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
