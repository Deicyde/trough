---
declaration: section
origin: cited
lean: Stacks.Divisors.IsWeaklyAssociatedPoint, Stacks.Divisors.weaklyAssociatedPoints, Stacks.Divisors.schemeWeaklyAssociatedPoints, AlgebraicGeometry.isWeaklyAssociatedPrime_iff_isWeaklyAssociatedPoint, AlgebraicGeometry.associatedPoints_subset_weaklyAssociatedPoints, AlgebraicGeometry.weaklyAssociatedPoints_subset_supp, AlgebraicGeometry.weaklyAssociatedPoints_subset_of_shortExact, AlgebraicGeometry.weaklyAssociatedPoints_subset_union_of_shortExact
statement: formalized
proof: formalized
---

# 31.5 Weakly associated points

Section 31.5 of the Stacks Project, [Tag 056K](https://stacks.math.columbia.edu/tag/056K). 12 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 056L, a definition

[Tag 056L](https://stacks.math.columbia.edu/tag/056L) in the Stacks Project.

**`Stacks.Divisors.IsWeaklyAssociatedPoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociated.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociated.lean#L87). The attribute's comment: “part (1)”.

> **Stacks 056L, part (1).** A point `x` is *weakly associated* to an `𝒪_X`-module `F` when
> the maximal ideal of the local ring `𝒪_{X, x}` is a weakly associated prime of the stalk
> `F_x`, that is, when it is minimal among the primes containing the annihilator of some element
> of `F_x`.

```lean
abbrev IsWeaklyAssociatedPoint (F : X.Modules) (x : X) : Prop
```

**`Stacks.Divisors.weaklyAssociatedPoints`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociated.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociated.lean#L95). The attribute's comment: “part (2)”.

> **Stacks 056L, part (2).** The set `WeakAss(F)` of points weakly associated to an
> `𝒪_X`-module `F`.

```lean
abbrev weaklyAssociatedPoints (F : X.Modules) : Set X
```

**`Stacks.Divisors.schemeWeaklyAssociatedPoints`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociated.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociated.lean#L107). The attribute's comment: “part (3)”.

> **Stacks 056L, part (3).** The weakly associated points `WeakAss(X)` of a scheme `X` are
> the weakly associated points of its structure sheaf.

```lean
abbrev schemeWeaklyAssociatedPoints (X : Scheme.{u}) : Set X
```

## Tag 056M, a lemma

[Tag 056M](https://stacks.math.columbia.edu/tag/056M) in the Stacks Project.

**`AlgebraicGeometry.isWeaklyAssociatedPrime_iff_isWeaklyAssociatedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/AffineComparison.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/AffineComparison.lean#L246).

> **Stacks Project, Tag 056M.** On an affine open, a point is weakly associated to a
> quasi-coherent sheaf if and only if its corresponding prime ideal is weakly associated to the
> module of sections.

```lean
theorem isWeaklyAssociatedPrime_iff_isWeaklyAssociatedPoint {X : Scheme.{u}} (F : X.Modules)
    [F.IsQuasicoherent] (U : X.Opens) (hU : IsAffineOpen U) (x : X) (hx : x ∈ U) :
    IsWeaklyAssociatedPrime Γ(X, U) Γ(F, U) (hU.primeIdealOf ⟨x, hx⟩).asIdeal ↔
      Stacks.Divisors.IsWeaklyAssociatedPoint F x
```

## Tag 05AM, a lemma

[Tag 05AM](https://stacks.math.columbia.edu/tag/05AM) in the Stacks Project.

**`AlgebraicGeometry.associatedPoints_subset_weaklyAssociatedPoints`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/WeaklyAssociated.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/WeaklyAssociated.lean#L62). The attribute's comment: “associated points”.

> **Stacks Project, Tag 05AM.** Every associated point of a sheaf of modules is weakly
> associated.

```lean
lemma associatedPoints_subset_weaklyAssociatedPoints {X : Scheme.{u}} (F : X.Modules) :
    Stacks.Divisors.associatedPoints F ⊆ Stacks.Divisors.weaklyAssociatedPoints F
```

**`AlgebraicGeometry.weaklyAssociatedPoints_subset_supp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/WeaklyAssociated.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/WeaklyAssociated.lean#L69). The attribute's comment: “weakly associated points”.

> **Stacks Project, Tag 05AM.** Every weakly associated point of a sheaf of modules belongs
> to its support.

```lean
lemma weaklyAssociatedPoints_subset_supp {X : Scheme.{u}} (F : X.Modules) :
    Stacks.Divisors.weaklyAssociatedPoints F ⊆ SheafOfModules.supp F
```

## Tag 05AN, a lemma

[Tag 05AN](https://stacks.math.columbia.edu/tag/05AN) in the Stacks Project.

**`AlgebraicGeometry.weaklyAssociatedPoints_subset_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/WeaklyAssociated.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/WeaklyAssociated.lean#L78). The attribute's comment: “subsheaf\_inclusion”.

> **Stacks Project, Tag 05AN.** In a short exact sequence of quasi-coherent modules on a
> scheme, the weakly associated points of the first module are weakly associated points of the
> middle module.

```lean
theorem weaklyAssociatedPoints_subset_of_shortExact {X : Scheme.{u}}
    (S : ShortComplex X.Modules) [S.X₁.IsQuasicoherent] [S.X₂.IsQuasicoherent]
    [S.X₃.IsQuasicoherent] (hS : S.ShortExact) :
    Stacks.Divisors.weaklyAssociatedPoints S.X₁ ⊆ Stacks.Divisors.weaklyAssociatedPoints S.X₂
```

**`AlgebraicGeometry.weaklyAssociatedPoints_subset_union_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/WeaklyAssociated.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/WeaklyAssociated.lean#L89). The attribute's comment: “middle\_term\_inclusion”.

> **Stacks Project, Tag 05AN.** In a short exact sequence of sheaves of modules, every weakly
> associated point of the middle term is weakly associated to an outer term.

```lean
theorem weaklyAssociatedPoints_subset_union_of_shortExact {X : Scheme.{u}}
    (S : ShortComplex X.Modules) (hS : S.ShortExact) :
    Stacks.Divisors.weaklyAssociatedPoints S.X₂ ⊆
      Stacks.Divisors.weaklyAssociatedPoints S.X₁ ∪
        Stacks.Divisors.weaklyAssociatedPoints S.X₃
```

## Tag 05AP, a lemma

[Tag 05AP](https://stacks.math.columbia.edu/tag/05AP) in the Stacks Project.

**`AlgebraicGeometry.isZero_iff_weaklyAssociatedPoints_eq_empty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Vanishing.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Vanishing.lean#L47).

> A quasi-coherent sheaf of modules is zero if and only if it has no weakly associated points.

```lean
theorem isZero_iff_weaklyAssociatedPoints_eq_empty {X : Scheme.{u}} (F : X.Modules)
    [F.IsQuasicoherent] : IsZero F ↔ Stacks.Divisors.weaklyAssociatedPoints F = ∅
```

## Tag 0B3M, a lemma

[Tag 0B3M](https://stacks.math.columbia.edu/tag/0B3M) in the Stacks Project.

**`AlgebraicGeometry.restriction_injective_of_weaklyAssociatedPoints_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Restriction.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Restriction.lean#L156).

> **Stacks Project, Tag 0B3M.** Restriction of sections of a quasi-coherent module to an open
> containing all its weakly associated points is injective.

```lean
theorem restriction_injective_of_weaklyAssociatedPoints_subset {X : Scheme.{u}} (F : X.Modules)
    [F.IsQuasicoherent] (U : X.Opens)
    (hU : Stacks.Divisors.weaklyAssociatedPoints F ⊆ U) :
    Function.Injective (F.presheaf.map (homOfLE le_top : U ⟶ ⊤).op)
```

## Tag 05AQ, a lemma

[Tag 05AQ](https://stacks.math.columbia.edu/tag/05AQ) in the Stacks Project.

**`AlgebraicGeometry.mem_weaklyAssociatedPoints_of_mem_supp_of_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/MinimalSupport.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/MinimalSupport.lean#L108). The attribute's comment: “minimal point of the support”.

> **Stacks Project, Tag 05AQ.** A point of the support of a quasi-coherent module which is not
> a specialization of another point of the support is weakly associated to the module.

```lean
theorem mem_weaklyAssociatedPoints_of_mem_supp_of_specializes (X : Scheme.{u}) (F : X.Modules)
    [F.IsQuasicoherent] (x : X) (hx : x ∈ SheafOfModules.supp F)
    (hmin : ∀ y : X, y ∈ SheafOfModules.supp F → Specializes y x → y = x) :
    x ∈ Stacks.Divisors.weaklyAssociatedPoints F
```

**`AlgebraicGeometry.mem_weaklyAssociatedPointsOfScheme_of_isGenericPoint_irreducibleComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/MinimalSupport.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/MinimalSupport.lean#L120). The attribute's comment: “generic points of irreducible components”.

> **Stacks Project, Tag 05AQ.** Every generic point of an irreducible component of a scheme is
> weakly associated to its structure sheaf.

```lean
theorem mem_weaklyAssociatedPointsOfScheme_of_isGenericPoint_irreducibleComponent
    (X : Scheme.{u}) {Z : Set X} (hZ : Z ∈ irreducibleComponents X) {x : X}
    (hx : IsGenericPoint x Z) :
    x ∈ Stacks.Divisors.schemeWeaklyAssociatedPoints X
```

## Tag 05AR, a lemma

[Tag 05AR](https://stacks.math.columbia.edu/tag/05AR) in the Stacks Project.

**`AlgebraicGeometry.mem_associatedPoints_iff_mem_weaklyAssociatedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/WeaklyAssociated.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/WeaklyAssociated.lean#L104). The attribute's comment: “finite\_generated\_maximal\_ideal”.

> **Stacks Project, Tag 05AR.** At a point whose local-ring maximal ideal is finitely
> generated, associated and weakly associated membership of a sheaf of modules coincide.

```lean
theorem mem_associatedPoints_iff_mem_weaklyAssociatedPoints {X : Scheme.{u}} (F : X.Modules)
    (x : X) (h : (IsLocalRing.maximalIdeal (X.presheaf.stalk x)).FG) :
    x ∈ Stacks.Divisors.associatedPoints F ↔
      x ∈ Stacks.Divisors.weaklyAssociatedPoints F
```

**`AlgebraicGeometry.associatedPoints_eq_weaklyAssociatedPoints`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/WeaklyAssociated.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/WeaklyAssociated.lean#L120). The attribute's comment: “locally\_noetherian”.

> **Stacks Project, Tag 05AR.** On a locally Noetherian scheme, the associated points and
> weakly associated points of a sheaf of modules coincide.

```lean
lemma associatedPoints_eq_weaklyAssociatedPoints (X : Scheme.{u}) [IsLocallyNoetherian X]
    (F : X.Modules) :
    Stacks.Divisors.associatedPoints F = Stacks.Divisors.weaklyAssociatedPoints F
```

## Tag 0AVN, a lemma

[Tag 0AVN](https://stacks.math.columbia.edu/tag/0AVN) in the Stacks Project.

**`Stacks.AlgebraicGeometry.WeakAssPushforward.not_isWeaklyAssociatedPoint_pushforward_of_not_mem_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/WeakAssPushforward.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/WeakAssPushforward.lean#L282).

> **Stacks Project, Tag 0AVN.** A point outside the image of a quasi-compact,
> quasi-separated morphism is not weakly associated to the pushforward of a quasi-coherent
> module.
>
> Neither quasi-separatedness nor quasi-coherence is used in the proof.

```lean
public theorem not_isWeaklyAssociatedPoint_pushforward_of_not_mem_range
    {X S : Scheme.{u}} (f : X ⟶ S) [QuasiCompact f] [QuasiSeparated f]
    (F : X.Modules) [F.IsQuasicoherent] (s : S) (hs : s ∉ Set.range f) :
    ¬ IsWeaklyAssociatedPoint ((Scheme.Modules.pushforward f).obj F) s
```

## Tag 0AVP, a lemma

[Tag 0AVP](https://stacks.math.columbia.edu/tag/0AVP) in the Stacks Project.

**`AlgebraicGeometry.mono_of_stalk_injective_on_weaklyAssociatedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Mono.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Mono.lean#L69).

> **Stacks Project, Tag 0AVP.** A map of quasi-coherent modules is a monomorphism if its map
> on stalks is injective at every weakly associated point of its source.

```lean
theorem mono_of_stalk_injective_on_weaklyAssociatedPoints {X : Scheme.{u}} {F G : X.Modules}
    [F.IsQuasicoherent] [G.IsQuasicoherent] (f : F ⟶ G)
    (hf : ∀ x : X,
      (Function.Injective
        ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} x).map
          ((PresheafOfModules.toPresheaf X.ringCatSheaf.obj).map f.val)).hom) ∨
        x ∉ Stacks.Divisors.weaklyAssociatedPoints F) :
    Mono f
```

## Tag 0E9I, a lemma

[Tag 0E9I](https://stacks.math.columbia.edu/tag/0E9I) in the Stacks Project.

**`AlgebraicGeometry.isIso_unit_restrict_pushforward_of_depth_ge_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/HartogsExtension/Basic.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/HartogsExtension/Basic.lean#L116). The attribute's comment: “canonical sheaf isomorphism”. References: EGA IV (5.10.6), “sufficiency”.

> **Stacks Project, Tag 0E9I.** A coherent sheaf with depth at least two along the
> complement of an open subscheme is canonically the pushforward of its restriction.

```lean
theorem isIso_unit_restrict_pushforward_of_depth_ge_two
    (X : Scheme.{u}) [IsLocallyNoetherian X] (F : X.Modules) [F.IsCoherent]
    (U : X.Opens)
    (hdepth : ∀ x : X, x ∉ (U : Set X) →
      let M := TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x
      letI : Module (X.presheaf.stalk x) M :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          F.val x
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) M) :
    IsIso ((Scheme.Modules.pullbackPushforwardAdjunction U.ι).unit.app F)
```

**`AlgebraicGeometry.restriction_bijective_of_depth_ge_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/HartogsExtension/Basic.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/HartogsExtension/Basic.lean#L176). The attribute's comment: “global sections”.

> **Stacks Project, Tag 0E9I.** Under the same depth hypothesis, every section on
> the open subscheme extends uniquely to a global section.

```lean
theorem restriction_bijective_of_depth_ge_two
    (X : Scheme.{u}) [IsLocallyNoetherian X] (F : X.Modules) [F.IsCoherent]
    (U : X.Opens)
    (hdepth : ∀ x : X, x ∉ (U : Set X) →
      let M := TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x
      letI : Module (X.presheaf.stalk x) M :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          F.val x
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) M) :
    Function.Bijective
      (F.presheaf.map (homOfLE (show U ≤ (⊤ : X.Opens) from le_top)).op)
```

## Tag 0EME, a lemma

[Tag 0EME](https://stacks.math.columbia.edu/tag/0EME) in the Stacks Project.

**`AlgebraicGeometry.weaklyAssociatedPointsOfScheme_eq_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Reduced.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Reduced.lean#L66).

> **Stacks Project, Tag 0EME.** The weakly associated points of a reduced scheme are exactly
> the generic points of its irreducible components.

```lean
theorem weaklyAssociatedPointsOfScheme_eq_genericPoints (X : Scheme.{u}) [IsReduced X] :
    Stacks.Divisors.schemeWeaklyAssociatedPoints X = genericPoints X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.5, Tag 056K](https://stacks.math.columbia.edu/tag/056K)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
