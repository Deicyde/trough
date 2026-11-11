---
declaration: theorem
origin: cited
lean: TauCeti.hasSum_one_div_natCard_residueField_pow_wildExponent
statement: formalized
proof: formalized
---

# The real form of the first mass formula

the real series
`∑_{L ∈ σ_K(n)} q ^ (-c(L))` converges to `n`, also when `σ_K(n)` is infinite.

```lean
TauCeti.hasSum_one_div_natCard_residueField_pow_wildExponent.{u_1} {K : Type u_1} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} :
  HasSum
    (fun L =>
      1 /
        ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
          (↑L).wildExponent)
    ↑n
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Proof depends on

- [Serre's first mass formula](serres-first-mass-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasSum_one_div_natCard_residueField_pow_wildExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.hasSum_one_div_natCard_residueField_pow_wildExponent).

## Sources

- [Tau Ceti documentation: `TauCeti.hasSum_one_div_natCard_residueField_pow_wildExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.hasSum_one_div_natCard_residueField_pow_wildExponent)
- [Source of `TauCeti.hasSum_one_div_natCard_residueField_pow_wildExponent` in TauCeti/NumberTheory/LocalField/MassFormula/Main.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/MassFormula/Main.lean#L107)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MassFormula/STATUS.md)
