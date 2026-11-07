---
declaration: theorem
origin: cited
lean: TauCeti.exists_analytic_delineation_of_orderAt_discr_eq
statement: formalized
proof: formalized
---

# Analytic delineability from constant discriminant order

A polynomial with nonzero
fibers of constant degree over a preconnected analytic submanifold, whose nonzero formal
discriminant has constant ambient order on the base, has a global delineation with intrinsically
analytic root functions. Each root function is represented by an ambient function whose values
off the base are immaterial. Along each root section, the polynomial, viewed as a polynomial in
all `n + 1` variables, has constant ambient order of vanishing.

No preservation of the formal degree or nonvanishing of the discriminant values is required.
Multiple roots are allowed, and their fiber multiplicities are constant.

```lean
TauCeti.exists_analytic_delineation_of_orderAt_discr_eq {n d : ℕ} {S : Set (Fin n → ℝ)}
  {p : Polynomial (MvPolynomial (Fin n) ℝ)} (hS : TauCeti.IsAnalyticSubmanifold d S)
  (hconn : IsPreconnected S) (hp : ∀ x ∈ S, Polynomial.map (MvPolynomial.eval x) p ≠ 0)
  (hdegree :
    ∀ x ∈ S,
      ∀ y ∈ S,
        (Polynomial.map (MvPolynomial.eval x) p).natDegree =
          (Polynomial.map (MvPolynomial.eval y) p).natDegree)
  (hdiscr : p.discr ≠ 0) (horder : ∀ x ∈ S, ∀ y ∈ S, p.discr.orderAt x = p.discr.orderAt y) :
  ∃ D,
    (∀ (i : Fin D.count),
        ∃ r, TauCeti.AnalyticOnSubmanifold d r S ∧ ∀ (x : ↑S), r ↑x = D.root i x) ∧
      ∀ (i : Fin D.count) (x y : ↑S),
        ((MvPolynomial.finSuccEquiv ℝ n).symm p).orderAt (Fin.cons (D.root i x) ↑x) =
          ((MvPolynomial.finSuccEquiv ℝ n).symm p).orderAt (Fin.cons (D.root i y) ↑y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../../part-07/universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_analytic_delineation_of_orderAt_discr_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Stack/Discriminant/Global.html#TauCeti.exists_analytic_delineation_of_orderAt_discr_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_analytic_delineation_of_orderAt_discr_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Stack/Discriminant/Global.html#TauCeti.exists_analytic_delineation_of_orderAt_discr_eq)
- [Source of `TauCeti.exists_analytic_delineation_of_orderAt_discr_eq` in TauCeti/Geometry/RealAlgebraic/Stack/Discriminant/Global.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/Stack/Discriminant/Global.lean#L173)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
