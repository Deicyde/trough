---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.continuousAutToGL_surjective
statement: formalized
proof: formalized
---

# TauCeti.freeProP.continuousAutToGL\_surjective

**Every invertible matrix over `𝔽_p` comes from a continuous automorphism** of the free
pro-`p` group of finite rank: the automorphism of the Frattini quotient it defines lifts.

```lean
TauCeti.freeProP.continuousAutToGL_surjective.{u} {p : ℕ} [Fact (Nat.Prime p)] {X : Type u}
  [Fintype X] [DecidableEq X] : Function.Surjective ⇑(TauCeti.freeProP.continuousAutToGL p X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.continuousAutToGL_surjective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/GeneralLinear.html#TauCeti.freeProP.continuousAutToGL_surjective).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.continuousAutToGL_surjective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/GeneralLinear.html#TauCeti.freeProP.continuousAutToGL_surjective)
- [Source of `TauCeti.freeProP.continuousAutToGL_surjective` in TauCeti/Topology/Algebra/Group/Profinite/Free/GeneralLinear.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/GeneralLinear.lean#L81)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteArithmetic/STATUS.md)
