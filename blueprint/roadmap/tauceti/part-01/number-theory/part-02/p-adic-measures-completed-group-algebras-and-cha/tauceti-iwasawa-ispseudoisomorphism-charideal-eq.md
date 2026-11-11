---
declaration: theorem
origin: cited
lean: TauCeti.Iwasawa.IsPseudoIsomorphism.charIdeal_eq
statement: formalized
proof: formalized
---

# TauCeti.Iwasawa.IsPseudoIsomorphism.charIdeal_eq

The characteristic ideal is invariant under pseudo-isomorphism.

```lean
TauCeti.Iwasawa.IsPseudoIsomorphism.charIdeal_eq.{u_1, u_2, u_3} {A : Type u_1} [CommRing A]
  {M : Type u_2} [AddCommGroup M] [_root_.Module A M] {N : Type u_3} [AddCommGroup N]
  [_root_.Module A N] {f : M →ₗ[A] N} (hf : TauCeti.Iwasawa.IsPseudoIsomorphism f) :
  TauCeti.Iwasawa.charIdeal A M = TauCeti.Iwasawa.charIdeal A N
```

## Depends on

- [TauCeti.Iwasawa.charIdeal](tauceti-iwasawa-charideal.md)

## Proof depends on

- [TauCeti.Iwasawa.charDivisor](tauceti-iwasawa-chardivisor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Iwasawa.IsPseudoIsomorphism.charIdeal_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/Char/Ideal.html#TauCeti.Iwasawa.IsPseudoIsomorphism.charIdeal_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Iwasawa.IsPseudoIsomorphism.charIdeal_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/Char/Ideal.html#TauCeti.Iwasawa.IsPseudoIsomorphism.charIdeal_eq)
- [Source of `TauCeti.Iwasawa.IsPseudoIsomorphism.charIdeal_eq` in TauCeti/RingTheory/Iwasawa/Char/Ideal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Iwasawa/Char/Ideal.lean#L122)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
