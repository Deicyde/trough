---
declaration: section
origin: cited
lean: PresheafOfModules.pushforward₀Obj, PresheafOfModules.pushforward₀, PresheafOfModules.map_smul, Stacks.PresheafOfModules.Pullback.pullback_presheaf_module, Stacks.PresheafOfModules.Pullback.pullbackModuleFunctor, Stacks.PresheafOfModules.Pullback.pullbackModuleFunctorCompToPresheaf, Stacks.PresheafOfModules.Pullback.pullbackModuleAdjunction, Stacks.PresheafOfModules.Pullback.toPresheaf_map_pullbackModuleAdjunction_homEquiv
statement: formalized
proof: formalized
---

# 6.24 Continuous maps and sheaves of modules

Section 6.24 of the Stacks Project, [Tag 008R](https://stacks.math.columbia.edu/tag/008R). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 008S, a lemma

[Tag 008S](https://stacks.math.columbia.edu/tag/008S) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModules.pushforward₀Obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.pushforward₀Obj#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Module/PushforwardPresheaf.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/PushforwardPresheaf.lean#L30) (StacksFrontier): “the pushforward `f_*ℱ` as a presheaf of `f_*𝒪`-modules”.
- [`PresheafOfModules.pushforward₀`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.pushforward₀#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Module/PushforwardPresheaf.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/PushforwardPresheaf.lean#L32) (StacksFrontier): “pushforward as a functor `PMod(𝒪) ⥤ PMod(f_*𝒪)`”.
- [`PresheafOfModules.map_smul`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.map_smul#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Module/PushforwardPresheaf.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/PushforwardPresheaf.lean#L34) (StacksFrontier): “the scalar action is compatible with restriction, which is the naturality of the map `f_*𝒪 × f_*ℱ ⟶ f_*ℱ`”. References: SGA 3 I (6.4), “more general”.

## Tag 008T, a lemma

[Tag 008T](https://stacks.math.columbia.edu/tag/008T) in the Stacks Project.

**`Stacks.PresheafOfModules.Pullback.pullback_presheaf_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/PullbackPresheaf.lean, line 629](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/PullbackPresheaf.lean#L629). The attribute's comment: “(1), (2)”.

> **Stacks 008T (1), (2).**
>
> Let `O` be a presheaf of rings on `Y` and `G` a presheaf of `O`-modules. Then the
> pullback presheaf of abelian groups `f_p G` carries the structure of a presheaf of
> `f_p O`-modules: there is a presheaf of `f_p O`-modules `M` whose underlying presheaf of
> abelian groups is exactly `f_p G`.
>
> The data of `M : PresheafOfModules (f_p O)` packages, for each open `U ⊆ X`, the scalar
> multiplication `(f_p O)(U) × (f_p G)(U) → (f_p G)(U)` together with the module axioms and
> the compatibility with the restriction maps. That `toPresheaf.obj M` is literally the
> pullback presheaf `f_p G` expresses that this module structure lives on `f_p G` itself.

```lean
theorem pullback_presheaf_module (O : TopCat.Presheaf RingCat.{u} Y) (G : PresheafOfModules.{u} O) :
    ∃ M : PresheafOfModules.{u} (pullbackRing f O),
      (PresheafOfModules.toPresheaf (pullbackRing f O)).obj M =
        pullbackAb f (underlyingAb O G)
```

**`Stacks.PresheafOfModules.Pullback.pullbackModuleFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/PullbackPresheaf.lean, line 658](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/PullbackPresheaf.lean#L658). The attribute's comment: “(3)”.

> **Stacks 008T (3): the functor lifting `f_p` to presheaves of modules.**
>
> The construction of the module structure is functorial in `G`: `f_p` lifts to a functor
> `Φ : PresheafOfModules O ⥤ PresheafOfModules (f_p O)` from the category of presheaves of
> `O`-modules on `Y` to the category of presheaves of `f_p O`-modules on `X`.  That it lies
> over the abelian-group-level functor `f_p` is `pullbackModuleFunctorCompToPresheaf`.
>
> On objects it sends `G` to the presheaf of `f_p O`-modules with carrier `f_p G` and the
> scalar action of `pullbackModule`. On a morphism `φ : G ⟶ G'` of `O`-modules with underlying
> Ab-presheaf morphism `φ̲`, it takes `(TopCat.Presheaf.pullback Ab f).map φ̲ : f_p G ⟶ f_p G'`,
> which is `(f_p O)(U)`-linear for each `U` by `pullbackModule_morphism_smul`: it is `colim` of
> the levelwise `O(V)`-linear maps `φ_V`, and the action is built from the levelwise
> `O(V)`-actions. Functoriality is inherited from that of `TopCat.Presheaf.pullback Ab f`, since
> `PresheafOfModules.homMk` is built on top of it and `toPresheaf` is faithful.

```lean
noncomputable def pullbackModuleFunctor (O : TopCat.Presheaf RingCat.{u} Y) :
    PresheafOfModules.{u} O ⥤ PresheafOfModules.{u} (pullbackRing f O)
```

**`Stacks.PresheafOfModules.Pullback.pullbackModuleFunctorCompToPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/PullbackPresheaf.lean, line 699](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/PullbackPresheaf.lean#L699). The attribute's comment: “(3)”.

> **Stacks 008T (3): the comparison isomorphism expressing that `pullbackModuleFunctor`
> lies over `f_p`:** `Φ ⋙ toPresheaf (f_p O) ≅ toPresheaf O ⋙ (pullback Ab f)`.
>
> Lying over `f_p` means that forgetting the module structure of `Φ.obj G` recovers `f_p`
> applied to the abelian-group presheaf underlying `G`, naturally in `G`.  In particular, for
> a morphism `φ : G → G'` of presheaves of `O`-modules, `Φ.map φ` is a morphism of presheaves
> of `f_p O`-modules whose underlying morphism of presheaves of abelian groups is `f_p φ`.
>
> It is the identity natural isomorphism: `Φ.obj G` is `ofPresheaf (f_p (underlying G)) …`,
> whose underlying Ab presheaf is `f_p (underlying G)` on the nose, and `Φ.map φ` is
> `homMk (f_p φ̲) …`, whose underlying Ab map is `f_p φ̲` on the nose, so both composites agree
> definitionally (compare `pushforward₀CompToPresheaf` and `restrictScalarsCompToPresheaf` in
> Mathlib, both also `Iso.refl _`).

```lean
noncomputable def pullbackModuleFunctorCompToPresheaf (O : TopCat.Presheaf RingCat.{u} Y) :
    pullbackModuleFunctor f O ⋙ PresheafOfModules.toPresheaf (pullbackRing f O) ≅
      PresheafOfModules.toPresheaf O ⋙ TopCat.Presheaf.pullback Ab.{u} f
```

## Tag 008U, a lemma

[Tag 008U](https://stacks.math.columbia.edu/tag/008U) in the Stacks Project.

**`Stacks.PresheafOfModules.Pullback.pullbackModuleAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/PullbackPresheafAdjunction.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/PullbackPresheafAdjunction.lean#L397).

> **Stacks 008U.**  Let `f : X ⟶ Y` be continuous and `O` a presheaf of rings on `Y`.  The
> explicit pullback `f_p` of presheaves of modules (with the `f_p O`-module structure of
> Stacks 008T) is left adjoint to the pushforward `f_*` (Stacks 008S), where `f_* F` is an
> `O`-module through the Kan-extension unit `i_O : O ⟶ f_*(f_p O)`.  Its hom-set bijection is
> `Mor_{PMod(f_p O)}(f_p G, F) ≃ Mor_{PMod(O)}(G, f_* F)`, natural in `G` and `F`; on underlying
> presheaves of abelian groups it is the bijection of `TopCat.Presheaf.pullbackPushforwardAdjunction`
> (`toPresheaf_map_pullbackModuleAdjunction_homEquiv`).

```lean
noncomputable def pullbackModuleAdjunction :
    pullbackModuleFunctor f O ⊣ PresheafOfModules.pushforward (pullbackRingUnitHom f O)
```

**`Stacks.PresheafOfModules.Pullback.toPresheaf_map_pullbackModuleAdjunction_homEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/PullbackPresheafAdjunction.lean, line 434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/PullbackPresheafAdjunction.lean#L434). The attribute's comment: “the bijection is the restriction of the one on presheaves of abelian groups”.

> **Stacks 008U, compatibility with abelian presheaves.**  The bijection of
> `pullbackModuleAdjunction` is the restriction to module maps of the bijection
> `Mor_{PAb(X)}(f_p G, F) ≃ Mor_{PAb(Y)}(G, f_* F)` of the adjunction `f_p ⊣ f_*` on presheaves
> of abelian groups: the underlying morphism of abelian presheaves of the transpose of `φ` is the
> abelian-level transpose of the underlying morphism of `φ`.

```lean
theorem toPresheaf_map_pullbackModuleAdjunction_homEquiv {M : PresheafOfModules.{u} O}
    {N : PresheafOfModules.{u} (pullbackRing f O)} (φ : (pullbackModuleFunctor f O).obj M ⟶ N) :
    (PresheafOfModules.toPresheaf O).map ((pullbackModuleAdjunction f O).homEquiv M N φ) =
      (abAdjunction f).homEquiv M.presheaf N.presheaf
        ((PresheafOfModules.toPresheaf (pullbackRing f O)).map φ)
```

## Tag 008V, a lemma

[Tag 008V](https://stacks.math.columbia.edu/tag/008V) in the Stacks Project.

**`Stacks.PresheafOfModules.TensorPullback.tensorPullbackAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/TensorPullbackAdjunction.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/TensorPullbackAdjunction.lean#L672). The attribute's comment: “the explicit `O ⊗_{p, f_p f_*O} f_p (-)` is left adjoint to `f_*`”.

> **Stacks 008V.** Let `f : X ⟶ Y` be a continuous map of topological spaces and `O` a
> presheaf of rings on `X`. The functor `G ↦ O ⊗_{p, f_p f_*O} f_p G` (`tensorPullback`), the
> presheaf pullback `f_p G` of a presheaf of `f_*O`-modules tensored up to `O` sectionwise along
> `c_O : f_p f_*O ⟶ O`, is left adjoint to the pushforward `f_* : PMod(O) ⥤ PMod(f_*O)`: for a
> presheaf of `O`-modules `F` and a presheaf of `f_*O`-modules `G` the hom-set bijection
> `Mor_{PMod(O)}(O ⊗_{p, f_p f_*O} f_p G, F) ≃ Mor_{PMod(f_*O)}(G, f_*F)`
> (`tensorPullbackHomEquiv`) is natural in `G` and `F`.

```lean
noncomputable def tensorPullbackAdjunction :
    tensorPullback f O ⊣ pushforwardModules008V f (ringsX O)
```

## Tag 008W, a lemma

[Tag 008W](https://stacks.math.columbia.edu/tag/008W) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.sheafPushforwardContinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPushforwardContinuous#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Module/PushforwardSheaf.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/PushforwardSheaf.lean#L26) (StacksFrontier): “the pushforward `f_*𝒪` of the sheaf of rings, along the continuous functor `Opens.map f`”. References: SGA 4 IV (4.9.1).
- [`SheafOfModules.pushforward`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.pushforward#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Module/PushforwardSheaf.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/PushforwardSheaf.lean#L28) (StacksFrontier): “pushforward of sheaves of modules: `f_*ℱ` is a sheaf of `f_*𝒪`-modules, functorially in `ℱ`”. References: EGA 0 (4.2.1), “more general”; EGA 0 (5.3.12); EGA II (1.1.1), “more general”; EGA II (1.1.2), “partial”; EGA IV (21.13.3); SGA 4 IV (11.2.2), “more general”; SGA 4 IV (13.2.1), “special case”; SGA 4 Vbis (1.3.6), “special case”.

## Tag 008X, a lemma

[Tag 008X](https://stacks.math.columbia.edu/tag/008X) in the Stacks Project.

**`InverseImageModules.exists_moduleStructure_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/InverseImage.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/InverseImage.lean#L135).

> **Stacks Tag 008X.**
>
> Let `f : X ⟶ Y` be a continuous map, `O` a sheaf of rings on `Y` and `G` a sheaf of
> `O`-modules.  There is a scalar multiplication turning `f⁻¹G` into a sheaf of
> `f⁻¹O`-modules, and it is natural in the sense that it extends the presheaf-level scalar
> multiplication `f_p O × f_p G → f_p G` of Tag 008T along the sheafification maps.
>
> Concretely: there is a sheaf of `f⁻¹O`-modules `M` whose underlying presheaf of abelian
> groups is literally `f⁻¹G`, together with a morphism `ι` of presheaves of `f_p O`-modules
> from `f_p G` to `M` restricted along `f_p O ⟶ f⁻¹O`, whose underlying morphism of
> presheaves of abelian groups is the sheafification map `f_p G ⟶ f⁻¹G`.

```lean
theorem exists_moduleStructure_inverseImage :
    ∃ (M : SheafOfModules.{u} (inverseImageRing f O))
      (h : M.val.presheaf = (inverseImageAb f O G).obj)
      (ι : pullbackPresheafOfModules f O G ⟶
            (PresheafOfModules.restrictScalars (toInverseImageRing f O)).obj M.val),
      (PresheafOfModules.toPresheaf _).map ι ≫ eqToHom h = toInverseImageAb f O G
```

## Tag 008Y, a lemma

[Tag 008Y](https://stacks.math.columbia.edu/tag/008Y) in the Stacks Project.

**`InverseImageModules.inverseImageModulesHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/InverseImageAdjunction.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/InverseImageAdjunction.lean#L108). The attribute's comment: “hom-set bijection of `inverseImageModulesAdjunction`, inverse image of 008X”.

> **Stacks Tag 008Y.**
>
> Let `f : X ⟶ Y` be a continuous map of topological spaces, `O` a sheaf of rings on `Y`,
> `G` a sheaf of `O`-modules and `F` a sheaf of `f⁻¹O`-modules. Then
> `Mor_{Mod(f⁻¹O)}(f⁻¹G, F) ≃ Mor_{Mod(O)}(G, f_*F)`, where `f⁻¹G` is the inverse image with its
> `f⁻¹O`-module structure of Tag 008X (`inverseImageSheafOfModules`), and `f_*F` is an
> `O`-module by restriction of scalars along `O ⟶ f_*f⁻¹O`. The bijection is the hom-set
> bijection of `inverseImageModulesAdjunction`, hence natural in `G` and `F`.

```lean
noncomputable def inverseImageModulesHomEquiv (G : SheafOfModules.{u} O)
    (F : SheafOfModules.{u} (inverseImageRingSheaf f O)) :
    (@Quiver.Hom (SheafOfModules.{u} (inverseImageRingSheaf f O)) _
        (inverseImageSheafOfModules f O G) F) ≃
      (G ⟶ (directImageModules f O).obj F)
```

## Tag 008Z, a lemma

[Tag 008Z](https://stacks.math.columbia.edu/tag/008Z) in the Stacks Project.

**`TensorInverseImagePushforward.adjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/TensorInverseImagePushforward.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/TensorInverseImagePushforward.lean#L362).

> **Stacks 008Z.** Let `f : X ⟶ Y` be a continuous map, `𝒪` a sheaf of (commutative) rings on
> `X`, `ℱ` a sheaf of `𝒪`-modules and `𝒢` a sheaf of `f_*𝒪`-modules. Then
> `Mor_{Mod(𝒪)}(𝒪 ⊗_{f^{-1}f_*𝒪} f^{-1}𝒢, ℱ) = Mor_{Mod(f_*𝒪)}(𝒢, f_*ℱ)`, naturally: the functor
> `tensorFunctor`, with `(tensorFunctor f O).obj 𝒢 = 𝒪 ⊗_{f^{-1}f_*𝒪} f^{-1}𝒢` the explicit
> tensor product (the sheafified sectionwise tensor product, Stacks 0088) of the inverse image
> `f^{-1}𝒢` (Stacks 008X) along the canonical map `counit : f^{-1}f_*𝒪 ⟶ 𝒪`, is left adjoint to
> the pushforward `f_*`, and the hom-set bijection of the adjunction is `homEquiv`.

```lean
noncomputable def adjunction : tensorFunctor f O ⊣ pushforwardModule f (ringSheaf O)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.24, Tag 008R](https://stacks.math.columbia.edu/tag/008R)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
