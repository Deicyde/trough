---
declaration: theorem
origin: cited
lean: TauCeti.exists_signInvariant_mcCallumProjection_stackCells_not_signInvariant
statement: formalized
proof: formalized
---

# Sign-invariance of the McCallum projection does not suffice for lifting

In
`Finset.IsSquarefreeBasis.exists_isSemialgebraicStack_signInvariant_of_mcCallumProjection`, the
hypothesis that the McCallum projection is order-invariant on the base cannot be weakened to
sign-invariance, even for a nonnullified squarefree basis over a connected semialgebraic
analytic submanifold. So a lower level of a CAD that is merely sign-invariant for the projection
cannot replace an order-invariant one.

Explicitly, let `f = (T - 1)² (T - 1 - x₀²) + x₁`, a monic cubic in the distinguished variable
`T` over `ℝ[x₀, x₁]`, and let `S ⊆ ℝ ^ 2` be the line `x₁ = 0`. As `f` is squarefree, it is its
own squarefree basis. Over `S` its coefficients `1`, `-(3 + x₀²)`, `3 + 2 x₀²` and `-(1 + x₀²)`
have constant signs, its content is `1`, and its discriminant vanishes, because each fibre
`(T - 1)² (T - 1 - x₀²)` has a double root. So the McCallum projection of `{f}` is sign-invariant
on `S`, and some member of it has nonconstant order on `S`; since the other members do not vanish
on `S`, this is the discriminant. But the fibre has the two roots `1` and `2` over `(1, 0)` and
the single root `1` over the origin. In the coordinates `(T, x₀, x₁)`, every cell of a stack over
`S` lies over all of `S`, so the cells through the zeros `(1, 1, 0)` and `(2, 1, 0)` of `f` would
both contain its only zero `(1, 0, 0)` over the origin, hence coincide, and then also contain
`(3 / 2, 1, 0)`, where `f` is negative. So no stack over `S`, given by pointwise strictly
increasing functions, continuous or not, has `f` sign-invariant on each cell.

```lean
TauCeti.exists_signInvariant_mcCallumProjection_stackCells_not_signInvariant
  (polynomialGCD : NormalizedGCDMonoid (MvPolynomial (Fin 2) ℝ)) :
  ∃ f S,
    {f}.IsSquarefreeBasis {f} ∧
      TauCeti.IsSemialgebraic S ∧
        TauCeti.IsAnalyticSubmanifold 1 S ∧
          IsConnected S ∧
            (∀ x ∈ S, Polynomial.map (MvPolynomial.eval x) f ≠ 0) ∧
              (∀ q ∈ {f}.mcCallumProjection {f},
                  TauCeti.SignInvariant (fun x => (MvPolynomial.eval x) q) S) ∧
                (∃ q ∈ {f}.mcCallumProjection {f}, ∃ x ∈ S, ∃ y ∈ S, q.orderAt x ≠ q.orderAt y) ∧
                  ∀ (k : ℕ) (θ : Fin k → ↑S → ℝ),
                    (∀ (x : ↑S), StrictMono fun i => θ i x) →
                      ∃ E ∈ TauCeti.stackCells S θ,
                        ¬TauCeti.SignInvariant
                            (fun y =>
                              (MvPolynomial.eval y) ((MvPolynomial.finSuccEquiv ℝ 2).symm f))
                            E
```

## Depends on

- [Finset.IsSquarefreeBasis](finset-issquarefreebasis.md)

## Proof depends on

- [The analytic implicit root theorem](../../../analysis/part-01/analytic/the-analytic-implicit-root-theorem.md)
- [Hadamard's lemma along a graph](../../../analysis/part-01/analytic/hadamards-lemma-along-a-graph.md)
- [Identity theorem on the real points](../../../analysis/part-01/real-analytic-geometry-and-semianalytic-triangul/identity-theorem-on-the-real-points.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../../../algebraic-topology/universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [The Riemann extension theorem across a coordinate hyperplane](../../../analysis/part-02/complex/part-02/the-riemann-extension-theorem-across-a-coordinat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_signInvariant_mcCallumProjection_stackCells_not_signInvariant`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Projection/McCallum/SignInvariant.html#TauCeti.exists_signInvariant_mcCallumProjection_stackCells_not_signInvariant).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_signInvariant_mcCallumProjection_stackCells_not_signInvariant`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Projection/McCallum/SignInvariant.html#TauCeti.exists_signInvariant_mcCallumProjection_stackCells_not_signInvariant)
- [Source of `TauCeti.exists_signInvariant_mcCallumProjection_stackCells_not_signInvariant` in TauCeti/Geometry/RealAlgebraic/Projection/McCallum/SignInvariant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/Projection/McCallum/SignInvariant.lean#L289)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
