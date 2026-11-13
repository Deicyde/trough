---
declaration: section
origin: cited
lean: AlgebraicGeometry.EtaleFundamentalGroup, AlgebraicGeometry.exists_finiteEtaleEquivalence, AlgebraicGeometry.nonempty_finiteEtaleFiberFunctorIso_of_connectedSpace, AlgebraicGeometry.nonempty_etaleFundamentalGroupContinuousMulEquiv, AlgebraicGeometry.isInnerConjugate_etaleFundamentalGroupContinuousMulEquiv, AlgebraicGeometry.etaleFundamentalGroupContinuousMulEquiv_action, AlgebraicGeometry.exists_finiteEtaleEquivalence_mapIso, AlgebraicGeometry.etaleFundamentalGroupMap
statement: formalized
proof: formalized
---

# 58.6 Fundamental groups

Section 58.6 of the Stacks Project, [Tag 0BQ8](https://stacks.math.columbia.edu/tag/0BQ8). 3 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BNC, a definition

[Tag 0BNC](https://stacks.math.columbia.edu/tag/0BNC) in the Stacks Project.

**`AlgebraicGeometry.EtaleFundamentalGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamentalGroup.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamentalGroup.lean#L80).

> **Stacks Project, Tag 0BNC.** The étale fundamental group of a connected scheme at a
> geometric point is the automorphism group of its finite-étale fibre functor, endowed with the
> topology induced by its actions on all fibres.

```lean
public def EtaleFundamentalGroup (X : Scheme.{u}) [ConnectedSpace X]
    (x : GeometricPoint X) : Type (u + 1)
```

## Tag 0BND, a theorem

[Tag 0BND](https://stacks.math.columbia.edu/tag/0BND) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteEtaleEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean#L85). The attribute's comment: “(1) the equivalence of FÉt\_X with the finite continuous π₁(X, x)-sets; (2) and (3) not covered here”.

> **Stacks Project, Tags 0BND (1) and 03VF (3).** Finite étale covers of a connected scheme `X`
> are equivalent to finite sets with a continuous action of `π₁(X, x)`, by an equivalence whose
> underlying finite sets are the geometric fibres at `x` and whose action is evaluation of natural
> automorphisms.

```lean
theorem exists_finiteEtaleEquivalence (X : Scheme.{u}) [ConnectedSpace X]
    (x : GeometricPoint X) :
    ∃ E : FiniteEtaleOver X ≌ ContAction FintypeCat.{u} (EtaleFundamentalGroup X x),
      ∃ α : E.functor ⋙
          forget₂ (ContAction FintypeCat.{u} (EtaleFundamentalGroup X x))
            FintypeCat.{u} ⋙ FintypeCat.incl ≅ finiteEtaleFiberFunctor x,
        ∀ (Y : FiniteEtaleOver X) (σ : EtaleFundamentalGroup X x)
          (y : (E.functor.obj Y).obj.V.obj),
          (α.hom.app Y) (ConcreteCategory.hom ((E.functor.obj Y).obj.ρ σ).asHom y) =
            (σ.asIso.app Y).hom ((α.hom.app Y) y)
```

**`AlgebraicGeometry.nonempty_finiteEtaleFiberFunctorIso_of_connectedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean#L104). The attribute's comment: “(2) existence of an isomorphism t : F\_x ≅ F\_x' of the geometric fibre functors at two base points; the comparison of fundamental groups it induces, that comparison's independence up to inner conjugation and its compatibility with (1) are separate, and (1) and (3) are not covered here”.

> **Stacks Project, Tag 0BND (2), existence of the isomorphism of fibre functors.** Given a
> second geometric point `x'` of a connected scheme `X`, there is an isomorphism
> `t : F_x ≅ F_{x'}` between the two geometric fibre functors on `FÉt_X`.

```lean
theorem nonempty_finiteEtaleFiberFunctorIso_of_connectedSpace (X : Scheme.{u}) [ConnectedSpace X]
    (x x' : GeometricPoint X) :
    Nonempty (finiteEtaleFiberFunctor x ≅ finiteEtaleFiberFunctor x')
```

**`AlgebraicGeometry.nonempty_etaleFundamentalGroupContinuousMulEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean#L116). The attribute's comment: “(2) existence of the comparison of two base points, as topological groups; its independence up to inner conjugation and its compatibility with (1) are separate, and (1) and (3) are not covered here”.

> **Stacks Project, Tag 0BND (2), existence.** The étale fundamental groups of a connected
> scheme at two geometric points are isomorphic as topological groups: the two geometric fibre
> functors are isomorphic, and conjugation by such an isomorphism is a homeomorphic group
> isomorphism.

```lean
theorem nonempty_etaleFundamentalGroupContinuousMulEquiv (X : Scheme.{u}) [ConnectedSpace X]
    (x x' : GeometricPoint X) :
    Nonempty (EtaleFundamentalGroup X x ≃ₜ* EtaleFundamentalGroup X x')
```

**`AlgebraicGeometry.isInnerConjugate_etaleFundamentalGroupContinuousMulEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean#L134). The attribute's comment: “(2) independence of the base-point comparison up to inner conjugation; its existence and its compatibility with (1) are separate, and (1) and (3) are not covered here”.

> **Stacks Project, Tag 0BND (2), independence of the choice.** Two isomorphisms of the geometric
> fibre functors at two geometric points induce isomorphisms of étale fundamental groups that differ
> by an inner automorphism of the target.

```lean
theorem isInnerConjugate_etaleFundamentalGroupContinuousMulEquiv {X : Scheme.{u}}
    [ConnectedSpace X] {x x' : GeometricPoint X}
    (t₁ t₂ : finiteEtaleFiberFunctor x ≅ finiteEtaleFiberFunctor x') :
    IsInnerConjugate (etaleFundamentalGroupContinuousMulEquiv t₁).toMulEquiv.toMonoidHom
      (etaleFundamentalGroupContinuousMulEquiv t₂).toMulEquiv.toMonoidHom
```

**`AlgebraicGeometry.etaleFundamentalGroupContinuousMulEquiv_action`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean#L147). The attribute's comment: “(2) compatibility of the base-point comparison with the actions of (1); its existence and its independence up to inner conjugation are separate, and (1) and (3) are not covered here”.

> **Stacks Project, Tag 0BND (2), compatibility with the equivalences.** The change-of-base-point
> isomorphism of topological groups intertwines the actions on the geometric fibres underlying the
> two equivalences of Tag 0BND (1) at the two base points.

```lean
theorem etaleFundamentalGroupContinuousMulEquiv_action {X : Scheme.{u}} [ConnectedSpace X]
    {x x' : GeometricPoint X} (t : finiteEtaleFiberFunctor x ≅ finiteEtaleFiberFunctor x')
    (Y : FiniteEtaleOver X) (σ : EtaleFundamentalGroup X x)
    (y : ((finiteEtaleEquivalenceOfIsGaloisCategory X x).functor.obj Y).obj.V.obj) :
    t.hom.app Y
        ((finiteEtaleEquivalenceOfIsGaloisCategoryFiberIso X x).hom.app Y
          (ConcreteCategory.hom
            (((finiteEtaleEquivalenceOfIsGaloisCategory X x).functor.obj Y).obj.ρ σ).asHom y)) =
      (finiteEtaleEquivalenceOfIsGaloisCategoryFiberIso X x').hom.app Y
        (ConcreteCategory.hom
          (((finiteEtaleEquivalenceOfIsGaloisCategory X x').functor.obj Y).obj.ρ
            (etaleFundamentalGroupContinuousMulEquiv t σ)).asHom
          ((finiteEtaleEquivalenceOfIsGaloisCategoryFiberIso X x').inv.app Y
            (t.hom.app Y
              ((finiteEtaleEquivalenceOfIsGaloisCategoryFiberIso X x).hom.app Y y))))
```

**`AlgebraicGeometry.exists_finiteEtaleEquivalence_mapIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean#L171). The attribute's comment: “(3) the square comparing base change with restriction along the induced homomorphism; the homomorphism and the equation determining it are separate, and (1) and (2) are not covered here”.

> **Stacks Project, Tag 0BND (3), the commuting square.** For a morphism `f : X ⟶ Y` of connected
> schemes, base change `FÉt_Y ⥤ FÉt_X` agrees under the equivalences of Tag 0BND (1) with restriction
> of the action along `AlgebraicGeometry.etaleFundamentalGroupMap`, and the comparison isomorphism is
> the canonical projection of geometric fibres.

```lean
theorem exists_finiteEtaleEquivalence_mapIso {X Y : Scheme.{u}} [ConnectedSpace X]
    [ConnectedSpace Y] (f : X ⟶ Y) (x : GeometricPoint X) :
    ∃ η : (finiteEtaleEquivalenceOfIsGaloisCategory Y (x.map f)).functor ⋙
          ContAction.res FintypeCat (etaleFundamentalGroupMap f x) ≅
        finiteEtaleBaseChange f ⋙
          (finiteEtaleEquivalenceOfIsGaloisCategory X x).functor,
      ∀ (V : FiniteEtaleOver Y)
        (a : (((finiteEtaleEquivalenceOfIsGaloisCategory X x).functor.obj
          ((finiteEtaleBaseChange f).obj V)).obj.V.obj)),
        (finiteEtaleEquivalenceOfIsGaloisCategoryFiberIso Y (x.map f)).hom.app V
            ((η.inv.app V).hom.hom a) =
          finiteEtaleFiberProjection f x V
            ((finiteEtaleEquivalenceOfIsGaloisCategoryFiberIso X x).hom.app
              ((finiteEtaleBaseChange f).obj V) a)
```

**`AlgebraicGeometry.etaleFundamentalGroupMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/MorphismMap.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/MorphismMap.lean#L191). The attribute's comment: “(3) the induced continuous homomorphism; the equation determining it and the commuting square are separate, and (1) and (2) are not covered here”.

> **Stacks Project, Tag 0BND (3).** The continuous homomorphism of étale fundamental groups
> induced by a morphism of connected schemes and a geometric point of its source.

```lean
def etaleFundamentalGroupMap {X Y : Scheme.{u}} [ConnectedSpace X] [ConnectedSpace Y]
    (f : X ⟶ Y) (x : GeometricPoint X) :
    EtaleFundamentalGroup X x →ₜ* EtaleFundamentalGroup Y (x.map f)
```

**`AlgebraicGeometry.etaleFundamentalGroupMap_finiteEtaleFiberProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/MorphismMap.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/MorphismMap.lean#L222). The attribute's comment: “(3) the equation determining the induced continuous homomorphism; the homomorphism itself and the commuting square are separate, and (1) and (2) are not covered here”.

> **Stacks Project, Tag 0BND (3).** The induced homomorphism commutes with the canonical
> projection from the geometric fibre of a base-changed finite étale cover to the original
> geometric fibre. Since the projections are bijective, this equation determines
> `AlgebraicGeometry.etaleFundamentalGroupMap`.

```lean
theorem etaleFundamentalGroupMap_finiteEtaleFiberProjection {X Y : Scheme.{u}}
    [ConnectedSpace X] [ConnectedSpace Y] (f : X ⟶ Y) (x : GeometricPoint X)
    (V : FiniteEtaleOver Y) (σ : EtaleFundamentalGroup X x)
    (p : finiteEtaleFiber x ((finiteEtaleBaseChange f).obj V)) :
    finiteEtaleFiberProjection f x V ((σ.asIso.app _).hom p) =
      ((etaleFundamentalGroupMap f x σ).asIso.app V).hom
        (finiteEtaleFiberProjection f x V p)
```

## Tag 0BNE, a lemma

[Tag 0BNE](https://stacks.math.columbia.edu/tag/0BNE) in the Stacks Project.

**`AlgebraicGeometry.finiteEtaleEquivalenceGaloisSets`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/FiberComparison.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/FiberComparison.lean#L184). The attribute's comment: “part (1): equivalence”. References: SGA 4½ Arcata (2.4.2), “partial”; SGA 4½ Arcata (2.4.3).

> Finite étale covers of a field are finite continuous sets for its absolute
> Galois group.

```lean
public noncomputable def finiteEtaleEquivalenceGaloisSets
    (K L Ω : Type u) [Field K] [Field L] [Field Ω]
    [Algebra K L] [IsSepClosure K L] [Algebra L Ω]
    [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω]
    [Algebra.IsAlgebraic K Ω] :
    FiniteEtaleOver (Spec (.of K)) ≌
      ContAction FintypeCat.{u} Gal(L/K)
```

**`AlgebraicGeometry.finiteEtaleFiberIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/FiberComparison.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/FiberComparison.lean#L259). The attribute's comment: “part (1): natural fibre comparison”.

> The underlying finite Galois set of a cover is naturally its geometric
> fibre over the algebraic closure.

```lean
public noncomputable def finiteEtaleFiberIso
    (K L Ω : Type u) [Field K] [Field L] [Field Ω]
    [Algebra K L] [IsSepClosure K L] [Algebra L Ω]
    [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω]
    [Algebra.IsAlgebraic K Ω] :
    (finiteEtaleEquivalenceGaloisSets K L Ω).functor ⋙
        forget₂ (ContAction FintypeCat.{u} Gal(L/K)) FintypeCat.{u} ⋙
      forget FintypeCat.{u} ≅
      finiteEtaleFiberFunctor
        (algebraicClosureGeometricPoint K Ω)
```

**`AlgebraicGeometry.separableFiberEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/FiberComparison.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/FiberComparison.lean#L354). The attribute's comment: “part (1): separable-closure fibre”.

> The Galois set attached to a finite étale cover is the set of its points
> over the separable closure.

```lean
public noncomputable def separableFiberEquiv
    (K L Ω : Type u) [Field K] [Field L] [Field Ω]
    [Algebra K L] [IsSepClosure K L] [Algebra L Ω]
    [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω]
    [Algebra.IsAlgebraic K Ω]
  (Y : FiniteEtaleOver (Spec (.of K))) :
    ((finiteEtaleEquivalenceGaloisSets K L Ω).functor.obj Y).obj.V ≃
      { f : Spec (.of L) ⟶ Y.left //
        f ≫ Y.hom = Spec.map (CommRingCat.ofHom (algebraMap K L)) }
```

**`AlgebraicGeometry.finiteEtaleFiberIso_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/FiberComparison.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/FiberComparison.lean#L386). The attribute's comment: “part (1): fibre comparison formula”.

> The natural fibre comparison is extension of a separable-closure point
> to the algebraic closure.

```lean
public theorem finiteEtaleFiberIso_apply
    (K L Ω : Type u) [Field K] [Field L] [Field Ω]
    [Algebra K L] [IsSepClosure K L] [Algebra L Ω]
    [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω]
    [Algebra.IsAlgebraic K Ω]
    (Y : FiniteEtaleOver (Spec (.of K)))
    (y : ((finiteEtaleEquivalenceGaloisSets K L Ω).functor.obj Y).obj.V) :
    (((finiteEtaleFiberIso K L Ω).hom.app Y) y).1 =
      Spec.map (CommRingCat.ofHom (algebraMap L Ω)) ≫
        (separableFiberEquiv K L Ω Y y).1
```

**`AlgebraicGeometry.separableFiberEquiv_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/FiberComparison.lean, line 405](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/FiberComparison.lean#L405). The attribute's comment: “part (1): naturality over the separable closure”.

> The separable-closure description is natural in a finite étale cover.

```lean
public theorem separableFiberEquiv_map
    (K L Ω : Type u) [Field K] [Field L] [Field Ω]
    [Algebra K L] [IsSepClosure K L] [Algebra L Ω]
    [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω]
    [Algebra.IsAlgebraic K Ω]
    {Y Z : FiniteEtaleOver (Spec (.of K))} (f : Y ⟶ Z)
    (y : ((finiteEtaleEquivalenceGaloisSets K L Ω).functor.obj Y).obj.V) :
    (separableFiberEquiv K L Ω Z
      (ConcreteCategory.hom
        ((finiteEtaleEquivalenceGaloisSets K L Ω).functor.map f) y)).1 =
      (separableFiberEquiv K L Ω Y y).1 ≫ f.left
```

**`AlgebraicGeometry.separableFiberEquiv_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/FiberComparison.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/FiberComparison.lean#L425). The attribute's comment: “part (1): Galois action”.

> The Galois action on a separable-closure point is precomposition with
> the corresponding field automorphism.

```lean
public theorem separableFiberEquiv_smul
    (K L Ω : Type u) [Field K] [Field L] [Field Ω]
    [Algebra K L] [IsSepClosure K L] [Algebra L Ω]
    [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω]
    [Algebra.IsAlgebraic K Ω]
    (Y : FiniteEtaleOver (Spec (.of K)))
    (σ : Gal(L/K))
    (y : ((finiteEtaleEquivalenceGaloisSets K L Ω).functor.obj Y).obj.V) :
    (separableFiberEquiv K L Ω Y
      (ConcreteCategory.hom
        (((finiteEtaleEquivalenceGaloisSets K L Ω).functor.obj Y).obj.ρ σ).asHom y)).1 =
      Spec.map (CommRingCat.ofHom σ.toAlgHom.toRingHom) ≫
        (separableFiberEquiv K L Ω Y y).1
```

**`AlgebraicGeometry.galoisEquivEtaleFundamentalGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/GaloisGroupIso.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/GaloisGroupIso.lean#L175). The attribute's comment: “part (2)”. References: SGA 1 IX (6.1), “π₁(Spec k, special case”; SGA 1 V (8.1), “special case”; SGA 4½ Arcata (2.4.1).

> The canonical isomorphism from the absolute Galois group to the étale
> fundamental group: its action on a fibre is precomposition on the corresponding
> separable-closure point.

```lean
public noncomputable def galoisEquivEtaleFundamentalGroup
    (K L Ω : Type u) [Field K] [Field L] [Field Ω]
    [Algebra K L] [IsSepClosure K L] [Algebra L Ω]
    [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω]
    [Algebra.IsAlgebraic K Ω] :
    Gal(L/K) ≃ₜ*
      EtaleFundamentalGroup (Spec (.of K))
        (algebraicClosureGeometricPoint K Ω)
```

**`AlgebraicGeometry.galoisEquivEtaleFundamentalGroup_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/GaloisGroupIso.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/FieldFundamentalGroup/GaloisGroupIso.lean#L344). The attribute's comment: “part (2): action formula”. References: SGA 1 V (8.1), “Canonicity clause”; SGA 4½ Arcata (2.4.2), “partial”.

> The canonical group isomorphism acts on geometric fibres through the
> absolute Galois action on separable-closure points.

```lean
public theorem galoisEquivEtaleFundamentalGroup_apply
    (K L Ω : Type u) [Field K] [Field L] [Field Ω]
    [Algebra K L] [IsSepClosure K L] [Algebra L Ω]
    [Algebra K Ω] [IsScalarTower K L Ω] [IsAlgClosed Ω]
    [Algebra.IsAlgebraic K Ω]
    (Y : FiniteEtaleOver (Spec (.of K)))
    (σ : Gal(L/K))
    (p : finiteEtaleFiber
      (algebraicClosureGeometricPoint K Ω) Y)
    (f : Spec (.of L) ⟶ Y.left)
    (hf : p.1 = Spec.map (CommRingCat.ofHom (algebraMap L Ω)) ≫ f) :
    ((((galoisEquivEtaleFundamentalGroup K L Ω) σ).asIso.app Y).hom p).1 =
      Spec.map (CommRingCat.ofHom (algebraMap L Ω)) ≫
        Spec.map (CommRingCat.ofHom σ.toAlgHom.toRingHom) ≫ f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.6, Tag 0BQ8](https://stacks.math.columbia.edu/tag/0BQ8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
