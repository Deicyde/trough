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
- [Source of `Polynomial.newtonPolygon_mul` in TauCeti/NumberTheory/NewtonPolygon/Mul.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NewtonPolygon/Mul.lean#L345)
- [Tau Ceti roadmap status: Newton polygons of polynomials and power series](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NewtonPolygons/STATUS.md)
