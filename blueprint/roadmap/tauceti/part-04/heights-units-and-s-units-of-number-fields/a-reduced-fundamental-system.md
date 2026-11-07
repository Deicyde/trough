---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.Units.exists_fundSystem_prod_absLogHeight₁_le
statement: formalized
proof: formalized
---

# A reduced fundamental system

(Bugeaud–Győry, Lemma 1). Some fundamental system `ε` of
units has `∏ i, absLogHeight₁ (ε i) ≤ (r!) ^ 2 / (2 ^ (r - 1) * [K : ℚ] ^ r) * regulator K`, where
`r = rank K`. The constant is attained for `ℚ(√2)`. By Hadamard's bound
`regulator_le_prod_absLogHeight₁`, every fundamental system also has
`regulator K ≤ (2 * [K : ℚ]) ^ r * ∏ i, absLogHeight₁ (ε i)`.

```lean
TauCeti.NumberField.Units.exists_fundSystem_prod_absLogHeight₁_le.{u_1} {K : Type u_1} [Field K]
  [NumberField K] :
  ∃ ε,
    Subgroup.closure (Set.range ε) ⊔ NumberField.Units.torsion K = ⊤ ∧
      ∏ i, NumberField.absLogHeight₁ ((algebraMap (NumberField.RingOfIntegers K) K) ↑(ε i)) ≤
        ↑(NumberField.Units.rank K).factorial ^ 2 /
            (2 ^ (NumberField.Units.rank K - 1) *
              ↑(Module.finrank ℚ K) ^ NumberField.Units.rank K) *
          NumberField.Units.regulator K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Minkowski's second theorem](minkowskis-second-theorem.md)
- [ZLattice.successiveMin](zlattice-successivemin.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.Units.exists_fundSystem_prod_absLogHeight₁_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/FundamentalSystem.html#TauCeti.NumberField.Units.exists_fundSystem_prod_absLogHeight%E2%82%81_le).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.Units.exists_fundSystem_prod_absLogHeight₁_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/FundamentalSystem.html#TauCeti.NumberField.Units.exists_fundSystem_prod_absLogHeight%E2%82%81_le)
- [Source of `TauCeti.NumberField.Units.exists_fundSystem_prod_absLogHeight₁_le` in TauCeti/NumberTheory/NumberField/Units/FundamentalSystem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Units/FundamentalSystem.lean#L245)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HeightsAndUnits/STATUS.md)
