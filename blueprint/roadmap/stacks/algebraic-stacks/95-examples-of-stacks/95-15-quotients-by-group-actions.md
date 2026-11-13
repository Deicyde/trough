---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.GroupActionSituation, AlgebraicGeometry.Space.TorsorWithMap.projection_isStackInGroupoids_of_isAlgebraicSpace, AlgebraicGeometry.Space.TorsorWithMap.projection_isStackInGroupoids_unconditional, AlgebraicGeometry.Space.trivialTorsorWithMap, AlgebraicGeometry.Space.quotientStackTorsorEquivalence, AlgebraicGeometry.Space.classifyingQuotientStackEquivalence, AlgebraicGeometry.Space.classifyingStackEquivalences, AlgebraicGeometry.Space.fppfTorsorsEquivPrincipal
statement: formalized
proof: formalized
---

# 95.15 Quotients by group actions

Section 95.15 of the Stacks Project, [Tag 04UV](https://stacks.math.columbia.edu/tag/04UV). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04WL, a situation

[Tag 04WL](https://stacks.math.columbia.edu/tag/04WL) in the Stacks Project.

**`AlgebraicGeometry.Space.GroupActionSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GroupActionSituation.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GroupActionSituation.lean#L48).

> **Stacks Project, Tag 04WL.** The data a quotient by a group action is formed from: a
> scheme `S` of a big fppf site, an algebraic space `B` over `S`, a group algebraic space `G`
> over `B`, an algebraic space `X` over `B`, and an action of `G` on `X` over `B`.

```lean
structure GroupActionSituation
```

## Tag 0370, a lemma

[Tag 0370](https://stacks.math.columbia.edu/tag/0370) in the Stacks Project.

**`AlgebraicGeometry.Space.TorsorWithMap.projection_isStackInGroupoids_of_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorStackUnconditional.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorStackUnconditional.lean#L260). The attribute's comment: “in Situation 04WL: the projection of [[X/G]] is a stack in groupoids for the fppf topology, with hB and G explicit”.

> **Stacks 0370**: in Situation 04WL the projection `p : [[X/G]] ⟶ (Sch/S)_fppf` is a stack
> in groupoids for the fppf topology.
>
> This is `AlgebraicGeometry.Space.TorsorWithMap.projection_isStackInGroupoids_unconditional` with
> `hB` and `G` explicit. The argument `hX` is part of Situation 04WL: `[[X/G]]` is formed for an
> arbitrary object `X` of `Over B`, and the situation asks that it be an algebraic space.

```lean
theorem projection_isStackInGroupoids_of_isAlgebraicSpace (X : Over B) [ModObj G.obj.X X]
    (hX : IsAlgebraicSpace 𝒞 S hS X.left) :
    Functor.IsStackInGroupoids.{w} (projection hB G X) (BigFppfOver.topology 𝒞 S hS)
```

**`AlgebraicGeometry.Space.TorsorWithMap.projection_isStackInGroupoids_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorsWithEquivariantMap.lean, line 997](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorsWithEquivariantMap.lean#L997). The attribute's comment: “in Situation 04WL: the projection of [[X/G]] is a stack in groupoids for the fppf topology”.

> In Situation 04WL the projection `p : [[X/G]] ⟶ (Sch/S)_fppf` is a stack in groupoids for the
> fppf topology.

```lean
theorem projection_isStackInGroupoids_unconditional
    (hX : IsAlgebraicSpace 𝒞 S hS X.left) :
    Functor.IsStackInGroupoids.{w} (projection hB G X) (BigFppfOver.topology 𝒞 S hS)
```

## Tag 04WM, a proposition

[Tag 04WM](https://stacks.math.columbia.edu/tag/04WM) in the Stacks Project.

**`AlgebraicGeometry.Space.trivialTorsorWithMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TrivialTorsorWithMap.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TrivialTorsorWithMap.lean#L281). The attribute's comment: “the trivial torsor with equivariant map attached to a point of X”.

> **Stacks 04WM**, the trivial torsor with its equivariant map.  The object of the category
> `[[X/G]]` of Situation 04WL attached to a point `x : U ⟶ X` of `X`: the trivial torsor
> `G_U = U ×_{b, B} G` over `U`, for `b = x ≫ X.hom`, with its left translation action, together
> with the `G`-equivariant morphism `G_U ⟶ X`, `h ↦ h · x`.

```lean
def trivialTorsorWithMap (U : BigFppfOver 𝒞 S hS) (x : yoneda.obj U ⟶ X.left) :
    TorsorWithMap hB G X
```

**`AlgebraicGeometry.Space.quotientStackTorsorEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackTorsorEquivalence.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackTorsorEquivalence.lean#L187). The attribute's comment: “the canonical equivalence [X/G] ≌ [[X/G]] over the big fppf site, whose forward functor extends the explicit pointwise comparison F\_p”.

> The quotient stack `[X/G]` of the action of a group algebraic space `G` over
> an algebraic space `B` on an algebraic space `X` over `B` is canonically equivalent, over the big
> fppf site of `S`, to the stack `[[X/G]]` of fppf `G`-torsors with a `G`-equivariant map to `X`;
> and the forward 1-morphism of the equivalence extends the explicit pointwise comparison `F_p` of
> `AlgebraicGeometry.Space.actionPointwiseComparison`, the identification being a natural
> isomorphism all of whose components lie over identities of the site.
>
> The source is the quotient stack of the action groupoid `(X, G ×_B X, pr₁, a, m)` of Stacks 0444,
> that is `AlgebraicGeometry.Stack.quotientStackOfAction` of Stacks 044Q part (2).

```lean
def quotientStackTorsorEquivalence :
    {e : StacksRepresentableCFG.EquivalenceOver
        (Stack.quotientStackOfAction ⟨B, hB⟩ G.obj.X X G.property hX).p
        (TorsorWithMap.projection hB G X) //
      ∃ α : Stack.pointwiseToQuotientStack
            (groupoidOfAction ⟨B, hB⟩ G.obj.X X G.property hX).groupoid ⋙ e.hom.functor ≅
          actionPointwiseComparison hB G X hX,
        ∀ A : (actionPointwiseCategory hB G X hX).obj,
          (TorsorWithMap.projection hB G X).IsHomLift (𝟙 A.base) (α.hom.app A)}
```

## Tag 0CQJ, a lemma

[Tag 0CQJ](https://stacks.math.columbia.edu/tag/0CQJ) in the Stacks Project.

**`AlgebraicGeometry.Space.classifyingQuotientStackEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ClassifyingStackEquivalences.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ClassifyingStackEquivalences.lean#L81). The attribute's comment: “the leg [B/G] ≌ [[B/G]] over the big fppf site, Stacks 04WM at X = B”.

> **Stacks 0CQJ**, the leg `[B/G] ≌ [[B/G]]`.  The quotient stack `[B/G]` of the trivial
> action of `G` on `B` (Stacks 044Q part (2), the quotient stack of the action groupoid of
> Stacks 0444) is equivalent over the big fppf site of `S` to `[[B/G]]`, the stack of fppf
> `G`-torsors with an equivariant morphism to `B`.  This is Stacks 04WM at `X = B`.

```lean
def classifyingQuotientStackEquivalence :
    StacksRepresentableCFG.EquivalenceOver
      (Stack.quotientStackOfAction ⟨B, hB⟩ G.obj.X (𝟙_ (Over B)) G.property hB).p
      (TorsorWithMap.projection hB G (𝟙_ (Over B)))
```

**`AlgebraicGeometry.Space.classifyingStackEquivalences`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ClassifyingStackEquivalences.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ClassifyingStackEquivalences.lean#L152). The attribute's comment: “the whole lemma: [B/G] ≌ [[B/G]] ≌ G-Torsors ≌ 𝒢/ℬ-Torsors over the big fppf site, and G-Torsors ≌ G-Principal for G ⟶ B flat and locally of finite presentation, each with its canonical forward functor”.

> **Stacks 0CQJ.** Let `S` be a scheme, `B` an algebraic space over `S` and `G` a group
> algebraic space over `B`.  Then the stacks in groupoids over `(Sch/S)_fppf`
> `[B/G]`, `[[B/G]]`, `G-Torsors` and `𝒢/ℬ-Torsors` are all canonically equivalent: this gives
> equivalences over the site
> `[B/G] ≌ [[B/G]]`, `[[B/G]] ≌ G-Torsors` and `G-Torsors ≌ 𝒢/ℬ-Torsors`, and, if `G ⟶ B` is flat
> and locally of finite presentation, `G-Torsors ≌ G-Principal`.
>
> Each is the canonical one:
> * the forward functor of `[B/G] ≌ [[B/G]]` extends the pointwise comparison `F_p`
>   (`AlgebraicGeometry.Space.actionPointwiseComparison`) sending a point `b : U ⟶ B` to the
>   trivial torsor, by a natural isomorphism lying over identities (Stacks 04WM at `X = B`);
> * the forward functor of `[[B/G]] ≌ G-Torsors` forgets the equivariant map to `B`;
> * the forward functor of `G-Torsors ≌ 𝒢/ℬ-Torsors` is the comparison functor of Stacks 04UT;
> * the forward functor of `G-Torsors ≌ G-Principal` is the canonical inclusion
>   `AlgebraicGeometry.Space.FppfTorsors.toPrincipal`.

```lean
def classifyingStackEquivalences :
    { c : StacksRepresentableCFG.EquivalenceOver
          (Stack.quotientStackOfAction ⟨B, hB⟩ G.obj.X (𝟙_ (Over B)) G.property hB).p
          (TorsorWithMap.projection hB G (𝟙_ (Over B))) ×
        StacksRepresentableCFG.EquivalenceOver (TorsorWithMap.projection hB G (𝟙_ (Over B)))
          (FppfTorsors.projection hB G) ×
        StacksRepresentableCFG.EquivalenceOver (FppfTorsors.projection hB G)
          (SheafTorsors.projection G.obj) ×
        (IsFlat 𝒞 S hS G.obj.X.hom → IsLocallyOfFinitePresentation 𝒞 S hS G.obj.X.hom →
          StacksRepresentableCFG.EquivalenceOver (FppfTorsors.projection hB G)
            (PrincipalHomogeneousSpaces.projection hB G)) //
      (∃ α : Stack.pointwiseToQuotientStack
            (groupoidOfAction ⟨B, hB⟩ G.obj.X (𝟙_ (Over B)) G.property hB).groupoid ⋙
              c.1.hom.functor ≅
            actionPointwiseComparison hB G (𝟙_ (Over B)) hB,
          ∀ A : (actionPointwiseCategory hB G (𝟙_ (Over B)) hB).obj,
            (TorsorWithMap.projection hB G (𝟙_ (Over B))).IsHomLift (𝟙 A.base) (α.hom.app A)) ∧
        c.2.1.hom.functor =
          TorsorWithMap.forget hB G (𝟙_ (Over B)) ⋙ torsorObjComparisonInverse hB G ∧
        c.2.2.1.hom.functor = FppfTorsors.comparison hB G ∧
        ∀ hflat hlfp, (c.2.2.2 hflat hlfp).hom.functor = FppfTorsors.toPrincipal hB G }
```

**`AlgebraicGeometry.Space.fppfTorsorsEquivPrincipal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/FppfTorsorsPrincipalComparison.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/FppfTorsorsPrincipalComparison.lean#L102). The attribute's comment: “G-Torsors ≌ G-Principal, for G ⟶ B flat and locally of finite presentation”.

> **Stacks 0CQJ.** For `G ⟶ B` flat and locally of finite presentation the canonical functor
> `G-Torsors ⥤ G-Principal` is an equivalence of categories, with quasi-inverse the functor
> reading a principal homogeneous space as an fppf torsor and with identity unit and counit.

```lean
def fppfTorsorsEquivPrincipal (hB : IsAlgebraicSpace 𝒞 S hS B)
    (G : GroupAlgebraicSpace 𝒞 S hS B hB) (hflat : IsFlat 𝒞 S hS G.obj.X.hom)
    (hlfp : IsLocallyOfFinitePresentation 𝒞 S hS G.obj.X.hom) :
    FppfTorsors hB G ≌ PrincipalHomogeneousSpaces hB G
```

**`AlgebraicGeometry.Space.FppfTorsors.nonempty_isEquivalenceOver_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonUnconditional.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonUnconditional.lean#L67). The attribute's comment: “the 𝒢/ℬ-Torsors leg: G-Torsors ≌ 𝒢/ℬ-Torsors over the big fppf site”.

> **Stacks 04UT**, with nothing carried, and with it the `𝒢/ℬ-Torsors` leg of **Stacks
> 0CQJ**: the comparison functor `G-Torsors ⥤ 𝒢/ℬ-Torsors` is an equivalence of stacks in
> groupoids over the big fppf site of `S`.
>
> The hypothesis every earlier rendering carried is the object half of Stacks 04U1, equivalently
> Stacks 04S6 part (3), which is now the theorem
> `AlgebraicGeometry.Space.isBootstrapAlgebraicSpaceAlongFlatSurjection`.

```lean
theorem nonempty_isEquivalenceOver_comparison (hB : IsAlgebraicSpace 𝒞 S hS B)
    (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    Nonempty (Functor.IsEquivalenceOver (projection hB G) (SheafTorsors.projection G.obj)
      (comparison hB G))
```

**`AlgebraicGeometry.Space.torsorObjToTorsorWithMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorsWithEquivariantMap.lean, line 1108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorsWithEquivariantMap.lean#L1108). The attribute's comment: “the functor G-Torsors ⥤ [[B/G]]”.

> The canonical functor `G-Torsors ⥤ [[B/G]]`, attaching to an fppf `G`-torsor its unique
> equivariant morphism to the base and to a morphism of torsors the same morphism.

```lean
def torsorObjToTorsorWithMap : TorsorObj hB G ⥤ TorsorWithMap hB G (𝟙_ (Over B))
```

**`AlgebraicGeometry.Space.torsorWithMapEquivTorsorObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorsWithEquivariantMap.lean, line 1140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorsWithEquivariantMap.lean#L1140). The attribute's comment: “[[B/G]] ≌ G-Torsors”.

> The category `[[B/G]]` of fppf `G`-torsors with an equivariant morphism to the base, that is
> the quotient category of the trivial action of `G` on `B`, is canonically equivalent to the
> category `G-Torsors` of fppf `G`-torsors; the equivalence forgets the equivariant morphism.

```lean
def torsorWithMapEquivTorsorObj : TorsorWithMap hB G (𝟙_ (Over B)) ≌ TorsorObj hB G
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.FppfTorsors.toPrincipal`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorsToPrincipal.lean#L315), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/FppfTorsorsPrincipalComparison.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/FppfTorsorsPrincipalComparison.lean#L70) (StacksFrontier): “the functor G-Torsors ⥤ G-Principal”.
- [`AlgebraicGeometry.Space.FppfTorsors.comparison`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparison.lean#L167), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonFibred.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonFibred.lean#L60) (StacksFrontier): “the canonical functor G-Torsors ⥤ 𝒢/ℬ-Torsors”.

## Tag 0371, a remark

[Tag 0371](https://stacks.math.columbia.edu/tag/0371) in the Stacks Project.

**`AlgebraicGeometry.AbstractGroupQuotientStack`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStack.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStack.lean#L104). The attribute's comment: “the objects of [[X/G]]”.

> **Stacks 0371.** An object of the quotient `[[X/G]]` of a sheaf `X` by an abstract group
> `G`: an object `U` of `(Sch/S)_fppf`, a torsor on `(Sch/U)_fppf` under the constant sheaf of
> groups with value `G`, and a `G`-equivariant map of sheaves from it to `X`.

```lean
structure AbstractGroupQuotientStack
```

**`AlgebraicGeometry.AbstractGroupQuotientStack.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStack.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStack.lean#L162). The attribute's comment: “the morphisms of [[X/G]]”.

> **Stacks 0371.** A morphism `(U, P, φ) ⟶ (U', P', φ')` of the quotient `[[X/G]]`: a
> morphism `f : U ⟶ U'` of `(Sch/S)_fppf` together with a `G`-equivariant isomorphism
> `g : P → f^{-1}P'` of torsors under the constant sheaf of groups with value `G`, compatible
> with `φ` and `φ'`. The isomorphism is recorded on total spaces: `g` is a map of sheaves on
> `(Sch/S)_fppf` over `f` restricting to a bijection from the fibre of `P` over each
> `a : V ⟶ U` to the fibre of `P'` over `a ≫ f`.

```lean
structure Hom (A A' : AbstractGroupQuotientStack B S hS G X ρ)
```

**`AlgebraicGeometry.AbstractGroupQuotientStack.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStack.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStack.lean#L226). The attribute's comment: “the category [[X/G]]”.

> **Stacks 0371.** The quotient `[[X/G]]` of a sheaf `X` by an abstract group `G` is a
> category: morphisms compose by composing `f` and `g`.

```lean
instance instCategory : Category (AbstractGroupQuotientStack B S hS G X ρ)
```

**`AlgebraicGeometry.AbstractGroupQuotientStack.projection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStack.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStack.lean#L237). The attribute's comment: “the functor to the big fppf site”.

> **Stacks 0371.** The functor `[[X/G]] ⥤ (Sch/S)_fppf` sending a triple `(U, P, φ)` to
> `U`, which is how `[[X/G]]` is regarded as a category over the big fppf site of `S`.

```lean
def projection :
    AbstractGroupQuotientStack B S hS G X ρ ⥤ BigFppfOver B S hS
```

**`AlgebraicGeometry.nonempty_isEquivalenceOver_abstractGroupQuotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackEquivalence.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackEquivalence.lean#L478). The attribute's comment: “the equivalence of [[X/G]] with [[X/G\_S]]”.

> Let `G` be an abstract group whose constant group scheme `G_S` lies in the big fppf site,
> `X` an algebraic space over `S` and `ρ : G →* Aut X` an action. Then the stack `[[X/G]]` of
> triples `(U, P, φ)`, `P` a torsor under the constant sheaf `G` on `(Sch/U)_fppf` and
> `φ : P → X` equivariant, is equivalent over `(Sch/S)_fppf` to the stack `[[X/G_S]]`, for `G_S`
> the constant group algebraic space `AlgebraicGeometry.Space.constantGroupSpace` acting on `X`
> through `ρ` (`AlgebraicGeometry.Space.constGSModObj`, whose constant sections act as `ρ` does by
> `AlgebraicGeometry.Space.constGS_isCompatibleAction`).

```lean
theorem nonempty_isEquivalenceOver_abstractGroupQuotientStack :
    letI : ModObj (constantGroupSpace 𝒞 S hS G (baseS 𝒞 S hS) (isAlgebraicSpace_baseS 𝒞 S hS)
        hG).obj.X (overBaseS X₀) := constGSModObj hG hX.isSheaf ρ₀
    ∃ F : TorsorWithMap (isAlgebraicSpace_baseS 𝒞 S hS)
        (constantGroupSpace 𝒞 S hS G (baseS 𝒞 S hS) (isAlgebraicSpace_baseS 𝒞 S hS) hG)
        (overBaseS X₀) ⥤
      AbstractGroupQuotientStack.{max t (u + 1)} 𝒞 S hS G (X₀ ⋙ uliftFunctor.{max t (u + 1)})
        (uliftAction.{max t (u + 1)} ρ₀),
      Nonempty (Functor.IsEquivalenceOver
        (TorsorWithMap.projection (isAlgebraicSpace_baseS 𝒞 S hS)
          (constantGroupSpace 𝒞 S hS G (baseS 𝒞 S hS) (isAlgebraicSpace_baseS 𝒞 S hS) hG)
          (overBaseS X₀))
        AbstractGroupQuotientStack.projection F)
```

**`AlgebraicGeometry.AbstractGroupQuotientStack.projection_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackIsStack.lean, line 772](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackIsStack.lean#L772). The attribute's comment: “[[X/G]] is a stack in groupoids over (Sch/S)\_fppf”.

> **Stacks 0371.** For an algebraic space `X` over `S` with an action `ρ : G →* Aut X` of an
> abstract group `G`, the functor `[[X/G]] ⥤ (Sch/S)_fppf` of
> `AlgebraicGeometry.AbstractGroupQuotientStack.projection` turns `[[X/G]]` into a stack in
> groupoids over the big fppf site of `S`.
>
> This is the assertion of the remark, under exactly its standing hypothesis that `X` is an
> algebraic space over `S`: nothing beyond the sheaf condition for `X` is used, and the three
> conditions of Stacks 02ZI are proved outright, with the stack property of the torsors under
> the constant sheaf of groups supplied by Stacks 04UK rather than assumed.

```lean
theorem projection_isStackInGroupoids
    (hX : Space.IsAlgebraicSpaceULift.{max t (u + 1)} B S hS X) :
    Functor.IsStackInGroupoids.{w}
      (projection : AbstractGroupQuotientStack.{max t (u + 1)} B S hS G X ρ ⥤
        BigFppfOver B S hS) (BigFppfOver.topology B S hS)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.constantGroupSheafRepresentedByConstantGroupScheme_bigFppf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean#L207), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackIsStack.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackIsStack.lean#L88) (StacksFrontier): “the constant sheaf G is representable by G\_S on (Sch/S)\_fppf”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 95.15, Tag 04UV](https://stacks.math.columbia.edu/tag/04UV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
