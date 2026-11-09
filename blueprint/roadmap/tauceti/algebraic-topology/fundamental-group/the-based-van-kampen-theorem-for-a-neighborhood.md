---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_vanKampenDesc
statement: formalized
proof: formalized
---

# The based van Kampen theorem for a neighborhood cover, in universal-property form

Pairwise compatible homomorphisms out of the fundamental groups of the cover members extend
uniquely to the ambient fundamental group. Repeated indices in the triple-intersection
hypothesis imply path connectedness of the double intersections and individual members. No
common pairwise intersection is required, and the target can be any monoid.

```lean
TauCeti.existsUnique_vanKampenDesc.{u, v, w} {K : Type w} [Monoid K] {X : Type v}
  [TopologicalSpace X] {ι : Type u} (U : ι → Set X) (x : X) (hCover : ∀ (y : X), ∃ i, U i ∈ nhds y)
  (hx : ∀ (i : ι), x ∈ U i) (hTriple : ∀ (i j k : ι), IsPathConnected (U i ∩ U j ∩ U k))
  (f : (i : ι) → FundamentalGroup ↑(U i) ⟨x, ⋯⟩ →* K)
  (hcompat :
    ∀ (i j : ι),
      (f i).comp (FundamentalGroup.map (ContinuousMap.inclusion ⋯) ⟨x, ⋯⟩) =
        (f j).comp (FundamentalGroup.map (ContinuousMap.inclusion ⋯) ⟨x, ⋯⟩)) :
  ∃! d, ∀ (i : ι), d.comp (FundamentalGroup.map (ContinuousMap.subtypeVal (U i)) ⟨x, ⋯⟩) = f i
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Uniqueness in the Seifert--van Kampen theorem for a family](uniqueness-in-the-seifert-van-kampen-theorem-for.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_vanKampenDesc`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Cover.html#TauCeti.existsUnique_vanKampenDesc).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_vanKampenDesc`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Cover.html#TauCeti.existsUnique_vanKampenDesc)
- [Source of `TauCeti.existsUnique_vanKampenDesc` in TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Cover.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Cover.lean#L48)
