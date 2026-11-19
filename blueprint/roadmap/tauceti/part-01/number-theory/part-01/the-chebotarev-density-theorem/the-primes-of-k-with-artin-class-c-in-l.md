---
declaration: def
origin: cited
lean: NumberField.Chebotarev.frobeniusPrimeSet
statement: formalized
---

# The primes of `K` with Artin class `C` in `L`

A height-one prime `𝔭` of `𝓞 K` belongs to
`frobeniusPrimeSet K L C` when `𝔭` is unramified in `L` — so that `artinSymbol` is applicable —
and its Artin class is `C`.

The unramifiedness proof is packaged existentially rather than assumed, because `artinSymbol`
takes it as an argument and no value is assigned at a ramified prime. See
`mem_frobeniusPrimeSet_iff_artinSymbol_eq` for the form used once such a proof is available.

```lean
NumberField.Chebotarev.frobeniusPrimeSet.{u_1, u_2} (K : Type u_1) (L : Type u_2) [Field K]
  [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (C : ConjClasses Gal(L/K)) :
  Set (IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.Chebotarev.frobeniusPrimeSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/FrobeniusPrimeSet.html#NumberField.Chebotarev.frobeniusPrimeSet).

## Sources

- [Tau Ceti documentation: `NumberField.Chebotarev.frobeniusPrimeSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/FrobeniusPrimeSet.html#NumberField.Chebotarev.frobeniusPrimeSet)
- [Source of `NumberField.Chebotarev.frobeniusPrimeSet` in TauCeti/NumberTheory/Chebotarev/FrobeniusPrimeSet.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Chebotarev/FrobeniusPrimeSet.lean#L82)
- [Tau Ceti roadmap status: The Chebotarev density theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/Chebotarev/STATUS.md)
