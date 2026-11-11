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
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../../../ring-theory/part-01/restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)
- [Weierstrass preparation](../../../ring-theory/part-01/power-series/weierstrass-preparation.md)

## Lean

Formalized in Tau Ceti as [`Polynomial.existsUnique_isPureSlopeFactorization`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Factorization.html#Polynomial.existsUnique_isPureSlopeFactorization).

## Sources

- [Tau Ceti documentation: `Polynomial.existsUnique_isPureSlopeFactorization`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Factorization.html#Polynomial.existsUnique_isPureSlopeFactorization)
- [Source of `Polynomial.existsUnique_isPureSlopeFactorization` in TauCeti/NumberTheory/NewtonPolygon/Factorization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NewtonPolygon/Factorization.lean#L478)
- [Tau Ceti roadmap status: Newton polygons of polynomials and power series](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NewtonPolygons/STATUS.md)
