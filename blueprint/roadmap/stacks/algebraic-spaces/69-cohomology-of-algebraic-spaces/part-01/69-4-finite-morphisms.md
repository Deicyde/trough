---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.smallEtaleAbelianPushforward_exact_of_isFinite, AlgebraicGeometry.Space.smallEtaleAbelianPushforward_rightDerivedPlus_isZero_of_isFinite, AlgebraicGeometry.Space.smallEtaleAbelianPushforward_exact_of_isIntegralHom, AlgebraicGeometry.Space.smallEtaleAbelianPushforward_rightDerivedPlus_isZero_of_isIntegralHom, AlgebraicGeometry.Space.finite_geometricLifts, AlgebraicGeometry.Space.stalkPushforwardToProduct, AlgebraicGeometry.Space.stalkPushforwardToProduct_natural, AlgebraicGeometry.Space.geometricLiftsEquivOfIsPullback
statement: formalized
proof: formalized
---

# 69.4 Finite morphisms

Section 69.4 of the Stacks Project, [Tag 0DK2](https://stacks.math.columbia.edu/tag/0DK2). 4 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A4K, a lemma

[Tag 0A4K](https://stacks.math.columbia.edu/tag/0A4K) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtaleAbelianPushforward_exact_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePushforwardExact.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FinitePushforwardExact.lean#L136). The attribute's comment: “exactness of f\_*, the finite case”.

> **Stacks 0A4K, exactness, for a finite morphism.** For a finite morphism `f : X ⟶ Y` of
> algebraic spaces over `S` the direct image on the abelian sheaves of the small étale sites is
> exact.
>
> The source states this for an integral morphism, "integral (for example finite)"; that case is
> `AlgebraicGeometry.Space.smallEtaleAbelianPushforward_exact_of_isIntegralHom`.  The step from
> surjections of sheaves of sets to exactness on abelian sheaves is Stacks 04DB, already
> available as `Stacks.Topos.AbelianPushforward.abelianPushforward_exact`, and the surjection
> statement is
> `AlgebraicGeometry.Space.smallEtalePushforward_preservesEpimorphisms_of_isFinite`.

```lean
theorem smallEtaleAbelianPushforward_exact_of_isFinite {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsFinite B S hS f.hom) :
    exactFunctor (Sheaf (SmallEtale.topology B S hS X.obj) AddCommGrpCat.{u + 1})
      (Sheaf (SmallEtale.topology B S hS Y.obj) AddCommGrpCat.{u + 1})
      (Stacks.Topos.AbelianPushforward.abelianPushforward (SmallEtale.topology B S hS X.obj)
        (smallToposMorphism B S hS f))
```

**`AlgebraicGeometry.Space.smallEtaleAbelianPushforward_rightDerivedPlus_isZero_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePushforwardExact.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FinitePushforwardExact.lean#L154). The attribute's comment: “vanishing of R^p f\_* for p > 0, the finite case”. References: SGA 4 Vbis (4.3.4), “Remarque 4.3.4”; SGA 4½ Arcata (2.3.6), “more general”.

> **Stacks 0A4K, vanishing of the positive-degree higher direct images, for a finite
> morphism.** For a finite morphism `f : X ⟶ Y` of algebraic spaces over `S` the right derived
> functors of the small étale direct image on abelian sheaves vanish in positive degree.
>
> The integral case, which contains this one, is
> `AlgebraicGeometry.Space.smallEtaleAbelianPushforward_rightDerivedPlus_isZero_of_isIntegralHom`.

```lean
theorem smallEtaleAbelianPushforward_rightDerivedPlus_isZero_of_isFinite
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsFinite B S hS f.hom)
    (F : Sheaf (SmallEtale.topology B S hS X.obj) AddCommGrpCat.{u + 1})
    (p : ℤ) (hp : 0 < p) :
    IsZero (((Stacks.Topos.AbelianPushforward.abelianPushforward
      (SmallEtale.topology B S hS X.obj)
      (smallToposMorphism B S hS f)).rightDerivedPlus p).obj F)
```

**`AlgebraicGeometry.Space.smallEtaleAbelianPushforward_exact_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralPushforwardExact.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralPushforwardExact.lean#L112). The attribute's comment: “exactness of f\_* for an integral morphism of algebraic spaces”.

> **Stacks 0A4K, exactness.** For an integral morphism `f : X ⟶ Y` of algebraic spaces over
> `S` the direct image on the abelian sheaves of the small étale sites is exact.
>
> The step from surjections of sheaves of sets to exactness on abelian sheaves is Stacks 04DB,
> available as `Stacks.Topos.AbelianPushforward.abelianPushforward_exact`, and the surjection
> statement is
> `AlgebraicGeometry.Space.smallEtalePushforward_preservesEpimorphisms_of_isIntegralHom`.

```lean
theorem smallEtaleAbelianPushforward_exact_of_isIntegralHom {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsIntegralHom B S hS f.hom) :
    exactFunctor (Sheaf (SmallEtale.topology B S hS X.obj) AddCommGrpCat.{u + 1})
      (Sheaf (SmallEtale.topology B S hS Y.obj) AddCommGrpCat.{u + 1})
      (Stacks.Topos.AbelianPushforward.abelianPushforward (SmallEtale.topology B S hS X.obj)
        (smallToposMorphism B S hS f))
```

**`AlgebraicGeometry.Space.smallEtaleAbelianPushforward_rightDerivedPlus_isZero_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralPushforwardExact.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralPushforwardExact.lean#L131). The attribute's comment: “vanishing of R^p f\_* for p > 0 for an integral morphism of algebraic spaces”. References: SGA 4 VIII (5.6), “more general”; SGA 4 Vbis (4.3.4), “more general”; SGA 4½ Arcata (2.3.6), “more general”.

> **Stacks 0A4K, vanishing of the positive-degree higher direct images.** For an integral
> morphism `f : X ⟶ Y` of algebraic spaces over `S` the right derived functors of the small étale
> direct image on abelian sheaves vanish in positive degree.
>
> Given the exactness this is formal, by
> `CategoryTheory.Functor.isZero_rightDerivedPlus_of_exact`.

```lean
theorem smallEtaleAbelianPushforward_rightDerivedPlus_isZero_of_isIntegralHom
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsIntegralHom B S hS f.hom)
    (F : Sheaf (SmallEtale.topology B S hS X.obj) AddCommGrpCat.{u + 1})
    (p : ℤ) (hp : 0 < p) :
    IsZero (((Stacks.Topos.AbelianPushforward.abelianPushforward
      (SmallEtale.topology B S hS X.obj)
      (smallToposMorphism B S hS f)).rightDerivedPlus p).obj F)
```

## Tag 0DK3, a lemma

[Tag 0DK3](https://stacks.math.columbia.edu/tag/0DK3) in the Stacks Project.

**`AlgebraicGeometry.Space.finite_geometricLifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteStalkPushforward.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteStalkPushforward.lean#L180). The attribute's comment: “the lifts `x₁, …, xₙ` of `y` are finite in number”.

> **Stacks 0DK3, finiteness of the index set.** A geometric point of the target of a finite
> morphism of algebraic spaces has finitely many lifts, so the product in the statement is a
> finite one.
>
> The field spectrum of `y` is affine, so testing `π` against the section `y` produces an affine
> scheme `V`, a finite morphism `V ⟶ Spec κ(y)` and a pullback square exhibiting `V` as the base
> change of `X`. A lift of `y` therefore determines a section of that finite morphism, and
> `AlgebraicGeometry.finite_lifts_of_isFinite` makes those finite in number; the assignment is
> injective because the Yoneda embedding and the functor to schemes are faithful.

```lean
theorem finite_geometricLifts (hπ : IsFinite B S hS π.hom)
    (y : GeometricPoint B S hS Y.1) :
    Finite (GeometricLifts B S hS π y)
```

**`AlgebraicGeometry.Space.stalkPushforwardToProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteStalkPushforward.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteStalkPushforward.lean#L301). The attribute's comment: “the canonical map `(π_*F)_y ⟶ ∏ᵢ F_{xᵢ}` over the lifts of `y`”.

> **The comparison map of Stacks 0DK3.** For a finite morphism `π : X ⟶ Y` of algebraic
> spaces and a geometric point `y` of `Y`, the stalk at `y` of the direct image of a sheaf of
> sets `F` on `X_étale` maps canonically to the product of the stalks of `F` over the lifts of
> `y`, the component at a lift being
> `AlgebraicGeometry.Space.stalkPushforwardComponent`.
>
> Stacks 0DK3 asserts that this map is bijective. That assertion is not proved for this map; it
> is proved for the comparison map `CategoryTheory.GrothendieckTopology.Point.presheafFiberCompToPi`
> as `AlgebraicGeometry.Space.bijective_presheafFiberCompToPi_of_isFinite`. What is proved about
> this map is its construction and its naturality in the sheaf.

```lean
def stalkPushforwardToProduct (y : GeometricPoint B S hS Y.1)
    (F : Sheaf (SmallEtale.topology B S hS X.1) (Type (u + 1))) :
    stalkSet y ((smallToposMorphism B S hS π).pushforward.obj F).obj →
      (∀ v : GeometricLifts B S hS π y,
        stalkSet (geometricLiftPoint B S hS π y v) F.obj)
```

**`AlgebraicGeometry.Space.stalkPushforwardToProduct_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteStalkPushforward.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteStalkPushforward.lean#L323). The attribute's comment: “naturality of the comparison map in the sheaf”.

> **Stacks 0DK3 is natural in the sheaf.** The comparison map commutes with the stalk maps
> induced by a morphism of sheaves of sets on `X_étale`.

```lean
theorem stalkPushforwardToProduct_natural (y : GeometricPoint B S hS Y.1)
    {F G : Sheaf (SmallEtale.topology B S hS X.1) (Type (u + 1))} (α : F ⟶ G)
    (z : stalkSet y ((smallToposMorphism B S hS π).pushforward.obj F).obj)
    (v : GeometricLifts B S hS π y) :
    stalkPushforwardToProduct B S hS π y G
        (stalkSetMap y ((smallToposMorphism B S hS π).pushforward.map α).hom z) v =
      stalkSetMap (geometricLiftPoint B S hS π y v) α.hom
        (stalkPushforwardToProduct B S hS π y F z v)
```

**`AlgebraicGeometry.Space.geometricLiftsEquivOfIsPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteStalkPushforward.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteStalkPushforward.lean#L415). The attribute's comment: “the lifts of `y` are the lifts of `v` along the base change of `π`”.

> **Stacks 0DK3: the index set of the product is unchanged by base change.** For a
> cartesian square
>
> ```
> X' --i--> X
> |         |
> f'        π
> ↓         ↓
> V --g---> Y
> ```
>
> of algebraic spaces over `S` and a geometric point `v` of `V`, the lifts of `v` along `f'`
> are the lifts along `π` of the image of `v` in `Y`, the bijection sending a lift to its image
> under `i`.
>
> This is the step with which the source's proof of Stacks 0DK3 begins, specialized to the
> index set: it replaces `Y` by an étale neighbourhood `(V, v)` of `y` and `X` by `X ×_Y V`, and
> the product over the lifts is the same product before and after exactly because of this
> bijection. Nothing is assumed of the four arrows beyond the square being cartesian, so neither
> finiteness of `π` nor étaleness of `g` is needed; the lifts of a geometric point are sections
> over its field spectrum, and sections over one object of the site of a cartesian square of
> algebraic spaces form a cartesian square of sets.

```lean
noncomputable def geometricLiftsEquivOfIsPullback {X' V : AlgebraicSpaces B S hS}
    {i : X' ⟶ X} {f' : X' ⟶ V} {g : V ⟶ Y} (sq : IsPullback i f' π g)
    (v : GeometricPoint B S hS V.1) :
    GeometricLifts B S hS f' v ≃ GeometricLifts B S hS π (geometricPointMap g.hom v)
```

**`AlgebraicGeometry.Space.bijective_presheafFiberCompToPi_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteStalkPushforwardProduct.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteStalkPushforwardProduct.lean#L356).

> **Stacks 0DK3.** Let `π : X ⟶ Y` be a finite morphism of algebraic spaces and `y` a geometric
> point of `Y` with lifts `x₁, …, xₙ` in `X`. For every sheaf of sets `F` on `X_étale` the stalk of
> the direct image `π_*F` at `y` is the product `∏ᵢ F_{xᵢ}`: the canonical map
> `CategoryTheory.GrothendieckTopology.Point.presheafFiberCompToPi`, sending the germ at `y` of a
> section of `F` over a base-changed chart `V ×_Y X` to the family of its germs at the lifts, is
> bijective.
>
> The direct image is that along base change of étale charts (`π` is representable, being finite,
> `AlgebraicGeometry.Space.relativelyRepresentable_hom_of_isFinite`),
> which is the direct image of the morphism of small étale topoi of Stacks 03G2, part (3)
> (`AlgebraicGeometry.Space.smallEtaleRingedToposHom_representable`); sheaves are valued in an
> arbitrary universe containing `Type u`, the universe of the fibres of the points
> `AlgebraicGeometry.Space.etaleSitePoint` at which stalks are taken.

```lean
theorem bijective_presheafFiberCompToPi_of_isFinite (hπ : IsFinite B S hS π.hom)
    (y : GeometricPoint B S hS Y.1)
    (F : Sheaf (SmallEtale.topology B S hS X.1) (Type (max u w))) :
    Function.Bijective (GrothendieckTopology.Point.presheafFiberCompToPi.{u, w, u, u + 1, u, u + 1}
      (smallBaseChange B S hS π (relativelyRepresentable_hom_of_isFinite B S hS π hπ))
      (etaleSitePoint B S hS Y.1 y Y.2)
      (fun v => etaleSitePoint B S hS X.1 (geometricLiftPoint B S hS π y v) X.2)
      (geometricFiberBaseChangeIso B S hS π (relativelyRepresentable_hom_of_isFinite B S hS π hπ) y)
      F.obj)
```

## Tag 0DK4, a lemma

[Tag 0DK4](https://stacks.math.columbia.edu/tag/0DK4) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtaleRingedToposHomOfSharp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModuleTensorPushforward.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModuleTensorPushforward.lean#L182). The attribute's comment: “the morphism of ringed topoi determined by `π`, `𝒜`, `ℬ` and `φ`”.

> **The morphism of ringed topoi of Stacks 04G0**, `f : (Sh(Z_étale), ℬ) ⟶ (Sh(X_étale), 𝒜)`:
> its underlying morphism of topoi is that of Stacks 03G2, part (3), and its structure map is `φ`.
>
> No hypothesis on `i` enters, so this is equally the morphism of ringed topoi of Stacks 0DK4,
> whose datum is the same `(i, φ)` in the same direction, with `i` finite instead of a closed
> immersion.

```lean
noncomputable def smallEtaleRingedToposHomOfSharp (i : Z ⟶ X)
    {𝒜 : Sheaf (SmallEtale.topology B S hS X.1) CommRingCat.{u}}
    {ℬ : Sheaf (SmallEtale.topology B S hS Z.1) CommRingCat.{u}}
    (φ : 𝒜 ⟶ (pushforwardCommRingFunctor.{u, u, u, u + 1, u, u + 1}
      (smallToposMorphismTypeU B S hS i)).obj ℬ) :
    Stacks.Sheaves.RingedToposModules.RingedToposHom
      (smallEtaleRingedToposOfRings B S hS Z ℬ) (smallEtaleRingedToposOfRings B S hS X 𝒜)
```

**`AlgebraicGeometry.Space.tensorPushforwardMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModuleTensorPushforward.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModuleTensorPushforward.lean#L202). The attribute's comment: “the canonical map `𝓖 ⊗_ℬ f_*𝓕 ⟶ f_*(f^*𝓖 ⊗_𝒜 𝓕)`”.

> **The canonical map of Stacks 04G0**, `𝓕 ⊗_𝒜 f_*𝓖 ⟶ f_*(f^*𝓕 ⊗_ℬ 𝓖)`: the adjoint
> transpose of `f^*(𝓕 ⊗_𝒜 f_*𝓖) = f^*𝓕 ⊗_ℬ f^*f_*𝓖 ⟶ f^*𝓕 ⊗_ℬ 𝓖`, built from the identity of
> `f^*𝓕` and the adjunction map `f^*f_*𝓖 ⟶ 𝓖`.
>
> No hypothesis on `i` enters, so this is equally the canonical map of Stacks 0DK4, which is the
> adjoint transpose of the same comparison for the same datum with `i` finite.

```lean
noncomputable def tensorPushforwardMap (i : Z ⟶ X)
    {𝒜 : Sheaf (SmallEtale.topology B S hS X.1) CommRingCat.{u}}
    {ℬ : Sheaf (SmallEtale.topology B S hS Z.1) CommRingCat.{u}}
    (φ : 𝒜 ⟶ (pushforwardCommRingFunctor.{u, u, u, u + 1, u, u + 1}
      (smallToposMorphismTypeU B S hS i)).obj ℬ)
    (𝓕 : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallEtaleRingedToposOfRings B S hS X 𝒜).O))
    (𝓖 : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallEtaleRingedToposOfRings B S hS Z ℬ).O)) :
    ((Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u} 𝒜).obj 𝓕).obj
      ((pushforwardModules (smallEtaleRingedToposHomOfSharp B S hS i φ)).obj 𝓖) ⟶
      (pushforwardModules (smallEtaleRingedToposHomOfSharp B S hS i φ)).obj
        (((Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u} ℬ).obj
          (((smallEtaleRingedToposHomOfSharp B S hS i φ).pullbackModules).obj 𝓕)).obj 𝓖)
```

**`AlgebraicGeometry.Space.isIso_tensorPushforwardMap_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTensorPushforwardIso.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTensorPushforwardIso.lean#L108).

> **Stacks 0DK4.** Let `π : X ⟶ Y` be a finite morphism of algebraic spaces over `S`, `𝒜` a
> sheaf of rings on `X_étale`, `ℬ` a sheaf of rings on `Y_étale` and `φ : ℬ ⟶ π_*𝒜` a
> homomorphism of sheaves of rings, with associated morphism of ringed topoi
> `f = (π, φ) : (Sh(X_étale), 𝒜) ⟶ (Sh(Y_étale), ℬ)`. For every sheaf of `𝒜`-modules `𝓕` and every
> sheaf of `ℬ`-modules `𝓖` the canonical map `𝓖 ⊗_ℬ f_*𝓕 ⟶ f_*(f^*𝓖 ⊗_𝒜 𝓕)` is an
> isomorphism.

```lean
theorem isIso_tensorPushforwardMap_of_isFinite (π : X ⟶ Y) (hπ : IsFinite B S hS π.hom)
    {𝒜 : Sheaf (SmallEtale.topology B S hS X.1) CommRingCat.{u}}
    {ℬ : Sheaf (SmallEtale.topology B S hS Y.1) CommRingCat.{u}}
    (φ : ℬ ⟶ (pushforwardCommRingFunctor.{u, u, u, u + 1, u, u + 1}
      (smallToposMorphismTypeU B S hS π)).obj 𝒜)
    (𝓕 : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedToposOfRings B S hS X 𝒜).O))
    (𝓖 : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedToposOfRings B S hS Y ℬ).O)) :
    IsIso (tensorPushforwardMap B S hS π φ 𝓖 𝓕)
```

## Tag 0DK5, a lemma

[Tag 0DK5](https://stacks.math.columbia.edu/tag/0DK5) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_derivedProjectionFormulaMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedModuleTensorPushforward.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedModuleTensorPushforward.lean#L164). The attribute's comment: “the invertibility clause, for a morphism of ringed topoi arising from a morphism of sites at a single universe, which is what the derived pullback tensor comparison of 07A4 requires — the small étale ringed topos of an algebraic space does not satisfy this — and given the counit of 07A6 at `M` and its unit at `Rf_*M ⊗^L K`, which is what finiteness of `π` is used for”.

> **Stacks 0DK5, the invertibility clause**, reduced to the derived adjunction of Stacks 07A6:
> the canonical map `Rf_*M ⊗^L_{𝒪_D} K ⟶ Rf_*(M ⊗^L_{𝒪_C} Lf^*K)` of Equation 21.50.0.1 is an
> isomorphism once the counit of `Lf^* ⊣ Rf_*` is invertible at `M` and its unit is invertible at
> `Rf_*M ⊗^L_{𝒪_D} K`.
>
> Writing the canonical map through the unit, `projectionFormulaMap_eq_unit_comp`, it becomes
>
> `Rf\_*M ⊗^L K --η--> Rf\_*Lf^*(Rf\_*M ⊗^L K) --Rf\_*(t)--> Rf\_*(Lf^*Rf\_*M ⊗^L Lf^*K)
>    --Rf\_*(ε ⊗ 1)--> Rf\_*(M ⊗^L Lf^*K)`,
>
> whose middle factor is the comparison of Stacks 07A4 and so invertible with no hypothesis, and
> whose two outer factors are `hη` and `hε`.

```lean
theorem isIso_derivedProjectionFormulaMap
    (M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))
    (hε : IsIso ((derivedAdjunction f hmos).counit.app M))
    (hη : IsIso ((derivedAdjunction f hmos).unit.app
      ((Functor.uncurry.obj (derivedTensorProductFunctor Y.O)).obj
        ((derivedPushforward f).obj M, K)))) :
    IsIso (projectionFormulaMap f hmos M K)
```

**`AlgebraicGeometry.Space.derivedProjectionFormulaIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedModuleTensorPushforward.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedModuleTensorPushforward.lean#L188). The attribute's comment: “the isomorphism, for a morphism of ringed topoi arising from a morphism of sites at a single universe, which is what the derived pullback tensor comparison of 07A4 requires — the small étale ringed topos of an algebraic space does not satisfy this — and given the counit of 07A6 at `M` and its unit at `Rf_*M ⊗^L K`, which is what finiteness of `π` is used for; the tensor factors in the order of Equation 21.50.0.1”.

> **Stacks 0DK5** as an isomorphism `Rf_*M ⊗^L_{𝒪_D} K ≅ Rf_*(M ⊗^L_{𝒪_C} Lf^*K)`, with the
> tensor factors in the order Equation 21.50.0.1 of Stacks 0B56 is written in; the forward map is
> the canonical one, not an unspecified isomorphism of objects.

```lean
def derivedProjectionFormulaIso
    (M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))
    (hε : IsIso ((derivedAdjunction f hmos).counit.app M))
    (hη : IsIso ((derivedAdjunction f hmos).unit.app
      ((Functor.uncurry.obj (derivedTensorProductFunctor Y.O)).obj
        ((derivedPushforward f).obj M, K)))) :
    ((derivedTensorProductFunctor Y.O).obj ((derivedPushforward f).obj M)).obj K ≅
      (derivedPushforward f).obj
        (((derivedTensorProductFunctor X.O).obj M).obj ((derivedPullback f).obj K))
```

**`AlgebraicGeometry.Space.derivedProjectionFormulaIsoSourceOrder`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedModuleTensorPushforward.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedModuleTensorPushforward.lean#L225). The attribute's comment: “the isomorphism in the source's order of tensor factors, for a morphism of ringed topoi arising from a morphism of sites at a single universe, which is what the derived pullback tensor comparison of 07A4 requires — the small étale ringed topos of an algebraic space does not satisfy this — and given the counit of 07A6 at `M` and its unit at `Rf_*M ⊗^L K`, which is what finiteness of `π` is used for”.

> **Stacks 0DK5 in the order the source writes it**,
> `K ⊗^L_{𝒪_D} Rf_*M ≅ Rf_*(Lf^*K ⊗^L_{𝒪_C} M)`.
>
> This is `AlgebraicGeometry.Space.derivedProjectionFormulaIso` read through the commutativity
> constraint of the derived tensor product (Stacks 0FPT) on each side: on `D(𝒪_D)` to transpose the
> source, and inside `Rf_*` on `D(𝒪_C)` to transpose the target. No hypothesis is added.

```lean
def derivedProjectionFormulaIsoSourceOrder
    (M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))
    (hε : IsIso ((derivedAdjunction f hmos).counit.app M))
    (hη : IsIso ((derivedAdjunction f hmos).unit.app
      ((Functor.uncurry.obj (derivedTensorProductFunctor Y.O)).obj
        ((derivedPushforward f).obj M, K)))) :
    ((derivedTensorProductFunctor Y.O).obj K).obj ((derivedPushforward f).obj M) ≅
      (derivedPushforward f).obj
        (((derivedTensorProductFunctor X.O).obj ((derivedPullback f).obj K)).obj M)
```

**`AlgebraicGeometry.Space.nonempty_derivedTensorPushforwardIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteDerivedTensorPushforward.lean, line 528](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteDerivedTensorPushforward.lean#L528).

> **Stacks 0DK5.** Let `π : X ⟶ Y` be a finite morphism of algebraic spaces over `S`, `𝒜` a
> sheaf of rings on `X_étale`, `ℬ` a sheaf of rings on `Y_étale` and `φ : ℬ ⟶ π_*𝒜` a homomorphism
> of sheaves of rings, with associated morphism of ringed topoi
> `f = (π, φ) : (Sh(X_étale), 𝒜) ⟶ (Sh(Y_étale), ℬ)`. Then for every `K ∈ D(ℬ)` and `M ∈ D(𝒜)`
>
> `K ⊗^L_ℬ Rf_*M ≅ Rf_*(Lf^*K ⊗^L_𝒜 M)` in `D(ℬ)`.
>
> `K` is represented by a K-flat complex with flat terms (Stacks 06YS) and `M` by any complex;
> on such representatives the isomorphism is
> `AlgebraicGeometry.Space.derivedTensorPushforwardIsoOfKFlat`.

```lean
theorem nonempty_derivedTensorPushforwardIso (hπ : IsFinite B S hS π.hom)
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf ℬ)))
    (M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf 𝒜))) :
    Nonempty (((Stacks.SheafOfModules.derivedTensorProductFunctor
        (smallEtaleRingedToposOfRings B S hS Y ℬ).toRingedSite).obj K).obj
        ((Stacks.Cohomology.DerivedPushforward.derivedPushforward
          (X := smallEtaleRingedToposOfRings B S hS X 𝒜)
          (Y := smallEtaleRingedToposOfRings B S hS Y ℬ)
          (ringedToposHomOfSharp B S hS π φ)).obj M) ≅
      (Stacks.Cohomology.DerivedPushforward.derivedPushforward
          (X := smallEtaleRingedToposOfRings B S hS X 𝒜)
          (Y := smallEtaleRingedToposOfRings B S hS Y ℬ)
          (ringedToposHomOfSharp B S hS π φ)).obj
        (((Stacks.SheafOfModules.derivedTensorProductFunctor
          (smallEtaleRingedToposOfRings B S hS X 𝒜).toRingedSite).obj
            ((Stacks.Cohomology.DerivedPullbackOfToposHom.derivedPullback
              (ringedToposHomOfSharp B S hS π φ)).obj K)).obj M))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.4, Tag 0DK2](https://stacks.math.columbia.edu/tag/0DK2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
