---
declaration: section
origin: cited
lean: SheafOfModules.IsFiniteType, AlgebraicGeometry.SheafOfModules.pullback_isFiniteType, Stacks.SheafOfModules.isFiniteType_image, Stacks.SheafOfModules.isFiniteType_middle_of_shortExact, Stacks.SheafOfModules.LocallySurjective.main_theorem, AlgebraicGeometry.exists_isZero_over_of_stalk_isZero, SheafOfModules.isClosed_supp, Stacks.SheafOfModules.exists_epi_to_colimit_of_isFiniteType
statement: formalized
proof: formalized
---

# 17.9 Modules of finite type

Section 17.9 of the Stacks Project, [Tag 01B4](https://stacks.math.columbia.edu/tag/01B4). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01B5, a definition

[Tag 01B5](https://stacks.math.columbia.edu/tag/01B5) in the Stacks Project.

Declarations registered for the tag:

- [`SheafOfModules.IsFiniteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.IsFiniteType#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch17.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch17.lean#L51) (StacksFrontier). References: EGA 0 (5.2.1); SGA 6 I (1.3).

## Tag 01B6, a lemma

[Tag 01B6](https://stacks.math.columbia.edu/tag/01B6) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.pullback_isFiniteType`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/FiniteType.lean, line 305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/FiniteType.lean#L305).

> **Stacks Project, Tag 01B6.** The pullback of a finite type module along a morphism of
> ringed spaces is of finite type.

```lean
noncomputable instance pullback_isFiniteType {X Y : RingedSpace.{u}} (f : X ⟶ Y)
    (G : _root_.Modules Y) [G.IsFiniteType] :
    ((_root_.pullback f).obj G).IsFiniteType
```

## Tag 01B7, a lemma

[Tag 01B7](https://stacks.math.columbia.edu/tag/01B7) in the Stacks Project.

**`Stacks.SheafOfModules.isFiniteType_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeExtension.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeExtension.lean#L350). The attribute's comment: “finite\_type\_image”.

> The image of a morphism out of a sheaf of modules of finite type is of finite type.

```lean
theorem isFiniteType_image (φ : M ⟶ N) (hM : M.IsFiniteType) : (image φ).IsFiniteType
```

**`Stacks.SheafOfModules.isFiniteType_middle_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeExtension.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeExtension.lean#L468). The attribute's comment: “finite\_type\_extension”. References: SGA 6 I (3.3), “c) finite type”.

> Let `R` be a sheaf of rings on a topological space. In a short exact sequence of sheaves of
> `R`-modules, if the first and third terms are of finite type then so is the middle term.

```lean
theorem isFiniteType_middle_of_shortExact (S : ShortComplex (SheafOfModules.{u} R))
    (hS : S.ShortExact) (h₁ : S.X₁.IsFiniteType) (h₃ : S.X₃.IsFiniteType) :
    S.X₂.IsFiniteType
```

## Tag 01B8, a lemma

[Tag 01B8](https://stacks.math.columbia.edu/tag/01B8) in the Stacks Project.

**`Stacks.SheafOfModules.LocallySurjective.main_theorem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeLocallySurjective.lean, line 683](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeLocallySurjective.lean#L683). References: EGA 0 (5.2.2), “generating sections”.

> Let `(X, O_X)` be a ringed space and `φ : G ⟶ F` a homomorphism of `O_X`-modules. Suppose `F`
> is of finite type and the induced map on stalks at `x` is surjective. Then there is an open
> neighbourhood `U` of `x` over which `φ` is surjective, i.e. for every `y ∈ U` the induced map on
> the stalk at `y` is surjective.

```lean
theorem main_theorem
    {F G : SheafOfModules.{u} R} (φ : G ⟶ F)
    (hF : SheafOfModules.IsFiniteType.{u, u, u} F) (x : X)
    (hx : SurjOnStalk φ x) :
    ∃ U : TopologicalSpace.Opens X, x ∈ U ∧ ∀ y ∈ U, SurjOnStalk φ y
```

## Tag 01B9, a lemma

[Tag 01B9](https://stacks.math.columbia.edu/tag/01B9) in the Stacks Project.

**`AlgebraicGeometry.exists_isZero_over_of_stalk_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalSurjectivity.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalSurjectivity.lean#L126). References: EGA 0 (5.2.2), “support closed”.

> **Stacks Project, Tag 01Y3.** A finite-type sheaf whose stalk vanishes at a point vanishes
> on a neighbourhood of that point.

```lean
public theorem exists_isZero_over_of_stalk_isZero (F : SheafOfModules.{u} R)
    [F.IsFiniteType] (x : X)
    (hx : IsZero (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x)) :
    ∃ U : Opens X, x ∈ U ∧ IsZero (F.over U)
```

## Tag 01BA, a lemma

[Tag 01BA](https://stacks.math.columbia.edu/tag/01BA) in the Stacks Project.

**`SheafOfModules.isClosed_supp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Support.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Support.lean#L151).

> The support of a sheaf of modules of finite type on a topological space is closed.

```lean
lemma isClosed_supp {X : TopCat.{u}} {R : TopCat.Sheaf RingCat.{u} X}
    (F : SheafOfModules.{u} R) [F.IsFiniteType] :
    IsClosed (supp F)
```

## Tag 01BB, a lemma

[Tag 01BB](https://stacks.math.columbia.edu/tag/01BB) in the Stacks Project.

**`Stacks.SheafOfModules.exists_epi_to_colimit_of_isFiniteType`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeColimit.lean, line 492](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeColimit.lean#L492). The attribute's comment: “surjective stage”.

> A finite type directed colimit of sheaves of modules on a quasi-compact space is the
> quotient of one of its stages.

```lean
lemma exists_epi_to_colimit_of_isFiniteType [CompactSpace X]
    (F : I ⥤ SheafOfModules.{u} R)
    [SheafOfModules.IsFiniteType (colimit F)] :
    ∃ i : I, Epi (colimit.ι F i)
```

**`Stacks.SheafOfModules.exists_isIso_to_colimit_of_isFiniteType`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeColimit.lean, line 529](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeColimit.lean#L529). The attribute's comment: “injective transition maps”.

> If the transition maps of a directed system of sheaves of modules on a quasi-compact space
> are injective, a finite type colimit is already one of its stages.

```lean
lemma exists_isIso_to_colimit_of_isFiniteType [CompactSpace X]
    (F : I ⥤ SheafOfModules.{u} R)
    [∀ (i j : I) (f : i ⟶ j), Mono (F.map f)]
    [SheafOfModules.IsFiniteType (colimit F)] :
    ∃ i : I, IsIso (colimit.ι F i)
```

## Tag 01BC, a lemma

[Tag 01BC](https://stacks.math.columbia.edu/tag/01BC) in the Stacks Project.

**`Stacks.SheafOfModules.essentiallySmall_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeEssentiallySmall.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeEssentiallySmall.lean#L53).

> The finite type sheaves of modules over the structure sheaf of a ringed
> space have only a set of isomorphism classes.

```lean
theorem essentiallySmall_isFiniteType (X : RingedSpace.{u, u}) :
    ObjectProperty.EssentiallySmall.{u}
      (fun M : SheafOfModules.{u}
          ((sheafCompose (Opens.grothendieckTopology X)
            (forget₂ CommRingCat RingCat)).obj X.sheaf) ↦
        SheafOfModules.IsFiniteType M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.9, Tag 01B4](https://stacks.math.columbia.edu/tag/01B4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
