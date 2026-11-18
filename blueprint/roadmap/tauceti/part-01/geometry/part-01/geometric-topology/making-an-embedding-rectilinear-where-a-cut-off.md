---
declaration: theorem
origin: cited
lean: TauCeti.IsStarImmersion.eventually_isStarImmersion_and_injective_lineMap_secantMap
statement: formalized
proof: formalized
---

# Making an embedding rectilinear where a cut-off is one

Let `f` be an injective `Cⁿ` star
immersion, `1 ≤ n`, of a complex `K` on a finite vertex type into a normed space, and let
`φ : |K| → ℝ` be `Cᵐ` on every closed simplex, `1 ≤ m`. For all sufficiently large `k`, the
interpolation `AffineMap.lineMap (f (π x)) (s x) (φ (π x))` on the `k`-th edgewise subdivision is
an injective `C^(min n m)` star immersion, where `s` is the secant map of `f` on the subdivision
and `π` is the canonical map onto `|K|`. It is linear on every closed simplex of the subdivision
on which `φ = 1`, and agrees with `f ∘ π` where `φ = 0`.

```lean
TauCeti.IsStarImmersion.eventually_isStarImmersion_and_injective_lineMap_secantMap.{u_1, u_2}
  {ι : Type u_1} {E : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E]
  {K : AbstractSimplicialComplex ι} {n : WithTop ℕ∞} {f : K.Realization → E} [Finite ι]
  [LinearOrder ι] {m : WithTop ℕ∞} {φ : K.Realization → ℝ} (h : TauCeti.IsStarImmersion n f)
  (hn : 1 ≤ n) (hf : Function.Injective f) (hm : 1 ≤ m)
  (hφ :
    ∀ (σ : TauCeti.SetLike.Face K),
      ∃ Φ,
        (∀ (x : AbstractSimplicialComplex.StandardSimplex ↑σ),
            (Φ fun a => ↑x ↑a) = φ (K.faceInclusion σ x)) ∧
          ContDiffOn ℝ m Φ (Set.range fun t => ⇑t.weights)) :
  ∀ᶠ (k : ℕ) in Filter.atTop,
    (TauCeti.IsStarImmersion (min n m) fun x =>
        (AffineMap.lineMap (f (K.edgewiseSubdivisionRealizationMap k x))
            ((K.edgewiseSubdivision k).secantMap (f ∘ K.edgewiseSubdivisionRealizationMap k) x))
          (φ (K.edgewiseSubdivisionRealizationMap k x))) ∧
      Function.Injective fun x =>
        (AffineMap.lineMap (f (K.edgewiseSubdivisionRealizationMap k x))
            ((K.edgewiseSubdivision k).secantMap (f ∘ K.edgewiseSubdivisionRealizationMap k) x))
          (φ (K.edgewiseSubdivisionRealizationMap k x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsStarImmersion.eventually_isStarImmersion_and_injective_lineMap_secantMap`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothTriangulation/Perturbation.html#TauCeti.IsStarImmersion.eventually_isStarImmersion_and_injective_lineMap_secantMap).

## Sources

- [Tau Ceti documentation: `TauCeti.IsStarImmersion.eventually_isStarImmersion_and_injective_lineMap_secantMap`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothTriangulation/Perturbation.html#TauCeti.IsStarImmersion.eventually_isStarImmersion_and_injective_lineMap_secantMap)
- [Source of `TauCeti.IsStarImmersion.eventually_isStarImmersion_and_injective_lineMap_secantMap` in TauCeti/Geometry/Manifold/SmoothTriangulation/Perturbation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/SmoothTriangulation/Perturbation.lean#L165)
- [Tau Ceti roadmap status: Geometric topology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricTopology/STATUS.md)
