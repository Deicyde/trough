---
declaration: section
origin: cited
lean: PresheafOfModules.isRightAdjoint_pushforward_of_univLE, PresheafOfModules.isRightAdjoint_pushforward_of_essentiallySmall, SheafOfModules.pushforward_isRightAdjoint_of_essentiallySmall, Stacks.Sheaves.RingedToposModules.pushforwardModules, Stacks.Sheaves.RingedToposModules.RingedToposHom.pullbackModules, AlgebraicGeometry.RingedToposHom.pullbackModulesCompIso, AlgebraicGeometry.smallEtalePushforwardModules, AlgebraicGeometry.smallEtalePullbackModules
statement: formalized
proof: formalized
---

# 18.13 Morphisms of ringed topoi and modules

Section 18.13 of the Stacks Project, [Tag 03D5](https://stacks.math.columbia.edu/tag/03D5). 3 tags here are carried by 25 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03D6, a definition

[Tag 03D6](https://stacks.math.columbia.edu/tag/03D6) in the Stacks Project.

**`PresheafOfModules.isRightAdjoint_pushforward_of_univLE`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/PullbackUnivLE.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/PullbackUnivLE.lean#L254). The attribute's comment: “part (2), presheaves of modules at independent universes”.

> **The pushforward of presheaves of modules is a right adjoint**, with the universes of the
> two sites, of their morphisms, of the presheaves of rings and of the module sections
> independent. Instance, so that `PresheafOfModules.pullback φ` and
> `PresheafOfModules.pullbackPushforwardAdjunction φ` are available with no adjointness
> hypothesis; this is what Mathlib supplies only for small sites in a single universe.

```lean
instance isRightAdjoint_pushforward_of_univLE :
    (pushforward.{v} φ).IsRightAdjoint
```

**`PresheafOfModules.isRightAdjoint_pushforward_of_essentiallySmall`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackEssentiallySmall.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackEssentiallySmall.lean#L96). The attribute's comment: “part (2), presheaves of modules over an essentially small site”.

> **The pushforward of presheaves of modules is a right adjoint** as soon as the source site is
> essentially small in the universe of the rings and of the module sections, the target site being
> locally small in that universe. Instance, so that `PresheafOfModules.pullback φ` and
> `PresheafOfModules.pullbackPushforwardAdjunction φ` are available with no adjointness
> hypothesis.

```lean
instance isRightAdjoint_pushforward_of_essentiallySmall :
    (pushforward.{v} φ).IsRightAdjoint
```

**`SheafOfModules.pushforward_isRightAdjoint_of_essentiallySmall`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackEssentiallySmall.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackEssentiallySmall.lean#L164). The attribute's comment: “part (2), sheaves of modules over an essentially small site”.

> **Pushforward of sheaves of modules along a continuous functor of sites has a left adjoint**
> as soon as the source site is essentially small in the universe of the sheaves of rings and of
> the module sections. This is the existence half of the lower shriek for modules.

```lean
instance pushforward_isRightAdjoint_of_essentiallySmall :
    (pushforward.{v} φ).IsRightAdjoint
```

**`Stacks.Sheaves.RingedToposModules.pushforwardModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean, line 972](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean#L972). The attribute's comment: “part (1)”.

> **Stacks 03D6, part (1)**: the pushforward of a sheaf of `O_C`-modules along a morphism
> of ringed topoi. As a sheaf of abelian groups it is the direct image `f_*F`
> (`moduleSheaf_pushforwardModules`), and its scalar action is the restriction along the
> direct-image form `f♯ : O_D ⟶ f_*O_C` of the structure map of the direct-image action of
> Stacks 03D1 (`pushforwardModules_smul`).

```lean
noncomputable def pushforwardModules :
    SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O) ⥤ SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)
```

**`Stacks.Sheaves.RingedToposModules.RingedToposHom.pullbackModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean, line 1040](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean#L1040). The attribute's comment: “part (2)”. References: EGA 0 (4.3.1), “Ψ* functor”; SGA 4 IV (13.2.2), “commutative O, left mod”.

> **Stacks 03D6, part (2)**: the pullback of a sheaf of `O_D`-modules along a morphism of
> ringed topoi: `O_C ⊗_{f⁻¹O_D} f⁻¹G`, i.e. the inverse image of Stacks 03D2 followed by
> extension of scalars along the inverse-image form of the structure map.

```lean
noncomputable def pullbackModules :
    SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf.{u', v', w'} Y.O) ⥤
      SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, v, w} X.O)
```

**`Stacks.Sheaves.RingedToposModules.RingedToposHom.pullbackModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean, line 1040](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean#L1040). The attribute's comment: “part (2), for the two-field morphism of ringed topoi”. References: EGA 0 (4.3.1), “Ψ* functor”; SGA 4 IV (13.2.2), “commutative O, left mod”.

> **Stacks 03D6, part (2)**: the pullback of a sheaf of `O_D`-modules along a morphism of
> ringed topoi: `O_C ⊗_{f⁻¹O_D} f⁻¹G`, i.e. the inverse image of Stacks 03D2 followed by
> extension of scalars along the inverse-image form of the structure map.

```lean
noncomputable def pullbackModules :
    SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf.{u', v', w'} Y.O) ⥤
      SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, v, w} X.O)
```

**`AlgebraicGeometry.RingedToposHom.pullbackModulesCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean#L112). The attribute's comment: “part (2), pseudo-functoriality: the pullback of a composite of morphisms of ringed topoi is the composite of the pullbacks”.

> **The pullback of sheaves of modules along a composite of morphisms of ringed topoi is the
> composite of the pullbacks**, `(g ∘ f)^* ≅ g^* ⋙ f^*`.
>
> Both sides are left adjoint to `f_* ⋙ g_*`: the left-hand side by
> `AlgebraicGeometry.RingedToposHom.pushforwardModulesCompIso` transported across its adjunction,
> the right-hand side because adjunctions compose. So they agree by uniqueness of left
> adjoints.

```lean
def pullbackModulesCompIso (f : RingedToposHom X Y) (g : RingedToposHom Y Z) :
    (g.comp f).toModulesHom.pullbackModules ≅
      g.toModulesHom.pullbackModules ⋙ f.toModulesHom.pullbackModules
```

**`AlgebraicGeometry.smallEtalePushforwardModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleModulesPullback.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleModulesPullback.lean#L102). The attribute's comment: “part (1): pushforward of sheaves of modules along the morphism of small étale ringed sites of a morphism of schemes”.

> **Stacks 03D6 part (1) for the small étale sites of schemes.** The pushforward
> `f_{small,*} : Mod(𝒪_{X_étale}) ⥤ Mod(𝒪_{Y_étale})` of sheaves of modules along the morphism of
> small étale ringed sites of a morphism of schemes: the underlying sheaf of abelian groups is the
> direct image, and the module structure is restriction of scalars along `f_{small}^♯`.

```lean
def smallEtalePushforwardModules (a : X ⟶ Y) :
    SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B X.obj X.property).O) ⥤
      SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B Y.obj Y.property).O)
```

**`AlgebraicGeometry.smallEtalePullbackModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleModulesPullback.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleModulesPullback.lean#L120). The attribute's comment: “part (2): pullback of sheaves of modules along the morphism of small étale ringed sites of a morphism of schemes, whose site is essentially small rather than small in the universe of the structure rings”.

> **Stacks 03D6 part (2) for the small étale sites of schemes.** The pullback
> `f_{small}^* : Mod(𝒪_{Y_étale}) ⥤ Mod(𝒪_{X_étale})` of sheaves of modules along the morphism of
> small étale ringed sites of a morphism of schemes, characterised as the left adjoint of the
> pushforward.
>
> The small étale site is not small in the universe of its structure rings, only essentially so,
> which is why this is not an instance of Mathlib's `SheafOfModules.pullback` with its
> `SmallCategory` hypothesis.

```lean
def smallEtalePullbackModules (a : X ⟶ Y) :
    SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B Y.obj Y.property).O) ⥤
      SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B X.obj X.property).O)
```

**`AlgebraicGeometry.RingedToposSiteHom.pushforwardTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedToposHom.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedToposHom.lean#L136). The attribute's comment: “part (1): pushforward of sheaves of modules along a morphism of ringed topoi, presented by a morphism of the underlying sites”. References: SGA 4 Vbis (1.3.6), “special case”.

> **Stacks 03D6, part (1).** The pushforward of sheaves of modules along a morphism of
> ringed topoi: the underlying sheaf of abelian groups is the direct image `f_* F`, and the
> module structure is restriction of scalars along `f^♯ : O_Y ⟶ f_* O_X`.

```lean
def pushforwardTopos (f : RingedToposSiteHom X Y) :
    SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, v, w} X.O) ⥤
      SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf.{u', v', w} Y.O)
```

**`AlgebraicGeometry.RingedToposSiteHom.pullbackTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedToposHom.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedToposHom.lean#L174). The attribute's comment: “part (2): pullback of sheaves of modules along a morphism of ringed topoi, presented by a morphism of the underlying sites, both of which are small in the universe of the sections of the structure sheaves; characterised as the left adjoint of the pushforward and identified with the sheafification of `O_X ⊗_{f⁻¹ O_Y} f⁻¹ G` in `pullbackToposIso`”. References: EGA 0 (4.3.1), “Ψ* functor”; SGA 4 IV (13.2.2), “commutative O, sites”.

> **Stacks 03D6, part (2).** The pullback of sheaves of modules along a morphism of ringed
> topoi, characterised as the left adjoint of the pushforward. By `pullbackToposIso` it is the
> sheafification of `O_X ⊗_{f⁻¹ O_Y} f⁻¹ G`, which is the formula of the source.

```lean
def pullbackTopos (f : RingedToposSiteHom X Y) :
    SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) ⥤
      SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
```

**`AlgebraicGeometry.RingedToposSiteHom.pullbackToposGeneral`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedToposPullbackEssentiallySmall.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedToposPullbackEssentiallySmall.lean#L100). The attribute's comment: “part (2): pullback of sheaves of modules along a morphism of ringed topoi, presented by a morphism of the underlying sites, with the object and morphism universes of the two sites independent of each other and of the universe of the sections of the structure sheaves; the source site is asked to be essentially small in that universe rather than small”.

> **Stacks 03D6, part (2), at independent universes.** The pullback of sheaves of modules
> along a morphism of ringed topoi, characterised as the left adjoint of the pushforward, with the
> objects and the morphisms of the two underlying sites in universes independent of each other and
> of the universe of the sections of the structure sheaves.  By `pullbackToposGeneralIso` it is
> the sheafification of `O_X ⊗_{f⁻¹ O_Y} f⁻¹ G`, which is the formula of the source.

```lean
def pullbackToposGeneral (f : RingedToposSiteHom X Y) :
    SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) ⥤ SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
```

## Tag 03D7, a lemma

[Tag 03D7](https://stacks.math.columbia.edu/tag/03D7) in the Stacks Project.

**`SheafOfModules.pullbackPushforwardAdjunctionUnivLE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackContinuousUnivLE.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackContinuousUnivLE.lean#L102). The attribute's comment: “ringed sites, at independent universes”.

> **Stacks 03D7**, with the universes of the two sites, of their morphisms, of the sheaves
> of rings and of the module sections independent: for a continuous functor of sites and a
> morphism of sheaves of rings, pullback of sheaves of modules is left adjoint to pushforward.
> The adjunction supplies the natural bijection between morphisms out of a pullback and
> morphisms into a pushforward.

```lean
def pullbackPushforwardAdjunctionUnivLE :
    SheafOfModules.pullback.{v} φ ⊣ SheafOfModules.pushforward.{v} φ
```

**`Stacks.Sheaves.RingedToposModules.pullbackAdjPushforwardModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean, line 1052](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean#L1052). The attribute's comment: “ringed topoi”.

> **Stacks 03D7**, the ringed-topoi case: for a morphism of ringed topoi
> `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)`, pullback of sheaves of modules is left adjoint to
> pushforward. The adjunction supplies the canonical bijection
> `Hom_{O_C}(f^*G, F) = Hom_{O_D}(G, f_*F)`, naturally in both variables.

```lean
noncomputable def pullbackAdjPushforwardModules :
    f.pullbackModules ⊣ pushforwardModules f
```

**`AlgebraicGeometry.RingedToposHom.pullbackAdjPushforwardModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullback.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullback.lean#L354). The attribute's comment: “for the two-field morphism of ringed topoi”. References: SGA 4 IV (13.4), “(a) 13.4.1”.

> **Stacks 03D7** for a morphism of ringed topoi in the sense of Stacks 01D3: pullback of
> sheaves of modules is left adjoint to pushforward. The adjunction supplies the canonical
> bijection `Hom_{O_C}(f^*G, F) = Hom_{O_D}(G, f_*F)`, naturally in both variables.
>
> It is the adjunction of the modules development for the four-field morphism `toModulesHom`,
> with the right adjoint transported along `toModulesPushforwardIso`.

```lean
def pullbackAdjPushforwardModules (f : RingedToposHom X Y) :
    f.toModulesHom.pullbackModules ⊣ pushforwardModules f
```

**`Stacks.Sheaves.ModuleAdjunction.pullbackPushforwardAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ToposModuleAdjunction.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ToposModuleAdjunction.lean#L107). The attribute's comment: “ringed sites”.

> **Stacks 03D7**, the ringed-site case: for a continuous functor of sites and a morphism
> of sheaves of rings, pullback of sheaves of modules is left adjoint to pushforward. The
> adjunction supplies the natural bijection between morphisms out of a pullback and morphisms
> into a pushforward.

```lean
noncomputable def pullbackPushforwardAdjunction :
    SheafOfModules.pullback.{u} φ ⊣ SheafOfModules.pushforward.{u} φ
```

**`AlgebraicGeometry.smallEtaleModulePullbackAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModulePullback.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModulePullback.lean#L125). The attribute's comment: “the small étale sites of schemes, at the module universe `u + 1` of the étale cohomology comparisons of Stacks 0DDH rather than at the universe `u` of the sections of the structure sheaves”.

> On sheaves of `𝒪`-modules on the small étale sites of schemes, at the module universe of
> Stacks 0DDH, `f_small^*` is left adjoint to `f_{small,*}`.

```lean
public def smallEtaleModulePullbackAdjunction :
    smallEtaleModulePullbackLarge B T S f ⊣ smallEtaleModulePushforward B T S f
```

**`AlgebraicGeometry.bigEtaleModuleInverseImageAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModulePullback.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModulePullback.lean#L227). The attribute's comment: “the big étale sites of schemes, where the pullback of sheaves of modules is the inverse image of Stacks 04CC part (2), at the module universe `u + 1`”. References: SGA 4 Vbis (1.3.6), “special case”.

> On the big étale sites of schemes, the inverse image `f_big^* = f_big^{-1}` of sheaves of
> `𝒪`-modules of Stacks 04CC part (2) is left adjoint to the direct image `f_{big,*}`.

```lean
public def bigEtaleModuleInverseImageAdjunction :
    bigEtaleInverseImageModules B T S f ⊣ bigEtaleModulePushforward B T S f
```

**`AlgebraicGeometry.smallEtalePullbackAdjPushforwardModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleModulesPullback.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleModulesPullback.lean#L130). The attribute's comment: “the small étale sites of schemes”.

> **Stacks 03D7 for the small étale sites of schemes.** The pullback of sheaves of modules
> along `f_small` is left adjoint to the pushforward.

```lean
def smallEtalePullbackAdjPushforwardModules (a : X ⟶ Y) :
    smallEtalePullbackModules B a ⊣ smallEtalePushforwardModules B a
```

**`Stacks.ChaoticSite.pointModuleAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ModuleAdjunction.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ModuleAdjunction.lean#L154). The attribute's comment: “chaotic site over its point, at independent universes”.

> **Stacks 03D7 at the point of a chaotic site**: lower shriek of sheaves of modules along
> the point functor is left adjoint to restriction, at independent universes. The adjunction
> supplies the natural bijection between morphisms out of `p_! M` and morphisms into `p^* N`.

```lean
def pointModuleAdjunction :
    SheafOfModules.pullback.{v} (F := Functor.star C) (R := R)
        (S := pointInverseImageRing C R)
        (𝟙 (pointInverseImageRing C R) :
          pointInverseImageRing C R ⟶ pointInverseImageRing C R) ⊣
      SheafOfModules.pushforward.{v} (F := Functor.star C) (R := R)
        (S := pointInverseImageRing C R)
        (𝟙 (pointInverseImageRing C R) :
          pointInverseImageRing C R ⟶ pointInverseImageRing C R)
```

**`Stacks.Cohomology.DerivedPushforward.pullbackAdjPushforwardMapHomotopy`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/PullbackAdjunction.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/PullbackAdjunction.lean#L168). The attribute's comment: “on unbounded homotopy categories”.

> **Stacks 03D7 on unbounded homotopy categories**: degreewise pullback is left adjoint to
> degreewise direct image, with the degreewise unit and counit. Both functors are additive, so
> `CategoryTheory.Adjunction.mapHomotopyCategory` applies to the adjunction
> `AlgebraicGeometry.RingedToposHom.pullbackAdjPushforwardModules` of Stacks 03D7.
>
> This is the adjunction that Stacks 09T5 derives.

```lean
def pullbackAdjPushforwardMapHomotopy (f : RingedToposHom X Y) :
    pullbackMapHomotopy f ⊣ pushforwardMapHomotopy f
```

**`AlgebraicGeometry.RingedToposSiteHom.pullbackPushforwardAdjunctionTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedToposHom.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedToposHom.lean#L185). The attribute's comment: “ringed topoi, with the geometric morphism presented by a continuous functor between the underlying sites and the two structure sheaves sharing the universe of their sections”. References: SGA 4 IV (13.4), “(a) 13.4.1”.

> The pullback of sheaves of modules is left adjoint to the pushforward.

```lean
def pullbackPushforwardAdjunctionTopos (f : RingedToposSiteHom X Y) :
    f.pullbackTopos ⊣ f.pushforwardTopos
```

**`AlgebraicGeometry.RingedToposSiteHom.homEquivModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedToposPullbackAdjunction.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedToposPullbackAdjunction.lean#L72). The attribute's comment: “the canonical bijection `Hom_{O_X}(f^* G, F) = Hom_{O_Y}(G, f_* F)`”. References: SGA 4 IV (13.4), “(a) 13.4.1”.

> **Stacks 03D7**, the displayed bijection. For a sheaf `G` of `O_Y`-modules and a sheaf
> `F` of `O_X`-modules, morphisms `f^* G ⟶ F` of `O_X`-modules correspond bijectively to
> morphisms `G ⟶ f_* F` of `O_Y`-modules.

```lean
noncomputable def homEquivModules (f : RingedToposSiteHom X Y)
    (G : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
    (F : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    (f.pullbackTopos.obj G ⟶ F) ≃ (G ⟶ f.pushforwardTopos.obj F)
```

**`AlgebraicGeometry.RingedToposSiteHom.pullbackPushforwardAdjunctionToposGeneral`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedToposPullbackEssentiallySmall.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedToposPullbackEssentiallySmall.lean#L109). The attribute's comment: “ringed topoi, with the geometric morphism presented by a morphism of the underlying sites and the object and morphism universes of the two sites independent of each other and of the universe of the sections of the structure sheaves”.

> **Stacks 03D7 at independent universes.** The pullback of sheaves of modules is left adjoint
> to the pushforward.

```lean
def pullbackPushforwardAdjunctionToposGeneral (f : RingedToposSiteHom X Y) :
    f.pullbackToposGeneral ⊣ f.pushforwardTopos
```

Declarations registered for the tag:

- [`SheafOfModules.pullbackPushforwardAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.pullbackPushforwardAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/RingedToposPullbackAdjunction.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedToposPullbackAdjunction.lean#L54) (StacksFrontier): “ringed sites: the adjunction attached to a continuous functor of sites together with a morphism of sheaves of rings”. References: SGA 3 VIIA (1.3), “more general”.

## Tag 03D8, a lemma

[Tag 03D8](https://stacks.math.columbia.edu/tag/03D8) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.conjugateEquiv_pullbackModulesCompIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean#L163). The attribute's comment: “pullback canonicity”.

> **Stacks 03D8.** The comparison `(g ∘ f)^* ≅ g^* ⋙ f^*` of pullbacks of sheaves of modules
> is the *canonical* one: its mate under the adjunctions `f^* ⊣ f_*` and `g^* ⊣ g_*` of
> Stacks 03D7 is the inverse of the comparison `(g ∘ f)_* ≅ f_* ⋙ g_*` of direct images. This is
> what pins down the normalization of the inverse-image comparison, the direct-image one being
> normalized by `AlgebraicGeometry.RingedToposHom.pushforwardModulesCompIso_underlying`.

```lean
theorem conjugateEquiv_pullbackModulesCompIso_hom (f : RingedToposHom X Y)
    (g : RingedToposHom Y Z) :
    conjugateEquiv ((pullbackAdjPushforwardModules g).comp (pullbackAdjPushforwardModules f))
        (pullbackAdjPushforwardModules (g.comp f)) (pullbackModulesCompIso f g).hom =
      (pushforwardModulesCompIso f g).inv
```

Declarations registered for the tag:

- [`AlgebraicGeometry.RingedToposHom.pushforwardModulesCompIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPushforwardComp.lean#L313), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean#L179) (StacksFrontier): “pushforward”.
- [`AlgebraicGeometry.RingedToposHom.pushforwardModulesCompIso_underlying`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPushforwardComp.lean#L323), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean#L182) (StacksFrontier): “pushforward canonicity”.
- [`AlgebraicGeometry.RingedToposHom.pullbackModulesCompIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean#L112), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean#L185) (StacksFrontier): “pullback”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.13, Tag 03D5](https://stacks.math.columbia.edu/tag/03D5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
