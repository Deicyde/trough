---
declaration: def
origin: cited
lean: TauCeti.Iwasawa.charDivisor
statement: formalized
---

# TauCeti.Iwasawa.charDivisor

The *characteristic divisor* `div_A(M) = Σ_𝔭 length_{A_𝔭}(M_𝔭) [𝔭]` of a module `M` over a
commutative ring `A`, the sum running over the primes `𝔭` of height one. It is meaningful when `A`
is noetherian and `M` is finitely generated and torsion: then each `M_𝔭` has finite length, which
is the value at `𝔭` (`coe_charDivisor_apply`), and only finitely many of them are nonzero.

```lean
TauCeti.Iwasawa.charDivisor.{u_1, u_2} (A : Type u_1) [CommRing A] (M : Type u_2) [AddCommGroup M]
  [_root_.Module A M] : PrimeSpectrum A →₀ ℕ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Iwasawa.charDivisor`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/Char/Divisor.html#TauCeti.Iwasawa.charDivisor).

## Sources

- [Tau Ceti documentation: `TauCeti.Iwasawa.charDivisor`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/Char/Divisor.html#TauCeti.Iwasawa.charDivisor)
- [Source of `TauCeti.Iwasawa.charDivisor` in TauCeti/RingTheory/Iwasawa/Char/Divisor.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Iwasawa/Char/Divisor.lean#L92)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
