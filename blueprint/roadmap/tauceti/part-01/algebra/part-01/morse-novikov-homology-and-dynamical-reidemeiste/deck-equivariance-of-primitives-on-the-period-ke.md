---
declaration: theorem
origin: cited
lean: TauCeti.PeriodCover.apply_deck_apply
statement: formalized
proof: formalized
---

# Deck-equivariance of primitives on the period-kernel cover

The deck transformation
labelled by the period `c` adds `c` to every `C²` primitive of the pulled-back form: for a deck
transformation `d`, `f (d y) = f y + P d`, where `P d` is the period labelling `d` under
`deckEquiv`.

```lean
TauCeti.PeriodCover.apply_deck_apply.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E] [T2Space M] [IsManifold I (↑⊤) M]
  {θ : TauCeti.SmoothForm I M ℝ 1} {x : M} [PreconnectedSpace M]
  (hθ : θ ∈ TauCeti.closedForms I M 1) {f : TauCeti.PeriodCover θ x → ℝ}
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 f)
  (hdf :
    TauCeti.mextDeriv (TauCeti.RoughForm.ofFunction I f) =
      TauCeti.mpullback I I (TauCeti.PeriodCover.proj θ x) ↑θ)
  (d : ↥(deck (TauCeti.PeriodCover.proj θ x))) (y : TauCeti.PeriodCover θ x) :
  f (↑d y) = f y + Multiplicative.toAdd ↑((TauCeti.PeriodCover.deckEquiv θ x) d)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus for path classes](../../../geometry/part-02/manifold/part-01/the-fundamental-theorem-of-calculus-for-path-cla.md)
- [The Poincaré lemma on manifolds](../../../geometry/part-02/manifold/part-02/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PeriodCover.apply_deck_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Cover.html#TauCeti.PeriodCover.apply_deck_apply).

## Sources

- [Tau Ceti documentation: `TauCeti.PeriodCover.apply_deck_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Cover.html#TauCeti.PeriodCover.apply_deck_apply)
- [Source of `TauCeti.PeriodCover.apply_deck_apply` in TauCeti/Geometry/Manifold/DeRham/Cover.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DeRham/Cover.lean#L290)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseNovikov/STATUS.md)
