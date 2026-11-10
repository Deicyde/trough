---
declaration: section
origin: cited
lean: CategoryTheory.baseChangeShriek, AlgebraicGeometry.extensionByZeroProperBaseChangeIso, CategoryTheory.compactificationShriek, AlgebraicGeometry.extensionByZeroCompactificationIso, CategoryTheory.restrictionHomNatTrans, CategoryTheory.extensionByZeroCovariance, CategoryTheory.extensionByZeroHomEquiv_covariance, CategoryTheory.extensionByZeroCovariance_app_eq
statement: formalized
proof: formalized
---

# 48.31 Preliminaries to compactly supported cohomology

Section 48.31 of the Stacks Project, [Tag 0G4V](https://stacks.math.columbia.edu/tag/0G4V). 3 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G4W, a lemma

[Tag 0G4W](https://stacks.math.columbia.edu/tag/0G4W) in the Stacks Project.

**`CategoryTheory.baseChangeShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/BaseChangeShriek.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/BaseChangeShriek.lean#L111). The attribute's comment: “the Deligne system assignments, the adjunctions Rg_* ⊣ g^! and Rf_* ⊣ f^!, and the compatibility (j')^* ∘ g^! ≅ f^! ∘ j^* coming from Tags 0ATX and 0AU0, supplied as data”.

> **Stacks Project, Tag 0G4W.** Let `f : X ⟶ Y` be a proper morphism of Noetherian schemes, let
> `V ⊆ Y` be open and let `U = f^{-1}(V)`, with `j : U ⟶ X`, `j' : V ⟶ Y` the open immersions and
> `g : U ⟶ V` the induced morphism. There is a canonical isomorphism
>
> `Rj'_! ∘ Rg_* ≅ Rf_* ∘ Rj_!`
>
> of functors `D^b_{Coh}(𝒪_U) ⥤ Pro-D^b_{Coh}(𝒪_Y)`.
>
> The isomorphism is constructed, not merely asserted: on functors of points it is the chain of
> adjunctions `CategoryTheory.baseChangeShriekPoints`, which is the source's second proof.

```lean
public def baseChangeShriek :
    gstar ⋙ extensionByZero jV A' ≅ extensionByZero jU A ⋙ ProSeq.pushforward adjf
```

**`AlgebraicGeometry.extensionByZeroProperBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/BaseChangeShriekProper.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/BaseChangeShriekProper.lean#L66).

> **Stacks Project, Tag 0G4W.** Let `f : X ⟶ Y` be a proper morphism of Noetherian schemes, let
> `V ⊆ Y` be open and let `U = f⁻¹(V)`, with `j : U ⟶ X`, `j' : V ⟶ Y` the open immersions and
> `g : U ⟶ V` the restriction of `f`. There is a canonical isomorphism
>
> `Rj'_! ∘ Rg_* ≅ Rf_* ∘ Rj_!`
>
> of functors `D^b_{Coh}(𝒪_U) ⥤ Pro-D^b_{Coh}(𝒪_Y)`, where `Rj_!`, `Rj'_!` are the extensions by
> zero of [Stacks, Tag 0G4N] and `Rf_*` acts on pro-objects termwise.
>
> This is the source's first proof: for a Deligne system `(K_n)` with value `K` the system
> `(Rf_* K_n)` is pro-isomorphic to a Deligne system
> (`AlgebraicGeometry.proIsoDeligneSystem_properPushforward`), and its restriction to `V` is
> constant with value `Rg_* K` by flat base change, so by the uniqueness of Deligne systems
> (Stacks 0G2H) it represents `Rj'_! Rg_* K`; this identification is natural in `K`
> (`CategoryTheory.baseChangeShriekOfLifting`).

```lean
public def extensionByZeroProperBaseChangeIso {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f]
    [IsNoetherian X] [IsNoetherian Y] (V : Y.Opens) :
    properPushforwardBoundedCoherent (f ∣_ V) ⋙ extensionByZeroOpenImmersion V.ι ≅
      extensionByZeroOpenImmersion (f ⁻¹ᵁ V).ι ⋙
        ProSeq.map (properPushforwardBoundedCoherent f)
```

## Tag 0G4X, a lemma

[Tag 0G4X](https://stacks.math.columbia.edu/tag/0G4X) in the Stacks Project.

**`CategoryTheory.compactificationShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/BaseChangeShriek.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/BaseChangeShriek.lean#L133). The attribute's comment: “the Deligne system assignments, the adjunction Rf_* ⊣ f^!, and the compatibility j^* ≅ f^! ∘ (j')^* coming from Tags 0ATX and 0AU0, supplied as data”.

> **Stacks Project, Tag 0G4X.** Let `j : U ⟶ X` be an open immersion of Noetherian schemes and
> let `j' : U ⟶ X'` be a compactification of `U` over `X`, with structure morphism `f : X' ⟶ X`.
> There is a canonical isomorphism
>
> `Rj_! ≅ Rf_* ∘ R(j')_!`
>
> of functors `D^b_{Coh}(𝒪_U) ⥤ Pro-D^b_{Coh}(𝒪_X)`.
>
> This is `CategoryTheory.baseChangeShriek` for the open `j(U) ⊆ X` and the identity `U ⟶ U`: the
> compatibility it needs becomes `j^* ≅ f^! ⋙ (j')^*`, which holds for a compactification because
> `f^!` is local on the source and `f ∘ j' = j` is an open immersion.

```lean
public def compactificationShriek {jX' : 𝒟 ⥤ 𝒞} (A₁ : DeligneSystemAssignment jX')
    {jX : 𝒟' ⥤ 𝒞} (A₂ : DeligneSystemAssignment jX)
    (κ' : jX ≅ fshriek ⋙ jX') :
    extensionByZero jX A₂ ≅ extensionByZero jX' A₁ ⋙ ProSeq.pushforward adjf
```

**`AlgebraicGeometry.extensionByZeroCompactificationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/CompactificationShriek.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/CompactificationShriek.lean#L291).

> **Stacks Project, Tag 0G4X.** Let `j : U ⟶ X` be an open immersion of Noetherian schemes and
> let `j' : U ⟶ X'` be a compactification of `U` over `X`, with structure morphism `f : X' ⟶ X`
> (`f` proper, `j'` an open immersion and `j = f ∘ j'`). Then there is a canonical isomorphism
>
> `Rj_! ≅ Rf_* ∘ R(j')_!`
>
> of functors `D^b_{Coh}(𝒪_U) ⥤ Pro-D^b_{Coh}(𝒪_X)`, where `Rj_!` and `R(j')_!` are the extensions
> by zero of [Stacks, Tag 0G4N] and `Rf_*` acts on pro-objects termwise.
>
> The proof is the source's. Let `X'' ⊆ X'` be the scheme-theoretic closure of `j'`, with
> `j'' : U ⟶ X''` and `f' : X'' ⟶ X'` (`AlgebraicGeometry.CompactificationOf.closure`). As `U` is
> dense in `X''`, [Stacks, Tag 0ATU] (c) gives `j''(U) = f'⁻¹(j'(U)) = (f ∘ f')⁻¹(j(U))`, so the case
> `AlgebraicGeometry.compactificationShriekOfPreimage` of [Stacks, Tag 0G4W] gives
> `Rf'_* ∘ Rj''_! ≅ Rj'_!` and `R(f ∘ f')_* ∘ Rj''_! ≅ Rj_!`; and `R(f ∘ f')_* ≅ Rf_* ∘ Rf'_*`
> (`AlgebraicGeometry.properPushforwardBoundedCoherentCompIso`).

```lean
public def extensionByZeroCompactificationIso :
    extensionByZeroOpenImmersion j ≅
      extensionByZeroOpenImmersion c.immersion ⋙
        ProSeq.map (properPushforwardBoundedCoherent c.toBase)
```

## Tag 0G4Y, a remark

[Tag 0G4Y](https://stacks.math.columbia.edu/tag/0G4Y) in the Stacks Project.

**`CategoryTheory.restrictionHomNatTrans`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroCovariance.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroCovariance.lean#L105). The attribute's comment: “the restriction map Hom_U(K, L|_U) → Hom_{U'}(K|_{U'}, L|_{U'}) of the display, as a transformation functorial in L”.

> The displayed arrow of [Stacks, Tag 0G4Y]: the restriction map
>
> `Hom_U(K, L|_U) ⟶ Hom_{U'}(K|_{U'}, L|_{U'})`,
>
> sending `α` to `i^* α` followed by the identification `e : j^* ⋙ i^* ≅ j'^*`, read as a
> transformation of the functors `L ↦ Hom_𝒞(K, j^* L)` and `L ↦ Hom_{𝒞'}(i^* K, j'^* L)`. Its
> naturality in `L` is the functoriality in `L` that the source uses to pin the canonical map
> down.

```lean
public def restrictionHomNatTrans (K : 𝒞) :
    jstar ⋙ coyoneda.obj (op K) ⟶ jstar' ⋙ coyoneda.obj (op (istar.obj K))
```

**`CategoryTheory.extensionByZeroCovariance`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroCovariance.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroCovariance.lean#L147). The attribute's comment: “the canonical map Rj'_!(K|_{U'}) ⟶ Rj_! K, with the functoriality in K as its naturality; the Deligne-system assignments on both sides supplied as data”.

> **Stacks Project, Tag 0G4Y.** Let `X ⊃ U ⊃ U'` be open subschemes of a Noetherian scheme,
> let `j : U ⟶ X`, `j' : U' ⟶ X` and `i : U' ⟶ U` be the inclusions. There is a canonical map
>
> `Rj'_!(K|_{U'}) ⟶ Rj_! K`
>
> in `Pro-D^b_{Coh}(𝒪_X)`, functorial for `K` in `D^b_{Coh}(𝒪_U)`. Here it is produced as a
> transformation `i^* ⋙ Rj'_! ⟶ Rj_!` of functors `𝒞 ⥤ Pro-𝒟`, so that the functoriality in `K`
> is its naturality.
>
> A morphism of pro-objects is a transformation of their functors of points in the opposite
> direction, which is the appeal to [Stacks, Tag 0G2X] in the source; the transformation used is
> the restriction map `CategoryTheory.restrictionHomNatTrans`, whose naturality in `L` is the
> functoriality in `L` of the display.

```lean
public def extensionByZeroCovariance :
    istar ⋙ extensionByZero jstar' A' ⟶ extensionByZero jstar A
```

**`CategoryTheory.extensionByZeroHomEquiv_covariance`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroCovariance.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroCovariance.lean#L183). The attribute's comment: “the display: composing with the canonical map is the restriction map Hom_U(K, L|_U) → Hom_{U'}(K|_{U'}, L|_{U'})”.

> **The characterising property of the canonical map of [Stacks, Tag 0G4Y].** Under the
> adjointness bijections of [Stacks, Tag 0G4N], composing a morphism `Rj_! K ⟶ L` with the
> canonical map `Rj'_!(K|_{U'}) ⟶ Rj_! K` is the restriction map of the display:
>
> `Hom_{Pro}(Rj_! K, L) = Hom_U(K, L|_U) → Hom_{U'}(K|_{U'}, L|_{U'}) = Hom_{Pro}(Rj'_!(K|_{U'}), L)`
>
> This is the equality the source asks the canonical map to satisfy; by
> `CategoryTheory.extensionByZeroCovariance_app_eq` it determines the map.

```lean
public lemma extensionByZeroHomEquiv_covariance (K : 𝒞) (L : 𝒟)
    (f : (extensionByZero jstar A).obj K ⟶ ProSeq.const.obj L) :
    extensionByZeroHomEquiv jstar' A' (istar.obj K) L
        ((extensionByZeroCovariance jstar jstar' istar e A A').app K ≫ f) =
      istar.map (extensionByZeroHomEquiv jstar A K L f) ≫ e.hom.app L
```

**`CategoryTheory.extensionByZeroCovariance_app_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroCovariance.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroCovariance.lean#L210). The attribute's comment: “the canonical map is the only one inducing the restriction map on morphisms into constant pro-objects, which is the appeal to Tag 0G2X”.

> **The canonical map of [Stacks, Tag 0G4Y] is the unique map with its characterising
> property.** This is what the appeal to [Stacks, Tag 0G2X] in the source provides: a morphism of
> pro-objects `Rj'_!(K|_{U'}) ⟶ Rj_! K` is determined by the induced map
> `Hom_{Pro}(Rj_! K, L) → Hom_{Pro}(Rj'_!(K|_{U'}), L)`, functorially in `L`, so requiring that map
> to be the restriction map of the display leaves exactly one choice.

```lean
public lemma extensionByZeroCovariance_app_eq (K : 𝒞)
    (g : (extensionByZero jstar' A').obj (istar.obj K) ⟶ (extensionByZero jstar A).obj K)
    (hg : ∀ (L : 𝒟) (f : (extensionByZero jstar A).obj K ⟶ ProSeq.const.obj L),
      extensionByZeroHomEquiv jstar' A' (istar.obj K) L (g ≫ f) =
        istar.map (extensionByZeroHomEquiv jstar A K L f) ≫ e.hom.app L) :
    g = (extensionByZeroCovariance jstar jstar' istar e A A').app K
```

**`AlgebraicGeometry.extensionByZeroOpenCovariance`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenCovariance.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenCovariance.lean#L113). The attribute's comment: “the canonical map Rj'_!(K|_{U'}) ⟶ Rj_! K, functorial in K”.

> **Stacks Project, Tag 0G4Y.** Let `X ⊃ U ⊃ U'` be open subschemes of a Noetherian scheme `X`
> and let `j : U ⟶ X`, `j' : U' ⟶ X` be the inclusions. There is a canonical map
>
> `Rj'_!(K|_{U'}) ⟶ Rj_! K`
>
> in `Pro-D^b_{Coh}(𝒪_X)`, functorial for `K` in `D^b_{Coh}(𝒪_U)`: a transformation
> `i^* ⋙ Rj'_! ⟶ Rj_!` of functors `D^b_{Coh}(𝒪_U) ⥤ Pro-D^b_{Coh}(𝒪_X)`, where `i : U' ⟶ U` is the
> inclusion and `Rj_!`, `Rj'_!` are the functors `AlgebraicGeometry.extensionByZeroOpenImmersion`.
>
> It induces, on morphisms into a constant pro-object `L`, the restriction map
> `Hom_U(K, L|_U) → Hom_{U'}(K|_{U'}, L|_{U'})`
> (`AlgebraicGeometry.extensionByZeroOpenHomEquiv_covariance`), it is the only map doing so
> (`AlgebraicGeometry.extensionByZeroOpenCovariance_app_eq`), and it is given by the inclusions
> `(𝓘')^n 𝓕^• ⊆ 𝓘^n 𝓕^•` (`AlgebraicGeometry.extensionByZeroOpenCovariance_conj_eq_ofMap`).

```lean
public def extensionByZeroOpenCovariance :
    restrictBoundedCoherentLift (X.homOfLE h) ⋙ extensionByZeroOpenImmersion U'.ι ⟶
      extensionByZeroOpenImmersion U.ι
```

**`AlgebraicGeometry.extensionByZeroOpenHomEquiv_covariance`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenCovariance.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenCovariance.lean#L137). The attribute's comment: “the display: composing with the canonical map is the restriction map Hom_U(K, L|_U) → Hom_{U'}(K|_{U'}, L|_{U'})”.

> **The display of [Stacks, Tag 0G4Y].** Under the identifications
> `Hom_{Pro}(Rj_! K, L) = Hom_U(K, L|_U)` of [Stacks, Tag 0G2H], composing with the canonical map
> `Rj'_!(K|_{U'}) ⟶ Rj_! K` is the restriction map
> `Hom_U(K, L|_U) → Hom_{U'}(K|_{U'}, L|_{U'})`.

```lean
public lemma extensionByZeroOpenHomEquiv_covariance
    (K : BoundedCoherentDerived U.toScheme) (L : BoundedCoherentDerived X)
    (f : (extensionByZeroOpenImmersion U.ι).obj K ⟶ ProSeq.const.obj L) :
    extensionByZeroHomEquiv _ (DeligneSystem.values U'.ι).toAssignment
        ((restrictBoundedCoherentLift (X.homOfLE h)).obj K) L
        ((extensionByZeroOpenCovariance h).app K ≫ f) =
      (restrictBoundedCoherentLift (X.homOfLE h)).map
          (extensionByZeroHomEquiv _ (DeligneSystem.values U.ι).toAssignment K L f) ≫
        (restrictBoundedCoherentLiftHomOfLEIso h).hom.app L
```

**`AlgebraicGeometry.extensionByZeroOpenCovariance_app_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenCovariance.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenCovariance.lean#L154). The attribute's comment: “the canonical map is the only one inducing the restriction map on morphisms into constant pro-objects, which is the appeal to Tag 0G2X”.

> **The canonical map of [Stacks, Tag 0G4Y] is the only one with the property of the display.**
> A morphism `Rj'_!(K|_{U'}) ⟶ Rj_! K` of pro-objects which induces the restriction map on morphisms
> into every constant pro-object is the canonical map; this is the appeal to [Stacks, Tag 0G2X] in
> the source.

```lean
public lemma extensionByZeroOpenCovariance_app_eq
    (K : BoundedCoherentDerived U.toScheme)
    (g : (extensionByZeroOpenImmersion U'.ι).obj
        ((restrictBoundedCoherentLift (X.homOfLE h)).obj K) ⟶
      (extensionByZeroOpenImmersion U.ι).obj K)
    (hg : ∀ (L : BoundedCoherentDerived X)
      (f : (extensionByZeroOpenImmersion U.ι).obj K ⟶ ProSeq.const.obj L),
      extensionByZeroHomEquiv _ (DeligneSystem.values U'.ι).toAssignment
          ((restrictBoundedCoherentLift (X.homOfLE h)).obj K) L (g ≫ f) =
        (restrictBoundedCoherentLift (X.homOfLE h)).map
            (extensionByZeroHomEquiv _ (DeligneSystem.values U.ι).toAssignment K L f) ≫
          (restrictBoundedCoherentLiftHomOfLEIso h).hom.app L) :
    g = (extensionByZeroOpenCovariance h).app K
```

**`AlgebraicGeometry.extensionByZeroOpenCovariance_conj_eq_ofMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenCovariance.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenCovariance.lean#L353). The attribute's comment: “the explicit construction: the canonical map is given by the maps K'_n = (𝓘')^n 𝓕^• ⟶ 𝓘^n 𝓕^• = K_n coming from the inclusions (𝓘')^n ⊆ 𝓘^n”.

> **The explicit construction of [Stacks, Tag 0G4Y].** Let `𝓕^•` be a bounded complex of
> coherent `𝒪_X`-modules whose restriction to `U` represents `K`, and let `𝓘' ⊆ 𝓘` be quasi-coherent
> sheaves of ideals with `V(𝓘) = X ∖ U` and `V(𝓘') = X ∖ U'`. Then `Rj_! K` and `Rj'_!(K|_{U'})` are
> represented by the inverse systems `K_n = 𝓘^n 𝓕^•` and `K'_n = (𝓘')^n 𝓕^•`
> (`AlgebraicGeometry.DeligneSystem.Value.extensionByZeroIso`), and under these identifications
> the canonical map `Rj'_!(K|_{U'}) ⟶ Rj_! K` is given by the maps `K'_n ⟶ K_n` coming from the
> inclusions `(𝓘')^n ⊆ 𝓘^n`.
>
> The reduction to `𝓘' ⊆ 𝓘` is `Stacks.AlgebraicGeometry.IdealPower.support_sup_eq_left`, and
> such complexes exist by `AlgebraicGeometry.exists_bounded_isCoherent_complex_restrict_Q_iso`;
> such ideals exist, e.g. the vanishing ideals of the closed complements.

```lean
public theorem extensionByZeroOpenCovariance_conj_eq_ofMap :
    (DeligneSystem.ofComplexValue (j := U'.ι) I' hI' F hFge hFle hFcoh _
          (restrictValueIsoOfLE h F K φ)).extensionByZeroIso.hom ≫
        (extensionByZeroOpenCovariance h).app K ≫
        (DeligneSystem.ofComplexValue (j := U.ι) I hI F hFge hFle hFcoh K
          φ).extensionByZeroIso.inv =
      ProSeq.ofMap (idealPowerSystemCompare F hFge hFle hFcoh hI hI' hle)
```

**`Stacks.AlgebraicGeometry.IdealPower.support_sup_eq_left`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/IdealPowerComplexComparison.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/IdealPowerComplexComparison.lean#L79). The attribute's comment: “the reduction to 𝓘' ⊆ 𝓘 of the explicit construction: replacing 𝓘 by 𝓘 + 𝓘' leaves the vanishing locus unchanged”.

> Replacing a quasi-coherent sheaf of ideals by its sum with one whose vanishing locus is
> larger does not change the vanishing locus. In [Stacks, Tag 0G4Y] this is the step that lets one
> assume `𝓘' ⊆ 𝓘`: there `V(𝓘) = X ∖ U` and `V(𝓘') = X ∖ U'` with `U' ⊆ U`, so
> `V(𝓘 + 𝓘') = V(𝓘)`, while `𝓘' ≤ 𝓘 + 𝓘'`.

```lean
public lemma support_sup_eq_left {I I' : X.IdealSheafData} (h : I.support ≤ I'.support) :
    (I ⊔ I').support = I.support
```

**`AlgebraicGeometry.IdealPowerComplexSystem.compareHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/IdealPowerComplexComparison.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/IdealPowerComplexComparison.lean#L177). The attribute's comment: “the maps K'_n = (𝓘')^n 𝓕^• ⟶ 𝓘^n 𝓕^• = K_n of the explicit construction, induced by the inclusions (𝓘')^n ⊆ 𝓘^n”.

> **The maps `K'_n ⟶ K_n` of the explicit construction in [Stacks, Tag 0G4Y].** For
> `𝓘' ≤ 𝓘` the inclusions `(𝓘')^n • 𝓕^i ⊆ 𝓘^n • 𝓕^i` assemble into a map of complexes
>
> `(𝓘')^n 𝓕^• ⟶ 𝓘^n 𝓕^•`.
>
> The source writes `K'_n = (𝓘')^n 𝓕^•` and `K_n = 𝓘^n 𝓕^•` and describes its canonical map
> `Rj'_!(K|_{U'}) ⟶ Rj_! K` as being given by these maps.

```lean
public def compareHom (S' : IdealPowerComplexSystem I F) (S : IdealPowerComplexSystem J F)
    (h : I ≤ J) (n : ℕ) : S'.complex n ⟶ S.complex n
```

**`AlgebraicGeometry.IdealPowerComplexSystem.compareHom_comp_inclusion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/IdealPowerComplexComparison.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/IdealPowerComplexComparison.lean#L203). The attribute's comment: “the maps K'_n ⟶ K_n of the explicit construction are the inclusions read inside 𝓕^•, which is what pins them down”.

> **The comparison map of [Stacks, Tag 0G4Y] is the inclusion, read inside `𝓕^•`.** Composing
> `K'_n ⟶ K_n` with the inclusion of `K_n` into `𝓕^•` gives the inclusion of `K'_n`. Since the
> inclusions are termwise monomorphisms, this characterises the comparison map.

```lean
public lemma compareHom_comp_inclusion (S' : IdealPowerComplexSystem I F)
    (S : IdealPowerComplexSystem J F) (h : I ≤ J) (n : ℕ) :
    S'.compareHom S h n ≫ S.inclusion n = S'.inclusion n
```

**`AlgebraicGeometry.IdealPowerComplexSystem.compareHom_comp_transition`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/IdealPowerComplexComparison.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/IdealPowerComplexComparison.lean#L213). The attribute's comment: “the maps K'_n ⟶ K_n of the explicit construction commute with the transitions, so they are a map of the inverse systems (K'_n) ⟶ (K_n)”.

> **The comparison maps of [Stacks, Tag 0G4Y] form a map of inverse systems.** They commute
> with the transitions `K'_{n+1} ⟶ K'_n` and `K_{n+1} ⟶ K_n` of the two ideal-power
> filtrations.

```lean
public lemma compareHom_comp_transition (S' : IdealPowerComplexSystem I F)
    (S : IdealPowerComplexSystem J F) (h : I ≤ J) (n : ℕ) :
    S'.transition n ≫ S'.compareHom S h n = S'.compareHom S h (n + 1) ≫ S.transition n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.31, Tag 0G4V](https://stacks.math.columbia.edu/tag/0G4V)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
