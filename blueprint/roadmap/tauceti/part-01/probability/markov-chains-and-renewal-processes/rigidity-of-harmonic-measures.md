---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.eq_smul_volume_of_map_coe_conv_eq_self
statement: formalized
proof: formalized
---

# Rigidity of harmonic measures

Let `μ` be a nonlattice probability law on `ℝ≥0`. A measure
`η` on `ℝ` with `μ ∗ η = η`, the law `μ` being taken on `ℝ`, and with uniformly bounded mass on
the unit windows `[a, a + 1]`, is the multiple `η (0, 1] • volume` of Lebesgue measure.

```lean
MeasureTheory.Measure.eq_smul_volume_of_map_coe_conv_eq_self {μ : MeasureTheory.Measure NNReal}
  [MeasureTheory.IsProbabilityMeasure μ] {η : MeasureTheory.Measure ℝ} {C : NNReal}
  (hμ : ¬μ.IsLattice) (hC : ∀ (a : ℝ), η (Set.Icc a (a + 1)) ≤ ↑C)
  (hη : (MeasureTheory.Measure.map NNReal.toReal μ).conv η = η) :
  η = η (Set.Ioc 0 1) • MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Choquet–Deny theorem, harmonic functions](../../measure-theory/group/choquet-deny-theorem-harmonic-functions.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.eq_smul_volume_of_map_coe_conv_eq_self`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/HarmonicMeasure.html#MeasureTheory.Measure.eq_smul_volume_of_map_coe_conv_eq_self).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.eq_smul_volume_of_map_coe_conv_eq_self`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/HarmonicMeasure.html#MeasureTheory.Measure.eq_smul_volume_of_map_coe_conv_eq_self)
- [Source of `MeasureTheory.Measure.eq_smul_volume_of_map_coe_conv_eq_self` in TauCeti/Probability/Renewal/HarmonicMeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Renewal/HarmonicMeasure.lean#L45)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
