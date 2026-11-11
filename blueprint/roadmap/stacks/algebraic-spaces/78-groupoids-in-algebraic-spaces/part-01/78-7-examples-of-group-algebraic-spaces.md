---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.multiplicativeGroupSiteObject, AlgebraicGeometry.Space.multiplicativeGroupSpace, AlgebraicGeometry.Space.multiplicativeGroupSpace_obj_X, AlgebraicGeometry.Space.multiplicativeGroupSpacePoints, AlgebraicGeometry.Space.multiplicativeGroupSpacePoints_apply, AlgebraicGeometry.Space.multiplicativeGroupSpacePoints_naturality, AlgebraicGeometry.Space.rootsOfUnitySiteObject, AlgebraicGeometry.Space.rootsOfUnitySpace
statement: formalized
proof: formalized
---

# 78.7 Examples of group algebraic spaces

Section 78.7 of the Stacks Project, [Tag 06P7](https://stacks.math.columbia.edu/tag/06P7). 6 tags here are carried by 33 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 043J, an example

[Tag 043J](https://stacks.math.columbia.edu/tag/043J) in the Stacks Project.

**`AlgebraicGeometry.Space.multiplicativeGroupSiteObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Multiplicative.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Multiplicative.lean#L74). The attribute's comment: “the multiplicative group scheme as an object of the site”.

> **Stacks Project, Tag 043J.** The multiplicative group scheme over `S`, read as an object of
> the big fppf site over `S`.

```lean
noncomputable def multiplicativeGroupSiteObject : BigFppfOver 𝒞 S hS
```

**`AlgebraicGeometry.Space.multiplicativeGroupSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Multiplicative.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Multiplicative.lean#L93).

> **Stacks Project, Tag 043J.** The multiplicative group algebraic space
> `Gₘ,B = B ×_S Gₘ,S` over an algebraic space `B` over `S`.

```lean
noncomputable def multiplicativeGroupSpace (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B) : GroupAlgebraicSpace 𝒞 S hS B hB
```

**`AlgebraicGeometry.Space.multiplicativeGroupSpace_obj_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Multiplicative.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Multiplicative.lean#L101). The attribute's comment: “the underlying base change”.

> **Stacks Project, Tag 043J.** The algebraic space underlying the multiplicative group
> algebraic space is the fibre product `B ×_S Gₘ,S`.

```lean
theorem multiplicativeGroupSpace_obj_X (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B) :
    (multiplicativeGroupSpace 𝒞 S hS B hB).obj.X =
      (Over.mk (prod.fst :
        B ⨯ (multiplicativeGroupPointsOnSite 𝒞 S hS ⋙ forget GrpCat) ⟶ B) : Over B)
```

**`AlgebraicGeometry.Space.multiplicativeGroupSpacePoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Multiplicative.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Multiplicative.lean#L111). The attribute's comment: “the functor of global units”.

> **Stacks Project, Tag 043J.** The group of points of the multiplicative group algebraic
> space over a scheme `T` over `B` is the group of units in the global sections of `T`.

```lean
noncomputable def multiplicativeGroupSpacePoints (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (T : BigFppfOver 𝒞 S hS) (b : yoneda.obj T ⟶ B) :
    ((Over.mk b : Over B) ⟶
        Over.mk (prod.fst :
          B ⨯ (multiplicativeGroupPointsOnSite 𝒞 S hS ⋙ forget GrpCat) ⟶ B)) ≃*
      (globalUnits S).obj (Opposite.op ((toSchemeOver 𝒞 S hS).obj T))
```

**`AlgebraicGeometry.Space.multiplicativeGroupSpacePoints_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Multiplicative.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Multiplicative.lean#L124). The attribute's comment: “the functor of global units”.

> `AlgebraicGeometry.Space.multiplicativeGroupSpacePoints` reads a point through the second
> projection of the fibre product and the canonical identification of **Stacks 022U**.

```lean
theorem multiplicativeGroupSpacePoints_apply (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (T : BigFppfOver 𝒞 S hS) (b : yoneda.obj T ⟶ B)
    (x : (Over.mk b : Over B) ⟶
      Over.mk (prod.fst : B ⨯ (multiplicativeGroupPointsOnSite 𝒞 S hS ⋙ forget GrpCat) ⟶ B)) :
    multiplicativeGroupSpacePoints 𝒞 S hS B T b x =
      (baseChangePointsIsoGlobalUnits S).hom.app
        (Opposite.op ((toSchemeOver 𝒞 S hS).obj T))
        (yonedaEquiv (x.left ≫ (prod.snd :
          B ⨯ (multiplicativeGroupPointsOnSite 𝒞 S hS ⋙ forget GrpCat) ⟶ _)))
```

**`AlgebraicGeometry.Space.multiplicativeGroupSpacePoints_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Multiplicative.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Multiplicative.lean#L139). The attribute's comment: “the functor of global units”.

> `AlgebraicGeometry.Space.multiplicativeGroupSpacePoints` is natural in the scheme over `B`,
> so what is asserted is representability of the functor of global units and not a family of
> unrelated group isomorphisms.

```lean
theorem multiplicativeGroupSpacePoints_naturality (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (T U : BigFppfOver 𝒞 S hS) (f : T ⟶ U) (b : yoneda.obj U ⟶ B)
    (x : (Over.mk b : Over B) ⟶
      Over.mk (prod.fst : B ⨯ (multiplicativeGroupPointsOnSite 𝒞 S hS ⋙ forget GrpCat) ⟶ B)) :
    multiplicativeGroupSpacePoints 𝒞 S hS B T (yoneda.map f ≫ b)
        ((Over.homMk (yoneda.map f) :
          (Over.mk (yoneda.map f ≫ b) : Over B) ⟶ Over.mk b) ≫ x) =
      (globalUnits S ⋙ forget GrpCat).map ((toSchemeOver 𝒞 S hS).map f).op
        (multiplicativeGroupSpacePoints 𝒞 S hS B U b x)
```

## Tag 043K, an example

[Tag 043K](https://stacks.math.columbia.edu/tag/043K) in the Stacks Project.

**`AlgebraicGeometry.Space.rootsOfUnitySiteObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean#L156). The attribute's comment: “the roots-of-unity group scheme as an object of the site”. References: SGA 1 XI (6.1).

> **Stacks Project, Tag 043K.** The group scheme `μₙ,S` of `n`-th roots of unity over `S`,
> read as an object of the big fppf site over `S`.

```lean
noncomputable def rootsOfUnitySiteObject : BigFppfOver 𝒞 S hS
```

**`AlgebraicGeometry.Space.rootsOfUnitySpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean#L175).

> **Stacks Project, Tag 043K.** The group algebraic space `μₙ,B = B ×_S μₙ,S` of `n`-th roots
> of unity over an algebraic space `B` over `S`.

```lean
noncomputable def rootsOfUnitySpace [Fact (0 < n)] (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B) : GroupAlgebraicSpace 𝒞 S hS B hB
```

**`AlgebraicGeometry.Space.rootsOfUnitySpace_obj_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean#L183). The attribute's comment: “the underlying base change”.

> **Stacks Project, Tag 043K.** The algebraic space underlying the group algebraic space of
> `n`-th roots of unity is the fibre product `B ×_S μₙ,S`.

```lean
theorem rootsOfUnitySpace_obj_X [Fact (0 < n)] (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B) :
    (rootsOfUnitySpace 𝒞 S hS n B hB).obj.X =
      (Over.mk (prod.fst :
        B ⨯ (rootsOfUnityPointsOnSite 𝒞 S hS n ⋙ forget GrpCat) ⟶ B) : Over B)
```

**`AlgebraicGeometry.Space.rootsOfUnitySpacePoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean#L194). The attribute's comment: “the functor of roots of unity”.

> **Stacks Project, Tag 043K.** The group of points of the group algebraic space of `n`-th
> roots of unity over a scheme `T` over `B` is the group of `n`-th roots of unity in the global
> sections of `T`.

```lean
noncomputable def rootsOfUnitySpacePoints [Fact (0 < n)]
    (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u) (T : BigFppfOver 𝒞 S hS) (b : yoneda.obj T ⟶ B) :
    ((Over.mk b : Over B) ⟶
        Over.mk (prod.fst :
          B ⨯ (rootsOfUnityPointsOnSite 𝒞 S hS n ⋙ forget GrpCat) ⟶ B)) ≃*
      (rootsOfUnityGroupOverFunctor n S).obj
        (Opposite.op ((toSchemeOver 𝒞 S hS).obj T))
```

**`AlgebraicGeometry.Space.rootsOfUnitySpacePoints_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean#L208). The attribute's comment: “the functor of roots of unity”.

> `AlgebraicGeometry.Space.rootsOfUnitySpacePoints` reads a point through the second
> projection of the fibre product and the canonical identification of **Stacks 040M**.

```lean
theorem rootsOfUnitySpacePoints_apply [Fact (0 < n)]
    (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u) (T : BigFppfOver 𝒞 S hS) (b : yoneda.obj T ⟶ B)
    (x : (Over.mk b : Over B) ⟶
      Over.mk (prod.fst : B ⨯ (rootsOfUnityPointsOnSite 𝒞 S hS n ⋙ forget GrpCat) ⟶ B)) :
    rootsOfUnitySpacePoints 𝒞 S hS n B T b x =
      (rootsOfUnityBaseChangeGroupPointsIso n S).hom.app
        (Opposite.op ((toSchemeOver 𝒞 S hS).obj T))
        (yonedaEquiv (x.left ≫ (prod.snd :
          B ⨯ (rootsOfUnityPointsOnSite 𝒞 S hS n ⋙ forget GrpCat) ⟶ _)))
```

**`AlgebraicGeometry.Space.rootsOfUnitySpacePoints_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean#L223). The attribute's comment: “the functor of roots of unity”.

> `AlgebraicGeometry.Space.rootsOfUnitySpacePoints` is natural in the scheme over `B`, so
> what is asserted is representability of the functor of roots of unity and not a family of
> unrelated group isomorphisms.

```lean
theorem rootsOfUnitySpacePoints_naturality [Fact (0 < n)]
    (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u) (T U : BigFppfOver 𝒞 S hS) (f : T ⟶ U)
    (b : yoneda.obj U ⟶ B)
    (x : (Over.mk b : Over B) ⟶
      Over.mk (prod.fst : B ⨯ (rootsOfUnityPointsOnSite 𝒞 S hS n ⋙ forget GrpCat) ⟶ B)) :
    rootsOfUnitySpacePoints 𝒞 S hS n B T (yoneda.map f ≫ b)
        ((Over.homMk (yoneda.map f) :
          (Over.mk (yoneda.map f ≫ b) : Over B) ⟶ Over.mk b) ≫ x) =
      (rootsOfUnityGroupOverFunctor n S ⋙ forget GrpCat).map
        ((toSchemeOver 𝒞 S hS).map f).op
        (rootsOfUnitySpacePoints 𝒞 S hS n B U b x)
```

## Tag 043L, an example

[Tag 043L](https://stacks.math.columbia.edu/tag/043L) in the Stacks Project.

**`AlgebraicGeometry.Space.additiveGroupSiteObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Additive.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Additive.lean#L64). The attribute's comment: “the additive group scheme as an object of the site”.

> The additive group scheme over `S`, read as an object of the big fppf site over `S`.

```lean
noncomputable def additiveGroupSiteObject : BigFppfOver 𝒞 S hS
```

**`AlgebraicGeometry.Space.additiveGroupSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Additive.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Additive.lean#L82).

> The additive group algebraic space `Gₐ,B = B ×_S Gₐ,S` over an algebraic space `B` over
> `S`.

```lean
noncomputable def additiveGroupSpace (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B) : GroupAlgebraicSpace 𝒞 S hS B hB
```

**`AlgebraicGeometry.Space.additiveGroupSpace_obj_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Additive.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Additive.lean#L90). The attribute's comment: “the underlying base change”.

> The algebraic space underlying the additive group algebraic space is the fibre product
> `B ×_S Gₐ,S`.

```lean
theorem additiveGroupSpace_obj_X (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B) :
    (additiveGroupSpace 𝒞 S hS B hB).obj.X =
      (Over.mk (prod.fst :
        B ⨯ (additiveGroupPointsOnSite 𝒞 S hS ⋙ forget GrpCat) ⟶ B) : Over B)
```

**`AlgebraicGeometry.Space.additiveGroupSpacePoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Additive.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Additive.lean#L100). The attribute's comment: “the functor of global sections”.

> The group of points of the additive group algebraic space over a scheme `T` over `B` is the
> additive group of global sections of `T`.

```lean
noncomputable def additiveGroupSpacePoints (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (T : BigFppfOver 𝒞 S hS) (b : yoneda.obj T ⟶ B) :
    ((Over.mk b : Over B) ⟶
        Over.mk (prod.fst :
          B ⨯ (additiveGroupPointsOnSite 𝒞 S hS ⋙ forget GrpCat) ⟶ B)) ≃*
      (globalSectionsAdditive S).obj (Opposite.op ((toSchemeOver 𝒞 S hS).obj T))
```

**`AlgebraicGeometry.Space.additiveGroupSpacePoints_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Additive.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Additive.lean#L113). The attribute's comment: “the functor of global sections”.

> `AlgebraicGeometry.Space.additiveGroupSpacePoints` reads a point through the second
> projection of the fibre product and the canonical identification of **Stacks 022V**.

```lean
theorem additiveGroupSpacePoints_apply (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (T : BigFppfOver 𝒞 S hS) (b : yoneda.obj T ⟶ B)
    (x : (Over.mk b : Over B) ⟶
      Over.mk (prod.fst : B ⨯ (additiveGroupPointsOnSite 𝒞 S hS ⋙ forget GrpCat) ⟶ B)) :
    additiveGroupSpacePoints 𝒞 S hS B T b x =
      (additiveGroupBaseChangePointsIsoGlobalSections S).hom.app
        (Opposite.op ((toSchemeOver 𝒞 S hS).obj T))
        (yonedaEquiv (x.left ≫ (prod.snd :
          B ⨯ (additiveGroupPointsOnSite 𝒞 S hS ⋙ forget GrpCat) ⟶ _)))
```

**`AlgebraicGeometry.Space.additiveGroupSpacePoints_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Additive.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/Additive.lean#L126). The attribute's comment: “the functor of global sections”.

> `AlgebraicGeometry.Space.additiveGroupSpacePoints` is natural in the scheme over `B`.

```lean
theorem additiveGroupSpacePoints_naturality (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (T U : BigFppfOver 𝒞 S hS) (f : T ⟶ U) (b : yoneda.obj U ⟶ B)
    (x : (Over.mk b : Over B) ⟶
      Over.mk (prod.fst : B ⨯ (additiveGroupPointsOnSite 𝒞 S hS ⋙ forget GrpCat) ⟶ B)) :
    additiveGroupSpacePoints 𝒞 S hS B T (yoneda.map f ≫ b)
        ((Over.homMk (yoneda.map f) :
          (Over.mk (yoneda.map f ≫ b) : Over B) ⟶ Over.mk b) ≫ x) =
      (globalSectionsAdditive S ⋙ forget GrpCat).map ((toSchemeOver 𝒞 S hS).map f).op
        (additiveGroupSpacePoints 𝒞 S hS B U b x)
```

## Tag 043M, an example

[Tag 043M](https://stacks.math.columbia.edu/tag/043M) in the Stacks Project.

**`AlgebraicGeometry.Space.generalLinearSiteObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/GeneralLinear.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/GeneralLinear.lean#L78). The attribute's comment: “the general linear group scheme as an object of the site”.

> The general linear group scheme over `S`, read as an object of the big fppf site over `S`.

```lean
noncomputable def generalLinearSiteObject : BigFppfOver 𝒞 S hS
```

**`AlgebraicGeometry.Space.generalLinearSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/GeneralLinear.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/GeneralLinear.lean#L97).

> The general linear group algebraic space `GLₙ,B = B ×_S GLₙ,S` over an algebraic space `B`
> over `S`.

```lean
noncomputable def generalLinearSpace (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B) : GroupAlgebraicSpace 𝒞 S hS B hB
```

**`AlgebraicGeometry.Space.generalLinearSpace_obj_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/GeneralLinear.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/GeneralLinear.lean#L105). The attribute's comment: “the underlying base change”.

> The algebraic space underlying the general linear group algebraic space is the fibre product
> `B ×_S GLₙ,S`.

```lean
theorem generalLinearSpace_obj_X (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B) :
    (generalLinearSpace 𝒞 S hS n B hB).obj.X =
      (Over.mk (prod.fst :
        B ⨯ (generalLinearPointsOnSite 𝒞 S hS n ⋙ forget GrpCat) ⟶ B) : Over B)
```

**`AlgebraicGeometry.Space.generalLinearSpacePoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/GeneralLinear.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/GeneralLinear.lean#L115). The attribute's comment: “the functor of invertible matrices”.

> The group of points of the general linear group algebraic space over a scheme `T` over `B` is
> the group of invertible `n × n` matrices over the global sections of `T`.

```lean
noncomputable def generalLinearSpacePoints (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (T : BigFppfOver 𝒞 S hS) (b : yoneda.obj T ⟶ B) :
    ((Over.mk b : Over B) ⟶
        Over.mk (prod.fst :
          B ⨯ (generalLinearPointsOnSite 𝒞 S hS n ⋙ forget GrpCat) ⟶ B)) ≃*
      (generalLinearGroupOverFunctor n S).obj
        (Opposite.op ((toSchemeOver 𝒞 S hS).obj T))
```

**`AlgebraicGeometry.Space.generalLinearSpacePoints_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/GeneralLinear.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/GeneralLinear.lean#L129). The attribute's comment: “the functor of invertible matrices”.

> `AlgebraicGeometry.Space.generalLinearSpacePoints` sends a point to the image of its second
> projection to `GLₙ,S` under the canonical identification of **Stacks 022W**.

```lean
theorem generalLinearSpacePoints_apply (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (T : BigFppfOver 𝒞 S hS) (b : yoneda.obj T ⟶ B)
    (x : (Over.mk b : Over B) ⟶
      Over.mk (prod.fst : B ⨯ (generalLinearPointsOnSite 𝒞 S hS n ⋙ forget GrpCat) ⟶ B)) :
    generalLinearSpacePoints 𝒞 S hS n B T b x =
      (baseChangeGroupPointsIso n S).hom.app
        (Opposite.op ((toSchemeOver 𝒞 S hS).obj T))
        (yonedaEquiv (x.left ≫ (prod.snd :
          B ⨯ (generalLinearPointsOnSite 𝒞 S hS n ⋙ forget GrpCat) ⟶ _)))
```

**`AlgebraicGeometry.Space.generalLinearSpacePoints_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/GeneralLinear.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/GeneralLinear.lean#L142). The attribute's comment: “the functor of invertible matrices”.

> `AlgebraicGeometry.Space.generalLinearSpacePoints` is natural in the scheme over `B`.

```lean
theorem generalLinearSpacePoints_naturality (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (T U : BigFppfOver 𝒞 S hS) (f : T ⟶ U) (b : yoneda.obj U ⟶ B)
    (x : (Over.mk b : Over B) ⟶
      Over.mk (prod.fst : B ⨯ (generalLinearPointsOnSite 𝒞 S hS n ⋙ forget GrpCat) ⟶ B)) :
    generalLinearSpacePoints 𝒞 S hS n B T (yoneda.map f ≫ b)
        ((Over.homMk (yoneda.map f) :
          (Over.mk (yoneda.map f ≫ b) : Over B) ⟶ Over.mk b) ≫ x) =
      (generalLinearGroupOverFunctor n S ⋙ forget GrpCat).map
        ((toSchemeOver 𝒞 S hS).map f).op
        (generalLinearSpacePoints 𝒞 S hS n B U b x)
```

## Tag 043N, an example

[Tag 043N](https://stacks.math.columbia.edu/tag/043N) in the Stacks Project.

**`AlgebraicGeometry.Space.determinantGroupSpaceMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Determinant.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Determinant.lean#L200).

> **Stacks Project, Tag 043N.** The determinant, as a morphism of group algebraic spaces
> `GLₙ,B ⟶ Gₘ,B` over an algebraic space `B` over `S`.  It is the base change to `B` of the
> determinant morphism of group schemes over `S`.

```lean
noncomputable def determinantGroupSpaceMorphism (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B) :
    generalLinearSpace 𝒞 S hS n B hB ⟶ multiplicativeGroupSpace 𝒞 S hS B hB
```

**`AlgebraicGeometry.Space.determinantGroupSpaceMorphism_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Determinant.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Determinant.lean#L214). The attribute's comment: “base change of the determinant morphism over the base scheme”.

> **Stacks Project, Tag 043N.** The morphism over `B` underlying the determinant morphism of
> group algebraic spaces is the product of the identity of `B` with the determinant morphism of
> group schemes over `S`; that is, `det` on `GLₙ,B` is the base change of `det` on `GLₙ,S`.

```lean
theorem determinantGroupSpaceMorphism_hom (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B) :
    (determinantGroupSpaceMorphism 𝒞 S hS n B hB).hom.hom.hom =
      determinantSpaceHom 𝒞 S hS n B
```

**`AlgebraicGeometry.Space.determinantSpaceHom_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Determinant.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Determinant.lean#L246). The attribute's comment: “the determinant on points”.

> **Stacks Project, Tag 043N.** On every scheme `T` over `B` the determinant morphism of group
> algebraic spaces sends a point of `GLₙ,B`, that is an invertible `n × n` matrix over the global
> sections of `T`, to its determinant, viewed as a global unit.  Its underlying morphism over `B`
> is `AlgebraicGeometry.Space.determinantSpaceHom`, by
> `AlgebraicGeometry.Space.determinantGroupSpaceMorphism_hom`.

```lean
theorem determinantSpaceHom_apply (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (T : BigFppfOver 𝒞 S hS) (b : yoneda.obj T ⟶ B)
    (x : (Over.mk b : Over B) ⟶
      Over.mk (prod.fst : B ⨯ (generalLinearPointsOnSite 𝒞 S hS n ⋙ forget GrpCat) ⟶ B)) :
    multiplicativeGroupSpacePoints 𝒞 S hS B T b (x ≫ determinantSpaceHom 𝒞 S hS n B) =
      Matrix.GeneralLinearGroup.det (generalLinearSpacePoints 𝒞 S hS n B T b x)
```

## Tag 043O, an example

[Tag 043O](https://stacks.math.columbia.edu/tag/043O) in the Stacks Project.

**`AlgebraicGeometry.Space.constantGroupSiteObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantGroup.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantGroup.lean#L80). The attribute's comment: “the constant group scheme as an object of the site”.

> **Stacks Project, Tag 043O.** The constant group scheme `G_S` of **Stacks 03YW**, read as an
> object of the big fppf site over `S`.  That it belongs to the site is a size hypothesis on the
> site: `G` is an arbitrary abstract group, so no single big site can contain `G_S` for all `G`.

```lean
noncomputable def constantGroupSiteObject
    (hG : 𝒞.Contains (constantGroupScheme G S).X.left) : BigFppfOver 𝒞 S hS
```

**`AlgebraicGeometry.Space.constantGroupSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantGroup.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantGroup.lean#L102).

> **Stacks Project, Tag 043O.** The constant group algebraic space `G_B = B ×_S G_S` over an
> algebraic space `B` over `S`, for an abstract group `G`.

```lean
noncomputable def constantGroupSpace (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B)
    (hG : 𝒞.Contains (constantGroupScheme G S).X.left) :
    GroupAlgebraicSpace 𝒞 S hS B hB
```

**`AlgebraicGeometry.Space.constantGroupSpace_obj_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantGroup.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantGroup.lean#L112). The attribute's comment: “the underlying base change”.

> **Stacks Project, Tag 043O.** The algebraic space underlying the constant group algebraic
> space is the fibre product `B ×_S G_S`.

```lean
theorem constantGroupSpace_obj_X (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B)
    (hG : 𝒞.Contains (constantGroupScheme G S).X.left) :
    (constantGroupSpace 𝒞 S hS G B hB hG).obj.X =
      (Over.mk (prod.fst :
        B ⨯ (constantGroupPointsOnSite 𝒞 S hS G hG ⋙ forget GrpCat) ⟶ B) : Over B)
```

**`AlgebraicGeometry.Space.constantGroupSpacePoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantGroup.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantGroup.lean#L123). The attribute's comment: “the functor of locally constant maps”. References: SGA 3 I (4.1), “Hom = loc const maps”.

> **Stacks Project, Tag 043O.** The group of points of the constant group algebraic space over
> a scheme `T` over `B` is the group of locally constant `G`-valued maps on `T`.

```lean
noncomputable def constantGroupSpacePoints (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hG : 𝒞.Contains (constantGroupScheme G S).X.left) (T : BigFppfOver 𝒞 S hS)
    (b : yoneda.obj T ⟶ B) :
    ((Over.mk b : Over B) ⟶
        Over.mk (prod.fst :
          B ⨯ (constantGroupPointsOnSite 𝒞 S hS G hG ⋙ forget GrpCat) ⟶ B)) ≃*
      (locallyConstantMapsOver G S).obj (Opposite.op ((toSchemeOver 𝒞 S hS).obj T))
```

**`AlgebraicGeometry.Space.constantGroupSpacePoints_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantGroup.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantGroup.lean#L139). The attribute's comment: “the functor of locally constant maps”.

> `AlgebraicGeometry.Space.constantGroupSpacePoints` reads a point through the second
> projection of the fibre product and the canonical identification of **Stacks 03YW**.

```lean
theorem constantGroupSpacePoints_apply (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hG : 𝒞.Contains (constantGroupScheme G S).X.left) (T : BigFppfOver 𝒞 S hS)
    (b : yoneda.obj T ⟶ B)
    (x : (Over.mk b : Over B) ⟶
      Over.mk (prod.fst :
        B ⨯ (constantGroupPointsOnSite 𝒞 S hS G hG ⋙ forget GrpCat) ⟶ B)) :
    constantGroupSpacePoints 𝒞 S hS G B hG T b x =
      (constantGroupSchemePointsIsoLocallyConstantMaps G S).hom.app
        (Opposite.op ((toSchemeOver 𝒞 S hS).obj T))
        (ULift.up (yonedaEquiv (x.left ≫ (prod.snd :
          B ⨯ (constantGroupPointsOnSite 𝒞 S hS G hG ⋙ forget GrpCat) ⟶ _))))
```

**`AlgebraicGeometry.Space.constantGroupSpacePoints_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantGroup.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantGroup.lean#L156). The attribute's comment: “the functor of locally constant maps”.

> `AlgebraicGeometry.Space.constantGroupSpacePoints` is natural in the scheme over `B`, so
> what is asserted is representability of the functor of locally constant maps and not a family of
> unrelated group isomorphisms.

```lean
theorem constantGroupSpacePoints_naturality (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hG : 𝒞.Contains (constantGroupScheme G S).X.left) (T U : BigFppfOver 𝒞 S hS) (f : T ⟶ U)
    (b : yoneda.obj U ⟶ B)
    (x : (Over.mk b : Over B) ⟶
      Over.mk (prod.fst :
        B ⨯ (constantGroupPointsOnSite 𝒞 S hS G hG ⋙ forget GrpCat) ⟶ B)) :
    constantGroupSpacePoints 𝒞 S hS G B hG T (yoneda.map f ≫ b)
        ((Over.homMk (yoneda.map f) :
          (Over.mk (yoneda.map f ≫ b) : Over B) ⟶ Over.mk b) ≫ x) =
      (locallyConstantMapsOver G S ⋙ forget GrpCat).map ((toSchemeOver 𝒞 S hS).map f).op
        (constantGroupSpacePoints 𝒞 S hS G B hG U b x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.7, Tag 06P7](https://stacks.math.columbia.edu/tag/06P7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
