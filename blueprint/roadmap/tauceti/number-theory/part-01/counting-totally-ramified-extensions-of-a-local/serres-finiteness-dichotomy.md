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

- [IntermediateField.wildExponent](intermediatefield-wildexponent.md)
- [TauCeti.totallyRamifiedOfDegree](tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [Infinitely many totally ramified extensions in equal characteristic](infinitely-many-totally-ramified-extensions-in-e.md)
- [Serre's first mass formula](serres-first-mass-formula.md)
- [The wild exponent is bounded on `σ_K(n)` away from equal characteristic `p ∣ n`](the-wild-exponent-is-bounded-on-k-n-away-from-eq.md)

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
- [Source of `TauCeti.infinite_totallyRamifiedOfDegree_iff` in TauCeti/NumberTheory/LocalField/MassFormula/Main.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Main.lean#L97)
