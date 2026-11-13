---
declaration: section
origin: cited
lean: OpenImmersionSheaves.presheaf_pullback_iso_restriction, OpenImmersionSheaves.sheaf_pullback_iso_restriction, OpenImmersionSheaves.stalk_sheaf_pullback_iso, OpenImmersionSheaves.presheaf_pullback_pushforward_counit_isIso, OpenImmersionSheaves.sheaf_pullback_pushforward_counit_isIso, OpenImmersionSheaves.restrictPresheafAdjunction, OpenImmersionSheaves.presheafPullbackIsoRestrict, OpenImmersionSheaves.isIso_restrictPresheafAdjunction_counit
statement: formalized
proof: formalized
---

# 6.31 Open immersions and (pre)sheaves

Section 6.31 of the Stacks Project, [Tag 009Z](https://stacks.math.columbia.edu/tag/009Z). 13 tags here are carried by 67 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00A0, a lemma

[Tag 00A0](https://stacks.math.columbia.edu/tag/00A0) in the Stacks Project.

**`OpenImmersionSheaves.presheaf_pullback_iso_restriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean#L86). The attribute's comment: “(1)”.

> **Stacks 00A0 (1).** For a presheaf of sets `G` on `X`, the presheaf pullback
> `j_p G` (the colimit-based left adjoint of `j_*`) is canonically isomorphic to
> the naive restriction `V ↦ G(j V)`:
> `(j_p G) ≅ restrictPresheaf hj G`.
> Componentwise, for every open `V ⊆ U`, the canonical colimit map
> `G(j V) → (j_p G)(V)` is a bijection (the colimit defining `(j_p G)(V)`
> collapses to its value at the largest neighbourhood `j V = V`). The
> isomorphism is exhibited as honest data: it is Mathlib's canonical
> `IsOpenMap.pullbackObjIso`, whose `V`-component is the canonical comparison
> `pullbackObjObjOfImageOpen`.

```lean
noncomputable def presheaf_pullback_iso_restriction (G : X.Presheaf (Type u)) :
    (Presheaf.pullback (Type u) j).obj G ≅ restrictPresheaf j hj G
```

**`OpenImmersionSheaves.sheaf_pullback_iso_restriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean#L111). The attribute's comment: “(2)”. References: EGA 0 (3.7.1), “special case”; SGA 4 III (2.7), “Φ^* ≅ (i^\{-1})^s”; SGA 4 III (5.3), “Clause 2, special case”.

> **Stacks 00A0 (2).** For a sheaf of sets `G` on `X`, the sheaf pullback
> `j⁻¹ G` (sheafification of `j_p G`) is canonically isomorphic, as a *sheaf on
> `U`*, to the restriction sheaf `restrictSheaf hj G` (no sheafification is needed,
> by the sheaf condition built into `restrictSheaf`). The isomorphism lives in the
> category `U.Sheaf (Type u)`. It is exhibited as honest data: the `G`-component of
> Mathlib's canonical natural isomorphism `Topology.IsOpenEmbedding.sheafPullbackIso`
> (note `(hj.sheafPullback _).obj G = restrictSheaf hj G` by definition).

```lean
noncomputable def sheaf_pullback_iso_restriction (G : X.Sheaf (Type u)) :
    (Sheaf.pullback (Type u) j).obj G ≅ restrictSheaf j hj G
```

**`OpenImmersionSheaves.stalk_sheaf_pullback_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean#L126). The attribute's comment: “(3)”.

> **Stacks 00A0 (3).** For a sheaf of sets `G` on `X` and a point `u ∈ U`, the
> stalk of the sheaf pullback `j⁻¹ G` at `u` is canonically isomorphic to the
> stalk of `G` at `j u`:
> `(j⁻¹ G)_u ≅ G_{j u}`.
> This is the special case `f = j` of the canonical stalk identity
> `(f⁻¹ G)_x ≅ G_{f x}`. It is exhibited as honest data, built from the canonical
> comparison maps: the underlying presheaf of `j⁻¹ G` is canonically isomorphic to
> the presheaf pullback `j_p (G^♭)` (via clause (2) and
> `IsOpenMap.pullbackObjIso`), and `Presheaf.stalkPullbackIso` identifies the
> stalk of the presheaf pullback at `u` with the stalk of `G` at `j u`.

```lean
noncomputable def stalk_sheaf_pullback_iso (G : X.Sheaf (Type u)) (u : U) :
    Presheaf.stalk ((Sheaf.pullback (Type u) j).obj G).obj u
      ≅ Presheaf.stalk G.obj ((ConcreteCategory.hom j) u)
```

**`OpenImmersionSheaves.presheaf_pullback_pushforward_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean#L249). The attribute's comment: “(4)”. References: SGA 4 IV (9.2.4), “a), special case”.

> **Stacks 00A0 (4).** On the category `PSh(U)` of presheaves of sets on `U`,
> the *canonical* natural transformation `j_p ∘ j_* ⟶ id` — namely the counit of
> the adjunction `j_p ⊣ j_*` (`pullback ⊣ pushforward`) — is a natural
> isomorphism. Equivalently, for every presheaf of sets `F` on `U` and every open
> `V ⊆ U`, the canonical map `(j_p j_* F)(V) → F(V)` is a bijection, naturally in
> `F`. This exhibits the canonical natural isomorphism `j_p ∘ j_* ≅ id_{PSh(U)}`.
> The open-embedding hypothesis `hj` is required: for an arbitrary continuous `j`
> this counit need not be an isomorphism.
>
> Proof: A counit of an adjunction `L ⊣ R` is an isomorphism whenever the right
> adjoint `R` is fully faithful (`Adjunction.counit_isIso_of_R_fully_faithful`).
> Here `R = j_* = Presheaf.pushforward (Type u) j`, which is fully faithful for the
> open embedding `j` by `presheafPushforwardFullyFaithful`.

```lean
theorem presheaf_pullback_pushforward_counit_isIso
    (j : U ⟶ X) (hj : Topology.IsOpenEmbedding (ConcreteCategory.hom j)) :
    IsIso (Presheaf.pullbackPushforwardAdjunction (Type u) j).counit
```

**`OpenImmersionSheaves.sheaf_pullback_pushforward_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean#L272). The attribute's comment: “(5)”. References: EGA I (9.4.2), “(i)”; SGA 4 IV (9.2.4), “a), special case”.

> **Stacks 00A0 (5).** On the category `Sh(U)` of sheaves of sets on `U`, the
> *canonical* natural transformation `j⁻¹ ∘ j_* ⟶ id` — namely the counit of the
> adjunction `j⁻¹ ⊣ j_*` (`Sheaf.pullback ⊣ Sheaf.pushforward`) — is a natural
> isomorphism. Equivalently, for every sheaf of sets `F` on `U` and every open
> `V ⊆ U`, the canonical map `(j⁻¹ j_* F)(V) → F(V)` is a bijection, naturally in
> `F`. This exhibits the canonical natural isomorphism `j⁻¹ ∘ j_* ≅ id_{Sh(U)}`.
> The open-embedding hypothesis `hj` is required: for an arbitrary continuous `j`
> this counit need not be an isomorphism.
>
> Proof: As for clause (4), the counit of `Sheaf.pullback ⊣ Sheaf.pushforward`
> is an isomorphism because its right adjoint `j_* = Sheaf.pushforward (Type u) j`
> is fully faithful for the open embedding `j`
> (`sheafPushforwardFullyFaithful`), via
> `Adjunction.counit_isIso_of_R_fully_faithful`.

```lean
theorem sheaf_pullback_pushforward_counit_isIso
    (j : U ⟶ X) (hj : Topology.IsOpenEmbedding (ConcreteCategory.hom j)) :
    IsIso (Sheaf.pullbackPushforwardAdjunction (Type u) j).counit
```

**`OpenImmersionSheaves.restrictPresheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean#L81). The attribute's comment: “(1) for presheaves with values in any category: restriction is left adjoint to `j_*`, i.e. is `j_p`; see `presheafPullbackIsoRestrict` for Mathlib's colimit-built `j_p`”.

> **Stacks 00A0 (1), for presheaves with values in any category `A`.** The restriction
> `G ↦ (V ↦ G(V))` of presheaves along the open embedding `j : U ⟶ X` is left adjoint to the
> pushforward `j_* = TopCat.Presheaf.pushforward A j`. Since Stacks defines `j_p` as the left
> adjoint of `j_*` (Stacks 008C), this says that `j_p G` is given by `V ↦ G(V)` for `V ⊆ U` open.
> No hypothesis on `A` is needed. The adjunction is the whiskering of the opposite of the
> adjunction `hj.functor ⊣ Opens.map j` of posets of opens.

```lean
noncomputable def restrictPresheafAdjunction :
    restrictPresheafFunctor A j hj ⊣ Presheaf.pushforward A j
```

**`OpenImmersionSheaves.presheafPullbackIsoRestrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean#L89). The attribute's comment: “(1) for Mathlib's colimit-built `j_p` (Mathlib `IsOpenMap.pullbackIso`)”.

> **Stacks 00A0 (1), Mathlib's `j_p`.** When `A` has colimits, Mathlib's presheaf pullback
> `TopCat.Presheaf.pullback A j` (the left Kan extension, computed by colimits) is isomorphic to
> the restriction. This is Mathlib's `IsOpenMap.pullbackIso`.

```lean
noncomputable def presheafPullbackIsoRestrict [HasColimits A] :
    Presheaf.pullback A j ≅ restrictPresheafFunctor A j hj
```

**`OpenImmersionSheaves.isIso_restrictPresheafAdjunction_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean#L97). The attribute's comment: “(4) for presheaves with values in any category”.

> **Stacks 00A0 (4), for presheaves with values in any category `A`.** The counit
> `j_p j_* ⟶ 𝟭` of `restrictPresheafAdjunction` is an isomorphism: its component at `F` and `V`
> is `F` applied to the isomorphism `V ≅ j⁻¹(j V)`.

```lean
theorem isIso_restrictPresheafAdjunction_counit :
    IsIso (restrictPresheafAdjunction A j hj).counit
```

**`OpenImmersionSheaves.isIso_presheafPullbackPushforwardAdjunction_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean#L123). The attribute's comment: “(4) for Mathlib's `j_p ⊣ j_*`”.

> **Stacks 00A0 (4), Mathlib's adjunction.** When `A` has colimits, the counit of Mathlib's
> adjunction `TopCat.Presheaf.pullback A j ⊣ TopCat.Presheaf.pushforward A j` is an isomorphism.

```lean
theorem isIso_presheafPullbackPushforwardAdjunction_counit [HasColimits A] :
    IsIso (Presheaf.pullbackPushforwardAdjunction A j).counit
```

**`OpenImmersionSheaves.restrictSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean#L137). The attribute's comment: “(2) for sheaves with values in any category: restriction is left adjoint to `j_*`, i.e. is `j⁻¹`; see `sheafPullbackIsoRestrict` for Mathlib's sheafified `j⁻¹`”.

> **Stacks 00A0 (2), for sheaves with values in any category `A`.** The restriction
> `hj.sheafPullback A : Sh(X, A) ⥤ Sh(U, A)`, `G ↦ (V ↦ G(V))` — a sheaf as it stands, with no
> sheafification — is left adjoint to the pushforward `j_* = TopCat.Sheaf.pushforward A j`.
> Since Stacks defines `j⁻¹` on sheaves as the left adjoint of `j_*` (Stacks 008C), this says
> that `j⁻¹ G` is given by `V ↦ G(V)` for `V ⊆ U` open. No hypothesis on `A` is needed.

```lean
noncomputable def restrictSheafAdjunction :
    hj.sheafPullback A ⊣ Sheaf.pushforward A j
```

**`OpenImmersionSheaves.isIso_restrictSheafAdjunction_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean#L145). The attribute's comment: “(5) for sheaves with values in any category”.

> **Stacks 00A0 (5), for sheaves with values in any category `A`.** The counit
> `j⁻¹ j_* ⟶ 𝟭` of `restrictSheafAdjunction` is an isomorphism.

```lean
theorem isIso_restrictSheafAdjunction_counit :
    IsIso (restrictSheafAdjunction A j hj).counit
```

**`OpenImmersionSheaves.restrictStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean#L177). The attribute's comment: “(3) for presheaves with values in any category, stalk of the restriction”.

> **Stacks 00A0 (3), for presheaves with values in any category `A`.** For a presheaf `G` on
> `X` and `u ∈ U`, if the stalk `G_{j u}` (the colimit of `G` over the open neighbourhoods of
> `j u`) exists, then so does the stalk at `u` of the restriction `V ↦ G(V)`
> (`hasColimit_restrict_nhds`) and the two are canonically isomorphic: the neighbourhoods of
> `j u` of the form `j V` are cofinal. No colimits are assumed in `A`. This is the argument of
> Mathlib's `AlgebraicGeometry.PresheafedSpace.restrictStalkIso`, which needs `HasColimits A`.

```lean
noncomputable def restrictStalkIso (G : X.Presheaf A) (u : U)
    [HasColimit ((OpenNhds.inclusion (j u)).op ⋙ G)] :
    haveI := hasColimit_restrict_nhds A j hj G u
    colimit ((OpenNhds.inclusion u).op ⋙ (restrictPresheafFunctor A j hj).obj G) ≅
      colimit ((OpenNhds.inclusion (j u)).op ⋙ G)
```

**`OpenImmersionSheaves.sheafPullbackIsoRestrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean#L199). The attribute's comment: “(2) for Mathlib's sheafified `j⁻¹` (Mathlib `Topology.IsOpenEmbedding.sheafPullbackIso`)”.

> **Stacks 00A0 (2), Mathlib's `j⁻¹`.** Under the hypotheses for which Mathlib constructs the
> sheaf pullback `TopCat.Sheaf.pullback A j` (the sheafification of the presheaf pullback), it is
> isomorphic to the restriction `hj.sheafPullback A`. This is Mathlib's
> `Topology.IsOpenEmbedding.sheafPullbackIso`.

```lean
noncomputable def sheafPullbackIsoRestrict :
    Sheaf.pullback A j ≅ hj.sheafPullback A
```

**`OpenImmersionSheaves.isIso_sheafPullbackPushforwardAdjunction_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean#L207). The attribute's comment: “(5) for Mathlib's `j⁻¹ ⊣ j_*`”.

> **Stacks 00A0 (5), Mathlib's adjunction.** The counit of Mathlib's adjunction
> `TopCat.Sheaf.pullback A j ⊣ TopCat.Sheaf.pushforward A j` is an isomorphism.

```lean
theorem isIso_sheafPullbackPushforwardAdjunction_counit :
    IsIso (Sheaf.pullbackPushforwardAdjunction A j).counit
```

**`OpenImmersionSheaves.sheafPullbackStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Coefficients.lean#L218). The attribute's comment: “(3) for Mathlib's sheafified `j⁻¹`”.

> **Stacks 00A0 (3), Mathlib's `j⁻¹`.** For a sheaf `G` on `X` and `u ∈ U`, the stalk of
> Mathlib's sheaf pullback `j⁻¹ G` at `u` is the stalk of `G` at `j u`:
> `(j⁻¹ G)_u ≅ (G|_U)_u ≅ G_{j u}`, through clause (2) and `restrictStalkIso`.

```lean
noncomputable def sheafPullbackStalkIso (G : X.Sheaf A) (u : U) :
    Presheaf.stalk ((Sheaf.pullback A j).obj G).obj u ≅
      Presheaf.stalk G.obj ((ConcreteCategory.hom j) u)
```

**`OpenImmersionSheaves.restrictPresheafOfModulesAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleRestriction.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleRestriction.lean#L96). The attribute's comment: “(1) for presheaves of modules: restriction is left adjoint to `j_*`, i.e. is `j_p`”.

> **Stacks 00A0 (1), for presheaves of modules.** Restriction of presheaves of `R`-modules
> along the open embedding `j`, `G ↦ (V ↦ G(V))` as a presheaf of `R|_U`-modules, is left adjoint
> to the pushforward `j_*` (with `R`-module structure through `R ⟶ j_* (R|_U)`). Since `j_p` on
> presheaves of modules is the left adjoint of `j_*` (Stacks 008U), this says that `j_p G` is
> given by `V ↦ G(V)`. Its underlying adjunction of presheaves of abelian groups is
> `restrictPresheafAdjunction Ab j hj`.

```lean
noncomputable def restrictPresheafOfModulesAdjunction :
    restrictPresheafOfModules.{v} j hj R ⊣ pushforwardPresheafOfModules.{v} j hj R
```

**`OpenImmersionSheaves.isIso_restrictPresheafOfModulesAdjunction_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleRestriction.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleRestriction.lean#L124). The attribute's comment: “(4) for presheaves of modules”.

> **Stacks 00A0 (4), for presheaves of modules.** The counit `j_p j_* ⟶ 𝟭` on presheaves of
> `R|_U`-modules is an isomorphism: on underlying presheaves of abelian groups it is the counit of
> `restrictPresheafAdjunction Ab j hj`, an isomorphism by `isIso_restrictPresheafAdjunction_counit`,
> and the forgetful functor to presheaves of abelian groups reflects isomorphisms.

```lean
theorem isIso_restrictPresheafOfModulesAdjunction_counit :
    IsIso (restrictPresheafOfModulesAdjunction.{v} j hj R).counit
```

**`OpenImmersionSheaves.restrictPresheafOfModulesIsoPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleRestriction.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleRestriction.lean#L142). The attribute's comment: “(1) for presheaves of modules, Mathlib's `PresheafOfModules.pullback`”.

> **Stacks 00A0 (1), for presheaves of modules, Mathlib's pullback.** Mathlib's
> `PresheafOfModules.pullback` along `R ⟶ j_* (R|_U)` — the left adjoint of `j_*` — is the
> restriction `G ↦ (V ↦ G(V))`.

```lean
noncomputable def restrictPresheafOfModulesIsoPullback :
    restrictPresheafOfModules.{v} j hj R ≅
      PresheafOfModules.pullback.{v} (ringHomPushforwardRestrict j hj R)
```

**`OpenImmersionSheaves.isIso_restrictSheafOfModulesAdj_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleRestriction.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleRestriction.lean#L162). The attribute's comment: “(5) for sheaves of modules”.

> **Stacks 00A0 (5), for sheaves of modules.** The counit `j⁻¹ j_* ⟶ 𝟭` of the adjunction
> `Stacks.SheafOfModules.restrictSheafOfModulesAdj` between restriction of sheaves of modules
> along the open embedding `f` and `j_*` is an isomorphism: its component at `F` and `V` is
> restriction along the equality `V = f⁻¹(f V)`.

```lean
theorem isIso_restrictSheafOfModulesAdj_counit :
    IsIso (restrictSheafOfModulesAdj.{v} hf R).counit
```

**`OpenImmersionSheaves.restrictSheafOfModulesIsoPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleRestriction.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleRestriction.lean#L191). The attribute's comment: “(2) for sheaves of modules: Mathlib's `SheafOfModules.pullback` is restriction”.

> **Stacks 00A0 (2), for sheaves of modules.** For a sheaf of `R`-modules `G`, `j⁻¹ G` — the
> pullback of sheaves of modules along `R ⟶ j_* (R|_U)`, i.e. the left adjoint of `j_*` (Mathlib's
> `SheafOfModules.pullback`, Stacks 008Y) — is given by the rule `V ↦ G(V)`: it is isomorphic to
> the restriction `Stacks.SheafOfModules.restrictSheafOfModules hf R`, whose underlying presheaf
> is `V ↦ G(f V)` and needs no sheafification.

```lean
noncomputable def restrictSheafOfModulesIsoPullback :
    restrictSheafOfModules.{v} hf R ≅
      SheafOfModules.pullback.{v} (pushforwardSheafOfRingsHom hf R)
```

Declarations registered for the tag:

- [`Stacks.SheafOfModules.stalkRestrictIso`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/StalkRestrictOpen.lean#L296), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleRestriction.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleRestriction.lean#L199) (StacksFrontier): “(3) for sheaves of modules: the stalk of the restriction of a sheaf of modules at `z` is its stalk at `f z`, semilinearly over the identification of stalks of rings”.

## Tag 00A1, a definition

[Tag 00A1](https://stacks.math.columbia.edu/tag/00A1) in the Stacks Project.

**`restrictPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean#L66). The attribute's comment: “(1)”. References: EGA 0 (3.1.5); SGA 3 I (2.1.1), “restriction G ↦ G\_S”; SGA 3 IV (4.3.17), “special case”.

> Restriction of a presheaf to an open subset: precomposition with the
> opposite of the open-embedding functor on opens.

```lean
def restrictPresheaf
    {C : Type*} [Category C] {X : TopCat}
    (G : TopCat.Presheaf C X) (U : Opens X) :
    TopCat.Presheaf C ((Opens.toTopCat X).obj U)
```

**`local_restrictSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean#L89). The attribute's comment: “(2)”. References: EGA 0 (3.1.5); EGA 0 (3.7.1), “special case”; SGA 4 III (1.9.2); SGA 4 III (5.3), “special case”.

> Restriction of a sheaf to an open subset, via the open-embedding sheaf pullback.

```lean
noncomputable def local_restrictSheaf
    {A : Type*} [Category A] {X : TopCat}
    (G : TopCat.Sheaf A X) (U : Opens X) :
    TopCat.Sheaf A ((Opens.toTopCat X).obj U)
```

**`openSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean#L110). The attribute's comment: “(3)”. References: EGA 0 (4.1.2), “special case”; SGA 2 I (1.7), “special case”; SGA 4 IV (14.1), “special case”.

> Open subspace of a ringed space `(X, 𝒪)` associated to an open `U ⊆ X`.

```lean
noncomputable def openSubspace
    (X : SheafedSpace CommRingCat) (U : Opens X) :
    SheafedSpace CommRingCat
```

**`restrictPresheafOfModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean#L128). The attribute's comment: “(4)”. References: SGA 3 I (3.1.4), “F ↦ F\_U for C = Opens(X)”; SGA 4 IV (11.2.2), “special case”; SGA 4 Vbis (1.3.7), “special case”.

> Restriction of a presheaf of `𝒪`-modules to an open subset, via
> `PresheafOfModules.pushforward` along the open-embedding functor.

```lean
noncomputable def restrictPresheafOfModules
    {X : TopCat} (𝒪 : (Opens X)ᵒᵖ ⥤ RingCat) (U : Opens X) :
    PresheafOfModules 𝒪 ⥤ PresheafOfModules (restrictPresheaf 𝒪 U)
```

## Tag 00A2, a definition

[Tag 00A2](https://stacks.math.columbia.edu/tag/00A2) in the Stacks Project.

**`TopCat.Presheaf.extendByInitial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L152). The attribute's comment: “(1)”.

> **Extension by an initial object.** For `j : U → X` the inclusion of an open subset,
> `C` a category with initial object `e`, and `F` a presheaf on `U` with values in `C`, this is
> the presheaf `j_{p!}F` on `X` with `j_{p!}F(V) = F(V)` for `V ⊆ U` and `j_{p!}F(V) = e`
> otherwise, with the obvious restriction maps.
>
> When `C` is a category of algebraic structures its zero object is initial, so this is the
> classical extension by zero of an abelian presheaf; and the initial object of `Type` is the
> empty type, so this is also the extension by the empty set of a presheaf of sets.
>
> The other clauses of Stacks 00A4 are registered on: `extendByInitialSheafify` and
> `extendByInitialSheaf` (2), the sheafification of `j_{p!}` for abelian sheaves;
> `AlgebraicStructureType.extendByInitialSheaf` (4), for sheaves of algebraic structures, whose
> sheafification is constructed rather than assumed; `extendByZeroPresheafOfModules` (5) and
> `extendByZeroSheafOfModules` (6), for (pre)sheaves of modules.

```lean
noncomputable def extendByInitial (F : Presheaf C (sp U)) : Presheaf C X
```

**`TopCat.Presheaf.extendByInitialFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L247). The attribute's comment: “(1)”.

> **Extension by an initial object, as a functor.** `j_{p!} : PSh(U) ⥤ PSh(X)`.

```lean
noncomputable def extendByInitialFunctor : Presheaf C (sp U) ⥤ Presheaf C X
```

**`TopCat.Presheaf.extendByInitialSheafify`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 489](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L489). The attribute's comment: “(2)”. References: SGA 4 III (1.9.2), “more general”.

> **Extension by an initial object for sheaves.** The extension `j_! F` of a sheaf `F` on
> `U` is the sheafification of the presheaf `j_{p!}F`.
>
> For a category of algebraic structures the initial object is the zero object, so this is the
> classical extension by zero of a sheaf; for `C = Type` the initial object is the empty type, so
> this is the extension by the empty set.

```lean
noncomputable def extendByInitialSheafify :
    Presheaf C (sp U) ⥤ TopCat.Sheaf C X
```

**`TopCat.Presheaf.extendByInitialSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L496). The attribute's comment: “(2)”. References: SGA 4 III (5.3), “opens of a top. space”.

> **Extension by an initial object, as a functor on sheaves.** `j_! : Sh(U) ⥤ Sh(X)` sends a
> sheaf `F` on `U` to the sheafification of `j_{p!}F`.

```lean
noncomputable def extendByInitialSheaf : TopCat.Sheaf C (sp U) ⥤ TopCat.Sheaf C X
```

## Tag 00A3, a lemma

[Tag 00A3](https://stacks.math.columbia.edu/tag/00A3) in the Stacks Project.

**`TopCat.Presheaf.extendByInitialAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L384). The attribute's comment: “(1) j\_\{p!} is a left adjoint to the restriction functor j\_p”. References: SGA 4 IV (11.3.1), “presheaf, constant ring”.

> **The extension-by-zero/restriction adjunction, presheaf level.** For `j : U → X` the
> inclusion of an open subset, `j_{p!}` is a left adjoint of the restriction functor `j_p`.

```lean
noncomputable def extendByInitialAdjunction :
    extendByInitialFunctor (C := C) U ⊣ restrictToOpen U
```

**`TopCat.Presheaf.restrictExtendByInitialIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L408). The attribute's comment: “(4) on presheaves on U we have j\_p j\_\{p!} = id”.

> **`j_p j_{p!} = id`.** The extension by an initial object of a presheaf on `U` restricts
> back to that presheaf, naturally in the presheaf.

```lean
noncomputable def restrictExtendByInitialIso :
    extendByInitialFunctor (C := C) U ⋙ restrictToOpen U ≅ 𝟭 (Presheaf C (sp U))
```

**`TopCat.Presheaf.extendByInitialSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 510](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L510). The attribute's comment: “(2) j\_! is a left adjoint to restriction on sheaves”. References: SGA 4 III (5.3), “j\_! ⊣ j^*, opens site”; SGA 4 IV (11.3.1), “sheaves on a space”; SGA 4 XVII (5.1.1), “topological spaces”.

> **The extension-by-zero/restriction adjunction, sheaf level.** `j_!` is a left adjoint of
> the restriction functor `j^{-1} : Sh(X) ⥤ Sh(U)`, i.e.
> `Mor_{Sh(X)}(j_!F, G) = Mor_{Sh(U)}(F, G|_U)` bifunctorially.
>
> Here `j^{-1}` is `TopologicalSpace.Opens.sheafRestrict U`, which is `G ↦ (W ↦ G(j(W)))` with no
> sheafification.

```lean
noncomputable def extendByInitialSheafAdjunction :
    extendByInitialSheaf U ⊣ Opens.sheafRestrict (C := C) U
```

**`TopCat.Presheaf.restrictExtendByInitialSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 539](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L539). The attribute's comment: “(5) on sheaves on U we have j^\{-1} j\_! = id”.

> **`j^{-1} j_! = id`.** The extension by an initial object of a sheaf on `U` restricts back
> to that sheaf, naturally in the sheaf. This is the unit of `j_! ⊣ j^{-1}`, inverted.

```lean
noncomputable def restrictExtendByInitialSheafIso :
    extendByInitialSheaf U ⋙ Opens.sheafRestrict (C := C) U ≅ 𝟭 _
```

**`TopCat.Presheaf.isInitialStalkExtendByInitialSheafify`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 625](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L625). The attribute's comment: “(3) the stalk of j\_!F at x ∉ U is initial (∅ for sheaves of sets)”.

> The stalk of `j_!F` at a point `x ∉ U` is an initial object.
> For sheaves of sets the initial object is `∅`, so this is `(j_!F)_x = ∅`; for abelian sheaves
> it is the zero object.

```lean
noncomputable def isInitialStalkExtendByInitialSheafify (F : Presheaf C (sp U)) {x : X}
    (hx : x ∉ U) :
    IsInitial (((extendByInitialSheafify U).obj F).presheaf.stalk x)
```

**`TopCat.Presheaf.stalkExtendByInitialSheafifyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 642](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L642). The attribute's comment: “(3) the stalk of j\_!F at a point of U is the stalk of F”.

> The stalk of `j_!F` at a point `j(x)` with `x ∈ U` is the stalk of `F` at `x`.

```lean
noncomputable def stalkExtendByInitialSheafifyIso (F : Presheaf C (sp U)) (x : sp U) :
    ((extendByInitialSheafify U).obj F).presheaf.stalk (U.inclusion' x) ≅ F.stalk x
```

**`TopCat.Presheaf.isEmpty_stalk_extendByInitialSheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 657](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L657). The attribute's comment: “(3) for sheaves of sets: (j\_!F)\_x = ∅ for x ∉ U”. References: SGA 4 III (1.9.2), “more general”.

> For a presheaf of sets `F` on `U`, the stalk of `j_!F` at a point outside `U` is empty:
> `(j_!F)_x = ∅`. This gives the inclusion of the essential image of `j_!` in the sheaves with
> empty stalks outside `U`; the complete Stacks 00A8 is
> `TopCat.Presheaf.extendByInitialSheaf_full_faithful_and_mem_essImage_iff`.

```lean
theorem isEmpty_stalk_extendByInitialSheafify {X : TopCat.{u}} (U : Opens X)
    (F : Presheaf (Type u) (sp U)) {x : X} (hx : x ∉ U) :
    IsEmpty (stalk ((extendByInitialSheafify U).obj F).presheaf x)
```

## Tag 00A4, a definition

[Tag 00A4](https://stacks.math.columbia.edu/tag/00A4) in the Stacks Project.

**`AlgebraicStructureType.extendByInitialSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean#L170). The attribute's comment: “(4)”.

> **Extension by the initial object of a sheaf of algebraic structures.** For `(C, F)` a type
> of algebraic structure such that `C` has an initial object `e`, the extension `j_!𝓕` by `e` of a
> sheaf `𝓕` of algebraic structures on `U` is the sheafification of the presheaf `j_{p!}𝓕`, as a
> functor `Sh(U, C) ⥤ Sh(X, C)`. The sheafification is `sheafifyFunctor`, the plus construction
> applied twice, which exists for every type of algebraic structure, so no sheafification
> hypothesis on `C` is made.

```lean
noncomputable def extendByInitialSheaf : TopCat.Sheaf S.C (sp U) ⥤ TopCat.Sheaf S.C X
```

**`TopCat.Presheaf.extendByInitial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L152). The attribute's comment: “(1), (3)”.

> **Extension by an initial object.** For `j : U → X` the inclusion of an open subset,
> `C` a category with initial object `e`, and `F` a presheaf on `U` with values in `C`, this is
> the presheaf `j_{p!}F` on `X` with `j_{p!}F(V) = F(V)` for `V ⊆ U` and `j_{p!}F(V) = e`
> otherwise, with the obvious restriction maps.
>
> When `C` is a category of algebraic structures its zero object is initial, so this is the
> classical extension by zero of an abelian presheaf; and the initial object of `Type` is the
> empty type, so this is also the extension by the empty set of a presheaf of sets.
>
> The other clauses of Stacks 00A4 are registered on: `extendByInitialSheafify` and
> `extendByInitialSheaf` (2), the sheafification of `j_{p!}` for abelian sheaves;
> `AlgebraicStructureType.extendByInitialSheaf` (4), for sheaves of algebraic structures, whose
> sheafification is constructed rather than assumed; `extendByZeroPresheafOfModules` (5) and
> `extendByZeroSheafOfModules` (6), for (pre)sheaves of modules.

```lean
noncomputable def extendByInitial (F : Presheaf C (sp U)) : Presheaf C X
```

**`TopCat.Presheaf.extendByInitialFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L247). The attribute's comment: “(1), (3)”.

> **Extension by an initial object, as a functor.** `j_{p!} : PSh(U) ⥤ PSh(X)`.

```lean
noncomputable def extendByInitialFunctor : Presheaf C (sp U) ⥤ Presheaf C X
```

**`TopCat.Presheaf.extendByInitialSheafify`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 489](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L489). The attribute's comment: “(2)”. References: SGA 4 III (1.9.2), “more general”.

> **Extension by an initial object for sheaves.** The extension `j_! F` of a sheaf `F` on
> `U` is the sheafification of the presheaf `j_{p!}F`.
>
> For a category of algebraic structures the initial object is the zero object, so this is the
> classical extension by zero of a sheaf; for `C = Type` the initial object is the empty type, so
> this is the extension by the empty set.

```lean
noncomputable def extendByInitialSheafify :
    Presheaf C (sp U) ⥤ TopCat.Sheaf C X
```

**`TopCat.Presheaf.extendByInitialSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L496). The attribute's comment: “(2)”. References: SGA 4 III (5.3), “opens of a top. space”.

> **Extension by an initial object, as a functor on sheaves.** `j_! : Sh(U) ⥤ Sh(X)` sends a
> sheaf `F` on `U` to the sheafification of `j_{p!}F`.

```lean
noncomputable def extendByInitialSheaf : TopCat.Sheaf C (sp U) ⥤ TopCat.Sheaf C X
```

**`TopCat.Presheaf.extendByZeroPresheafOfModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZeroModules.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZeroModules.lean#L195). The attribute's comment: “(5)”.

> **Extension by zero of a presheaf of modules** (Stacks 00A4 (5)). Let `𝒪` be a presheaf of
> rings on `X` and `ℱ` a presheaf of `𝒪|_U`-modules, where `𝒪|_U` is the presheaf `W ↦ 𝒪(j(W))`
> on `U`. The extension by zero `j_{p!}ℱ` is the presheaf of `𝒪`-modules which is equal to the
> extension by zero `j_{p!}ℱ` of the underlying abelian presheaf of `ℱ`
> (`extendByZeroPresheafOfModules_presheaf`), endowed with the multiplication
> `𝒪 × j_{p!}ℱ → j_{p!}ℱ`: over an open `V ⊆ U` a section of `𝒪` acts on `ℱ(j⁻¹ V)` through
> its restriction to `𝒪|_U(j⁻¹ V)` (`extendByZeroPresheafOfModules_smul_of_le`), and over an open
> `V ⊄ U` the sections form the zero module.

```lean
noncomputable def extendByZeroPresheafOfModules (F : PresheafOfModules.{v} ((imF U).op ⋙ O)) :
    PresheafOfModules.{v} O
```

**`TopCat.Presheaf.extendByZeroSheafOfModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZeroModules.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZeroModules.lean#L228). The attribute's comment: “(6)”.

> **Extension by zero of a sheaf of modules** (Stacks 00A4 (6)). Let `𝒪` be a sheaf of rings
> on `X` and `ℱ` a sheaf of `𝒪|_U`-modules. The extension by zero `j_!ℱ` is the sheaf of
> `𝒪`-modules which is equal to the extension by zero `j_!ℱ` of the underlying abelian sheaf of
> `ℱ`, i.e. the sheafification of `j_{p!}ℱ` (`extendByZeroSheafOfModules_val_presheaf`), endowed
> with the multiplication `𝒪 × j_!ℱ → j_!ℱ` induced by that of `j_{p!}ℱ`: the sheafification map
> `j_{p!}ℱ ⟶ j_!ℱ` is `𝒪`-linear (`toExtendByZeroSheafOfModules`).

```lean
noncomputable def extendByZeroSheafOfModules
    (F : SheafOfModules.{u} ((Opens.sheafRestrict U).obj O)) :
    SheafOfModules.{u} O
```

## Tag 00A5, a lemma

[Tag 00A5](https://stacks.math.columbia.edu/tag/00A5) in the Stacks Project.

**`TopCat.Presheaf.extendByInitialAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L384). The attribute's comment: “(1)”. References: SGA 4 IV (11.3.1), “presheaf, constant ring”.

> **The extension-by-zero/restriction adjunction, presheaf level.** For `j : U → X` the
> inclusion of an open subset, `j_{p!}` is a left adjoint of the restriction functor `j_p`.

```lean
noncomputable def extendByInitialAdjunction :
    extendByInitialFunctor (C := C) U ⊣ restrictToOpen U
```

**`TopCat.Presheaf.restrictExtendByInitialIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L408). The attribute's comment: “(4)”.

> **`j_p j_{p!} = id`.** The extension by an initial object of a presheaf on `U` restricts
> back to that presheaf, naturally in the presheaf.

```lean
noncomputable def restrictExtendByInitialIso :
    extendByInitialFunctor (C := C) U ⋙ restrictToOpen U ≅ 𝟭 (Presheaf C (sp U))
```

**`TopCat.Presheaf.extendByInitialSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 510](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L510). The attribute's comment: “(2)”. References: SGA 4 III (5.3), “j\_! ⊣ j^*, opens site”; SGA 4 IV (11.3.1), “sheaves on a space”; SGA 4 XVII (5.1.1), “topological spaces”.

> **The extension-by-zero/restriction adjunction, sheaf level.** `j_!` is a left adjoint of
> the restriction functor `j^{-1} : Sh(X) ⥤ Sh(U)`, i.e.
> `Mor_{Sh(X)}(j_!F, G) = Mor_{Sh(U)}(F, G|_U)` bifunctorially.
>
> Here `j^{-1}` is `TopologicalSpace.Opens.sheafRestrict U`, which is `G ↦ (W ↦ G(j(W)))` with no
> sheafification.

```lean
noncomputable def extendByInitialSheafAdjunction :
    extendByInitialSheaf U ⊣ Opens.sheafRestrict (C := C) U
```

**`TopCat.Presheaf.restrictExtendByInitialSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 539](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L539). The attribute's comment: “(5)”.

> **`j^{-1} j_! = id`.** The extension by an initial object of a sheaf on `U` restricts back
> to that sheaf, naturally in the sheaf. This is the unit of `j_! ⊣ j^{-1}`, inverted.

```lean
noncomputable def restrictExtendByInitialSheafIso :
    extendByInitialSheaf U ⋙ Opens.sheafRestrict (C := C) U ≅ 𝟭 _
```

**`TopCat.Presheaf.isZero_stalk_extendByInitialSheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 633](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L633). The attribute's comment: “(3)”. References: SGA 4 III (1.9.2), “stalk at x∉Y is zero”.

> When the value category has a zero object — as the categories of abelian groups and of
> modules do — the stalk of `j_!F` at a point `x ∉ U` is a *zero* object.

```lean
theorem isZero_stalk_extendByInitialSheafify [HasZeroObject C] (F : Presheaf C (sp U)) {x : X}
    (hx : x ∉ U) :
    IsZero (((extendByInitialSheafify U).obj F).presheaf.stalk x)
```

**`TopCat.Presheaf.stalkExtendByInitialSheafifyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 642](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L642). The attribute's comment: “(3)”.

> The stalk of `j_!F` at a point `j(x)` with `x ∈ U` is the stalk of `F` at `x`.

```lean
noncomputable def stalkExtendByInitialSheafifyIso (F : Presheaf C (sp U)) (x : sp U) :
    ((extendByInitialSheafify U).obj F).presheaf.stalk (U.inclusion' x) ≅ F.stalk x
```

## Tag 00A6, a lemma

[Tag 00A6](https://stacks.math.columbia.edu/tag/00A6) in the Stacks Project.

**`AlgebraicStructureType.extendByInitialAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean#L153). The attribute's comment: “(1) j\_\{p!} is a left adjoint to the restriction functor j\_p”.

> **Stacks 00A6 (1).** On presheaves of algebraic structures, the extension by the initial
> object `j_{p!}` is a left adjoint of the restriction functor `j_p`.

```lean
noncomputable def extendByInitialAdjunction :
    extendByInitialFunctor (C := S.C) U ⊣ restrictToOpen U
```

**`AlgebraicStructureType.restrictExtendByInitialIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean#L159). The attribute's comment: “(4) on presheaves of algebraic structures on U we have j\_p j\_\{p!} = id”.

> **Stacks 00A6 (4).** On presheaves of algebraic structures on `U`, `j_p j_{p!} = id`.

```lean
noncomputable def restrictExtendByInitialIso :
    extendByInitialFunctor (C := S.C) U ⋙ restrictToOpen U ≅ 𝟭 (TopCat.Presheaf S.C (sp U))
```

**`AlgebraicStructureType.extendByInitialSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean#L176). The attribute's comment: “(2) j\_! is a left adjoint to restriction on sheaves, bifunctorially”.

> **Stacks 00A6 (2).** `j_!` is a left adjoint of the restriction `j^{-1} : Sh(X, C) ⥤ Sh(U, C)`,
> `𝓖 ↦ 𝓖|_U`: `Mor(j_!𝓕, 𝓖) = Mor(𝓕, 𝓖|_U)` bifunctorially in `𝓕` and `𝓖`.

```lean
noncomputable def extendByInitialSheafAdjunction :
    S.extendByInitialSheaf U ⊣ Opens.sheafRestrict (C := S.C) U
```

**`AlgebraicStructureType.restrictExtendByInitialSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean#L200). The attribute's comment: “(5) on sheaves of algebraic structures on U we have j^\{-1} j\_! = id”.

> **Stacks 00A6 (5).** On sheaves of algebraic structures on `U`, `j^{-1} j_! = id`.

```lean
noncomputable def restrictExtendByInitialSheafIso :
    S.extendByInitialSheaf U ⋙ Opens.sheafRestrict (C := S.C) U ≅ 𝟭 _
```

**`AlgebraicStructureType.isInitialStalkExtendByInitialSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean#L239). The attribute's comment: “(3) the stalk of j\_!F at a point x ∉ U is the initial object e”.

> **Stacks 00A6 (3), points outside `U`.** For a sheaf `𝓕` of algebraic structures on `U`
> and `x ∉ U`, the stalk `(j_!𝓕)_x` is the initial object `e`.

```lean
noncomputable def isInitialStalkExtendByInitialSheaf (F : TopCat.Sheaf S.C (sp U)) {x : X}
    (hx : x ∉ U) :
    IsInitial ((CategoryStalk.stalkFunctor S.C x).obj ((S.extendByInitialSheaf U).obj F).obj)
```

**`AlgebraicStructureType.stalkExtendByInitialSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean#L247). The attribute's comment: “(3) the stalk of j\_!F at a point x ∈ U is the stalk F\_x”.

> **Stacks 00A6 (3), points of `U`.** For a sheaf `𝓕` of algebraic structures on `U` and
> `x ∈ U`, the stalk `(j_!𝓕)_x` is the stalk `𝓕_x`.

```lean
noncomputable def stalkExtendByInitialSheafIso (F : TopCat.Sheaf S.C (sp U)) {x : X}
    (hx : x ∈ U) :
    (CategoryStalk.stalkFunctor S.C x).obj ((S.extendByInitialSheaf U).obj F).obj ≅
      (CategoryStalk.stalkFunctor S.C (⟨x, hx⟩ : sp U)).obj F.obj
```

## Tag 00A7, a lemma

[Tag 00A7](https://stacks.math.columbia.edu/tag/00A7) in the Stacks Project.

**`ExtensionByZeroModules.extendByZeroAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZeroExplicit.lean, line 480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZeroExplicit.lean#L480). The attribute's comment: “(1): `j_{p!}` is the explicit extension by zero of presheaves of modules”.

> **Stacks 00A7 (1).** The explicit extension by zero `j_{p!}` of presheaves of modules
> (`V ↦ F(V)` for `V ⊆ U`, `V ↦ 0` otherwise, `ExtensionByZeroModules.extendByZero`) is left adjoint
> to the restriction functor `PMod(𝒪) ⥤ PMod(𝒪|_U)`, `G ↦ G|_U`: `Hom(j_{p!}F, G) = Hom(F, G|_U)`,
> naturally in `F` and `G`. The bijection sends `φ` to `t ↦ φ(t)` over opens of `U`, and `ψ` to
> the map which is `ψ` over opens `V ⊆ U` and zero over the other opens.

```lean
noncomputable def extendByZeroAdjunction : extendByZero U O ⊣ jpStar U O
```

**`ExtensionByZeroModules.jShriekExplicitAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZeroExplicit.lean, line 514](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZeroExplicit.lean#L514). The attribute's comment: “(2): `j_!` is the sheafification of the explicit `j_{p!}`”.

> **Stacks 00A7 (2).** Extension by zero `j_!` of sheaves of modules, the sheafification of the
> explicit `j_{p!}`, is left adjoint to the restriction functor `Mod(𝒪) ⥤ Mod(𝒪|_U)`:
> `Hom(j_!F, G) = Hom(F, G|_U)`, naturally in `F` and `G`. It is obtained from the adjunction of (1)
> and the sheafification adjunction, through the identification `jShriekExplicitIso`.

```lean
noncomputable def jShriekExplicitAdjunction : jShriekExplicit U O ⊣ jStar U O
```

**`ExtensionByZeroModules.isZero_stalk_jShriekExplicit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZeroExplicit.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZeroExplicit.lean#L521). The attribute's comment: “(3), the stalk of `j_!F` at `x ∉ U` is zero”.

> **Stacks 00A7 (3), points outside `U`.** For a sheaf `F` of `𝒪|_U`-modules and `x ∉ U`, the
> stalk `(j_!F)_x` is zero. The statement is about the underlying abelian group of the
> `𝒪_{X,x}`-module `(j_!F)_x`, which vanishes exactly when the module does.

```lean
theorem isZero_stalk_jShriekExplicit (F : SheafOfModules.{u} (resRing U O)) (x : X) (hx : x ∉ U) :
    IsZero (TopCat.Presheaf.stalk (X := X) ((jShriekExplicit U O).obj F).val.presheaf x)
```

**`ExtensionByZeroModules.jShriekExplicitCompJStarIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZeroExplicit.lean, line 541](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZeroExplicit.lean#L541). The attribute's comment: “(4): `j^{-1} j_! ≅ id` on sheaves of `𝒪|_U`-modules”.

> **Stacks 00A7 (4).** `j^{-1} j_! = id` on sheaves of `𝒪|_U`-modules: restricting the extension
> by zero of `F` back to `U` gives `F`, naturally in `F`.

```lean
noncomputable def jShriekExplicitCompJStarIso :
    jShriekExplicit U O ⋙ jStar U O ≅ 𝟭 (SheafOfModules.{u} (resRing U O))
```

**`ExtensionByZeroModules.stalkJShriekExplicitLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZeroExplicit.lean, line 701](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZeroExplicit.lean#L701). The attribute's comment: “(3), the stalk of `j_!F` at `x ∈ U` is `F_x`, linearly over `𝒪_{X,x} ≅ 𝒪|_U,x`”.

> **Stacks 00A7 (3), points of `U`.** For a sheaf `F` of `𝒪|_U`-modules and a point `x ∈ U`
> (written `x = j u` with `u` the point `x` of the subspace `U`), the stalk `(j_!F)_x` is `F_x` as
> modules. The stalk `(j_!F)_x` is an `𝒪_{X,x}`-module, `F_x` is an
> `𝒪|_U,x`-module, and the identification is linear along the canonical isomorphism
> `𝒪_{X,x} ≅ 𝒪|_U,x` (`stalkResRingIso`): it is an isomorphism of `𝒪_{X,x}`-modules from
> `(j_!F)_x` to `F_x` with scalars restricted along that ring isomorphism. Its underlying additive
> map is `stalkJShriekExplicitAddIso`.

```lean
noncomputable def stalkJShriekExplicitLinearEquiv (F : SheafOfModules.{u} (resRing U O))
    (u : Usp U) :
    TopCat.Presheaf.stalk (C := AddCommGrpCat.{u}) (X := X)
        ((jShriekExplicit U O).obj F).val.presheaf (U.inclusion' u) ≃ₗ[
          TopCat.Presheaf.stalk (C := RingCat.{u}) (X := X) O.obj (U.inclusion' u)]
      (ModuleCat.restrictScalars (stalkResRingIso U O u).hom.hom).obj
        (ModuleCat.of
          (TopCat.Presheaf.stalk (C := RingCat.{u}) (X := Usp U) (resRing U O).obj u)
          (TopCat.Presheaf.stalk (C := AddCommGrpCat.{u}) (X := Usp U) F.val.presheaf u))
```

## Tag 00A8, a lemma

[Tag 00A8](https://stacks.math.columbia.edu/tag/00A8) in the Stacks Project.

**`TopCat.Presheaf.extendByInitialSheaf_full_faithful_and_mem_essImage_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 747](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L747).

> **Stacks 00A8.** Let `j : U → X` be the inclusion of an open subset. The functor
> `j_! : Sh(U) ⥤ Sh(X)` on sheaves of sets is fully faithful, and its essential image consists
> exactly of the sheaves `G` on `X` with `G_x = ∅` for all `x ∈ X \ U`.

```lean
theorem extendByInitialSheaf_full_faithful_and_mem_essImage_iff :
    (extendByInitialSheaf (C := Type u) U).Full ∧
      (extendByInitialSheaf (C := Type u) U).Faithful ∧
      ∀ G : TopCat.Sheaf (Type u) X,
        (extendByInitialSheaf U).essImage G ↔ ∀ x : X, x ∉ U → IsEmpty (G.presheaf.stalk x)
```

## Tag 00A9, a lemma

[Tag 00A9](https://stacks.math.columbia.edu/tag/00A9) in the Stacks Project.

**`ExtensionByZero.jExt_full`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZero.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZero.lean#L92). The attribute's comment: “(1)”.

> **Stacks 00A9 (1).** The extension by zero functor `j_!` is full: every morphism
> `j_! F ⟶ j_! F'` of sheaves on `X` comes from a morphism `F ⟶ F'` of sheaves on `U`.

```lean
theorem jExt_full : (jExt U).Full
```

**`ExtensionByZero.jExt_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZero.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZero.lean#L98). The attribute's comment: “(1)”. References: SGA 4 IV (11.3.1), “special case”.

> **Stacks 00A9 (1).** The extension by zero functor `j_!` is faithful: a morphism of sheaves
> on `U` is determined by the morphism it induces on the extensions by zero.

```lean
theorem jExt_faithful : (jExt U).Faithful
```

**`ExtensionByZero.jExt_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZero.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZero.lean#L148). The attribute's comment: “(2)”. References: SGA 4 XVII (5.1.1), “partial”.

> **Stacks 00A9 (2), description of the essential image.** An abelian sheaf `G` on `X` lies in
> the essential image of `j_!` if and only if the stalk `G_x` is the zero abelian group for every
> point `x ∈ X` not belonging to `U`.
>
> For "only if", an isomorphism `G ≅ j_! F` induces an isomorphism of stalks, and the stalk of
> `j_! F` at a point outside `U` is zero. For "if", the vanishing hypothesis makes the counit
> `j_! (j⁻¹ G) ⟶ G` an isomorphism, which exhibits `G` in the essential image.

```lean
theorem jExt_essImage (G : TopCat.Sheaf AddCommGrpCat.{u} X) :
    (jExt U).essImage G ↔ ∀ x : X, x ∉ U → IsZero (G.presheaf.stalk x)
```

## Tag 00AA, a lemma

[Tag 00AA](https://stacks.math.columbia.edu/tag/00AA) in the Stacks Project.

**`AlgebraicStructureType.extendByInitialSheaf_full_faithful_and_mem_essImage_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/ExtensionByInitial.lean#L350).

> **Stacks 00AA.** Let `X` be a topological space, `j : U → X` the inclusion of an open
> subset, and `(C, F)` a type of algebraic structure (Stacks 007L) such that `C` has an initial
> object `e`. Then `j_! : Sh(U, C) ⥤ Sh(X, C)` is fully faithful, and its essential image
> consists exactly of the sheaves `𝓖` with `𝓖_x = e` (that is, `𝓖_x` initial) for all
> `x ∈ X ∖ U`.
>
> The homs of `C` live in the universe of `X` and its objects in any universe, so `C` may be
> `Type v`, `Ab.{v}`, `CommRingCat.{v}`, …; nothing beyond 007L and the initial object is
> assumed. `j_!` is `extendByInitialSheaf`, the sheafification of the source's `j_{p!}`, and
> the stalk is the filtered colimit of Stacks 007H.

```lean
theorem extendByInitialSheaf_full_faithful_and_mem_essImage_iff :
    (S.extendByInitialSheaf U).Full ∧ (S.extendByInitialSheaf U).Faithful ∧
      ∀ G : TopCat.Sheaf S.C X, (S.extendByInitialSheaf U).essImage G ↔
        ∀ x : X, x ∉ U →
          Nonempty (IsInitial ((CategoryStalk.stalkFunctor S.C x).obj G.obj))
```

## Tag 00AB, a lemma

[Tag 00AB](https://stacks.math.columbia.edu/tag/00AB) in the Stacks Project.

**`ExtensionByZeroModules.full_and_faithful_and_essImage_jShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZero.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZero.lean#L395). References: SGA 4 IV (11.3.1), “special case”.

> **Stacks 00AB.** Let `(X, 𝒪)` be a ringed space and let `j : (U, 𝒪|_U) → (X, 𝒪)` be an open
> subspace. The extension-by-zero functor `j_! : Mod(𝒪|_U) ⥤ Mod(𝒪)` is fully faithful, and its
> essential image consists exactly of those sheaves `G` of `𝒪`-modules with `G_x = 0` for all
> `x ∈ X ∖ U`.
>
> The stalk `G_x` is a module over the stalk `𝒪_x` whose underlying abelian group is the stalk of
> the underlying abelian sheaf of `G` (Mathlib's `PresheafOfModules.instModuleStalk`), and a module
> is zero exactly when its underlying group is; so `G_x = 0` is expressed here as vanishing of that
> abelian group. The sheaf of rings is allowed to be non-commutative, which is more general than
> the ringed spaces of the source.

```lean
theorem full_and_faithful_and_essImage_jShriek :
    (jShriek U O).Full ∧ (jShriek U O).Faithful ∧
      ∀ G : SheafOfModules.{u} O, (jShriek U O).essImage G ↔
        ∀ x : X, x ∉ U → IsZero (TopCat.Presheaf.stalk (X := X) G.val.presheaf x)
```

## Tag 00AC, a remark

[Tag 00AC](https://stacks.math.columbia.edu/tag/00AC) in the Stacks Project.

**`TopCat.Presheaf.isEmpty_isTerminal_extendByInitialSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/NotLeftExact.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/NotLeftExact.lean#L68). The attribute's comment: “j\_! does not transform a final object of Sh(U) into a final object of Sh(X)”.

> **Stacks 00AC, first half.** For `U ≠ X` the sheaf `j_!F` is not a final object of
> `Sh(X, Type)`, whatever the sheaf `F` on `U` is. In particular `j_!` does not transform a final
> object of `Sh(U)` into a final object of `Sh(X)`.
>
> A final object of a category of sheaves of sets has a one-point set of sections over every open,
> because `Sheaf.forget` and evaluation at an open both preserve limits; but the global sections of
> `j_!F` are empty by `isEmpty_sections_extendByInitialSheafify`.

```lean
theorem isEmpty_isTerminal_extendByInitialSheaf (hU : U ≠ ⊤)
    (F : TopCat.Sheaf (Type u) (sp U)) :
    IsEmpty (IsTerminal ((extendByInitialSheaf U).obj F))
```

**`TopCat.Presheaf.not_preservesFiniteLimits_extendByInitialSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/NotLeftExact.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/OpenImmersion/NotLeftExact.lean#L86). The attribute's comment: “j\_! is not left exact as a functor between the categories of sheaves of sets”.

> **Stacks 00AC.** For `U ≠ X` the functor `j_! : Sh(U, Type) ⥤ Sh(X, Type)` does not preserve
> finite limits, i.e. it is not left exact.
>
> The final object is the limit of the empty diagram, so a functor preserving finite limits would
> send the final object of `Sh(U, Type)` to a final object of `Sh(X, Type)`, contradicting
> `isEmpty_isTerminal_extendByInitialSheaf`.

```lean
theorem not_preservesFiniteLimits_extendByInitialSheaf (hU : U ≠ ⊤) :
    ¬ PreservesFiniteLimits
      (extendByInitialSheaf U : TopCat.Sheaf (Type u) (sp U) ⥤ TopCat.Sheaf (Type u) X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.31, Tag 009Z](https://stacks.math.columbia.edu/tag/009Z)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
