---
declaration: section
origin: cited
lean: RingedSpaceModuleAdjunction.modulePushforward, PullbackStalkTensor.modulePullbackTensor, PullbackStalkTensor.ringedSpacePullbackTensor, RingedSpaceModuleAdjunction.modulePullback, RingedSpaceModuleAdjunction.modulePullbackPushforwardAdjunction, RingedSpaceModuleAdjunction.homEquiv, pushforwardComp, pullbackComp
statement: formalized
proof: formalized
---

# 6.26 Morphisms of ringed spaces and modules

Section 6.26 of the Stacks Project, [Tag 0094](https://stacks.math.columbia.edu/tag/0094). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0095, a definition

[Tag 0095](https://stacks.math.columbia.edu/tag/0095) in the Stacks Project.

**`RingedSpaceModuleAdjunction.modulePushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/RingedSpace.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/RingedSpace.lean#L123). The attribute's comment: “(1)”. References: EGA 0 (4.2.1), “Ψ\_* functor”; EGA 0 (12.2.1); SGA 4 Vbis (1.3.6), “ringed spaces, φ\_*”; SGA 3 VIIA (1.1), “more general”; SGA 4 IV (13.2.1), “special case”; SGA 4 V (5.0), “special case”.

> Pushforward of sheaves of modules along a morphism of ringed spaces,
> `f_* : Mod(𝒪_X) ⥤ Mod(𝒪_Y)`, given on sections by `(f_* F)(V) = F(f⁻¹ V)`, with the
> `𝒪_Y`-module structure restricted along `f^♯`.

```lean
noncomputable def modulePushforward :
    SheafOfModules.{u} (structureSheafRing X) ⥤ SheafOfModules.{u} (structureSheafRing Y)
```

**`PullbackStalkTensor.modulePullbackTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/ModulePullbackTensor.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/ModulePullbackTensor.lean#L129). The attribute's comment: “(2)”. References: EGA 0 (4.3.1), “Ψ*(G) definition”; SGA 4 IV (13.2.2), “ringed space, comm O”; SGA 4 Vbis (1.3.6), “ringed spaces, φ^*”.

> **Stacks 0095 (2).**  The pullback of a sheaf of `O_Y`-modules `G` along a morphism of
> ringed spaces `(f, f^\sharp)`:
> `f^*G = O_X ⊗_{f^{-1}O_Y} f^{-1}G`,
> a sheaf of `O_X`-modules.  The tensor product is `Stacks.Sheafify.ModuleStalkTensor.tensorSheaf`,
>   i.e. the
> sheafification of the sectionwise tensor product presheaf
> `U ↦ O_X(U) ⊗_{(f^{-1}O_Y)(U)} (f^{-1}G)(U)`; the `f^{-1}O_Y`-module `f^{-1}G` is
> `invMod f OY G`, the inverse image of Stacks 008X; and the ring map `f^{-1}O_Y → O_X` is
> `sharpTranspose f OY OX sharp`, the map corresponding to `f^\sharp`.

```lean
noncomputable def modulePullbackTensor : SheafOfModules.{u} (ringSheaf OX)
```

**`PullbackStalkTensor.ringedSpacePullbackTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/ModulePullbackTensor.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/ModulePullbackTensor.lean#L151). The attribute's comment: “(2)”. References: EGA 0 (4.3.1), “Ψ*(G) definition”; SGA 4 IV (13.2.2), “ringed space, comm O”; SGA 4 Vbis (1.3.6), “ringed spaces, φ^*”.

> **Stacks 0095 (2)** for a morphism of ringed spaces: the pullback
> `g^*G = O_X ⊗_{g^{-1}O_Y} g^{-1}G` of a sheaf of `O_Y`-modules `G`, with the ring map
> `g^{-1}O_Y → O_X` the one corresponding to the structure morphism `g^\sharp = g.hom.c`.

```lean
noncomputable def ringedSpacePullbackTensor (G : SheafOfModules.{u} (ringSheaf Y.sheaf)) :
    SheafOfModules.{u} (ringSheaf X.sheaf)
```

## Tag 0096, a lemma

[Tag 0096](https://stacks.math.columbia.edu/tag/0096) in the Stacks Project.

**`RingedSpaceModuleAdjunction.modulePushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/RingedSpace.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/RingedSpace.lean#L123). References: EGA 0 (4.2.1), “Ψ\_* functor”; EGA 0 (12.2.1); SGA 4 Vbis (1.3.6), “ringed spaces, φ\_*”; SGA 3 VIIA (1.1), “more general”; SGA 4 IV (13.2.1), “special case”; SGA 4 V (5.0), “special case”.

> Pushforward of sheaves of modules along a morphism of ringed spaces,
> `f_* : Mod(𝒪_X) ⥤ Mod(𝒪_Y)`, given on sections by `(f_* F)(V) = F(f⁻¹ V)`, with the
> `𝒪_Y`-module structure restricted along `f^♯`.

```lean
noncomputable def modulePushforward :
    SheafOfModules.{u} (structureSheafRing X) ⥤ SheafOfModules.{u} (structureSheafRing Y)
```

**`RingedSpaceModuleAdjunction.modulePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/RingedSpace.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/RingedSpace.lean#L161). References: EGA 0 (4.3.1); SGA 4 IV (13.2.2), “ringed space, comm O”; SGA 4 IV (13.2), “u^* for ringed spaces”; SGA 4 Vbis (1.3.6), “ringed spaces, φ^*”; SGA 4 XVII (4.1), “ringed spaces”; SGA 3 III (0.1.4), “more general”; SGA 6 IV (2.6), “special case”; SGA 6 VI (2.3.1), “more general”.

> Pullback of sheaves of modules along a morphism of ringed spaces,
> `f^* : Mod(𝒪_Y) ⥤ Mod(𝒪_X)`: the left adjoint of `f_*`.

```lean
noncomputable def modulePullback {X Y : RingedSpace.{u, u}} (f : X ⟶ Y) :
    SheafOfModules.{u} (structureSheafRing Y) ⥤ SheafOfModules.{u} (structureSheafRing X)
```

**`RingedSpaceModuleAdjunction.modulePullbackPushforwardAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/RingedSpace.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/RingedSpace.lean#L177). References: EGA 0 (4.4.3), “partial”; EGA III (7.7.9), “more general”; SGA 4 IV (13.4), “a), ringed spaces”; SGA 4 Vbis (1.3.6), “ringed spaces”; SGA 3 I (4.6.4), “more general”; SGA 4 IV (14.2), “special case”; SGA 6 VI (2.3.1), “more general”.

> The adjunction `f^* ⊣ f_*` between the categories of sheaves of modules on the ringed
> spaces `Y` and `X`.

```lean
noncomputable def modulePullbackPushforwardAdjunction {X Y : RingedSpace.{u, u}} (f : X ⟶ Y) :
    modulePullback f ⊣ modulePushforward f
```

**`RingedSpaceModuleAdjunction.homEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/RingedSpace.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/Module/RingedSpace.lean#L198). References: EGA 0 (4.4.3), “partial”; EGA III (7.7.9), “more general”; SGA 4 IV (13.4), “a), ringed spaces”; SGA 4 Vbis (1.3.6), “ringed spaces”; SGA 3 I (4.6.4), “more general”; SGA 3 VIB (11.4), “(†)”; SGA 6 VI (2.3.1), “partial”.

> The bijection of hom-sets `Hom_{𝒪_X}(f^* G, F) ≃ Hom_{𝒪_Y}(G, f_* F)` given by the
> adjunction `f^* ⊣ f_*`, natural in both `F` and `G`.

```lean
noncomputable def homEquiv {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (F : SheafOfModules.{u} (structureSheafRing X))
    (G : SheafOfModules.{u} (structureSheafRing Y)) :
    ((modulePullback f).obj G ⟶ F) ≃ (G ⟶ (modulePushforward f).obj F)
```

## Tag 0097, a lemma

[Tag 0097](https://stacks.math.columbia.edu/tag/0097) in the Stacks Project.

**`pushforwardComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/ModuleFunctors.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/ModuleFunctors.lean#L170). The attribute's comment: “(1)”. References: EGA 0 (4.2.6).

> For composable morphisms of ringed spaces `f : X ⟶ Y` and `g : Y ⟶ Z`, there
> is a canonical natural isomorphism between the pushforward of the composite
> and the composite of the pushforwards.

```lean
noncomputable def pushforwardComp {X Y Z : RingedSpace.{u}}
    (f : X ⟶ Y) (g : Y ⟶ Z) :
    pushforward (f ≫ g) ≅ pushforward f ⋙ pushforward g
```

**`pullbackComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/ModuleFunctors.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/ModuleFunctors.lean#L181). The attribute's comment: “(2)”. References: EGA 0 (4.3.6).

> For composable morphisms of ringed spaces `f : X ⟶ Y` and `g : Y ⟶ Z`, there
> is a canonical natural isomorphism between the pullback of the composite and
> the composite of the pullbacks (in the reverse order).

```lean
noncomputable def pullbackComp {X Y Z : RingedSpace.{u}}
    (f : X ⟶ Y) (g : Y ⟶ Z) :
    pullback (f ≫ g) ≅ pullback g ⋙ pullback f
```

## Tag 0098, a lemma

[Tag 0098](https://stacks.math.columbia.edu/tag/0098) in the Stacks Project.

**`Stacks.ModuleSkyscraper.pullbackStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackStalkColimit.lean, line 470](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackStalkColimit.lean#L470). The attribute's comment: “the stalk of Mathlib's `Scheme.Modules.pullback` at `x`, naturally in the module; the companion carrier `PullbackStalkTensor.stalkPullbackTensorIso` instead computes the stalk of the hand-built Tag 0095 (2) model over an arbitrary morphism of ringed spaces”.

> **Stacks 0098 for Mathlib's pullback of sheaves of modules on schemes.**  The stalk at `x`
> of the pullback along `f` is the base change of the stalk at `f x` along the stalk map of `f`:
>
> `(f^*N)_x = 𝒪_{X,x} ⊗_{𝒪_{Y,f x}} N_{f x}`,
>
> naturally in `N`.  Both sides are left adjoints — `pullback f ⋙ stalk_x` by
> `Scheme.Modules.pullbackPushforwardAdjunction` composed with `modulesStalkSkyAdjunction`, and
> `stalk_{f x} ⋙ extendScalars` by `modulesStalkSkyAdjunction` composed with
> `ModuleCat.extendRestrictScalarsAdj` — and `pushSkyIso` identifies their right adjoints, so
> `CategoryTheory.conjugateIsoEquiv` identifies them.  No description of the sections of the
> pullback, and no colimit interchange, is used.
>
> **On the covering set.**  Tag 0098 is also carried by
> `PullbackStalkTensor.stalkPullbackTensorIso`
> (`StacksFrontier/Topology/Sheaves/RingedSpace/ModulePullbackStalk.lean`), and the two
> declarations state different things, which is what the covering-set rule requires of a shared
> tag.  That one works over an arbitrary morphism of *ringed spaces* and computes the stalk of the
> hand-built model `O_X ⊗_{f^{-1}O_Y} f^{-1}G` of Tag 0095 (2), at a single object, as a linear
> equivalence; it does not know that model to be a pullback functor.  This one works over a
> morphism of *schemes*, is about Mathlib's `Scheme.Modules.pullback` itself, and is natural in
> `N`.  Neither subsumes the other: the first is more general in its spaces, the second in what it
> identifies.

```lean
noncomputable def pullbackStalkIso :
    modulesStalkFunctor Y (f x) ⋙ ModuleCat.extendScalars (f.stalkMap x).hom ≅
      Scheme.Modules.pullback f ⋙ modulesStalkFunctor X x
```

**`PullbackStalkTensor.stalkPullbackTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/ModulePullbackStalk.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/ModulePullbackStalk.lean#L354). References: EGA 0 (4.3.1), “stalk formula”; EGA 0 (6.7.2), “special case”; EGA I (9.1.12), “case Y = S”.

> For a morphism of ringed spaces `(f, f^\sharp)` and a sheaf of `O_Y`-modules `G`, the stalk
> of the pullback `f^*G = O_X ⊗_{f^{-1}O_Y} f^{-1}G` at `x` is `G_{f(x)} ⊗_{O_{Y,f(x)}} O_{X,x}`,
> where the tensor product uses `f^\sharp_x : O_{Y,f(x)} → O_{X,x}`.

```lean
noncomputable def stalkPullbackTensorIso :
    letI := (sharpStalk f OY OX alpha x).toAlgebra
    letI := rightTensorModule (ToType (TopCat.Presheaf.stalk (C := CommRingCat.{u}) OY.obj (f x)))
      (ToType (TopCat.Presheaf.stalk (C := CommRingCat.{u}) OX.obj x))
      (ToType (TopCat.Presheaf.stalk (C := Ab.{u}) (srcMod OY G).presheaf (f x)))
    TensorProduct (ToType (TopCat.Presheaf.stalk (C := CommRingCat.{u}) OY.obj (f x)))
        (ToType (TopCat.Presheaf.stalk (C := Ab.{u}) (srcMod OY G).presheaf (f x)))
        (ToType (TopCat.Presheaf.stalk (C := CommRingCat.{u}) OX.obj x))
      ≃ₗ[ToType (TopCat.Presheaf.stalk (C := CommRingCat.{u}) OX.obj x)]
      ToType (TopCat.Presheaf.stalk (C := Ab.{u})
        (tensorSheaf (invRing f OY) OX alpha (invMod f OY G)).val.presheaf x)
```

**`RingedSpaceModuleAdjunction.exists_modulePullbackStalkLinearEquiv`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/ModulePullbackStalkAdjunction.lean, line 1164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/ModulePullbackStalkAdjunction.lean#L1164).

> The stalk of the pullback is extension of scalars along the structure map on stalks,
> by a linear equivalence sending the germ of the adjunction-unit image of every section
> to the pure tensor of `1` with its original germ.

```lean
lemma exists_modulePullbackStalkLinearEquiv {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (G : SheafOfModules.{u} (structureSheafRing Y)) (x : X) :
    let G' : PresheafOfModules (Y.presheaf ⋙ forget₂ CommRingCat RingCat) := G.val
    let P' : PresheafOfModules (X.presheaf ⋙ forget₂ CommRingCat RingCat) :=
      ((modulePullback f).obj G).val
    letI : Algebra (Y.presheaf.stalk (f.hom.base x)) (X.presheaf.stalk x) :=
      (f.hom.stalkMap x).hom.toAlgebra
    ∃ e : ↑(TopCat.Presheaf.stalk P'.presheaf x) ≃ₗ[X.presheaf.stalk x]
        TensorProduct (Y.presheaf.stalk (f.hom.base x)) (X.presheaf.stalk x)
          ↑(TopCat.Presheaf.stalk G'.presheaf (f.hom.base x)),
      ∀ (V : Opens Y.carrier) (hx : f.hom.base x ∈ V) (s : G.val.obj (op V)),
        e (TopCat.Presheaf.germ P'.presheaf ((opensMap f).obj V) x hx
            (((modulePullbackPushforwardAdjunction f).unit.app G).val.app (op V) s)) =
          (1 : X.presheaf.stalk x) ⊗ₜ[Y.presheaf.stalk (f.hom.base x)]
            TopCat.Presheaf.germ G'.presheaf V (f.hom.base x) hx s
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.26, Tag 0094](https://stacks.math.columbia.edu/tag/0094)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
