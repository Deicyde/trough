---
declaration: theorem
origin: cited
lean: NumberField.Chebotarev.hasNaturalDensity_setOf_map_inertiaDeg_eq
statement: formalized
proof: formalized
---

# Natural-density Chebotarev for splitting types

The primes with residue-degree multiset
`μ` in `E` have natural density the total proportion of elements whose action on
`Gal(L/K) ⧸ Gal(L/E)` has full cycle type `μ`, expressed as a sum of conjugacy-class
proportions. No normality of `E/K` or realizability hypothesis on `μ` is needed.

```lean
NumberField.Chebotarev.hasNaturalDensity_setOf_map_inertiaDeg_eq.{u_1, u_2} (K : Type u_1)
  (L : Type u_2) [Field K] [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (E : IntermediateField K L) (μ : Multiset ℕ) :
  NumberField.Set.HasNaturalDensity
    {𝔭 | Multiset.map (fun P => (↑P).inertiaDeg (NumberField.RingOfIntegers K)) Finset.univ.val = μ}
    (∑ C with (MulAction.toPerm (Quotient.out C)).fullCycleType = μ,
      ↑(Nat.card ↑C.carrier) / ↑(Nat.card Gal(L/K)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn](../../part-02/number-fields-ramification-frobenius-and-the-lmf/ideal-card-stabilizer-eq-ramificationidxin-mul-i.md)
- [NumberField.Chebotarev.hasNaturalDensity_frobeniusPrimeSet](numberfield-chebotarev-hasnaturaldensity-frobeni.md)
- [The primes of `K` with Artin class `C` in `L`](the-primes-of-k-with-artin-class-c-in-l.md)

## Lean

Formalized in Tau Ceti as [`NumberField.Chebotarev.hasNaturalDensity_setOf_map_inertiaDeg_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/PrimeCounting/SplittingType.html#NumberField.Chebotarev.hasNaturalDensity_setOf_map_inertiaDeg_eq).

## Sources

- [Tau Ceti documentation: `NumberField.Chebotarev.hasNaturalDensity_setOf_map_inertiaDeg_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/PrimeCounting/SplittingType.html#NumberField.Chebotarev.hasNaturalDensity_setOf_map_inertiaDeg_eq)
- [Source of `NumberField.Chebotarev.hasNaturalDensity_setOf_map_inertiaDeg_eq` in TauCeti/NumberTheory/Chebotarev/PrimeCounting/SplittingType.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Chebotarev/PrimeCounting/SplittingType.lean#L50)
- [Tau Ceti roadmap status: The Chebotarev density theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/Chebotarev/STATUS.md)
