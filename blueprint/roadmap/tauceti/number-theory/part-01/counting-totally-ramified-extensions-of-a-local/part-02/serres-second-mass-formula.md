---
declaration: theorem
origin: cited
lean: TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent
statement: formalized
proof: formalized
---

# Serre's second mass formula

for `0 < n` and every set `R` of representatives of the
`K`-isomorphism classes in `σ_K(n)`, `∑_{M ∈ R} 1 / (#Aut_K(M) · q ^ c(M)) = 1`.

```lean
TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent.{u_1}
  {K : Type u_1} [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  {n : ℕ} {R : Set (IntermediateField K (SeparableClosure K))}
  (hR : TauCeti.IsRepresentativeSet n R) (hn : 0 < n) :
  ∑' (M : ↑R),
      1 /
        (↑(Nat.card Gal(↥↑M/K)) *
          ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
            (↑M).wildExponent) =
    1
```

## Depends on

- [IntermediateField.wildExponent](../part-01/intermediatefield-wildexponent.md)
- [TauCeti.totallyRamifiedOfDegree](../part-01/tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [Serre's first mass formula](../part-01/serres-first-mass-formula.md)
- [TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent_eq_one_iff](../part-01/tauceti-isrepresentativeset-tsum-one-div-natcard.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent).

## Sources

- [Tau Ceti documentation: `TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent)
- [Source of `TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent` in TauCeti/NumberTheory/LocalField/MassFormula/Main.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Main.lean#L87)
