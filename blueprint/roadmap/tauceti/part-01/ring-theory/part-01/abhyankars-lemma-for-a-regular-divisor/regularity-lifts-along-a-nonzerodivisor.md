---
declaration: theorem
origin: cited
lean: TauCeti.IsRegularLocalRing.of_quotient_nonZeroDivisor
statement: formalized
proof: formalized
---

# Regularity lifts along a nonzerodivisor

A Noetherian local ring with a nonzerodivisor `x`
in the maximal ideal such that `R ⧸ (x)` is a regular local ring is a regular local ring. Stacks,
Lemma 10.106.7 (00NU), first sentence.

```lean
TauCeti.IsRegularLocalRing.of_quotient_nonZeroDivisor.{u} (R : Type u) [CommRing R] [IsLocalRing R]
  [IsNoetherianRing R] {x : R} (hx : x ∈ IsLocalRing.maximalIdeal R) (hreg : x ∈ nonZeroDivisors R)
  [IsRegularLocalRing (R ⧸ Ideal.span {x})] : IsRegularLocalRing R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsRegularLocalRing.of_quotient_nonZeroDivisor`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/OfQuotient.html#TauCeti.IsRegularLocalRing.of_quotient_nonZeroDivisor).

## Sources

- [Tau Ceti documentation: `TauCeti.IsRegularLocalRing.of_quotient_nonZeroDivisor`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/OfQuotient.html#TauCeti.IsRegularLocalRing.of_quotient_nonZeroDivisor)
- [Source of `TauCeti.IsRegularLocalRing.of_quotient_nonZeroDivisor` in TauCeti/RingTheory/RegularLocalRing/OfQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/RegularLocalRing/OfQuotient.lean#L103)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
