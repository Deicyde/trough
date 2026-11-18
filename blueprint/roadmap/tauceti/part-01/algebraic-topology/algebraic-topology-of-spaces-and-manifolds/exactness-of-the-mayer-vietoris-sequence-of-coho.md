---
declaration: theorem
origin: cited
lean: TopCat.compactSupportCohomologyMayerVietoris_exact₂
statement: formalized
proof: formalized
---

# Exactness of the Mayer–Vietoris sequence of cohomology with compact supports at `Hⁿ_c(U) ⊞ Hⁿ_c(V)`, for an open cover `X = U ∪ V` of a Hausdorff space

```lean
TopCat.compactSupportCohomologyMayerVietoris_exact₂.{v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Limits.HasCoproducts C]
  [CategoryTheory.Abelian C] (R : C) (k : Type v) [Ring k] [CategoryTheory.Linear k C] (M : C)
  {X : TopCat} (U V : TopologicalSpace.Opens ↑X) [T2Space ↑X] (hUV : U ⊔ V = ⊤) (n : ℕ) :
  { X₁ := ((TopologicalSpace.Opens.toTopCat X).obj (U ⊓ V)).compactSupportCohomology R k M n,
      X₂ :=
        ((TopologicalSpace.Opens.toTopCat X).obj U).compactSupportCohomology R k M n ⊞
          ((TopologicalSpace.Opens.toTopCat X).obj V).compactSupportCohomology R k M n,
      X₃ := X.compactSupportCohomology R k M n,
      f := TopCat.compactSupportCohomologyMayerVietorisToBiprod R k M U V n,
      g := TopCat.compactSupportCohomologyMayerVietorisFromBiprod R k M U V n, zero := ⋯ }.Exact
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Mayer–Vietoris for the complements of two closed sets, exactness at the middle term](../cohomology/mayer-vietoris-for-the-complements-of-two-closed.md)
- [The relative small-chain theorem for cochains](../cohomology/the-relative-small-chain-theorem-for-cochains.md)

## Lean

Formalized in Tau Ceti as [`TopCat.compactSupportCohomologyMayerVietoris_exact₂`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/MayerVietoris.html#TopCat.compactSupportCohomologyMayerVietoris_exact%E2%82%82).

## Sources

- [Tau Ceti documentation: `TopCat.compactSupportCohomologyMayerVietoris_exact₂`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/MayerVietoris.html#TopCat.compactSupportCohomologyMayerVietoris_exact%E2%82%82)
- [Source of `TopCat.compactSupportCohomologyMayerVietoris_exact₂` in TauCeti/AlgebraicTopology/Cohomology/CompactSupport/MayerVietoris.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/MayerVietoris.lean#L264)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
