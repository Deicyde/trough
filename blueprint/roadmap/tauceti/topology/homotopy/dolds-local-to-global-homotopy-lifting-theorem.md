---
declaration: theorem
origin: cited
lean: TauCeti.HasHomotopyLiftingProperty.of_partitionOfUnity
statement: formalized
proof: formalized
---

# Dold's local-to-global homotopy lifting theorem

Let `p : E → B` be a map and
`(U i)_{i ∈ ι}` a numerable cover of `B`, witnessed by a partition of unity
`ρ : PartitionOfUnity ι B` with `support (ρ i) ⊆ U i` for every `i`. If each restriction
`p ⁻¹' U i → U i` has the homotopy lifting property with respect to every open subset of `A`, then
`p` has the homotopy lifting property with respect to `A`.

```lean
TauCeti.HasHomotopyLiftingProperty.of_partitionOfUnity.{w, u, v, u_1} {ι : Type u_1} {E : Type u}
  {B : Type v} {A : Type w} [TopologicalSpace E] [TopologicalSpace B] [TopologicalSpace A]
  {p : E → B} {U : ι → Set B} (ρ : PartitionOfUnity ι B)
  (hρ : ∀ (i : ι), Function.support ⇑(ρ i) ⊆ U i)
  (hlift :
    ∀ (i : ι) (W : Set A),
      IsOpen W →
        TauCeti.HasHomotopyLiftingProperty (Set.MapsTo.restrict p (p ⁻¹' U i) (U i) ⋯) ↑W) :
  TauCeti.HasHomotopyLiftingProperty p A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasHomotopyLiftingProperty.of_partitionOfUnity`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/HurewiczFibration/Numerable.html#TauCeti.HasHomotopyLiftingProperty.of_partitionOfUnity).

## Sources

- [Tau Ceti documentation: `TauCeti.HasHomotopyLiftingProperty.of_partitionOfUnity`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/HurewiczFibration/Numerable.html#TauCeti.HasHomotopyLiftingProperty.of_partitionOfUnity)
- [Source of `TauCeti.HasHomotopyLiftingProperty.of_partitionOfUnity` in TauCeti/Topology/Homotopy/HurewiczFibration/Numerable.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Homotopy/HurewiczFibration/Numerable.lean#L807)
