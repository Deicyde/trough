---
declaration: theorem
origin: cited
lean: TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent_eq_one_iff
statement: formalized
proof: formalized
---

# TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent_eq_one_iff

For `0 < n`, Serre's mass formula over a set of representatives,
`∑_{M ∈ R} 1 / (#Aut_K(M) · q ^ c(M)) = 1`, is equivalent to the mass formula over `σ_K(n)`,
`∑_{L ∈ σ_K(n)} q ^ (-c(L)) = n`.

```lean
TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent_eq_one_iff.{u_1}
  {K : Type u_1} [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  {n : ℕ} {R : Set (IntermediateField K (SeparableClosure K))}
  (hR : TauCeti.IsRepresentativeSet n R) (hn : 0 < n) :
  ∑' (M : ↑R),
        1 /
          (↑(Nat.card Gal(↥↑M/K)) *
            ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
              (↑M).wildExponent) =
      1 ↔
    ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree K n)),
        1 /
          ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
            (↑L).wildExponent =
      ↑n
```

## Depends on

- [IntermediateField.wildExponent](intermediatefield-wildexponent.md)
- [TauCeti.totallyRamifiedOfDegree](tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [The orbit count (\[Serre 1978, Remarque 3°\])](the-orbit-count-serre-1978-remarque-3.md)
- [TauCeti.algebraicExtensionNormedField](../../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Representative.html#TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent_eq_one_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Representative.html#TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent_eq_one_iff)
- [Source of `TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent_eq_one_iff` in TauCeti/NumberTheory/LocalField/MassFormula/Representative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Representative.lean#L163)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
