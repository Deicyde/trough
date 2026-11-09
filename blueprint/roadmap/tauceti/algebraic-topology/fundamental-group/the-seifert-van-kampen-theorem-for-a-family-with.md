---
declaration: def
origin: cited
lean: TauCeti.isColimitFundamentalGroupWideCocone, TauCeti.vanKampenWideEquiv
statement: formalized
---

# The Seifert--van Kampen theorem for a family with a common pairwise intersection

If the
interiors of the path-connected sets `U i` cover `X`, all of them contain the path-connected set
`C ∋ x`, and two distinct members meet inside `C`, then `π₁(X, x)` is the wide pushout in the
category of groups of the groups `π₁(U i, x)` over `π₁(C, x)`, along the maps induced by the
inclusions.

```lean
TauCeti.isColimitFundamentalGroupWideCocone.{u_1, u_2} {X : Type u_1} [TopologicalSpace X]
  {ι : Type u_2} {U : ι → Set X} {C : Set X} {x : X} (hU : ∀ (y : X), ∃ i, U i ∈ nhds y)
  (hUp : ∀ (i : ι), IsPathConnected (U i)) (hC : IsPathConnected C) (hCU : ∀ (i : ι), C ⊆ U i)
  (hUC : Pairwise fun i j => U i ∩ U j ⊆ C) (hx : x ∈ C) :
  CategoryTheory.Limits.IsColimit (TauCeti.fundamentalGroupWideCocone hCU hx)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Uniqueness in the Seifert--van Kampen theorem for a family](uniqueness-in-the-seifert-van-kampen-theorem-for.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isColimitFundamentalGroupWideCocone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.html#TauCeti.isColimitFundamentalGroupWideCocone).

## Other forms

**The Seifert--van Kampen theorem for a family with a simply connected common pairwise intersection.** Formalized in Tau Ceti as [`TauCeti.vanKampenWideEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.html#TauCeti.vanKampenWideEquiv).

```lean
TauCeti.vanKampenWideEquiv.{u_1, u_2} {X : Type u_1} [TopologicalSpace X] {ι : Type u_2}
  {U : ι → Set X} {C : Set X} {x : X} (hU : ∀ (y : X), ∃ i, U i ∈ nhds y)
  (hUp : ∀ (i : ι), IsPathConnected (U i)) (hC : IsSimplyConnected C) (hCU : ∀ (i : ι), C ⊆ U i)
  (hUC : Pairwise fun i j => U i ∩ U j ⊆ C) (hx : x ∈ C) :
  (Monoid.CoprodI fun i => FundamentalGroup ↑(U i) ⟨x, ⋯⟩) ≃* FundamentalGroup X x
```

## Sources

- [Tau Ceti documentation: `TauCeti.isColimitFundamentalGroupWideCocone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.html#TauCeti.isColimitFundamentalGroupWideCocone)
- [Source of `TauCeti.isColimitFundamentalGroupWideCocone` in TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.lean#L709)
