---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.QuasicoherentSheaves, AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isClosedImmersion, AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite, AlgebraicGeometry.Space.quasicoherentPullbackFunctor, AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_presentation, AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isFinitePresentation, AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isEtale, AlgebraicGeometry.Space.quasicoherentPullbackOfIsEtale
statement: formalized
proof: formalized
---

# 66.29 Quasi-coherent sheaves on algebraic spaces

Section 66.29 of the Stacks Project, [Tag 03G5](https://stacks.math.columbia.edu/tag/03G5). 7 tags here are carried by 47 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03G9, a definition

[Tag 03G9](https://stacks.math.columbia.edu/tag/03G9) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasicoherentSheaves`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RingedSite.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RingedSite.lean#L82).

> The category `QCoh(𝒪_F)` of quasi-coherent sheaves on the algebraic space `F`: the full
> subcategory of the `𝒪_F`-modules cut out by quasi-coherence on the small étale ringed site.

```lean
noncomputable abbrev QuasicoherentSheaves (hF : IsAlgebraicSpace B S hS F)
```

## Tag 03GA, a lemma

[Tag 03GA](https://stacks.math.columbia.edu/tag/03GA) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentPushforward.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentPushforward.lean#L81). The attribute's comment: “the inverse image along a closed immersion of algebraic spaces”.

> **Stacks 03GA along a closed immersion of algebraic spaces.**  The inverse image `i^*F` of a
> quasi-coherent `𝒪_X`-module along a closed immersion `i : Z ⟶ X` is quasi-coherent.
>
> Quasi-coherence is local on `Z`, the base changes of the affine étale charts of `X` cover `Z`,
> and over such a chart the composite to `X` factors through an affine chart, which is the case of
> Stacks 03GA already available.

```lean
theorem isQuasicoherentOnSite_modulePullback_of_isClosedImmersion (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) :
    ((modulePullback B S hS i).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModulePullbackQuasicoherentFromChartDiagrams.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModulePullbackQuasicoherentFromChartDiagrams.lean#L109). The attribute's comment: “the pullback functor preserves quasi-coherence”.

> **[Stacks, Tag 03GA].**  The pullback `f^*F` of Stacks 03LU of a quasi-coherent
> `𝒪_Y`-module along an arbitrary morphism `f : X ⟶ Y` of algebraic spaces is quasi-coherent.
>
> On the chart space of a chart of `X` carrying an affine chart diagram over `f` the pullback of
> `F` along the composite with `f` is quasi-coherent, because that composite factors through the
> structure morphism of an affine étale chart of `Y`; the composition comparison of Stacks 03LU
> turns that into quasi-coherence of the pullback of `f^*F` to the chart space, and those charts
> cover the final object of the small étale site of `X`.

```lean
theorem isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS Y.1 Y.2) (hF : F.IsQuasicoherentOnSite) :
    ((modulePullback B S hS f).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.quasicoherentPullbackFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModulePullbackQuasicoherentFromChartDiagrams.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModulePullbackQuasicoherentFromChartDiagrams.lean#L131). The attribute's comment: “the induced functor on quasi-coherent modules”.

> **[Stacks, Tag 03GA], in the form the source states it.**  The pullback of Stacks 03LU
> along an arbitrary morphism of algebraic spaces restricts to a functor
> `QCoh(𝒪_Y) ⥤ QCoh(𝒪_X)` between the categories of quasi-coherent modules of Stacks 03G9.

```lean
noncomputable def quasicoherentPullbackFunctor (f : X ⟶ Y) :
    QuasicoherentSheaves.{u, u} B S hS Y.1 Y.2 ⥤
      QuasicoherentSheaves.{u, u} B S hS X.1 X.2
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackQuasicoherence.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackQuasicoherence.lean#L223). The attribute's comment: “the pullback of a module with a global presentation is quasi-coherent”.

> **Stacks 03GA for a module with a global presentation.**  If an `𝒪_Y`-module `F` admits a
> `SheafOfModules.Presentation` then its pullback `f^*F` of Stacks 03LU along an arbitrary
> morphism `f : X ⟶ Y` of algebraic spaces is quasi-coherent.
>
> The inverse image of Stacks 03D2 is a left adjoint carrying `𝒪_Y` to `f⁻¹𝒪_Y`, so it carries
> the presentation along; extension of scalars to `𝒪_X` carries it further.

```lean
theorem isQuasicoherentOnSite_modulePullback_of_presentation (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS Y.1 Y.2) (P : F.Presentation) :
    ((modulePullback B S hS f).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackQuasicoherence.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackQuasicoherence.lean#L248). The attribute's comment: “the pullback of a module of finite presentation is quasi-coherent”.

> **Stacks 03GA for a module of finite presentation.**  The pullback `f^*F` of Stacks 03LU of
> an `𝒪_Y`-module of finite presentation along an arbitrary morphism `f : X ⟶ Y` of algebraic
> spaces is quasi-coherent.
>
> Unlike the globally presented case this assumes only *local* presentations, which transport
> along `f⁻¹` because a finite presentation over an object is a point of a sheaf of sets indexed
> by `ℕ × ℕ`.  The clause 03DL (7) of Stacks 03DO therefore holds outright, and a module of
> finite presentation is quasi-coherent.

```lean
theorem isQuasicoherentOnSite_modulePullback_of_isFinitePresentation (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS Y.1 Y.2) (hF : F.IsFinitePresentation) :
    ((modulePullback B S hS f).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackQuasicoherence.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackQuasicoherence.lean#L269). The attribute's comment: “the pullback functor preserves quasi-coherence along an étale morphism”.

> **Stacks 03GA along an étale morphism.**  The pullback functor
> `f^* : Mod(𝒪_Y) ⟶ Mod(𝒪_X)` of Stacks 03LU along an étale morphism `f : X ⟶ Y` of algebraic
> spaces preserves quasi-coherence, with no hypothesis on the module beyond quasi-coherence.
>
> Along an étale morphism the pullback of Stacks 03LU is restriction of sections along
> postcomposition of étale charts, by Stacks' Equation 03LW, and quasi-coherence is inherited by
> that restriction.

```lean
theorem isQuasicoherentOnSite_modulePullback_of_isEtale (f : X ⟶ Y)
    (hf : IsEtale B S hS f.hom) (F : Modules.{u, u} B S hS Y.1 Y.2)
    (hF : F.IsQuasicoherentOnSite) :
    ((modulePullback B S hS f).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.quasicoherentPullbackOfIsEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackQuasicoherence.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackQuasicoherence.lean#L281). The attribute's comment: “the induced functor on quasi-coherent modules, along an étale morphism”.

> **Stacks 03GA along an étale morphism, in the form the source states it**: the pullback of
> Stacks 03LU along an étale morphism of algebraic spaces restricts to a functor
> `QCoh(𝒪_Y) ⥤ QCoh(𝒪_X)` between the categories of quasi-coherent modules of Stacks 03G9.

```lean
noncomputable def quasicoherentPullbackOfIsEtale (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) :
    QuasicoherentSheaves.{u, u} B S hS Y.1 Y.2 ⥤
      QuasicoherentSheaves.{u, u} B S hS X.1 X.2
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_affineChartFactorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackQuasicoherence.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackQuasicoherence.lean#L318). The attribute's comment: “the pullback along a morphism factoring through an affine chart of the target”.

> **Stacks 03GA along a morphism factoring through an affine étale chart of the target.**  If
> `f : X ⟶ Y` factors as `k ≫ φ` with `φ` the structure morphism of an étale chart of `Y` whose
> underlying scheme is affine, then `f^*` carries quasi-coherent `𝒪_Y`-modules to quasi-coherent
> `𝒪_X`-modules, with no hypothesis on `k` and none on the module beyond quasi-coherence.
>
> This is the general case of Stacks 03GA localized at one chart of the target; see the
> implementation notes for what the general case still needs.

```lean
theorem isQuasicoherentOnSite_modulePullback_of_affineChartFactorization (f : X ⟶ Y)
    (V : SmallEtale B S hS Y.1)
    (hV : IsAffine ((BigFppfOver.toScheme B S hS).obj ((SmallEtale.toOver B S hS Y.1).obj V)))
    (k : X ⟶ chartSpace B S hS Y V) (hk : f = k ≫ chartToSpace B S hS Y V)
    (F : Modules.{u, u} B S hS Y.1 Y.2) (hF : F.IsQuasicoherentOnSite) :
    ((modulePullback B S hS f).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.quasicoherentPullbackOfAffineChartFactorization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackQuasicoherence.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackQuasicoherence.lean#L332). The attribute's comment: “the induced functor on quasi-coherent modules, through an affine chart”.

> **Stacks 03GA along a morphism factoring through an affine étale chart of the target, in the
> form the source states it**: the pullback of Stacks 03LU along `k ≫ φ`, with `φ` the structure
> morphism of an affine étale chart of `Y`, restricts to a functor `QCoh(𝒪_Y) ⥤ QCoh(𝒪_X)`
> between the categories of quasi-coherent modules of Stacks 03G9.

```lean
noncomputable def quasicoherentPullbackOfAffineChartFactorization (V : SmallEtale B S hS Y.1)
    (hV : IsAffine ((BigFppfOver.toScheme B S hS).obj ((SmallEtale.toOver B S hS Y.1).obj V)))
    (k : X ⟶ chartSpace B S hS Y V) :
    QuasicoherentSheaves.{u, u} B S hS Y.1 Y.2 ⥤
      QuasicoherentSheaves.{u, u} B S hS X.1 X.2
```

## Tag 03LZ, a lemma

[Tag 03LZ](https://stacks.math.columbia.edu/tag/03LZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_chartModuleInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueing.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueing.lean#L93). The attribute's comment: “the chartwise pullback preserves quasi-coherence”.

> **Stacks 03LZ.** The chartwise pullback of modules preserves quasi-coherence: a morphism of
> étale scheme charts of `X` represents an étale morphism of algebraic spaces, along which the
> pullback of Stacks 03LU is restriction of sections.

```lean
theorem isQuasicoherentOnSite_chartModuleInverseImage {V U : SmallEtale B S hS X.1} (f : V ⟶ U)
    (F : Modules.{u, u} B S hS (chartSpace B S hS X U).1 (chartSpace B S hS X U).2)
    (hF : F.IsQuasicoherentOnSite) :
    ((chartModuleInverseImage B S hS X f).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_iff_forall_chartModuleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueing.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueing.lean#L112). The attribute's comment: “quasi-coherence of a module is quasi-coherence of its chartwise restrictions”.

> **Stacks 03LZ.** An `𝒪_X`-module is quasi-coherent exactly when its restriction to every
> étale scheme chart of `X` is quasi-coherent: the chartwise family of restrictions of a module
> satisfies datum (1) of Stacks 03LZ precisely for the quasi-coherent modules.

```lean
theorem isQuasicoherentOnSite_iff_forall_chartModuleRestriction
    (M : Modules.{u, u} B S hS X.1 X.2) :
    M.IsQuasicoherentOnSite ↔
      ∀ U : SmallEtale B S hS X.1,
        ((chartModuleRestriction B S hS X U).obj M).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isChartwiseQuasicoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueing.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueing.lean#L126). The attribute's comment: “datum (1): the chartwise modules are quasi-coherent”.

> **Datum (1) of Stacks 03LZ**: the module of a chartwise glueing datum is quasi-coherent on
> the small étale site of every étale scheme chart of `X`.

```lean
def isChartwiseQuasicoherent : ObjectProperty (ChartModuleGlueingData B S hS X)
```

**`AlgebraicGeometry.Space.QuasicoherentChartModuleGlueingData`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueing.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueing.lean#L133). The attribute's comment: “the data (1), (2) and the cocycle condition”.

> **The data of Stacks 03LZ**: a quasi-coherent `𝒪_U`-module on the small étale site of every
> étale scheme chart `U` of `X`, transition isomorphisms along the chartwise pullbacks, and the
> cocycle condition relating them.

```lean
noncomputable abbrev QuasicoherentChartModuleGlueingData
```

**`AlgebraicGeometry.Space.quasicoherentChartModuleGlueingFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueing.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueing.lean#L160). The attribute's comment: “the canonical chartwise description of quasi-coherent modules”.

> **The canonical chartwise description of quasi-coherent `𝒪_X`-modules**: the functor of
> Stacks 03LY cut down to the quasi-coherent objects on both sides, so that composing it with the
> inclusion of the chartwise quasi-coherent data is
> `AlgebraicGeometry.Space.chartModuleGlueingFunctor` on the nose.  It is well defined because
> the restriction of a quasi-coherent module to a chart is quasi-coherent, which is
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_chartModuleRestriction`.  That this functor is an
> equivalence is Stacks 03LZ, proved as
> `AlgebraicGeometry.Space.quasicoherentChartModuleGlueingFunctor_isEquivalence` in
> `StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueingEquivalence.lean`.

```lean
noncomputable def quasicoherentChartModuleGlueingFunctor :
    QuasicoherentSheaves.{u, u} B S hS X.1 X.2 ⥤ QuasicoherentChartModuleGlueingData B S hS X
```

**`AlgebraicGeometry.Space.quasicoherentChartModuleGlueingEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueingEquivalence.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueingEquivalence.lean#L54). The attribute's comment: “quasi-coherent modules are the chartwise quasi-coherent glueing data”.

> A quasi-coherent `𝒪_X`-module on the small étale site of an algebraic space `X` is the same
> thing as a chartwise quasi-coherent glueing datum: a *quasi-coherent* `𝒪_U`-module `F_U` on the
> small étale site of every étale scheme chart `U` of `X`, transition isomorphisms
> `c_f : f^*F_U ≅ F_V` along the chartwise pullbacks of Stacks 03LU for the morphisms `f : V ⟶ U`
> of charts, and the cocycle condition `c_g ∘ g^*c_f = c_{g ≫ f}` — an *equivalence of categories*,
> given by sending a quasi-coherent module to the family of its restrictions to the charts.
>
> It is the equivalence `AlgebraicGeometry.Space.chartModuleGlueingEquivalence` of Stacks 03LY,
> cut down to the quasi-coherent objects on both sides.

```lean
def quasicoherentChartModuleGlueingEquivalence :
    QuasicoherentSheaves.{u, u} B S hS X.1 X.2 ≌ QuasicoherentChartModuleGlueingData B S hS X
```

**`AlgebraicGeometry.Space.quasicoherentChartModuleGlueingFunctor_isEquivalence`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueingEquivalence.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartQuasicoherentGlueingEquivalence.lean#L70). The attribute's comment: “the canonical chartwise description of quasi-coherent modules is an equivalence”.

> The canonical chartwise description of quasi-coherent `𝒪_X`-modules
> `AlgebraicGeometry.Space.quasicoherentChartModuleGlueingFunctor` — restriction to the étale
> scheme charts — is an equivalence onto the chartwise quasi-coherent glueing data.

```lean
instance quasicoherentChartModuleGlueingFunctor_isEquivalence :
    (quasicoherentChartModuleGlueingFunctor B S hS X).IsEquivalence
```

## Tag 05VP, a lemma

[Tag 05VP](https://stacks.math.columbia.edu/tag/05VP) in the Stacks Project.

**`AlgebraicGeometry.Space.chartLocalRingToEtaleLocalRing_germ_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartLocalRingGermsOnOpens.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChartLocalRingGermsOnOpens.lean#L106). The attribute's comment: “the comparison map on germs of functions on an open of the chart”.

> **The comparison map `𝒪_{U, u} → 𝒪_{X, x̄}` on germs of functions on an open of the
> chart.**  The ordinary germ at `u` of a regular function on a Zariski open `W ∋ u` of the chart
> is sent to the germ at `x̄` of the same function, read on the small étale neighbourhood
> `AlgebraicGeometry.Space.chartOpenNeighborhood` given by `W`.  This extends
> `AlgebraicGeometry.Space.chartLocalRingToEtaleLocalRing_germ`, which is the case `W = ⊤`.

```lean
theorem chartLocalRingToEtaleLocalRing_germ_open {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) (W : (chartScheme V.chart).Opens)
    (hw : chartPoint B S hS X V ∈ W) (a : Γ(chartScheme V.chart, W)) :
    chartLocalRingToEtaleLocalRing B S hS X hX V
        ((chartScheme V.chart).presheaf.germ W (chartPoint B S hS X V) hw a) =
      etaleLocalRingGerm B S hS X x (op (chartOpenNeighborhood B S hS V W hw))
        (W.topIso.inv a)
```

**`AlgebraicGeometry.Space.chartLocalRingToEtaleLocalRing_germ_open'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartLocalRingGermsOnOpens.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChartLocalRingGermsOnOpens.lean#L160). The attribute's comment: “the comparison map on germs, through the chart restriction of functions”.

> `AlgebraicGeometry.Space.chartLocalRingToEtaleLocalRing_germ_open` with the restricted
> function written through `AlgebraicGeometry.Space.chartRestrictionRingHom`, the form in which
> the sections of a module on the algebraic space carry their scalars over an open of the
> chart.

```lean
theorem chartLocalRingToEtaleLocalRing_germ_open' {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) (W : (chartScheme V.chart).Opens)
    (hw : chartPoint B S hS X V ∈ W) (a : Γ(chartScheme V.chart, W)) :
    chartLocalRingToEtaleLocalRing B S hS X hX V
        ((chartScheme V.chart).presheaf.germ W (chartPoint B S hS X V) hw a) =
      etaleLocalRingGerm B S hS X x (op (chartOpenNeighborhood B S hS V W hw))
        (((chartRestrictionRingHom B S hS hX V.chart).app (op W)).hom a)
```

**`AlgebraicGeometry.Space.chartStalkTensorComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartStalkTensorComparison.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChartStalkTensorComparison.lean#L311). The attribute's comment: “the comparison map (phi^* F)\_u tensor O\_\{U, u} O\_\{X, xbar} to F\_xbar”.

> The comparison map from the Zariski stalk `(φ^* F)_u` of the restriction of an `𝒪_X`-module
> to an étale scheme chart, base changed along the canonical map `𝒪_{U, u} → 𝒪_{X, x̄}`, to the
> stalk `F_{x̄}` of `F` at the geometric point.

```lean
noncomputable def chartStalkTensorComparison {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) (F : Modules.{u, m} B S hS X hX) :
    chartStalkTensorEtaleLocalRing B S hS X hX V F ⟶
      geometricModuleStalk B S hS ⟨X, hX⟩ x F
```

**`AlgebraicGeometry.Space.chartStalkTensorComparison_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartStalkTensorComparison.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChartStalkTensorComparison.lean#L321). The attribute's comment: “the comparison map is the identity on germs of sections”.

> The comparison map `(φ^* F)_u ⊗_{𝒪_{U, u}} 𝒪_{X, x̄} → F_{x̄}` sends the base change of the
> Zariski germ at `u` of a section of `F` over a Zariski open `W` of the chart containing `u` to the
> germ at `x̄` of the same section, read on the small étale neighbourhood `W`.

```lean
theorem chartStalkTensorComparison_germ {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) (F : Modules.{u, m} B S hS X hX)
    (W : (etaleChartScheme B S hS V.chart).Opens) (hw : chartPoint B S hS X V ∈ W)
    (s : F.val.obj (op ((chartOpens B S hS V.chart).obj W))) :
    chartStalkTensorComparison B S hS hX V F
        ((1 : ↥(etaleLocalRing B S hS X x)) ⊗ₜ[↥(chartLocalRing B S hS X V),
            chartLocalRingToEtaleLocalRing B S hS X hX V]
          chartZariskiSectionGerm B S hS hX V F W hw s :
          chartStalkTensorEtaleLocalRing B S hS X hX V F) =
      geometricModuleStalkGerm B S hS ⟨X, hX⟩ x F
        (chartOpenNeighborhood B S hS V W hw) s
```

**`AlgebraicGeometry.Space.isIso_chartStalkTensorComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartStalkTensorIsomorphism.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChartStalkTensorIsomorphism.lean#L197). The attribute's comment: “the comparison map is an isomorphism”.

> **Stacks 05VP.**  Let `F` be a quasi-coherent `𝒪_X`-module on an algebraic space `X`, let
> `x̄` be a geometric point of `X` and let `φ : (U, ū) → (X, x̄)` be an étale neighbourhood whose
> chart `U` is a scheme.  Then the canonical comparison map
>
> `(φ^* F)_u ⊗_{𝒪_{U, u}} 𝒪_{X, x̄} → F_{x̄}`
>
> is an isomorphism.
>
> The hypothesis of quasi-coherence is necessary: for a general `𝒪_X`-module the comparison map
> is not even surjective.  The statement is at module universe `m = u`, that is for
> `AlgebraicGeometry.Space.Modules.{u, u}`, which is where the cartesian criterion of Stacks
> 03DX(2) that quasi-coherence is used through is available.

```lean
theorem isIso_chartStalkTensorComparison {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) (F : Modules.{u, u} B S hS X hX)
    [F.IsQuasicoherentOnSite] :
    IsIso (chartStalkTensorComparison B S hS hX V F)
```

**`AlgebraicGeometry.Space.surjective_chartStalkTensorComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartStalkTensorSurjective.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChartStalkTensorSurjective.lean#L83). The attribute's comment: “the comparison map is surjective for a quasi-coherent module”.

> **The comparison map of Stacks 05VP is surjective for a quasi-coherent module.**  Every germ
> at the geometric point of a section of a quasi-coherent `𝒪_X`-module is the image of a base
> changed Zariski germ on the chart.
>
> Quasi-coherence is required: it enters through Stacks 03DX(2), which writes a section over a
> small affine étale neighbourhood as a sum of multiples of restrictions of sections over a fixed
> affine neighbourhood of the point.

```lean
theorem surjective_chartStalkTensorComparison {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) (F : Modules.{u, u} B S hS X hX)
    [F.IsQuasicoherentOnSite] :
    Function.Surjective (chartStalkTensorComparison B S hS hX V F)
```

**`AlgebraicGeometry.Space.chartLocalRingToEtaleLocalRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean#L141). The attribute's comment: “the canonical map O\_\{U, u} → O\_\{X, xbar}”.

> The canonical map `𝒪_{U, u} → 𝒪_{X, x̄}` of Stacks 05VP: the structure map of `𝒪_{U, u}`
> into its strict henselization, followed by the identification of that strict henselization with
> the étale local ring at the geometric point.

```lean
noncomputable def chartLocalRingToEtaleLocalRing {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) :
    ↥(chartLocalRing B S hS X V) →+* ↥(etaleLocalRing B S hS X x)
```

**`AlgebraicGeometry.Space.chartLocalRingToEtaleLocalRing_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean#L151). The attribute's comment: “the comparison map is the identity on germs of regular functions”.

> The canonical map `𝒪_{U, u} → 𝒪_{X, x̄}` sends the ordinary germ at `u` of a regular
> function on the chart to the germ of the same function at the geometric point.

```lean
theorem chartLocalRingToEtaleLocalRing_germ {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) (a : Γ(chartScheme V.chart, ⊤)) :
    chartLocalRingToEtaleLocalRing B S hS X hX V
        ((chartScheme V.chart).presheaf.germ ⊤ (chartPoint B S hS X V) trivial a) =
      etaleLocalRingGerm B S hS X x (op V) a
```

**`AlgebraicGeometry.Space.faithfullyFlat_chartLocalRingToEtaleLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean#L164). The attribute's comment: “the base-change map is faithfully flat”.

> **The base change of Stacks 05VP is faithfully flat.** The canonical map
> `𝒪_{U, u} → 𝒪_{X, x̄}` is faithfully flat: the étale local ring is the strict henselization of
> the chart's local ring, and a strict henselization is faithfully flat over the ring it
> henselizes.

```lean
theorem faithfullyFlat_chartLocalRingToEtaleLocalRing {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) :
    (chartLocalRingToEtaleLocalRing B S hS X hX V).FaithfullyFlat
```

**`AlgebraicGeometry.Space.flat_chartLocalRingToEtaleLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean#L182). The attribute's comment: “the base-change map is flat”.

> The canonical map `𝒪_{U, u} → 𝒪_{X, x̄}` is flat, so the base change of Stacks 05VP along
> it is exact.

```lean
theorem flat_chartLocalRingToEtaleLocalRing {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) :
    (chartLocalRingToEtaleLocalRing B S hS X hX V).Flat
```

**`AlgebraicGeometry.Space.chartStalkBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean#L196). The attribute's comment: “the base-change functor - ⊗\_\{O\_\{U, u}} O\_\{X, xbar}”.

> The base-change functor `- ⊗_{𝒪_{U, u}} 𝒪_{X, x̄}` of Stacks 05VP, taking a module over the
> local ring of the chart to a module over the étale local ring at the geometric point.

```lean
noncomputable def chartStalkBaseChange {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) :
    ModuleCat.{max u m} ↥(chartLocalRing B S hS X V) ⥤
      ModuleCat.{max (u + 1) m} ↥(etaleLocalRing B S hS X x)
```

**`AlgebraicGeometry.Space.chartZariskiModuleStalk`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean#L209). The attribute's comment: “the Zariski stalk of the chart restriction, the left factor of the tensor”.

> The ordinary (Zariski) stalk `(φ^* F)_u` of the restriction of an `𝒪_X`-module to an étale
> scheme chart, as a module over the local ring `𝒪_{U, u}` of the chart.
>
> It is the stalk of `AlgebraicGeometry.Space.restrictToChart` at the point
> `AlgebraicGeometry.Space.chartZariskiPoint` of the Zariski site of the chart, with its scalars
> restricted along `AlgebraicGeometry.Space.chartZariskiFiberIso`.

```lean
noncomputable def chartZariskiModuleStalk {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) (F : Modules.{u, m} B S hS X hX) :
    ModuleCat.{max u m} ↥(chartLocalRing B S hS X V)
```

**`AlgebraicGeometry.Space.chartStalkTensorEtaleLocalRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkBaseChange.lean#L224). The attribute's comment: “the left-hand side (phi^* F)\_u ⊗\_\{O\_\{U, u}} O\_\{X, xbar}”.

> The left-hand side `(φ^* F)_u ⊗_{𝒪_{U, u}} 𝒪_{X, x̄}` of Stacks 05VP: the Zariski stalk of
> the chart restriction, base changed along the canonical map to the étale local ring.
>
> Its type is the category in which `AlgebraicGeometry.Space.geometricModuleStalk` also lands, so
> the equation of Stacks 05VP relates two objects of one category.

```lean
noncomputable def chartStalkTensorEtaleLocalRing {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) (F : Modules.{u, m} B S hS X hX) :
    ModuleCat.{max (u + 1) m} ↥(etaleLocalRing B S hS X x)
```

## Tag 05VQ, a lemma

[Tag 05VQ](https://stacks.math.columbia.edu/tag/05VQ) in the Stacks Project.

**`AlgebraicGeometry.Space.geometricModuleStalk`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricModuleStalk.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricModuleStalk.lean#L244). The attribute's comment: “the module stalk at a geometric point”.

> **Stacks 05VQ.** The stalk of an `𝒪_X`-module at a geometric point `x̄` of an algebraic
> space, as a module over the étale local ring `𝒪_{X, x̄}`: the stalk at the point of the small
> étale site determined by `x̄`, with its scalars extended along
> `AlgebraicGeometry.Space.pointStalkRingEquiv`.

```lean
noncomputable def geometricModuleStalk (X : AlgebraicSpaces B S hS)
    (x : GeometricPoint B S hS X.1) (F : Modules.{u, m} B S hS X.1 X.2) :
    ModuleCat (etaleLocalRing B S hS X.1 x)
```

**`AlgebraicGeometry.Space.geometricModuleStalkPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricModuleStalkBaseChange.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricModuleStalkBaseChange.lean#L93). The attribute's comment: “the base-change formula `(f^*G)_x̄ ≅ 𝒪_{X, x̄} ⊗_{𝒪_{Y, f ∘ x̄}} G_{f ∘ x̄}` for the geometric stalk of a pullback of modules”.

> The stalk at a geometric point `x̄` of the
> pullback of an `𝒪_Y`-module `G` along a morphism `f : X ⟶ Y` of algebraic spaces is the base
> change of the stalk of `G` at the image point `f ∘ x̄` along the canonical homomorphism
> `𝒪_{Y, f ∘ x̄} ⟶ 𝒪_{X, x̄}` of étale local rings of Stacks 04NG:
>
> `(f^*G)_{x̄} ≅ 𝒪_{X, x̄} ⊗_{𝒪_{Y, f ∘ x̄}} G_{f ∘ x̄}`.

```lean
def geometricModuleStalkPullbackIso :
    geometricModuleStalk B S hS X x ((modulePullback B S hS f).obj G) ≅
      (ModuleCat.extendScalars (etaleLocalRingMap X.2 f.hom x)).obj
        (geometricModuleStalk B S hS Y (geometricPointMap f.hom x) G)
```

## Tag 03M0, a lemma

[Tag 03M0](https://stacks.math.columbia.edu/tag/03M0) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_iff_over_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentEtaleChart.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentEtaleChart.lean#L250). The attribute's comment: “(1) iff (3)”.

> **Stacks 03M0, conditions (1) and (3).** A sheaf of `𝒪_F`-modules on the small étale site
> of an algebraic space `F` is quasi-coherent if and only if its restriction along one étale
> chart whose structure morphism is surjective on points is quasi-coherent.
>
> The restriction is restriction to the slice of the small étale site at the chart; see the
> implementation notes.

```lean
theorem isQuasicoherentOnSite_iff_over_of_isSurjective (M : Modules.{u, u} B S hS F hF)
    (U : (smallEtaleRingedSite B S hS F hF).C) (hsurj : IsSurjective B S hS U.1.hom) :
    M.IsQuasicoherentOnSite ↔ (M.over U).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_iff_forall_affine_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentEtaleChart.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentEtaleChart.lean#L264). The attribute's comment: “(1) iff (4)”.

> **Stacks 03M0, conditions (1) and (4).** A sheaf of `𝒪_F`-modules on the small étale site
> of an algebraic space `F` is quasi-coherent if and only if its restriction along every étale
> chart whose underlying scheme is affine is quasi-coherent.
>
> The restriction is restriction to the slice of the small étale site at the chart; see the
> implementation notes.

```lean
theorem isQuasicoherentOnSite_iff_forall_affine_over (M : Modules.{u, u} B S hS F hF) :
    M.IsQuasicoherentOnSite ↔
      ∀ U : (smallEtaleRingedSite B S hS F hF).C,
        IsAffine ((BigFppfOver.toScheme B S hS).obj ((SmallEtale.toOver B S hS F).obj U)) →
        (M.over U).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_etaleModulePullback_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentEtaleMorphism.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentEtaleMorphism.lean#L256). The attribute's comment: “(1) iff (2)”.

> **Stacks 03M0, conditions (1) and (2).** A sheaf of `𝒪_X`-modules on the small étale site
> of an algebraic space `X` is quasi-coherent if and only if its pullback along an étale
> morphism `f : Y ⟶ X` of algebraic spaces which is surjective on points is quasi-coherent.
>
> The forward implication needs no surjectivity: quasi-coherence of a module is inherited by
> every étale pullback, because a covering of the composite chart of `X` lifts to a covering of
> the chart of `Y` (`AlgebraicGeometry.Space.SmallEtale.smallEtalePostcomp_cover_lift`) and
> global presentations transfer by
> `AlgebraicGeometry.Space.hasGlobalPresentation_over_postcomp_iff`.  The converse is where
> surjectivity enters: an étale chart of `Y` surjective on points composes with `f` to an étale
> chart of `X` surjective on points, which covers the final object of the small étale site of
> `X` by `AlgebraicGeometry.Space.SmallEtale.coversTop_of_isSurjective`, so every chart of `X`
> is covered by charts that map to it; those are, up to isomorphism, the composites
> of the charts of `Y`, which carry global presentations by hypothesis.

```lean
theorem isQuasicoherentOnSite_etaleModulePullback_iff (f : Y ⟶ X) (hf : IsEtale B S hS f.hom)
    (hsurj : IsSurjective B S hS f.hom) (M : Modules.{u, u} B S hS X.1 X.2) :
    M.IsQuasicoherentOnSite ↔
      ((etaleModulePullback B S hS f hf).obj M).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_iff_exists_etale_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentEtaleMorphism.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentEtaleMorphism.lean#L295). The attribute's comment: “(1) iff (2), existential form”.

> **Stacks 03M0, conditions (1) and (2), in the existential form of the source.** A sheaf of
> `𝒪_X`-modules on the small étale site of an algebraic space `X` is quasi-coherent if and only
> if there is an étale morphism `f : Z ⟶ X` of algebraic spaces, surjective on points, whose
> pullback of the module is quasi-coherent.
>
> The witness for the forward implication is the identity of `X`, which is étale because
> precomposing an étale chart with it returns the chart, and surjective on points because
> `AlgebraicGeometry.Space.pointsMap_id` is the identity.  No comparison of
> `AlgebraicGeometry.Space.smallEtalePostcomp` with the identity functor is needed: the pullback
> along the identity is quasi-coherent because
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_etaleModulePullback_iff` applies to every étale
> morphism, the identity included.

```lean
theorem isQuasicoherentOnSite_iff_exists_etale_surjective
    (M : Modules.{u, u} B S hS X.1 X.2) :
    M.IsQuasicoherentOnSite ↔
      ∃ (Z : AlgebraicSpaces B S hS) (f : Z ⟶ X) (hf : IsEtale B S hS f.hom),
        IsSurjective B S hS f.hom ∧
          ((etaleModulePullback B S hS f hf).obj M).IsQuasicoherentOnSite
```

## Tag 03M1, a lemma

[Tag 03M1](https://stacks.math.columbia.edu/tag/03M1) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_smallEtaleInternalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InternalHomQuasicoherentChartLocal.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/InternalHomQuasicoherentChartLocal.lean#L206). The attribute's comment: “(6) internal hom out of a module of finite presentation”. References: SGA 3 III (0.6), “more general”.

> **Stacks 03M1, the internal Hom.**  Let `F` be an algebraic space over a scheme `S` and let
> `M`, `N` be quasi-coherent `𝒪_F`-modules with `M` of finite presentation, Stacks 03DL(7).  Then
> the internal Hom `𝓗om_{𝒪_F}(M, N)` is quasi-coherent.
>
> The internal Hom is `AlgebraicGeometry.Space.smallEtaleInternalHom`, formed on the small étale
> ringed site of `F`; its sections over an étale chart `U` are the morphisms `M|_U ⟶ N|_U`, so they
> lie in `u + 1` even though those of `M` and `N` lie in `u`.
>
> The proof is the source's.  Quasi-coherence is local on a covering of each object
> (`Stacks.SheafOfModules.isQuasicoherentOnSite_of_locally_over`), the finite-presentation
> hypothesis supplies for each étale chart a covering on whose members `M` has a finite global
> presentation, and on such a member the conclusion is
> `isQuasicoherentOnSite_smallEtaleInternalHom_over_of_hasFiniteGlobalPresentation`: restriction
> to an étale chart is a localization and formation of internal Hom commutes with localization
> (Stacks 04M1 and 0E8H), so the chart case is the globally presented case
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_smallEtaleInternalHom_of_presentation'` on the
> small étale site of the chart.
>
> The source also assumes `M` quasi-coherent; that hypothesis is omitted here, since finite
> presentation already implies it.

```lean
theorem isQuasicoherentOnSite_smallEtaleInternalHom (M N : Modules.{u, u} B S hS F hF)
    (hN : N.IsQuasicoherentOnSite)
    (hMfp : M.IsFinitePresentationOnSite) :
    (smallEtaleInternalHom B S hS F hF M N).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherent_left_of_shortExact'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentClausesUnconditional.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentClausesUnconditional.lean#L172). The attribute's comment: “clause (4), left term, for the small étale site of an algebraic space, at module universe u”.

> **Stacks 03M1 for short exact sequences, left term, at `m := u`, with nothing assumed.**  The
> kernel term of a short exact sequence of `𝒪_F`-modules on an algebraic space is quasi-coherent if
> the other two terms are.
>
> No instance of Stacks 03DW occurs, because sections of a short exact sequence are left exact;
> this is `AlgebraicGeometry.Space.isQuasicoherent_left_of_shortExact` with its `h03DX` supplied by
> `AlgebraicGeometry.Space.isCartesianOnAffineCharts_of_isQuasicoherentOnSite`.

```lean
theorem isQuasicoherent_left_of_shortExact'
    (T : ShortComplex (Modules.{u, u} B S hS F hF)) (hT : T.ShortExact)
    [T.X₂.IsQuasicoherentOnSite] [T.X₃.IsQuasicoherentOnSite] :
    T.X₁.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherent_middle_of_shortExact'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentClausesUnconditional.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentClausesUnconditional.lean#L188). The attribute's comment: “clause (4), middle term, for the small étale site of an algebraic space, at module universe u”.

> **Stacks 03M1 for short exact sequences, middle term, at `m := u`, with nothing assumed.**  An
> extension of quasi-coherent `𝒪_F`-modules on an algebraic space is quasi-coherent.
>
> This is `AlgebraicGeometry.Space.isQuasicoherent_middle_of_shortExact` with its `h03DX` supplied
> by `AlgebraicGeometry.Space.isCartesianOnAffineCharts_of_isQuasicoherentOnSite` and its
> `T.g`-specific instance of Stacks 03DW by
> `AlgebraicGeometry.Space.surjective_g_val_app_of_shortExact_of_isCartesian`.

```lean
theorem isQuasicoherent_middle_of_shortExact'
    (T : ShortComplex (Modules.{u, u} B S hS F hF)) (hT : T.ShortExact)
    [T.X₁.IsQuasicoherentOnSite] [T.X₃.IsQuasicoherentOnSite] :
    T.X₂.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherent_right_of_shortExact'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentClausesUnconditional.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentClausesUnconditional.lean#L206). The attribute's comment: “clause (4), right term, for the small étale site of an algebraic space, at module universe u”.

> **Stacks 03M1 for short exact sequences, right term, at `m := u`, with nothing assumed.**  The
> quotient term of a short exact sequence of `𝒪_F`-modules on an algebraic space is quasi-coherent
> if the other two terms are.
>
> Its two hypotheses are supplied as in
> `AlgebraicGeometry.Space.isQuasicoherent_middle_of_shortExact'`.

```lean
theorem isQuasicoherent_right_of_shortExact'
    (T : ShortComplex (Modules.{u, u} B S hS F hF)) (hT : T.ShortExact)
    [T.X₁.IsQuasicoherentOnSite] [T.X₂.IsQuasicoherentOnSite] :
    T.X₃.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_of_isColimit_cofan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSheavesProperties.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSheavesProperties.lean#L154). The attribute's comment: “(1) any direct sum of quasi-coherent 𝒪\_X-modules is quasi-coherent”.

> **Stacks 03M1 (1).**  Any direct sum of quasi-coherent `𝒪_X`-modules on an algebraic space
> `X` is quasi-coherent: the vertex of a colimiting cofan on a family of quasi-coherent
> `𝒪_X`-modules, indexed by an arbitrary type, is quasi-coherent.
>
> This is `AlgebraicGeometry.Space.isQuasicoherentOnSite_of_isColimit_cofan_of_h03DX` with Descent,
> Proposition 03DX(2) supplied by
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_iff_isCartesianOnAffineCharts`.

```lean
theorem isQuasicoherentOnSite_of_isColimit_cofan {ι : Type w}
    {G : ι → Modules.{u, u} B S hS F hF} (c : Cofan G) (hc : IsColimit c)
    (hG : ∀ i, (G i).IsQuasicoherentOnSite) :
    c.pt.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isClosedUnderColimitsOfShape_quasicoherentSheaves_of_essentiallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSheavesProperties.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSheavesProperties.lean#L170). The attribute's comment: “(2) any colimit of quasi-coherent 𝒪\_X-modules is quasi-coherent”.

> **Stacks 03M1 (2).**  Any colimit of quasi-coherent `𝒪_X`-modules on an algebraic space `X`
> is quasi-coherent: quasi-coherence is closed under colimits of every small shape `K`.
>
> The shape `K` is replaced by its small model, for which this is
> `AlgebraicGeometry.Space.isClosedUnderColimitsOfShape_quasicoherentSheaves_schemeUniverse`: a
> colimit is the cokernel of a map between two direct sums, and clauses (1) and (3) apply.

```lean
theorem isClosedUnderColimitsOfShape_quasicoherentSheaves_of_essentiallySmall (K : Type w)
    [Category.{w'} K] [EssentiallySmall.{u} K] :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B S hS F hF).O))).IsClosedUnderColimitsOfShape K
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_kernel_and_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSheavesProperties.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSheavesProperties.lean#L185). The attribute's comment: “(3) the kernel and the cokernel of a morphism of quasi-coherent 𝒪\_X-modules are quasi-coherent”.

> **Stacks 03M1 (3).**  The kernel and the cokernel of a morphism of quasi-coherent
> `𝒪_X`-modules on an algebraic space `X` are quasi-coherent.

```lean
theorem isQuasicoherentOnSite_kernel_and_cokernel {M N : Modules.{u, u} B S hS F hF}
    (f : M ⟶ N) (hM : M.IsQuasicoherentOnSite) (hN : N.IsQuasicoherentOnSite) :
    (kernel f).IsQuasicoherentOnSite ∧ (cokernel f).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_shortExact_twoOutOfThree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSheavesProperties.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSheavesProperties.lean#L213). The attribute's comment: “(4) in a short exact sequence of 𝒪\_X-modules, if two of the three terms are quasi-coherent so is the third”.

> **Stacks 03M1 (4).**  Given a short exact sequence `0 → 𝓕₁ → 𝓕₂ → 𝓕₃ → 0` of `𝒪_X`-modules
> on an algebraic space `X`, if two out of the three terms are quasi-coherent then so is the
> third.

```lean
theorem isQuasicoherentOnSite_shortExact_twoOutOfThree
    {T : ShortComplex (Modules.{u, u} B S hS F hF)} (hT : T.ShortExact) :
    (T.X₂.IsQuasicoherentOnSite → T.X₃.IsQuasicoherentOnSite → T.X₁.IsQuasicoherentOnSite) ∧
      (T.X₁.IsQuasicoherentOnSite → T.X₃.IsQuasicoherentOnSite →
        T.X₂.IsQuasicoherentOnSite) ∧
      (T.X₁.IsQuasicoherentOnSite → T.X₂.IsQuasicoherentOnSite →
        T.X₃.IsQuasicoherentOnSite)
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_tensorModule_schemeUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSheavesProperties.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSheavesProperties.lean#L236). The attribute's comment: “(5) the tensor product of two quasi-coherent 𝒪\_X-modules is quasi-coherent”.

> **Stacks 03M1 (5).**  The tensor product of two quasi-coherent `𝒪_X`-modules on an algebraic
> space `X` is quasi-coherent.
>
> The tensor product is `AlgebraicGeometry.Space.tensorModule`, the sheafified objectwise tensor
> product on the small étale ringed site; the two sheafification conditions it uses hold at the
> universe of the schemes.

```lean
theorem isQuasicoherentOnSite_tensorModule_schemeUniverse (M N : Modules.{u, u} B S hS F hF)
    (hM : M.IsQuasicoherentOnSite) (hN : N.IsQuasicoherentOnSite) :
    (tensorModule.{u, u, u} B S hS F hF M N).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_internalHomSheafSmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSheavesProperties.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSheavesProperties.lean#L303). The attribute's comment: “(6) the internal Hom 𝓗om(𝓕, 𝓖) of two quasi-coherent 𝒪\_X-modules with 𝓕 of finite presentation is quasi-coherent”. References: SGA 3 III (0.6), “more general”.

> **Stacks 03M1 (6).**  Let `𝓕`, `𝓖` be quasi-coherent `𝒪_X`-modules on an algebraic space `X`
> with `𝓕` of finite presentation (Stacks 03DL(7)).  Then the internal Hom
> `𝓗om_{𝒪_X}(𝓕, 𝓖)` is quasi-coherent.
>
> The internal Hom is the one of Stacks 03EM in `Mod(𝒪_X)`,
> `AlgebraicGeometry.RingedSite.internalHomSheafSmall`; see the module documentation.  The
> quasi-coherence of `𝓕` is part of the source's statement; the argument does not use it, a module
> of finite presentation being quasi-coherent.  Quasi-coherence is local on the members of a
> covering family (Stacks 03DN), the charts over which `𝓕` has a finite presentation cover `X`, and
> over each of them
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_over_internalHomSheafSmall` applies.

```lean
theorem isQuasicoherentOnSite_internalHomSheafSmall (M N : Modules.{u, u} B S hS F hF)
    (_hM : M.IsQuasicoherentOnSite) (hN : N.IsQuasicoherentOnSite)
    (hfp : M.IsFinitePresentationOnSite) :
    letI := smallEtaleRingedSite_essentiallySmall B S hS F hF
    (RingedSite.internalHomSheafSmall (smallEtaleRingedSite B S hS F hF) M
      N).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_tensorModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentTensorProduct.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentTensorProduct.lean#L132). The attribute's comment: “(5) tensor products”.

> **Stacks 03M1, tensor products.**  The tensor product of two quasi-coherent `𝒪_F`-modules on
> an algebraic space is quasi-coherent.
>
> The tensor product is `AlgebraicGeometry.Space.tensorModule`, formed on the small étale ringed
> site of `F`; the sections of the two factors may lie in independent universes.

```lean
theorem isQuasicoherentOnSite_tensorModule (M : Modules.{u, m} B S hS F hF)
    (N : Modules.{u, n} B S hS F hF) (hM : M.IsQuasicoherentOnSite)
    (hN : N.IsQuasicoherentOnSite) :
    (tensorModule B S hS F hF M N).IsQuasicoherentOnSite
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.29, Tag 03G5](https://stacks.math.columbia.edu/tag/03G5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
