---
declaration: section
origin: cited
lean: AlgebraicGeometry.DescentDatum, AlgebraicGeometry.DescentDatum.Hom, AlgebraicGeometry.DescentData, AlgebraicGeometry.DescentData.Hom, AlgebraicGeometry.DescentData.familyCoproductEquivalence, AlgebraicGeometry.DescentData.pullbackFunctors, AlgebraicGeometry.DescentData.pullbackFunctor, AlgebraicGeometry.MorphismOfSchemeFamilies.pullbackFunctorIso
statement: formalized
proof: formalized
---

# 35.34 Descent data for schemes over schemes

Section 35.34 of the Stacks Project, [Tag 023U](https://stacks.math.columbia.edu/tag/023U). 11 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 023V, a definition

[Tag 023V](https://stacks.math.columbia.edu/tag/023V) in the Stacks Project.

**`AlgebraicGeometry.DescentDatum`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/SingleMorphism.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/SingleMorphism.lean#L105). The attribute's comment: “(1) descent datum for V/X/S, (2) descent datum relative to X ⟶ S”. References: SGA 3 IV (2.1), “descent datum”.

> Descent data for schemes relative to a single morphism `f : X ⟶ S`: a scheme `V` over
> `X` together with an isomorphism `V ×_S X ≅ X ×_S V` of schemes over `X ×_S X` satisfying the
> cocycle condition. This is the one-member family case of
> `AlgebraicGeometry.DescentData`.

```lean
abbrev DescentDatum (f : X ⟶ S)
```

**`AlgebraicGeometry.DescentDatum.Hom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/SingleMorphism.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/SingleMorphism.lean#L115). The attribute's comment: “(3) morphisms of descent data relative to X ⟶ S”. References: SGA 3 IV (2.1), “partial”.

> A morphism of descent data relative to `f : X ⟶ S`: a morphism of `X`-schemes commuting
> with the two gluing isomorphisms.

```lean
abbrev Hom (D E : DescentDatum f)
```

## Tag 02VP, a remark

[Tag 02VP](https://stacks.math.columbia.edu/tag/02VP) in the Stacks Project.

**`AlgebraicGeometry.DescentData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/DescentData.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/DescentData.lean#L149). The attribute's comment: “remark reading the gluing isomorphism as pr\_0^*V → pr\_1^*V over X ×\_S X”. References: SGA 3 IV (2.1), “descent datum”.

> Descent data for schemes relative to a family of morphisms with common target.

```lean
structure DescentData
```

## Tag 023W, a definition

[Tag 023W](https://stacks.math.columbia.edu/tag/023W) in the Stacks Project.

**`AlgebraicGeometry.DescentData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/DescentData.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/DescentData.lean#L149). The attribute's comment: “(1) descent data”. References: SGA 3 IV (2.1), “descent datum”.

> Descent data for schemes relative to a family of morphisms with common target.

```lean
structure DescentData
```

**`AlgebraicGeometry.DescentData.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/DescentData.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/DescentData.lean#L197). The attribute's comment: “(2) morphisms of descent data”.

> A morphism of descent data is a family of maps over the family members,
> compatible with the gluing isomorphisms.

```lean
structure Hom (D E : DescentData f)
```

## Tag 02VQ, a remark

[Tag 02VQ](https://stacks.math.columbia.edu/tag/02VQ) in the Stacks Project.

**`AlgebraicGeometry.DescentData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/DescentData.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/DescentData.lean#L149). The attribute's comment: “the gluing isomorphisms read over the pairwise fibre product, with the cocycle”. References: SGA 3 IV (2.1), “descent datum”.

> Descent data for schemes relative to a family of morphisms with common target.

```lean
structure DescentData
```

## Tag 023X, a lemma

[Tag 023X](https://stacks.math.columbia.edu/tag/023X) in the Stacks Project.

**`AlgebraicGeometry.DescentData.familyCoproductEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/FamilyCoproduct.lean, line 705](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/FamilyCoproduct.lean#L705).

> Descent data relative to a family `X i ⟶ S` are canonically equivalent to descent data
> relative to the single morphism `(∐ i, X i) ⟶ S`. Under this equivalence both objects and gluing
> maps are formed by coproduct, as specified by `FamilyCoproductEquivalence`.

```lean
noncomputable def familyCoproductEquivalence :
    FamilyCoproductEquivalence f
```

## Tag 023Y, a lemma

[Tag 023Y](https://stacks.math.columbia.edu/tag/023Y) in the Stacks Project.

**`AlgebraicGeometry.DescentData.pullbackFunctors`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/PullbackFunctorIso.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/PullbackFunctorIso.lean#L270).

> The pullback functors on descent data along the morphisms completing a commutative square
> over `h`, together with the canonical isomorphisms between any two of them.

```lean
def pullbackFunctors {S S' X X' : Scheme.{u}} (a : X ⟶ S) (a' : X' ⟶ S') (h : S' ⟶ S) :
    PullbackFunctors a a' h
```

## Tag 02VR, a definition

[Tag 02VR](https://stacks.math.columbia.edu/tag/02VR) in the Stacks Project.

**`AlgebraicGeometry.DescentData.pullbackFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/PullbackSquare.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/PullbackSquare.lean#L107). The attribute's comment: “the pullback functor on descent data”.

> Pullback of descent data along a commutative square of schemes. On underlying schemes this
> is base change along `f`; the gluing isomorphism is pulled back along the induced map of
> self-fibre products.

```lean
noncomputable def pullbackFunctor
    {S S' X X' : Scheme.{u}} (a : X ⟶ S) (a' : X' ⟶ S') (h : S' ⟶ S)
    (f : X' ⟶ X) (comm : f ≫ a = a' ≫ h) :
    PullbackFunctor a a' h f comm
```

## Tag 02VS, a lemma

[Tag 02VS](https://stacks.math.columbia.edu/tag/02VS) in the Stacks Project.

**`AlgebraicGeometry.MorphismOfSchemeFamilies.pullbackFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FamilyPullbackFunctorIso.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FamilyPullbackFunctorIso.lean#L78). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 02VS, part (3).** Two morphisms of families of morphisms with fixed
> target which have the same morphism `h` of base schemes induce canonically isomorphic pullback
> functors on descent data, whatever their index maps and component morphisms are.

```lean
def pullbackFunctorIso :
    (pullbackFunctor (ofHomOver 𝒰 𝒱 h φ)).functor ≅
      (pullbackFunctor (ofHomOver 𝒰 𝒱 h ψ)).functor
```

**`AlgebraicGeometry.MorphismOfSchemeFamilies.pullbackCompatibility`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/PullbackCompatibility.lean, line 723](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germs/PullbackCompatibility.lean#L723). The attribute's comment: “compatibility”.

> Pullback of descent data commutes canonically with the equivalence between
> a family and its coproduct morphism.

```lean
public noncomputable def pullbackCompatibility
    (F : MorphismOfSchemeFamilies.{u}) : PullbackCompatibility F
```

**`AlgebraicGeometry.MorphismOfSchemeFamilies.pullback_descentData_homOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/PullbackFamilyLemma.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/PullbackFamilyLemma.lean#L53). The attribute's comment: “all four parts, for morphisms of families over a fixed base morphism”.

> **Stacks Project, Tag 02VS.** Let `𝒰 = {Uᵢ ⟶ S'}` and `𝒱 = {Vⱼ ⟶ S}` be families of
> morphisms with fixed target and `h : S' ⟶ S`.
>
> 1. For every morphism of families `φ` over `h` and every descent datum `D` relative to `𝒱`, the
>    system `pulledBackDatum` is a descent datum relative to `𝒰` whose component at `i` is
>    `gᵢ^* Y_(α i)` and whose gluing isomorphism at `(i, i')` is the pullback of the gluing
>    isomorphism of `D` at `(α i, α i')` along `gᵢ × gᵢ'`.
> 2. There is, for every such `φ`, a functor from descent data relative to `𝒱` to descent data
>    relative to `𝒰` sending `D` to this pulled-back datum and acting on morphisms by
>    componentwise base change;
> 3. for two morphisms of families `φ, ψ` over the same `h` these functors are isomorphic; and
> 4. after composing with the equivalences of Tag 023X between descent data for a family and
>    descent data for its coproduct morphism, each of them is isomorphic to every pullback functor
>    of Tag 023Y along the induced morphism of coproducts `∐ Uᵢ ⟶ ∐ Vⱼ` over `h`.

```lean
theorem pullback_descentData_homOver {S S' : Scheme.{u}} (𝒰 : PreZeroHypercover.{u} S')
    (𝒱 : PreZeroHypercover.{u} S) (h : S' ⟶ S) :
    (∀ (φ : 𝒰.HomOver 𝒱 h) (D : DescentData 𝒱.f) (i : 𝒰.I₀),
      (pulledBackDatum (ofHomOver 𝒰 𝒱 h φ) D).obj i =
          (Over.pullback (φ.h₀ i)).obj (D.obj (φ.s₀ i)) ∧
        ∀ i' : 𝒰.I₀,
          ((pulledBackDatum (ofHomOver 𝒰 𝒱 h φ) D).gluingPullbackIso i i').hom ≫
              pulledBackDatumTargetMap (ofHomOver 𝒰 𝒱 h φ) D i i' =
            pulledBackDatumSourceMap (ofHomOver 𝒰 𝒱 h φ) D i i' ≫
              (D.gluingPullbackIso (φ.s₀ i) (φ.s₀ i')).hom) ∧
    ∃ G : 𝒰.HomOver 𝒱 h → (DescentData 𝒱.f ⥤ DescentData 𝒰.f),
      (∀ φ : 𝒰.HomOver 𝒱 h,
        ∃ hG : ∀ D : DescentData 𝒱.f, (G φ).obj D = pulledBackDatum (ofHomOver 𝒰 𝒱 h φ) D,
          ∀ (D E : DescentData 𝒱.f) (α : D ⟶ E) (i : 𝒰.I₀),
            (eqToHom (hG D)).hom i ≫
                (pulledBackDatumObjIso (ofHomOver 𝒰 𝒱 h φ) D i).hom ≫
                (Over.pullback (φ.h₀ i)).map (α.hom (φ.s₀ i)) =
              ((G φ).map α).hom i ≫ (eqToHom (hG E)).hom i ≫
                (pulledBackDatumObjIso (ofHomOver 𝒰 𝒱 h φ) E i).hom) ∧
      (∀ φ ψ : 𝒰.HomOver 𝒱 h, Nonempty (G φ ≅ G ψ)) ∧
      ∀ (φ : 𝒰.HomOver 𝒱 h)
        (P : DescentData.PullbackFunctor (Sigma.desc 𝒱.f) (Sigma.desc 𝒰.f) h
          (ofHomOver 𝒰 𝒱 h φ).coproductHom (ofHomOver 𝒰 𝒱 h φ).coproductHom_comp),
        Nonempty ((DescentData.familyCoproductEquivalence 𝒱.f).equivalence.functor ⋙
            P.functor ≅
          G φ ⋙ (DescentData.familyCoproductEquivalence 𝒰.f).equivalence.functor)
```

**`AlgebraicGeometry.MorphismOfSchemeFamilies.pullbackFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/PullbackFunctor.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/PullbackFunctor.lean#L120). The attribute's comment: “pullback\_functor”.

> The pullback of descent data along a morphism of families is functorial.

```lean
public noncomputable def pullbackFunctor (F : MorphismOfSchemeFamilies.{u}) :
    PullbackFunctor F
```

**`AlgebraicGeometry.MorphismOfSchemeFamilies.pulledBackDatum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/PulledBackDatum.lean, line 1061](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/PulledBackDatum.lean#L1061). The attribute's comment: “pulled\_back\_datum”.

> Pull a descent datum back componentwise along a morphism of families.  If the morphism has
> index map `α` and component maps `gᵢ`, its objects are `gᵢ * Y_(α i)` and its gluing
> isomorphisms are the pullbacks of the original gluing isomorphisms along `gᵢ × gᵢ'`.

```lean
noncomputable def pulledBackDatum (F : MorphismOfSchemeFamilies.{u})
    (D : DescentData F.targetFamily.f) :
    DescentData F.sourceFamily.f
```

**`AlgebraicGeometry.MorphismOfSchemeFamilies.pulledBackDatum_obj`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/PulledBackDatum.lean, line 1089](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/PulledBackDatum.lean#L1089). The attribute's comment: “pulled\_back\_datum”.

> The component of the pulled-back datum at `i` is the pullback of the component at
> `F.familyHom.s₀ i`.

```lean
lemma pulledBackDatum_obj (F : MorphismOfSchemeFamilies.{u})
    (D : DescentData F.targetFamily.f) (i : F.sourceFamily.I₀) :
    (pulledBackDatum F D).obj i =
      (Over.pullback (F.familyHom.h₀ i)).obj (D.obj (F.familyHom.s₀ i))
```

**`AlgebraicGeometry.MorphismOfSchemeFamilies.pulledBackDatum_gluing`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/PulledBackDatum.lean, line 1151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/PulledBackDatum.lean#L1151). The attribute's comment: “pulled\_back\_datum”.

> On each pair of indices, the gluing isomorphism of the pulled-back datum is the
> pullback of the original gluing isomorphism along the two component morphisms.

```lean
lemma pulledBackDatum_gluing (F : MorphismOfSchemeFamilies.{u})
    (D : DescentData F.targetFamily.f) (i i' : F.sourceFamily.I₀) :
    ((pulledBackDatum F D).gluingPullbackIso i i').hom ≫
        pulledBackDatumTargetMap F D i i' =
      pulledBackDatumSourceMap F D i i' ≫
        (D.gluingPullbackIso (F.familyHom.s₀ i) (F.familyHom.s₀ i')).hom
```

## Tag 02VT, a definition

[Tag 02VT](https://stacks.math.columbia.edu/tag/02VT) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.MorphismOfSchemeFamilies.pullbackFunctor`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/PullbackFunctor.lean#L120), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/PullbackFunctor.lean, line 758](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Scheme/PullbackFunctor.lean#L758) (StacksFrontier).

## Tag 023Z, a definition

[Tag 023Z](https://stacks.math.columbia.edu/tag/023Z) in the Stacks Project.

**`AlgebraicGeometry.DescentData.trivialFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/EffectiveDescentData.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germs/EffectiveDescentData.lean#L51). The attribute's comment: “part (1)”.

> The functor sending a scheme over `S` to its trivial descent datum relative to the
> singleton family consisting of `𝟙 S`.

```lean
def trivialFunctor (S : Scheme.{u}) :
    Over S ⥤ DescentData (S := S) (X := fun _ : Unit ↦ S) (fun _ ↦ 𝟙 S)
```

**`AlgebraicGeometry.DescentData.canonicalFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/EffectiveDescentData.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germs/EffectiveDescentData.lean#L71). The attribute's comment: “part (2)”.

> The functor sending a scheme over `S` to its canonical descent datum relative to
> `f : X ⟶ S`, obtained by pulling back its trivial descent datum.

```lean
def canonicalFunctor {S X : Scheme.{u}} (f : X ⟶ S) :
    Over S ⥤ DescentData (S := S) (X := fun _ : Unit ↦ X) (fun _ ↦ f)
```

**`AlgebraicGeometry.DescentData.IsEffective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/EffectiveDescentData.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germs/EffectiveDescentData.lean#L80). The attribute's comment: “part (3)”. References: SGA 3 IV (3.5.1).

> A descent datum relative to `f : X ⟶ S` is effective if it is isomorphic to the
> canonical descent datum of a scheme over `S`.

```lean
abbrev IsEffective
    (D : DescentData (S := S) (X := fun _ : Unit ↦ X) (fun _ ↦ f)) : Prop
```

## Tag 02VU, a definition

[Tag 02VU](https://stacks.math.columbia.edu/tag/02VU) in the Stacks Project.

**`AlgebraicGeometry.DescentData.canonicalFamilyFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/CanonicalFamilyDatum.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/CanonicalFamilyDatum.lean#L127). The attribute's comment: “(1) canonical descent datum on the family X i ×\_S U”.

> **The canonical descent datum relative to a family.** The functor sending a scheme `U` over
> `S` to the descent datum relative to `{X i ⟶ S}` whose member over `X i` is the base change of
> `U` along `X i ⟶ S`, obtained by pulling back the trivial descent datum of `U`.

```lean
def canonicalFamilyFunctor (f : ∀ i, X i ⟶ S) : Over S ⥤ DescentData f
```

**`AlgebraicGeometry.DescentData.IsEffectiveFamily`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/CanonicalFamilyDatum.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/CanonicalFamilyDatum.lean#L140). The attribute's comment: “(2) effective descent datum relative to a family”. References: SGA 3 IV (3.5.1).

> **Effectivity of a descent datum relative to a family.** A descent datum relative to
> `{X i ⟶ S}` is effective if it is isomorphic to the canonical descent datum of a scheme over
> `S`.

```lean
abbrev IsEffectiveFamily {f : ∀ i, X i ⟶ S} (D : DescentData f) : Prop
```

**`AlgebraicGeometry.canonicalFamilyDescentFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/CanonicalDatum.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/CanonicalDatum.lean#L256). The attribute's comment: “part (1)”.

> The canonical descent datum functor for an arbitrarily indexed family of schemes over `S`:
> it sends a scheme `U` over `S` to the descent datum whose components are the fibre products of
> `U` with the members of the family, with the gluing isomorphisms that preserve the projection to
> `U`.

```lean
def canonicalFamilyDescentFunctor {I : Type v} {S : Scheme.{u}}
    {X : I → Scheme.{u}} (f : ∀ i, X i ⟶ S) :
    CanonicalDescentFunctor f
```

**`AlgebraicGeometry.DescentData.IsFamilyEffective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/CanonicalDatum.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/CanonicalDatum.lean#L292). The attribute's comment: “part (2)”. References: SGA 3 IV (3.5.1).

> A descent datum relative to a family is effective if it is isomorphic to the canonical
> descent datum of some scheme over the common base.

```lean
abbrev IsFamilyEffective (D : DescentData f) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.34, Tag 023U](https://stacks.math.columbia.edu/tag/023U)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
