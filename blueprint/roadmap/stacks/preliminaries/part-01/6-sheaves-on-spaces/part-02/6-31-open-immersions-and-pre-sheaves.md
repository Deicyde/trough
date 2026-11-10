---
declaration: section
origin: cited
lean: OpenImmersionSheaves.presheaf_pullback_iso_restriction, OpenImmersionSheaves.sheaf_pullback_iso_restriction, OpenImmersionSheaves.stalk_sheaf_pullback_iso, OpenImmersionSheaves.presheaf_pullback_pushforward_counit_isIso, OpenImmersionSheaves.sheaf_pullback_pushforward_counit_isIso, restrictPresheaf, local_restrictSheaf, openSubspace
statement: formalized
proof: formalized
---

# 6.31 Open immersions and (pre)sheaves

Section 6.31 of the Stacks Project, [Tag 009Z](https://stacks.math.columbia.edu/tag/009Z). 13 tags here are carried by 47 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00A0, a lemma

[Tag 00A0](https://stacks.math.columbia.edu/tag/00A0) in the Stacks Project.

**`OpenImmersionSheaves.presheaf_pullback_iso_restriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean#L82). The attribute's comment: “(1)”.

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

**`OpenImmersionSheaves.sheaf_pullback_iso_restriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean#L107). The attribute's comment: “(2)”. References: EGA 0 (3.7.1), “special case”; SGA 4 III (2.7), “Φ^* ≅ (i^{-1})^s”; SGA 4 III (5.3), “Clause 2, special case”.

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

**`OpenImmersionSheaves.stalk_sheaf_pullback_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean#L122). The attribute's comment: “(3)”.

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

**`OpenImmersionSheaves.presheaf_pullback_pushforward_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean#L245). The attribute's comment: “(4)”. References: SGA 4 IV (9.2.4), “a), special case”.

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

**`OpenImmersionSheaves.sheaf_pullback_pushforward_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/Basic.lean#L268). The attribute's comment: “(5)”. References: EGA I (9.4.2), “(i)”; SGA 4 IV (9.2.4), “a), special case”.

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

## Tag 00A1, a definition

[Tag 00A1](https://stacks.math.columbia.edu/tag/00A1) in the Stacks Project.

**`restrictPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean#L66). The attribute's comment: “(1)”. References: EGA 0 (3.1.5); SGA 3 I (2.1.1), “restriction G ↦ G_S”; SGA 3 IV (4.3.17), “special case”.

> Restriction of a presheaf to an open subset: precomposition with the
> opposite of the open-embedding functor on opens.

```lean
def restrictPresheaf
    {C : Type*} [Category C] {X : TopCat}
    (G : TopCat.Presheaf C X) (U : Opens X) :
    TopCat.Presheaf C ((Opens.toTopCat X).obj U)
```

**`local_restrictSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean#L89). The attribute's comment: “(2)”. References: EGA 0 (3.1.5); EGA 0 (3.7.1), “special case”; SGA 4 III (1.9.2); SGA 4 III (5.3), “special case”.

> Restriction of a sheaf to an open subset, via the open-embedding sheaf pullback.

```lean
noncomputable def local_restrictSheaf
    {A : Type*} [Category A] {X : TopCat}
    (G : TopCat.Sheaf A X) (U : Opens X) :
    TopCat.Sheaf A ((Opens.toTopCat X).obj U)
```

**`openSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean#L110). The attribute's comment: “(3)”. References: EGA 0 (4.1.2), “special case”; SGA 2 I (1.7), “special case”; SGA 4 IV (14.1), “special case”.

> Open subspace of a ringed space `(X, 𝒪)` associated to an open `U ⊆ X`.

```lean
noncomputable def openSubspace
    (X : SheafedSpace CommRingCat) (U : Opens X) :
    SheafedSpace CommRingCat
```

**`restrictPresheafOfModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/Restriction.lean#L128). The attribute's comment: “(4)”. References: SGA 3 I (3.1.4), “F ↦ F_U for C = Opens(X)”; SGA 4 IV (11.2.2), “special case”; SGA 4 Vbis (1.3.7), “special case”.

> Restriction of a presheaf of `𝒪`-modules to an open subset, via
> `PresheafOfModules.pushforward` along the open-embedding functor.

```lean
noncomputable def restrictPresheafOfModules
    {X : TopCat} (𝒪 : (Opens X)ᵒᵖ ⥤ RingCat) (U : Opens X) :
    PresheafOfModules 𝒪 ⥤ PresheafOfModules (restrictPresheaf 𝒪 U)
```

## Tag 00A2, a definition

[Tag 00A2](https://stacks.math.columbia.edu/tag/00A2) in the Stacks Project.

**`TopCat.Presheaf.extendByInitial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L142). The attribute's comment: “(1)”.

> **Extension by an initial object.** For `j : U → X` the inclusion of an open subset,
> `C` a category with initial object `e`, and `F` a presheaf on `U` with values in `C`, this is
> the presheaf `j_{p!}F` on `X` with `j_{p!}F(V) = F(V)` for `V ⊆ U` and `j_{p!}F(V) = e`
> otherwise, with the obvious restriction maps.
>
> When `C` is a category of algebraic structures its zero object is initial, so this is the
> classical extension by zero of an abelian presheaf; and the initial object of `Type` is the
> empty type, so this is also the extension by the empty set of a presheaf of sets.

```lean
noncomputable def extendByInitial (F : Presheaf C (sp U)) : Presheaf C X
```

**`TopCat.Presheaf.extendByInitialFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L237). The attribute's comment: “(1)”.

> **Extension by an initial object, as a functor.** `j_{p!} : PSh(U) ⥤ PSh(X)`.

```lean
noncomputable def extendByInitialFunctor : Presheaf C (sp U) ⥤ Presheaf C X
```

**`TopCat.Presheaf.extendByInitialSheafify`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L479). The attribute's comment: “(2)”. References: SGA 4 III (1.9.2), “more general”.

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

**`TopCat.Presheaf.extendByInitialSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L486). The attribute's comment: “(2)”. References: SGA 4 III (5.3), “opens of a top. space”.

> **Extension by an initial object, as a functor on sheaves.** `j_! : Sh(U) ⥤ Sh(X)` sends a
> sheaf `F` on `U` to the sheafification of `j_{p!}F`.

```lean
noncomputable def extendByInitialSheaf : TopCat.Sheaf C (sp U) ⥤ TopCat.Sheaf C X
```

## Tag 00A3, a lemma

[Tag 00A3](https://stacks.math.columbia.edu/tag/00A3) in the Stacks Project.

**`TopCat.Presheaf.extendByInitialAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L374). The attribute's comment: “(1) j_{p!} is a left adjoint to the restriction functor j_p”. References: SGA 4 IV (11.3.1), “presheaf, constant ring”.

> **The extension-by-zero/restriction adjunction, presheaf level.** For `j : U → X` the
> inclusion of an open subset, `j_{p!}` is a left adjoint of the restriction functor `j_p`.

```lean
noncomputable def extendByInitialAdjunction :
    extendByInitialFunctor (C := C) U ⊣ restrictToOpen U
```

**`TopCat.Presheaf.restrictExtendByInitialIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L398). The attribute's comment: “(4) on presheaves on U we have j_p j_{p!} = id”.

> **`j_p j_{p!} = id`.** The extension by an initial object of a presheaf on `U` restricts
> back to that presheaf, naturally in the presheaf.

```lean
noncomputable def restrictExtendByInitialIso :
    extendByInitialFunctor (C := C) U ⋙ restrictToOpen U ≅ 𝟭 (Presheaf C (sp U))
```

**`TopCat.Presheaf.extendByInitialSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L500). The attribute's comment: “(2) j_! is a left adjoint to restriction on sheaves”. References: SGA 4 III (5.3), “j_! ⊣ j^*, opens site”; SGA 4 IV (11.3.1), “sheaves on a space”; SGA 4 XVII (5.1.1), “topological spaces”.

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

**`TopCat.Presheaf.restrictExtendByInitialSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L529). The attribute's comment: “(5) on sheaves on U we have j^{-1} j_! = id”.

> **`j^{-1} j_! = id`.** The extension by an initial object of a sheaf on `U` restricts back
> to that sheaf, naturally in the sheaf. This is the unit of `j_! ⊣ j^{-1}`, inverted.

```lean
noncomputable def restrictExtendByInitialSheafIso :
    extendByInitialSheaf U ⋙ Opens.sheafRestrict (C := C) U ≅ 𝟭 _
```

**`TopCat.Presheaf.isInitialStalkExtendByInitialSheafify`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 612](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L612). The attribute's comment: “(3) the stalk of j_!F at x ∉ U is initial (∅ for sheaves of sets)”.

> The stalk of `j_!F` at a point `x ∉ U` is an initial object.
> For sheaves of sets the initial object is `∅`, so this is `(j_!F)_x = ∅`; for abelian sheaves
> it is the zero object.

```lean
noncomputable def isInitialStalkExtendByInitialSheafify (F : Presheaf C (sp U)) {x : X}
    (hx : x ∉ U) :
    IsInitial (((extendByInitialSheafify U).obj F).presheaf.stalk x)
```

**`TopCat.Presheaf.stalkExtendByInitialSheafifyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 629](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L629). The attribute's comment: “(3) the stalk of j_!F at a point of U is the stalk of F”.

> The stalk of `j_!F` at a point `j(x)` with `x ∈ U` is the stalk of `F` at `x`.

```lean
noncomputable def stalkExtendByInitialSheafifyIso (F : Presheaf C (sp U)) (x : sp U) :
    ((extendByInitialSheafify U).obj F).presheaf.stalk (U.inclusion' x) ≅ F.stalk x
```

**`TopCat.Presheaf.isEmpty_stalk_extendByInitialSheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 643](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L643). The attribute's comment: “(3) for sheaves of sets: (j_!F)_x = ∅ for x ∉ U”. References: SGA 4 III (1.9.2), “more general”.

> For a presheaf of sets `F` on `U`, the stalk of `j_!F` at a point outside `U` is empty:
> `(j_!F)_x = ∅`.

```lean
theorem isEmpty_stalk_extendByInitialSheafify {X : TopCat.{u}} (U : Opens X)
    (F : Presheaf (Type u) (sp U)) {x : X} (hx : x ∉ U) :
    IsEmpty (stalk ((extendByInitialSheafify U).obj F).presheaf x)
```

## Tag 00A4, a definition

[Tag 00A4](https://stacks.math.columbia.edu/tag/00A4) in the Stacks Project.

**`TopCat.Presheaf.extendByInitial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L142). The attribute's comment: “(1), (3)”.

> **Extension by an initial object.** For `j : U → X` the inclusion of an open subset,
> `C` a category with initial object `e`, and `F` a presheaf on `U` with values in `C`, this is
> the presheaf `j_{p!}F` on `X` with `j_{p!}F(V) = F(V)` for `V ⊆ U` and `j_{p!}F(V) = e`
> otherwise, with the obvious restriction maps.
>
> When `C` is a category of algebraic structures its zero object is initial, so this is the
> classical extension by zero of an abelian presheaf; and the initial object of `Type` is the
> empty type, so this is also the extension by the empty set of a presheaf of sets.

```lean
noncomputable def extendByInitial (F : Presheaf C (sp U)) : Presheaf C X
```

**`TopCat.Presheaf.extendByInitialFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L237). The attribute's comment: “(1), (3)”.

> **Extension by an initial object, as a functor.** `j_{p!} : PSh(U) ⥤ PSh(X)`.

```lean
noncomputable def extendByInitialFunctor : Presheaf C (sp U) ⥤ Presheaf C X
```

**`TopCat.Presheaf.extendByInitialSheafify`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L479). The attribute's comment: “(2)”. References: SGA 4 III (1.9.2), “more general”.

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

**`TopCat.Presheaf.extendByInitialSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L486). The attribute's comment: “(2)”. References: SGA 4 III (5.3), “opens of a top. space”.

> **Extension by an initial object, as a functor on sheaves.** `j_! : Sh(U) ⥤ Sh(X)` sends a
> sheaf `F` on `U` to the sheafification of `j_{p!}F`.

```lean
noncomputable def extendByInitialSheaf : TopCat.Sheaf C (sp U) ⥤ TopCat.Sheaf C X
```

## Tag 00A5, a lemma

[Tag 00A5](https://stacks.math.columbia.edu/tag/00A5) in the Stacks Project.

**`TopCat.Presheaf.extendByInitialAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L374). The attribute's comment: “(1)”. References: SGA 4 IV (11.3.1), “presheaf, constant ring”.

> **The extension-by-zero/restriction adjunction, presheaf level.** For `j : U → X` the
> inclusion of an open subset, `j_{p!}` is a left adjoint of the restriction functor `j_p`.

```lean
noncomputable def extendByInitialAdjunction :
    extendByInitialFunctor (C := C) U ⊣ restrictToOpen U
```

**`TopCat.Presheaf.restrictExtendByInitialIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L398). The attribute's comment: “(4)”.

> **`j_p j_{p!} = id`.** The extension by an initial object of a presheaf on `U` restricts
> back to that presheaf, naturally in the presheaf.

```lean
noncomputable def restrictExtendByInitialIso :
    extendByInitialFunctor (C := C) U ⋙ restrictToOpen U ≅ 𝟭 (Presheaf C (sp U))
```

**`TopCat.Presheaf.extendByInitialSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L500). The attribute's comment: “(2)”. References: SGA 4 III (5.3), “j_! ⊣ j^*, opens site”; SGA 4 IV (11.3.1), “sheaves on a space”; SGA 4 XVII (5.1.1), “topological spaces”.

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

**`TopCat.Presheaf.restrictExtendByInitialSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L529). The attribute's comment: “(5)”.

> **`j^{-1} j_! = id`.** The extension by an initial object of a sheaf on `U` restricts back
> to that sheaf, naturally in the sheaf. This is the unit of `j_! ⊣ j^{-1}`, inverted.

```lean
noncomputable def restrictExtendByInitialSheafIso :
    extendByInitialSheaf U ⋙ Opens.sheafRestrict (C := C) U ≅ 𝟭 _
```

**`TopCat.Presheaf.isZero_stalk_extendByInitialSheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 620](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L620). The attribute's comment: “(3)”. References: SGA 4 III (1.9.2), “stalk at x∉Y is zero”.

> When the value category has a zero object — as the categories of abelian groups and of
> modules do — the stalk of `j_!F` at a point `x ∉ U` is a *zero* object.

```lean
theorem isZero_stalk_extendByInitialSheafify [HasZeroObject C] (F : Presheaf C (sp U)) {x : X}
    (hx : x ∉ U) :
    IsZero (((extendByInitialSheafify U).obj F).presheaf.stalk x)
```

**`TopCat.Presheaf.stalkExtendByInitialSheafifyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 629](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L629). The attribute's comment: “(3)”.

> The stalk of `j_!F` at a point `j(x)` with `x ∈ U` is the stalk of `F` at `x`.

```lean
noncomputable def stalkExtendByInitialSheafifyIso (F : Presheaf C (sp U)) (x : sp U) :
    ((extendByInitialSheafify U).obj F).presheaf.stalk (U.inclusion' x) ≅ F.stalk x
```

## Tag 00A6, a lemma

[Tag 00A6](https://stacks.math.columbia.edu/tag/00A6) in the Stacks Project.

**`statement_1_jp_adjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/SheafOfAlgStruct.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/AlgebraicStructure/SheafOfAlgStruct.lean#L442). The attribute's comment: “(1)”. References: SGA 4 I (5.1), “special case”; SGA 4 I (5.8.3), “partial”; SGA 4 IV (9.2.4), “special case”.

> Adjointness on presheaves: the extension `j_{p!} : PShCategory(U, C) ⥤ PShCategory(X, C)` is
> left adjoint to the restriction `j_p : PShCategory(X, C) ⥤ PShCategory(U, C)`.

```lean
theorem statement_1_jp_adjoint :
    Nonempty (jpShriek00A6 S X U ⊣ jpRestrict S X U)
```

**`statement_2_jShriek_adjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/SheafOfAlgStruct.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/AlgebraicStructure/SheafOfAlgStruct.lean#L449). The attribute's comment: “(2)”. References: SGA 4 XVII (5.1.1), “top. spaces, alg. struct”.

> Adjointness on sheaves: for a sheaf `𝓕` on `U` and a sheaf `𝓖` on `X` there is a bijection
> `Hom(j_!𝓕, 𝓖) ≃ Hom(𝓕, j^{-1}𝓖)`.

```lean
theorem statement_2_jShriek_adjoint :
    ∀ (𝓕 : ShOfAlgStruct S (openTopCat X U)) (𝓖 : ShOfAlgStruct S X),
      Nonempty ((((jShriek00A6 S X U) 𝓕).1 ⟶ 𝓖.1) ≃ (𝓕.1 ⟶ ((jInverseSheaf S X U) 𝓖).1))
```

**`statement_3_stalk_in_U`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/SheafOfAlgStruct.lean, line 491](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/AlgebraicStructure/SheafOfAlgStruct.lean#L491). The attribute's comment: “(3)”. References: SGA 4 III (1.9.2), “stalk at y∈Y ≅ H_y”.

> For `x ∈ U`, the stalk `(j_!𝓕)_x` is isomorphic to the stalk `𝓕_x`.

```lean
theorem statement_3_stalk_in_U
    (𝓕 : ShOfAlgStruct S (openTopCat X U))
    (x : X) (hx : x ∈ U) :
    Nonempty (stalk00A6 S X (jShriek00A6 S X U 𝓕).1 x ≅
              stalk00A6 S (openTopCat X U) 𝓕.1 ⟨x, hx⟩)
```

**`statement_3_stalk_off_U`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/SheafOfAlgStruct.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/AlgebraicStructure/SheafOfAlgStruct.lean#L513). The attribute's comment: “(3)”. References: SGA 4 III (1.9.2), “special case”.

> For `x ∉ U`, the stalk `(j_!𝓕)_x` is isomorphic to the initial object of `S.C`.

```lean
theorem statement_3_stalk_off_U
    (𝓕 : ShOfAlgStruct S (openTopCat X U))
    (x : X) (hx : x ∉ U) :
    Nonempty (stalk00A6 S X (jShriek00A6 S X U 𝓕).1 x ≅ (⊥_ S.C))
```

**`statement_4_counit_presheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/SheafOfAlgStruct.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/AlgebraicStructure/SheafOfAlgStruct.lean#L535). The attribute's comment: “(4)”.

> The composite `j_p ∘ j_{p!}` is naturally isomorphic to the identity functor on
> `PShCategory(U, C)`.

```lean
theorem statement_4_counit_presheaf :
    Nonempty ((jpShriek00A6 S X U ⋙ jpRestrict S X U) ≅
              (Functor.id (PShCategory S (openTopCat X U))))
```

**`statement_5_counit_sheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/SheafOfAlgStruct.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/AlgebraicStructure/SheafOfAlgStruct.lean#L543). The attribute's comment: “(5)”.

> For every sheaf `𝓕` on `U`, the underlying presheaves of `j^{-1}(j_!𝓕)` and of `𝓕` are
> isomorphic.

```lean
theorem statement_5_counit_sheaf :
    ∀ (𝓕 : ShOfAlgStruct S (openTopCat X U)),
      Nonempty ((jInverseSheaf S X U (jShriek00A6 S X U 𝓕)).1 ≅ 𝓕.1)
```

## Tag 00A7, a lemma

[Tag 00A7](https://stacks.math.columbia.edu/tag/00A7) in the Stacks Project.

**`jpShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleAdjunction.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleAdjunction.lean#L152). The attribute's comment: “(1)”. References: SGA 4 IV (11.3.1), “presheaves on a space”.

> The adjunction exhibiting the extension-by-zero functor `j_{p!}` on presheaves of modules as a
> left adjoint of the restriction functor `j^{-1}`.

```lean
noncomputable def jpShriekAdjunction : jpShriek X U ⊣ restPMod X U
```

**`jShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleAdjunction.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleAdjunction.lean#L164). The attribute's comment: “(2)”. References: SGA 4 IV (11.3.1), “ringed space, open U”; SGA 4 XVII (5.1.1), “ringed spaces, modules”; SGA 2 I (1.7), “special case”; SGA 4 IV (14.2), “partial”.

> The adjunction exhibiting the extension-by-zero functor `j_!` on sheaves of modules as a left
> adjoint of the restriction functor `j^{-1}`.

```lean
noncomputable def jShriekAdjunction : jShriek00A7 X U ⊣ restMod X U
```

## Tag 00A8, a lemma

[Tag 00A8](https://stacks.math.columbia.edu/tag/00A8) in the Stacks Project.

**`TopCat.Presheaf.extendByInitialSheafFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L536). References: SGA 4 IV (11.3.1), “special case”.

> `j_! : Sh(U) ⥤ Sh(X)` is fully faithful.

```lean
noncomputable def extendByInitialSheafFullyFaithful :
    (extendByInitialSheaf (C := C) U).FullyFaithful
```

**`TopCat.Presheaf.isEmpty_stalk_extendByInitialSheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean, line 643](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitial.lean#L643). References: SGA 4 III (1.9.2), “more general”.

> For a presheaf of sets `F` on `U`, the stalk of `j_!F` at a point outside `U` is empty:
> `(j_!F)_x = ∅`.

```lean
theorem isEmpty_stalk_extendByInitialSheafify {X : TopCat.{u}} (U : Opens X)
    (F : Presheaf (Type u) (sp U)) {x : X} (hx : x ∉ U) :
    IsEmpty (stalk ((extendByInitialSheafify U).obj F).presheaf x)
```

## Tag 00A9, a lemma

[Tag 00A9](https://stacks.math.columbia.edu/tag/00A9) in the Stacks Project.

**`ExtensionByZero.jExt_full`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZero.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZero.lean#L92). The attribute's comment: “(1)”.

> **Stacks 00A9 (1).** The extension by zero functor `j_!` is full: every morphism
> `j_! F ⟶ j_! F'` of sheaves on `X` comes from a morphism `F ⟶ F'` of sheaves on `U`.

```lean
theorem jExt_full : (jExt U).Full
```

**`ExtensionByZero.jExt_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZero.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZero.lean#L98). The attribute's comment: “(1)”. References: SGA 4 IV (11.3.1), “special case”.

> **Stacks 00A9 (1).** The extension by zero functor `j_!` is faithful: a morphism of sheaves
> on `U` is determined by the morphism it induces on the extensions by zero.

```lean
theorem jExt_faithful : (jExt U).Faithful
```

**`ExtensionByZero.jExt_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZero.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByZero.lean#L148). The attribute's comment: “(2)”. References: SGA 4 XVII (5.1.1), “partial”.

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

**`Stacks.full_and_faithful_and_essImage_jLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitialAlgStruct.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ExtensionByInitialAlgStruct.lean#L556).

> **Stacks 00AA.** For `S = (C, F)` a type of algebraic structure whose category
> `C` has an initial object, and `j : U → X` the inclusion of an open subset, the
> extension-by-initial functor `j_! : Sh(U, C) ⥤ Sh(X, C)` is full and faithful, and
> a sheaf `G ∈ Sh(X, C)` lies in its essential image exactly when the stalk `G_x` is
> an initial object of `C` for every `x ∈ X ∖ U`.

```lean
theorem full_and_faithful_and_essImage_jLowerShriek (S : AlgebraicStructureType.{u, u})
    [HasColimits S.C] [HasInitial S.C] (X : TopCat.{u}) (U : Opens X)
    [HasWeakSheafify (Opens.grothendieckTopology X) S.C]
    [HasWeakSheafify (Opens.grothendieckTopology (TopCat.of (U : Type _))) S.C] :
    (jLowerShriek (C := S.C) X U).Full ∧
      (jLowerShriek (C := S.C) X U).Faithful ∧
      ∀ G : TopCat.Sheaf S.C X,
        (jLowerShriek (C := S.C) X U).essImage G ↔
          ∀ x : X, x ∉ (U : Set X) → Nonempty (IsInitial (G.presheaf.stalk x))
```

## Tag 00AB, a lemma

[Tag 00AB](https://stacks.math.columbia.edu/tag/00AB) in the Stacks Project.

**`ExtensionByZeroModules.full_and_faithful_and_essImage_jShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZero.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/ModuleExtensionByZero.lean#L395). References: SGA 4 IV (11.3.1), “special case”.

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

**`TopCat.Presheaf.isEmpty_isTerminal_extendByInitialSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/NotLeftExact.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/NotLeftExact.lean#L68). The attribute's comment: “j_! does not transform a final object of Sh(U) into a final object of Sh(X)”.

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

**`TopCat.Presheaf.not_preservesFiniteLimits_extendByInitialSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/OpenImmersion/NotLeftExact.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/OpenImmersion/NotLeftExact.lean#L86). The attribute's comment: “j_! is not left exact as a functor between the categories of sheaves of sets”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
