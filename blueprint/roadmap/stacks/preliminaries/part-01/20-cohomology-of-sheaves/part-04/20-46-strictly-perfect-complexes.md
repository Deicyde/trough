---
declaration: section
origin: cited
lean: StrictlyPerfect.IsStrictlyPerfect, StrictlyPerfect.isStrictlyPerfect_mappingCone, strictlyPerfect_tensorObj, Stacks.StrictlyPerfect.Pullback.isStrictlyPerfect_modulePullback, StrictlyPerfect.exists_over_lift_of_isDirectSummandOfFiniteFree, StrictlyPerfect.exists_local_lift_of_isDirectSummandOfFiniteFree, AlgebraicGeometry.RingedSpace.exists_local_lift_of_isDirectSummandOfFiniteFree, StrictlyPerfect.LocalLifting.exists_local_lift
statement: formalized
proof: formalized
---

# 20.46 Strictly perfect complexes

Section 20.46 of the Stacks Project, [Tag 08C3](https://stacks.math.columbia.edu/tag/08C3). 11 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08C4, a definition

[Tag 08C4](https://stacks.math.columbia.edu/tag/08C4) in the Stacks Project.

Declarations registered for the tag:

- [`StrictlyPerfect.IsStrictlyPerfect`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfect/FiniteFreeSummands.lean#L298), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfect/Defs.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfect/Defs.lean#L42) (StacksFrontier).

## Tag 08C5, a lemma

[Tag 08C5](https://stacks.math.columbia.edu/tag/08C5) in the Stacks Project.

**`StrictlyPerfect.isStrictlyPerfect_mappingCone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfect/FiniteFreeSummands.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfect/FiniteFreeSummands.lean#L311).

> The cone on a morphism of strictly perfect complexes is strictly perfect.
>
> The cone `C(f)` is `CochainComplex.mappingCone f`, whose `n`-th term is `L^n ⊕ K^{n+1}`. The
> hypothesis `HasHomotopyCofiber f` is the (automatically satisfied, since the category has
> binary biproducts) condition ensuring the mapping cone exists.

```lean
theorem isStrictlyPerfect_mappingCone {K L : CochainComplex (OXMod.{u, w} X) ℤ}
    (f : K ⟶ L) [HomologicalComplex.HasHomotopyCofiber f]
    (hK : IsStrictlyPerfect K) (hL : IsStrictlyPerfect L) :
    IsStrictlyPerfect (CochainComplex.mappingCone f)
```

## Tag 09J2, a lemma

[Tag 09J2](https://stacks.math.columbia.edu/tag/09J2) in the Stacks Project.

**`strictlyPerfect_tensorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfect/TensorOfFiniteFreeSummands.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfect/TensorOfFiniteFreeSummands.lean#L250).

> **Stacks Tag 09J2 (Lemma 20.46.3).** If `E` and `F` are strictly perfect complexes, then the
> total complex `HomologicalComplex.tensorObj E F` of their tensor product, whose degree `n` term is
> `⨁_{p+q=n} E^p ⊗ F^q` with the Koszul-sign differential, is strictly perfect.
>
> The hypothesis `[E.HasTensor F]` asserts that the total complex exists; for bounded complexes
> (such as strictly perfect ones) it is automatically satisfied since each total degree only
> involves finitely many summands.

```lean
theorem strictlyPerfect_tensorObj
    (E F : CochainComplex C ℤ) [E.HasTensor F]
    (hE : StrictlyPerfect E) (hF : StrictlyPerfect F) :
    StrictlyPerfect (HomologicalComplex.tensorObj E F)
```

## Tag 09U6, a lemma

[Tag 09U6](https://stacks.math.columbia.edu/tag/09U6) in the Stacks Project.

**`Stacks.StrictlyPerfect.Pullback.isStrictlyPerfect_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfectRestriction/PullbackOnRingedSpaces.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfectRestriction/PullbackOnRingedSpaces.lean#L142). The attribute's comment: “for every morphism of ringed spaces f : X ⟶ Y (rings and sections in one universe), the termwise pullback f^* of a strictly perfect complex of O\_Y-modules is strictly perfect”.

> **Stacks 09U6 (Lemma 20.46.4).** The termwise pullback of a strictly perfect complex of
> `𝒪_Y`-modules along a morphism of ringed spaces `f : X ⟶ Y` is a strictly perfect complex of
> `𝒪_X`-modules.
>
> Boundedness is preserved because `f^*` preserves zero morphisms and so carries a zero object to a
> zero object, hence cannot create a nonzero term; the termwise condition is
> `Stacks.StrictlyPerfect.Pullback.isDirectSummandOfFiniteFree_modulePullback`.
>
> This is the full lemma: `f` is an arbitrary morphism of ringed spaces, `f^*` is the pullback of
> sheaves of modules (`f^{-1}G ⊗_{f^{-1}O_Y} O_X`), and strictly perfect is Definition 20.46.1
> (tag 08C4): finitely many nonzero terms, each a direct summand of a finite free module.

```lean
theorem isStrictlyPerfect_modulePullback (K : CochainComplex (OXMod.{u} Y) ℤ)
    (hK : IsStrictlyPerfect K) :
    IsStrictlyPerfect
      (((modulePullback f).mapHomologicalComplex (ComplexShape.up ℤ)).obj K)
```

## Tag 08C6, a lemma

[Tag 08C6](https://stacks.math.columbia.edu/tag/08C6) in the Stacks Project.

**`StrictlyPerfect.exists_over_lift_of_isDirectSummandOfFiniteFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/StrictlyPerfectLiftModuleUniverse.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/StrictlyPerfectLiftModuleUniverse.lean#L265). The attribute's comment: “at an arbitrary module universe”.

> **Stacks 08C6.** Let `X` be a ringed space, `p : 𝒢 ⟶ ℱ` an epimorphism of `𝒪_X`-modules and
> `f : ℰ ⟶ ℱ` a morphism out of a direct summand of a finite free `𝒪_X`-module. Then every point
> of `X` has an open neighbourhood `U` and a morphism `l : ℰ|_U ⟶ 𝒢|_U` with `l ≫ p|_U = f|_U`.
>
> The ring universe, the space universe and the module universe are independent; the price is the
> two sheafification hypotheses, which are what make `Mod(𝒪_X)` abelian and are Stacks' standing
> convention. See the module docstring for how the module universe is freed and for the two other
> carriers of this tag.

```lean
theorem exists_over_lift_of_isDirectSummandOfFiniteFree {E F G : OXMod.{u, w} X} (f : E ⟶ F)
    (p : G ⟶ F) [Epi p] (hE : IsDirectSummandOfFiniteFree E) :
    ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      ∃ l : E.over U ⟶ G.over U, l ≫ p.over U = f.over U
```

**`StrictlyPerfect.exists_local_lift_of_isDirectSummandOfFiniteFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/StrictlyPerfectRestriction.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/StrictlyPerfectRestriction.lean#L269). The attribute's comment: “module universe = ring universe, space universe free, stated through `restrictModules`. Strictly more general than the collapsed form in `StacksFrontier/AlgebraicGeometry/PseudoCoherent/StrictlyPerfectLift.lean`, strictly less than the arbitrary-module-universe form in `StrictlyPerfectLiftModuleUniverse.lean`.”.

> Given `α : E ⟶ F` and an epimorphism `p : G ⟶ F` of `O_X`-modules with `E` a direct summand of
> a finite free `O_X`-module, a factorisation of `α` through `p` exists locally on `X`: every point
> has an open neighbourhood `U` and a morphism `β : E|_U ⟶ G|_U` with `β ≫ p|_U = α|_U`.

```lean
theorem exists_local_lift_of_isDirectSummandOfFiniteFree {E F G : OXMod.{r, r} X}
    (hE : IsDirectSummandOfFiniteFree E) (α : E ⟶ F) (p : G ⟶ F) [Epi p] (x : X.carrier) :
    ∃ U : Opens X.carrier, x ∈ U ∧
      ∃ β : (restrictModules X U).obj E ⟶ (restrictModules X U).obj G,
        β ≫ (restrictModules X U).map p = (restrictModules X U).map α
```

**`AlgebraicGeometry.RingedSpace.exists_local_lift_of_isDirectSummandOfFiniteFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/StrictlyPerfectLift.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/StrictlyPerfectLift.lean#L217). The attribute's comment: “all three universes collapsed (space = ring = module), stated through `restrictModules`. The module-universe-free form is in `StacksFrontier/Algebra/Homology/StrictlyPerfectLiftModuleUniverse.lean`; neither subsumes the other.”.

> **Stacks 08C6.** Let `X` be a ringed space, let `p : 𝒢 ⟶ ℱ` be an epimorphism of
> `𝒪_X`-modules and let `f : ℰ ⟶ ℱ` be a map out of a direct summand of a finite free
> `𝒪_X`-module. Then every point of `X` has an open neighbourhood over which `f` factors
> through `p`.
>
> Writing `ℰ` as a retract `(i, r)` of `𝒪_X^{⊕ n}`, it is enough to lift `r ≫ f` and compose
> the lift with `i`, since `i ≫ r = 𝟙`.

```lean
theorem exists_local_lift_of_isDirectSummandOfFiniteFree
    {E F G : StrictlyPerfect.OXMod.{u, u, u} X} (f : E ⟶ F) (p : G ⟶ F) [Epi p]
    (hE : StrictlyPerfect.IsDirectSummandOfFiniteFree E) :
    ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      ∃ l : (restrictModules X U).obj E ⟶ (restrictModules X U).obj G,
        l ≫ (restrictModules X U).map p = (restrictModules X U).map f
```

**`StrictlyPerfect.LocalLifting.exists_local_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfect/LocalLiftingOfMaps.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfect/LocalLiftingOfMaps.lean#L141).

> A map from a direct summand of a finite free module lifts locally through
> any epimorphism of sheaves of modules.

```lean
theorem exists_local_lift [Epi p] (hE : IsDirectSummandOfFiniteFree E) :
    ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      ∃ l : E.over U ⟶ G.over U, l ≫ p.over U = f.over U
```

## Tag 08C7, a lemma

[Tag 08C7](https://stacks.math.columbia.edu/tag/08C7) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.exists_local_homotopy_zero_of_isZero_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfectRestriction/LocalNullHomotopyOverSlices.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfectRestriction/LocalNullHomotopyOverSlices.lean#L82). The attribute's comment: “part (2)”. References: SGA 6 I (4.1), “ringed space”.

> A map from a strictly perfect complex concentrated in degrees at least
> `a` is locally null-homotopic if the target's cohomology vanishes in those
> degrees.
>
> This is the ringed-space-facing name for
> `Stacks.Cohomology.LocalNullHomotopy.exists_local_homotopy_zero_of_isZero_homology`, which
> carries the proof.

```lean
theorem exists_local_homotopy_zero_of_isZero_homology (a : ℤ)
    (hE : StrictlyPerfect.IsStrictlyPerfect E) (hE₀ : ∀ i : ℤ, i < a → IsZero (E.X i))
    (hF : ∀ i : ℤ, a ≤ i → IsZero (F.homology i)) :
    ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      Nonempty (Homotopy
        (((SheafOfModules.overFunctor (structureSheafOfRings X) U).mapHomologicalComplex
          (ComplexShape.up ℤ)).map α) 0)
```

**`AlgebraicGeometry.RingedSpace.exists_local_homotopy_zero_of_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfectRestriction/LocalNullHomotopyOverSlices.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfectRestriction/LocalNullHomotopyOverSlices.lean#L99). The attribute's comment: “part (1)”. References: SGA 6 I (4.1), “ringed space”.

> A map from a strictly perfect complex to an acyclic complex is locally
> null-homotopic.
>
> This is the ringed-space-facing name for
> `Stacks.Cohomology.LocalNullHomotopy.exists_local_homotopy_zero_of_acyclic`, which carries the
> proof.

```lean
theorem exists_local_homotopy_zero_of_acyclic
    (hE : StrictlyPerfect.IsStrictlyPerfect E) (hF : F.Acyclic) :
    ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      Nonempty (Homotopy
        (((SheafOfModules.overFunctor (structureSheafOfRings X) U).mapHomologicalComplex
          (ComplexShape.up ℤ)).map α) 0)
```

## Tag 08C8, a lemma

[Tag 08C8](https://stacks.math.columbia.edu/tag/08C8) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.exists_local_lift_homotopy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/StrictlyPerfectCone.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/StrictlyPerfectCone.lean#L150). References: SGA 6 I (4.2), “ringed space case”.

> **Stacks 08C8.** Let `X` be a ringed space, let `α : ℰ ⟶ ℱ` be a morphism of complexes of
> `𝒪_X`-modules with `ℰ` strictly perfect and `ℰ^j = 0` for `j < a`, and let `f : 𝒢 ⟶ ℱ` be a
> morphism of complexes of `𝒪_X`-modules which is an isomorphism on cohomology in every degree
> above `a` and an epimorphism on cohomology in degree `a`. Then every point of `X` has an open
> neighbourhood `U` carrying a morphism `β : ℰ|_U ⟶ 𝒢|_U` with `β ≫ f|_U` homotopic to `α|_U`.
>
> The mapping cone `C(f)` has vanishing cohomology in degrees at least `a`
> (`AlgebraicGeometry.RingedSpace.isZero_homology_mappingCone`), so Stacks 08C7 makes the
> composite `α ≫ inr f` null-homotopic over some open neighbourhood `U` of the given point. Hence
> `α|_U` composed with the second map of the distinguished triangle `𝒢|_U ⟶ ℱ|_U ⟶ C(f|_U)` is
> zero in the homotopy category over `U`, and `Triangle.coyoneda_exact₂` factors it through
> `f|_U`; any representative `β` of that factorization satisfies the conclusion.

```lean
public theorem exists_local_lift_homotopy
    {E F G : CochainComplex (OXMod.{u, u} X) ℤ} (α : E ⟶ F) (f : G ⟶ F) (a : ℤ)
    (hE : IsStrictlyPerfect E) (hEa : ∀ j : ℤ, j < a → IsZero (E.X j))
    (hf_gt : ∀ j : ℤ, a < j → IsIso (HomologicalComplex.homologyMap f j))
    (hf_a : Epi (HomologicalComplex.homologyMap f a)) :
    ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      ∃ β : ((overFunctor (structureSheafOfRings X) U).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj E ⟶
          ((overFunctor (structureSheafOfRings X) U).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj G,
        Nonempty (Homotopy
          (β ≫ ((overFunctor (structureSheafOfRings X) U).mapHomologicalComplex
            (ComplexShape.up ℤ)).map f)
          (((overFunctor (structureSheafOfRings X) U).mapHomologicalComplex
            (ComplexShape.up ℤ)).map α))
```

**`Stacks.PseudoCoherence.DerivedCharacterization.exists_local_lift_homotopy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/Defs.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/Defs.lean#L138). References: SGA 6 I (4.2), “ringed space case”; SGA 6 I (4.1), “special case”.

> A map from a strictly perfect complex lifts locally up to homotopy through a map that is
> cohomologically an isomorphism above the lower bound and surjective at the lower bound.

```lean
theorem exists_local_lift_homotopy (α : E ⟶ F) (f : G ⟶ F) (a : ℤ)
    (hE : IsStrictlyPerfect E) (hEa : ∀ j : ℤ, j < a → IsZero (E.X j))
    (hf_gt : ∀ j : ℤ, a < j → IsIso (HomologicalComplex.homologyMap f j))
    (hf_a : Epi (HomologicalComplex.homologyMap f a)) :
    ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      ∃ β : ((overFunctor.{u} (structureSheafOfRings X) U).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj E ⟶
          ((overFunctor.{u} (structureSheafOfRings X) U).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj G,
        Nonempty (Homotopy
          (β ≫ ((overFunctor.{u} (structureSheafOfRings X) U).mapHomologicalComplex
            (ComplexShape.up ℤ)).map f)
          (((overFunctor.{u} (structureSheafOfRings X) U).mapHomologicalComplex
            (ComplexShape.up ℤ)).map α))
```

## Tag 08C9, a lemma

[Tag 08C9](https://stacks.math.columbia.edu/tag/08C9) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.exists_local_homotopy_zero_of_derived_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/StrictlyPerfectLocalRep.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/StrictlyPerfectLocalRep.lean#L338). The attribute's comment: “local\_null\_homotopy”. References: SGA 6 I (4.1), “special case”.

> **Stacks 08C9, part (2).** Let `α : ℰ ⟶ ℱ` be a morphism of complexes of `𝒪_X`-modules with
> `ℰ` strictly perfect whose image in the derived category of `X` is zero. Then every point of `X`
> has an open neighbourhood over which `α` is homotopic to zero.
>
> The image of `α` in the derived category vanishes, so its image in the homotopy category is
> killed by a quasi-isomorphism `t : 𝒵 ⟶ ℰ`; that is, `t ≫ α` is null-homotopic. Stacks 08C8,
> applied to the identity of `ℰ` and to `t`, produces over some open neighbourhood `U` a map
> `β : ℰ|_U ⟶ 𝒵|_U` with `β ≫ t|_U` homotopic to the identity, and
> `CochainComplex.nonempty_homotopy_zero_of_lift_homotopy_id` concludes.

```lean
public theorem exists_local_homotopy_zero_of_derived_eq_zero
    [HasDerivedCategory.{d} (OXMod.{u, u} X)] {E F : CochainComplex (OXMod.{u, u} X) ℤ}
    (α : E ⟶ F) (hE : IsStrictlyPerfect E) (hα : DerivedCategory.Q.map α = 0) :
    ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      Nonempty (Homotopy
        (((SheafOfModules.overFunctor (structureSheafOfRings X) U).mapHomologicalComplex
          (ComplexShape.up ℤ)).map α) 0)
```

**`AlgebraicGeometry.RingedSpace.exists_local_complex_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/StrictlyPerfectLocalRep.lean, line 433](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/StrictlyPerfectLocalRep.lean#L433). The attribute's comment: “local\_representation”.

> **Stacks 08C9, part (1).** Let `ℰ`, `ℱ` be complexes of `𝒪_X`-modules with `ℰ` strictly
> perfect and let `α : ℰ ⟶ ℱ` be a morphism in the derived category of `X`. Then every point of `X`
> has an open neighbourhood `U` over which `α` is induced by a morphism of complexes
> `β : ℰ|_U ⟶ ℱ|_U`, the comparison being made through the canonical isomorphism
> `CategoryTheory.Functor.mapDerivedCategoryFactors` of the exact functor `restrictModules X U`.
>
> The exactness of restriction, which is what makes that comparison available, is part of the
> assertion; the witnesses are the instances
> `AlgebraicGeometry.RingedSpace.restrictModules_additive`,
> `AlgebraicGeometry.RingedSpace.restrictModules_preservesFiniteLimits` and
> `AlgebraicGeometry.RingedSpace.restrictModules_preservesFiniteColimits`, and the content is
> `AlgebraicGeometry.RingedSpace.exists_local_complex_map_of_instances`.

```lean
public theorem exists_local_complex_map [HasDerivedCategory.{d} (OXMod.{u, u} X)]
    [∀ U : Opens X.carrier,
      HasDerivedCategory.{d'} (OXMod.{u, u} (X.restrict U.isOpenEmbedding))]
    {E F : CochainComplex (OXMod.{u, u} X) ℤ} (hE : IsStrictlyPerfect E)
    (α : DerivedCategory.Q.obj E ⟶ DerivedCategory.Q.obj F) :
    ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      ∃ (hadd : (restrictModules.{u, u} X U).Additive)
        (hlim : PreservesFiniteLimits (restrictModules.{u, u} X U))
        (hcolim : PreservesFiniteColimits (restrictModules.{u, u} X U)),
        letI := hadd
        letI := hlim
        letI := hcolim
        ∃ β : ((restrictModules.{u, u} X U).mapHomologicalComplex (ComplexShape.up ℤ)).obj E ⟶
            ((restrictModules.{u, u} X U).mapHomologicalComplex (ComplexShape.up ℤ)).obj F,
          (restrictModules.{u, u} X U).mapDerivedCategory.map α ≫
              (restrictModules.{u, u} X U).mapDerivedCategoryFactors.hom.app F =
            (restrictModules.{u, u} X U).mapDerivedCategoryFactors.hom.app E ≫
              DerivedCategory.Q.map β
```

**`Stacks.Cohomology.exists_local_complex_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/LocalRepresentation.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/LocalRepresentation.lean#L216). The attribute's comment: “local\_representation”.

> A derived morphism out of a strictly perfect complex is locally represented by a morphism of
> complexes.

```lean
theorem exists_local_complex_map (hE : IsStrictlyPerfect E)
    (α : DerivedCategory.Q.obj E ⟶ DerivedCategory.Q.obj F) :
    ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      ∃ (hadd : (RingedSpace.restrictModules.{u, u} X U).Additive)
        (hlim : PreservesFiniteLimits (RingedSpace.restrictModules.{u, u} X U))
        (hcolim : PreservesFiniteColimits (RingedSpace.restrictModules.{u, u} X U)),
        letI := hadd
        letI := hlim
        letI := hcolim
        ∃ β : ((RingedSpace.restrictModules.{u, u} X U).mapHomologicalComplex
              (ComplexShape.up ℤ)).obj E ⟶
            ((RingedSpace.restrictModules.{u, u} X U).mapHomologicalComplex
              (ComplexShape.up ℤ)).obj F,
          (RingedSpace.restrictModules.{u, u} X U).mapDerivedCategory.map α ≫
              (RingedSpace.restrictModules.{u, u} X U).mapDerivedCategoryFactors.hom.app F =
          (RingedSpace.restrictModules.{u, u} X U).mapDerivedCategoryFactors.hom.app E ≫
              DerivedCategory.Q.map β
```

## Tag 08DM, a lemma

[Tag 08DM](https://stacks.math.columbia.edu/tag/08DM) in the Stacks Project.

**`Stacks.SheafOfModules.strictlyPerfectHomDegreeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/StrictlyPerfectHomRepresentation.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/StrictlyPerfectHomRepresentation.lean#L90). The attribute's comment: “finite direct-sum terms and Hom differential”.

> **Stacks 08DM, the degreewise description.** The degree-`n` term of the internal Hom complex
> `SheafHom(E, F)` of a bounded complex `E` is the finite direct sum `⊕\_q Hom\_\{O\_X}(E^\{-q},
> F^\{n-q})`, that is `⊕\_\{n = p + q} Hom\_\{O\_X}(E^\{-q}, F^p)`.

```lean
def strictlyPerfectHomDegreeIso (hE : {i : ℤ | ¬ IsZero (E.X i)}.Finite) (n : ℤ) :
    (RingedSite.sheafHomComplex (ringedSite Rc) E F).obj.X n ≅
      ∐ (fun q : ℤ => RingedSite.internalHomSheaf (ringedSite Rc) (E.X (-q)) (F.X (n - q)))
```

**`Stacks.SheafOfModules.strictlyPerfectHomComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/StrictlyPerfectHomRepresentation.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/StrictlyPerfectHomRepresentation.lean#L106). The attribute's comment: “representation by the finite direct-sum Hom complex”.

> **Stacks 08DM.** For `E` strictly perfect — bounded, with every term a direct summand of a
> finite free `O_X`-module — the derived internal Hom `RSheafHom(E, F)` is represented by the
> ordinary internal Hom complex `SheafHom(E, F)` of Stacks 0A8Z, for every complex `F`, the
> comparison being the canonical one. No injective resolution of `F` is needed.
>
> The comparison is an isomorphism exactly when the map of internal Hom complexes induced by the
> K-injective augmentation of `F` is a quasi-isomorphism, and strict perfectness of `E` makes it
> one: the statement holds for a source concentrated in one degree whose term is the structure
> sheaf, hence for finite free terms by direct sums, hence for direct summands of those by
> retracts, and the stupid filtration of the bounded complex `E` assembles the terms.

```lean
theorem strictlyPerfectHomComparison_isIso
    (hE : {i : ℤ | ¬ IsZero (E.X i)}.Finite)
    (hterm : ∀ i : ℤ, RingedSite.IsFiniteFreeSummand (ringedSite Rc) (E.X i)) :
    IsIso (strictlyPerfectHomComparison Rc E F)
```

## Tag 0GM5, a lemma

[Tag 0GM5](https://stacks.math.columbia.edu/tag/0GM5) in the Stacks Project.

**`Stacks.SheafOfModules.isKFlat_sheafHomComplex_of_isKFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/StrictlyPerfectHomKFlat.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/StrictlyPerfectHomKFlat.lean#L260). The attribute's comment: “the whole lemma on a ringed space: for E strictly perfect, written out as in Definition 20.46.1 -- hE is 'E^i is zero for all but finitely many i' and hterm is 'E^i is a direct summand of a finite free O\_X-module for all i' -- and F K-flat (hF), the complex sheafHomComplex E F is K-flat”.

> **Stacks 0GM5.** In the situation of Stacks 08DM — `E` strictly perfect, so that the
> internal Hom complex `H = SheafHom(E, F)` represents `RSheafHom(E, F)` — the complex `H` is
> K-flat as soon as `F` is.
>
> For an acyclic `G` the argument is: `F` is K-flat and `G` is acyclic, so `Tot(G ⊗ F)` is
> acyclic; the internal Hom complex out of a strictly perfect source into an acyclic complex is
> acyclic, so the target of the Stacks 0BYR comparison
> `Tot(G ⊗ SheafHom(E, F)) ⟶ SheafHom(E, Tot(G ⊗ F))` is acyclic; that comparison is a
> quasi-isomorphism at a strictly perfect source, by the dévissage along the termwise split
> stupid filtration of Homology, Section 0118 on the ringed site of the opens of `X`
> in `AlgebraicGeometry.RingedSite.tensorHomInterchange_quasiIso_of_isFiniteFreeSummand`; hence
> its source is acyclic too, and that source is the total complex K-flatness of `H` asks
> about.

```lean
theorem isKFlat_sheafHomComplex_of_isKFlat
    (E F : CochainComplex (StructureSheafModules Rc) ℤ)
    (hE : {i : ℤ | ¬ IsZero (E.X i)}.Finite)
    (hterm : ∀ i : ℤ, RingedSite.IsFiniteFreeSummand (ringedSite Rc) (E.X i))
    (hF : IsKFlat Rc F) :
    IsKFlat Rc (sheafHomComplex Rc E F).obj
```

**`AlgebraicGeometry.RingedSite.isKFlat_sheafHomComplex_of_isKFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/StrictlyPerfectHomKFlatSite.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/StrictlyPerfectHomKFlatSite.lean#L124). The attribute's comment: “on a ringed site”.

> **Stacks 0GM5 on a ringed site.** In the situation of Stacks 08DM — `E` with finitely many
> nonzero terms, each a direct summand of a finite free module, so that the internal Hom complex
> `SheafHom(E, F)` represents `RSheafHom(E, F)` — that complex is K-flat as soon as `F` is.
>
> This is what makes the dual `SheafHom(P, O[0])` of a strictly perfect complex `P` usable as the
> K-flat tensor factor in the invertibility criterion for the composition morphism of derived
> internal Homs, and so is the input the local step of the third assertion of Stacks 08DQ needs on
> the slices of the site.

```lean
theorem isKFlat_sheafHomComplex_of_isKFlat
    (E F : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (hE : {i : ℤ | ¬ IsZero (E.X i)}.Finite)
    (hterm : ∀ i : ℤ, IsFiniteFreeSummand X (E.X i))
    (hF : letI : X.J.WEqualsLocallyBijective AddCommGrpCat.{u} := inferInstance
      Stacks.SheafOfModules.IsKFlat X.O F) :
    letI : X.J.WEqualsLocallyBijective AddCommGrpCat.{u} := inferInstance
    Stacks.SheafOfModules.IsKFlat X.O (sheafHomComplex X E F).obj
```

## Tag 08I5, a lemma

[Tag 08I5](https://stacks.math.columbia.edu/tag/08I5) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.homMap_quasiIso_of_boundedAbove_isFiniteFreeSummand`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/BoundedAboveHomComparison.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/BoundedAboveHomComparison.lean#L281). The attribute's comment: “invariance of the internal Hom complex under quasi-isomorphism”.

> **Stacks 08I5**, the quasi-isomorphism invariance. Let `E` be a complex of `O`-modules which
> is bounded above and all of whose terms are direct summands of finite free `O`-modules. Then the
> internal Hom complex out of `E` carries a quasi-isomorphism between two complexes vanishing in
> all degrees below a common bound `a` to a quasi-isomorphism.
>
> This is the whole content of the tag; the representation statement
> `strictlyPerfectHomComparison_isIso_of_boundedAbove` is obtained from it by the formal reduction
> `strictlyPerfectHomComparison_isIso_iff`.
>
> Unlike `homMap_quasiIso_of_isFiniteFreeSummand` (Stacks 08JH) the source is not assumed to have
> finitely many nonzero terms, and in exchange the targets are assumed bounded below. The proof is
> degreewise: `quasiIsoAt_homMap_of_boundedAbove` at `k = a - n - 1`.

```lean
theorem homMap_quasiIso_of_boundedAbove_isFiniteFreeSummand (a : ℤ)
    (hF : ∀ i, i < a → IsZero (F.X i))
    (hG : ∀ i, i < a → IsZero (G.X i))
    (hE : ∃ b : ℤ, ∀ i, b < i → IsZero (E.X i))
    (hterm : ∀ i, IsFiniteFreeSummand X (E.X i))
    (f : F ⟶ G) [QuasiIso f] :
    QuasiIso (homMap X (𝟙 E) f)
```

**`AlgebraicGeometry.RingedSite.strictlyPerfectHomComparison_isIso_of_boundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/BoundedAboveHomComparison.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/BoundedAboveHomComparison.lean#L309). The attribute's comment: “representation of derived internal Hom by the ordinary Hom complex”.

> **Stacks 08I5**, the representation statement. Let `E` be a complex of `O`-modules which is
> bounded above and all of whose terms are direct summands of finite free `O`-modules, and let `F`
> vanish in all degrees below `a`. Then the derived internal Hom `RSheafHom(E, F)` is represented
> by the ordinary internal Hom complex `SheafHom(E, F)` of Stacks 0A8Z, the comparison being the
> canonical one of `strictlyPerfectHomComparison`.
>
> By `strictlyPerfectHomComparison_isIso_iff` the claim is the quasi-isomorphy of the map of
> internal Hom complexes induced by the K-injective augmentation `F ⟶ I` of the target. The
> chosen resolution `I` carries no lower bound, so the invariance is applied instead to a
> degreewise injective resolution `u : F ⟶ I₀` which is again zero below `a`, and transported to
> the augmentation of `F` along the naturality square of the augmentation; the two maps between
> K-injective complexes occurring there are handled by `homMap_quasiIso` (Stacks 0A95). See the
> implementation notes.

```lean
theorem strictlyPerfectHomComparison_isIso_of_boundedAbove (a : ℤ)
    (hF : ∀ i, i < a → IsZero (F.X i))
    (hE : ∃ b : ℤ, ∀ i, b < i → IsZero (E.X i))
    (hterm : ∀ i, IsFiniteFreeSummand X (E.X i)) :
    IsIso (strictlyPerfectHomComparison X D E F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.46, Tag 08C3](https://stacks.math.columbia.edu/tag/08C3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
