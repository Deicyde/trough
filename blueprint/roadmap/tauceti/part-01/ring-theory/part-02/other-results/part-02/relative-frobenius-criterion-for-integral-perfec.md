---
declaration: theorem
origin: cited
lean: TauCeti.Perfectoid.IsIntegralPerfectoid.of_bijective_frobeniusModPow
statement: formalized
proof: formalized
---

# Relative Frobenius criterion for integral perfectoid rings

**Relative Frobenius criterion for integral perfectoid rings** (Bhatt–Morrow–Scholze,
*Integral `p`-adic Hodge theory*, Lemma 3.10(ii)). Let `A` be `π`-adically complete for a
nonzerodivisor `π` with `π ^ p ∣ p`. If relative Frobenius `A ⧸ (π) → A ⧸ (π ^ p)` is bijective,
then `A` is an integral perfectoid ring.

```lean
TauCeti.Perfectoid.IsIntegralPerfectoid.of_bijective_frobeniusModPow.{u_1} {p : ℕ}
  [Fact (Nat.Prime p)] {A : Type u_1} [CommRing A] {π : A} {hdvd : π ^ p ∣ ↑p}
  [IsAdicComplete (Ideal.span {π}) A] (hreg : π ∈ nonZeroDivisors A)
  (hbij : Function.Bijective ⇑(TauCeti.frobeniusModPow p hdvd)) :
  TauCeti.Perfectoid.IsIntegralPerfectoid p A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Perfectoid.IsIntegralPerfectoid.of_bijective_frobeniusModPow`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/Integral.html#TauCeti.Perfectoid.IsIntegralPerfectoid.of_bijective_frobeniusModPow).

## Sources

- [Tau Ceti documentation: `TauCeti.Perfectoid.IsIntegralPerfectoid.of_bijective_frobeniusModPow`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/Integral.html#TauCeti.Perfectoid.IsIntegralPerfectoid.of_bijective_frobeniusModPow)
- [Source of `TauCeti.Perfectoid.IsIntegralPerfectoid.of_bijective_frobeniusModPow` in TauCeti/RingTheory/Perfectoid/Integral.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Perfectoid/Integral.lean#L178)
