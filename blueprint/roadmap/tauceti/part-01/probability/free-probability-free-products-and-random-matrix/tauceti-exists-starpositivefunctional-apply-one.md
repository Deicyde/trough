---
declaration: theorem
origin: cited
lean: TauCeti.exists_starPositiveFunctional_apply_one_not_exists_cstar_starDistribution
statement: formalized
proof: formalized
---

# TauCeti.exists_starPositiveFunctional_apply_one_not_exists_cstar_starDistribution

Over any nonempty index type `ι`, there exists a normalized positive functional on
`StarPolynomial ℂ ι` that cannot be realized as the `⋆`-distribution of any family in any unital
C⋆-algebra (in any universe) with respect to a positive linear functional.

```lean
TauCeti.exists_starPositiveFunctional_apply_one_not_exists_cstar_starDistribution.{u_1, v}
  (ι : Type u_1) [Nonempty ι] :
  ∃ φ,
    φ 1 = 1 ∧
      ∀ (C : Type v) [inst : CStarAlgebra C] [inst_1 : PartialOrder C] [StarOrderedRing C]
        (ω : C →ₚ[ℂ] ℂ) (c : ι → C), TauCeti.starDistribution ω.toLinearMap c ≠ φ.toLinearMap
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_starPositiveFunctional_apply_one_not_exists_cstar_starDistribution`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Distribution/GNS.html#TauCeti.exists_starPositiveFunctional_apply_one_not_exists_cstar_starDistribution).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_starPositiveFunctional_apply_one_not_exists_cstar_starDistribution`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Distribution/GNS.html#TauCeti.exists_starPositiveFunctional_apply_one_not_exists_cstar_starDistribution)
- [Source of `TauCeti.exists_starPositiveFunctional_apply_one_not_exists_cstar_starDistribution` in TauCeti/Probability/FreeProbability/Distribution/GNS.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/Distribution/GNS.lean#L606)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
