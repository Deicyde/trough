---
declaration: theorem
origin: cited
lean: TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_boundary, TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_domain, TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_halfStripExterior_polygonal_domain, TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_halfStrip_polygonal_domain, TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_unbounded_polygonal_domain
statement: formalized
proof: formalized
---

# The Schwarz--Christoffel formula

Let `f` be holomorphic with nonvanishing derivative on
the upper half-plane.  Assume that away from the distinct real prevertices `a i` its boundary
values run along affine lines with the upper half-plane on one side, and that each `a i` is
carried to a vertex of one of four kinds:
* a finite vertex: `f` opens the sector of angle `(e i + 1) * π` at `f (a i)`, with boundary values
  on the two bounding rays, where `-1 < e i < 1`;
* a vertex at infinity of opening `β * π` with `0 < β < 2`, where `e i = -β - 1`: the inverted map
  `b / (f - c)` extends across `a i` with value `0`, opens the sector of angle `β * π` there, and
  has its other boundary values on the two bounding rays;
* a vertex at infinity between two parallel sides, where `e i = -1`: the exponential
  `exp ((f - c) / b)` extends across `a i` with value `0`, injectively, with real boundary values
  and upper half-plane values above the axis;
* a vertex at infinity of opening `2 * π`, where `e i = -3`: `f` is continuous and injective on
  the closed upper half-disc about `a i` with `a i` removed, tends to infinity at `a i`, and far
  out the image of the open upper half-disc is the exterior of the closed half-strip
  `{0 ≤ re ((w - c) / b), 0 ≤ im ((w - c) / b) ≤ π}`.

Assume finally that `z * f''(z) / f'(z)` has a finite limit as `z` tends to infinity in the upper
half-plane.  Then throughout the upper half-plane

`f z = (f'(z₀) / integrand(z₀)) * F z + f z₀`,

where `F` is the normalized Schwarz--Christoffel primitive for the data `a` and `e`.  So `f` is an
affine image of `F`, and the two constants are read off from the value and derivative of `f` at
the normalization point `z₀`.

```lean
TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_boundary.{u_1} {ι : Type u_1}
  [Fintype ι] (a e : ι → ℝ) (ha : Function.Injective a) (z₀ : UpperHalfPlane) {f : ℂ → ℂ}
  (hf : DifferentiableOn ℂ f UpperHalfPlane.upperHalfPlaneSet)
  (hfn : ∀ z ∈ UpperHalfPlane.upperHalfPlaneSet, deriv f z ≠ 0)
  (hside :
    ∀ (x : ℝ),
      (∀ (i : ι), a i ≠ x) →
        ∃ r > 0,
          ∃ q b,
            b ≠ 0 ∧
              ContinuousOn f (Metric.ball (↑x) r ∩ {z | 0 ≤ z.im}) ∧
                Set.InjOn f (Metric.ball (↑x) r ∩ {z | 0 ≤ z.im}) ∧
                  (∀ z ∈ Metric.ball (↑x) r, z.im = 0 → ((f z - q) / b).im = 0) ∧
                    ∀ z ∈ Metric.ball (↑x) r, 0 < z.im → 0 < ((f z - q) / b).im)
  (hvertex :
    ∀ (i : ι),
      (e i ∈ Set.Ioo (-1) 1 ∧
          ∃ r > 0,
            ∃ b,
              b ≠ 0 ∧
                ContinuousOn f (Metric.ball (↑(a i)) r ∩ {z | 0 ≤ z.im}) ∧
                  Set.InjOn f (Metric.ball (↑(a i)) r ∩ {z | 0 ≤ z.im}) ∧
                    (∀ z ∈ Metric.ball (↑(a i)) r,
                        0 < z.im → |((f z - f ↑(a i)) / b).arg| < (e i + 1) * Real.pi / 2) ∧
                      ∀ z ∈ Metric.ball (↑(a i)) r,
                        z.im = 0 →
                          f z ≠ f ↑(a i) → |((f z - f ↑(a i)) / b).arg| = (e i + 1) * Real.pi / 2) ∨
        (e i ∈ Set.Ioo (-3) (-1) ∧
            ∃ r > 0,
              ∃ c b,
                b ≠ 0 ∧
                  ∃ g,
                    Set.EqOn g (fun z => b / (f z - c)) (Metric.ball (↑(a i)) r ∩ {z | 0 < z.im}) ∧
                      g ↑(a i) = 0 ∧
                        ContinuousOn g (Metric.ball (↑(a i)) r ∩ {z | 0 ≤ z.im}) ∧
                          Set.InjOn g (Metric.ball (↑(a i)) r ∩ {z | 0 ≤ z.im}) ∧
                            (∀ z ∈ Metric.ball (↑(a i)) r,
                                0 < z.im → |(g z).arg| < (-e i - 1) * Real.pi / 2) ∧
                              ∀ z ∈ Metric.ball (↑(a i)) r,
                                z.im = 0 → g z ≠ 0 → |(g z).arg| = (-e i - 1) * Real.pi / 2) ∨
          (e i = -1 ∧
              ∃ r > 0,
                ∃ c b,
                  b ≠ 0 ∧
                    ∃ g,
                      Set.EqOn g (fun z => Complex.exp ((f z - c) / b))
                          (Metric.ball (↑(a i)) r ∩ {z | 0 < z.im}) ∧
                        g ↑(a i) = 0 ∧
                          ContinuousOn g (Metric.ball (↑(a i)) r ∩ {z | 0 ≤ z.im}) ∧
                            (∀ z ∈ Metric.ball (↑(a i)) r, z.im = 0 → (g z).im = 0) ∧
                              Set.MapsTo g (Metric.ball (↑(a i)) r ∩ {z | 0 < z.im})
                                  {z | 0 < z.im} ∧
                                Set.InjOn g (Metric.ball (↑(a i)) r ∩ {z | 0 ≤ z.im})) ∨
            e i = -3 ∧
              ∃ r > 0,
                ∃ ρ c b,
                  b ≠ 0 ∧
                    ContinuousOn f ((Metric.closedBall (↑(a i)) r ∩ {z | 0 ≤ z.im}) \ {↑(a i)}) ∧
                      Set.InjOn f ((Metric.closedBall (↑(a i)) r ∩ {z | 0 ≤ z.im}) \ {↑(a i)}) ∧
                        Filter.Tendsto f (nhdsWithin (↑(a i)) ({z | 0 ≤ z.im} \ {↑(a i)}))
                            (Bornology.cobounded ℂ) ∧
                          ∀ (w : ℂ),
                            ρ < ‖w - c‖ →
                              (w ∈
                                  f '' (Metric.ball (↑(a i)) r ∩ UpperHalfPlane.upperHalfPlaneSet) ↔
                                ((w - c) / b).re < 0 ∨ ((w - c) / b).im ∉ Set.Icc 0 Real.pi))
  {L : ℂ}
  (hinfty :
    Filter.Tendsto (fun z => z * logDeriv (deriv f) z)
      (Bornology.cobounded ℂ ⊓ Filter.principal UpperHalfPlane.upperHalfPlaneSet) (nhds L)) :
  Set.EqOn f
    (fun z =>
      deriv f ↑z₀ / TauCeti.schwarzChristoffelIntegrand a e ↑z₀ *
          TauCeti.schwarzChristoffelPrimitive a e z₀ z +
        f ↑z₀)
    UpperHalfPlane.upperHalfPlaneSet
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The converse Schwarz--Christoffel theorem from the prevertex residues](../part-01/the-converse-schwarz-christoffel-theorem-from-th.md)
- [Rouché's theorem for a disc, classical form](rouches-theorem-for-a-disc-classical-form.md)
- [Schwarz reflection principle (real axis)](../part-01/schwarz-reflection-principle-real-axis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_boundary`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Formula.html#TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_boundary).

## Other forms

**The Schwarz--Christoffel formula for a conformal map onto a polygonal domain.** Formalized in Tau Ceti as [`TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_domain`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/PolygonalDomain.html#TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_domain).

```lean
TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_domain.{u_1} {U : Set ℂ}
  {f : ℂ → ℂ} {ι : Type u_1} [Fintype ι] (a e : ι → ℝ) (ha : Function.Injective a)
  (he : ∀ (i : ι), e i ∈ Set.Ioo (-1) 1) (z₀ : UpperHalfPlane) {v : ι → ℂ} {p : ℂ}
  (hf : DifferentiableOn ℂ f UpperHalfPlane.upperHalfPlaneSet) (hfc : ContinuousOn f {z | 0 ≤ z.im})
  (hfi : Set.InjOn f {z | 0 ≤ z.im}) (hfU : f '' UpperHalfPlane.upperHalfPlaneSet = U)
  (hfv : ∀ (i : ι), f ↑(a i) = v i)
  (hp : Filter.Tendsto f (Bornology.cobounded ℂ ⊓ Filter.principal {z | 0 ≤ z.im}) (nhds p))
  (hpf : p ∉ f '' {z | 0 ≤ z.im})
  (hside :
    ∀ w ∈ frontier U,
      (∀ (i : ι), w ≠ v i) →
        ∃ ρ > 0, ∃ q b, b ≠ 0 ∧ ∀ z ∈ Metric.ball w ρ, z ∈ U ↔ 0 < ((z - q) / b).im)
  (hcorner :
    ∀ (i : ι),
      ∃ ρ > 0,
        ∃ b,
          b ≠ 0 ∧
            ∀ z ∈ Metric.ball (v i) ρ,
              z ≠ v i → (z ∈ U ↔ |((z - v i) / b).arg| < (e i + 1) * Real.pi / 2)) :
  Set.EqOn f
    (fun z =>
      deriv f ↑z₀ / TauCeti.schwarzChristoffelIntegrand a e ↑z₀ *
          TauCeti.schwarzChristoffelPrimitive a e z₀ z +
        f ↑z₀)
    UpperHalfPlane.upperHalfPlaneSet
```

**The Schwarz--Christoffel formula for a conformal map onto a polygonal domain whose end is the exterior of a half-strip.** Formalized in Tau Ceti as [`TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_halfStripExterior_polygonal_domain`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/PolygonalDomain.html#TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_halfStripExterior_polygonal_domain).

```lean
TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_halfStripExterior_polygonal_domain.{u_1}
  {U : Set ℂ} {f : ℂ → ℂ} {ι : Type u_1} [Fintype ι] (a e : ι → ℝ) (ha : Function.Injective a)
  (he : ∀ (i : ι), e i ∈ Set.Ioo (-1) 1) (z₀ : UpperHalfPlane) {v : ι → ℂ}
  (hf : DifferentiableOn ℂ f UpperHalfPlane.upperHalfPlaneSet) (hfc : ContinuousOn f {z | 0 ≤ z.im})
  (hfi : Set.InjOn f {z | 0 ≤ z.im}) (hfU : f '' UpperHalfPlane.upperHalfPlaneSet = U)
  (hfv : ∀ (i : ι), f ↑(a i) = v i)
  (hp :
    Filter.Tendsto f (Bornology.cobounded ℂ ⊓ Filter.principal {z | 0 ≤ z.im})
      (Bornology.cobounded ℂ))
  (hside :
    ∀ w ∈ frontier U,
      (∀ (i : ι), w ≠ v i) →
        ∃ ρ > 0, ∃ q b, b ≠ 0 ∧ ∀ z ∈ Metric.ball w ρ, z ∈ U ↔ 0 < ((z - q) / b).im)
  (hcorner :
    ∀ (i : ι),
      ∃ ρ > 0,
        ∃ b,
          b ≠ 0 ∧
            ∀ z ∈ Metric.ball (v i) ρ,
              z ≠ v i → (z ∈ U ↔ |((z - v i) / b).arg| < (e i + 1) * Real.pi / 2))
  (hinfty :
    ∃ ρ c b,
      b ≠ 0 ∧
        ∀ (z : ℂ),
          ρ < ‖z - c‖ → (z ∈ U ↔ ((z - c) / b).re < 0 ∨ ((z - c) / b).im ∉ Set.Icc 0 Real.pi)) :
  Set.EqOn f
    (fun z =>
      deriv f ↑z₀ / TauCeti.schwarzChristoffelIntegrand a e ↑z₀ *
          TauCeti.schwarzChristoffelPrimitive a e z₀ z +
        f ↑z₀)
    UpperHalfPlane.upperHalfPlaneSet
```

**The Schwarz--Christoffel formula for a conformal map onto a polygonal domain with a half-strip end.** Formalized in Tau Ceti as [`TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_halfStrip_polygonal_domain`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/PolygonalDomain.html#TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_halfStrip_polygonal_domain).

```lean
TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_halfStrip_polygonal_domain.{u_1}
  {U : Set ℂ} {f : ℂ → ℂ} {ι : Type u_1} [Fintype ι] (a e : ι → ℝ) (ha : Function.Injective a)
  (he : ∀ (i : ι), e i ∈ Set.Ioo (-1) 1) (z₀ : UpperHalfPlane) {v : ι → ℂ}
  (hf : DifferentiableOn ℂ f UpperHalfPlane.upperHalfPlaneSet) (hfc : ContinuousOn f {z | 0 ≤ z.im})
  (hfi : Set.InjOn f {z | 0 ≤ z.im}) (hfU : f '' UpperHalfPlane.upperHalfPlaneSet = U)
  (hfv : ∀ (i : ι), f ↑(a i) = v i)
  (hp :
    Filter.Tendsto f (Bornology.cobounded ℂ ⊓ Filter.principal {z | 0 ≤ z.im})
      (Bornology.cobounded ℂ))
  (hside :
    ∀ w ∈ frontier U,
      (∀ (i : ι), w ≠ v i) →
        ∃ ρ > 0, ∃ q b, b ≠ 0 ∧ ∀ z ∈ Metric.ball w ρ, z ∈ U ↔ 0 < ((z - q) / b).im)
  (hcorner :
    ∀ (i : ι),
      ∃ ρ > 0,
        ∃ b,
          b ≠ 0 ∧
            ∀ z ∈ Metric.ball (v i) ρ,
              z ≠ v i → (z ∈ U ↔ |((z - v i) / b).arg| < (e i + 1) * Real.pi / 2))
  (hinfty :
    ∃ ρ c b,
      b ≠ 0 ∧
        ∀ (z : ℂ),
          ρ < ‖z - c‖ → (z ∈ U ↔ 0 < ((z - c) / b).re ∧ ((z - c) / b).im ∈ Set.Ioo 0 Real.pi)) :
  Set.EqOn f
    (fun z =>
      deriv f ↑z₀ / TauCeti.schwarzChristoffelIntegrand a e ↑z₀ *
          TauCeti.schwarzChristoffelPrimitive a e z₀ z +
        f ↑z₀)
    UpperHalfPlane.upperHalfPlaneSet
```

**The Schwarz--Christoffel formula for a conformal map onto an unbounded polygonal domain.** Formalized in Tau Ceti as [`TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_unbounded_polygonal_domain`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/PolygonalDomain.html#TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_unbounded_polygonal_domain).

```lean
TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_unbounded_polygonal_domain.{u_1}
  {U : Set ℂ} {f : ℂ → ℂ} {ι : Type u_1} [Fintype ι] (a e : ι → ℝ) (ha : Function.Injective a)
  (he : ∀ (i : ι), e i ∈ Set.Ioo (-1) 1) (z₀ : UpperHalfPlane) {v : ι → ℂ} {β : ℝ}
  (hβ : β ∈ Set.Ioo 0 2) (hf : DifferentiableOn ℂ f UpperHalfPlane.upperHalfPlaneSet)
  (hfc : ContinuousOn f {z | 0 ≤ z.im}) (hfi : Set.InjOn f {z | 0 ≤ z.im})
  (hfU : f '' UpperHalfPlane.upperHalfPlaneSet = U) (hfv : ∀ (i : ι), f ↑(a i) = v i)
  (hp :
    Filter.Tendsto f (Bornology.cobounded ℂ ⊓ Filter.principal {z | 0 ≤ z.im})
      (Bornology.cobounded ℂ))
  (hside :
    ∀ w ∈ frontier U,
      (∀ (i : ι), w ≠ v i) →
        ∃ ρ > 0, ∃ q b, b ≠ 0 ∧ ∀ z ∈ Metric.ball w ρ, z ∈ U ↔ 0 < ((z - q) / b).im)
  (hcorner :
    ∀ (i : ι),
      ∃ ρ > 0,
        ∃ b,
          b ≠ 0 ∧
            ∀ z ∈ Metric.ball (v i) ρ,
              z ≠ v i → (z ∈ U ↔ |((z - v i) / b).arg| < (e i + 1) * Real.pi / 2))
  (hinfty :
    ∃ ρ c b, b ≠ 0 ∧ ∀ (z : ℂ), ρ < ‖z - c‖ → (z ∈ U ↔ |((z - c) / b).arg| < β * Real.pi / 2)) :
  Set.EqOn f
    (fun z =>
      deriv f ↑z₀ / TauCeti.schwarzChristoffelIntegrand a e ↑z₀ *
          TauCeti.schwarzChristoffelPrimitive a e z₀ z +
        f ↑z₀)
    UpperHalfPlane.upperHalfPlaneSet
```

## Sources

- [Tau Ceti documentation: `TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_boundary`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Formula.html#TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_boundary)
- [Source of `TauCeti.eqOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_boundary` in TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Formula.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Formula.lean#L111)
