---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.isFiniteEtaleTorsor_iff
statement: formalized
proof: formalized
---

# Chase–Harrison–Rosenberg (`TauCeti.Algebra.isFiniteEtaleTorsor_iff`)

`B` is a finite étale `G`-torsor over `A` if and only if
`A → B` is injective, `A` is the ring of invariants, and the action is free: for each `g ≠ 1` the
elements `g • b - b` generate the unit ideal of `B`.

```lean
TauCeti.Algebra.isFiniteEtaleTorsor_iff.{u_1, u_2, u_3} {G : Type u_1} {A : Type u_2} {B : Type u_3}
  [Group G] [CommRing A] [CommRing B] [Algebra A B] [MulSemiringAction G B] [SMulCommClass G A B]
  [Finite G] :
  TauCeti.Algebra.IsFiniteEtaleTorsor G A B ↔
    FaithfulSMul A B ∧
      Algebra.IsInvariant A B G ∧ ∀ (g : G), g ≠ 1 → Ideal.span (Set.range fun b => g • b - b) = ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chase–Harrison–Rosenberg (`TauCeti.MulSemiringAction.tensorToPi_bijective`)](chase-harrison-rosenberg-tauceti-mulsemiringacti.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.isFiniteEtaleTorsor_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Torsor/Basic.html#TauCeti.Algebra.isFiniteEtaleTorsor_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.isFiniteEtaleTorsor_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Torsor/Basic.html#TauCeti.Algebra.isFiniteEtaleTorsor_iff)
- [Source of `TauCeti.Algebra.isFiniteEtaleTorsor_iff` in TauCeti/RingTheory/Etale/Torsor/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Etale/Torsor/Basic.lean#L114)
