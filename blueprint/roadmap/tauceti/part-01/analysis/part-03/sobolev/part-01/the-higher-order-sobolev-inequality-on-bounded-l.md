---
declaration: theorem
origin: cited
lean: TauCeti.Wkp.exists_eLpNorm_value_le_of_isLipschitzDomainWith
statement: formalized
proof: formalized
---

# The higher-order Sobolev inequality on bounded Lipschitz domains

If `Ω ⊆ ℝ × E` is a
bounded Lipschitz domain of dimension `n`, `1 ≤ p`, and `1/q + k/n = 1/p` with `q < ∞`, then for
every `r ≤ q` there is a constant `C` with `‖u‖_{L^r(Ω)} ≤ C ‖u‖_{W^{k,p}(Ω)}`.

```lean
TauCeti.Wkp.exists_eLpNorm_value_le_of_isLipschitzDomainWith.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {Ω : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {L : NNReal} {p : ENNReal}
  [Fact (1 ≤ p)] (k : ℕ) {q : ENNReal} (hq : q ≠ ⊤)
  (hexp : q⁻¹ + ↑k * (↑(Module.finrank ℝ (WithLp 2 (ℝ × E))))⁻¹ = p⁻¹)
  (hΩ : (↑Ω).IsLipschitzDomainWith L) (hb : Bornology.IsBounded ↑Ω) {r : ENNReal} (hr : r ≤ q) :
  ∃ C,
    ∀ (u : TauCeti.Wkp MeasureTheory.volume Ω p k),
      MeasureTheory.eLpNorm (↑↑(TauCeti.Wkp.value k u)) r (MeasureTheory.volume.restrict ↑Ω) ≤
        ↑C * ‖u‖ₑ
```

## Depends on

- [TauCeti.Wkp](../../../part-01/partial-differential-equations/tauceti-wkp.md)

## Proof depends on

- [Extension theorem for bounded Lipschitz domains](extension-theorem-for-bounded-lipschitz-domains.md)
- [The Gagliardo–Nirenberg–Sobolev inequality in dimension two](the-gagliardo-nirenberg-sobolev-inequality-in-di.md)
- [The Sobolev inequality on `W^{1,p}_0` of a ball](../part-02/the-sobolev-inequality-on-w-1-p-0-of-a-ball.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Wkp.exists_eLpNorm_value_le_of_isLipschitzDomainWith`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/Wkp/Embedding.html#TauCeti.Wkp.exists_eLpNorm_value_le_of_isLipschitzDomainWith).

## Sources

- [Tau Ceti documentation: `TauCeti.Wkp.exists_eLpNorm_value_le_of_isLipschitzDomainWith`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/Wkp/Embedding.html#TauCeti.Wkp.exists_eLpNorm_value_le_of_isLipschitzDomainWith)
- [Source of `TauCeti.Wkp.exists_eLpNorm_value_le_of_isLipschitzDomainWith` in TauCeti/Analysis/Sobolev/LipschitzDomain/Wkp/Embedding.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/LipschitzDomain/Wkp/Embedding.lean#L187)
