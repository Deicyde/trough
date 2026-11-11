---
declaration: theorem
origin: cited
lean: HeckeCosetModule.mul_comm_of_antiInvolution
statement: formalized
proof: formalized
---

# Shimura's commutativity criterion (Proposition 3.8 of [Shimura][shimura1971])

the
Hecke ring over a commutative semiring is commutative when an anti-involution fixes every
double coset.

```lean
HeckeCosetModule.mul_comm_of_antiInvolution.{u_1, u_2} {G : Type u_1} [Group G] (R : Type u_2)
  {Δ : Submonoid G} {H : Subgroup G} [IsHeckeTriple Δ H H] [CommSemiring R]
  (ι : HeckeAntiInvolution Δ H) (h_fix : ∀ (D : HeckeCoset Δ H H), ι.onHeckeCoset D = D)
  (f g : HeckeRing Δ H R) : f * g = g * f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HeckeCosetModule.mul_comm_of_antiInvolution`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/Commutativity.html#HeckeCosetModule.mul_comm_of_antiInvolution).

## Sources

- [Tau Ceti documentation: `HeckeCosetModule.mul_comm_of_antiInvolution`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/Commutativity.html#HeckeCosetModule.mul_comm_of_antiInvolution)
- [Source of `HeckeCosetModule.mul_comm_of_antiInvolution` in TauCeti/NumberTheory/HeckeRing/Commutativity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/HeckeRing/Commutativity.lean#L456)
