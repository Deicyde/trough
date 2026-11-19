---
declaration: theorem
origin: cited
lean: RingHom.IsRueckert.uniqueFactorizationMonoid
statement: formalized
proof: formalized
---

# Rückert's factorial descent

If `A` is a unique factorisation domain and `B` is a domain,
then `B` is a unique factorisation domain.

```lean
RingHom.IsRueckert.uniqueFactorizationMonoid.{u_1, u_2} {A : Type u_1} {B : Type u_2} [CommRing A]
  [CommRing B] {φ : Polynomial A →+* B} {W : Set (Polynomial A)} (h : φ.IsRueckert W) [IsDomain A]
  [UniqueFactorizationMonoid A] [IsDomain B] : UniqueFactorizationMonoid B
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`RingHom.IsRueckert.uniqueFactorizationMonoid`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Rueckert.html#RingHom.IsRueckert.uniqueFactorizationMonoid).

## Sources

- [Tau Ceti documentation: `RingHom.IsRueckert.uniqueFactorizationMonoid`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Rueckert.html#RingHom.IsRueckert.uniqueFactorizationMonoid)
- [Source of `RingHom.IsRueckert.uniqueFactorizationMonoid` in TauCeti/RingTheory/Polynomial/Rueckert.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Polynomial/Rueckert.lean#L192)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
