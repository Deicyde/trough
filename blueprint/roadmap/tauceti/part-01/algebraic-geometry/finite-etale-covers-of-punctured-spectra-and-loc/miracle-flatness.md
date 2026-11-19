---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.flat_of_isCohenMacaulay
statement: formalized
proof: formalized
---

# Miracle flatness

Let `R → S` be a local homomorphism of Noetherian local rings with `R`
regular and `S` Cohen–Macaulay. If `dim S = dim R + dim S ⧸ 𝔪_R S`, then `S` is flat over `R`.
Here `S` need not be finite over `R`.

```lean
TauCeti.Algebra.flat_of_isCohenMacaulay.{u_1, u_2} {R : Type u_1} {S : Type u_2} [CommRing R]
  [IsRegularLocalRing R] [CommRing S] [IsLocalRing S] [IsNoetherianRing S] [Algebra R S]
  [IsLocalHom (algebraMap R S)] (hS : Module.IsCohenMacaulay S S)
  (hdim :
    ringKrullDim S =
      ringKrullDim R + ringKrullDim (S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R))) :
  Module.Flat R S
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.flat_of_isCohenMacaulay`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/MiracleFlatness.html#TauCeti.Algebra.flat_of_isCohenMacaulay).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.flat_of_isCohenMacaulay`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/MiracleFlatness.html#TauCeti.Algebra.flat_of_isCohenMacaulay)
- [Source of `TauCeti.Algebra.flat_of_isCohenMacaulay` in TauCeti/RingTheory/RegularLocalRing/MiracleFlatness.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/RegularLocalRing/MiracleFlatness.lean#L69)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LocalPurity/STATUS.md)
