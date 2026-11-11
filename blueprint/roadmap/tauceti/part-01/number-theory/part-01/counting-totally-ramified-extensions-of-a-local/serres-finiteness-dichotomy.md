---
declaration: theorem
origin: cited
lean: TauCeti.infinite_totallyRamifiedOfDegree_iff, TauCeti.infinite_totallyRamifiedOfDegree_iff_or_tsum_eq_top
statement: formalized
proof: formalized
---

# Serre's finiteness dichotomy

for `0 < n`, there are infinitely many totally ramified
degree-`n` subextensions of a separable closure of `K` exactly when `K` has equal
characteristic `p`, the residue characteristic, and `p ∣ n`.

```lean
TauCeti.infinite_totallyRamifiedOfDegree_iff.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} (hn : 0 < n) :
  (TauCeti.totallyRamifiedOfDegree K n).Infinite ↔
    ringChar K = ringChar (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer) ∧
      ringChar (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer) ∣ n
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Proof depends on

- [Serre's first mass formula](serres-first-mass-formula.md)
- [The upper bound of Dedekind's different theorem](../../part-02/local-field/the-upper-bound-of-dedekinds-different-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.infinite_totallyRamifiedOfDegree_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.infinite_totallyRamifiedOfDegree_iff).

## Other forms

**Serre's finiteness dichotomy, relative to the weighted count.** Formalized in Tau Ceti as [`TauCeti.infinite_totallyRamifiedOfDegree_iff_or_tsum_eq_top`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Finite.html#TauCeti.infinite_totallyRamifiedOfDegree_iff_or_tsum_eq_top).

```lean
TauCeti.infinite_totallyRamifiedOfDegree_iff_or_tsum_eq_top.{u_1} {K : Type u_1} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} (hn : 0 < n) :
  (TauCeti.totallyRamifiedOfDegree K n).Infinite ↔
    ringChar K = ringChar (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer) ∧
        ringChar (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer) ∣ n ∨
      ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree K n)),
          1 /
            ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
              (↑L).wildExponent =
        ⊤
```

## Sources

- [Tau Ceti documentation: `TauCeti.infinite_totallyRamifiedOfDegree_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.infinite_totallyRamifiedOfDegree_iff)
- [Source of `TauCeti.infinite_totallyRamifiedOfDegree_iff` in TauCeti/NumberTheory/LocalField/MassFormula/Main.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/MassFormula/Main.lean#L97)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MassFormula/STATUS.md)
