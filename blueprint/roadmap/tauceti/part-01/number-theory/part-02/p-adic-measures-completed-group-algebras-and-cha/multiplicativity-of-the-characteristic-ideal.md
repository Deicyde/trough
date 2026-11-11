---
declaration: theorem
origin: cited
lean: TauCeti.Iwasawa.charIdeal_eq_mul_of_exact
statement: formalized
proof: formalized
---

# Multiplicativity of the characteristic ideal

In a short exact sequence
`0 → M → N → P → 0` of finitely generated torsion modules over a noetherian ring,
`char_A(N) = char_A(M) * char_A(P)`.

```lean
TauCeti.Iwasawa.charIdeal_eq_mul_of_exact.{u_1, u_2, u_3, u_4} {A : Type u_1} [CommRing A]
  {M : Type u_2} [AddCommGroup M] [_root_.Module A M] {N : Type u_3} {P : Type u_4} [AddCommGroup N]
  [_root_.Module A N] [AddCommGroup P] [_root_.Module A P] [IsNoetherianRing A] [Module.Finite A N]
  (hN : Module.IsTorsion A N) {f : M →ₗ[A] N} {g : N →ₗ[A] P} (hfg : Function.Exact ⇑f ⇑g)
  (hf : Function.Injective ⇑f) (hg : Function.Surjective ⇑g) :
  TauCeti.Iwasawa.charIdeal A N = TauCeti.Iwasawa.charIdeal A M * TauCeti.Iwasawa.charIdeal A P
```

## Depends on

- [TauCeti.Iwasawa.charIdeal](tauceti-iwasawa-charideal.md)

## Proof depends on

- [TauCeti.Iwasawa.charDivisor](tauceti-iwasawa-chardivisor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Iwasawa.charIdeal_eq_mul_of_exact`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/Char/Ideal.html#TauCeti.Iwasawa.charIdeal_eq_mul_of_exact).

## Sources

- [Tau Ceti documentation: `TauCeti.Iwasawa.charIdeal_eq_mul_of_exact`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/Char/Ideal.html#TauCeti.Iwasawa.charIdeal_eq_mul_of_exact)
- [Source of `TauCeti.Iwasawa.charIdeal_eq_mul_of_exact` in TauCeti/RingTheory/Iwasawa/Char/Ideal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Iwasawa/Char/Ideal.lean#L127)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
