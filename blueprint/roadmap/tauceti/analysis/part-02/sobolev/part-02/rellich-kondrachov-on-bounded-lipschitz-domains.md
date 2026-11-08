---
declaration: theorem
origin: cited
lean: TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith, TauCeti.W1p0.isCompactOperator_valueL
statement: formalized
proof: formalized
---

# Rellich–Kondrachov on bounded Lipschitz domains

If `Ω` is a bounded Lipschitz domain and
`1 ≤ p < ∞`, the value map `W^{1,p}(Ω) → Lᵖ(Ω)` is a compact operator.

```lean
TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {Ω : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {L : NNReal} {p : ENNReal}
  [Fact (1 ≤ p)] (hp : p ≠ ⊤) (hΩ : (↑Ω).IsLipschitzDomainWith L) (hb : Bornology.IsBounded ↑Ω) :
  IsCompactOperator ⇑TauCeti.W1p.valueL
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Extension theorem for bounded Lipschitz domains](../part-01/extension-theorem-for-bounded-lipschitz-domains.md)
- [The Fréchet--Kolmogorov criterion for a family vanishing almost everywhere off a fixed bounded set](../../../../measure-theory/function/the-frechet-kolmogorov-criterion-for-a-family-va.md)
- [Hölder's inequality for the integral of a product](../../../../measure-theory/function/holders-inequality-for-the-integral-of-a-product.md)

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

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/RellichKondrachov.html#TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith)
- [Source of `TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith` in TauCeti/Analysis/Sobolev/LipschitzDomain/RellichKondrachov.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/LipschitzDomain/RellichKondrachov.lean#L51)
