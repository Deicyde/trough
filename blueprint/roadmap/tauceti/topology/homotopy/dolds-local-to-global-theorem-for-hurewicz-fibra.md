---
declaration: theorem
origin: cited
lean: TauCeti.isHurewiczFibration_of_partitionOfUnity
statement: formalized
proof: formalized
---

# Dold's local-to-global theorem for Hurewicz fibrations

A continuous map `p : E → B` whose
restrictions `p ⁻¹' U i → U i` over a numerable cover `(U i)_{i ∈ ι}` of `B` (witnessed by a
partition of unity `ρ` with `support (ρ i) ⊆ U i`) are Hurewicz fibrations is itself a Hurewicz
fibration.

```lean
TauCeti.isHurewiczFibration_of_partitionOfUnity.{w, u, v, u_1} {ι : Type u_1} {E : Type u}
  {B : Type v} [TopologicalSpace E] [TopologicalSpace B] {p : E → B} (hp : Continuous p)
  {U : ι → Set B} (ρ : PartitionOfUnity ι B) (hρ : ∀ (i : ι), Function.support ⇑(ρ i) ⊆ U i)
  (hpU : ∀ (i : ι), TauCeti.IsHurewiczFibration (Set.MapsTo.restrict p (p ⁻¹' U i) (U i) ⋯)) :
  TauCeti.IsHurewiczFibration p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dold's local-to-global homotopy lifting theorem](dolds-local-to-global-homotopy-lifting-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isHurewiczFibration_of_partitionOfUnity`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/HurewiczFibration/Numerable.html#TauCeti.isHurewiczFibration_of_partitionOfUnity).

## Sources

- [Tau Ceti documentation: `TauCeti.isHurewiczFibration_of_partitionOfUnity`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/HurewiczFibration/Numerable.html#TauCeti.isHurewiczFibration_of_partitionOfUnity)
- [Source of `TauCeti.isHurewiczFibration_of_partitionOfUnity` in TauCeti/Topology/Homotopy/HurewiczFibration/Numerable.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Homotopy/HurewiczFibration/Numerable.lean#L880)
