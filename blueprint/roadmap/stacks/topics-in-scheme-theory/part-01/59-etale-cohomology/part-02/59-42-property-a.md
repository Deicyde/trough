---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.smallEtalePushforwardAb_properties_of_hasPropertyA, AlgebraicGeometry.hasPropertyA_of_locallyQuasiFinite, AlgebraicGeometry.hasPropertyA_of_isIntegralHom, Stacks.EtaleCohomology.smallEtalePushforwardAb_properties_of_isIntegralHom_or_locallyQuasiFinite
statement: formalized
proof: formalized
---

# 59.42 Property (A)

Section 59.42 of the Stacks Project, [Tag 04DJ](https://stacks.math.columbia.edu/tag/04DJ). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04DK, a lemma

[Tag 04DK](https://stacks.math.columbia.edu/tag/04DK) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtalePushforwardAb_properties_of_hasPropertyA`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PropertyAPushforward.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PropertyAPushforward.lean#L281).

> **Stacks Project, Tag 04DK.** Let `f : X ⟶ Y` be a morphism of schemes with property (A).
> Then direct image of abelian sheaves on the small étale sites reflects injections and
> surjections, the counit `f^{-1} f_* F ⟶ F` is surjective for every abelian sheaf `F` on the
> small étale site of `X`, and direct image is faithful.

```lean
public theorem smallEtalePushforwardAb_properties_of_hasPropertyA {X Y : Scheme.{u}}
    (f : X ⟶ Y) (hf : HasPropertyA f) :
    (smallEtalePushforwardAb f).ReflectsMonomorphisms ∧
      (smallEtalePushforwardAb f).ReflectsEpimorphisms ∧
      (∀ F : Sheaf (smallEtaleTopology X) Ab.{u + 1},
          Epi ((smallEtaleAdjunctionAb f).counit.app F)) ∧
      (smallEtalePushforwardAb f).Faithful
```

## Tag 04DL, a lemma

[Tag 04DL](https://stacks.math.columbia.edu/tag/04DL) in the Stacks Project.

**`AlgebraicGeometry.hasPropertyA_of_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PropertyA.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PropertyA.lean#L413).

> **Stacks Project, Tag 04DL.** A separated locally quasi-finite morphism of schemes has
> property (A).

```lean
theorem hasPropertyA_of_locallyQuasiFinite {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsSeparated f] [LocallyOfFiniteType f] [LocallyQuasiFinite f] : HasPropertyA f
```

## Tag 04DM, a lemma

[Tag 04DM](https://stacks.math.columbia.edu/tag/04DM) in the Stacks Project.

**`AlgebraicGeometry.hasPropertyA_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PropertyA.lean, line 672](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PropertyA.lean#L672).

> **Stacks Project, Tag 04DM.** Every integral morphism of schemes has property (A).

```lean
theorem hasPropertyA_of_isIntegralHom {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] :
    HasPropertyA f
```

## Tag 04C9, a lemma

[Tag 04C9](https://stacks.math.columbia.edu/tag/04C9) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtalePushforwardAb_properties_of_isIntegralHom_or_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralQuasiFinitePushforward.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralQuasiFinitePushforward.lean#L70).

> Let `f : X ⟶ Y` be a morphism of schemes which is either integral, or separated and locally
> quasi-finite. Then the counit `f^{-1} f_* F ⟶ F` is surjective for every abelian sheaf `F` on the
> small étale site of `X`, direct image of abelian sheaves along the small étale sites is faithful,
> and it reflects injections and surjections.

```lean
public theorem smallEtalePushforwardAb_properties_of_isIntegralHom_or_locallyQuasiFinite
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : IsIntegralHom f ∨ (IsSeparated f ∧ LocallyOfFiniteType f ∧ LocallyQuasiFinite f)) :
    (∀ F : Sheaf (smallEtaleTopology X) Ab.{u + 1},
        Epi ((smallEtaleAdjunctionAb f).counit.app F)) ∧
      (smallEtalePushforwardAb f).Faithful ∧
      (smallEtalePushforwardAb f).ReflectsMonomorphisms ∧
      (smallEtalePushforwardAb f).ReflectsEpimorphisms
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.42, Tag 04DJ](https://stacks.math.columbia.edu/tag/04DJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
