---
declaration: theorem
origin: cited
lean: TauCeti.vanKampenWide_hom_ext
statement: formalized
proof: formalized
---

# Uniqueness in the Seifert--van Kampen theorem for a family

If the interiors of the sets
`U i ∋ x` cover `X` and their pairwise intersections are path connected, then two homomorphisms out
of `π₁(X, x)` which agree on the image of every `π₁(U i, x)` are equal.

```lean
TauCeti.vanKampenWide_hom_ext.{u_1, u_2, u_3} {X : Type u_1} [TopologicalSpace X] {ι : Type u_2}
  {U : ι → Set X} {x : X} {K : Type u_3} [Monoid K] (hU : ∀ (y : X), ∃ i, U i ∈ nhds y)
  (hx : ∀ (i : ι), x ∈ U i) (hpc : ∀ (i j : ι), IsPathConnected (U i ∩ U j))
  {f g : FundamentalGroup X x →* K}
  (hfg :
    ∀ (i : ι),
      f.comp (FundamentalGroup.map (ContinuousMap.subtypeVal (U i)) ⟨x, ⋯⟩) =
        g.comp (FundamentalGroup.map (ContinuousMap.subtypeVal (U i)) ⟨x, ⋯⟩)) :
  f = g
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.vanKampenWide_hom_ext`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.html#TauCeti.vanKampenWide_hom_ext).

## Sources

- [Tau Ceti documentation: `TauCeti.vanKampenWide_hom_ext`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.html#TauCeti.vanKampenWide_hom_ext)
- [Source of `TauCeti.vanKampenWide_hom_ext` in TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.lean#L651)
