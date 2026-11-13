---
declaration: section
origin: cited
lean: AlgebraicGeometry.VanishingSituation, AlgebraicGeometry.VanishingSituation.exists_isAdmissibleBlowup_dominating_of_noetherian, AlgebraicGeometry.VanishingSituation.exists_ne_zero_mem_maximalIdeal_factorization, AlgebraicGeometry.VanishingSituation.exists_ne_zero_mem_maximalIdeal_factorization_of_le_topologicalKrullDim_specialFiber, AlgebraicGeometry.VanishingSituation.exists_subset_invertibleCurveDegree_conormalOnComponent_pos, AlgebraicGeometry.VanishingSituation.not_isTrivial_conormalSheaf_of_nonempty, AlgebraicGeometry.VanishingSituation.firstCohomologyRestriction_injective, AlgebraicGeometry.VanishingSituation.hom_residueFieldShift_derivedPushforwardStructureSheaf_eq_zero
statement: formalized
proof: formalized
---

# 54.7 Vanishing

Section 54.7 of the Stacks Project, [Tag 0AX7](https://stacks.math.columbia.edu/tag/0AX7). 8 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AX8, a situation

[Tag 0AX8](https://stacks.math.columbia.edu/tag/0AX8) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/Basic.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/Basic.lean#L49).

> **Stacks Project, Tag 0AX8.** The standing data for the vanishing results: a
> two-dimensional Noetherian normal local domain, a modification of its spectrum, and an
> enumeration of the irreducible components of the special fibre.

```lean
structure VanishingSituation
```

## Tag 0B4M, a lemma

[Tag 0B4M](https://stacks.math.columbia.edu/tag/0B4M) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation.exists_isAdmissibleBlowup_dominating_of_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/StrictTransformOpenImmersion.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/StrictTransformOpenImmersion.lean#L147). The attribute's comment: “the full statement in Situation 0AX8: the inputs 080Y and 081S of 081T are proved, by `cartierBoundaryReduction` and `VanishingSituation.strictTransformOpenImmersion`”.

> **Stacks Project, Tag 0B4M.** In Situation [Stacks, Tag 0AX8] — `A` a Noetherian normal
> local domain of dimension two, `S = Spec(A)`, `U = S ∖ {s}` its punctured spectrum and
> `f : X ⟶ S` a modification — there is a `U`-admissible blowup `b : S' ⟶ S` which dominates `X`:
> it factors as `S' ⟶ X ⟶ S`.
>
> As in the source this is the case of [Stacks, Tag 081T] at `f`. Both results 081T cites are
> proved here for this situation: [Stacks, Tag 080Y] by `AlgebraicGeometry.cartierBoundaryReduction`
> and [Stacks, Tag 081S] by `strictTransformOpenImmersion`. The hypothesis of the source's
> discussion that the special fibre has positive dimension is not needed.

```lean
theorem exists_isAdmissibleBlowup_dominating_of_noetherian (V : VanishingSituation.{u}) :
    ∃ (S' : Scheme.{u}) (b : S' ⟶ V.base),
      Stacks.Blowup.IsAdmissibleBlowup V.puncturedSpectrumOpen b ∧
        ∃ g : S' ⟶ V.X, g ≫ V.f = b
```

## Tag 0AX9, a lemma

[Tag 0AX9](https://stacks.math.columbia.edu/tag/0AX9) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation.exists_ne_zero_mem_maximalIdeal_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ComponentFactorization.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ComponentFactorization.lean#L427). The attribute's comment: “under the standing observation following Situation 0AX8 that every irreducible component of the special fibre has dimension one”.

> A nonzero element of the maximal ideal which, along every irreducible component of the special
> fibre, admits at some closed point of that component and of no other a factorization one factor of
> which lies in the local maximal ideal and restricts to a nonzero function on the component.

```lean
theorem exists_ne_zero_mem_maximalIdeal_factorization
    (V : VanishingSituation.{u})
    (hdim : ∀ i : Fin V.numberOfComponents, topologicalKrullDim (V.component i) = 1) :
    ∃ a : V.A, a ≠ 0 ∧ a ∈ V.maximalIdeal ∧
      ∀ i : Fin V.numberOfComponents,
        ∃ y : componentScheme V i,
          IsClosed
              ({(Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι y} : Set V.X) ∧
          (Scheme.IdealSheafData.vanishingIdeal
              (componentClosed V i)).subschemeι y ∈ componentInSource V i ∧
          (∀ j : Fin V.numberOfComponents, j ≠ i →
            (Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι y ∉ componentInSource V j) ∧
          ∃ g h : V.X.presheaf.stalk
              ((Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι y),
            g ∈ IsLocalRing.maximalIdeal _ ∧
            (Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι.stalkMap y g ≠ 0 ∧
            ((StructureSheaf.toStalk V.A (V.f _) ≫ V.f.stalkMap _) a = g * h)
```

**`AlgebraicGeometry.VanishingSituation.exists_ne_zero_mem_maximalIdeal_factorization_of_le_topologicalKrullDim_specialFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ComponentFactorizationSupplement.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ComponentFactorizationSupplement.lean#L64). The attribute's comment: “the lemma under the standing exclusion of Section 54.7 (Situation 0AX8): the case dim X\_s = 0, discarded by the source, which notes there that f is then finite and hence an isomorphism. The geometric connectedness of the special fibre that the source reads off the Stein factorization is proved here where it is used: a zero-dimensional component is a point open in the special fibre, so Zariski's main theorem over the local base makes the modification an isomorphism and the special fibre a single point, which the exclusion rules out”.

> **Stacks Project, Tag 0AX9.** A nonzero element of the maximal ideal which, along every
> irreducible component of the special fibre, admits at some closed point of that component and of
> no other a factorization one factor of which lies in the local maximal ideal and restricts to a
> nonzero function on the component.
>
> `hfib` is the standing exclusion of Section 54.7 (Situation 0AX8), transcribed. The section states
> it in these words:
>
> > If $X_s$ has dimension $0$, then $f$ is finite and hence an isomorphism. We will discard this
> > uninteresting case.
>
> So `hfib : 1 ≤ topologicalKrullDim V.specialFiber` is that sentence, and every later lemma of the
> section is read under it. It appears as a binder here only because
> `AlgebraicGeometry.VanishingSituation` transcribes Situation 0AX8 itself, which states the
> situation without the section's subsequent exclusion.
>
> Nothing else is carried. The source passes that exclusion from the fibre to each of its
> components through the geometric connectedness of `X_s`, which it has from the Stein
> factorization — More on Morphisms, Lemma 37.53.6, [Stacks, Tag 0AY8], whose second conclusion is
> not available unconditionally in this library (see
> `StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/NormalBase.lean`, where the
> first conclusion `f_*𝒪_X = 𝒪_S` is tagged and the second is given only over [Stacks, Tag 0G7X]).
> That input is not needed: a zero-dimensional component is a point lying on no other component,
> hence open in the special fibre and so a quasi-finite point of `f`, and a modification of the
> spectrum of a normal local domain with such a point in its closed fibre is an isomorphism
> (`AlgebraicGeometry.IsModification.isIso_of_isOpen_singleton_fiber`), whence the special fibre is
> a single point of dimension zero, which `hfib` forbids. So `hfib` alone gives the observation
> following Situation 54.7.1, that every component has dimension one, as
> `AlgebraicGeometry.VanishingSituation.topologicalKrullDim_component_eq_one`.

```lean
theorem exists_ne_zero_mem_maximalIdeal_factorization_of_le_topologicalKrullDim_specialFiber
    (V : VanishingSituation.{u})
    (hfib : 1 ≤ topologicalKrullDim V.specialFiber) :
    ∃ a : V.A, a ≠ 0 ∧ a ∈ V.maximalIdeal ∧
      ∀ i : Fin V.numberOfComponents,
        ∃ y : componentScheme V i,
          IsClosed
              ({(Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι y} : Set V.X) ∧
          (Scheme.IdealSheafData.vanishingIdeal
              (componentClosed V i)).subschemeι y ∈ componentInSource V i ∧
          (∀ j : Fin V.numberOfComponents, j ≠ i →
            (Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι y ∉ componentInSource V j) ∧
          ∃ g h : V.X.presheaf.stalk
              ((Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι y),
            g ∈ IsLocalRing.maximalIdeal _ ∧
            (Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι.stalkMap y g ≠ 0 ∧
            ((StructureSheaf.toStalk V.A (V.f _) ≫ V.f.stalkMap _) a = g * h)
```

## Tag 0AXA, a lemma

[Tag 0AXA](https://stacks.math.columbia.edu/tag/0AXA) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation.exists_subset_invertibleCurveDegree_conormalOnComponent_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ConormalDegreePositive.lean, line 710](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ConormalDegreePositive.lean#L710). The attribute's comment: “the precise clause: in Situation 0AX8 with X normal, for a nonempty effective Cartier divisor Z of X contained set theoretically in the special fibre, there is a component C\_i of the special fibre with C\_i contained in Z and deg(C\_\{Z/X}|\_\{C\_i}) > 0; the dimension-one observation following Situation 0AX8, the section built from Lemma 0AX9 and part (2) of Tag 0B40 are all proved in the library”.

> In Situation [Stacks, Tag 0AX8] let `X` be normal and let `Z ⊆ X` be a nonempty effective
> Cartier divisor contained set theoretically in the special fibre. Then there is a component `C_i`
> of the special fibre with `C_i ⊆ Z` and `deg(𝒞_{Z/X}|_{C_i}) > 0`.
>
> The proof is the source's. Let `a ∈ 𝔪` be the function of [Stacks, Tag 0AX9], with its points
> `x_i ∈ C_i` and factorizations `a = g_i h_i` in `𝒪_{X, x_i}`. The local rings `𝒪_{X, ξ_i}` at the
> generic points are discrete valuation rings; let `e_i` be the valuation of `a` and `d_i` that of
> a local equation of `Z`, and pick `i` with `d_i / e_i` maximal (so `d_i > 0` and `C_i ⊆ Z`).
> Then `a^{d_i}` vanishes at the generic points of `e_i Z`, all of which are generic points of
> components of the special fibre, so it is a global section of `ℐ_{e_i Z}` because `e_i Z` is
> `(S_1)` ([Stacks, Tags 0B3S, 0346, 0B3M]). Its restriction to `C_i` is nonzero, since `a^{d_i}`
> generates `ℐ_{e_i Z}` at `ξ_i`, and vanishes at `x_i` by Krull's principal ideal theorem applied
> to `g_i`; so `deg(𝒞_{e_i Z/X}|_{C_i}) > 0` by part (2) of [Stacks, Tag 0B40], and this degree is
> `e_i · deg(𝒞_{Z/X}|_{C_i})` ([Stacks, Tags 02OP, 0B3P, 0AYX]).

```lean
theorem exists_subset_invertibleCurveDegree_conormalOnComponent_pos [IsNormal V.X]
    (I : V.X.IdealSheafData) [hI : Stacks.Divisors.IsEffectiveCartierDivisor I]
    (hne : I.supportSet.Nonempty)
    (hZs : I.supportSet ⊆ Set.range (V.f.fiberι V.closedPoint)) :
    ∃ i : Fin V.numberOfComponents, componentInSource V i ⊆ I.supportSet ∧
      0 < invertibleCurveDegree (V.base.residueField V.closedPoint)
        (componentToSpecResidueField V i)
        (topologicalKrullDim_componentScheme_le_one_of_isNormal V i)
        (conormalOnComponent V I i)
```

**`AlgebraicGeometry.VanishingSituation.not_isTrivial_conormalSheaf_of_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ConormalDegreePositive.lean, line 762](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ConormalDegreePositive.lean#L762). The attribute's comment: “the first clause: in Situation 0AX8 with X normal, the conormal sheaf of a nonempty effective Cartier divisor Z of X contained set theoretically in the special fibre is not trivial, derived from the precise clause since a trivial conormal sheaf restricts to a sheaf of degree zero on C\_i”.

> In Situation [Stacks, Tag 0AX8] with `X` normal, the conormal sheaf of a nonempty effective
> Cartier divisor `Z ⊆ X` contained set theoretically in the special fibre is not trivial. If it
> were, its restriction to the component `C_i ⊆ Z` provided by
> `exists_subset_invertibleCurveDegree_conormalOnComponent_pos` would be isomorphic to `𝒪_{C_i}`
> and so would have degree zero.

```lean
theorem not_isTrivial_conormalSheaf_of_nonempty [IsNormal V.X] (I : V.X.IdealSheafData)
    [Stacks.Divisors.IsEffectiveCartierDivisor I] (hne : I.supportSet.Nonempty)
    (hZs : I.supportSet ⊆ Set.range (V.f.fiberι V.closedPoint)) :
    ¬ SheafOfModules.IsTrivial I.subscheme.presheaf I.subscheme.ringCatSheaf.2
      (Stacks.Conormal.conormalSheaf I.subschemeι)
```

## Tag 0AXB, a lemma

[Tag 0AXB](https://stacks.math.columbia.edu/tag/0AXB) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation.firstCohomologyRestriction_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/LipDPuncturedRestriction.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/LipDPuncturedRestriction.lean#L478). The attribute's comment: “in Situation 0AX8 with X normal, the restriction map H^1(X, O\_X) -> H^1(f^\{-1}(U), O\_X) is injective; the source's Nagata hypothesis on A is not needed”.

> **[Stacks, Tag 0AXB].** In Situation 0AX8 with `X` normal, the restriction map
> `H¹(X, 𝒪_X) ⟶ H¹(f⁻¹(U), 𝒪_X)` on the first cohomology of the structure sheaf is injective.
>
> The source assumes `A` Nagata as well; the argument below does not use it. A class in the
> kernel is represented, through an injective resolution `I` of `𝒪_X`, by a cocycle `c ∈ Γ(X, I¹)`
> which has primitives on `f⁻¹(U)` and on the members of an open cover of `X` (locality of
> cohomology, [Stacks, Tag 01E3]); `exists_d_eq_of_local_primitives` glues them, using the polar
> lemma in place of the projective-bundle construction of the source's proof.

```lean
theorem firstCohomologyRestriction_injective [IsNormal V.X] :
    Function.Injective V.firstCohomologyRestriction
```

## Tag 0AXC, a lemma

[Tag 0AXC](https://stacks.math.columbia.edu/tag/0AXC) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation.hom_residueFieldShift_derivedPushforwardStructureSheaf_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/DerivedPushforwardAffineIdentification.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/DerivedPushforwardAffineIdentification.lean#L129). The attribute's comment: “the vanishing of Hom\_\{D(A)}(kappa[-1], Rf\_*O\_X) with Rf\_*O\_X the ACTUAL derived direct image: the restricted unbounded derived direct image quasiCoherentDerivedPushforward applied to the structure sheaf of X in degree zero, an object of D\_QCoh(O\_S), carried into D(A) by the inverse of the derived sheafification equivalence of Tag 06Z0 (DualizingDivisor.tildeEquivalence, the affine identification D(A) = D\_QCoh(O\_S) that the tag invokes). The vanishing is the base carrier hom\_residueFieldShift\_derivedGlobalSections\_eq\_zero transported along Leray over the base ring (Tag 0D5W, DualizingDivisor.lerayIso), which identifies that object with the A-linear derived global sections RGamma(X, O\_X). Stated for X normal without the Nagata hypothesis on A, which enters the source's proof only through Tag 0AXB and is not needed on the route taken here”.

> In Situation [Stacks, Tag 0AX8] with `X` normal, the group
> `Hom_{D(A)}(κ[-1], Rf_*𝒪_X)` is zero: every morphism from `κ[-1]` to the derived direct image of
> the structure sheaf, read in `D(A)` through the affine identification `D(A) = D_QCoh(𝒪_S)` of
> [Stacks, Tag 06Z0], vanishes.
>
> Leray over the base ring identifies that object with `RΓ(X, 𝒪_X)`, so this is
> `hom_residueFieldShift_derivedGlobalSections_eq_zero` transported along
> `derivedGlobalSectionsStructureSheafIsoPushforward`. The source also assumes `A` Nagata; that
> hypothesis is not needed, since it enters the source's proof only through
> [Stacks, Tag 0AXB].

```lean
theorem hom_residueFieldShift_derivedPushforwardStructureSheaf_eq_zero [IsNormal V.X]
    (α : V.residueFieldShift ⟶ V.derivedPushforwardStructureSheaf) : α = 0
```

**`AlgebraicGeometry.VanishingSituation.hom_residueFieldShift_derivedGlobalSections_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/DerivedPushforwardStructureSheaf.lean, line 575](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/DerivedPushforwardStructureSheaf.lean#L575). The attribute's comment: “the vanishing of Hom\_\{D(A)}(kappa[-1], Rf\_*O\_X), the pushforward being the derived global sections RGamma(X, O\_X), which isDerivedPushforwardStructureSheaf\_derivedGlobalSectionsStructureSheaf identifies with Rf\_*O\_X by its cohomology H^n(X, O\_X); stated for X normal without the Nagata hypothesis on A, which is not needed. For a nonzero a in the maximal ideal the triangle of 0 -> O\_X -> O\_X -> O\_X/aO\_X -> 0 has first morphism a times the identity, so a morphism out of kappa[-1] factors through RGamma(X, O\_X/aO\_X); in degree zero that is a global section of O\_X/aO\_X annihilated by the maximal ideal, hence supported in the special fibre, hence zero by eq\_zero\_of\_res\_preimagePuncturedSpectrum\_eq\_zero (Lipman's argument from Tag 0AX9, used in place of Tag 0AXB), and Hom\_A(m, A) = A over a Noetherian normal local domain of dimension at least two kills the morphism”.

> **Stacks Project, Tag 0AXC.** In Situation [Stacks, Tag 0AX8] with `X` normal, every
> morphism `κ[-1] ⟶ RΓ(X, 𝒪_X)` in `D(A)` is zero; that is, the group `Hom_{D(A)}(κ[-1], Rf_*𝒪_X)`
> vanishes, the pushforward being read as the derived global sections `RΓ(X, 𝒪_X)`, which
> `isDerivedPushforwardStructureSheaf_derivedGlobalSectionsStructureSheaf` identifies with
> `Rf_*𝒪_X` by its cohomology. The source also assumes `A` Nagata; that is not needed here.
>
> For a nonzero `a ∈ 𝔪` the triangle of `0 → 𝒪_X → 𝒪_X → 𝒪_X/a𝒪_X → 0` has `a • 𝟙` as its first
> morphism, so `α` factors through `RΓ(X, 𝒪_X/a𝒪_X)`. In degree zero the factorisation is a global
> section of `𝒪_X/a𝒪_X` annihilated by `𝔪`. Such a section dies over the punctured spectrum, so it
> is zero by `eq_zero_of_res_preimagePuncturedSpectrum_eq_zero`, and in particular it is the image
> of a global function of `X`. Two consecutive morphisms of the triangle then kill the restriction
> of `α` along `A[-1] ⟶ κ[-1]`, and `Hom_A(𝔪, A) = A` kills `α`.
>
> The source reaches the same lift through [Stacks, Tag 0AXB], whose proof needs the Nagata
> condition to make a normalization finite. Here it comes from the vanishing of sections of
> `𝒪_X/a𝒪_X` supported in the special fibre, which is proved directly by Lipman's argument from
> [Stacks, Tag 0AX9], algebraic Hartogs and the fact that a proper integral curve has no nonconstant
> functions.

```lean
theorem hom_residueFieldShift_derivedGlobalSections_eq_zero (V : VanishingSituation.{u})
    [IsNormal V.X]
    (α : V.residueFieldShift ⟶ derivedGlobalSectionsStructureSheaf V.f) : α = 0
```

## Tag 0B4R, a remark

[Tag 0B4R](https://stacks.math.columbia.edu/tag/0B4R) in the Stacks Project.

**`Stacks.Duality.IsDualizingModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModule.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModule.lean#L52). The attribute's comment: “dualizing\_module\_terminology”.

> A sheaf of modules on a locally Noetherian scheme is a **dualizing module** when it is
> coherent and becomes a dualizing complex once placed in some cohomological degree.

```lean
abbrev IsDualizingModule {X : Scheme.{u}} [IsLocallyNoetherian X] (ω : X.Modules) : Prop
```

**`Stacks.Duality.IsDualizingRingModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModule.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModule.lean#L59). The attribute's comment: “dualizing\_module\_terminology”.

> A module over a Noetherian ring is a **dualizing module** when it is finite and becomes a
> dualizing complex once placed in some cohomological degree.

```lean
abbrev IsDualizingRingModule (A : Type u) [CommRing A] [IsNoetherianRing A] (M : Type v)
    [AddCommGroup M] [Module A M] : Prop
```

**`Stacks.Duality.exists_isDualizingComplex_iff_exists_isDualizingModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleExistence.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleExistence.lean#L64). The attribute's comment: “the equivalence of (1) and (2)”.

> **Stacks Project, Remark 0B4R, the equivalence of (1) and (2).** An integral Noetherian
> normal scheme of dimension at most two carries a dualizing complex if and only if it carries a
> dualizing module, that is a coherent module which is a dualizing complex in some degree.

```lean
public theorem exists_isDualizingComplex_iff_exists_isDualizingModule (X : Scheme.{u})
    [IsIntegral X] [IsNoetherian X] [IsNormal X] (hX : topologicalKrullDim X ≤ 2) :
    (∃ K : DerivedCategory X.Modules, IsDualizingComplex K) ↔
      ∃ ω : X.Modules, IsDualizingModule ω
```

**`Stacks.Duality.isDualizingModule_iff_forall_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleNormalModification.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleNormalModification.lean#L90). The attribute's comment: “in (2), the integer n can be any integer”.

> **Stacks Project, Remark 0B4R, "where `n` can be any integer".** A sheaf of modules is a
> dualizing module if and only if it is coherent and is a dualizing complex placed in *every*
> cohomological degree: placing it in degree `n` is a shift of placing it in degree `m`.

```lean
theorem isDualizingModule_iff_forall_isDualizingComplex {X : Scheme.{u}} [IsLocallyNoetherian X]
    (ω : X.Modules) :
    IsDualizingModule ω ↔ ω.IsCoherent ∧
      ∀ n : ℤ, IsDualizingComplex ((DerivedCategory.singleFunctor X.Modules n).obj ω)
```

**`Stacks.Duality.isDualizingRingModule_iff_forall_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleNormalModification.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleNormalModification.lean#L120). The attribute's comment: “in (2) over a Noetherian ring, the integer n can be any integer”.

> **Stacks Project, Remark 0B4R, "where `n` can be any integer", over a ring.** A module over a
> Noetherian ring is a dualizing module if and only if it is finite and is a dualizing complex
> placed in every cohomological degree.

```lean
theorem isDualizingRingModule_iff_forall_isDualizingComplex (A : Type u) [CommRing A]
    [IsNoetherianRing A] (M : Type v) [AddCommGroup M] [Module A M] :
    IsDualizingRingModule A M ↔ Module.Finite A M ∧
      ∀ n : ℤ, Dualizing.IsDualizingComplex (A := A)
        ((DerivedCategory.singleFunctor (ModuleCat.{v} A) n).obj (ModuleCat.of A M))
```

**`Stacks.Duality.exists_isDualizingComplex_iff_exists_isDualizingRingModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleNormalModification.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleNormalModification.lean#L136). The attribute's comment: “the equivalence of (1) and (2) for a Noetherian normal local domain of dimension 2”.

> **Stacks Project, Remark 0B4R, for a Noetherian normal local domain of dimension two.** Such
> a ring `A` has a dualizing complex if and only if it has a dualizing module, with complexes and
> modules in any universe `max u v` containing `A`. It is Cohen–Macaulay, being normal of dimension
> two, so by [Stacks, Tag 0AWS] a dualizing complex has its cohomology in a single degree and is
> that cohomology module placed there.

```lean
theorem exists_isDualizingComplex_iff_exists_isDualizingRingModule (A : Type u) [CommRing A]
    [IsLocalRing A] [IsNoetherianRing A] [IsNormalDomain A] (hA : ringKrullDim A = 2) :
    (∃ K : DerivedCategory (ModuleCat.{max u v} A), Dualizing.IsDualizingComplex K) ↔
      ∃ (M : Type (max u v)) (_ : AddCommGroup M) (_ : Module A M),
        IsDualizingRingModule A M
```

**`Stacks.Duality.exists_isDualizingModule_of_isModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleNormalModification.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleNormalModification.lean#L268). The attribute's comment: “if A has a dualizing module, so does every normal modification X of Spec(A)”.

> **Stacks Project, Remark 0B4R: a normal modification inherits a dualizing module.** Let `A`
> be a Noetherian normal local domain of dimension two which has a dualizing module, that is,
> `Spec(A)` has one, and let `f : X ⟶ Spec(A)` be a modification with `X` normal. Then `X` has a
> dualizing module: by [Stacks, Tag 0AWI] the twisted inverse image of the normalized dualizing
> complex of `Spec(A)` is a dualizing complex on `X`, and its cohomology in degree `-2` is a
> dualizing module.

```lean
theorem exists_isDualizingModule_of_isModification (hA2 : ringKrullDim A = 2)
    (hA : ∃ ωA : (Spec (.of A)).Modules, IsDualizingModule ωA)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) (hf : IsModification f) [IsNormal X] :
    haveI : IsProper f := hf.isProper
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    ∃ ωX : X.Modules, IsDualizingModule ωX
```

**`Stacks.Duality.exists_normalized_isDualizingModule_of_isModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleNormalModification.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleNormalModification.lean#L363). The attribute's comment: “for every dualizing module omega\_A of Spec(A), omega\_A[2] is normalized and the dualizing module omega\_X of X normalized relative to omega\_A exists: f^!(omega\_A) = omega\_X in degree zero”.

> **Stacks Project, Remark 0B4R: the dualizing module of `X` normalized relative to `ω_A`.**
> Let `A` be a Noetherian normal local domain of dimension two, `ω_A` a dualizing module of
> `Spec(A)`, and `f : X ⟶ Spec(A)` a modification with `X` normal. Then
>
> * `ω_A[2]` is the normalized dualizing complex of `Spec(A)`: it is modelled on `Spec(A)` by a
>   normalized dualizing complex over `Γ(Spec(A), ⊤)`, and
> * there is a dualizing module `ω_X` of `X` with `f^!(ω_A[0]) ≅ ω_X[0]`.
>
> As `f^!` commutes with shifts, the last isomorphism says that `ω_X[2]` is the dualizing complex
> of `X` normalized relative to `ω_A[2]`, which is the convention fixed by the remark
> ([Stacks, Section 0AU5]). The statement is for every dualizing module `ω_A` of `Spec(A)`.

```lean
theorem exists_normalized_isDualizingModule_of_isModification (hA2 : ringKrullDim A = 2)
    (ωA : (Spec (.of A)).Modules) (hωA : IsDualizingModule ωA)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) (hf : IsModification f) [IsNormal X] :
    haveI : IsProper f := hf.isProper
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    letI := isNoetherianRing_globalSections_spec A
    letI := isLocalRing_globalSections_spec A
    haveI : ωA.IsCoherent := hωA.1
    (∃ ω : DerivedCategory (ModuleCat.{u} Γ(Spec (.of A), ⊤)),
      Dualizing.IsNormalizedDualizingComplex.{u, u} ω ∧
        IsTildeModelOnAnyModel ((DerivedCategory.singleFunctor _ (-2)).obj ωA) ⊤
          (isAffineOpen_top _) ω) ∧
    ∃ ωX : X.Modules, IsDualizingModule ωX ∧
      Nonempty (((twistedInverseImage f
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
        (singleQuasiCoherent ωA (isQuasicoherent_of_isCoherent ωA) 0)).obj ≅
          (DerivedCategory.singleFunctor X.Modules 0).obj ωX)
```

## Tag 0AXD, a proposition

[Tag 0AXD](https://stacks.math.columbia.edu/tag/0AXD) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation.isZero_firstCohomology_of_properRightAdjoint_isoShiftTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/GrauertRiemenschneiderUnconditional.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/GrauertRiemenschneiderUnconditional.lean#L478). The attribute's comment: “the conclusion R^1 f\_* omega\_X = 0 read over the affine base S = Spec(A) as the vanishing of H^1(X, omega\_X) as an A-module, for every normalized dualizing complex omega\_A^bullet over A and every O\_X-module omega\_X with f^times(omega\_A^bullet-tilde) = omega\_X[2], which is the dualizing module of Remark 0B4R normalized with respect to omega\_A^bullet; the hypotheses are the Proposition's own: the Situation of Tag 0AX8, X normal, A Nagata, and the dualizing complex omega\_A^bullet, taken normalized as the source does (Tag 0A7M). The source's proof is carried out in full: omega\_X^bullet = omega\_X[2] (Tags 0B3D, 0AWT, 0AWI), a nonzero R^1 f\_* omega\_X -> kappa gives a nonzero alpha : Rf\_* omega\_X^bullet -> kappa[1], and RHom\_A(-, omega\_A^bullet) carries it to a nonzero beta : kappa[-1] -> Rf\_* O\_X (Tags 0A7M, 0GEW, 0AA3), contradicting Tag 0AXC”.

> **Stacks Project, Tag 0AXD** (Grauert-Riemenschneider), for every normalized `ω_A^•` and
> every `ω_X` normalized with respect to it. Let `(A, 𝔪, κ)` be a two-dimensional Noetherian
> normal local domain, `f : X ⟶ S = Spec(A)` a modification with `X` normal, and suppose `A` is
> Nagata. Let `ω_A^•` be a normalized dualizing complex over `A`, and let `ω_X` be an
> `𝒪_X`-module with `f^×(ω̃_A^•) ≅ ω_X[2]` — the dualizing module of [Stacks, Remark 0B4R],
> normalized with respect to `ω_A^•`. Then `H¹(X, ω_X) = 0`, which over the affine base `S` is
> `R¹f_*ω_X = 0`.
>
> The source's hypothesis that `A` has a dualizing complex is carried by `ω_A^•` itself, which the
> source may and does take normalized ([Stacks, Tag 0A7M]). That `ω_X` is coherent and a dualizing
> module is not assumed: the isomorphism `f^×(ω̃_A^•) ≅ ω_X[2]` determines `ω_X` up to isomorphism,
> and `AlgebraicGeometry.VanishingSituation.exists_isDualizingModule_properRightAdjoint_isoShiftTwo`
> supplies a coherent such module, which is a dualizing module because `f^×` preserves dualizing
> complexes ([Stacks, Tag 0AA3]).
>
> The vanishing for that module is the source's argument,
> `AlgebraicGeometry.VanishingSituation.isZero_firstCohomology_dualizingModule_of_isTildeDualizing`;
> it passes to `ω_X` along the isomorphism `ω_X ≅ H⁰(ω_X[2][-2])` of the two modules.

```lean
theorem isZero_firstCohomology_of_properRightAdjoint_isoShiftTwo (V : VanishingSituation.{u})
    [IsNormal V.X]
    (hnag : IsNagataRing V.A)
    (ωA : DerivedCategory (ModuleCat.{u} V.A))
    (hωA : Dualizing.IsNormalizedDualizingComplex.{u, u} ωA) (ωX : V.X.Modules) :
    letI : IsProper V.f := V.modification.isProper
    letI : CompactSpace V.X := QuasiCompact.compactSpace_of_compactSpace V.f
    letI : QuasiSeparatedSpace V.X := quasiSeparatedSpace_of_quasiSeparated V.f
    Nonempty (((properRightAdjoint V.f).obj
          ((derivedTilde (CommRingCat.of V.A)).obj ωA)).obj ≅
        ((DerivedCategory.singleFunctor V.X.Modules 0).obj ωX)⟦(2 : ℤ)⟧) →
      IsZero (firstCohomologySheafAsBaseModule V.X V.f ωX)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.7, Tag 0AX7](https://stacks.math.columbia.edu/tag/0AX7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
