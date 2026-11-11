---
declaration: theorem
origin: cited
lean: TauCeti.exists_isSl2Triple_of_isNilpotent_ad
statement: formalized
proof: formalized
---

# The Jacobson–Morozov theorem

In a Lie algebra with nondegenerate
Killing form over a field of characteristic zero, every nonzero `ad`-nilpotent element `e` is the
nilpositive element of an `sl₂` triple `(h, e, f)`.

```lean
TauCeti.exists_isSl2Triple_of_isNilpotent_ad.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] {e : L}
  (he : IsNilpotent ((LieAlgebra.ad K L) e)) (he0 : e ≠ 0) : ∃ h f, IsSl2Triple h e f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobson's lemma on commutators](../../../linear-algebra/other-results/jacobsons-lemma-on-commutators.md)
- [Morozov's lemma](morozovs-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isSl2Triple_of_isNilpotent_ad`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/JacobsonMorozov.html#TauCeti.exists_isSl2Triple_of_isNilpotent_ad).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isSl2Triple_of_isNilpotent_ad`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/JacobsonMorozov.html#TauCeti.exists_isSl2Triple_of_isNilpotent_ad)
- [Source of `TauCeti.exists_isSl2Triple_of_isNilpotent_ad` in TauCeti/Algebra/Lie/Sl2/JacobsonMorozov.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Sl2/JacobsonMorozov.lean#L83)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
