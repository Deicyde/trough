---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.hasDerivAt_toReal_pathELength
statement: formalized
proof: formalized
---

# The first variation of length

Let `F` be a two-parameter family which is `C²` at every
point of `{0} × [a, b]`, whose central curve `γ = F 0` has constant speed `C > 0` on `[a, b]`.
Then the length of `F s` between `a` and `b` is differentiable at `s = 0`, with derivative

`(⟪V(b), γ'(b)⟫ - ⟪V(a), γ'(a)⟫ - ∫_a^b ⟪V(t), D_t γ'(t)⟫ dt) / C`,

where `V` is the variation field and `D_t γ'` is the covariant acceleration of `γ` for the
Levi-Civita connection. The endpoints of the curves `F s` are not required to be fixed.

```lean
TauCeti.Manifold.hasDerivAt_toReal_pathELength.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I 2 M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {F : ℝ → ℝ → M} {a b : ℝ}
  (hab : a ≤ b)
  (hF :
    ∀ t ∈ Set.Icc a b, ContMDiffAt (modelWithCornersSelf ℝ (ℝ × ℝ)) I 2 (fun z => F z.1 z.2) (0, t))
  {C : ℝ} (hC : 0 < C) (hγ : ∀ t ∈ Set.Icc a b, ‖TauCeti.Manifold.curveVelocity I (F 0) t‖ = C) :
  HasDerivAt (fun s => (Manifold.pathELength I (F s) a b).toReal)
    ((inner ℝ (TauCeti.Manifold.variationField I F b) (TauCeti.Manifold.curveVelocity I (F 0) b) -
          inner ℝ (TauCeti.Manifold.variationField I F a)
            (TauCeti.Manifold.curveVelocity I (F 0) a) -
        ∫ (t : ℝ) in a..b,
          inner ℝ (TauCeti.Manifold.variationField I F t)
            ((CovariantDerivative.leviCivitaConnection I M).acceleration (F 0) t)) /
      C)
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.hasDerivAt_toReal_pathELength`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/FirstVariation/Length.html#TauCeti.Manifold.hasDerivAt_toReal_pathELength).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.hasDerivAt_toReal_pathELength`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/FirstVariation/Length.html#TauCeti.Manifold.hasDerivAt_toReal_pathELength)
- [Source of `TauCeti.Manifold.hasDerivAt_toReal_pathELength` in TauCeti/Geometry/Manifold/Riemannian/FirstVariation/Length.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/FirstVariation/Length.lean#L199)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
