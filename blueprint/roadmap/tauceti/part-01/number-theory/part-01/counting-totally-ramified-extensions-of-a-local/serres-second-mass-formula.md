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

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Proof depends on

- [The orbit count (\[Serre 1978, Remarque 3°\])](the-orbit-count-serre-1978-remarque-3.md)
- [Serre's first mass formula](serres-first-mass-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent).

## Sources

- [Tau Ceti documentation: `TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent)
- [Source of `TauCeti.IsRepresentativeSet.tsum_one_div_natCard_algEquiv_mul_natCard_residueField_pow_wildExponent` in TauCeti/NumberTheory/LocalField/MassFormula/Main.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/MassFormula/Main.lean#L87)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MassFormula/STATUS.md)
