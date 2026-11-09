---
declaration: theorem
origin: cited
lean: TauCeti.measure_eisensteinSet
statement: formalized
proof: formalized
---

# The volume of the Eisenstein region

for a left-invariant measure on `Fin n → K`
normalized on the integer box, the Eisenstein region has volume `q ^ (-n) (1 - q⁻¹)` for
`0 < n`, where `q = Nat.card 𝓀[K]`.

```lean
TauCeti.measure_eisensteinSet.{u_1} {K : Type u_1} [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] {n : ℕ} (hn : 0 < n) [MeasurableSpace (Fin n → K)]
  [BorelSpace (Fin n → K)] (μ : MeasureTheory.Measure (Fin n → K)) [μ.IsAddLeftInvariant]
  (hμ : μ (TauCeti.integerBox K (Fin n)) = 1) :
  μ (TauCeti.eisensteinSet K n) =
    1 / ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^ n *
      (1 - 1 / ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)))
```

## Depends on

- [TauCeti.eisensteinSet](tauceti-eisensteinset.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.measure_eisensteinSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Eisenstein/Region.html#TauCeti.measure_eisensteinSet).

## Sources

- [Tau Ceti documentation: `TauCeti.measure_eisensteinSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Eisenstein/Region.html#TauCeti.measure_eisensteinSet)
- [Source of `TauCeti.measure_eisensteinSet` in TauCeti/NumberTheory/LocalField/MassFormula/Eisenstein/Region.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Eisenstein/Region.lean#L211)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
