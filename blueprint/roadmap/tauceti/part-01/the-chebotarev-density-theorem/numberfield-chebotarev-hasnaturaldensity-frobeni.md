---
declaration: theorem
origin: cited
lean: NumberField.Chebotarev.hasNaturalDensity_frobeniusPrimeSet
statement: formalized
proof: formalized
---

# NumberField.Chebotarev.hasNaturalDensity\_frobeniusPrimeSet

Natural-density Chebotarev: among the primes of `K`, the primes with arithmetic Frobenius
class `C` have density `#C / #Gal(L/K)`.

```lean
NumberField.Chebotarev.hasNaturalDensity_frobeniusPrimeSet.{u_1, u_2} (K : Type u_1) (L : Type u_2)
  [Field K] [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (C : ConjClasses Gal(L/K)) :
  NumberField.Set.HasNaturalDensity (NumberField.Chebotarev.frobeniusPrimeSet K L C)
    (↑(Nat.card ↑C.carrier) / ↑(Nat.card Gal(L/K)))
```

## Depends on

- [The primes of `K` with Artin class `C` in `L`](the-primes-of-k-with-artin-class-c-in-l.md)

## Proof depends on

- [The fixed-field Frobenius fiber count](the-fixed-field-frobenius-fiber-count.md)
- [Weighted Chebotarev for abelian extensions](weighted-chebotarev-for-abelian-extensions.md)

## Lean

Formalized in Tau Ceti as [`NumberField.Chebotarev.hasNaturalDensity_frobeniusPrimeSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/PrimeCounting/FrobeniusPrimeCount.html#NumberField.Chebotarev.hasNaturalDensity_frobeniusPrimeSet).

## Sources

- [Tau Ceti documentation: `NumberField.Chebotarev.hasNaturalDensity_frobeniusPrimeSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/PrimeCounting/FrobeniusPrimeCount.html#NumberField.Chebotarev.hasNaturalDensity_frobeniusPrimeSet)
- [Source of `NumberField.Chebotarev.hasNaturalDensity_frobeniusPrimeSet` in TauCeti/NumberTheory/Chebotarev/PrimeCounting/FrobeniusPrimeCount.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Chebotarev/PrimeCounting/FrobeniusPrimeCount.lean#L106)
- [Tau Ceti roadmap status: The Chebotarev density theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Chebotarev/STATUS.md)
