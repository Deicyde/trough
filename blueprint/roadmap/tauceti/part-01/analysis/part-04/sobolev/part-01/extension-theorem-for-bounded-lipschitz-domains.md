---
declaration: theorem
origin: cited
lean: TauCeti.W1p.exists_extensionL_of_isLipschitzDomainWith
statement: formalized
proof: formalized
---

# Extension theorem for bounded Lipschitz domains

There is a bounded linear extension
from `W^{1,p}(Ω)` to the whole space, and restriction to `Ω` recovers the original function.
The extension preserves almost-everywhere nonnegativity. Both endpoint exponents `p = 1`
and `p = ∞` are included.

```lean
TauCeti.W1p.exists_extensionL_of_isLipschitzDomainWith.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {Ω : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {L : NNReal} {p : ENNReal} [Fact (1 ≤ p)]
  (hΩ : (↑Ω).IsLipschitzDomainWith L) (hb : Bornology.IsBounded ↑Ω) :
  ∃ T,
    TauCeti.W1p.restrictL ⋯ ∘SL T =
        ContinuousLinearMap.id ℝ ↥(TauCeti.W1p MeasureTheory.volume Ω p) ∧
      ∀ (u : ↥(TauCeti.W1p MeasureTheory.volume Ω p)),
        (∀ᵐ (x : WithLp 2 (ℝ × E)) ∂MeasureTheory.volume.restrict ↑Ω,
            0 ≤ ↑↑(TauCeti.W1p.value u) x) →
          ∀ᵐ (x : WithLp 2 (ℝ × E)), 0 ≤ ↑↑(TauCeti.W1p.value (T u)) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rademacher's theorem for locally Lipschitz functions](../../../part-03/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.exists_extensionL_of_isLipschitzDomainWith`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/GlobalExtension.html#TauCeti.W1p.exists_extensionL_of_isLipschitzDomainWith).

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.exists_extensionL_of_isLipschitzDomainWith`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/GlobalExtension.html#TauCeti.W1p.exists_extensionL_of_isLipschitzDomainWith)
- [Source of `TauCeti.W1p.exists_extensionL_of_isLipschitzDomainWith` in TauCeti/Analysis/Sobolev/LipschitzDomain/GlobalExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/LipschitzDomain/GlobalExtension.lean#L106)
