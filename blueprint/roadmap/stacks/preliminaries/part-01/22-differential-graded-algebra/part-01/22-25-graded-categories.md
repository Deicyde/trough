---
declaration: section
origin: cited
lean: CategoryTheory.GradedCategory, CategoryTheory.Functor.Graded, CategoryTheory.GradedCategory.DegreeZero, CategoryTheory.GradedCategory.DegreeZero.Hom, CategoryTheory.GradedCategory.GradedBinaryBiproductData, CategoryTheory.GradedObject.gradedCategoryData, CategoryTheory.GradedObject.degreeZeroEquivalence, ExternallyGraded.RightModuleCat.homogeneousMapSubmodule
statement: formalized
proof: formalized
---

# 22.25 Graded categories

Section 22.25 of the Stacks Project, [Tag 09L1](https://stacks.math.columbia.edu/tag/09L1). 6 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09L2, a definition

[Tag 09L2](https://stacks.math.columbia.edu/tag/09L2) in the Stacks Project.

**`CategoryTheory.GradedCategory`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/Category.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/Category.lean#L43).

> A category graded over a ring `R`: every morphism module is the direct sum of its
> integer-indexed homogeneous pieces, identities are homogeneous of degree zero, and composition
> of morphisms of degrees `m` and `n` has degree `m + n`.

```lean
class GradedCategory (R : Type w) [Ring R] (C : Type u) [Category.{v} C] [Preadditive C]
    extends Linear R C
```

## Tag 09L3, a definition

[Tag 09L3](https://stacks.math.columbia.edu/tag/09L3) in the Stacks Project.

**`CategoryTheory.Functor.Graded`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/Functor.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/Functor.lean#L40).

> A functor between categories graded over `R` is graded if its maps on morphisms are
> `R`-linear and preserve each homogeneous degree.

```lean
class Functor.Graded (R : Type w) [Ring R] {C : Type u₁} [Category.{v₁} C] [Preadditive C]
    [GradedCategory R C] {D : Type u₂} [Category.{v₂} D] [Preadditive D] [GradedCategory R D]
    (F : C ⥤ D) : Prop extends F.Additive, F.Linear R
```

## Tag 09ML, a definition

[Tag 09ML](https://stacks.math.columbia.edu/tag/09ML) in the Stacks Project.

**`CategoryTheory.GradedCategory.DegreeZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/DegreeZero.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/DegreeZero.lean#L43).

> The degree-zero category of a graded category. It has the same objects as the ambient
> category, and its morphisms are the homogeneous morphisms of degree zero.

```lean
def DegreeZero (_R : Type w) (C : Type u)
```

**`CategoryTheory.GradedCategory.DegreeZero.Hom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/DegreeZero.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/DegreeZero.lean#L51).

> The degree-zero homogeneous morphisms between two objects.

```lean
abbrev Hom (X Y : DegreeZero R C) : Type v
```

**An instance with no name** in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/DegreeZero.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/DegreeZero.lean#L64).

> Composition and identities of a graded category restrict to its degree-zero morphisms.

```lean
instance : Category.{v} (DegreeZero R C)
```

## Tag 09P2, a definition

[Tag 09P2](https://stacks.math.columbia.edu/tag/09P2) in the Stacks Project.

**`CategoryTheory.GradedCategory.GradedBinaryBiproductData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/Biproduct.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/Biproduct.lean#L42).

> A chosen binary biproduct in a category graded over `R` whose inclusions and projections are
> all homogeneous of degree zero.

```lean
structure GradedBinaryBiproductData (R : Type w) [Ring R] {C : Type u} [Category.{v} C]
    [Preadditive C] [GradedCategory R C] (X Y : C) extends BinaryBiproductData X Y
```

## Tag 09MM, an example

[Tag 09MM](https://stacks.math.columbia.edu/tag/09MM) in the Stacks Project.

**`CategoryTheory.GradedObject.gradedCategoryData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/GradedObject.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/GradedObject.lean#L310). The attribute's comment: “graded\_category\_of\_graded\_objects”.

> The graded category of integer-graded objects in a preadditive category.

```lean
noncomputable def gradedCategoryData : GradedCategoryData B
```

**`CategoryTheory.GradedObject.degreeZeroEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/GradedObject.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/GradedObject.lean#L332).

> Degree-zero homogeneous maps of graded objects are precisely the componentwise maps: the
> degree-zero category of the graded category of graded objects is canonically equivalent to the
> ordinary category of graded objects.

```lean
noncomputable def degreeZeroEquivalence :
    { E : @CategoryTheory.Equivalence
        (GradedCategory.DegreeZero ℤ (GradedObject ℤ B)) (GradedObject ℤ B)
        (degreeZeroCategory B) (GradedObject.categoryOfGradedObjects ℤ) //
      let F := @CategoryTheory.Equivalence.functor
        (GradedCategory.DegreeZero ℤ (GradedObject ℤ B)) (GradedObject ℤ B)
        (degreeZeroCategory B) (GradedObject.categoryOfGradedObjects ℤ) E
      (∀ X : GradedCategory.DegreeZero ℤ (GradedObject ℤ B),
        @CategoryTheory.Functor.obj _ (degreeZeroCategory B) _
          (GradedObject.categoryOfGradedObjects ℤ) F X = X) ∧
      (∀ (X Y : GradedCategory.DegreeZero ℤ (GradedObject ℤ B))
          (f : @Quiver.Hom _ (degreeZeroCategory B).toQuiver X Y) (i : ℤ),
        HEq ((@CategoryTheory.Functor.map _ (degreeZeroCategory B) _
          (GradedObject.categoryOfGradedObjects ℤ) F X Y f) i)
          (((DirectSum.component ℤ ℤ
            (fun n ↦ Cochain
              (zeroDifferentialComplex B X)
              (zeroDifferentialComplex B Y) n) 0)
            ((gradedCategoryData B).homEquiv X Y f.1)).v
              i i (add_zero i))) }
```

## Tag 09MN, an example

[Tag 09MN](https://stacks.math.columbia.edu/tag/09MN) in the Stacks Project.

**`ExternallyGraded.RightModuleCat.homogeneousMapSubmodule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/GradedModule.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/GradedModule.lean#L101). The attribute's comment: “graded\_category\_of\_graded\_modules”.

> The degree-`n` right `𝒜`-linear maps between graded right modules.

```lean
def homogeneousMapSubmodule (M N : RightModuleCat 𝒜) (n : ℤ) :
    Submodule R (M.Total →ₗ[R] N.Total)
```

**`ExternallyGraded.RightModuleCat.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/GradedModule.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/GradedModule.lean#L282). The attribute's comment: “graded\_category\_of\_graded\_modules”.

> Graded right modules, with finite sums of homogeneous maps as morphisms.

```lean
instance instCategory : Category (RightModuleCat 𝒜)
```

**`ExternallyGraded.RightModuleCat.instGradedCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/GradedModule.lean, line 361](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/GradedModule.lean#L361). The attribute's comment: “graded\_category\_of\_graded\_modules”.

> The category of graded right modules is graded by the degrees of homogeneous maps.

```lean
instance instGradedCategory : GradedCategory R (RightModuleCat 𝒜)
```

**`ExternallyGraded.RightModuleCat.degreeZeroHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/GradedModule.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/GradedModule.lean#L380). The attribute's comment: “degree-zero morphisms”.

> The canonical identification of degree-zero morphisms with graded right-module maps.

```lean
noncomputable def degreeZeroHomEquiv (𝒜 : ExternallyGradedAlgebra.{u, v} R)
    (M N : RightModuleCat.{u, v, w} 𝒜) :
    { e : GradedCategory.DegreeZero.Hom R (RightModuleCat 𝒜) M N ≃ HomogeneousMap M N 0 //
      ∀ f, (e f).1 = toLinearMap M N f.1 }
```

**`ExternallyGraded.RightModuleCat.degreeZeroHomEquiv_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/GradedModule.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/GradedModule.lean#L403). The attribute's comment: “identities”.

> Under the canonical identification, the identity is the identity homogeneous map.

```lean
theorem degreeZeroHomEquiv_id (𝒜 : ExternallyGradedAlgebra.{u, v} R)
    (M : RightModuleCat.{u, v, w} 𝒜) :
    ((degreeZeroHomEquiv 𝒜 M M).1
      (GradedCategory.DegreeZero.identity R (RightModuleCat 𝒜) M)) =
      HomogeneousMap.id M
```

**`ExternallyGraded.RightModuleCat.degreeZeroHomEquiv_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Graded/GradedModule.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Graded/GradedModule.lean#L414). The attribute's comment: “composition”.

> Under the canonical identification, composition is composition of homogeneous maps.

```lean
theorem degreeZeroHomEquiv_comp (𝒜 : ExternallyGradedAlgebra.{u, v} R)
    {M N P : RightModuleCat.{u, v, w} 𝒜}
    (f : GradedCategory.DegreeZero.Hom R (RightModuleCat 𝒜) M N)
    (g : GradedCategory.DegreeZero.Hom R (RightModuleCat 𝒜) N P) :
    (degreeZeroHomEquiv 𝒜 M P).1
      (GradedCategory.DegreeZero.comp R (RightModuleCat 𝒜) f g) =
      HomogeneousMap.comp ((degreeZeroHomEquiv 𝒜 M N).1 f)
        ((degreeZeroHomEquiv 𝒜 N P).1 g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.25, Tag 09L1](https://stacks.math.columbia.edu/tag/09L1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
