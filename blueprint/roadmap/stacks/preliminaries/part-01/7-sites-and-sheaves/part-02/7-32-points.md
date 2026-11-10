---
declaration: section
origin: cited
lean: PointOfTopos, CategoryTheory.GrothendieckTopology.Point.presheafFiber, CategoryTheory.GrothendieckTopology.Point.toPresheafFiber, CategoryTheory.GrothendieckTopology.Point.toPresheafFiber_w, CategoryTheory.GrothendieckTopology.Point.fiber_jointly_surjective_of_ofArrows, CategoryTheory.GrothendieckTopology.Point.fiber_pullbackComparison_bijective, CategoryTheory.GrothendieckTopology.Point.sheafFiber_leftExact, CategoryTheory.GrothendieckTopology.Point
statement: formalized
proof: formalized
---

# 7.32 Points

Section 7.32 of the Stacks Project, [Tag 00Y3](https://stacks.math.columbia.edu/tag/00Y3). 12 tags here are carried by 25 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00Y4, a definition

[Tag 00Y4](https://stacks.math.columbia.edu/tag/00Y4) in the Stacks Project.

**`PointOfTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Defs.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Defs.lean#L27). References: SGA 4 IV (6.1).

> A *point of the topos* `Sh(C, J)` is a morphism of topoi `p : Sh(pt) → Sh(C, J)`, where
> `Sh(pt) = Sets` is modelled by `Type w`. Concretely, a point is an adjoint pair `p⁻¹ ⊣ p_*` with
> `p⁻¹ : Sh(C, J) ⥤ Type w` (the stalk functor) and `p_* : Type w ⥤ Sh(C, J)` (the skyscraper
> functor), such that `p⁻¹` is left exact.

```lean
def PointOfTopos.{w, v, u} {C : Type u} [Category.{v} C] (J : GrothendieckTopology C) : Type _
```

## Tag 04EH, an equation

[Tag 04EH](https://stacks.math.columbia.edu/tag/04EH) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.Point.presheafFiber`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Point.presheafFiber#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Point/StalkAsColimit.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Point/StalkAsColimit.lean#L28) (StacksCore): “the stalk `F_p = colim_{{(U, x)}ᵒᵖ} F(U)` of a presheaf at a point of a site”. References: SGA 4 IV (6.8.7), “special case”; SGA 4 IV (6.10), “more general”; SGA 4 VIII (7.9.3).
- [`CategoryTheory.GrothendieckTopology.Point.toPresheafFiber`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Point.toPresheafFiber#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Point/StalkAsColimit.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Point/StalkAsColimit.lean#L30) (StacksCore): “the canonical map `F(U) ⟶ F_p` attached to a neighbourhood `(U, x)` of the point”.
- [`CategoryTheory.GrothendieckTopology.Point.toPresheafFiber_w`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Point.toPresheafFiber_w#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Point/StalkAsColimit.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Point/StalkAsColimit.lean#L32) (StacksCore): “the canonical maps are compatible with morphisms of neighbourhoods”.

## Tag 00Y5, a definition

[Tag 00Y5](https://stacks.math.columbia.edu/tag/00Y5) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.Point.fiber_jointly_surjective_of_ofArrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Basic.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Basic.lean#L55). The attribute's comment: “(1)”.

> **Stacks 00Y5 (1)** for Mathlib's notion of a point: for a covering family
> `{U_i → U}_{i ∈ I}` of a site `C` and a point `Φ`, the map `∐ u(U_i) → u(U)` is
> surjective, i.e. every element of `u(U)` is the image of an element of some `u(U_i)`.
>
> Mathlib's `Point.jointly_surjective` field is stated for covering *sieves*, giving only
> some `g : Y ⟶ U` in the sieve; here the factorisation of `g` through one of the `f i`,
> which is what membership in `Sieve.ofArrows` means, is used to land in `u(U_i)`.

```lean
theorem Point.fiber_jointly_surjective_of_ofArrows {I : Type*} {U : C} {Ui : I → C}
    (f : ∀ i, Ui i ⟶ U) (hf : Sieve.ofArrows Ui f ∈ J U) (x : Φ.fiber.obj U) :
    ∃ (i : I) (y : Φ.fiber.obj (Ui i)), Φ.fiber.map (f i) y = x
```

**`CategoryTheory.GrothendieckTopology.Point.fiber_pullbackComparison_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Basic.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Basic.lean#L70). The attribute's comment: “(2)”.

> **Stacks 00Y5 (2)** for Mathlib's notion of a point: the fiber functor turns fibre
> products into fibre products, i.e. the comparison map
> `u(X ×_Z Y) → u(X) ×_{u(Z)} u(Y)` is bijective.
>
> Stacks assumes this for the members of a covering; Mathlib derives it — from
> cofilteredness of the category of elements of `u` — for *every* pair of morphisms with
> common target, which is the stronger statement proved here.

```lean
theorem Point.fiber_pullbackComparison_bijective [LocallySmall.{w} C]
    {X Y Z : C} (f : X ⟶ Z) (g : Y ⟶ Z) [HasPullback f g] :
    Function.Bijective (pullbackComparison Φ.fiber f g)
```

**`CategoryTheory.GrothendieckTopology.Point.sheafFiber_leftExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Basic.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Basic.lean#L81). The attribute's comment: “(3)”.

> **Stacks 00Y5 (3)** for Mathlib's notion of a point: the stalk functor
> `Sh(C) ⥤ Set`, `F ↦ F_p`, is left exact.
>
> `Point.sheafFiber` is Mathlib's stalk functor, `sheafToPresheaf J _ ⋙ Φ.presheafFiber`,
> the filtered colimit of the sections of `F` over the category of elements of `u`.

```lean
theorem Point.sheafFiber_leftExact [LocallySmall.{w} C] :
    PreservesFiniteLimits (Φ.sheafFiber (A := Type w))
```

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.Point`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Point#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Point/Basic.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Basic.lean#L39) (StacksFrontier): “Mathlib's definition of a point of a site: the fiber functor `u : C ⥤ Type w` together with the conditions making it a point. Mathlib assumes joint surjectivity on covering sieves (Stacks axiom (1)) and cofilteredness of the category of elements of the fiber, from which Stacks axioms (2) and (3) — exactness of the fiber and of the stalk functor on sheaves — follow rather than being assumed; see `Point.fiber_jointly_surjective_of_ofArrows`, `Point.fiber_pullbackComparison_bijective` and `Point.sheafFiber_leftExact` below.”. References: SGA 4 IV (6.3).

## Tag 00Y6, a lemma

[Tag 00Y6](https://stacks.math.columbia.edu/tag/00Y6) in the Stacks Project.

**`Phi_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkFunctor.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/StalkFunctor.lean#L44). The attribute's comment: “isomorphism”.

> **Stacks 00Y6.** The canonical map `Φ_U : p U ⟶ (h_U)_p` from the value of the point at `U`
> to the stalk of the representable presheaf `h_U` is bijective.

```lean
theorem Phi_bijective (p : C ⥤ Type u) (U : C) :
    Function.Bijective (theta p U)
```

**`Phi_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkFunctor.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/StalkFunctor.lean#L52). The attribute's comment: “functoriality”.

> **Stacks 00Y6.** The maps `Φ_U` are natural in `U`: they commute with `p.map g` on the source
> and with the stalk of `yoneda.map g` on the target.

```lean
theorem Phi_naturality (p : C ⥤ Type u) {U U' : C} (g : U ⟶ U') (x : p.obj U) :
    theta p U' (p.map g x) = (presheafStalk p).map (yoneda.map g) (theta p U x)
```

## Tag 04EI, an equation

[Tag 04EI](https://stacks.math.columbia.edu/tag/04EI) in the Stacks Project.

**`pushforwardPresheaf04EI`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/PresheafPushforwardPoint.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/PresheafPushforwardPoint.lean#L27). References: SGA 4 I (1.3), “special case”.

> **Stacks 04EI.** The presheaf `u^p E` attached to a functor `u : C ⥤ Type` and a type `E`:
> it sends an object `U` to the type of functions `u U → E`, and a morphism `f : V ⟶ U` to
> precomposition with `u f`.

```lean
def pushforwardPresheaf04EI {C : Type u} [Category.{v} C] (u : Functor C (Type v)) (E : Type v) :
    Functor Cᵒᵖ (Type v)
```

## Tag 00Y7, a lemma

[Tag 00Y7](https://stacks.math.columbia.edu/tag/00Y7) in the Stacks Project.

**`PresheafPushforwardStalkAdjunction.presheafStalk_adjoint_presheafPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkLeftAdjoint.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/StalkLeftAdjoint.lean#L297).

> **Stacks 00Y7.** For any functor `u : C ⥤ Type w` such that the
> appropriate colimits exist, the pushforward functor `presheafPushforward u`
> is a right adjoint to the stalk functor `presheafStalk u`.

```lean
theorem presheafStalk_adjoint_presheafPushforward
    (u : C ⥤ Type w)
    [HasColimitsOfShape u.Elementsᵒᵖ (Type w)] :
    Nonempty (presheafStalk u ⊣ presheafPushforward u)
```

## Tag 00Y8, a lemma

[Tag 00Y8](https://stacks.math.columbia.edu/tag/00Y8) in the Stacks Project.

**`main_theorem00Y8`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkExact.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/StalkExact.lean#L43).

> **Stacks 00Y8, statement (3), narrow form.**
>
> Let `C` be a small category equipped with a Grothendieck topology `J`, let
> `L : (Cᵒᵖ ⥤ Type v) ⥤ Type v` be the "stalk-at-a-point" functor on presheaves,
> and let `R : Type v ⥤ (Cᵒᵖ ⥤ Type v)` be the "point-pushforward" functor.
> Assume:
>
> * `L ⊣ R` (this packages tag 00Y8 statement (2) at the presheaf level: the
>   stalk functor is left adjoint to the point-pushforward functor), and
> * for every set `E`, the presheaf `R.obj E` is a sheaf for `J` (this is tag
>   00Y8 statement (1): `u^p E` is a sheaf).
>
> Then for every presheaf `F` and every set `E`, precomposition by
> `L.map (toSheafify J F)` is a bijection
> `(L.obj (sheafify J F) ⟶ E) → (L.obj F ⟶ E)`. By Yoneda this is the abstract
> content of tag 00Y8 statement (3): the canonical map `F_p → (F^#)_p` from the
> stalk of a presheaf to the stalk of its sheafification is an isomorphism in
> `Type v`.

```lean
theorem main_theorem00Y8
    {C : Type u} [SmallCategory C] (J : GrothendieckTopology C)
    [HasWeakSheafify J (Type v)]
    (L : (Cᵒᵖ ⥤ Type v) ⥤ Type v) (R : Type v ⥤ Cᵒᵖ ⥤ Type v)
    (adj : L ⊣ R)
    (hR : ∀ E : Type v, Presheaf.IsSheaf J (R.obj E))
    (F : Cᵒᵖ ⥤ Type v) (E : Type v) :
    Function.Bijective
      (fun g : L.obj (sheafify J F) ⟶ E => L.map (toSheafify J F) ≫ g)
```

## Tag 00Y9, a definition

[Tag 00Y9](https://stacks.math.columbia.edu/tag/00Y9) in the Stacks Project.

**`pushforwardPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/PushforwardPoint.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/PushforwardPoint.lean#L27). References: EGA IV (21.9.1), “more general”.

> **Stacks 00Y9.** The pushforward `p_* E` of an object `E` along a point `p` of the site
> `(C, J)`: the skyscraper sheaf at `p` with value `E`.

```lean
noncomputable def pushforwardPoint
    {C : Type u} [Category.{v} C] {J : GrothendieckTopology C}
    (p : J.Point) {A : Type*} [Category A] [Limits.HasProducts A] (E : A) :
    Sheaf J A
```

## Tag 00YA, a lemma

[Tag 00YA](https://stacks.math.columbia.edu/tag/00YA) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.targetSitePoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/TargetSitePoint.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/TargetSitePoint.lean#L107). The attribute's comment: “(2), applied to the composite of a point of the source site with a morphism of ringed topoi”.

> **Stacks 00YA (2) along a morphism of ringed topoi.** The point of the target site `(D, K)`
> whose stalk functor is the inverse image along `f` followed by the stalk functor of the point
> `Φ` of the source site.

```lean
def targetSitePoint (f : RingedToposHom X Y) (Φ : X.J.Point.{w}) : Y.J.Point.{w}
```

**`CategoryTheory.GrothendieckTopology.Point.pointOfTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L294). The attribute's comment: “(1): a point of the site defines a morphism of topoi `Sh(pt) → Sh(C)`”. References: SGA 4 IV (6.8.7), “(ii)”; SGA 4 IV (7.1), “more general”.

> **Stacks 00YA (1).** Let `p` be a point of the site `C`, given by a fibre functor
> `u = Φ.fiber`. Then the pair of functors `(p_*, p^{-1}) = (Φ.skyscraperSheafFunctor,
> Φ.sheafFiber)` is a morphism of topoi `Sh(pt) → Sh(C)`, i.e. a point of the topos `Sh(C)` in
> the sense of Stacks 00Y4.
>
> The two functors are adjoint by `Point.skyscraperSheafAdjunction`, and `p^{-1}` is left exact
> by `Point.sheafFiber_leftExact` (Stacks 00Y5 (3)), which are exactly the two conditions in the
> definition of a morphism of topoi (Stacks 00XA).

```lean
noncomputable def pointOfTopos (Φ : Point.{w} J) : PointOfTopos.{w, v, u} J
```

**`CategoryTheory.GrothendieckTopology.Point.sheafFiberComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L372). The attribute's comment: “(2): the canonical comparison from the reconstructed stalk functor”.

> The canonical comparison from the stalk functor to `F`, induced by a natural
> transformation on the sheafified representables. On a germ `(U, x, σ)` it is
> `F(σ)(α_U(x))`, viewing the section `σ` as a map out of `h_U^#`.

```lean
noncomputable def sheafFiberComparison : Φ.sheafFiber ⟶ F
```

**`PointOfTopos.exists_sitePoint_fiber_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L523). The attribute's comment: “(2): reconstruction of the site point”.

> **Stacks 00YA (2).** Every point `p` of the topos arises from a point of the site
> whose fiber functor is `U ↦ p⁻¹(h_U^#)` on the nose.
>
> `PointOfTopos.exists_sitePoint` is the same reconstruction stated up to isomorphism of stalk
> functors; this form is the one consumers need when they have to transport along the identity of
> fibre functors with `eqToIso`.

```lean
theorem exists_sitePoint_fiber_eq {C : Type u} [Category.{v} C] {J : GrothendieckTopology C}
    (p : PointOfTopos.{max u v, v, u} J) :
    ∃ Φ : GrothendieckTopology.Point.{max u v} J,
      Φ.fiber = Sheaf.sheafifiedYoneda J ⋙ p.inverseImage
```

**`PointOfTopos.isIso_sheafFiberComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 602](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L602). The attribute's comment: “(2): the canonical inverse-image comparison is an isomorphism”.

> **Stacks 00YA (2).** The canonical comparison identifies the reconstructed stalk
> functor with `p.inverseImage`.

```lean
theorem isIso_sheafFiberComparison :
    IsIso (Φ.sheafFiberComparison p.inverseImage e.hom)
```

**`PointOfTopos.isIso_conjugate_sheafFiberComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L635). The attribute's comment: “(2): recovery of the pushforward by the adjoint mate”.

> **Stacks 00YA (2).** The adjoint mate of the canonical comparison is an isomorphism
> `p.pushforward ⟶ Φ.skyscraperSheafFunctor`, recovering the pushforward compatibly with
> the given adjunctions.

```lean
theorem isIso_conjugate_sheafFiberComparison :
    IsIso (conjugateEquiv p.adj Φ.skyscraperSheafAdjunction
      (Φ.sheafFiberComparison p.inverseImage e.hom))
```

## Tag 04EL, a lemma

[Tag 04EL](https://stacks.math.columbia.edu/tag/04EL) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.Point.exists_equivalence_isMorphismOfSites_pushforward_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Points.lean, line 586](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Points.lean#L586).

> **Stacks 04EL.** Let `Φ` be a point of a locally `w`-small site `(C, J)`, with fibre functor
> `u = Φ.fiber`. Let `ι : S ⥤ Type w` be a full subcategory of the category of sets in which some
> object `pt` is a singleton, let `K` be the topology on `S` whose covering sieves are the jointly
> surjective ones, and suppose the fibre functor factors as `u ⋙ ι` for some `u : C ⥤ S`. Then
>
> 1. there is an equivalence `i : Sh(pt) → Sh(S, K)` whose inverse image is `F ↦ F(pt)`, hence
>    whose forward functor sends a set `E` to the sheaf `V ↦ Mor(ι V, E)`;
> 2. `u : C ⥤ S` defines a morphism of sites `f : (S, K) → (C, J)`; and
> 3. the composition `Sh(pt) → Sh(S, K) → Sh(C, J)` is the morphism of topoi `(p_*, p⁻¹)` of the
>    point, in the sense that `i_* ⋙ f_*` is isomorphic to the skyscraper sheaf functor `p_*`.

```lean
public theorem exists_equivalence_isMorphismOfSites_pushforward_iso {C : Type u} [Category.{v} C]
    {J : GrothendieckTopology C} [LocallySmall.{w} C] (Φ : Point.{w} J) {S : Type w}
    [SmallCategory S] (ι : S ⥤ Type w) [ι.Full] [ι.Faithful] (pt : S) (hpt : Unique (ι.obj pt))
    (K : GrothendieckTopology S)
    (hK :
      ∀ (V : S) (R : Sieve V),
        R ∈ K V ↔ ∀ x : ι.obj V, ∃ (W : S) (f : W ⟶ V) (y : ι.obj W), R.arrows f ∧ ι.map f y = x)
    (u : C ⥤ S) (hu : u ⋙ ι ≅ Φ.fiber) :
    ∃ (e : Type w ≌ Sheaf K (Type w)) (_ : _root_.IsMorphismOfSites.{w} u J K),
      e.inverse = sheafToPresheaf K (Type w) ⋙ (evaluation Sᵒᵖ (Type w)).obj (Opposite.op pt) ∧
        Nonempty
          (e.functor ⋙ u.sheafPushforwardContinuous (Type w) J K ≅
            Φ.skyscraperSheafFunctor (A := Type w))
```

## Tag 05UX, a lemma

[Tag 05UX](https://stacks.math.columbia.edu/tag/05UX) in the Stacks Project.

**`ToposPoint.epsilon_comp_eta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Skyscraper.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Skyscraper.lean#L94).

> **Stacks 05UX.** For any set `E` there are canonical maps
> `E ⟶ (p_* E)_p ⟶ E` whose composition is the identity of `E`.
>
> Proof: apply naturality of the counit `ε` of `p⁻¹ ⊣ p_*` to the constant map
> `i_e : PUnit → E`, then evaluate at `default : p⁻¹(p_*(PUnit))`.

```lean
theorem epsilon_comp_eta (E : Type v) : p.epsilon E ∘ p.eta E = id
```

## Tag 05UY, a lemma

[Tag 05UY](https://stacks.math.columbia.edu/tag/05UY) in the Stacks Project.

**`PointOfTopos.preservesLimitsOfSize_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L216). The attribute's comment: “commutes with arbitrary limits”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos commutes with arbitrary
> limits, because it is a right adjoint.

```lean
theorem preservesLimitsOfSize_pushforward : PreservesLimitsOfSize.{w₁, w₂} p.pushforward
```

**`PointOfTopos.preservesFiniteLimits_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L221). The attribute's comment: “is left exact”. References: SGA 4 IV (3.1.2), “point; finite limits”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos is left exact.

```lean
theorem preservesFiniteLimits_pushforward : PreservesFiniteLimits p.pushforward
```

**`PointOfTopos.faithful_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L228). The attribute's comment: “is faithful”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos is faithful: the counit
> `ε_E : p^{-1}p_*E → E` is a (split) epimorphism, and `ε` is natural.

```lean
theorem faithful_pushforward : p.pushforward.Faithful
```

**`PointOfTopos.preservesEpimorphisms_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L241). The attribute's comment: “transforms surjections into surjections. The other claim of the same sentence of the source — that `p_*` commutes with coequalizers — is FALSE and is not claimed anywhere in this file; see `Point.subsingleton_fiber_of_preservesCoequalizers`”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos transforms surjections into
> surjections: every epimorphism of sets is a *split* epimorphism, and a split epimorphism is
> carried to a split epimorphism by any functor.

```lean
theorem preservesEpimorphisms_pushforward : p.pushforward.PreservesEpimorphisms
```

**`PointOfTopos.reflectsMonomorphisms_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L248). The attribute's comment: “reflects injections”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos reflects injections.

```lean
theorem reflectsMonomorphisms_pushforward : p.pushforward.ReflectsMonomorphisms
```

**`PointOfTopos.reflectsEpimorphisms_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L254). The attribute's comment: “reflects surjections”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos reflects surjections.

```lean
theorem reflectsEpimorphisms_pushforward : p.pushforward.ReflectsEpimorphisms
```

**`PointOfTopos.reflectsIsomorphisms_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L266). The attribute's comment: “reflects isomorphisms”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos reflects isomorphisms: it
> reflects both injections and surjections, and a map of sets which is both injective and
> surjective is bijective.

```lean
theorem reflectsIsomorphisms_pushforward : p.pushforward.ReflectsIsomorphisms
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.32, Tag 00Y3](https://stacks.math.columbia.edu/tag/00Y3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
