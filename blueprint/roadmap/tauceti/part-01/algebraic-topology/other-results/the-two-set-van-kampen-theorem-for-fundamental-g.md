---
declaration: theorem
origin: cited
lean: TauCeti.isPushout_fundamentalGroupoid, TauCeti.isPushout_fundamentalGroupoidOn
statement: formalized
proof: formalized
---

# The two-set van Kampen theorem for fundamental groupoids

If the interiors of `A` and `B`
cover `X`, the square of fundamental groupoids induced by the inclusions of `A ∩ B` into `A` and
`B` and of `A` and `B` into `X` is a pushout in the category of groupoids.

```lean
TauCeti.isPushout_fundamentalGroupoid.{u} {X : Type u} [TopologicalSpace X] {A B : Set X}
  (hCover : interior A ∪ interior B = Set.univ) :
  CategoryTheory.IsPushout (FundamentalGroupoid.map (ContinuousMap.inclusion ⋯))
    (FundamentalGroupoid.map (ContinuousMap.inclusion ⋯))
    (FundamentalGroupoid.map (ContinuousMap.subtypeVal A))
    (FundamentalGroupoid.map (ContinuousMap.subtypeVal B))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isPushout_fundamentalGroupoid`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroupoid/Pushout.html#TauCeti.isPushout_fundamentalGroupoid).

## Other forms

**The two-set van Kampen theorem for fundamental groupoids on a set of basepoints.** Formalized in Tau Ceti as [`TauCeti.isPushout_fundamentalGroupoidOn`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroupoid/Pushout.html#TauCeti.isPushout_fundamentalGroupoidOn).

```lean
TauCeti.isPushout_fundamentalGroupoidOn.{u} {X : Type u} [TopologicalSpace X] {A B S : Set X}
  (hSA : ∀ x ∈ A, ∃ y ∈ S, JoinedIn A x y) (hSB : ∀ x ∈ B, ∃ y ∈ S, JoinedIn B x y)
  (hSAB : ∀ x ∈ A ∩ B, ∃ y ∈ S, JoinedIn (A ∩ B) x y)
  (hCover : interior A ∪ interior B = Set.univ) :
  CategoryTheory.IsPushout (TauCeti.FundamentalGroupoidOn.map (ContinuousMap.inclusion ⋯) ⋯)
    (TauCeti.FundamentalGroupoidOn.map (ContinuousMap.inclusion ⋯) ⋯)
    (TauCeti.FundamentalGroupoidOn.map (ContinuousMap.subtypeVal A) ⋯)
    (TauCeti.FundamentalGroupoidOn.map (ContinuousMap.subtypeVal B) ⋯)
```

## Sources

- [Tau Ceti documentation: `TauCeti.isPushout_fundamentalGroupoid`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroupoid/Pushout.html#TauCeti.isPushout_fundamentalGroupoid)
- [Source of `TauCeti.isPushout_fundamentalGroupoid` in TauCeti/AlgebraicTopology/FundamentalGroupoid/Pushout.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/FundamentalGroupoid/Pushout.lean#L162)
