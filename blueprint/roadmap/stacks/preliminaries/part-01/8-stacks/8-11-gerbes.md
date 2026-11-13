---
declaration: section
origin: cited
lean: CategoryTheory.Functor.IsGerbe, CategoryTheory.Functor.isGerbe_iff_of_isEquivalenceOver, CategoryTheory.isGerbe_of_factorization_iff_isGerbeOver, CategoryTheory.IsGerbeOverStackInGroupoids, CategoryTheory.IsGerbeOver.twoFibreProduct, CategoryTheory.IsGerbeOver.comp, CategoryTheory.IsGerbeOver.of_twoFibreProduct, CategoryTheory.Gerbe.exists_sheaf_iso_morPresheaf_self_uliftFunctor
statement: formalized
proof: formalized
---

# 8.11 Gerbes

Section 8.11 of the Stacks Project, [Tag 06NY](https://stacks.math.columbia.edu/tag/06NY). 8 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06NZ, a definition

[Tag 06NZ](https://stacks.math.columbia.edu/tag/06NZ) in the Stacks Project.

**`CategoryTheory.Functor.IsGerbe`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/Defs.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/Defs.lean#L58).

> A *gerbe* over the site `(𝒞, J)` is a category `p : 𝒮 ⥤ 𝒞` over `𝒞` which is a stack in
> groupoids over `𝒞` (Stacks 02ZI), locally nonempty, and locally connected.

```lean
def IsGerbe (p : 𝒮 ⥤ 𝒞) (J : GrothendieckTopology 𝒞) : Prop
```

## Tag 06P0, a lemma

[Tag 06P0](https://stacks.math.columbia.edu/tag/06P0) in the Stacks Project.

**`CategoryTheory.Functor.isGerbe_iff_of_isEquivalenceOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/EquivalenceStack.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/EquivalenceStack.lean#L80).

> **Stacks 06P0.** Let `(𝒞, J)` be a site and let `p : 𝒳 ⥤ 𝒞`, `p' : 𝒳' ⥤ 𝒞` be categories
> over `𝒞` which are equivalent as categories over `𝒞`: `a : 𝒳 ⥤ 𝒳'` is a 1-morphism over `𝒞`
> (`a ⋙ p' = p`) and an equivalence over `𝒞` (its quasi-inverse is strictly over `𝒞` and unit and
> counit are vertical). Then `𝒳` is a gerbe over `(𝒞, J)` (`CategoryTheory.Functor.IsGerbe`,
> Stacks 06NZ) if and only if `𝒳'` is.
>
> As in the source, the stack clause is Stacks 042X,
> `CategoryTheory.Functor.IsStackInGroupoids.iff_of_isEquivalenceOver`, and local nonemptiness and
> local connectedness transport by `isGerbeOver_iff_of_isEquivalenceOver` read through
> `isGerbeOver_id_iff`.

```lean
theorem Functor.isGerbe_iff_of_isEquivalenceOver {J : GrothendieckTopology 𝒞} {p : 𝒳 ⥤ 𝒞}
    {p' : 𝒳' ⥤ 𝒞} {a : 𝒳 ⥤ 𝒳'} (ha : a ⋙ p' = p) (e : Functor.IsEquivalenceOver p p' a) :
    p.IsGerbe.{w} J ↔ p'.IsGerbe.{w} J
```

## Tag 06P1, a lemma

[Tag 06P1](https://stacks.math.columbia.edu/tag/06P1) in the Stacks Project.

**`CategoryTheory.isGerbe_of_factorization_iff_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/WhenGerbe.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/WhenGerbe.lean#L323).

> **Stacks 06P1**. Let `(𝒞, J)` be a site, let `q : 𝒴 ⥤ 𝒞` and `F ⋙ q : 𝒳 ⥤ 𝒞` be stacks in
> groupoids over `𝒞` and let `J𝒴` be the topology on `𝒴` inherited from `(𝒞, J)`. Let
> `F = a ⋙ F'` be a factorization of `F` through an equivalence `a` over `𝒞` with `F'` fibred in
> groupoids — a factorization of exactly the kind Stacks 06N7 produces. Then clause (1) of
> Stacks 06P1 — that `F'` is a gerbe over the site `(𝒴, J𝒴)` — holds exactly when clause (2) does,
> that is exactly when `IsGerbeOver J q F`.
>
> Since the right-hand side does not mention the factorization, this also says that clause (1) holds
> for one such factorization exactly when it holds for every one, which is the source's parenthesis
> "for some (equivalently any)".
>
> The equivalence `a` is asked to be an equivalence over `𝒞`, as the source asks and as Stacks 06N7
> delivers, not over `𝒴`: `CategoryTheory.isGerbeOver_iff_of_isEquivalenceOver`, the relative
> Stacks 06P0, assumes the latter, and 06N7's factorization does not satisfy it — see
> `StacksFrontier.CategoryTheory.Sites.Gerbe.BaseEquivalence`, which supplies the version used here.

```lean
theorem isGerbe_of_factorization_iff_isGerbeOver {𝒳' : Type u₄} [Category.{v₄} 𝒳']
    {F' : 𝒳' ⥤ 𝒴} {a : 𝒳 ⥤ 𝒳'} (ha : a ⋙ F' = F)
    (e : Functor.IsEquivalenceOver (F ⋙ q) (F' ⋙ q) a)
    (hp' : Functor.IsStackInGroupoids.{max u₃ v₃} (F' ⋙ q) J)
    (hq : Functor.IsStackInGroupoids.{max u₃ v₃} q J) (hF' : F'.IsFiberedInGroupoids)
    (hJ𝒴 : Functor.IsInheritedTopology.{max u₃ v₃} q J J𝒴) :
    F'.IsGerbe.{max u₃ v₃} J𝒴 ↔ IsGerbeOver J q F
```

## Tag 06P2, a definition

[Tag 06P2](https://stacks.math.columbia.edu/tag/06P2) in the Stacks Project.

**`CategoryTheory.IsGerbeOverStackInGroupoids`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/InGroupoids.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/InGroupoids.lean#L115).

> **Stacks 06P2.** Let `(𝒞, J)` be a site, let `q : 𝒴 ⥤ 𝒞` and `F ⋙ q : 𝒳 ⥤ 𝒞` be stacks in
> groupoids over `𝒞`, and let `F : 𝒳 ⥤ 𝒴` be the `1`-morphism of categories over `𝒞` between
> them. `𝒳` is a *gerbe over* `𝒴` if the equivalent conditions of Stacks 06P1 hold; this records
> condition (2) of 06P1, `CategoryTheory.IsGerbeOver`:
> (a) for `y` in `𝒴` over `U` there is a covering of `U` along whose members `y|_{U_i}` is
>     isomorphic in `𝒴_{U_i}` to the image of an object of `𝒳` over `U_i`;
> (b) for `x`, `x'` in `𝒳_U` and `b : F(x) ⟶ F(x')` in `𝒴_U` there is a covering of `U` along
>     whose members `b|_{U_i}` is the image of a morphism `x|_{U_i} ⟶ x'|_{U_i}` of `𝒳_{U_i}`.
>
> The two stacks-in-groupoids conditions are the standing hypotheses of the source. Condition (1)
> of Stacks 06P1 is equivalent, by
> `CategoryTheory.isGerbeOverStackInGroupoids_iff_isGerbe_of_factorization`.

```lean
def IsGerbeOverStackInGroupoids (J : GrothendieckTopology 𝒞) (q : 𝒴 ⥤ 𝒞) (F : 𝒳 ⥤ 𝒴) :
    Prop
```

## Tag 06P3, a lemma

[Tag 06P3](https://stacks.math.columbia.edu/tag/06P3) in the Stacks Project.

**`CategoryTheory.IsGerbeOver.twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/Pullback.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/Pullback.lean#L292).

> **Stacks 06P3**. Let `𝒳' = 𝒴' ×_𝒴 𝒳` be the 2-fibre product over `𝒞` of `G : 𝒴' ⥤ 𝒴`
> and `F : 𝒳 ⥤ 𝒴`, where `𝒳` sits over `𝒞` by `F ⋙ q` and `𝒴'` by `G ⋙ q`. If `F` makes `𝒳`
> a gerbe over `𝒴` and `𝒴'` is fibred in groupoids over `𝒞`, then the first projection makes
> `𝒳'` a gerbe over `𝒴'`.
>
> Both local conditions are pulled back along `G`: an object of `𝒳` over a member of a covering
> whose `F`-image is a restriction of `G y'` is the second component of an object of `𝒳'` over
> that member whose first component is a restriction of `y'`, and a morphism of `𝒳` matching
> the `G`-image of `b'` is the second component of a morphism of `𝒳'` whose first component is
> the restriction of `b'`.

```lean
theorem IsGerbeOver.twoFibreProduct {J : GrothendieckTopology 𝒞} (hF : IsGerbeOver J q F)
    (hG : (G ⋙ q).IsFiberedInGroupoids) :
    IsGerbeOver J (G ⋙ q) (fst (G ⋙ q) (F ⋙ q) q G F)
```

## Tag 06R3, a lemma

[Tag 06R3](https://stacks.math.columbia.edu/tag/06R3) in the Stacks Project.

**`CategoryTheory.IsGerbeOver.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/Basic.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/Basic.lean#L175).

> **Stacks 06R3**. If `𝒳` is a gerbe over `𝒴` and `𝒴` is a gerbe over `𝒵`, then `𝒳` is a
> gerbe over `𝒵`.
>
> This is also **Stacks 06R8**, the same statement for morphisms of algebraic stacks: the
> source proves 06R8 by citing 06R3, and an algebraic stack is a category fibred in groupoids
> over the big fppf site, so the two differ only in the generality of the ambient site.

```lean
theorem comp (hF : IsGerbeOver J (G ⋙ r) F) (hG : IsGerbeOver J r G) :
    IsGerbeOver J r (F ⋙ G)
```

## Tag 06P4, a lemma

[Tag 06P4](https://stacks.math.columbia.edu/tag/06P4) in the Stacks Project.

**`CategoryTheory.IsGerbeOver.of_twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/Pullback.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/Pullback.lean#L333).

> **Stacks 06P4**. Let `𝒳' = 𝒴' ×_𝒴 𝒳` be the 2-fibre product over `𝒞` of `G : 𝒴' ⥤ 𝒴`
> and `F : 𝒳 ⥤ 𝒴`. If every object of `𝒴` is locally in the image of `G` — the condition
> `CategoryTheory.IsGerbeOver.locally_essSurj` for `G` — and the first projection makes `𝒳'` a
> gerbe over `𝒴'`, then `F` makes `𝒳` a gerbe over `𝒴`.
>
> This is the converse direction of Stacks 06P3: the two local conditions are descended along
> `G`. For the first, an object `y'` of `𝒴'` whose `G`-image restricts `y` is refined by a
> covering along which `𝒳'` has objects over `y'`, and their second components are objects of
> `𝒳` whose `F`-images restrict `y`. For the second, two restrictions of `x₁` and `x₂` and the
> comparison isomorphisms `G y' ≅ F x₁|_V`, `G y' ≅ F x₂|_V` obtained from `b` assemble into two
> objects of `𝒳'` with the *same* first component `y'`, so that the identity of `y'` is a
> morphism of a fibre between their images; local fullness of the first projection then supplies
> the morphism of `𝒳` wanted.

```lean
theorem IsGerbeOver.of_twoFibreProduct {J : GrothendieckTopology 𝒞} (hq : q.IsFiberedInGroupoids)
    (hFq : (F ⋙ q).IsFiberedInGroupoids)
    (hGsurj : ∀ {U : 𝒞} (y : 𝒴), q.obj y = U → ∃ S ∈ J U,
      ∀ ⦃V : 𝒞⦄ (f : V ⟶ U), S f → ∃ (y' : 𝒴') (ψ : G.obj y' ⟶ y), q.IsHomLift f ψ)
    (h : IsGerbeOver J (G ⋙ q) (fst (G ⋙ q) (F ⋙ q) q G F)) :
    IsGerbeOver J q F
```

## Tag 0CJY, a lemma

[Tag 0CJY](https://stacks.math.columbia.edu/tag/0CJY) in the Stacks Project.

**`CategoryTheory.Gerbe.exists_sheaf_iso_morPresheaf_self_uliftFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/BandedSheaf.lean, line 1158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/BandedSheaf.lean#L1158).

> **Stacks 0CJY, with no hypothesis on the universes.** Let `p : 𝒮 ⥤ 𝒞` be a gerbe over the site
> `(𝒞, J)`: fibred in groupoids, a stack, locally nonempty and locally connected. Assume that for
> every `U` and every object `x` of the fibre `𝒮_U` the sheaf of groups
> `Aut(x) = Isom(x, x) = Mor(x, x)` on `𝒞/U` is abelian, that is that the endomorphisms of every
> object of every fibre commute. Then there are
>
> 1. a sheaf `𝒢` of abelian groups on `𝒞`, and
> 2. for every `U` and every object `x` of `𝒮_U` an isomorphism `θ x : 𝒢|_U ≅ Aut(x)` of sheaves of
>    groups on `𝒞/U`, that is an isomorphism of presheaves whose components are multiplicative,
>
> such that for every `U` and every morphism `φ : x ⟶ y` of `𝒮_U` conjugation by `φ` carries `θ x` to
> `θ y`: on sections over `g : V ⟶ U` one has `θ y a = φ|_V ∘ θ x a ∘ (φ|_V)⁻¹`.
>
> `𝒢` is the band, `CategoryTheory.Gerbe.Band`, which lives in `Type (max u₁ v₁ v₂)` and not in the
> universe `v₂` of `Aut(x)`; the isomorphism of (2) is therefore stated against the universe lift of
> `Aut(x)`, which is what makes the statement true in every universe. See
> `CategoryTheory.Gerbe.exists_sheaf_iso_morPresheaf_self` for the unlifted form, which needs
> `UnivLE.{max u₁ v₁, v₂}` and is false without it.

```lean
public theorem exists_sheaf_iso_morPresheaf_self_uliftFunctor (p : 𝒮 ⥤ 𝒞)
    (J : GrothendieckTopology 𝒞) (hp : p.IsFiberedInGroupoids) (hst : p.IsStack J)
    (hne : p.LocallyNonempty J) (hlc : p.LocallyConnected J)
    (habel : ∀ (U : 𝒞) (x : p.Fiber U) (α β : x ⟶ x), α ≫ β = β ≫ α) :
    haveI : p.IsFibered := hp.isFibered
    haveI : ∀ U : 𝒞, IsGroupoid (p.Fiber U) := hp.fiber_isGroupoid
    ∃ (𝒢 : Sheaf J CommGrpCat.{max u₁ v₁ v₂})
      (θ : ∀ (U : 𝒞) (x : p.Fiber U),
        (Over.forget U).op ⋙ 𝒢.obj ⋙ forget CommGrpCat.{max u₁ v₁ v₂} ≅
          p.morPresheaf x x ⋙ uliftFunctor.{max u₁ v₁, v₂}),
      (∀ (U : 𝒞) (x : p.Fiber U) (g : Over U) (a b : 𝒢.obj.obj (op g.left)),
          ((θ U x).hom.app (op g) (a * b)).down =
            ((θ U x).hom.app (op g) a).down ≫ ((θ U x).hom.app (op g) b).down) ∧
        ∀ (U : 𝒞) (x y : p.Fiber U) (φ : x ⟶ y) (g : Over U) (a : 𝒢.obj.obj (op g.left)),
          ((θ U y).hom.app (op g) a).down =
            pullbackFiberHom (CategoryTheory.inv φ) g.hom ≫ ((θ U x).hom.app (op g) a).down ≫
              pullbackFiberHom φ g.hom
```

**`CategoryTheory.Gerbe.exists_sheaf_iso_morPresheaf_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/BandedSheaf.lean, line 1196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/BandedSheaf.lean#L1196).

> **Stacks 0CJY.** Let `p : 𝒮 ⥤ 𝒞` be a gerbe over the site `(𝒞, J)` whose automorphism sheaves
> are abelian. Then there are a sheaf `𝒢` of abelian groups on `𝒞` and, for every `U` and every
> object `x` of the fibre `𝒮_U`, an isomorphism `θ x : 𝒢|_U ≅ Aut(x)` of sheaves of groups on `𝒞/U`,
> and these are compatible with conjugation.
>
> The hypothesis `UnivLE.{max u₁ v₁, v₂}` is what makes `𝒢` exist in the universe `v₂` of the
> morphisms of `𝒮`, and it cannot be dropped: `Type 0`-many copies of a nontrivial `ℤ/2`-gerbe give a
> band whose sections at the top object have cardinality `2 ^ |Type 0|`, which is the cardinality of
> no `Type 0`. Without it the statement still holds in the form
> `CategoryTheory.Gerbe.exists_sheaf_iso_morPresheaf_self_uliftFunctor`, with `Aut(x)` lifted into
> the universe `𝒢` is valued in.

```lean
public theorem exists_sheaf_iso_morPresheaf_self [UnivLE.{max u₁ v₁, v₂}] (p : 𝒮 ⥤ 𝒞)
    (J : GrothendieckTopology 𝒞) (hp : p.IsFiberedInGroupoids) (hst : p.IsStack J)
    (hne : p.LocallyNonempty J) (hlc : p.LocallyConnected J)
    (habel : ∀ (U : 𝒞) (x : p.Fiber U) (α β : x ⟶ x), α ≫ β = β ≫ α) :
    haveI : p.IsFibered := hp.isFibered
    haveI : ∀ U : 𝒞, IsGroupoid (p.Fiber U) := hp.fiber_isGroupoid
    ∃ (𝒢 : Sheaf J CommGrpCat.{v₂})
      (θ : ∀ (U : 𝒞) (x : p.Fiber U),
        (Over.forget U).op ⋙ 𝒢.obj ⋙ forget CommGrpCat.{v₂} ≅ p.morPresheaf x x),
      (∀ (U : 𝒞) (x : p.Fiber U) (g : Over U) (a b : 𝒢.obj.obj (op g.left)),
          (θ U x).hom.app (op g) (a * b) =
            (θ U x).hom.app (op g) a ≫ (θ U x).hom.app (op g) b) ∧
        ∀ (U : 𝒞) (x y : p.Fiber U) (φ : x ⟶ y) (g : Over U) (a : 𝒢.obj.obj (op g.left)),
          (θ U y).hom.app (op g) a =
            pullbackFiberHom (CategoryTheory.inv φ) g.hom ≫ (θ U x).hom.app (op g) a ≫
              pullbackFiberHom φ g.hom
```

**`CategoryTheory.Gerbe.exists_sheaf_iso_morPresheaf_self_uliftFunctor_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/BandedSheaf.lean, line 1240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/BandedSheaf.lean#L1240).

> **Stacks 0CJY, with the compatibility of the comparisons over varying base object.** Let
> `p : 𝒮 ⥤ 𝒞` be a gerbe over the site `(𝒞, J)` whose automorphism sheaves are abelian. Then there
> are a sheaf `𝒢` of abelian groups on `𝒞` and, for every `U` and every object `x` of the fibre
> `𝒮_U`, an isomorphism `θ x : 𝒢|_U ≅ Aut(x)` of sheaves of groups on `𝒞/U`, such that
>
> 1. each `θ x` is multiplicative on sections,
> 2. for `φ : x ⟶ y` in `𝒮_U`, conjugation by `φ` carries `θ x` to `θ y`, and
> 3. `θ x` read on sections over `g : Over U` is `θ (x|_g)` read on sections over the identity of
>    `g.left`, conjugated by the contraction of the chosen pullback along that identity.
>
> Clauses (1) and (2) are the conclusion of Stacks 0CJY as the source states it, so this is
> `CategoryTheory.Gerbe.exists_sheaf_iso_morPresheaf_self_uliftFunctor` with (3) added. Clause (3)
> is the compatibility of the local comparisons over varying `U` whose verification the source's
> proof omits; for the band it is `CategoryTheory.Gerbe.Band.fiberHom_pullbackFiber_base`, the
> naturality of a band section. It is what makes "the sheaf of abelian groups constructed in Stacks
> 0CJY" pin `𝒢` down well enough to use it as the coefficient sheaf of Stacks 0CK0, so that no
> hypothesis of
> `CategoryTheory.Gerbe.exists_band_nonempty_fiber_of_cohomology_vanishing` has to be assumed.

```lean
public theorem exists_sheaf_iso_morPresheaf_self_uliftFunctor_base (p : 𝒮 ⥤ 𝒞)
    (J : GrothendieckTopology 𝒞) (hp : p.IsFiberedInGroupoids) (hst : p.IsStack J)
    (hne : p.LocallyNonempty J) (hlc : p.LocallyConnected J)
    (habel : ∀ (U : 𝒞) (x : p.Fiber U) (α β : x ⟶ x), α ≫ β = β ≫ α) :
    haveI : p.IsFibered := hp.isFibered
    haveI : ∀ U : 𝒞, IsGroupoid (p.Fiber U) := hp.fiber_isGroupoid
    ∃ (𝒢 : Sheaf J CommGrpCat.{max u₁ v₁ v₂})
      (θ : ∀ (U : 𝒞) (x : p.Fiber U),
        (Over.forget U).op ⋙ 𝒢.obj ⋙ forget CommGrpCat.{max u₁ v₁ v₂} ≅
          p.morPresheaf x x ⋙ uliftFunctor.{max u₁ v₁, v₂}),
      (∀ (U : 𝒞) (x : p.Fiber U) (g : Over U) (a b : 𝒢.obj.obj (op g.left)),
          ((θ U x).hom.app (op g) (a * b)).down =
            ((θ U x).hom.app (op g) a).down ≫ ((θ U x).hom.app (op g) b).down) ∧
        (∀ (U : 𝒞) (x y : p.Fiber U) (φ : x ⟶ y) (g : Over U) (a : 𝒢.obj.obj (op g.left)),
          ((θ U y).hom.app (op g) a).down =
            pullbackFiberHom (CategoryTheory.inv φ) g.hom ≫ ((θ U x).hom.app (op g) a).down ≫
              pullbackFiberHom φ g.hom) ∧
        ∀ (U : 𝒞) (x : p.Fiber U) (g : Over U) (a : 𝒢.obj.obj (op g.left)),
          ((θ U x).hom.app (op g) a).down =
            (pullbackFiberIdIso (pullbackFiber p x g.hom)).inv ≫
              ((θ g.left (pullbackFiber p x g.hom)).hom.app (op (Over.mk (𝟙 g.left))) a).down ≫
                (pullbackFiberIdIso (pullbackFiber p x g.hom)).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.11, Tag 06NY](https://stacks.math.columbia.edu/tag/06NY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
