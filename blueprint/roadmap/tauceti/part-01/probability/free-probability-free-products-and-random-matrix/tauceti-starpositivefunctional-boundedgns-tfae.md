---
declaration: theorem
origin: cited
lean: TauCeti.StarPositiveFunctional.boundedGNS_TFAE
statement: formalized
proof: formalized
---

# TauCeti.StarPositiveFunctional.boundedGNS_TFAE

Characterization of bounded GNS realizations with prescribed generator norm bounds `R i ≥ 0`:
generator inequalities, generator and adjoint-generator inequalities, boundedness of GNS left
multiplication, bounded GNS Hilbert representations, Hilbert-space vector-functional realizations,
and C⋆-algebra realizations are all equivalent.

```lean
TauCeti.StarPositiveFunctional.boundedGNS_TFAE.{u} {ι : Type u}
  (φ : TauCeti.StarPositiveFunctional (TauCeti.StarPolynomial ℂ ι)) {R : ι → ℝ}
  (hR : ∀ (i : ι), 0 ≤ R i) :
  [∀ (i : ι) (p : TauCeti.StarPolynomial ℂ ι),
        φ (star p * star (TauCeti.StarPolynomial.X i) * TauCeti.StarPolynomial.X i * p) ≤
          ↑(R i) ^ 2 * φ (star p * p),
      (∀ (i : ι) (p : TauCeti.StarPolynomial ℂ ι),
          φ (star p * star (TauCeti.StarPolynomial.X i) * TauCeti.StarPolynomial.X i * p) ≤
            ↑(R i) ^ 2 * φ (star p * p)) ∧
        ∀ (i : ι) (p : TauCeti.StarPolynomial ℂ ι),
          φ (star p * TauCeti.StarPolynomial.X i * star (TauCeti.StarPolynomial.X i) * p) ≤
            ↑(R i) ^ 2 * φ (star p * p),
      ∀ (i : ι) (x : φ.GNS), ‖(φ.leftMul (TauCeti.StarPolynomial.X i)) x‖ ≤ R i * ‖x‖,
      ∃ (hX : ∀ (i : ι), Continuous ⇑(φ.leftMul (TauCeti.StarPolynomial.X i))),
        ∀ (i : ι), ‖(φ.starPolynomialRepresentation hX) (TauCeti.StarPolynomial.X i)‖ ≤ R i,
      ∃ H x x_1,
        ∃ (x_2 : CompleteSpace H),
          ∃ ξ T,
            (∀ (i : ι), ‖T i‖ ≤ R i) ∧
              TauCeti.starDistribution (ContinuousLinearMap.innerPositiveLinearMap ℂ ξ).toLinearMap
                  T =
                φ.toLinearMap,
      ∃ C x x_1,
        ∃ (_ : StarOrderedRing C),
          ∃ ω c,
            (∀ (i : ι), ‖c i‖ ≤ R i) ∧
              TauCeti.starDistribution ω.toLinearMap c = φ.toLinearMap].TFAE
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.StarPositiveFunctional.boundedGNS_TFAE`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Distribution/GNS.html#TauCeti.StarPositiveFunctional.boundedGNS_TFAE).

## Sources

- [Tau Ceti documentation: `TauCeti.StarPositiveFunctional.boundedGNS_TFAE`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Distribution/GNS.html#TauCeti.StarPositiveFunctional.boundedGNS_TFAE)
- [Source of `TauCeti.StarPositiveFunctional.boundedGNS_TFAE` in TauCeti/Probability/FreeProbability/Distribution/GNS.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/Distribution/GNS.lean#L304)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
