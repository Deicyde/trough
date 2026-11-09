---
declaration: theorem
origin: cited
lean: TauCeti.SuzukiLieIndex.finiteFixedSubgroup_le_suzukiGroup
statement: formalized
proof: formalized
---

# The finite-field generation theorem

every Steinberg fixed point over the generator field
is a product of the standard generators. A fixed point fixing `∞` is a torus element times a
unipotent generator, and any other is carried to one by `w u(a, b)` for the unipotent generator
moving its last column onto the line through `e₀`.

```lean
TauCeti.SuzukiLieIndex.finiteFixedSubgroup_le_suzukiGroup (m : ℕ)
  (hvalid : (TauCeti.LieTypeIndex.suzuki m).Valid) :
  TauCeti.SuzukiLieIndex.finiteFixedSubgroup m hvalid ≤ TauCeti.suzukiGroup m
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy--Binet for `2 × 2` minors](../../linear-algebra/matrix/cauchy-binet-for-2-2-minors.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SuzukiLieIndex.finiteFixedSubgroup_le_suzukiGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/Suzuki/Generation.html#TauCeti.SuzukiLieIndex.finiteFixedSubgroup_le_suzukiGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.SuzukiLieIndex.finiteFixedSubgroup_le_suzukiGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/Suzuki/Generation.html#TauCeti.SuzukiLieIndex.finiteFixedSubgroup_le_suzukiGroup)
- [Source of `TauCeti.SuzukiLieIndex.finiteFixedSubgroup_le_suzukiGroup` in TauCeti/GroupTheory/SpecificGroups/CFSG/Suzuki/Generation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/SpecificGroups/CFSG/Suzuki/Generation.lean#L328)
