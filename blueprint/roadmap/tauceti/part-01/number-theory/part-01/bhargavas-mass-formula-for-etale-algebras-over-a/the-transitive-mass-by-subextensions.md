---
declaration: theorem
origin: cited
lean: TauCeti.tsum_isTransitive_one_div_natCard_residueField_pow_discriminantExponent
statement: formalized
proof: formalized
---

# The transitive mass by subextensions

Summed over the transitive labelled Galois sets of
positive size `n`, the weights `q ^ (-d(ρ))` are `(n - 1)!` times the sum of `q ^ (-d(L))` over
the subextensions `L` of `SeparableClosure K` of degree `n`.

```lean
TauCeti.tsum_isTransitive_one_div_natCard_residueField_pow_discriminantExponent.{u_1} {K : Type u_1}
  [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ}
  (hn : 0 < n) :
  ∑' (ρ : { ρ // ρ.IsTransitive }),
      1 /
        ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
          (↑ρ).discriminantExponent =
    ↑(n - 1).factorial *
      ∑' (L : { L // Module.finrank K ↥L = n }),
        1 /
          ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
            (↑L).discriminantExponent
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.GaloisSet](tauceti-galoisset.md)
- [TauCeti.orbitDiscriminantExponent](tauceti-orbitdiscriminantexponent.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Proof depends on

- [Transitive Galois sets and subextensions](transitive-galois-sets-and-subextensions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_isTransitive_one_div_natCard_residueField_pow_discriminantExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/EtaleMassFormula/Mass.html#TauCeti.tsum_isTransitive_one_div_natCard_residueField_pow_discriminantExponent).

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_isTransitive_one_div_natCard_residueField_pow_discriminantExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/EtaleMassFormula/Mass.html#TauCeti.tsum_isTransitive_one_div_natCard_residueField_pow_discriminantExponent)
- [Source of `TauCeti.tsum_isTransitive_one_div_natCard_residueField_pow_discriminantExponent` in TauCeti/NumberTheory/LocalField/EtaleMassFormula/Mass.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/EtaleMassFormula/Mass.lean#L142)
- [Tau Ceti roadmap status: Bhargava's mass formula for étale algebras over a local field](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EtaleMassFormula/STATUS.md)
