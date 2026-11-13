---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.representedToSchemeZariskiRingedToposHom, AlgebraicGeometry.SmallEtale.toZariskiRingedToposHom, AlgebraicGeometry.SmallEtale.preservesFiniteLimits_associatedModule, AlgebraicGeometry.SmallEtale.isZero_of_isZero_associatedModule, AlgebraicGeometry.SmallEtale.isFlatMapULift_inverseImageStructureMap, AlgebraicGeometry.SmallEtale.isRightAdjoint_toZariskiModulePushforward, AlgebraicGeometry.SmallEtale.exactFunctor_pullbackModules_toZariski, AlgebraicGeometry.SmallEtale.isZero_of_isZero_toZariskiModulePullback
statement: formalized
proof: formalized
---

# 75.4 Derived category of quasi-coherent modules on the small étale site

Section 75.4 of the Stacks Project, [Tag 071P](https://stacks.math.columbia.edu/tag/071P). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08H7, an equation

[Tag 08H7](https://stacks.math.columbia.edu/tag/08H7) in the Stacks Project.

**`AlgebraicGeometry.Space.representedToSchemeZariskiRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentedSchemeZariskiRingedToposHom.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RepresentedSchemeZariskiRingedToposHom.lean#L283). The tag is given by the `attribute` command at [StacksFrontier/AlgebraicGeometry/Spaces/RepresentedSchemeZariskiRingedToposHom.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RepresentedSchemeZariskiRingedToposHom.lean#L296). The attribute's comment: “the morphism ε of the displayed equation, as a morphism of ringed topoi, for the small étale site of an algebraic space represented by a scheme — the same ε as `AlgebraicGeometry.SmallEtale.toZariskiAbstractRingedToposHom`, read along the equivalence of that site with the small étale site of the representing scheme”.

> **`ε : (X_étale, 𝒪_X) ⟶ (X_{0, Zar}, 𝒪_{X_0})` as a morphism of ringed topoi**, for `X = h_U`
> the algebraic space represented by an object `U` of the big fppf site over `S` and `X_0` the
> scheme underlying `U`.
>
> This is Equation 75.4.0.1 of Stacks Section 75.4, read on the small étale site of the algebraic
> space: the composite of the equivalence of that site with the small étale site of `X_0`
> (`AlgebraicGeometry.Space.representedEtaleRingedToposHom`) with the comparison
> `AlgebraicGeometry.SmallEtale.toZariskiAbstractRingedToposHom` of the small étale and small
> Zariski sites of `X_0`.
>
> Being a morphism of ringed topoi, it carries `ε⁻¹` on sheaves of commutative rings
> (`AlgebraicGeometry.Space.representedZariskiInverseImageCommRing`) and the inverse-image form
> `ε⁻¹𝒪_{X_0} ⟶ 𝒪_X` of its structure map
> (`AlgebraicGeometry.Space.representedZariskiStructureSharpInverseImage`), which is what the
> canonical map of Stacks 0D0X is built from.

```lean
public def representedToSchemeZariskiRingedToposHom :
    AlgebraicGeometry.RingedToposHom
      (smallEtaleRingedTopos B S hS (representedAlgebraicSpace B S hS U))
      ((BigFppfOver.toScheme B S hS).obj U).zariskiRingedTopos
```

Declarations registered for the tag:

- [`AlgebraicGeometry.SmallEtale.toZariskiRingedToposHom`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRingedToposHom.lean#L156), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRingedToposHom.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRingedToposHom.lean#L166) (StacksFrontier).

## Tag 08H8, a lemma

[Tag 08H8](https://stacks.math.columbia.edu/tag/08H8) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.preservesFiniteLimits_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleExactAssociatedModule.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleExactAssociatedModule.lean#L93). The attribute's comment: “the exactness assertion: `ε^* : Mod(𝒪_S) → Mod(𝒪_étale)` is left exact, hence exact, right exactness being automatic for a left adjoint. The flatness assertion is carried by isFlatMapULift\_inverseImageStructureMap; the zero-detection assertion `ε^*𝓕 = 0 ⟹ 𝓕 = 0` is not carried here, and is available for a quasi-coherent module as isZero\_of\_isZero\_associatedModule”.

> **The exactness assertion of Stacks 08H8.**  The associated-module functor
> `ε^* = (𝓕 ↦ 𝓕^a)` of Stacks 03DU (4) at `τ = étale` is left exact.
>
> Stacks 08H8 deduces this from flatness of `ε`, which is Stacks 0GNA; the criterion is Stacks
> 04JC, available for the pullback of sheaves of modules along the four-field morphism of ringed
> topoi attached to `ε`, and that pullback is `ε^*` by
> `AlgebraicGeometry.RingedSite.HomGeneral.pullbackModulesToposIsoGeneral`.

```lean
public theorem preservesFiniteLimits_associatedModule :
    PreservesFiniteLimits (associatedModule B S hS)
```

**`AlgebraicGeometry.SmallEtale.isZero_of_isZero_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFiniteType.lean, line 532](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFiniteType.lean#L532). The attribute's comment: “the zero-detection assertion `ε^*𝓕 = 0 ⟹ 𝓕 = 0`, for quasi-coherent `𝓕`, by a route needing no exactness. The flatness assertion is `isFlatMapULift_inverseImageStructureMap`, the exactness assertion is `preservesFiniteLimits_associatedModule`, and zero detection for an arbitrary `𝒪_X`-module is `isZero_of_isZero_associatedModule_general`.”.

> **Stacks 08H8, the zero-detection assertion, for quasi-coherent modules.**  A quasi-coherent
> `𝒪_X`-module `𝓕` whose pullback `ε^*𝓕` along the morphism of ringed sites
> `ε : (X_étale, 𝒪) ⟶ (X_Zar, 𝒪_X)` is a zero object is itself a zero object.
>
> The unit of the associated-module adjunction is a monomorphism at `𝓕`, and it factors through
> `ε_*ε^*𝓕`, which vanishes with `ε^*𝓕`; so the identity of `𝓕` vanishes.  The source instead
> computes the stalk of `ε^*𝓕` at a geometric point as `𝓕_x ⊗_{𝒪_{X, x}} 𝒪_{étale, x̄}` and
> appeals to faithful flatness of the strict henselization. For an arbitrary `𝒪_X`-module the
> assertion is `AlgebraicGeometry.SmallEtale.isZero_of_isZero_associatedModule_general`.

```lean
theorem isZero_of_isZero_associatedModule (F : X.Modules) [F.IsQuasicoherent]
    (h : IsZero ((associatedModule B X hX).obj F)) : IsZero F
```

**`AlgebraicGeometry.SmallEtale.isFlatMapULift_inverseImageStructureMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFlatInverseImage.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFlatInverseImage.lean#L354). The attribute's comment: “the flatness assertion: `ε` is a flat morphism of ringed sites. The exactness of `ε^* : Mod(𝒪_X) → Mod(𝒪_étale)` is carried by `AlgebraicGeometry.SmallEtale.exactFunctor_pullbackModules_toZariski`; the faithfulness assertion `ε^*𝓕 = 0 ⟹ 𝓕 = 0` is not carried here and is not in the library”.

> **Stacks 0GNA.**  The morphism of ringed sites `ε = id_{small, étale, Zar} : S_étale → S_Zar`
> is flat: `𝒪_{S_étale}` is a flat module over `ε⁻¹𝒪_{S_Zar}`, the flatness being asserted for
> the structure map `AlgebraicGeometry.SmallEtale.inverseImageStructureMap` of `ε` in
> inverse-image form.
>
> This is also the first assertion of **Stacks 08H8**, which states exactly that the `ε` of
> Equation 75.4.0.1 — `AlgebraicGeometry.SmallEtale.toZariskiRingedToposHom`, carrying Stacks
> 08H7 — is a flat morphism of ringed sites, and cites Descent, Lemma 35.10.1, which is 0GNA,
> for it.  The second assertion of 08H8, exactness of `ε^*`, is carried by
> `AlgebraicGeometry.SmallEtale.exactFunctor_pullbackModules_toZariski`.  The third, the
> implication `ε^*𝓕 = 0 ⟹ 𝓕 = 0`, is *not* carried by this statement and is not available in
> the library; the attribute clause records that scope.

```lean
public theorem isFlatMapULift_inverseImageStructureMap :
    AlgebraicGeometry.SheafOfModules.IsFlatMapULift.{u, u + 1, u}
      (inverseImageStructureMap B S hS)
```

**`AlgebraicGeometry.SmallEtale.isRightAdjoint_toZariskiModulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtalePullbackExact.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtalePullbackExact.lean#L143). The attribute's comment: “the existence assertion: the direct image `ε_*` of sheaves of modules along `ε` has a left adjoint, i.e. `ε^* : Mod(𝒪_S) ⟶ Mod(𝒪_{S_étale})` exists. Both functors are taken in the sense of Stacks 03D6 for the two-field morphism of ringed topoi of Stacks 01D3 (2) carrying `ε`, which is the library's spelling of the pair; the left adjoint is `AlgebraicGeometry.SmallEtale.toZariskiModulePullback`”.

> **Stacks 08H8, the existence assertion.**  The direct image `ε_*` of sheaves of modules
> along `ε = id_{small, étale, Zar} : S_étale → S_Zar` has a left adjoint, i.e. the pullback
> `ε^* : Mod(𝒪_S) ⟶ Mod(𝒪_{S_étale})` exists.
>
> The left adjoint is `AlgebraicGeometry.SmallEtale.toZariskiModulePullback` and the adjunction
> exhibiting it is `AlgebraicGeometry.SmallEtale.toZariskiModulePullbackAdjPushforward`.

```lean
public theorem isRightAdjoint_toZariskiModulePushforward :
    (toZariskiModulePushforward B S hS).IsRightAdjoint
```

**`AlgebraicGeometry.SmallEtale.exactFunctor_pullbackModules_toZariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtalePullbackExact.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtalePullbackExact.lean#L168). The attribute's comment: “the exactness assertion: `ε^* : Mod(𝒪_S) ⟶ Mod(𝒪_{S_étale})` is exact, for `ε` the morphism of ringed topoi of Equation 75.4.0.1 in the two-field shape of Stacks 01D3 (2). The flatness assertion is carried by `AlgebraicGeometry.SmallEtale.isFlatMapULift_inverseImageStructureMap`; the implication `ε^*𝓕 = 0 ⟹ 𝓕 = 0` is not carried here”.

> **Stacks 08H8, the exactness assertion.**  The pullback `ε^*` of sheaves of modules along
> `ε = id_{small, étale, Zar} : S_étale → S_Zar` is exact: it preserves finite limits and finite
> colimits.
>
> The flatness assertion of the same tag is
> `AlgebraicGeometry.SmallEtale.isFlatMapULift_inverseImageStructureMap`, which is Stacks 0GNA;
> the remaining assertion, that `ε^*𝓕 = 0` implies `𝓕 = 0`, is not carried here.

```lean
public theorem exactFunctor_pullbackModules_toZariski :
    exactFunctor
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.zariskiRingedTopos.O))
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (ringedTopos B S hS).O))
      (toZariskiModulePullback B S hS)
```

**`AlgebraicGeometry.SmallEtale.isZero_of_isZero_toZariskiModulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtalePullbackExact.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtalePullbackExact.lean#L290). The attribute's comment: “the faithfulness assertion: `ε^*𝓕 = 0 ⟹ 𝓕 = 0`, for `ε^*` the pullback of sheaves of modules of Stacks 03D6 (2) along the two-field morphism of ringed topoi of Stacks 01D3 (2) carrying `ε`. The flatness assertion is carried by `AlgebraicGeometry.SmallEtale.isFlatMapULift_inverseImageStructureMap`, the exactness assertion by `AlgebraicGeometry.SmallEtale.exactFunctor_pullbackModules_toZariski` and the existence assertion by `AlgebraicGeometry.SmallEtale.isRightAdjoint_toZariskiModulePushforward`”.

> **Stacks 08H8, the faithfulness assertion.**  If the pullback `ε^*𝓕` of a sheaf of
> `𝒪_S`-modules along `ε = id_{small, étale, Zar} : S_étale → S_Zar` vanishes, then `𝓕` vanishes.
>
> The pullback is the inverse image of Stacks 03D2 followed by extension of scalars along the
> structure map, and the two halves are reflected separately.  Extension of scalars reflects the
> zero sheaf because the structure map is locally faithfully flat over the comparison presheaf
> `(f : V → S) ↦ 𝒪_S(f(V))`
> (`AlgebraicGeometry.SmallEtale.locallyFaithfullyFlat_imageSectionsRestriction`), and the
> inverse image reflects it by
> `AlgebraicGeometry.SmallEtale.isZero_of_isZero_inverseImageModules`.

```lean
public theorem isZero_of_isZero_toZariskiModulePullback
    (𝓕 : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.zariskiRingedTopos.O))
    (h : IsZero ((toZariskiModulePullback B S hS).obj 𝓕)) : IsZero 𝓕
```

## Tag 071Q, a lemma

[Tag 071Q](https://stacks.math.columbia.edu/tag/071Q) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.derivedAssociatedModule_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDerivedEquivalence.lean, line 524](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDerivedEquivalence.lean#L524).

> **Stacks 071Q.**  For a scheme `S`, the functor `ε^* : D_QCoh(𝒪_S) ⟶ D_QCoh(S_étale, 𝒪)`
> induced by the exact functor `ε^*` of Stacks 08H8 is an equivalence.
>
> The quasi-inverse is `Rε_*`, `AlgebraicGeometry.SmallEtale.derivedRestrictModuleQcoh`, as in the
> source: the adjunction `ε^* ⊣ Rε_*` restricts to the two derived categories with quasi-coherent
> cohomology, where its unit and counit are isomorphisms because `H^q(Rε_* E) = ε_* H^q(E)` for
> `E` with quasi-coherent cohomology (Stacks 03DW, 01XB and 0BKZ) and `ε^*` and `ε_*` are mutually
> inverse on quasi-coherent modules (Stacks 03DX).

```lean
theorem derivedAssociatedModule_isEquivalence :
    (derivedAssociatedModule.{w} B S hS).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.4, Tag 071P](https://stacks.math.columbia.edu/tag/071P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
