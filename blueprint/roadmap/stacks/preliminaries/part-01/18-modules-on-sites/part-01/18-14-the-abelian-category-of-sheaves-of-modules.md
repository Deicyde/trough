---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.instPreservesFiniteColimitsToSheaf, Stacks.SheafOfModules.toSheafKernelIso, Stacks.SheafOfModules.toSheafCokernelIso, Stacks.SheafOfModules.exact_iff_toSheaf_exact, SheafOfModules.instAbelian, SheafOfModules.instPreservesFiniteLimitsSheafAddCommGrpCatToSheaf, AlgebraicGeometry.SheafOfModules.instAB5SheafOfModules, AlgebraicGeometry.SheafOfModules.toSheaf_preservesLimits
statement: formalized
proof: formalized
---

# 18.14 The abelian category of sheaves of modules

Section 18.14 of the Stacks Project, [Tag 03D9](https://stacks.math.columbia.edu/tag/03D9). 4 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03DA, a lemma

[Tag 03DA](https://stacks.math.columbia.edu/tag/03DA) in the Stacks Project.

**`Stacks.SheafOfModules.instPreservesFiniteColimitsToSheaf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Abelian.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Abelian.lean#L81). The attribute's comment: “exact forgetful functor”.

> The forgetful functor from sheaves of modules to abelian sheaves preserves finite colimits,
> including cokernels. Together with its finite-limit preservation this says the functor is
> exact.

```lean
public noncomputable instance instPreservesFiniteColimitsToSheaf
    [HasSheafify J AddCommGrpCat.{v}]
    [J.WEqualsLocallyBijective AddCommGrpCat.{v}] :
    PreservesFiniteColimits (_root_.SheafOfModules.toSheaf.{v} R)
```

**`Stacks.SheafOfModules.toSheafKernelIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Abelian.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Abelian.lean#L113). The attribute's comment: “kernels correspond”.

> Kernels of sheaves of modules correspond to kernels of abelian sheaves: the forgetful
> functor carries the kernel of a morphism `f` of sheaves of modules to the kernel of the
> underlying morphism of abelian sheaves.

```lean
public noncomputable def toSheafKernelIso {M N : _root_.SheafOfModules.{v} R} (f : M ⟶ N) :
    (_root_.SheafOfModules.toSheaf.{v} R).obj (kernel f) ≅
      kernel ((_root_.SheafOfModules.toSheaf.{v} R).map f)
```

**`Stacks.SheafOfModules.toSheafCokernelIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Abelian.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Abelian.lean#L122). The attribute's comment: “cokernels correspond”.

> Cokernels of sheaves of modules correspond to cokernels of abelian sheaves: the forgetful
> functor carries the cokernel of a morphism `f` of sheaves of modules to the cokernel of the
> underlying morphism of abelian sheaves.

```lean
public noncomputable def toSheafCokernelIso {M N : _root_.SheafOfModules.{v} R} (f : M ⟶ N) :
    (_root_.SheafOfModules.toSheaf.{v} R).obj (cokernel f) ≅
      cokernel ((_root_.SheafOfModules.toSheaf.{v} R).map f)
```

**`Stacks.SheafOfModules.exact_iff_toSheaf_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Abelian.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Abelian.lean#L131). The attribute's comment: “exactness corresponds”.

> Exactness of sheaves of modules corresponds to exactness of abelian sheaves: a short
> complex of sheaves of `R`-modules is exact if and only if the underlying short complex of
> abelian sheaves is.

```lean
public theorem exact_iff_toSheaf_exact (S : ShortComplex (_root_.SheafOfModules.{v} R)) :
    (S.map (_root_.SheafOfModules.toSheaf.{v} R)).Exact ↔ S.Exact
```

Declarations registered for the tag:

- [`SheafOfModules.instAbelian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.instAbelian#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Abelian.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Abelian.lean#L60) (StacksFrontier): “abelian category”. References: SGA 3 I (3.1.1), “more general”; SGA 3 I (4.7.1.1), “more general”; SGA 4 II (6.7); SGA 4 IV (11.1.2), “partial”; SGA 4 Vbis (2.4.0), “The fibers of Mod(E°”; SGA 4 XVII (2.2.6), “partial”; SGA 6 I (1.3), “partial”.
- [`SheafOfModules.instPreservesFiniteLimitsSheafAddCommGrpCatToSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.instPreservesFiniteLimitsSheafAddCommGrpCatToSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Abelian.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Abelian.lean#L69) (StacksFrontier): “exact forgetful functor”. References: SGA 4 V (3.5), “left exactness of M ↦ ℳ”.

## Tag 03DB, a lemma

[Tag 03DB](https://stacks.math.columbia.edu/tag/03DB) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.instAB5SheafOfModules`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Colimits.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Colimits.lean#L182). The attribute's comment: “exactness of filtered colimits”. References: SGA 4 II (6.7), “(AB 5)”; SGA 3 I (3.1.1), “more general”.

> Filtered colimits of sheaves of modules are exact.

```lean
noncomputable instance instAB5SheafOfModules (R : Sheaf J RingCat.{u}) :
    AB5OfSize.{v, v} (_root_.SheafOfModules.{v} R)
```

**`AlgebraicGeometry.SheafOfModules.toSheaf_preservesLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Colimits.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Colimits.lean#L199). The attribute's comment: “forgetful functor preserves limits”.

> Forgetting a sheaf of modules to an abelian sheaf preserves all limits
> indexed by diagram objects in the module universe.

```lean
theorem toSheaf_preservesLimits :
    PreservesLimitsOfSize.{max u' v, v} (_root_.SheafOfModules.toSheaf.{v} R)
```

**`AlgebraicGeometry.SheafOfModules.toSheaf_preservesColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Colimits.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Colimits.lean#L243). The attribute's comment: “forgetful functor preserves colimits”.

> Forgetting a sheaf of modules to an abelian sheaf preserves all colimits.

```lean
theorem toSheaf_preservesColimits
    [HasWeakSheafify J AddCommGrpCat.{v}]
    [J.WEqualsLocallyBijective AddCommGrpCat.{v}] :
    PreservesColimitsOfSize.{max u' v, v} (_root_.SheafOfModules.toSheaf.{v} R)
```

Declarations registered for the tag:

- [`SheafOfModules.hasLimitsOfSize`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.hasLimitsOfSize#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/Colimits.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Colimits.lean#L60) (StacksFrontier): “existence of limits”.
- [`SheafOfModules.instHasColimitsOfSizeOfPresheafOfModulesObjFunctorOppositeRingCatIsSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.instHasColimitsOfSizeOfPresheafOfModulesObjFunctorOppositeRingCatIsSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/Colimits.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Colimits.lean#L61) (StacksFrontier): “existence of colimits”.

## Tag 03DC, a lemma

[Tag 03DC](https://stacks.math.columbia.edu/tag/03DC) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.pushforwardModules_preservesLimitsOfSize`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullback.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullback.lean#L400). The attribute's comment: “part (1): the direct image commutes with all limits”.

> **Stacks 03DC, part (1).** The direct image of sheaves of modules along a morphism of ringed
> topoi commutes with all limits, of every diagram size: it is a right adjoint, the left adjoint
> being the pullback `f^*` of Stacks 03D6.

```lean
theorem pushforwardModules_preservesLimitsOfSize (f : RingedToposHom X Y) :
    PreservesLimitsOfSize.{t, t'} (pushforwardModules f)
```

**`AlgebraicGeometry.RingedToposHom.pushforwardModules_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullback.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullback.lean#L410). The attribute's comment: “part (1): the direct image is left exact”. References: SGA 4 V (5.0), “left exactness of u\_*”; SGA 4 IV (13.6), “u\_* left exact”.

> **Stacks 03DC, part (1).** The direct image of sheaves of modules along a morphism of ringed
> topoi is left exact. This is the finite case of
> `AlgebraicGeometry.RingedToposHom.pushforwardModules_preservesLimitsOfSize`.

```lean
theorem pushforwardModules_preservesFiniteLimits (f : RingedToposHom X Y) :
    PreservesFiniteLimits (pushforwardModules f)
```

**`AlgebraicGeometry.RingedToposHom.pullbackModules_preservesColimitsOfSize`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullback.lean, line 420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullback.lean#L420). The attribute's comment: “part (2): the pullback commutes with all colimits”. References: SGA 4 IV (13.6), “u* commutes w/ colimits”; SGA 4 IV (11.2.2), “j\_X^* inductive limits”.

> **Stacks 03DC, part (2).** The pullback of sheaves of modules along a morphism of ringed
> topoi commutes with all colimits, of every diagram size: it is a left adjoint, the right adjoint
> being the direct image `f_*` of Stacks 03D6.

```lean
theorem pullbackModules_preservesColimitsOfSize (f : RingedToposHom X Y) :
    PreservesColimitsOfSize.{t, t'} (f.toModulesHom.pullbackModules)
```

**`AlgebraicGeometry.RingedToposHom.pullbackModules_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullback.lean, line 428](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullback.lean#L428). The attribute's comment: “part (2): the pullback is right exact”. References: SGA 4 IV (13.6), “u* right exact”.

> **Stacks 03DC, part (2).** The pullback of sheaves of modules along a morphism of ringed
> topoi is right exact. This is the finite case of
> `AlgebraicGeometry.RingedToposHom.pullbackModules_preservesColimitsOfSize`.

```lean
theorem pullbackModules_preservesFiniteColimits (f : RingedToposHom X Y) :
    PreservesFiniteColimits (f.toModulesHom.pullbackModules)
```

## Tag 05V3, a lemma

[Tag 05V3](https://stacks.math.columbia.edu/tag/05V3) in the Stacks Project.

**`Stacks.StalkExact.exact_iff_forall_sheafFiber_exact_of_hasEnoughPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExactEnoughPoints.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExactEnoughPoints.lean#L56). The attribute's comment: “enough Mathlib points (`GrothendieckTopology.HasEnoughPoints`)”.

> On a site with enough points, a short complex of abelian sheaves is exact if and only if its
> stalks at all points are exact.
>
> Points and "enough points" are Mathlib's (`GrothendieckTopology.Point`,
> `GrothendieckTopology.HasEnoughPoints`); the form for the points of Stacks 00Y5 is
> `Stacks.StalkExact.exact_iff_forall_abelianStalk_exact_of_hasEnoughSitePoints`.

```lean
theorem exact_iff_forall_sheafFiber_exact_of_hasEnoughPoints
    [GrothendieckTopology.HasEnoughPoints.{w} J] (S : ShortComplex (Sheaf J AddCommGrpCat.{w})) :
    S.Exact ↔ ∀ Φ : J.Point.{w}, (S.map (Φ.sheafFiber (A := AddCommGrpCat.{w}))).Exact
```

**`Stacks.StalkExact.exact_iff_forall_abelianStalk_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExactSitePoints.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExactSitePoints.lean#L226). The attribute's comment: “conservative family of points in the sense of Stacks 00Y5”.

> **Stacks 05V3**, for the points of Stacks 00Y5. If `{p_i}_{i ∈ I}` is a conservative family
> of points of the site, a short complex of abelian sheaves is exact if and only if its stalks at
> the points `p_i` are exact.

```lean
theorem exact_iff_forall_abelianStalk_exact {I : Type t} {u : I → C ⥤ Type w}
    (hu : ∀ i, IsSitePoint K (u i)) (hc : IsConservativeFamilyOfSitePoints K u)
    (S : ShortComplex (Sheaf K.toGrothendieck AddCommGrpCat.{w})) :
    S.Exact ↔ ∀ i, (S.map (abelianStalk K (u i))).Exact
```

**`Stacks.StalkExact.exact_iff_forall_abelianStalk_exact_of_hasEnoughSitePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExactSitePoints.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExactSitePoints.lean#L240). The attribute's comment: “enough points, for the points of Stacks 00Y5”.

> **Stacks 05V3**, for the points of Stacks 00Y5. If the site has enough points, a short complex
> of abelian sheaves is exact if and only if its stalks at all points are exact.

```lean
theorem exact_iff_forall_abelianStalk_exact_of_hasEnoughSitePoints (h : HasEnoughSitePoints K)
    (S : ShortComplex (Sheaf K.toGrothendieck AddCommGrpCat.{w})) :
    S.Exact ↔ ∀ u : C ⥤ Type w, IsSitePoint K u → (S.map (abelianStalk K u)).Exact
```

Declarations registered for the tag:

- [`Stacks.StalkExact.exact_iff_forall_sheafFiber_exact`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveGlobalSectionsPerfectStalks.lean#L64), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExactEnoughPoints.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExactEnoughPoints.lean#L37) (StacksFrontier): “conservative family of Mathlib points (`GrothendieckTopology.Point`)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.14, Tag 03D9](https://stacks.math.columbia.edu/tag/03D9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
