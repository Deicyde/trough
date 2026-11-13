---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.Descent.DescentData, AlgebraicGeometry.Space.Descent.DescentData.Hom, AlgebraicGeometry.Space.Descent.gluingProjEquiv, AlgebraicGeometry.Space.Descent.DescentData.projGluing, AlgebraicGeometry.Space.Descent.DescentData.projGluing01_comp_projGluing12, AlgebraicGeometry.Space.Descent.familyCoproductEquivalenceOfAdmitsCoproductIndex, AlgebraicGeometry.Space.Descent.pullbackDescentDataFunctor, AlgebraicGeometry.Space.Descent.pullbackDescentDataFunctor_canonicalIso
statement: formalized
proof: formalized
---

# 74.22 Descent data for spaces over spaces

Section 74.22 of the Stacks Project, [Tag 0ADF](https://stacks.math.columbia.edu/tag/0ADF). 11 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ADG, a definition

[Tag 0ADG](https://stacks.math.columbia.edu/tag/0ADG) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.DescentData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Descent.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Descent.lean#L58). The attribute's comment: “parts (1) and (2): a descent datum relative to one morphism Y → X”. References: SGA 3 IV (2.1), “descent datum”.

> A descent datum relative to a family of morphisms of algebraic spaces over a scheme.

```lean
public structure DescentData
    (hT : IsAlgebraicSpace B S hS T)
    (hX : ∀ i, IsAlgebraicSpace B S hS (X i))
```

**`AlgebraicGeometry.Space.Descent.DescentData.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Descent.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Descent.lean#L84). The attribute's comment: “parts (1) and (2): a descent datum relative to one morphism Y → X”.

> A morphism of descent data is a compatible family of maps over the family members.

```lean
public structure Hom (D E : DescentData f hT hX)
```

## Tag 0ADH, a remark

[Tag 0ADH](https://stacks.math.columbia.edu/tag/0ADH) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.gluingProjEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/ProjectionBaseChange.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/ProjectionBaseChange.lean#L217). The attribute's comment: “the two presentations of the gluing isomorphism of a descent datum”.

> Over the pairwise fibre product `X i ×_T X j`, an isomorphism `V_i ×_T X_j ≅ X_i ×_T V_j`
> is the same thing as an isomorphism `pr₀^* V_i ≅ pr₁^* V_j` of the two base changes along the
> projections.

```lean
def gluingProjEquiv (i j : ι) (Vi : Over (X i)) (Vj : Over (X j)) :
    (Over.mk (prod.map (structureMap (f i) Vi) (𝟙 (Over.mk (f j)))) ≅
        Over.mk (prod.map (𝟙 (Over.mk (f i))) (structureMap (f j) Vj))) ≃
      (projFstObj f i j Vi ≅ projSndObj f i j Vj)
```

**`AlgebraicGeometry.Space.Descent.DescentData.projGluing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/ProjectionBaseChange.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/ProjectionBaseChange.lean#L251). The attribute's comment: “the gluing isomorphism read as a map pr₀^* V ⟶ pr₁^* V”.

> The gluing isomorphism of a descent datum, read as an isomorphism `pr₀^* V_i ≅ pr₁^* V_j`
> of algebraic spaces over the pairwise fibre product `X i ×_T X j`.

```lean
def projGluing (D : DescentData f hT hX) (i j : ι) :
    projFstObj f i j (D.obj i) ≅ projSndObj f i j (D.obj j)
```

**`AlgebraicGeometry.Space.Descent.DescentData.projGluing01_comp_projGluing12`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/ProjectionBaseChange.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/ProjectionBaseChange.lean#L379). The attribute's comment: “the cocycle condition in the form pr₀₂^* φ = pr₁₂^* φ ∘ pr₀₁^* φ”.

> The cocycle condition of a descent datum, read on base changes along the projections of
> the triple fibre product: `pr₀₂^* φ_ik = pr₁₂^* φ_jk ∘ pr₀₁^* φ_ij`.

```lean
theorem projGluing01_comp_projGluing12 (D : DescentData f hT hX) (i j k : ι) :
    D.projGluing01 i j k ≫ D.projGluing12 i j k = D.projGluing02 i j k
```

## Tag 0ADI, a definition

[Tag 0ADI](https://stacks.math.columbia.edu/tag/0ADI) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.DescentData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Descent.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Descent.lean#L58). The attribute's comment: “part (1), descent data”. References: SGA 3 IV (2.1), “descent datum”.

> A descent datum relative to a family of morphisms of algebraic spaces over a scheme.

```lean
public structure DescentData
    (hT : IsAlgebraicSpace B S hS T)
    (hX : ∀ i, IsAlgebraicSpace B S hS (X i))
```

**`AlgebraicGeometry.Space.Descent.DescentData.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Descent.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Descent.lean#L84). The attribute's comment: “part (2), morphisms of descent data”.

> A morphism of descent data is a compatible family of maps over the family members.

```lean
public structure Hom (D E : DescentData f hT hX)
```

## Tag 0ADJ, a remark

[Tag 0ADJ](https://stacks.math.columbia.edu/tag/0ADJ) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.DescentData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Descent.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Descent.lean#L58). The attribute's comment: “the gluing isomorphisms and the cocycle condition in pullback form”. References: SGA 3 IV (2.1), “descent datum”.

> A descent datum relative to a family of morphisms of algebraic spaces over a scheme.

```lean
public structure DescentData
    (hT : IsAlgebraicSpace B S hS T)
    (hX : ∀ i, IsAlgebraicSpace B S hS (X i))
```

## Tag 0ADK, a lemma

[Tag 0ADK](https://stacks.math.columbia.edu/tag/0ADK) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.familyCoproductEquivalenceOfAdmitsCoproductIndex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/CoproductAlgebraicityFull.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/CoproductAlgebraicityFull.lean#L188).

> Let `{f i : X i → T}` be a family of morphisms of algebraic spaces over `S` with fixed
> target, and let `Y = ∐ X i` be the coproduct of the sources in sheaves on the big fppf site, an
> algebraic space over `S` by `AlgebraicGeometry.Space.Descent.sigmaAlgebraicSheafCoproduct`. There
> is a canonical equivalence from the category of descent data relative to the family to the
> category of descent data relative to `Y → T`, which sends `(V i, φ i j)` to `(V, φ)` with
> `V = ∐ V i` and `φ` restricting to `φ i j` on each pair of summands, and a morphism `(ψ i)` to
> `∐ ψ i`.
>
> The index type is `u`-small and of cardinality below the cofinality of the site's size cutoff,
> as is every countable index type.

```lean
public def familyCoproductEquivalenceOfAdmitsCoproductIndex :
    FullFamilyCoproductEquivalence.{u, v, w} f hT hX (sigmaAlgebraicSheafCoproduct X hX)
```

## Tag 0ADL, a lemma

[Tag 0ADL](https://stacks.math.columbia.edu/tag/0ADL) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.pullbackDescentDataFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/HomDescent.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/HomDescent.lean#L157). The attribute's comment: “part (1), pullback functor”.

> The pullback functor on descent data, with the canonical natural comparison of its
> underlying space over `Y'` with ordinary pullback along `f`.

```lean
public def pullbackDescentDataFunctor
    {X X' Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : Y ⟶ X) (a' : Y' ⟶ X') (h : X' ⟶ X) (f : Y' ⟶ Y)
    (ha : f ≫ a = a' ≫ h)
    (hX : IsAlgebraicSpace B S hS X)
    (hX' : IsAlgebraicSpace B S hS X')
    (hY : IsAlgebraicSpace B S hS Y)
    (hY' : IsAlgebraicSpace B S hS Y') :
    { F : HomDescentData.{u, v} a hX hY ⥤ HomDescentData.{u, w} a' hX' hY' //
      ∃ α : ∀ D : HomDescentData.{u, v} a hX hY,
          (F.obj D).obj PUnit.unit ≅ (Over.pullback f).obj (D.obj PUnit.unit),
        (∀ {D E : HomDescentData.{u, v} a hX hY} (φ : D ⟶ E),
          (F.map φ).hom PUnit.unit ≫ (α E).hom =
            (α D).hom ≫ (Over.pullback f).map (φ.hom PUnit.unit)) ∧
        (∀ D : HomDescentData.{u, v} a hX hY,
          let A' := (Over.map a').obj ((F.obj D).obj PUnit.unit)
          let B' := Over.mk a'
          let A := (Over.map a).obj (D.obj PUnit.unit)
          let B := Over.mk a
          ∃ (q : (Over.map h).obj A' ⟶ A)
            (r : (Over.map h).obj B' ⟶ B),
            q.left = (α D).hom.left ≫ pullback.fst (D.obj PUnit.unit).hom f ∧
            r.left = f ∧
            (let s : (Over.map h).obj (A' ⨯ B') ⟶ A ⨯ B :=
                prod.lift ((Over.map h).map (prod.fst : A' ⨯ B' ⟶ A') ≫ q)
                  ((Over.map h).map (prod.snd : A' ⨯ B' ⟶ B') ≫ r)
             let t : (Over.map h).obj (B' ⨯ A') ⟶ B ⨯ A :=
                prod.lift ((Over.map h).map (prod.fst : B' ⨯ A' ⟶ B') ≫ r)
                  ((Over.map h).map (prod.snd : B' ⨯ A' ⟶ A') ≫ q)
             (Over.map h).map ((F.obj D).gluing PUnit.unit PUnit.unit).hom.left ≫ t =
               s ≫ (D.gluing PUnit.unit PUnit.unit).hom.left)) }
```

**`AlgebraicGeometry.Space.Descent.pullbackDescentDataFunctor_canonicalIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/HomDescent.lean, line 445](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/HomDescent.lean#L445). The attribute's comment: “part (2), canonical isomorphism”.

> Pullback along two maps completing the same square is canonically and naturally
> isomorphic, by the gluing isomorphism of the descent datum.

```lean
public def pullbackDescentDataFunctor_canonicalIso :
    let F₀ := pullbackDescentDataFunctor.{u, v, w} a a' h f₀ ha₀ hX hX' hY hY'
    let F₁ := pullbackDescentDataFunctor.{u, v, w} a a' h f₁ ha₁ hX hX' hY hY'
    let α₀ := Classical.choose F₀.property
    let α₁ := Classical.choose F₁.property
    { η : F₀.val ≅ F₁.val //
      ∀ D : HomDescentData.{u, v} a hX hY,
        let V₀ := (F₀.val.obj D).obj PUnit.unit
        let V₁ := (F₁.val.obj D).obj PUnit.unit
        let A := (Over.map a).obj (D.obj PUnit.unit)
        let B₀ := Over.mk a
        ∃ (q₀ : (Over.map (a' ≫ h)).obj V₀ ⟶ A)
          (q₁ : (Over.map (a' ≫ h)).obj V₁ ⟶ A)
          (y₁ : (Over.map (a' ≫ h)).obj V₀ ⟶ B₀)
          (y₀ : (Over.map (a' ≫ h)).obj V₁ ⟶ B₀),
          q₀.left = (α₀ D).hom.left ≫ pullback.fst (D.obj PUnit.unit).hom f₀ ∧
          q₁.left = (α₁ D).hom.left ≫ pullback.fst (D.obj PUnit.unit).hom f₁ ∧
          y₁.left = V₀.hom ≫ f₁ ∧ y₀.left = V₁.hom ≫ f₀ ∧
          prod.lift q₀ y₁ ≫ (D.gluing PUnit.unit PUnit.unit).hom.left =
            (Over.map (a' ≫ h)).map ((η.hom.app D).hom PUnit.unit) ≫
              prod.lift y₀ q₁ }
```

## Tag 0ADM, a definition

[Tag 0ADM](https://stacks.math.columbia.edu/tag/0ADM) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.pullbackDescentDataFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/HomDescent.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/HomDescent.lean#L157). The attribute's comment: “the functor so constructed is the pullback functor on descent data”.

> The pullback functor on descent data, with the canonical natural comparison of its
> underlying space over `Y'` with ordinary pullback along `f`.

```lean
public def pullbackDescentDataFunctor
    {X X' Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : Y ⟶ X) (a' : Y' ⟶ X') (h : X' ⟶ X) (f : Y' ⟶ Y)
    (ha : f ≫ a = a' ≫ h)
    (hX : IsAlgebraicSpace B S hS X)
    (hX' : IsAlgebraicSpace B S hS X')
    (hY : IsAlgebraicSpace B S hS Y)
    (hY' : IsAlgebraicSpace B S hS Y') :
    { F : HomDescentData.{u, v} a hX hY ⥤ HomDescentData.{u, w} a' hX' hY' //
      ∃ α : ∀ D : HomDescentData.{u, v} a hX hY,
          (F.obj D).obj PUnit.unit ≅ (Over.pullback f).obj (D.obj PUnit.unit),
        (∀ {D E : HomDescentData.{u, v} a hX hY} (φ : D ⟶ E),
          (F.map φ).hom PUnit.unit ≫ (α E).hom =
            (α D).hom ≫ (Over.pullback f).map (φ.hom PUnit.unit)) ∧
        (∀ D : HomDescentData.{u, v} a hX hY,
          let A' := (Over.map a').obj ((F.obj D).obj PUnit.unit)
          let B' := Over.mk a'
          let A := (Over.map a).obj (D.obj PUnit.unit)
          let B := Over.mk a
          ∃ (q : (Over.map h).obj A' ⟶ A)
            (r : (Over.map h).obj B' ⟶ B),
            q.left = (α D).hom.left ≫ pullback.fst (D.obj PUnit.unit).hom f ∧
            r.left = f ∧
            (let s : (Over.map h).obj (A' ⨯ B') ⟶ A ⨯ B :=
                prod.lift ((Over.map h).map (prod.fst : A' ⨯ B' ⟶ A') ≫ q)
                  ((Over.map h).map (prod.snd : A' ⨯ B' ⟶ B') ≫ r)
             let t : (Over.map h).obj (B' ⨯ A') ⟶ B ⨯ A :=
                prod.lift ((Over.map h).map (prod.fst : B' ⨯ A' ⟶ B') ≫ r)
                  ((Over.map h).map (prod.snd : B' ⨯ A' ⟶ A') ≫ q)
             (Over.map h).map ((F.obj D).gluing PUnit.unit PUnit.unit).hom.left ≫ t =
               s ≫ (D.gluing PUnit.unit PUnit.unit).hom.left)) }
```

## Tag 0ADN, a lemma

[Tag 0ADN](https://stacks.math.columbia.edu/tag/0ADN) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.pullbackDatum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/FamilyPullback.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/FamilyPullback.lean#L224). The attribute's comment: “family\_pullback\_datum”.

> Pullback of a descent datum along a morphism of families of algebraic spaces.

```lean
public def pullbackDatum (g : T' ⟶ T) (comm : ∀ i, gᵢ i ≫ f (α i) = f' i ≫ g) :
    PulledBackDatum f f' hT hX hT' hX' α gᵢ D
```

**`AlgebraicGeometry.Space.Descent.pullbackFunctorCoproductComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/FamilyPullbackCoproduct.lean, line 1086](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/FamilyPullbackCoproduct.lean#L1086). The attribute's comment: “part (4), agreement with the pullback functors of 0ADL through 0ADK”.

> **Stacks Project, Tag 0ADN part (4).** Let `U = {X j → T}` and `U' = {X' i → T'}` be
> families of morphisms of algebraic spaces over `S` with fixed target, and let
> `α : I' → I`, `g : T' → T`, `gᵢ : X' i → X (α i)` be a morphism of families with fixed
> target. The pullback functor on descent data along that morphism of families, Tag 0ADN
> part (2), agrees — through the canonical equivalences of Tag 0ADK between descent data for a
> family and descent data for the coproduct of its sources — with the pullback functor of
> Tag 0ADL for the induced commutative square
> `∐ X' i → ∐ X j`, `T' → T` of single morphisms.
>
> The isomorphism is pinned on each summand: on the `i`-th summand of the coproduct of the
> pulled-back components it is the projection of `X' i ×_{X (α i)} V (α i)` onto `V (α i)`,
> followed by the inclusion of the `α i`-th summand of the coproduct of the original
> components.
>
> The index types are `u`-small and of cardinality below the cofinality of the site's size
> cutoff, as is every countable index type. This is the same size condition that
> `AlgebraicGeometry.Space.Descent.familyCoproductEquivalenceOfAdmitsCoproductIndex` carries,
> and it is what makes the coproducts exist at all.

```lean
public def pullbackFunctorCoproductComparison :
    let Ycop := sigmaAlgebraicSheafCoproduct X hX
    let Y'cop := sigmaAlgebraicSheafCoproduct X' hX'
    let E := familyCoproductEquivalenceOfAdmitsCoproductIndex.{u, v, w} f hT hX
    let E' := familyCoproductEquivalenceOfAdmitsCoproductIndex.{u, v', w} f' hT' hX'
    let P := pullbackFunctor f f' hT hX hT' hX' α g gᵢ comm
    let F := pullbackDescentDataFunctor.{u, w, w} (Ycop.desc (spaceSheaf T hT) f)
      (Y'cop.desc (spaceSheaf T' hT') f') g (coproductMap hX hX' α gᵢ Ycop Y'cop)
      (coproductMap_comm f f' hT hX hT' hX' α g gᵢ comm Ycop Y'cop) hT hT'
      Ycop.isAlgebraicSpace Y'cop.isAlgebraicSpace
    let αF := Classical.choose F.property
    { η : P.functor ⋙ E'.equivalence.functor ≅ E.equivalence.functor ⋙ F.val //
      ∀ (D : DescentData f hT hX) (i : ι'),
        ((fullTotalCoproduct f' hT' hX' (P.functor.obj D)).ι i).hom ≫
            (E'.objIso (P.functor.obj D)).inv.left ≫
            ((η.hom.app D).hom PUnit.unit).left ≫
            (αF (E.equivalence.functor.obj D)).hom.left ≫
            pullback.fst ((E.equivalence.functor.obj D).obj PUnit.unit).hom
              (coproductMap hX hX' α gᵢ Ycop Y'cop) =
          ((eqToHom (P.obj_eq D)).hom i).left ≫
            (pullbackDatum f f' hT hX hT' hX' α gᵢ D g comm).objMap i ≫
            ((fullTotalCoproduct f hT hX D).ι (α i)).hom ≫ (E.objIso D).inv.left }
```

**`AlgebraicGeometry.Space.Descent.pullbackFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/FamilyPullbackFunctor.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/FamilyPullbackFunctor.lean#L81). The attribute's comment: “family\_pullback\_functor”.

> Pullback along a morphism of families is functorial on descent data. This is the pullback
> functor named by Tag 0ADP.

```lean
public noncomputable def pullbackFunctor :
    PullbackFunctor f f' hT hX hT' hX' α g gᵢ comm
```

**`AlgebraicGeometry.Space.Descent.pullbackFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/FamilyPullbackIndependence.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/FamilyPullbackIndependence.lean#L306). The attribute's comment: “family\_map\_independence”.

> The canonical natural isomorphism between the pullback functors induced by two morphisms of
> families with the same map of targets.

```lean
public def pullbackFunctorIso :
    PullbackFunctorIso f f' hT hX hT' hX' α β g gᵢ hᵢ commα commβ
      (pullbackFunctor f f' hT hX hT' hX' α g gᵢ commα)
      (pullbackFunctor f f' hT hX hT' hX' β g hᵢ commβ)
```

## Tag 0ADP, a definition

[Tag 0ADP](https://stacks.math.columbia.edu/tag/0ADP) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.pullbackFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/FamilyPullbackFunctor.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/FamilyPullbackFunctor.lean#L81).

> Pullback along a morphism of families is functorial on descent data. This is the pullback
> functor named by Tag 0ADP.

```lean
public noncomputable def pullbackFunctor :
    PullbackFunctor f f' hT hX hT' hX' α g gᵢ comm
```

## Tag 0ADQ, a definition

[Tag 0ADQ](https://stacks.math.columbia.edu/tag/0ADQ) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.trivialDescentFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/Effective.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/Effective.lean#L57). The attribute's comment: “part (1), trivial descent datum”.

> An algebraic space over `X` carries its trivial descent datum for the identity of `X`.

```lean
public def trivialDescentFunctor (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) :
    AlgebraicSpacesOver (B := B) (S := S) (hS := hS) X ⥤
      HomDescentData.{u, v} (𝟙 X) hX hX
```

**`AlgebraicGeometry.Space.Descent.canonicalDescentFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/Effective.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/Effective.lean#L78). The attribute's comment: “part (2), canonical descent datum”.

> Pulling the trivial descent datum back along a morphism gives the canonical descent
> datum of an algebraic space over the target.

```lean
public def canonicalDescentFunctor {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : Y ⟶ X)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    AlgebraicSpacesOver (B := B) (S := S) (hS := hS) X ⥤ HomDescentData.{u, v} f hX hY
```

**`AlgebraicGeometry.Space.Descent.HomDescentData.IsEffective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/Effective.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/Effective.lean#L87). The attribute's comment: “part (3), effectivity”.

> A descent datum for one morphism is effective if it is isomorphic to the canonical descent
> datum of an algebraic space over the target.

```lean
public abbrev HomDescentData.IsEffective {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : Y ⟶ X}
    {hX : IsAlgebraicSpace B S hS X} {hY : IsAlgebraicSpace B S hS Y}
    (D : HomDescentData.{u, v} f hX hY) : Prop
```

## Tag 0ADR, a definition

[Tag 0ADR](https://stacks.math.columbia.edu/tag/0ADR) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.familyCanonicalDescentFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/Effective.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/Effective.lean#L98). The attribute's comment: “part (1), canonical descent datum”.

> Pulling the trivial descent datum over `T` back to each member of a family gives the
> canonical descent datum of an algebraic space over `T`.

```lean
public def familyCanonicalDescentFunctor (f : ∀ i, X i ⟶ T)
    (hT : IsAlgebraicSpace B S hS T) (hX : ∀ i, IsAlgebraicSpace B S hS (X i)) :
    AlgebraicSpacesOver (B := B) (S := S) (hS := hS) T ⥤ DescentData f hT hX
```

**`AlgebraicGeometry.Space.Descent.DescentData.IsEffective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/Effective.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/Effective.lean#L108). The attribute's comment: “part (2), effectivity”.

> A descent datum for a family is effective if it is isomorphic to the canonical descent
> datum of an algebraic space over the target.

```lean
public abbrev DescentData.IsEffective {f : ∀ i, X i ⟶ T} {hT : IsAlgebraicSpace B S hS T}
    {hX : ∀ i, IsAlgebraicSpace B S hS (X i)} (D : DescentData f hT hX) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.22, Tag 0ADF](https://stacks.math.columbia.edu/tag/0ADF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
