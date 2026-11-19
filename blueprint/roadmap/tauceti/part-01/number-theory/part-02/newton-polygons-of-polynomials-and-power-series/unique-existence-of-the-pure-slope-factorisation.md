---
declaration: theorem
origin: cited
lean: Polynomial.existsUnique_isPureSlopeFactorization
statement: formalized
proof: formalized
---

# Unique existence of the pure slope factorisation

Over a complete ultrametric normed field,
every polynomial `f` with `f.coeff 0 = 1` has a unique pure slope factorisation over `K`.

```lean
Polynomial.existsUnique_isPureSlopeFactorization.{u_1} {K : Type u_1} [NormedField K]
  [IsUltrametricDist K] [CompleteSpace K] (v : AddValuation K (WithTop ℝ)) {b : ℝ} (hb : 1 < b)
  (hv : ∀ (x : K), x ≠ 0 → ‖x‖ = b ^ (-(v x).untop₀)) {f : Polynomial K} (hf0 : f.coeff 0 = 1) :
  ∃! g, f.IsPureSlopeFactorization v g
```

## Depends on

- [TauCeti.lowerConvexEnvelope](tauceti-lowerconvexenvelope.md)

## Proof depends on

- [Polynomial.newtonPolygon_mul](polynomial-newtonpolygon-mul.md)
- [TauCeti.FiniteSlopeData](tauceti-finiteslopedata.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../../../ring-theory/part-01/restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [Weierstrass preparation](../../../ring-theory/part-02/power-series/weierstrass-preparation.md)

## Lean

Formalized in Tau Ceti as [`Polynomial.existsUnique_isPureSlopeFactorization`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Factorization.html#Polynomial.existsUnique_isPureSlopeFactorization).

## Sources

- [Tau Ceti documentation: `Polynomial.existsUnique_isPureSlopeFactorization`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Factorization.html#Polynomial.existsUnique_isPureSlopeFactorization)
- [Source of `Polynomial.existsUnique_isPureSlopeFactorization` in TauCeti/NumberTheory/NewtonPolygon/Factorization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NewtonPolygon/Factorization.lean#L478)
- [Tau Ceti roadmap status: Newton polygons of polynomials and power series](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NewtonPolygons/STATUS.md)
