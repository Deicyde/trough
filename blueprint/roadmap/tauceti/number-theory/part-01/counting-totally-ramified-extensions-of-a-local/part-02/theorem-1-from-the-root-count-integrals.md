---
declaration: theorem
origin: cited
lean: TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_of_lintegral_rootCount_eq
statement: formalized
proof: formalized
---

# Theorem 1 from the root-count integrals

if, for Haar measure normalized on the integer
box, the root count of each `L ∈ σ_K(n)` integrates over the Eisenstein region to Serre's value
`q ^ (-(d(L) + 1)) (1 - q⁻¹)`, then `∑ q ^ (-c(L)) = n`.

```lean
TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_of_lintegral_rootCount_eq.{u_1}
  {K : Type u_1} [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  {n : ℕ} [MeasurableSpace (Fin n → K)] [BorelSpace (Fin n → K)] (hn : 0 < n)
  (μ : MeasureTheory.Measure (Fin n → K)) [μ.IsAddHaarMeasure]
  (hμ : μ (TauCeti.integerBox K (Fin n)) = 1)
  (h :
    ∀ L ∈ TauCeti.totallyRamifiedOfDegree K n,
      ∫⁻ (a : Fin n → K) in TauCeti.eisensteinSet K n, ↑(L.rootCount a) ∂μ =
        1 /
            ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
              (L.discriminantExponent + 1) *
          (1 - 1 / ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)))) :
  ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree K n)),
      1 /
        ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
          (↑L).wildExponent =
    ↑n
```

## Depends on

- [IntermediateField.rootCount](../part-01/intermediatefield-rootcount.md)
- [IntermediateField.wildExponent](../part-01/intermediatefield-wildexponent.md)
- [TauCeti.algebraicExtensionNormedField](../../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.eisensteinSet](../part-01/tauceti-eisensteinset.md)
- [TauCeti.relDiscr](../../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)
- [TauCeti.totallyRamifiedOfDegree](../part-01/tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [The first half of Dedekind's different theorem](../../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Theorem 1 in integral form](theorem-1-in-integral-form.md)
- [The volume of the Eisenstein region](../part-01/the-volume-of-the-eisenstein-region.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_of_lintegral_rootCount_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Total.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_of_lintegral_rootCount_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_of_lintegral_rootCount_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Total.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_of_lintegral_rootCount_eq)
- [Source of `TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_eq_of_lintegral_rootCount_eq` in TauCeti/NumberTheory/LocalField/MassFormula/Total.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Total.lean#L140)
