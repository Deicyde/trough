---
declaration: theorem
origin: cited
lean: Polynomial.newtonPolygon_mul
statement: formalized
proof: formalized
---

# Polynomial.newtonPolygon_mul

The Newton polygon of a product of polynomials is the Minkowski sum of the Newton polygons
of the factors. If either factor has the empty Newton polygon, for example if it is zero, so
does the product.

```lean
Polynomial.newtonPolygon_mul.{u_1} {R : Type u_1} [Ring R] (f g : Polynomial R)
  (v : AddValuation R (WithTop ℝ)) :
  (f * g).newtonPolygon v = TauCeti.minkowskiSum (f.newtonPolygon v) (g.newtonPolygon v)
```

## Depends on

- [TauCeti.lowerConvexEnvelope](tauceti-lowerconvexenvelope.md)

## Lean

Formalized in Tau Ceti as [`Polynomial.newtonPolygon_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Mul.html#Polynomial.newtonPolygon_mul).

## Sources

- [Tau Ceti documentation: `Polynomial.newtonPolygon_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Mul.html#Polynomial.newtonPolygon_mul)
- [Source of `Polynomial.newtonPolygon_mul` in TauCeti/NumberTheory/NewtonPolygon/Mul.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NewtonPolygon/Mul.lean#L345)
- [Tau Ceti roadmap status: Newton polygons of polynomials and power series](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NewtonPolygons/STATUS.md)
