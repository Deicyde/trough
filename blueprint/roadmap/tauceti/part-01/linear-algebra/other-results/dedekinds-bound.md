---
declaration: theorem
origin: cited
lean: TauCeti.natCard_monoidHom_le
statement: formalized
proof: formalized
---

# Dedekind's bound

A finite monoid `G` has at most `#G` homomorphisms into a domain `M`,
since they are linearly independent in the `M`-module `G → M` of rank `#G`.

```lean
TauCeti.natCard_monoidHom_le.{u_1, u_2} (G : Type u_1) (M : Type u_2) [MulOneClass G] [Finite G]
  [CommRing M] [IsDomain M] : Nat.card (G →* M) ≤ Nat.card G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.natCard_monoidHom_le`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/LinearIndependent/MonoidHom.html#TauCeti.natCard_monoidHom_le).

## Sources

- [Tau Ceti documentation: `TauCeti.natCard_monoidHom_le`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/LinearIndependent/MonoidHom.html#TauCeti.natCard_monoidHom_le)
- [Source of `TauCeti.natCard_monoidHom_le` in TauCeti/LinearAlgebra/LinearIndependent/MonoidHom.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/LinearIndependent/MonoidHom.lean#L63)
