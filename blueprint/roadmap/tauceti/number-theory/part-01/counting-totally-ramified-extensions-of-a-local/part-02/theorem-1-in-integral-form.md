---
declaration: theorem
origin: cited
lean: TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_iff_tsum_lintegral_rootCount_eq
statement: formalized
proof: formalized
---

# Theorem 1 in integral form

for any additive Haar measure `μ`, the weighted count
`∑ q ^ (-c(L))` of the totally ramified degree-`n` subextensions equals `n` exactly when the
root-count integrals add up to `∑ q ^ (-c(L)) * μ(E_n)`, where `E_n` is the Eisenstein region.
The total of the integrals is `n * μ(E_n)`, and `μ(E_n)` is positive and finite.

```lean
TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_iff_tsum_lintegral_rootCount_eq.{u_1}
  {K : Type u_1} [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  {n : ℕ} [MeasurableSpace (Fin n → K)] [BorelSpace (Fin n → K)] (hn : 0 < n)
  (μ : MeasureTheory.Measure (Fin n → K)) [μ.IsAddHaarMeasure] :
  ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree K n)),
        1 /
          ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
            (↑L).wildExponent =
      ↑n ↔
    ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree K n)),
        ∫⁻ (a : Fin n → K) in TauCeti.eisensteinSet K n, ↑((↑L).rootCount a) ∂μ =
      ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree K n)),
        1 /
            ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
              (↑L).wildExponent *
          μ (TauCeti.eisensteinSet K n)
```

## Depends on

- [IntermediateField.rootCount](../part-01/intermediatefield-rootcount.md)
- [IntermediateField.wildExponent](../part-01/intermediatefield-wildexponent.md)
- [TauCeti.eisensteinSet](../part-01/tauceti-eisensteinset.md)
- [TauCeti.totallyRamifiedOfDegree](../part-01/tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [Local constancy of the root count](../part-01/local-constancy-of-the-root-count.md)
- [The root counts over `σ_K(n)` sum to `n`](../part-01/the-root-counts-over-k-n-sum-to-n.md)
- [TauCeti.algebraicExtensionNormedField](../../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [The volume of the Eisenstein region](../part-01/the-volume-of-the-eisenstein-region.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_iff_tsum_lintegral_rootCount_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Total.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_iff_tsum_lintegral_rootCount_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_iff_tsum_lintegral_rootCount_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Total.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_iff_tsum_lintegral_rootCount_eq)
- [Source of `TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_iff_tsum_lintegral_rootCount_eq` in TauCeti/NumberTheory/LocalField/MassFormula/Total.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Total.lean#L108)
