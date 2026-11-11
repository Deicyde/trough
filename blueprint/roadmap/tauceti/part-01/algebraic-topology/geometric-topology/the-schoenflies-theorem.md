---
declaration: theorem
origin: cited
lean: TauCeti.IsJordanCurve.exists_homeomorph_image_sphere, TauCeti.IsJordanCurve.exists_homeomorph_image_inner_eq_zero, TauCeti.IsJordanCurve.exists_homeomorph_image_sphere_of_mem
statement: formalized
proof: formalized
---

# The Schoenflies theorem

For every Jordan curve `C ⊆ ℂ` there is a homeomorphism of `ℂ`
carrying the unit circle onto `C`, the open unit disc onto the inside `filledHull C \ C` of `C`, and
the closed unit disc onto `filledHull C`.

```lean
TauCeti.IsJordanCurve.exists_homeomorph_image_sphere {C : Set ℂ} (hC : TauCeti.IsJordanCurve C) :
  ∃ e,
    ⇑e '' Metric.sphere 0 1 = C ∧
      ⇑e '' Metric.ball 0 1 = TauCeti.filledHull C \ C ∧
        ⇑e '' Metric.closedBall 0 1 = TauCeti.filledHull C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Carathéodory's theorem for the inside of a Jordan curve](../../analysis/part-02/complex/part-01/caratheodorys-theorem-for-the-inside-of-a-jordan.md)
- [The Jordan separation theorem](../../analysis/part-02/complex/part-02/the-jordan-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.exists_homeomorph_image_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Jordan/Schoenflies.html#TauCeti.IsJordanCurve.exists_homeomorph_image_sphere).

## Other forms

**The Schoenflies theorem on the 2-sphere.** Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.exists_homeomorph_image_inner_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Jordan/Schoenflies.html#TauCeti.IsJordanCurve.exists_homeomorph_image_inner_eq_zero).

```lean
TauCeti.IsJordanCurve.exists_homeomorph_image_inner_eq_zero.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [Fact (Module.finrank ℝ E = 3)]
  {C : Set ↑(Metric.sphere 0 1)} (hC : TauCeti.IsJordanCurve C) {v : ↑(Metric.sphere 0 1)}
  (hv : v ∉ C) : ∃ e, e v = v ∧ ⇑e '' {x | inner ℝ ↑x ↑v = 0} = C
```

**The Schoenflies theorem, centred at a point of the inside.** Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.exists_homeomorph_image_sphere_of_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Jordan/Schoenflies.html#TauCeti.IsJordanCurve.exists_homeomorph_image_sphere_of_mem).

```lean
TauCeti.IsJordanCurve.exists_homeomorph_image_sphere_of_mem {C : Set ℂ} {p : ℂ}
  (hC : TauCeti.IsJordanCurve C) (hp : p ∈ TauCeti.filledHull C \ C) :
  ∃ e,
    e 0 = p ∧
      ⇑e '' Metric.sphere 0 1 = C ∧
        ⇑e '' Metric.ball 0 1 = TauCeti.filledHull C \ C ∧
          ⇑e '' Metric.closedBall 0 1 = TauCeti.filledHull C
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsJordanCurve.exists_homeomorph_image_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Jordan/Schoenflies.html#TauCeti.IsJordanCurve.exists_homeomorph_image_sphere)
- [Source of `TauCeti.IsJordanCurve.exists_homeomorph_image_sphere` in TauCeti/Analysis/Complex/Conformal/Jordan/Schoenflies.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/Jordan/Schoenflies.lean#L119)
- [Tau Ceti roadmap status: Geometric topology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricTopology/STATUS.md)
