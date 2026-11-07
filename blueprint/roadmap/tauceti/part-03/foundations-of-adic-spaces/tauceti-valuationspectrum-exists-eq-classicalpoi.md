---
declaration: theorem
origin: cited
lean: TauCeti.ValuationSpectrum.exists_eq_classicalPoint_or_discPoint_or_discPointAbove_or_discPointBelow_or_nestedDiscPoint
statement: formalized
proof: formalized
---

# TauCeti.ValuationSpectrum.exists\_eq\_classicalPoint\_or\_discPoint\_or\_discPointAbove\_or\_discPointBelow\_or\_nestedDiscPoint

**Every point of the closed unit disc is of one of Wedhorn's five types**, over an
algebraically closed complete nonarchimedean field (Example 7.57): a classical point `x_a`
(type (1)), a point `η_{a,r}` (types (2) and (3)), the point attached to a decreasing sequence of
discs `D(aₙ, |cₙ|)` with no common point in `K` (type (4)), or a rank-two point `η_{a,r⁺}` or
`η_{a,r⁻}` with `r` the norm of an element of `K` (type (5)).

```lean
TauCeti.ValuationSpectrum.exists_eq_classicalPoint_or_discPoint_or_discPointAbove_or_discPointBelow_or_nestedDiscPoint.{u_1}
  {K : Type u_1} [NontriviallyNormedField K] [NonarchimedeanRing K] [IsUltrametricDist K]
  [CompleteSpace K] [IsAlgClosed K] (x : ↑(TauCeti.ValuationSpectrum.closedPolydisc 1 K)) :
  (∃ y a,
      ∃ (ha : ∀ (i : Fin 1), TauCeti.Huber.IsPowerBounded (a i)),
        x = TauCeti.ValuationSpectrum.classicalPoint y a ha) ∨
    (∃ a,
        ∃ (ha : ‖a‖ ≤ 1),
          ∃ r,
            ∃ (hr₀ : 0 < r) (hr₁ : r ≤ 1), x = TauCeti.ValuationSpectrum.discPoint a ha hr₀ hr₁) ∨
      (∃ a,
          ∃ (ha : ‖a‖ ≤ 1),
            ∃ c,
              ∃ (hc₀ : 0 < ‖c‖) (hc₁ : ‖c‖ < 1),
                x = TauCeti.ValuationSpectrum.discPointAbove a ha hc₀ hc₁) ∨
        (∃ a,
            ∃ (ha : ‖a‖ ≤ 1),
              ∃ c,
                ∃ (hc₀ : 0 < ‖c‖) (hc₁ : ‖c‖ ≤ 1),
                  x = TauCeti.ValuationSpectrum.discPointBelow a ha hc₀ hc₁) ∨
          ∃ a,
            ∃ (ha : ∀ (n : ℕ), ‖a n‖ ≤ 1),
              ∃ c,
                ∃ (hc₀ : ∀ (n : ℕ), c n ≠ 0) (hc₁ : ∀ (n : ℕ), ‖c n‖ ≤ 1) (hac :
                  ∀ (n : ℕ), ‖a (n + 1) - a n‖ ≤ ‖c n‖) (hcc : ∀ (n : ℕ), ‖c (n + 1)‖ ≤ ‖c n‖),
                  (∀ (b : K), ∃ n, ‖c n‖ < ‖b - a n‖) ∧
                    x = TauCeti.ValuationSpectrum.nestedDiscPoint a ha c hc₀ hc₁ hac hcc
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.exists_eq_classicalPoint_or_discPoint_or_discPointAbove_or_discPointBelow_or_nestedDiscPoint`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/Classification.html#TauCeti.ValuationSpectrum.exists_eq_classicalPoint_or_discPoint_or_discPointAbove_or_discPointBelow_or_nestedDiscPoint).

## Sources

- [Tau Ceti documentation: `TauCeti.ValuationSpectrum.exists_eq_classicalPoint_or_discPoint_or_discPointAbove_or_discPointBelow_or_nestedDiscPoint`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/Classification.html#TauCeti.ValuationSpectrum.exists_eq_classicalPoint_or_discPoint_or_discPointAbove_or_discPointBelow_or_nestedDiscPoint)
- [Source of `TauCeti.ValuationSpectrum.exists_eq_classicalPoint_or_discPoint_or_discPointAbove_or_discPointBelow_or_nestedDiscPoint` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/Classification.lean#L773)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AdicSpaces/STATUS.md)
