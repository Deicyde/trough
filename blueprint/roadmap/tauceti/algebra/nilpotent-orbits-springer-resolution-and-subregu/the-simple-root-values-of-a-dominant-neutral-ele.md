---
declaration: theorem
origin: cited
lean: IsSl2Triple.root_apply_eq_zero_or_eq_one_or_eq_two
statement: formalized
proof: formalized
---

# The simple root values of a dominant neutral element lie in `{0, 1, 2}`

If the neutral
element `h` of an `sl₂` triple lies in the Cartan subalgebra `H` and every simple root takes a
natural value at `h`, then each simple root takes the value `0`, `1` or `2` at `h`. These values
label the weighted Dynkin diagram of the triple.

```lean
IsSl2Triple.root_apply_eq_zero_or_eq_one_or_eq_two.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L]
  [LieAlgebra.IsKilling K L] {H : LieSubalgebra K L} [H.IsCartanSubalgebra]
  [LieModule.IsTriangularizable K (↥H) L] {b : (LieAlgebra.IsKilling.rootSystem H).Base} {h : ↥H}
  {e f : L} (t : IsSl2Triple (↑h) e f) (hh : ∀ j ∈ b.support, ∃ n, ↑j h = ↑n)
  {i : ↥LieSubalgebra.root} (hi : i ∈ b.support) : ↑i h = 0 ∨ ↑i h = 1 ∨ ↑i h = 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsSl2Triple.root_apply_eq_zero_or_eq_one_or_eq_two`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/WeightedDiagram/Basic.html#IsSl2Triple.root_apply_eq_zero_or_eq_one_or_eq_two).

## Sources

- [Tau Ceti documentation: `IsSl2Triple.root_apply_eq_zero_or_eq_one_or_eq_two`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/WeightedDiagram/Basic.html#IsSl2Triple.root_apply_eq_zero_or_eq_one_or_eq_two)
- [Source of `IsSl2Triple.root_apply_eq_zero_or_eq_one_or_eq_two` in TauCeti/Algebra/Lie/Sl2/WeightedDiagram/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Sl2/WeightedDiagram/Basic.lean#L120)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
