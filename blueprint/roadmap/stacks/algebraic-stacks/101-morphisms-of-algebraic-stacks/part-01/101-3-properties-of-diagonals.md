---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isLocallyOfFiniteType_isomPresheaf, AlgebraicGeometry.Stack.isomSpaceOver_isGroupAlgebraicSpace, AlgebraicGeometry.Stack.isomSpaceOverGrpObj_mul, AlgebraicGeometry.Stack.isomSpaceOverModObj, AlgebraicGeometry.Stack.isomSpaceOverModObj_smul, AlgebraicGeometry.Stack.isomSpaceOver_isPseudoTorsor, AlgebraicGeometry.Stack.automorphismGroupSpace, AlgebraicGeometry.Stack.isLocallyOfFiniteType_relativeDiagonal_of_isAlgebraicStack
statement: formalized
proof: formalized
---

# 101.3 Properties of diagonals

Section 101.3 of the Stacks Project, [Tag 04XQ](https://stacks.math.columbia.edu/tag/04XQ). 7 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04XR, a lemma

[Tag 04XR](https://stacks.math.columbia.edu/tag/04XR) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyOfFiniteType_isomPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomPresheafFiniteType.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomPresheafFiniteType.lean#L318).

> Let `𝒳` be an algebraic stack over `S`, let `T` be an object of the big fppf site of `S` and
> let `x`, `y` be two objects of the fibre of `𝒳` over `T`. Then the structural morphism of the
> isomorphism sheaf `Isom(x, y)`, read over `T`, is locally of finite type.

```lean
theorem isLocallyOfFiniteType_isomPresheaf
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (T : BigFppfOver B S hS) :
    letI : 𝒳.val.p.IsFibered := 𝒳.isFiberedInGroupoids.isFibered
    ∀ x y : 𝒳.val.p.Fiber T,
      Space.IsLocallyOfFiniteType B T.left.1 T.left.2
        (terminal.from ((Over.iteratedSliceBackward T).op ⋙ 𝒳.val.p.isomPresheaf x y))
```

## Tag 04YP, a lemma

[Tag 04YP](https://stacks.math.columbia.edu/tag/04YP) in the Stacks Project.

**`AlgebraicGeometry.Stack.isomSpaceOver_isGroupAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomGroupAlgebraicSpace.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomGroupAlgebraicSpace.lean#L49). The attribute's comment: “part (1): Isom(y, y) is a group algebraic space over T”.

> **Stacks 04YP, part (1).** For an object `y` of the fibre category of an algebraic stack `𝒳`
> over a scheme `T` of the big fppf site of `S`, `Isom_𝒳(y, y)` is a group algebraic space over
> `T`: the group object `Isom_𝒳(y, y)` over the base `AlgebraicGeometry.Stack.siteTerminalSpace`,
> with the group structure `AlgebraicGeometry.Stack.isomSpaceOverGrpObj`, is (on the nose) an
> object of the category `AlgebraicGeometry.Space.GroupAlgebraicSpace` of group algebraic spaces
> over `T`, and its multiplication is composition of local automorphisms
> (`AlgebraicGeometry.Stack.isomSpaceComp`).

```lean
theorem isomSpaceOver_isGroupAlgebraicSpace (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (U : BigFppfOver B S hS) (y : 𝒳.val.p.Fiber U) :
    letI : GrpObj (isomSpaceOver B S hS 𝒳 U y y) := isomSpaceOverGrpObj B S hS 𝒳 U y
    (∃ G : Space.GroupAlgebraicSpace B U.left.1 U.left.2 (siteTerminalSpace B S hS U)
        (isAlgebraicSpace_yoneda B U.left.1 U.left.2
          (⊤_ (BigFppfOver B U.left.1 U.left.2))),
        G.obj = Grp.mk (isomSpaceOver B S hS 𝒳 U y y)) ∧
      ∀ (Q : Over (siteTerminalSpace B S hS U)) (a b : Q ⟶ isomSpaceOver B S hS 𝒳 U y y)
        (V : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ) (t : Q.left.obj V),
        ((CartesianMonoidalCategory.lift a b ≫
          MonObj.mul (X := isomSpaceOver B S hS 𝒳 U y y)).left.app V) t =
          isomSpaceComp B S hS 𝒳 U y V ((a.left.app V) t) ((b.left.app V) t)
```

**`AlgebraicGeometry.Stack.isomSpaceOverGrpObj_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomGroupSpace.lean, line 692](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomGroupSpace.lean#L692). The attribute's comment: “part (1): the group law is composition of automorphisms”.

> **The group law of `Isom_𝒳(y, y)` is composition of local automorphisms.** On a pair of
> sections of `Isom_𝒳(y, y)` over a test object `Q`, the multiplication of
> `AlgebraicGeometry.Stack.isomSpaceOverGrpObj` is
> `AlgebraicGeometry.Stack.isomSpaceComp`, i.e. reverse categorical composition.

```lean
theorem isomSpaceOverGrpObj_mul (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1}
      (BigFppfOver B S hS))
    (U : BigFppfOver B S hS)
    (y : 𝒳.val.p.Fiber U)
    (Q : Over (siteTerminalSpace B S hS U))
    (a b : Q ⟶ isomSpaceOver B S hS 𝒳 U y y)
    (V : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ) (t : Q.left.obj V) :
    (letI : GrpObj (isomSpaceOver B S hS 𝒳 U y y) :=
      isomSpaceOverGrpObj B S hS 𝒳 U y;
      ((CartesianMonoidalCategory.lift a b ≫
        MonObj.mul (X := isomSpaceOver B S hS 𝒳 U y y)).left.app V) t =
      isomSpaceComp B S hS 𝒳 U y V
        ((a.left.app V) t)
        ((b.left.app V) t))
```

**`AlgebraicGeometry.Stack.isomSpaceOverModObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomGroupSpace.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomGroupSpace.lean#L719). The attribute's comment: “part (2): the action by postcomposition”.

> **Stacks 04YP, part (2): the action.** `Isom_𝒳(y, y)` acts on `Isom_𝒳(x, y)` over
> `AlgebraicGeometry.Stack.siteTerminalSpace`, by postcomposition.

```lean
noncomputable def isomSpaceOverModObj
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1}
      (BigFppfOver B S hS))
    (U : BigFppfOver B S hS)
    (x y : 𝒳.val.p.Fiber U) :
    let G := isomSpaceOver B S hS 𝒳 U y y
    let P := isomSpaceOver B S hS 𝒳 U x y
    letI : GrpObj G := isomSpaceOverGrpObj B S hS 𝒳 U y
    ModObj G P
```

**`AlgebraicGeometry.Stack.isomSpaceOverModObj_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomGroupSpace.lean, line 752](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomGroupSpace.lean#L752). The attribute's comment: “part (2): the action is postcomposition”.

> **The action of `Isom_𝒳(y, y)` on `Isom_𝒳(x, y)` is postcomposition.** On a section of
> `Isom_𝒳(y, y)` and a section of `Isom_𝒳(x, y)` over a test object `Q`, the action of
> `AlgebraicGeometry.Stack.isomSpaceOverModObj` is
> `AlgebraicGeometry.Stack.isomSpaceSmul`.

```lean
theorem isomSpaceOverModObj_smul
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1}
      (BigFppfOver B S hS))
    (U : BigFppfOver B S hS)
    (x y : 𝒳.val.p.Fiber U)
    (Q : Over (siteTerminalSpace B S hS U))
    (g : Q ⟶ isomSpaceOver B S hS 𝒳 U y y)
    (p : Q ⟶ isomSpaceOver B S hS 𝒳 U x y)
    (V : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ) (t : Q.left.obj V) :
    (letI : GrpObj (isomSpaceOver B S hS 𝒳 U y y) :=
      isomSpaceOverGrpObj B S hS 𝒳 U y;
      letI : ModObj (isomSpaceOver B S hS 𝒳 U y y)
        (isomSpaceOver B S hS 𝒳 U x y) :=
        isomSpaceOverModObj B S hS 𝒳 U x y;
      ((CartesianMonoidalCategory.lift g p ≫
        ModObj.smul (M := isomSpaceOver B S hS 𝒳 U y y)
          (X := isomSpaceOver B S hS 𝒳 U x y)).left.app V) t) =
      isomSpaceSmul B S hS 𝒳 U x y V ((p.left.app V) t) ((g.left.app V) t)
```

**`AlgebraicGeometry.Stack.isomSpaceOver_isPseudoTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomGroupSpace.lean, line 810](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomGroupSpace.lean#L810). The attribute's comment: “part (2): isomorphism pseudo-torsor”.

> **Stacks 04YP, part (2).** `Isom_𝒳(x, y)` is a pseudo-torsor under `Isom_𝒳(y, y)` over `U`:
> the shear map `(g, p) ↦ (p ≫ g, p)` is an isomorphism, because for two local isomorphisms
> `p, q : x ⟶ y` the unique local automorphism `g` of `y` with `p ≫ g = q` is `p⁻¹ ≫ q`.

```lean
theorem isomSpaceOver_isPseudoTorsor
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1}
      (BigFppfOver B S hS))
    (U : BigFppfOver B S hS) (x y : 𝒳.val.p.Fiber U) :
    let G := isomSpaceOver B S hS 𝒳 U y y
    let P := isomSpaceOver B S hS 𝒳 U x y
    letI : GrpObj G := isomSpaceOverGrpObj B S hS 𝒳 U y
    letI : ModObj G P := isomSpaceOverModObj B S hS 𝒳 U x y
    IsPseudoTorsor G P
```

**`AlgebraicGeometry.Stack.automorphismGroupSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomGroupSpace.lean, line 868](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomGroupSpace.lean#L868). The attribute's comment: “part (1): automorphism group algebraic space”.

> **Stacks 04YP, part (1).** For an object `y` of the fibre category of an algebraic stack `𝒳`
> over a scheme `T` of the big fppf site of `S`, the automorphisms of `y` form a group algebraic
> space over `T`: the presheaf `Isom_𝒳(y, y)` is an algebraic space
> (`AlgebraicGeometry.Stack.isAlgebraicSpace_isomSpace`) and it carries the group object structure
> `AlgebraicGeometry.Stack.isomSpaceOverGrpObj`, whose law is composition of local automorphisms by
> `AlgebraicGeometry.Stack.isomSpaceOverGrpObj_mul`.

```lean
def automorphismGroupSpace (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (U : BigFppfOver B S hS) (y : 𝒳.val.p.Fiber U) :
    Space.GroupAlgebraicSpace B U.left.1 U.left.2 (siteTerminalSpace B S hS U)
      (isAlgebraicSpace_yoneda B U.left.1 U.left.2
        (⊤_ (BigFppfOver B U.left.1 U.left.2)))
```

## Tag 04XS, a lemma

[Tag 04XS](https://stacks.math.columbia.edu/tag/04XS) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyOfFiniteType_relativeDiagonal_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalFiniteType.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalFiniteType.lean#L266). The attribute's comment: “diagonal_locally_finite_type”.

> **Stacks 04XS, part (2).** The relative diagonal of a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic
> stacks over the big fppf site of `S` is locally of finite type: it is representable by algebraic
> spaces, and every algebraic space representing one of its base changes along a scheme-valued
> point of `𝒳 ×_{f, 𝒴, f} 𝒳` has locally-of-finite-type structural morphism — the
> every-étale-chart form of part (1) of Stacks 03XF.
>
> No hypothesis is placed on `f`; part (2) of Stacks 04YQ is the same statement for a 1-morphism
> representable by algebraic spaces.

```lean
theorem isLocallyOfFiniteType_relativeDiagonal_of_isAlgebraicStack
    {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴) :
    ∃ _hΔ : IsRepresentableByAlgebraicSpaces B S hS
        (relativeDiagonalBasedFunctor B S hS 𝒳.val 𝒴.val f.hom.hom),
      ∀ (U : BigFppfOver B S hS)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤
          (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.obj)
        (_hy : y ⋙ (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.p
          = Over.map U.hom)
        (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.val.p
            (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.p y
            (relativeDiagonalBasedFunctor B S hS 𝒳.val 𝒴.val f.hom.hom).toFunctor)
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Space.IsLocallyOfFiniteType B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_relativeDiagonal_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalRepresentable.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalRepresentable.lean#L103). The attribute's comment: “diagonal_representable”.

> **Stacks 04XS, part (1).** The relative diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` of a
> 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over the big fppf site of `S` is representable by
> algebraic spaces.
>
> Only the representability of the absolute diagonals of `𝒳` and of `𝒴` — the second clause of
> `AlgebraicGeometry.Stack.IsAlgebraicStack` — is used, by
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_relativeDiagonal`.

```lean
theorem isRepresentableByAlgebraicSpaces_relativeDiagonal_of_isAlgebraicStack
    (𝒳 𝒴 : CatFiberedInGroupoids.{u, max u v, u + 1, max (max (u + 1) w) v}
      (BigFppfOver B S hS))
    (f : 𝒳 ⟶ 𝒴)
    (h𝒳 : IsAlgebraicStack.{u, t} B S hS 𝒳.val)
    (h𝒴 : IsAlgebraicStack.{u, t} B S hS 𝒴.val) :
    IsRepresentableByAlgebraicSpaces B S hS
      (relativeDiagonalBasedFunctor B S hS 𝒳 𝒴 f.hom)
```

## Tag 04YQ, a lemma

[Tag 04YQ](https://stacks.math.columbia.edu/tag/04YQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.mono_relativeDiagonal_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalMonomorphism.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalMonomorphism.lean#L261). The attribute's comment: “part (3): monomorphism”.

> **Stacks 04YQ, part (3).** The relative diagonal of a 1-morphism of algebraic stacks over
> the big fppf site of `S` which is representable by algebraic spaces is a monomorphism: it is
> representable by algebraic spaces, and every algebraic space representing one of its base
> changes along a scheme-valued point of `𝒳 ×_{f, 𝒴, f} 𝒳` has monomorphic structural morphism.

```lean
theorem mono_relativeDiagonal_of_isRepresentableByAlgebraicSpaces
    {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    ∃ _hΔ : IsRepresentableByAlgebraicSpaces B S hS
        (relativeDiagonalBasedFunctor B S hS 𝒳.val 𝒴.val f.hom.hom),
      ∀ (U : BigFppfOver B S hS)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤
          (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.obj)
        (_hy : y ⋙ (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.p
          = Over.map U.hom)
        (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.val.p
            (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.p y
            (relativeDiagonalBasedFunctor B S hS 𝒳.val 𝒴.val f.hom.hom).toFunctor)
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Mono (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩))
```

**`AlgebraicGeometry.Stack.isSeparated_relativeDiagonal_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalMonomorphism.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalMonomorphism.lean#L293). The attribute's comment: “part (4): separated”.

> **Stacks 04YQ, part (4).** The relative diagonal of a 1-morphism of algebraic stacks over
> the big fppf site of `S` which is representable by algebraic spaces is separated: it is
> representable by algebraic spaces, and every algebraic space representing one of its base
> changes along a scheme-valued point of `𝒳 ×_{f, 𝒴, f} 𝒳` has separated structural morphism.
>
> By part (3) that structural morphism is a monomorphism, and a monomorphism of algebraic spaces
> is separated (Stacks 042N).

```lean
theorem isSeparated_relativeDiagonal_of_isRepresentableByAlgebraicSpaces
    {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    ∃ _hΔ : IsRepresentableByAlgebraicSpaces B S hS
        (relativeDiagonalBasedFunctor B S hS 𝒳.val 𝒴.val f.hom.hom),
      ∀ (U : BigFppfOver B S hS)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤
          (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.obj)
        (_hy : y ⋙ (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.p
          = Over.map U.hom)
        (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.val.p
            (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.p y
            (relativeDiagonalBasedFunctor B S hS 𝒳.val 𝒴.val f.hom.hom).toFunctor)
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Space.IsSeparated B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom
```

**`AlgebraicGeometry.Stack.isLocallyQuasiFinite_relativeDiagonal_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalQuasiFinite.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalQuasiFinite.lean#L195). The attribute's comment: “part (5): locally quasi-finite”.

> **Stacks 04YQ, part (5).** The relative diagonal of a 1-morphism of algebraic stacks over
> the big fppf site of `S` which is representable by algebraic spaces is locally quasi-finite: it
> is representable by algebraic spaces, and every algebraic space representing one of its base
> changes along a scheme-valued point of `𝒳 ×_{f, 𝒴, f} 𝒳` has locally quasi-finite structural
> morphism.
>
> That structural morphism is a monomorphism by part (3) and its represented base changes are
> locally of finite type by part (2) for a representable 1-morphism
> (`AlgebraicGeometry.Stack.presheaf_locallyOfFiniteType_relativeDiagonal`), so Stacks 0463
> applies.

```lean
theorem isLocallyQuasiFinite_relativeDiagonal_of_isRepresentableByAlgebraicSpaces :
    ∃ _hΔ : IsRepresentableByAlgebraicSpaces B S hS
        (relativeDiagonalBasedFunctor B S hS 𝒳.val 𝒴.val f.hom.hom),
      ∀ (U : BigFppfOver B S hS)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤
          (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.obj)
        (_hy : y ⋙ (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.p
          = Over.map U.hom)
        (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.val.p
            (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.p y
            (relativeDiagonalBasedFunctor B S hS 𝒳.val 𝒴.val f.hom.hom).toFunctor)
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Space.IsLocallyQuasiFinite B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom
```

**`AlgebraicGeometry.Stack.isLocallyOfFiniteType_relativeDiagonal_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalQuasiFinite.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalQuasiFinite.lean#L236). The attribute's comment: “part (2): locally of finite type”.

> **Stacks 04YQ, part (2).** The relative diagonal of a 1-morphism of algebraic stacks over
> the big fppf site of `S` which is representable by algebraic spaces is locally of finite type:
> it is representable by algebraic spaces, and every algebraic space representing one of its base
> changes along a scheme-valued point of `𝒳 ×_{f, 𝒴, f} 𝒳` has locally-of-finite-type structural
> morphism — the every-étale-chart form of part (1) of Stacks 03XF.
>
> This is read off part (5), the every-chart condition being monotone in the tested property of
> scheme morphisms, local finite type being the first conjunct of the meet part (5) is proved at.
>
> The hypothesis is the source's own: Stacks 04YQ asserts all five parts for a 1-morphism
> representable by algebraic spaces. The statement asserted for an *arbitrary* 1-morphism of
> algebraic stacks is part (2) of **Stacks 04XS**, which rests on Stacks 04XR and is proved in
> `StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalFiniteType.lean`; see the implementation
> notes.

```lean
theorem isLocallyOfFiniteType_relativeDiagonal_of_isRepresentableByAlgebraicSpaces :
    ∃ _hΔ : IsRepresentableByAlgebraicSpaces B S hS
        (relativeDiagonalBasedFunctor B S hS 𝒳.val 𝒴.val f.hom.hom),
      ∀ (U : BigFppfOver B S hS)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤
          (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.obj)
        (_hy : y ⋙ (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.p
          = Over.map U.hom)
        (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.val.p
            (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.p y
            (relativeDiagonalBasedFunctor B S hS 𝒳.val 𝒴.val f.hom.hom).toFunctor)
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Space.IsLocallyOfFiniteType B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom
```

**`AlgebraicGeometry.Stack.isRepresentableMorphism_relativeDiagonal_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalRepresentableBySchemes.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalRepresentableBySchemes.lean#L316). The attribute's comment: “part (1): representable by schemes”.

> The relative diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` of a 1-morphism `f` of algebraic stacks
> over the big fppf site of `S` which is representable by algebraic spaces is a *representable*
> 1-morphism in the sense of Stacks 02Y7 — representable by objects of the site, that is by
> schemes.

```lean
theorem isRepresentableMorphism_relativeDiagonal_of_isRepresentableByAlgebraicSpaces
    {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒳.val.val.p
      (twoFibreProduct B S hS 𝒴.val 𝒳.val 𝒳.val f.hom.hom f.hom.hom).val.p
      (relativeDiagonalBasedFunctor B S hS 𝒳.val 𝒴.val f.hom.hom).toFunctor
```

## Tag 04YS, a lemma

[Tag 04YS](https://stacks.math.columbia.edu/tag/04YS) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSeparated_relativeDiagonal_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedDiagonalTFAE.lean, line 690](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedDiagonalTFAE.lean#L690).

> **Stacks 04YS.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` which is
> representable by algebraic spaces and write `Δ_f : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` for its relative
> diagonal. The following are equivalent:
>
> 1. `f` is separated, in the relative sense of Stacks 04XB;
> 2. `Δ_f` is a closed immersion of algebraic stacks, part (2) of Stacks 04YL;
> 3. `Δ_f` is proper, in the relative sense of Stacks 04XB;
> 4. `Δ_f` is universally closed, in that sense.

```lean
theorem isSeparated_relativeDiagonal_tfae :
    List.TFAE
      [IsSeparated B S hS f.hom,
       AlgebraicStacks.IsClosedImmersion B S hS
         (Bicategory.InducedBicategory.mkHom
           (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom) :
             𝒳 ⟶ relativeDiagonalTargetStack B S hS 𝒳 𝒴 f),
       IsProper B S hS (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom),
       UniversallyClosed B S hS
         (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom)]
```

## Tag 04YT, a lemma

[Tag 04YT](https://stacks.math.columbia.edu/tag/04YT) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparated_iff_isQuasiCompact_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedDiagonal.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedDiagonal.lean#L108). The attribute's comment: “the equivalence of parts (1) and (2)”.

> A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` which is representable by algebraic
> spaces is quasi-separated if and only if its relative diagonal `Δ_f` is quasi-compact.

```lean
theorem isQuasiSeparated_iff_isQuasiCompact_relativeDiagonal (f : 𝒵 ⟶ 𝒯)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    IsQuasiSeparated B S hS f ↔
      Stack.IsQuasiCompact.{u, u, u + 1} B S hS
        (Stack.relativeDiagonal.{u, u, u + 1} B S hS 𝒵.val 𝒯.val f.hom)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiCompact_relativeDiagonal_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedDiagonal.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedDiagonal.lean#L120). The attribute's comment: “the implication (3) => (2)”.

> If the relative diagonal `Δ_f` of a 1-morphism of algebraic stacks over `S` is of finite
> type, then it is quasi-compact.

```lean
theorem isQuasiCompact_relativeDiagonal_of_isFiniteType (f : 𝒵 ⟶ 𝒯)
    (h : Stack.IsFiniteType.{u, u, u + 1} B S hS
      (Stack.relativeDiagonal.{u, u, u + 1} B S hS 𝒵.val 𝒯.val f.hom)) :
    Stack.IsQuasiCompact.{u, u, u + 1} B S hS
      (Stack.relativeDiagonal.{u, u, u + 1} B S hS 𝒵.val 𝒯.val f.hom)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFiniteType_relativeDiagonal_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedDiagonal.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedDiagonal.lean#L130). The attribute's comment: “the implication (2) => (3)”.

> If the relative diagonal `Δ_f` of a 1-morphism of algebraic stacks over `S` which is
> representable by algebraic spaces is quasi-compact, then it is of finite type.

```lean
theorem isFiniteType_relativeDiagonal_of_isQuasiCompact (f : 𝒵 ⟶ 𝒯)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (h : Stack.IsQuasiCompact.{u, u, u + 1} B S hS
      (Stack.relativeDiagonal.{u, u, u + 1} B S hS 𝒵.val 𝒯.val f.hom)) :
    Stack.IsFiniteType.{u, u, u + 1} B S hS
      (Stack.relativeDiagonal.{u, u, u + 1} B S hS 𝒵.val 𝒯.val f.hom)
```

## Tag 04YU, a lemma

[Tag 04YU](https://stacks.math.columbia.edu/tag/04YU) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallySeparated_iff_isImmersion_relativeDiagonalAlgebraicStacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallySeparatedDiagonal.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallySeparatedDiagonal.lean#L233).

> **Stacks 04YU.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` which is
> representable by algebraic spaces. Then `f` is locally separated, in the relative sense of
> Stacks 04XB, if and only if its relative diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` is an immersion
> of algebraic stacks, part (3) of Stacks 04YL.
>
> The content is
> `AlgebraicGeometry.Stack.isLocallySeparated_iff_isImmersion_relativeDiagonal`; the
> representability clause that part (3) of Stacks 04YL carries on top of the quantifier of
> Stacks 04XB is automatic, by part (1) of Stacks 04XS in the form
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_relativeDiagonal_algebraicStacks`.

```lean
theorem isLocallySeparated_iff_isImmersion_relativeDiagonalAlgebraicStacks :
    IsLocallySeparated B S hS f.hom ↔
      AlgebraicStacks.IsImmersion B S hS (relativeDiagonalAlgebraicStacks B S hS f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.3, Tag 04XQ](https://stacks.math.columbia.edu/tag/04XQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
