---
declaration: theorem
origin: cited
lean: TauCeti.isMorseOneForm_iff_surjective_sectionLinearization
statement: formalized
proof: formalized
---

# TauCeti.isMorseOneForm_iff_surjective_sectionLinearization

A smooth closed real one-form is Morse exactly when it is regular at every zero as a
section of the alternating cotangent bundle.

```lean
TauCeti.isMorseOneForm_iff_surjective_sectionLinearization.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [I.Boundaryless] [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I 1 M] {α : TauCeti.RoughForm I M ℝ 1} [FiniteDimensional ℝ E] [T2Space M]
  [IsManifold I (↑⊤) M] (hα : TauCeti.IsSmoothForm I (↑⊤) α) (hclosed : TauCeti.mextDeriv α = 0) :
  TauCeti.IsMorseOneForm α ↔
    ∀ (x : M), α x = 0 → Function.Surjective ⇑(TauCeti.sectionLinearization I id α x)
```

## Depends on

- [TauCeti.IsMorseOneForm](tauceti-ismorseoneform.md)

## Proof depends on

- [The Poincaré lemma on manifolds](../../../geometry/part-02/manifold/part-03/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isMorseOneForm_iff_surjective_sectionLinearization`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/OneForm/Linearization.html#TauCeti.isMorseOneForm_iff_surjective_sectionLinearization).

## Sources

- [Tau Ceti documentation: `TauCeti.isMorseOneForm_iff_surjective_sectionLinearization`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/OneForm/Linearization.html#TauCeti.isMorseOneForm_iff_surjective_sectionLinearization)
- [Source of `TauCeti.isMorseOneForm_iff_surjective_sectionLinearization` in TauCeti/Geometry/Manifold/Morse/OneForm/Linearization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/OneForm/Linearization.lean#L97)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseNovikov/STATUS.md)
