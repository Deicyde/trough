---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.FrameAlgebra.isFiniteEtaleTorsor
statement: formalized
proof: formalized
---

# The frame algebra is a torsor

For a finite étale `R`-algebra `S` of constant rank
`Fintype.card ι`, the frame algebra of `ι`-tuples of pairwise distinct points of `S` is a finite
étale `Perm ι`-torsor over `R`.

```lean
TauCeti.Algebra.FrameAlgebra.isFiniteEtaleTorsor.{u, u_1, u_2} {R : Type u} {S : Type u_1}
  [CommRing R] [CommRing S] [Algebra R S] [Algebra.Etale R S] [Module.Finite R S] {ι : Type u_2}
  [Fintype ι] [DecidableEq ι] (h : Module.rankAtStalk S = ↑(Fintype.card ι)) :
  TauCeti.Algebra.IsFiniteEtaleTorsor (Equiv.Perm ι) R (TauCeti.Algebra.FrameAlgebra R S ι)
```

## Depends on

- [TauCeti.Algebra.FrameAlgebra](tauceti-algebra-framealgebra.md)

## Proof depends on

- [Chase–Harrison–Rosenberg (`TauCeti.Algebra.isFiniteEtaleTorsor_iff`)](chase-harrison-rosenberg-tauceti-algebra-isfinit.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.FrameAlgebra.isFiniteEtaleTorsor`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Torsor/Frame.html#TauCeti.Algebra.FrameAlgebra.isFiniteEtaleTorsor).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.FrameAlgebra.isFiniteEtaleTorsor`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Torsor/Frame.html#TauCeti.Algebra.FrameAlgebra.isFiniteEtaleTorsor)
- [Source of `TauCeti.Algebra.FrameAlgebra.isFiniteEtaleTorsor` in TauCeti/RingTheory/Etale/Torsor/Frame.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Etale/Torsor/Frame.lean#L102)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
