---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.isCompactlyGenerated_derivedCategory_bigProetaleOver, AlgebraicGeometry.ProEtale.isCompactlyGenerated_derivedCategory_bigProetaleOver_abelian, AlgebraicGeometry.ProEtale.isCompactlyGenerated_derivedCategory_bigProetaleOver_constant, AlgebraicGeometry.ProEtale.isCompactlyGenerated_derivedCategory_smallProetale, AlgebraicGeometry.ProEtale.isCompactlyGenerated_derivedCategory_smallProetale_constant, AlgebraicGeometry.ProEtale.isCompactlyGenerated_derivedCategory_smallProetale_abelian
statement: formalized
proof: formalized
---

# 61.15 Compact generation

Section 61.15 of the Stacks Project, [Tag 0994](https://stacks.math.columbia.edu/tag/0994). 1 tag here is carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F4Q, a lemma

[Tag 0F4Q](https://stacks.math.columbia.edu/tag/0F4Q) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isCompactlyGenerated_derivedCategory_bigProetaleOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean#L326). The attribute's comment: “clause (6): the derived category of sheaves of modules over a sheaf of rings on the big pro-étale site (Sch/S)\_proétale of a scheme S in a chosen big pro-étale site”.

> For a sheaf of rings `𝒜` on the big pro-étale site of a scheme `S`, the unbounded derived
> category of sheaves of `𝒜`-modules is compactly generated.

```lean
theorem isCompactlyGenerated_derivedCategory_bigProetaleOver
    (𝒜 : Sheaf (BigProetaleOver.topology B S hS) RingCat.{u + 1}) :
    Pretriangulated.IsCompactlyGenerated.{u + 1}
      (DerivedCategory (SheafOfModules.{u + 1} 𝒜))
```

**`AlgebraicGeometry.ProEtale.isCompactlyGenerated_derivedCategory_bigProetaleOver_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean#L366). The attribute's comment: “clause (4): the derived category of abelian sheaves on the big pro-étale site (Sch/S)\_proétale of a scheme S in a chosen big pro-étale site”.

> The unbounded derived category of abelian sheaves on the big pro-étale site of a scheme `S`
> is compactly generated.

```lean
theorem isCompactlyGenerated_derivedCategory_bigProetaleOver_abelian :
    Pretriangulated.IsCompactlyGenerated.{u + 1}
      (DerivedCategory (Sheaf (BigProetaleOver.topology B S hS) AddCommGrpCat.{u + 1}))
```

**`AlgebraicGeometry.ProEtale.isCompactlyGenerated_derivedCategory_bigProetaleOver_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean#L383). The attribute's comment: “clause (5): the derived category of sheaves of Λ-modules, for a ring Λ, on the big pro-étale site (Sch/S)\_proétale of a scheme S in a chosen big pro-étale site”.

> For a ring `Λ`, the unbounded derived category of sheaves of `Λ`-modules on the big
> pro-étale site of a scheme `S`, the sheaves of modules over the constant sheaf of rings with
> value `Λ`, is compactly generated.

```lean
theorem isCompactlyGenerated_derivedCategory_bigProetaleOver_constant (Λ : Type u) [Ring Λ] :
    Pretriangulated.IsCompactlyGenerated.{u + 1}
      (DerivedCategory (SheafOfModules.{u + 1}
        ((constantSheaf (BigProetaleOver.topology B S hS) RingCat.{u + 1}).obj
          (RingCat.of (ULift.{u + 1} Λ)))))
```

**`AlgebraicGeometry.ProEtale.isCompactlyGenerated_derivedCategory_smallProetale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean#L394). The attribute's comment: “clause (3): the derived category of sheaves of modules over a sheaf of rings on the small pro-étale site S\_proétale of a scheme S in a chosen big pro-étale site”.

> For a sheaf of rings `𝒜` on the small pro-étale site of a scheme `S`, the unbounded derived
> category of sheaves of `𝒜`-modules is compactly generated.

```lean
theorem isCompactlyGenerated_derivedCategory_smallProetale
    (𝒜 : Sheaf (SmallProetale.topology B S hS) RingCat.{u + 1}) :
    Pretriangulated.IsCompactlyGenerated.{u + 1}
      (DerivedCategory (SheafOfModules.{u + 1} 𝒜))
```

**`AlgebraicGeometry.ProEtale.isCompactlyGenerated_derivedCategory_smallProetale_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean#L412). The attribute's comment: “clause (2): the derived category of sheaves of Λ-modules, for a ring Λ, on the small pro-étale site S\_proétale of a scheme S in a chosen big pro-étale site”.

> For a ring `Λ`, the unbounded derived category of sheaves of `Λ`-modules on the small
> pro-étale site of a scheme `S`, the sheaves of modules over the constant sheaf of rings with
> value `Λ`, is compactly generated.

```lean
theorem isCompactlyGenerated_derivedCategory_smallProetale_constant (Λ : Type u) [Ring Λ] :
    Pretriangulated.IsCompactlyGenerated.{u + 1}
      (DerivedCategory (SheafOfModules.{u + 1}
        ((constantSheaf (SmallProetale.topology B S hS) RingCat.{u + 1}).obj
          (RingCat.of (ULift.{u + 1} Λ)))))
```

**`AlgebraicGeometry.ProEtale.isCompactlyGenerated_derivedCategory_smallProetale_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean#L423). The attribute's comment: “clause (1): the derived category of abelian sheaves on the small pro-étale site S\_proétale of a scheme S in a chosen big pro-étale site”.

> The unbounded derived category of abelian sheaves on the small pro-étale site of a scheme
> `S` is compactly generated.

```lean
theorem isCompactlyGenerated_derivedCategory_smallProetale_abelian :
    Pretriangulated.IsCompactlyGenerated.{u + 1}
      (DerivedCategory (Sheaf (SmallProetale.topology B S hS) AddCommGrpCat.{u + 1}))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.15, Tag 0994](https://stacks.math.columbia.edu/tag/0994)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
