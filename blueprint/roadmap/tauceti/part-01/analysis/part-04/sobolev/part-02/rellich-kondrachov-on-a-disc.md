---
declaration: theorem
origin: cited
lean: TauCeti.Wkp.isCompactOperator_lowerOrderL_complexBall, TauCeti.W1p0.isCompactOperator_valueL, TauCeti.W1p.exists_isCompactOperator_of_isLipschitzDomainWith, TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith, TauCeti.Wkp.isCompactOperator_lowerOrderL_of_isLipschitzDomainWith_image, TauCeti.Wkp.isCompactOperator_lowerOrderL_complexHalfDisc
statement: formalized
proof: formalized
---

# Rellich–Kondrachov on a disc

On a disc `Metric.ball c r` of `ℂ`, forgetting the highest
weak derivative is a compact operator `W^{k+1,p} → W^{k,p}` for every `k` and every
`1 ≤ p ≤ ∞`.

```lean
TauCeti.Wkp.isCompactOperator_lowerOrderL_complexBall {p : ENNReal} [Fact (1 ≤ p)] (c : ℂ) (r : ℝ)
  (k : ℕ) : IsCompactOperator ⇑(TauCeti.Wkp.lowerOrderL k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The endpoint local Morrey estimate](../part-01/the-endpoint-local-morrey-estimate.md)
- [Extension theorem for bounded Lipschitz domains](../part-01/extension-theorem-for-bounded-lipschitz-domains.md)
- [The Fréchet--Kolmogorov criterion for a family vanishing almost everywhere off a fixed bounded set](../../../../measure-theory/function/part-01/the-frechet-kolmogorov-criterion-for-a-family-va.md)
- [Hölder's inequality for disjoint pieces](../../../../measure-theory/function/part-01/holders-inequality-for-disjoint-pieces.md)
- [The local Morrey inequality](../part-01/the-local-morrey-inequality.md)
- [Rademacher's theorem for locally Lipschitz functions](../../../part-03/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)
- [The Sobolev inequality on `W^{1,p}_0` of a ball](the-sobolev-inequality-on-w-1-p-0-of-a-ball.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Wkp.isCompactOperator_lowerOrderL_complexBall`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/Wkp/Planar.html#TauCeti.Wkp.isCompactOperator_lowerOrderL_complexBall).

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

**Rellich–Kondrachov on bounded Lipschitz domains.** Formalized in Tau Ceti as [`TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/RellichKondrachov.html#TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith).

```lean
TauCeti.W1p.isCompactOperator_valueL_of_isLipschitzDomainWith.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {Ω : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {L : NNReal} {p : ENNReal}
  [Fact (1 ≤ p)] (hΩ : (↑Ω).IsLipschitzDomainWith L) (hb : Bornology.IsBounded ↑Ω) :
  IsCompactOperator ⇑TauCeti.W1p.valueL
```

**Rellich–Kondrachov on isometric copies of Lipschitz domains.** Formalized in Tau Ceti as [`TauCeti.Wkp.isCompactOperator_lowerOrderL_of_isLipschitzDomainWith_image`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/Wkp/LinearIsometry.html#TauCeti.Wkp.isCompactOperator_lowerOrderL_of_isLipschitzDomainWith_image).

```lean
TauCeti.Wkp.isCompactOperator_lowerOrderL_of_isLipschitzDomainWith_image.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [InnerProductSpace ℝ F]
  [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F] {L : NNReal} {p : ENNReal}
  [Fact (1 ≤ p)] (e : F ≃ₗᵢ[ℝ] WithLp 2 (ℝ × E)) {Ω : TopologicalSpace.Opens F}
  (hΩ : (⇑e '' ↑Ω).IsLipschitzDomainWith L) (hb : Bornology.IsBounded ↑Ω) (k : ℕ) :
  IsCompactOperator ⇑(TauCeti.Wkp.lowerOrderL k)
```

**Rellich–Kondrachov on the planar half-disc.** Formalized in Tau Ceti as [`TauCeti.Wkp.isCompactOperator_lowerOrderL_complexHalfDisc`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/Wkp/Planar.html#TauCeti.Wkp.isCompactOperator_lowerOrderL_complexHalfDisc).

```lean
TauCeti.Wkp.isCompactOperator_lowerOrderL_complexHalfDisc {p : ENNReal} [Fact (1 ≤ p)] (r : ℝ)
  (k : ℕ) : IsCompactOperator ⇑(TauCeti.Wkp.lowerOrderL k)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Wkp.isCompactOperator_lowerOrderL_complexBall`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/Wkp/Planar.html#TauCeti.Wkp.isCompactOperator_lowerOrderL_complexBall)
- [Source of `TauCeti.Wkp.isCompactOperator_lowerOrderL_complexBall` in TauCeti/Analysis/Sobolev/LipschitzDomain/Wkp/Planar.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/LipschitzDomain/Wkp/Planar.lean#L98)
