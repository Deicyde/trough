---
declaration: theorem
origin: cited
lean: TauCeti.IsGoodDixonPrime.nonempty_center_algEquiv_conjClasses
statement: formalized
proof: formalized
---

# The good-prime structure theorem

At a good Dixon prime the centre of `ZMod p [G]` is the
algebra of `ZMod p`-valued functions on the conjugacy classes of `G`.

This is what guarantees that the class-multiplication matrices are simultaneously diagonalizable
over `ZMod p` with exactly `r` distinct common eigenrows, so that the eigenvector search of the
Burnside--Dixon--Schneider algorithm terminates in one-dimensional common eigenspaces, with no
bad-prime merging of distinct central characters.

```lean
TauCeti.IsGoodDixonPrime.nonempty_center_algEquiv_conjClasses.{u_1} {G : Type u_1} [Group G] {p : ℕ}
  (hp : TauCeti.IsGoodDixonPrime G p) :
  Nonempty
    (↥(Subalgebra.center (ZMod p) (MonoidAlgebra (ZMod p) G)) ≃ₐ[ZMod p] ConjClasses G → ZMod p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The good-splitting structure theorem for a finite coefficient field](the-good-splitting-structure-theorem-for-a-finit.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsGoodDixonPrime.nonempty_center_algEquiv_conjClasses`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Dixon/Structure.html#TauCeti.IsGoodDixonPrime.nonempty_center_algEquiv_conjClasses).

## Sources

- [Tau Ceti documentation: `TauCeti.IsGoodDixonPrime.nonempty_center_algEquiv_conjClasses`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Dixon/Structure.html#TauCeti.IsGoodDixonPrime.nonempty_center_algEquiv_conjClasses)
- [Source of `TauCeti.IsGoodDixonPrime.nonempty_center_algEquiv_conjClasses` in TauCeti/RepresentationTheory/CharacterTable/Dixon/Structure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/CharacterTable/Dixon/Structure.lean#L73)
