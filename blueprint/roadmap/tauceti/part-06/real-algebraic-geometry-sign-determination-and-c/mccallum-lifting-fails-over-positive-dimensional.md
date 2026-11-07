---
declaration: theorem
origin: cited
lean: TauCeti.exists_nullified_mcCallumProjection_orderAt_ne
statement: formalized
proof: formalized
---

# McCallum lifting fails over positive-dimensional nullifying cells

The hypothesis of
`TauCeti.exists_isSemialgebraicStack_orderAt_eq_of_mcCallumProjection` that no basis member is
nullified over a cell with more than one point cannot be dropped, even over a connected
semialgebraic analytic submanifold on which the McCallum projection is order-invariant.

Explicitly, let `f = X₂ (X₀ + 1) + X₃ X₁`, a polynomial in the distinguished variable `X₀` and the
base coordinates `X₁, X₂, X₃`, and let `C ⊆ ℝ ^ 3` be the line of base points `x` with
`x₁ = x₂ = 0`. As a polynomial in `X₀`, `f` is linear with coprime coefficients `X₂` and
`X₂ + X₃ X₁`, each of which vanishes to order one at every point of `C`; its content and
discriminant are units. So for every irreducible basis `B` of `{f}`, every element of the McCallum
projection has constant order on `C`, while every member of `B` is nullified over `C`. But `f` has
order at least two at the point `(-1, 0, 0, 0)` above `C`, and order one at every point above
`C` where `X₀ ≠ -1` or `X₁ ≠ 0`. Since every cell of a stack over `C` lies over the whole of `C`,
no stack over `C`, given by pointwise strictly increasing functions, continuous or not, has `f`
order-invariant on each cell.

```lean
TauCeti.exists_nullified_mcCallumProjection_orderAt_ne
  (polynomialGCD : NormalizedGCDMonoid (MvPolynomial (Fin 3) ℝ)) :
  have this := polynomialGCD;
  ∃ f C,
    TauCeti.IsSemialgebraic C ∧
      TauCeti.IsAnalyticSubmanifold 1 C ∧
        IsConnected C ∧
          ∀ (B : Finset (Polynomial (MvPolynomial (Fin 3) ℝ))),
            (Finset.map (MvPolynomial.finSuccEquiv ℝ 3).toEmbedding {f}).IsIrreducibleBasis B →
              (∀
                  q ∈
                    (Finset.map (MvPolynomial.finSuccEquiv ℝ 3).toEmbedding {f}).mcCallumProjection
                      B,
                  ∀ x ∈ C, ∀ y ∈ C, q.orderAt x = q.orderAt y) ∧
                (∀ b ∈ B, ∀ x ∈ C, Polynomial.map (MvPolynomial.eval x) b = 0) ∧
                  ∀ (k : ℕ) (θ : Fin k → ↑C → ℝ),
                    (∀ (x : ↑C), StrictMono fun i => θ i x) →
                      ∃ E ∈ TauCeti.stackCells C θ, ∃ y ∈ E, ∃ y' ∈ E, f.orderAt y ≠ f.orderAt y'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_nullified_mcCallumProjection_orderAt_ne`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.html#TauCeti.exists_nullified_mcCallumProjection_orderAt_ne).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_nullified_mcCallumProjection_orderAt_ne`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.html#TauCeti.exists_nullified_mcCallumProjection_orderAt_ne)
- [Source of `TauCeti.exists_nullified_mcCallumProjection_orderAt_ne` in TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.lean#L204)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
