---
declaration: theorem
origin: cited
lean: TauCeti.Probability.strictMono_cdf_stableMeasure_of_one_le
statement: formalized
proof: formalized
---

# TauCeti.Probability.strictMono_cdf_stableMeasure_of_one_le

From shape one onward, the cdf of every positive-scale stable law is strictly increasing on
the whole real line, including at full skewness.

```lean
TauCeti.Probability.strictMono_cdf_stableMeasure_of_one_le {α β : ℝ} {s : NNReal}
  (hα : α ∈ Set.Icc 1 2) (hβ : |β| ≤ 1) (hs : 0 < s) (m : ℝ) :
  StrictMono ↑(ProbabilityTheory.cdf (TauCeti.Probability.stableMeasure α β s m))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inversion theorem](../../analysis/part-03/bochner/the-inversion-theorem.md)
- [Lévy's continuity theorem, including existence](levys-continuity-theorem-including-existence.md)
- [The Lévy–Khintchine formula for stable exponents](../distributions/the-levy-khintchine-formula-for-stable-exponents.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.strictMono_cdf_stableMeasure_of_one_le`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Stable/Cdf.html#TauCeti.Probability.strictMono_cdf_stableMeasure_of_one_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.strictMono_cdf_stableMeasure_of_one_le`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Stable/Cdf.html#TauCeti.Probability.strictMono_cdf_stableMeasure_of_one_le)
- [Source of `TauCeti.Probability.strictMono_cdf_stableMeasure_of_one_le` in TauCeti/Probability/Distributions/Stable/Cdf.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Distributions/Stable/Cdf.lean#L98)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StandardDistributions/STATUS.md)
