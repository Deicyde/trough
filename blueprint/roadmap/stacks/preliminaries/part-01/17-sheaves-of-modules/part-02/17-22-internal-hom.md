---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.internalHomTensorIso, Stacks.SheafOfModules.internalHomTensorIso_hom_app_tmul, Stacks.SheafOfModules.tensorHomEquiv, Stacks.SheafOfModules.tensorHomEquiv_isTensorCurry, Stacks.SheafOfModules.internalHomTensorIso_natural_left, Stacks.SheafOfModules.internalHomTensorIso_natural_middle, Stacks.SheafOfModules.internalHomTensorIso_natural_right, sheafHom_leftExact_fst
statement: formalized
proof: formalized
---

# 17.22 Internal Hom

Section 17.22 of the Stacks Project, [Tag 01CM](https://stacks.math.columbia.edu/tag/01CM). 8 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01CN, a lemma

[Tag 01CN](https://stacks.math.columbia.edu/tag/01CN) in the Stacks Project.

**`Stacks.SheafOfModules.internalHomTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean#L212). The attribute's comment: “canonical isomorphism”.

> The sheaf-hom out of a tensor product is canonically the corresponding iterated sheaf-hom:
> `ℋom(F ⊗ G, H) ≅ ℋom(F, ℋom(G, H))`.

```lean
noncomputable def internalHomTensorIso
    (F G H : _root_.SheafOfModules.{u} (structureSheafRing X)) :
    sheafHomSpace X (((Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩).obj F).obj G) H ≅
      sheafHomSpace X F (sheafHomSpace X G H)
```

**`Stacks.SheafOfModules.internalHomTensorIso_hom_app_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean#L228). The attribute's comment: “canonical characterization”.

> The canonical sheaf-hom isomorphism is currying: on every open, its evaluation on two
> local sections agrees with evaluation on their pure tensor.

```lean
theorem internalHomTensorIso_hom_app_tmul
    (U : Opens X.carrier)
    (s : (sheafHomSpace X
      (((Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩).obj F).obj G) H).val.obj (op U))
    (f : F.val.obj (op U)) (g : G.val.obj (op U)) :
    evalNestedInternalHomSection X U
        ((internalHomTensorIso X F G H).hom.val.app (op U) s) f g =
      evalTensorHomSection X U s f g
```

**`Stacks.SheafOfModules.tensorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean#L251). The attribute's comment: “morphism equivalence”.

> Giving a morphism `F ⊗ G ⟶ H` is canonically equivalent to giving a morphism
> `F ⟶ ℋom(G, H)`.

```lean
noncomputable def tensorHomEquiv
    (F G H : _root_.SheafOfModules.{u} (structureSheafRing X)) :
    (((Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩).obj F).obj G ⟶ H) ≃ (F ⟶ sheafHomSpace X G H)
```

**`Stacks.SheafOfModules.tensorHomEquiv_isTensorCurry`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean#L264). The attribute's comment: “morphism equivalence characterization”.

> The forward direction of `tensorHomEquiv` is the canonical currying map.

```lean
theorem tensorHomEquiv_isTensorCurry
    (t : ((Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩).obj F).obj G ⟶ H) :
    IsTensorCurry X t (tensorHomEquiv X F G H t)
```

**`Stacks.SheafOfModules.internalHomTensorIso_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean#L359). The attribute's comment: “functoriality in the first entry”.

> The canonical isomorphism commutes with precomposition in its first argument.

```lean
theorem internalHomTensorIso_natural_left
    {F' : _root_.SheafOfModules.{u} (structureSheafRing X)} (f : F' ⟶ F) :
    (internalHomTensorIso X F G H).hom ≫ sheafHomMapLeft X f =
      sheafHomMapLeft X ((Functor.uncurry.obj (Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩)).map
        ((f, 𝟙 G) : (_, _) ⟶ (_, _))) ≫
        (internalHomTensorIso X F' G H).hom
```

**`Stacks.SheafOfModules.internalHomTensorIso_natural_middle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean, line 371](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean#L371). The attribute's comment: “functoriality in the second entry”.

> The canonical isomorphism commutes with precomposition in its second argument.

```lean
theorem internalHomTensorIso_natural_middle
    {G' : _root_.SheafOfModules.{u} (structureSheafRing X)} (g : G' ⟶ G) :
    (internalHomTensorIso X F G H).hom ≫ sheafHomMapRight X (sheafHomMapLeft X g) =
      sheafHomMapLeft X ((Functor.uncurry.obj (Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩)).map
        ((𝟙 F, g) : (_, _) ⟶ (_, _))) ≫
        (internalHomTensorIso X F G' H).hom
```

**`Stacks.SheafOfModules.internalHomTensorIso_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/InternalHom.lean#L383). The attribute's comment: “functoriality in the third entry”.

> The canonical isomorphism commutes with postcomposition in its target.

```lean
theorem internalHomTensorIso_natural_right
    {H' : _root_.SheafOfModules.{u} (structureSheafRing X)} (h : H ⟶ H') :
    sheafHomMapRight X h ≫ (internalHomTensorIso X F G H').hom =
      (internalHomTensorIso X F G H).hom ≫ sheafHomMapRight X (sheafHomMapRight X h)
```

## Tag 01CO, a lemma

[Tag 01CO](https://stacks.math.columbia.edu/tag/01CO) in the Stacks Project.

**`sheafHom_leftExact_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomLeftExact.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomLeftExact.lean#L353). The attribute's comment: “(1)”. References: EGA 0 (4.1.5), “special case”; EGA 0 (6.7.6), “partial”; SGA 4 IV (12.2), “partial”.

> Left exactness of `SheafHom` in the first argument. Given an exact sequence
> `F₂ --α--> F₁ --β--> F → 0` of `O_X`-modules (encoded as the exact `ComposableArrows`
> `F₂ → F₁ → F → 0`, whose final node forces `β` epi), and internal homs `SheafHom(F,G)`,
> `SheafHom(F₁,G)`, `SheafHom(F₂,G)` with induced precomposition maps `β* = mβ`, `α* = mα`
> (morphisms of `O_X`-modules), the induced sequence of `O_X`-modules
>   `0 → SheafHom(F, G) --β*--> SheafHom(F₁, G) --α*--> SheafHom(F₂, G)`
> is exact in `SheafOfModules R` (`β*` is mono and `im β* = ker α*`).

```lean
theorem sheafHom_leftExact_fst
    (F₂ F₁ F G : SheafOfModules.{v} (structureSheaf Rc)) (α : F₂ ⟶ F₁) (β : F₁ ⟶ F)
    (hin : (ComposableArrows.mk₃ α β (0 : F ⟶ 0)).Exact)
    (HF : SheafHom Rc F G) (HF₁ : SheafHom Rc F₁ G) (HF₂ : SheafHom Rc F₂ G)
    (mβ : HF.obj ⟶ HF₁.obj) (mα : HF₁.obj ⟶ HF₂.obj)
    (hmβ : SheafHom.IsPrecomp Rc β HF HF₁ mβ) (hmα : SheafHom.IsPrecomp Rc α HF₁ HF₂ mα) :
    (ComposableArrows.mk₃
      (0 : (0 : SheafOfModules.{v} (structureSheaf Rc)) ⟶ HF.obj) mβ mα).Exact
```

**`sheafHom_leftExact_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomLeftExact.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomLeftExact.lean#L416). The attribute's comment: “(2)”. References: EGA 0 (4.1.5), “special case”; SGA 4 IV (12.2), “partial”; SGA 4 V (6.0), “6.0, special case”.

> Left exactness of `SheafHom` in the second argument. Given an exact sequence
> `0 → G --u--> G₁ --v--> G₂` of `O_X`-modules (encoded as the exact `ComposableArrows`
> `0 → G → G₁ → G₂`, whose first node forces `u` mono), and internal homs `SheafHom(F,G)`,
> `SheafHom(F,G₁)`, `SheafHom(F,G₂)` with induced postcomposition maps `u_* = mu`, `v_* = mv`
> (morphisms of `O_X`-modules), the induced sequence of `O_X`-modules
>   `0 → SheafHom(F, G) --u_*--> SheafHom(F, G₁) --v_*--> SheafHom(F, G₂)`
> is exact in `SheafOfModules R` (`u_*` is mono and `im u_* = ker v_*`).

```lean
theorem sheafHom_leftExact_snd
    (F G G₁ G₂ : SheafOfModules.{v} (structureSheaf Rc)) (u : G ⟶ G₁) (v : G₁ ⟶ G₂)
    (hin : (ComposableArrows.mk₃
      (0 : (0 : SheafOfModules.{v} (structureSheaf Rc)) ⟶ G) u v).Exact)
    (HG : SheafHom Rc F G) (HG₁ : SheafHom Rc F G₁) (HG₂ : SheafHom Rc F G₂)
    (mu : HG.obj ⟶ HG₁.obj) (mv : HG₁.obj ⟶ HG₂.obj)
    (hmu : SheafHom.IsPostcomp Rc u HG HG₁ mu) (hmv : SheafHom.IsPostcomp Rc v HG₁ HG₂ mv) :
    (ComposableArrows.mk₃
      (0 : (0 : SheafOfModules.{v} (structureSheaf Rc)) ⟶ HG.obj) mu mv).Exact
```

## Tag 0A6F, a lemma

[Tag 0A6F](https://stacks.math.columbia.edu/tag/0A6F) in the Stacks Project.

**`RingedSpaceModuleAdjunction.homSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/HomSheaf.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/HomSheaf.lean#L424). The attribute's comment: “the internal Hom sheaf, as a functor to modules over the target ring”.

> The functor `SheafHom_{𝒪₁}(𝒪₂, -)` from `𝒪₁`-modules to `𝒪₂`-modules. On underlying
> presheaves it is the coextension of scalars `Stacks.PresheafOfModules.CoextendScalars.coextFunMap`.

```lean
noncomputable def homSheaf
    {C : Type u} [Category.{u} C] {J : GrothendieckTopology C}
    {𝒪₁ 𝒪₂ : CategoryTheory.Sheaf J RingCat.{u}}
    (α : 𝒪₁ ⟶ 𝒪₂) : SheafOfModules.{u} 𝒪₁ ⥤ SheafOfModules.{u} 𝒪₂
```

**`RingedSpaceModuleAdjunction.restrictScalarsHomAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/HomSheaf.lean, line 438](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/HomSheaf.lean#L438). The attribute's comment: “the bifunctorial Hom identification”. References: SGA 4 IV (14.5), “adjunction i\_* ⊣ i^!”.

> Restriction of scalars along a homomorphism of sheaves of rings is left adjoint to the
> internal-Hom functor `SheafHom_{𝒪₁}(𝒪₂, -)`.

```lean
noncomputable def restrictScalarsHomAdjunction
    {C : Type u} [Category.{u} C] {J : GrothendieckTopology C}
    {𝒪₁ 𝒪₂ : CategoryTheory.Sheaf J RingCat.{u}}
    (α : 𝒪₁ ⟶ 𝒪₂) :
    SheafOfModules.restrictScalars.{u} α ⊣ homSheaf α
```

## Tag 01CP, a lemma

[Tag 01CP](https://stacks.math.columbia.edu/tag/01CP) in the Stacks Project.

**`Stacks.SheafOfModules.SheafHomStalk.injective_sheafHomStalkLinearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomStalk.lean, line 903](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomStalk.lean#L903). The attribute's comment: “finite\_type\_injective”. References: EGA 0 (5.2.6), “partial”.

> **Injectivity half of Stacks 01CP.** For `F` of finite type the canonical map from the stalk
> of the internal hom to the module of homomorphisms of the stalks is injective. Only local
> generation by finitely many sections is used, which is exactly `LocalGenerators`; the relations
> of a `LocalPresentation` are needed only for surjectivity.
>
> This is `injective_sheafHomStalkLinearMap_of_localGenerators`, whose hypothesis is only that `F`
> has local generators at `x`, applied to the generators that finite type produces there.

```lean
theorem injective_sheafHomStalkLinearMap (H : SheafHom Rc F G) (x : X)
    [F.IsFiniteType] : Function.Injective (sheafHomStalkLinearMap H x)
```

**`Stacks.SheafOfModules.SheafHomStalk.sheafHomStalkLinearEquivOfFinitePresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomStalk.lean, line 1130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomStalk.lean#L1130). The attribute's comment: “finite\_presentation\_isomorphism”.

> **Stacks Project, Tag 01CP.** If `F` is of finite presentation, the canonical map from the
> stalk of `SheafHom(F, G)` at `x` to the module of `O_{X,x}`-linear maps from `F_x` to `G_x` is an
> isomorphism. The equivalence produced here is the canonical map `sheafHomStalkLinearMap H x`: its
> `germ_apply` field records that it sends the germ of a local homomorphism and the germ of a local
> section to the germ of the evaluation, and by `sheafHomStalkLinearMap_unique` that property
> determines it.

```lean
noncomputable def sheafHomStalkLinearEquivOfFinitePresentation
    (H : SheafHom Rc F G) (x : X) [F.IsFinitePresentation] :
    SheafHomStalkLinearEquiv Rc F G H x
```

## Tag 0C6I, a lemma

[Tag 0C6I](https://stacks.math.columbia.edu/tag/0C6I) in the Stacks Project.

**`Stacks.SheafHomPullback.isIso_pullbackSheafHomMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Recovery17/PullbackInternalHomCanonical.lean, line 518](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/Recovery17/PullbackInternalHomCanonical.lean#L518).

> **Stacks Project, Tag 0C6I.** Let `f : X ⟶ Y` be a flat morphism of ringed spaces and let
> `F`, `G` be `𝒪_Y`-modules with `F` finitely presented. Then the canonical map
> `f^* SheafHom(F, G) ⟶ SheafHom(f^*F, f^*G)` is an isomorphism.
>
> The canonical map is `pullbackSheafHomMap`, the adjoint transpose of pulling back local
> homomorphisms along `f`; the two internal Homs are any `SheafHom` models.

```lean
theorem isIso_pullbackSheafHomMap (hf : AlgebraicGeometry.IsFlat f) [F.IsFinitePresentation] :
    IsIso (pullbackSheafHomMap f F G H H')
```

## Tag 01CQ, a lemma

[Tag 01CQ](https://stacks.math.columbia.edu/tag/01CQ) in the Stacks Project.

**`Stacks.SheafOfModules.sheafHom_locallyKernelFiniteCoproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomSlice.lean, line 732](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomSlice.lean#L732). The attribute's comment: “local kernel presentation”.

> **The internal hom out of a finitely presented module is locally the kernel of a map
> between finite direct sums of copies of the target.**

```lean
theorem sheafHom_locallyKernelFiniteCoproduct [F.IsFinitePresentation] :
    ∀ x : X, ∃ U : Opens X, x ∈ U ∧ ∃ m n : ℕ,
      ∃ f : (∐ fun _ : Fin m => G.over U) ⟶ (∐ fun _ : Fin n => G.over U),
        Nonempty ((sheafHom 𝒪 h𝒪 F G).over U ≅ kernel f)
```

**`Stacks.SheafOfModules.sheafHom_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomSlice.lean, line 759](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomSlice.lean#L759). The attribute's comment: “coherence of internal Hom”.

> **The internal hom out of a finitely presented module into a coherent module is
> coherent.**

```lean
theorem sheafHom_isCoherent [F.IsFinitePresentation] [IsCoherent G] :
    IsCoherent (sheafHom 𝒪 h𝒪 F G)
```

**`Stacks.SheafOfModules.InternalHom.exists_locally_isoKernel_sheafInternalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InternalHomCoherent/LocalKernel.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InternalHomCoherent/LocalKernel.lean#L284). The attribute's comment: “local kernel presentation”.

> **The first clause of [Stacks, Tag 01CQ].** Let `(Y, 𝒪_Y)` be a ringed space and let `F`,
> `G` be `𝒪_Y`-modules with `F` of finite presentation. Then `SheafHom(F, G)` is *locally a kernel
> of a map between finite direct sums of copies of `G`*: every point of `Y` has an open
> neighbourhood `U` for which `SheafHom(F, G)|_U` is the kernel of a morphism
> `∐_{i < m} G|_U ⟶ ∐_{j < n} G|_U`.

```lean
theorem exists_locally_isoKernel_sheafInternalHom
    (F G : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (spaceRingedSite O).O))
    [F.IsFinitePresentation] (y : Y) :
    ∃ U : Opens Y, y ∈ U ∧ ∃ (m n : ℕ)
      (f : (∐ fun _ : Fin m => G.over U) ⟶ (∐ fun _ : Fin n => G.over U)),
      Nonempty ((sheafInternalHom (spaceRingedSite O) F G).over U ≅ kernel f)
```

**`Stacks.SheafOfModules.InternalHom.isCoherent_sheafInternalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InternalHomCoherent/LocalKernel.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InternalHomCoherent/LocalKernel.lean#L306). The attribute's comment: “coherence of internal Hom”.

> **The second clause of [Stacks, Tag 01CQ].** On a ringed space, the internal Hom from a
> module of finite presentation into a coherent module is coherent. This combines the first clause
> with the gluing step `Stacks.SheafOfModules.isCoherent_of_locallyKernelFiniteCoproduct`.
>
> The coherence predicate here is the one of
> `StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Coherent.lean`; for the one of
> Stacks Tag 01BW see `isCoherent_sheafInternalHom'`, which is the same
> statement and is deliberately left untagged so that the tag is not counted twice.

```lean
theorem isCoherent_sheafInternalHom
    (F G : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (spaceRingedSite O).O))
    [F.IsFinitePresentation] [Stacks.SheafOfModules.IsCoherent G] :
    Stacks.SheafOfModules.IsCoherent
      (sheafInternalHom (spaceRingedSite O) F G)
```

**`Stacks.AlgebraicGeometry.InternalHomLocalKernel.sheafHom_locallyKernelFiniteCoproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InternalHomLocalKernel/Basic.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InternalHomLocalKernel/Basic.lean#L375). The attribute's comment: “local kernel presentation”.

> **Stacks 01CQ, first assertion, for a ringed space.** A sheaf Hom from a finitely presented
> module is locally the kernel of a map between finite direct sums of copies of the target.

```lean
theorem sheafHom_locallyKernelFiniteCoproduct
    (F G : _root_.SheafOfModules.{u}
      (structureSheafRing X))
    [F.IsFinitePresentation] :
    ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      ∃ m n : ℕ,
        ∃ f : (∐ (fun _ : Fin m => G.over U)) ⟶ (∐ (fun _ : Fin n => G.over U)),
          Nonempty ((_root_.Stacks.SheafOfModules.sheafHom X.presheaf
              (structureSheafRing X).property F G).over
                U ≅
            (kernel f :
              _root_.SheafOfModules.{u}
                ((structureSheafRing X).over U)))
```

**`Stacks.AlgebraicGeometry.InternalHomLocalKernel.sheafHom_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InternalHomLocalKernel/Basic.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InternalHomLocalKernel/Basic.lean#L395). The attribute's comment: “coherence of internal Hom”.

> **Stacks 01CQ, second assertion, for a ringed space.** Internal Hom from a finitely
> presented module into a coherent module is coherent.

```lean
theorem sheafHom_isCoherent
    (F G : _root_.SheafOfModules.{u}
      (structureSheafRing X))
    [F.IsFinitePresentation] [G.IsCoherent] :
    (_root_.Stacks.SheafOfModules.sheafHom X.presheaf
      (structureSheafRing X).property F G).IsCoherent
```

## Tag 0GMV, a lemma

[Tag 0GMV](https://stacks.math.columbia.edu/tag/0GMV) in the Stacks Project.

**`Stacks.SheafOfModules.isColimit_sheafHomCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomFilteredColimit.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomFilteredColimit.lean#L170).

> **Stacks Project, Tag 0GMV.** Let `F` be an `O_X`-module of finite presentation on a ringed
> space and let `G = colim_λ G_λ` be a filtered colimit of `O_X`-modules. Then the canonical
> cocone of internal homs over `SheafHom_{O_X}(F, G)`, whose legs are the postcomposition maps
> induced by the colimit inclusions, is a colimit cocone; that is, the canonical map
> `colim_λ SheafHom_{O_X}(F, G_λ) ⟶ SheafHom_{O_X}(F, G)` is an isomorphism.

```lean
noncomputable def isColimit_sheafHomCocone [F.IsFinitePresentation] [IsFiltered K]
    (c : Cocone D) (hc : IsColimit c)
    (H : ∀ j, SheafHom Rc F (D.obj j)) (Hc : SheafHom Rc F c.pt) :
    IsColimit (sheafHomCocone F D c H Hc)
```

**`Stacks.SheafOfModules.isIso_desc_sheafHomCocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomFilteredColimit.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomFilteredColimit.lean#L196).

> **Stacks Project, Tag 0GMV**, in comparison-map form: for `F` of finite presentation and a
> filtered diagram, the canonical map from any colimit of the internal homs
> `SheafHom_{O_X}(F, G_λ)` to `SheafHom_{O_X}(F, colim_λ G_λ)` is an isomorphism.

```lean
theorem isIso_desc_sheafHomCocone [F.IsFinitePresentation] [IsFiltered K]
    (c : Cocone D) (hc : IsColimit c)
    (H : ∀ j, SheafHom Rc F (D.obj j)) (Hc : SheafHom Rc F c.pt)
    (t : Cocone (sheafHomDiagram F D H)) (ht : IsColimit t) :
    IsIso (ht.desc (sheafHomCocone F D c H Hc))
```

## Tag 01BS, a lemma

[Tag 01BS](https://stacks.math.columbia.edu/tag/01BS) in the Stacks Project.

**`Stacks.SheafOfModules.preservesColimitsOfShape_coyoneda_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomFilteredColimitSections.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomFilteredColimitSections.lean#L119).

> **Stacks Project, Tag 01BS.**  Let `X` be a ringed space with a cofinal system of open
> coverings `X = ⋃_{j ∈ J} U_j` with `J` finite and all `U_j ∩ U_j'` quasi-compact, let `F` be an
> `O_X`-module of finite presentation and let `λ ↦ G_λ` be a filtered system of `O_X`-modules.  Then
>
> `colim_λ Hom_X(F, G_λ) = Hom_X(F, colim_λ G_λ)`;
>
> here in the form that `Hom_X(F, -)` preserves colimits of the given filtered shape, which says
> exactly that the canonical comparison map out of any colimit of the `Hom_X(F, G_λ)` is an
> isomorphism.

```lean
theorem preservesColimitsOfShape_coyoneda_of_isFinitePresentation
    (F : _root_.SheafOfModules.{u} (structureSheaf Rc)) [F.IsFinitePresentation]
    (K : Type u) [Category.{u} K] [IsFiltered K]
    (hX : DirectedColimitOfSheaves.HasFiniteCompactCofinalCovers (X := X) ⊤) :
    PreservesColimitsOfShape K (coyoneda.obj (op F))
```

**`Stacks.SheafOfModules.isIso_colimitPost_coyoneda_of_hasFiniteCompactCofinalCovers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomFilteredColimitSections.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomFilteredColimitSections.lean#L145).

> **Stacks Project, Tag 01BS as the source displays it.**  The canonical comparison map
>
> `colim_λ Hom_X(F, G_λ) ⟶ Hom_X(F, colim_λ G_λ)`
>
> is an isomorphism of types, for `F` an `O_X`-module of finite presentation and `G` a filtered
> system of `O_X`-modules on a ringed space with a cofinal system of finite open coverings having
> quasi-compact pairwise intersections.

```lean
theorem isIso_colimitPost_coyoneda_of_hasFiniteCompactCofinalCovers
    (F : _root_.SheafOfModules.{u} (structureSheaf Rc)) [F.IsFinitePresentation]
    {K : Type u} [Category.{u} K] [IsFiltered K]
    (G : K ⥤ _root_.SheafOfModules.{u} (structureSheaf Rc))
    (hX : DirectedColimitOfSheaves.HasFiniteCompactCofinalCovers (X := X) ⊤) :
    IsIso (colimit.post G (coyoneda.obj (op F)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.22, Tag 01CM](https://stacks.math.columbia.edu/tag/01CM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
