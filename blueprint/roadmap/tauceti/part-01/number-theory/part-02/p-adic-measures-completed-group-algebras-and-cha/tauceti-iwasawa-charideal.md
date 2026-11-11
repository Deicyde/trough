---
declaration: def
origin: cited
lean: TauCeti.Iwasawa.charIdeal
statement: formalized
---

# TauCeti.Iwasawa.charIdeal

The *characteristic ideal* `char_A(M) = ∏_𝔭 𝔭 ^ length_{A_𝔭}(M_𝔭)` of a module `M` over a
commutative ring `A`, the product running over the primes `𝔭` of height one, with exponents the
multiplicities of the characteristic divisor `div_A(M)`. It is meant for finitely generated
torsion modules over a noetherian ring, where the product is finite, and it is principal over a
unique factorization domain (`charIdeal_isPrincipal`).

```lean
TauCeti.Iwasawa.charIdeal.{u_1, u_2} (A : Type u_1) [CommRing A] (M : Type u_2) [AddCommGroup M]
  [_root_.Module A M] : Ideal A
```

## Depends on

- [TauCeti.Iwasawa.charDivisor](tauceti-iwasawa-chardivisor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Iwasawa.charIdeal`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/Char/Ideal.html#TauCeti.Iwasawa.charIdeal).

## Sources

- [Tau Ceti documentation: `TauCeti.Iwasawa.charIdeal`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/Char/Ideal.html#TauCeti.Iwasawa.charIdeal)
- [Source of `TauCeti.Iwasawa.charIdeal` in TauCeti/RingTheory/Iwasawa/Char/Ideal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Iwasawa/Char/Ideal.lean#L78)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
