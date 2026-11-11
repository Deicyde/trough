---
declaration: theorem
origin: cited
lean: PowerSeries.IsEntire.newtonPolygon_mul
statement: formalized
proof: formalized
---

# PowerSeries.IsEntire.newtonPolygon_mul

The Newton polygon of a product of entire series is the Minkowski sum of the Newton polygons
of the factors.

```lean
PowerSeries.IsEntire.newtonPolygon_mul.{u_1} {K : Type u_1} [NormedDivisionRing K]
  (v : AddValuation K (WithTop ℝ)) {b : ℝ} (hb : 1 < b)
  (hv : ∀ (x : K), x ≠ 0 → ‖x‖ = b ^ (-(v x).untop₀)) {f g : PowerSeries K} (hf : f.IsEntire)
  (hg : g.IsEntire) :
  (f * g).newtonPolygon v = TauCeti.minkowskiSum (f.newtonPolygon v) (g.newtonPolygon v)
```

## Depends on

- [TauCeti.lowerConvexEnvelope](tauceti-lowerconvexenvelope.md)

## Lean

Formalized in Tau Ceti as [`PowerSeries.IsEntire.newtonPolygon_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Entire.html#PowerSeries.IsEntire.newtonPolygon_mul).

## Sources

- [Tau Ceti documentation: `PowerSeries.IsEntire.newtonPolygon_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Entire.html#PowerSeries.IsEntire.newtonPolygon_mul)
- [Source of `PowerSeries.IsEntire.newtonPolygon_mul` in TauCeti/NumberTheory/NewtonPolygon/Entire.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NewtonPolygon/Entire.lean#L84)
- [Tau Ceti roadmap status: Newton polygons of polynomials and power series](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NewtonPolygons/STATUS.md)
