---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallAffineZariski.abelian_fullyFaithful_and_essImage_iff
statement: formalized
proof: formalized
---

# 59.98 Comparing chaotic and Zariski topologies

Section 59.98 of the Stacks Project, [Tag 0F1K](https://stacks.math.columbia.edu/tag/0F1K). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F1L, a lemma

[Tag 0F1L](https://stacks.math.columbia.edu/tag/0F1L) in the Stacks Project.

**`AlgebraicGeometry.SmallAffineZariski.abelian_fullyFaithful_and_essImage_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/ChaoticAbelianComparison.lean, line 469](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/ChaoticAbelianComparison.lean#L469).

> **Stacks 0F1L.** Let `S_affine` be the affine opens of the scheme `S` with the chaotic
> topology, for which abelian sheaves are abelian presheaves, let `S_{affine,Zar}` be the same
> category with the Zariski topology, and let `ε : S_{affine,Zar} ⟶ S_affine` be the comparison.
> Then the derived direct image `Rε_* : D(S_{affine,Zar}) ⟶ D(S_affine)` is fully faithful, and an
> object `K` of `D⁺(S_affine)` is in its essential image if and only if
>
> 1. `RΓ(∅, K)` is zero in `D(Ab)`, and
> 2. whenever `U = V ∪ W` with `U, V, W` affine opens of `S` and `V, W ⊆ U` standard opens, the map
>    `c^K_{U,V,W,V ∩ W}` of Stacks 0F16 is a quasi-isomorphism.
>
> `Rε_*` is any right derived functor of `ε_*`, given with its unit `η`; condition (1) is stated
> for every affine open with empty underlying scheme, and condition (2) for every square of affine
> opens exhibiting `U` as the union of two standard opens with intersection the fourth corner.

```lean
theorem abelian_fullyFaithful_and_essImage_iff :
    Nonempty Rε.FullyFaithful ∧
      ∀ K : DerivedCategory (Sheaf (chaotic B S hS) AddCommGrpCat.{u + 1}),
        (DerivedCategory.TStructure.t
          (C := Sheaf (chaotic B S hS) AddCommGrpCat.{u + 1})).plus K →
        (Rε.essImage K ↔
          (∀ U : SmallAffineZariski B S hS, IsEmpty ((toScheme B S hS).obj U) →
              IsZero ((chaoticDerivedSections B S hS U).obj K)) ∧
            ∀ sq : Square (SmallAffineZariski B S hS), IsStandardOpenCoverSquare B S hS sq →
              (chaoticCSquareData B S hS sq).IsCSquareIso K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.98, Tag 0F1K](https://stacks.math.columbia.edu/tag/0F1K)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
