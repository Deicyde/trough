---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsIndQuasiAffine, AlgebraicGeometry.IsIndQuasiAffineHom, AlgebraicGeometry.isIndQuasiAffineHom_tfae, AlgebraicGeometry.isIndQuasiAffineHom_isZariskiLocalAtTarget, AlgebraicGeometry.isIndQuasiAffineHom_isStableUnderComposition, AlgebraicGeometry.isIndQuasiAffineHom_of_isQuasiAffineHom, AlgebraicGeometry.isIndQuasiAffineHom_of_isImmersion, AlgebraicGeometry.isIndQuasiAffineHom_of_comp
statement: formalized
proof: formalized
---

# 37.66 Ind-quasi-affine morphisms

Section 37.66 of the Stacks Project, [Tag 0AP5](https://stacks.math.columbia.edu/tag/0AP5). 8 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AP6, a definition

[Tag 0AP6](https://stacks.math.columbia.edu/tag/0AP6) in the Stacks Project.

**`AlgebraicGeometry.IsIndQuasiAffine`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/IndQuasiAffine.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/IndQuasiAffine.lean#L39). The attribute's comment: “schemes”.

> A scheme is ind-quasi-affine if each quasi-compact open subscheme is quasi-affine.

```lean
class IsIndQuasiAffine (X : Scheme.{u}) : Prop
```

**`AlgebraicGeometry.IsIndQuasiAffineHom`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/IndQuasiAffine.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/IndQuasiAffine.lean#L48). The attribute's comment: “morphisms”.

> A morphism of schemes is ind-quasi-affine if the inverse image of every affine open subscheme
> of its target is an ind-quasi-affine scheme.

```lean
class IsIndQuasiAffineHom {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop
```

## Tag 0F1U, a lemma

[Tag 0F1U](https://stacks.math.columbia.edu/tag/0F1U) in the Stacks Project.

**`AlgebraicGeometry.isIndQuasiAffineHom_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/Characterization.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/Characterization.lean#L106). The attribute's comment: “equivalent characterizations”.

> Ind-quasi-affineness of a morphism of schemes can be tested on the quasi-compact open
> subschemes above the affine opens of the target, above the members of one cover of the target by
> quasi-compact quasi-separated opens, or above all quasi-compact quasi-separated opens of the
> target.

```lean
theorem isIndQuasiAffineHom_tfae {X Y : Scheme.{u}} (f : X ⟶ Y) :
    List.TFAE [
      IsIndQuasiAffineHom f,
      ∀ (V : Y.Opens), IsAffineOpen V →
        ∀ (U : (f ⁻¹ᵁ V).toScheme.Opens), IsCompact (U : Set (f ⁻¹ᵁ V).toScheme) →
          IsQuasiAffineHom (U.ι ≫ f ∣_ V),
      ∃ (ι : Type u) (V : ι → Y.Opens),
        (iSup V = ⊤) ∧
          (∀ j, IsCompact (V j : Set Y)) ∧
          (∀ j, IsQuasiSeparated (V j : Set Y)) ∧
          (∀ j (U : (f ⁻¹ᵁ V j).toScheme.Opens),
              IsCompact (U : Set (f ⁻¹ᵁ V j).toScheme) →
                IsQuasiAffineHom (U.ι ≫ f ∣_ (V j))),
      ∀ (V : Y.Opens), IsCompact (V : Set Y) → IsQuasiSeparated (V : Set Y) →
        ∀ (U : (f ⁻¹ᵁ V).toScheme.Opens), IsCompact (U : Set (f ⁻¹ᵁ V).toScheme) →
          IsQuasiAffineHom (U.ι ≫ f ∣_ V)]
```

**`AlgebraicGeometry.isIndQuasiAffineHom_isZariskiLocalAtTarget`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/Characterization.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/Characterization.lean#L242). The attribute's comment: “Zariski locality on the base”.

> Being an ind-quasi-affine morphism is Zariski local on the base.

```lean
instance isIndQuasiAffineHom_isZariskiLocalAtTarget :
    IsZariskiLocalAtTarget (@IsIndQuasiAffineHom : MorphismProperty Scheme.{u})
```

## Tag 0F1V, a lemma

[Tag 0F1V](https://stacks.math.columbia.edu/tag/0F1V) in the Stacks Project.

**`AlgebraicGeometry.isIndQuasiAffineHom_isStableUnderComposition`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/Comp.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/Comp.lean#L71).

> Being an ind-quasi-affine morphism of schemes is stable under composition.

```lean
instance isIndQuasiAffineHom_isStableUnderComposition :
    MorphismProperty.IsStableUnderComposition
      (@IsIndQuasiAffineHom : MorphismProperty Scheme.{u})
```

## Tag 0F1W, a lemma

[Tag 0F1W](https://stacks.math.columbia.edu/tag/0F1W) in the Stacks Project.

**`AlgebraicGeometry.isIndQuasiAffineHom_of_isQuasiAffineHom`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/QuasiAffineAndImmersion.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/QuasiAffineAndImmersion.lean#L36). The attribute's comment: “quasi-affine morphisms”.

> A quasi-affine morphism of schemes is ind-quasi-affine.

```lean
instance isIndQuasiAffineHom_of_isQuasiAffineHom {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsQuasiAffineHom f] : IsIndQuasiAffineHom f
```

**`AlgebraicGeometry.isIndQuasiAffineHom_of_isImmersion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/QuasiAffineAndImmersion.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/QuasiAffineAndImmersion.lean#L45). The attribute's comment: “immersions”.

> An immersion of schemes is ind-quasi-affine.

```lean
instance isIndQuasiAffineHom_of_isImmersion {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsImmersion f] : IsIndQuasiAffineHom f
```

## Tag 0F1X, a lemma

[Tag 0F1X](https://stacks.math.columbia.edu/tag/0F1X) in the Stacks Project.

**`AlgebraicGeometry.isIndQuasiAffineHom_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/Comp.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/Comp.lean#L79).

> If the composite `f ≫ g` of two morphisms of schemes is ind-quasi-affine, then `f` is
> ind-quasi-affine.

```lean
theorem isIndQuasiAffineHom_of_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    [IsIndQuasiAffineHom (f ≫ g)] : IsIndQuasiAffineHom f
```

## Tag 0AP7, a lemma

[Tag 0AP7](https://stacks.math.columbia.edu/tag/0AP7) in the Stacks Project.

**`AlgebraicGeometry.isIndQuasiAffineHom_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/BaseChange.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/BaseChange.lean#L41).

> Ind-quasi-affine morphisms of schemes are stable under arbitrary base change.

```lean
instance isIndQuasiAffineHom_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (@IsIndQuasiAffineHom : MorphismProperty Scheme.{u})
```

## Tag 0AP8, a lemma

[Tag 0AP8](https://stacks.math.columbia.edu/tag/0AP8) in the Stacks Project.

**`AlgebraicGeometry.isIndQuasiAffineHom_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/FpqcDescent.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/IndQuasiAffine/FpqcDescent.lean#L55).

> Being an ind-quasi-affine morphism of schemes is fpqc local on the base.

```lean
instance isIndQuasiAffineHom_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@IsIndQuasiAffineHom : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 0AP9, a lemma

[Tag 0AP9](https://stacks.math.columbia.edu/tag/0AP9) in the Stacks Project.

**`AlgebraicGeometry.isIndQuasiAffineHom_of_isSeparated_of_locallyQuasiFinite`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/IndQuasiAffineSeparated.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/IndQuasiAffineSeparated.lean#L59).

> A separated morphism of schemes which is locally quasi-finite and locally of finite type is
> ind-quasi-affine.

```lean
instance isIndQuasiAffineHom_of_isSeparated_of_locallyQuasiFinite {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsSeparated f] [LocallyQuasiFinite f] [LocallyOfFiniteType f] :
    IsIndQuasiAffineHom f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.66, Tag 0AP5](https://stacks.math.columbia.edu/tag/0AP5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
