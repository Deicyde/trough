---
declaration: theorem
origin: cited
lean: TauCeti.isPushout_fundamentalGroup, TauCeti.vanKampenLift_bijective
statement: formalized
proof: formalized
---

# The based Seifert--van Kampen theorem

If the interiors of `A` and `B` cover `X`, the sets
`A`, `B` and `A ∩ B` are path connected, and all three contain the basepoint `x`, then the square
of fundamental groups induced by the inclusions of `A ∩ B` into `A` and `B` and of `A` and `B`
into `X` is a pushout of groups. That is, `π₁(X, x)` is the free product of `π₁(A, x)` and
`π₁(B, x)` amalgamated over `π₁(A ∩ B, x)`.

```lean
TauCeti.isPushout_fundamentalGroup.{u_1} {X : Type u_1} [TopologicalSpace X] {A B : Set X} {x : X}
  (hCover : interior A ∪ interior B = Set.univ) (hA : IsPathConnected A) (hB : IsPathConnected B)
  (hAB : IsPathConnected (A ∩ B)) (hxA : x ∈ A) (hxB : x ∈ B) :
  CategoryTheory.IsPushout (GrpCat.ofHom (FundamentalGroup.map (ContinuousMap.inclusion ⋯) ⟨x, ⋯⟩))
    (GrpCat.ofHom (FundamentalGroup.map (ContinuousMap.inclusion ⋯) ⟨x, ⋯⟩))
    (GrpCat.ofHom (FundamentalGroup.map (ContinuousMap.subtypeVal A) ⟨x, hxA⟩))
    (GrpCat.ofHom (FundamentalGroup.map (ContinuousMap.subtypeVal B) ⟨x, hxB⟩))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isPushout_fundamentalGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.html#TauCeti.isPushout_fundamentalGroup).

## Other forms

**The based Seifert--van Kampen theorem for a simply connected overlap.** Formalized in Tau Ceti as [`TauCeti.vanKampenLift_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.html#TauCeti.vanKampenLift_bijective).

```lean
TauCeti.vanKampenLift_bijective.{u_1} {X : Type u_1} [TopologicalSpace X] {A B : Set X} {x : X}
  (hCover : interior A ∪ interior B = Set.univ) (hA : IsPathConnected A) (hB : IsPathConnected B)
  (hAB : IsSimplyConnected (A ∩ B)) (hxA : x ∈ A) (hxB : x ∈ B) :
  Function.Bijective ⇑(TauCeti.vanKampenLift A B x hxA hxB)
```

## Sources

- [Tau Ceti documentation: `TauCeti.isPushout_fundamentalGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.html#TauCeti.isPushout_fundamentalGroup)
- [Source of `TauCeti.isPushout_fundamentalGroup` in TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.lean#L345)
