---
declaration: section
origin: cited
lean: CochainComplex.ComputingTor.derivedTensorProduct, CochainComplex.DerivedExtensionScalars.derivedExtensionScalars
statement: formalized
proof: formalized
---

# 15.58 Computing Tor

Section 15.58 of the Stacks Project, [Tag 064F](https://stacks.math.columbia.edu/tag/064F). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 064G, an equation

[Tag 064G](https://stacks.math.columbia.edu/tag/064G) in the Stacks Project.

**`CochainComplex.ComputingTor.derivedTensorProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/Computing.lean, line 517](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/Computing.lean#L517).

> **Stacks 064G.** For every `R`-module `M`, the total left derived tensor product
> `- ⊗ᴸ_R M : D⁻(R) ⟶ D⁻(R)` exists.

```lean
public def derivedTensorProduct (M : ModuleCat.{u} R) : TotalDerivedTensor M
```

## Tag 064H, an equation

[Tag 064H](https://stacks.math.columbia.edu/tag/064H) in the Stacks Project.

**`CochainComplex.DerivedExtensionScalars.derivedExtensionScalars`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedExtensionScalars.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/DerivedExtensionScalars.lean#L190). References: SGA 4½ Rapport (4.1), “special case”.

> **Stacks 064H.** Derived extension of scalars on bounded-above derived categories.
> This is the dual of the bounded-below right derived functor of extension of scalars on
> opposite module categories, where projective modules become injective objects.

```lean
public def derivedExtensionScalars (f : R →+* A)
    [HasDerivedCategory.{wR} (ModuleCat.{max uA (max uR v)} R)]
    [HasDerivedCategory.{wA} (ModuleCat.{max uA (max uR v)} A)]
    [HasDerivedCategory (ModuleCat.{max uA (max uR v)} R)ᵒᵖ]
    [HasDerivedCategory (ModuleCat.{max uA (max uR v)} A)ᵒᵖ] :
    DerivedCategory.Minus (ModuleCat.{max uA (max uR v)} R) ⥤
      DerivedCategory.Minus (ModuleCat.{max uA (max uR v)} A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.58, Tag 064F](https://stacks.math.columbia.edu/tag/064F)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
