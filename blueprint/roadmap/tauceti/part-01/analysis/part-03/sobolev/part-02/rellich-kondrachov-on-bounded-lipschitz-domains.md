---
declaration: theorem
origin: cited
lean: TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith, TauCeti.W1p0.isCompactOperator_valueL, TauCeti.W1p.exists_isCompactOperator_of_isLipschitzDomainWith
statement: formalized
proof: formalized
---

# Rellich–Kondrachov on bounded Lipschitz domains

If `Ω` is a bounded Lipschitz domain and
`1 ≤ p ≤ ∞`, the value map `W^{1,p}(Ω) → Lᵖ(Ω)` is a compact operator.

```lean
TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {Ω : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {L : NNReal} {p : ENNReal}
  [Fact (1 ≤ p)] (hΩ : (↑Ω).IsLipschitzDomainWith L) (hb : Bornology.IsBounded ↑Ω) :
  IsCompactOperator ⇑TauCeti.W1p.valueL
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The endpoint local Morrey estimate](../part-01/the-endpoint-local-morrey-estimate.md)
- [Extension theorem for bounded Lipschitz domains](../part-01/extension-theorem-for-bounded-lipschitz-domains.md)
- [The Fréchet--Kolmogorov criterion for a family vanishing almost everywhere off a fixed bounded set](../../../../measure-theory/function/part-01/the-frechet-kolmogorov-criterion-for-a-family-va.md)
- [Hölder's inequality for the integral of a product](../../../../measure-theory/function/part-01/holders-inequality-for-the-integral-of-a-product.md)
- [The local Morrey inequality](../part-01/the-local-morrey-inequality.md)
- [The Sobolev inequality on `W^{1,p}_0` of a ball](the-sobolev-inequality-on-w-1-p-0-of-a-ball.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/RellichKondrachov.html#TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith).

## Other forms

**Rellich--Kondrachov for zero-boundary Sobolev spaces.** Formalized in Tau Ceti as [`TauCeti.W1p0.isCompactOperator_valueL`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/RellichKondrachov.html#TauCeti.W1p0.isCompactOperator_valueL).

```lean
TauCeti.W1p0.isCompactOperator_valueL.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens E}
  {p : ENNReal} [Fact (1 ≤ p)] (hp : p ≠ ⊤) (hOmega : Bornology.IsBounded ↑Omega) :
  IsCompactOperator ⇑TauCeti.W1p0.valueL
```

**Rellich–Kondrachov for subcritical target exponents.** Formalized in Tau Ceti as [`TauCeti.W1p.exists_isCompactOperator_of_isLipschitzDomainWith`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/RellichKondrachov.html#TauCeti.W1p.exists_isCompactOperator_of_isLipschitzDomainWith).

```lean
TauCeti.W1p.exists_isCompactOperator_of_isLipschitzDomainWith.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {Ω : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {L : NNReal} {p : ENNReal}
  [Fact (1 ≤ p)] {q : ENNReal} [Fact (1 ≤ q)] (hq : q ≠ ⊤)
  (hpq : p⁻¹ < q⁻¹ + (↑(Module.finrank ℝ (WithLp 2 (ℝ × E))))⁻¹) (hΩ : (↑Ω).IsLipschitzDomainWith L)
  (hb : Bornology.IsBounded ↑Ω) :
  ∃ S,
    IsCompactOperator ⇑S ∧
      ∀ (u : ↥(TauCeti.W1p MeasureTheory.volume Ω p)),
        ↑↑(S u) =ᵐ[MeasureTheory.volume.restrict ↑Ω] ↑↑(TauCeti.W1p.value u)
```

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/RellichKondrachov.html#TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith)
- [Source of `TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith` in TauCeti/Analysis/Sobolev/LipschitzDomain/RellichKondrachov.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/LipschitzDomain/RellichKondrachov.lean#L69)
