---
declaration: abbrev
origin: cited
lean: TauCeti.Algebra.FrameAlgebra
statement: formalized
---

# TauCeti.Algebra.FrameAlgebra

The *frame algebra* of `S` indexed by `ι`: the ring of functions on the open and closed
subscheme of `ι`-tuples of pairwise distinct points of `Spec S` in the `ι`-fold fibre power of
`Spec S` over `Spec R`. It is the quotient of `⨂[R] _ : ι, S` by `1 - ε`, the factor
`ε · (⨂[R] _ : ι, S)` cut out by `TauCeti.Algebra.distinctIdempotent`.

For `S` finite étale of constant rank `n` and `ι = Fin n` this is the standard construction of a
`Perm (Fin n)`-torsor splitting `S`, the ring-theoretic Galois closure of `S`; its split model is
`TauCeti.Algebra.FrameAlgebra.permEquiv`.

```lean
TauCeti.Algebra.FrameAlgebra.{u_1, u_2, u_3} (R : Type u_1) (S : Type u_2) [CommRing R] [CommRing S]
  [Algebra R S] [Algebra.EssFiniteType R S] [Algebra.FormallyUnramified R S] (ι : Type u_3)
  [Fintype ι] [DecidableEq ι] : Type (max (max (max u_1 u_2) u_3) (max u_2 u_1) u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.FrameAlgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Unramified/Frame.html#TauCeti.Algebra.FrameAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.FrameAlgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Unramified/Frame.html#TauCeti.Algebra.FrameAlgebra)
- [Source of `TauCeti.Algebra.FrameAlgebra` in TauCeti/RingTheory/Unramified/Frame.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Unramified/Frame.lean#L209)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
