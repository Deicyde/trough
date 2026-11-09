---
declaration: def
origin: cited
lean: IsSl2Triple.contractingAction
statement: formalized
---

# The contracting action of `Kˣ` on `L` attached to an `sl₂` triple `(h, e, f)`

`c` acts by `c ^ 2 • gradingAut c⁻¹`, that is, by `c ^ (2 - j)` on the `j`-eigenspace of `ad h`
(`IsSl2Triple.contractingAction_apply_of_mem`). For an algebraic group with Lie algebra `L` and a
cocharacter `λ` with differential `h` this is `c ↦ c ^ 2 • Ad (λ c⁻¹)`. It fixes `e` and preserves
the Slodowy slice `e + ker (ad f)`, on which it extends to `c = 0`
(`IsSl2Triple.exists_contractingAction_eq`).

```lean
IsSl2Triple.contractingAction.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K] [CharZero K]
  [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] {h e f : L} (t : IsSl2Triple h e f) :
  Kˣ →* Module.End K L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsSl2Triple.contractingAction`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/SlodowySlice/Basic.html#IsSl2Triple.contractingAction).

## Sources

- [Tau Ceti documentation: `IsSl2Triple.contractingAction`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/SlodowySlice/Basic.html#IsSl2Triple.contractingAction)
- [Source of `IsSl2Triple.contractingAction` in TauCeti/Algebra/Lie/Sl2/SlodowySlice/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Sl2/SlodowySlice/Basic.lean#L133)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
