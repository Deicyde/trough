---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsParasitic, AlgebraicGeometry.Stack.isParasitic_of_isFlat_isLfp_jointlySurjective, AlgebraicGeometry.Stack.isParasitic_modulePresheafPullbackOfHom, AlgebraicGeometry.Stack.isParasitic_of_mono, AlgebraicGeometry.Stack.isParasitic_X₂_of_shortExact, AlgebraicGeometry.Stack.isParasitic_of_epi, AlgebraicGeometry.Stack.isSerreClass_parasiticModules, AlgebraicGeometry.Stack.isParasitic_sheafification
statement: formalized
proof: formalized
---

# 103.9 Parasitic modules

Section 103.9 of the Stacks Project, [Tag 0772](https://stacks.math.columbia.edu/tag/0772). 4 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0773, a definition

[Tag 0773](https://stacks.math.columbia.edu/tag/0773) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsParasitic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticModules.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticModules.lean#L64). The attribute's comment: “parasitic”.

> **Stacks 0773.** A presheaf of modules over the structure sheaf of one of the sites
> associated with an algebraic stack `𝒳` is *parasitic* when its module of sections at every flat
> object of `𝒳` vanishes — an object being flat, as in **Stacks 0787**, when the 1-morphism it
> names out of the scheme it lies over is flat.

```lean
abbrev IsParasitic
    (F : PresheafOfModules.{t}
      (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids τ).obj) : Prop
```

## Tag 0774, a lemma

[Tag 0774](https://stacks.math.columbia.edu/tag/0774) in the Stacks Project.

**`AlgebraicGeometry.Stack.isParasitic_of_isFlat_isLfp_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticFlatDescent.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticFlatDescent.lean#L89). The attribute's comment: “part (4): an fppf sheaf of modules whose inverse images along a jointly surjective family of flat, locally finitely presented 1-morphisms of algebraic stacks are all parasitic is parasitic”.

> **Stacks 0774** (4). Let `f j : 𝒳 j ⟶ 𝒴` be a jointly surjective family of flat, locally
> finitely presented 1-morphisms of algebraic stacks over `S`, and let `ℱ` be a sheaf of
> `𝒪_𝒴`-modules on the fppf site of `𝒴`. If every inverse image `(f j)^*ℱ` is parasitic, then `ℱ`
> is parasitic.
>
> At a flat object `y` of `𝒴` the covering of
> `AlgebraicGeometry.Stack.exists_fppfCovering_family_flatObject_lift` supplies an fppf covering
> family of `y` by objects `f (a i)(x_i)` with `x_i` a *flat* object of `𝒳 (a i)`; the sections of
> `ℱ` there are the sections of `(f (a i))^*ℱ` at `x_i`, which vanish, and a sheaf is
> separated.

```lean
theorem isParasitic_of_isFlat_isLfp_jointlySurjective {J : Type v}
    {𝒳 : J → AlgebraicStacks.{u, w} B S hS} {𝒴 : AlgebraicStacks.{u, w} B S hS}
    (f : ∀ j, 𝒳 j ⟶ 𝒴)
    (hflat : ∀ j, AlgebraicStacks.IsFlat B S hS (f j))
    (hlfp : ∀ j, AlgebraicStacks.IsLocallyOfFinitePresentation B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒴)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (F : SheafOfModules.{t}
      (FibredSite.ringStructureSheafCore B S hS 𝒴.val.val.p
        𝒴.val.isFiberedInGroupoids SiteKind.fppf))
    (hF : ∀ j, IsParasitic B S hS (𝒳 j) SiteKind.fppf
      ((modulePresheafPullbackOfHom.{u, w, t} B S hS (f j) SiteKind.fppf).obj F.val)) :
    IsParasitic B S hS 𝒴 SiteKind.fppf F.val
```

**`AlgebraicGeometry.Stack.isParasitic_modulePresheafPullbackOfHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticPullback.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticPullback.lean#L127). The attribute's comment: “part (1): the inverse image of a parasitic presheaf of modules along a flat 1-morphism of algebraic stacks is parasitic”.

> **Stacks 0774** (1). If `F` is a parasitic presheaf of `𝒪_𝒳`-modules and `g : 𝒴 ⟶ 𝒳` is a
> flat 1-morphism of algebraic stacks, then the inverse image `g^*F` is a parasitic presheaf of
> `𝒪_𝒴`-modules.
>
> Let `y` be an object of `𝒴` lying over a scheme `V` for which `y : V → 𝒴` is flat. Then
> `g y : V → 𝒴 → 𝒳` is flat, being a composite of flat 1-morphisms (**Stacks 06PX**), so `F`
> vanishes at `g y` by hypothesis. The sections of `g^*F` at `y` are the sections of `F` at
> `g y`, whence the conclusion.

```lean
theorem isParasitic_modulePresheafPullbackOfHom
    (hg : AlgebraicStacks.IsFlat B S hS g)
    (F : PresheafOfModules.{t}
      (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids τ).obj)
    (hF : IsParasitic B S hS 𝒳 τ F) :
    IsParasitic B S hS 𝒴 τ
      ((modulePresheafPullbackOfHom.{u, w, t} B S hS g τ).obj F)
```

**`AlgebraicGeometry.Stack.isParasitic_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticSerreSubcategory.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticSerreSubcategory.lean#L181). The attribute's comment: “part (2)(b), the closure under submodules: a submodule of a parasitic module is parasitic”.

> **Stacks 0774** (2)(b), the closure under submodules. A submodule of a parasitic module on
> one of the sites associated with an algebraic stack is parasitic.
>
> It is immediate from the definition, as the source says: a monomorphism of sheaves of modules is
> injective on sections, so at a flat object the sections of the submodule inject into the
> vanishing sections of the ambient module.

```lean
theorem isParasitic_of_mono
    {F' F : SheafOfModules.{t}
      (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids τ)}
    (i : F' ⟶ F) [Mono i] (hF : IsParasitic B S hS 𝒳 τ F.val) :
    IsParasitic B S hS 𝒳 τ F'.val
```

**`AlgebraicGeometry.Stack.isParasitic_X₂_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticSerreSubcategory.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticSerreSubcategory.lean#L205). The attribute's comment: “part (2)(b), the closure under extensions: the middle term of a short exact sequence of modules whose outer terms are parasitic is parasitic”.

> **Stacks 0774** (2)(b), the closure under extensions. Given a short exact sequence
> `0 → F₁ → F₂ → F₃ → 0` of modules on one of the sites associated with an algebraic stack, with
> `F₁` and `F₃` parasitic, the module `F₂` is parasitic.
>
> This is the source's "evaluate on `x` lying over a scheme flat over `𝒳`": at a flat object the
> sections of `F₁` and of `F₃` vanish, and taking sections is left exact, so the sections of `F₂`
> vanish too.

```lean
theorem isParasitic_X₂_of_shortExact
    {Sq : ShortComplex (SheafOfModules.{t}
      (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids τ))}
    (hSq : Sq.ShortExact)
    (h₁ : IsParasitic B S hS 𝒳 τ Sq.X₁.val) (h₃ : IsParasitic B S hS 𝒳 τ Sq.X₃.val) :
    IsParasitic B S hS 𝒳 τ Sq.X₂.val
```

**`AlgebraicGeometry.Stack.isParasitic_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticSerreSubcategory.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticSerreSubcategory.lean#L237). The attribute's comment: “part (2)(b), the closure under quotients: a quotient of a parasitic module is parasitic”.

> **Stacks 0774** (2)(b), the closure under quotients. If `p : F ⟶ G` is an epimorphism of
> modules on one of the sites associated with an algebraic stack and `F` is parasitic, then `G` is
> parasitic.
>
> An epimorphism of sheaves of modules is locally surjective, so this is
> `AlgebraicGeometry.Stack.isParasitic_of_isLocallySurjective`: at a flat object every section of
> `G` comes from a section of `F` on a covering, and that covering may be refined by one whose
> sources are again flat objects, where `F` vanishes.

```lean
theorem isParasitic_of_epi
    {F G : SheafOfModules.{t}
      (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids τ)}
    (p : F ⟶ G) [Epi p] (hF : IsParasitic B S hS 𝒳 τ F.val) :
    IsParasitic B S hS 𝒳 τ G.val
```

**`AlgebraicGeometry.Stack.isSerreClass_parasiticModules`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticSerreSubcategory.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticSerreSubcategory.lean#L255). The attribute's comment: “part (2)(b): the parasitic modules are a Serre subcategory of Mod(𝒳\_τ, 𝒪\_𝒳)”.

> **Stacks 0774** (2)(b). The full subcategory of `Mod(𝒳_τ, 𝒪_𝒳)` consisting of the parasitic
> modules is a Serre subcategory: it contains a zero object and is closed under submodules, under
> quotients and under extensions, which are the four instances above.

```lean
instance isSerreClass_parasiticModules :
    (parasiticModules.{u, w, t} B S hS 𝒳 τ).IsSerreClass
```

**`AlgebraicGeometry.Stack.isParasitic_sheafification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticSheafification.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticSheafification.lean#L133). The attribute's comment: “part (2)(a): the τ-sheafification of a parasitic presheaf of modules is parasitic”.

> **Stacks 0774** (2)(a). The `τ`-sheafification of a parasitic presheaf of
> `𝒪_𝒳`-modules is parasitic, for each of the five topologies `τ` of **Stacks 06TP**.
>
> The map from a presheaf of modules to its sheafification is locally surjective, so this is
> `AlgebraicGeometry.Stack.isParasitic_of_isLocallySurjective`.

```lean
theorem isParasitic_sheafification
    (F : PresheafOfModules.{t}
      (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids τ).obj)
    (hF : IsParasitic B S hS 𝒳 τ F) :
    IsParasitic B S hS 𝒳 τ
      ((PresheafOfModules.sheafification.{t}
        (𝟙 (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
          𝒳.val.isFiberedInGroupoids τ).obj)).obj F).val
```

**`AlgebraicGeometry.Stack.isParasitic_of_isSmooth_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticSmoothDescent.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticSmoothDescent.lean#L186). The attribute's comment: “part (3): an étale sheaf of modules whose inverse images along a jointly surjective family of smooth 1-morphisms of algebraic stacks are all parasitic is parasitic”.

> **Stacks 0774** (3). Let `f j : 𝒳 j ⟶ 𝒴` be a jointly surjective family of smooth
> 1-morphisms of algebraic stacks over `S`, and let `ℱ` be a sheaf of `𝒪_𝒴`-modules on the étale
> site of `𝒴`. If every inverse image `(f j)^*ℱ` is parasitic, then `ℱ` is parasitic.
>
> At a flat object `y` of `𝒴`, every point of the scheme `y` lies over is hit by a smooth morphism
> `m` of the site carrying a lift of `y` to some `𝒳 j` which is a *flat* object there
> (`AlgebraicGeometry.Stack.exists_flatObject_lift_of_isSmooth_at_point`), so the sections of `ℱ`
> restrict to zero along the comparison morphism. Refining `m` by an étale morphism factoring
> through it (**Stacks 055U**) and taking a cartesian lift of the comparison morphism gives an
> *étale* covering family of `y` along every member of which the sections of `ℱ` restrict to zero;
> `ℱ` is an étale sheaf, hence separated, so they vanish.

```lean
theorem isParasitic_of_isSmooth_jointlySurjective {J : Type v}
    {𝒳 : J → AlgebraicStacks.{u, w} B S hS} {𝒴 : AlgebraicStacks.{u, w} B S hS}
    (f : ∀ j, 𝒳 j ⟶ 𝒴)
    (hsmooth : ∀ j, AlgebraicStacks.IsSmooth B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒴)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (F : SheafOfModules.{t}
      (FibredSite.ringStructureSheafCore B S hS 𝒴.val.val.p
        𝒴.val.isFiberedInGroupoids SiteKind.etale))
    (hF : ∀ j, IsParasitic B S hS (𝒳 j) SiteKind.etale
      ((modulePresheafPullbackOfHom.{u, w, t} B S hS (f j) SiteKind.etale).obj F.val)) :
    IsParasitic B S hS 𝒴 SiteKind.etale F.val
```

## Tag 0775, a lemma

[Tag 0775](https://stacks.math.columbia.edu/tag/0775) in the Stacks Project.

**`AlgebraicGeometry.Stack.isZero_fppfModuleCohomology_of_isParasitic_atSchemeUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticCohomologyVanishingAtSchemeUniverse.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticCohomologyVanishingAtSchemeUniverse.lean#L66). The attribute's comment: “part (1) for τ = fppf at the module universe u of the schemes: H^i(𝒳, ℱ) = 0 for a parasitic ℱ, with H^i = Ext^i(𝒪\_𝒳, -) as in FlatFppf.fppfModuleCohomology”.

> **Stacks 0775** part (1), for the fppf topology, at the module universe `u` of the schemes.
> Let `𝒳` be an algebraic stack and `ℱ` a parasitic sheaf of `𝒪_𝒳`-modules (**Stacks 0773**).
> Then `H^i(𝒳, ℱ) = 0` for every `i`, where `H^i(𝒳, -)` is
> `AlgebraicGeometry.Stack.FlatFppf.fppfModuleCohomology`, `Ext^i` out of the structure sheaf, in
> any universe `t` of `Ext`-groups.
>
> The instance argument `HasExt.{t}` is not a hypothesis on `ℱ`: `fppfModuleCohomology.{u, w, t}`
> is only defined in its presence. At `t = u` it is supplied by the Grothendieck abelian structure
> (`AlgebraicGeometry.Stack.isGrothendieckAbelian_fppfModules`), which is
> `AlgebraicGeometry.Stack.isZero_fppfModuleCohomology_of_isParasitic_ofGrothendieck`.
>
> By `AlgebraicGeometry.Stack.fppfModuleCohomologyULiftIso` this is the vanishing of `Ext^i` out of
> the lifted structure sheaf of the universe lift of `ℱ`, which is parasitic as `ℱ` is, and that
> is `AlgebraicGeometry.Stack.isZero_ext_uliftUnit_of_isParasitic`.

```lean
theorem isZero_fppfModuleCohomology_of_isParasitic_atSchemeUniverse
    {𝒳 : AlgebraicStacks.{u, w} B S hS} [HasExt.{t} (fppfModules B S hS 𝒳)]
    (N : fppfModules B S hS 𝒳) (hN : IsParasitic B S hS 𝒳 .fppf N.val) (i : ℕ) :
    IsZero ((FlatFppf.fppfModuleCohomology.{u, w, t} B S hS 𝒳 i).obj N)
```

**`AlgebraicGeometry.Stack.isZero_ext_unit_of_isParasitic_atSchemeUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticCohomologyVanishingAtSchemeUniverse.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticCohomologyVanishingAtSchemeUniverse.lean#L110). The attribute's comment: “part (1) for τ the étale or the fppf topology, at the module universe u of the schemes: H^i\_τ(𝒳, ℱ) = Ext^i(𝒪\_𝒳, ℱ) = 0 for a parasitic ℱ”.

> **Stacks 0775** part (1), for `τ` the étale or the fppf topology, at the module universe `u` of
> the schemes. Let `𝒳` be an algebraic stack and `ℱ` a parasitic sheaf of `𝒪_𝒳`-modules on `𝒳_τ`
> (**Stacks 0773**). Then `H^i_τ(𝒳, ℱ) = Ext^i(𝒪_𝒳, ℱ) = 0` for every `i`, for `Ext`-groups in any
> universe `t`.
>
> The instance argument `HasExt.{t}` is not a hypothesis on `ℱ`: it is what makes `Ext`-groups in
> the universe `t` exist at all, and it is always available at `t = u`, the category of modules
> being Grothendieck abelian (`AlgebraicGeometry.Stack.isGrothendieckAbelian_moduleRingSheaf`, see
> `AlgebraicGeometry.Stack.isZero_ext_unit_of_isParasitic_atSchemeUniverse_ofGrothendieck`).
>
> By `AlgebraicGeometry.Stack.isZero_ext_unit_iff_isZero_ext_uliftUnit` this is the vanishing of
> `Ext^i` out of the lifted structure sheaf of the universe lift of `ℱ`, which is parasitic as `ℱ`
> is, and that is `AlgebraicGeometry.Stack.isZero_ext_uliftUnit_of_isParasitic`.

```lean
theorem isZero_ext_unit_of_isParasitic_atSchemeUniverse {τ : SiteKind}
    (hτ : τ = .etale ∨ τ = .fppf) {𝒳 : AlgebraicStacks.{u, w} B S hS}
    [HasExt.{t} (SheafOfModules.{u}
      (Stacks.RelativeCech.moduleRingSheaf B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids τ))]
    (N : SheafOfModules.{u}
      (Stacks.RelativeCech.moduleRingSheaf B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids τ))
    (hN : IsParasitic B S hS 𝒳 τ N.val) (i : ℕ) :
    IsZero ((extFunctorObj.{t} (SheafOfModules.unit _) i).obj N)
```

**`AlgebraicGeometry.Stack.isZero_ext_uliftUnit_of_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticFlatSubsiteCohomology.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticFlatSubsiteCohomology.lean#L218). The attribute's comment: “part (1), for τ the étale or the fppf topology, with no hypothesis: H^i\_τ(𝒳, ℱ) = 0 for a parasitic ℱ, at the module universe u + 1 of the objects of the site”.

> **Stacks 0775** part (1). Let `𝒳` be an algebraic stack, let `τ` be the étale or the fppf
> topology, and let `ℱ` be a parasitic sheaf of `𝒪_𝒳`-modules on `𝒳_τ` (**Stacks 0773**). Then
> `H^i_τ(𝒳, ℱ) = 0` for all `i`.
>
> The modules have their sections in the universe `u + 1` of the objects of the site, where the
> structure sheaf `𝒪_𝒳` is a module through its universe lift `Stacks.SheafOfModules.uliftUnit`
> and `H^i_τ(𝒳, -) = Ext^i(𝒪_𝒳, -)`, in any universe `t` of `Ext`-groups. By **Stacks 03FD** this
> is the cohomology of the underlying abelian sheaf
> (`Stacks.Cohomology.ULiftUnitComparison.extULiftUnitIso`), which vanishes because that sheaf
> vanishes at the flat objects (`AlgebraicGeometry.Stack.isZero_functorH_of_subsingleton_flatObject`,
> from the cohomology comparison of **Stacks 07AK** along the inclusion of the flat objects).

```lean
theorem isZero_ext_uliftUnit_of_isParasitic (hτ : τ = .etale ∨ τ = .fppf)
    [HasExt.{t} (SheafOfModules.{u + 1}
      (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids τ))]
    (F : SheafOfModules.{u + 1}
      (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids τ))
    (hF : IsParasitic B S hS 𝒳 τ F.val) (i : ℕ) :
    IsZero ((extFunctorObj.{t} (Stacks.SheafOfModules.uliftUnit.{u + 1}
      (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids τ))
        i).obj F)
```

**`AlgebraicGeometry.Stack.isParasitic_moduleSheafHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticHigherDirectImage.lean, line 407](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticHigherDirectImage.lean#L407). The attribute's comment: “part (2), for τ the étale or the fppf topology, at the module universe u + 1 of the objects of the site: R^if\_*ℱ is parasitic for a parasitic ℱ”.

> **Stacks 0775 (2) at the module universe `u + 1` of the objects of the site.** Let
> `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks, `τ` the étale or the fppf topology, and `ℱ` a
> parasitic sheaf of `𝒪_𝒳`-modules on `𝒳_τ` (**Stacks 0773**). Then every higher direct image
> `R^nf_*ℱ` (**Stacks 06WE**, `AlgebraicGeometry.Stack.moduleSheafHigherDirectImage`) is a
> parasitic sheaf of `𝒪_𝒴`-modules.
>
> This is `AlgebraicGeometry.Stack.isParasitic_rightDerived_stackModuleDirectImageSucc` moved along
> `AlgebraicGeometry.AlgebraicStacks.moduleDirectImageRightDerivedIso`.

```lean
theorem isParasitic_moduleSheafHigherDirectImage (hτ : τ = .etale ∨ τ = .fppf)
    (N : SheafOfModules.{u + 1} (Stacks.RelativeCech.moduleRingSheaf B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids τ)) (hN : IsParasitic B S hS 𝒳 τ N.val) (n : ℕ) :
    IsParasitic B S hS 𝒴 τ ((moduleSheafHigherDirectImage.{u, u + 1, u, u + 1, u} B S hS
      𝒳.val.val.p 𝒴.val.val.p 𝒳.val.isFiberedInGroupoids 𝒴.val.isFiberedInGroupoids
      (CatFiberedInGroupoids.homFunctor k.hom) (CatFiberedInGroupoids.homFunctor_comp_p k.hom)
      (B.baseTopology τ) (B.baseTopology_le_topology τ) n).obj N).val
```

**`AlgebraicGeometry.Stack.isParasitic_stackModuleHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticHigherDirectImage.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticHigherDirectImage.lean#L431). The attribute's comment: “part (2), for τ the étale or the fppf topology, at the module universe u of the schemes: R^if\_*ℱ is parasitic for a parasitic ℱ”.

> **Stacks 0775 (2)**, for `τ` the étale or the fppf topology, at the module universe `u` of the
> schemes. Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks and `ℱ` a parasitic sheaf of
> `𝒪_𝒳`-modules on `𝒳_τ` (**Stacks 0773**). Then every higher direct image `R^nf_*ℱ`
> (`AlgebraicGeometry.Stack.stackModuleHigherDirectImage`) is parasitic.
>
> The universe lift carries `R^nf_*ℱ` to `R^nf_*` at `u + 1` of the lift of `ℱ`
> (`AlgebraicGeometry.Stack.stackModuleHigherDirectImageULiftIso`), the lift of a parasitic module
> is parasitic, and at `u + 1` this is
> `AlgebraicGeometry.Stack.isParasitic_moduleSheafHigherDirectImage`.

```lean
theorem isParasitic_stackModuleHigherDirectImage (hτ : τ = .etale ∨ τ = .fppf)
    (N : SheafOfModules.{u} (Stacks.RelativeCech.moduleRingSheaf B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids τ)) (hN : IsParasitic B S hS 𝒳 τ N.val) (n : ℕ) :
    IsParasitic B S hS 𝒴 τ ((stackModuleHigherDirectImage B S hS k τ n).obj N).val
```

**`AlgebraicGeometry.Stack.isParasitic_fppfModulesHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticHigherDirectImage.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticHigherDirectImage.lean#L446). The attribute's comment: “part (2) for τ = fppf at the module universe u of the schemes: R^if\_*ℱ is parasitic for a parasitic ℱ, with R^if\_* as in fppfModulesHigherDirectImage”.

> **Stacks 0775 (2) for the fppf topology at the module universe `u`**: for every 1-morphism
> `f : 𝒳 ⟶ 𝒴` of algebraic stacks, the higher direct images
> `AlgebraicGeometry.Stack.fppfModulesHigherDirectImage` of a parasitic module are parasitic. This
> is `AlgebraicGeometry.Stack.isParasitic_stackModuleHigherDirectImage` at `τ = fppf`.

```lean
theorem isParasitic_fppfModulesHigherDirectImage
    (N : SheafOfModules.{u} (Stacks.RelativeCech.moduleRingSheaf B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids .fppf)) (hN : IsParasitic B S hS 𝒳 .fppf N.val) (n : ℕ) :
    IsParasitic B S hS 𝒴 .fppf ((fppfModulesHigherDirectImage B S hS k n).obj N).val
```

## Tag 0776, a lemma

[Tag 0776](https://stacks.math.columbia.edu/tag/0776) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.tfae_exact_isParasitic_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ExactParasiticHomology.lean, line 514](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ExactParasiticHomology.lean#L514).

> **Stacks 0776.** Let `𝒳` be an algebraic stack and let `α : 𝓕 ⟶ 𝓖` and `β : 𝓖 ⟶ 𝓗` be maps in
> `QCoh(𝒪_𝒳)` with `β ∘ α = 0`. The following are equivalent:
>
> 1. in the abelian category `QCoh(𝒪_𝒳)` the complex `𝓕 ⟶ 𝓖 ⟶ 𝓗` is exact at `𝓖`;
> 2. `Ker(β)/Im(α)` computed in `Mod(𝒳_étale, 𝒪_𝒳)` is parasitic;
> 3. `Ker(β)/Im(α)` computed in `Mod(𝒳_fppf, 𝒪_𝒳)` is parasitic.
>
> The abelian structure of `QCoh(𝒪_𝒳)` is
> `AlgebraicGeometry.Stack.AlgebraicStacks.instAbelianQuasicoherentModules`; `Ker(β)/Im(α)`
> computed in `Mod(𝒳_τ, 𝒪_𝒳)` is the homology of the complex `𝓕 ⟶ 𝓖 ⟶ 𝓗` regarded as a complex of
> sheaves of modules on the site of `τ` (**Stacks 06TP**), and parasitic is **Stacks 0773**.

```lean
theorem tfae_exact_isParasitic_homology {F G H : quasicoherentModules B S hS 𝒳} (α : F ⟶ G)
    (β : G ⟶ H) (w : α ≫ β = 0) :
    List.TFAE [(ShortComplex.mk α β w).Exact,
      IsParasitic B S hS 𝒳 .etale ((ShortComplex.mk α β w).map
        (FibredSite.toSiteModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
          .etale)).homology.val,
      IsParasitic B S hS 𝒳 .fppf ((ShortComplex.mk α β w).map
        (FibredSite.toSiteModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
          .fppf)).homology.val]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.9, Tag 0772](https://stacks.math.columbia.edu/tag/0772)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
