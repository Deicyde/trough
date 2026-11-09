---
declaration: theorem
origin: cited
lean: TauCeti.rectangleIntegral_sub_rectangleIntegral_eq_sides, TauCeti.rectangleIntegral_mextDeriv
statement: formalized
proof: formalized
---

# Stokes' formula for a homotopy of maps of a rectangle

Let `φ` be a closed `C¹` two-form
and `Φ : (ℝ × ℝ) × ℝ → M` a `C²` homotopy from `Φ(·, 0)` to `Φ(·, 1)`. The integral of `Φ^* φ`
over the boundary of the cube `[a, b] × [0, 1]` vanishes: the change of the integral over the
rectangle `[a, b]` from `Φ(·, 0)` to `Φ(·, 1)` is the signed sum of the integrals over the side
faces `(t, c) ↦ Φ((a.1, t), c)`, `(t, c) ↦ Φ((b.1, t), c)`, `(s, c) ↦ Φ((s, a.2), c)` and
`(s, c) ↦ Φ((s, b.2), c)` swept out by the edges of the rectangle.

```lean
TauCeti.rectangleIntegral_sub_rectangleIntegral_eq_sides.{u_1, u_2, u_3, u_4} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] [IsManifold I 2 M]
  {φ : TauCeti.RoughForm I M F 2} (hφ : TauCeti.IsSmoothForm I 1 φ) (hdφ : TauCeti.mextDeriv φ = 0)
  {Φ : (ℝ × ℝ) × ℝ → M} (hΦ : ContMDiff (modelWithCornersSelf ℝ ((ℝ × ℝ) × ℝ)) I 2 Φ)
  (a b : ℝ × ℝ) :
  TauCeti.rectangleIntegral φ (fun z => Φ (z, 1)) a b -
      TauCeti.rectangleIntegral φ (fun z => Φ (z, 0)) a b =
    TauCeti.rectangleIntegral φ (fun p => Φ ((a.1, p.1), p.2)) (a.2, 0) (b.2, 1) -
        TauCeti.rectangleIntegral φ (fun p => Φ ((b.1, p.1), p.2)) (a.2, 0) (b.2, 1) -
      (TauCeti.rectangleIntegral φ (fun p => Φ ((p.1, a.2), p.2)) (a.1, 0) (b.1, 1) -
        TauCeti.rectangleIntegral φ (fun p => Φ ((p.1, b.2), p.2)) (a.1, 0) (b.1, 1))
```

## Depends on

- [TauCeti.pathIntegral](tauceti-pathintegral.md)

## Proof depends on

- [Stokes' formula on the boundary of a cube for a closed two-form `ψ` that is C¹ on `(ℝ × ℝ) × ℝ`](../../../../analysis/part-02/calculus/part-02/stokes-formula-on-the-boundary-of-a-cube-for-a-c.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.rectangleIntegral_sub_rectangleIntegral_eq_sides`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Homotopy.html#TauCeti.rectangleIntegral_sub_rectangleIntegral_eq_sides).

## Other forms

**Stokes' formula for the integral over a map of a rectangle.** Formalized in Tau Ceti as [`TauCeti.rectangleIntegral_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Homotopy.html#TauCeti.rectangleIntegral_mextDeriv).

```lean
TauCeti.rectangleIntegral_mextDeriv.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [IsManifold I 2 M] {α : TauCeti.RoughForm I M F 1}
  (hα : TauCeti.IsSmoothForm I 1 α) {u : ℝ × ℝ → M}
  (hu : ContMDiff (modelWithCornersSelf ℝ (ℝ × ℝ)) I 2 u) (a b : ℝ × ℝ) :
  TauCeti.rectangleIntegral (TauCeti.mextDeriv α) u a b =
    TauCeti.pathIntegral α (fun t => u (b.1, t)) a.2 b.2 -
        TauCeti.pathIntegral α (fun t => u (a.1, t)) a.2 b.2 -
      (TauCeti.pathIntegral α (fun s => u (s, b.2)) a.1 b.1 -
        TauCeti.pathIntegral α (fun s => u (s, a.2)) a.1 b.1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.rectangleIntegral_sub_rectangleIntegral_eq_sides`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Homotopy.html#TauCeti.rectangleIntegral_sub_rectangleIntegral_eq_sides)
- [Source of `TauCeti.rectangleIntegral_sub_rectangleIntegral_eq_sides` in TauCeti/Geometry/Manifold/DifferentialForm/Integration/Homotopy.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Homotopy.lean#L371)
