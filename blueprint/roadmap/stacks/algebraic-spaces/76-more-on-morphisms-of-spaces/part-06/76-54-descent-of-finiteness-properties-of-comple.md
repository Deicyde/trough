---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isPseudoCoherentFrom_iff_forall_derivedPullback_of_isFpqcCovering, AlgebraicGeometry.Space.hasTorAmplitudeCanonical_etaleStalk_iff_of_cartesian, AlgebraicGeometry.Space.hasFiniteTorDimensionCanonical_etaleStalk_iff_of_cartesian, AlgebraicGeometry.Space.locallyHasFiniteTorDimension_derivedScalarRestriction_iff_forall_of_isFpqcCovering, AlgebraicGeometry.Space.hasTorAmplitude_derivedScalarRestriction_iff_forall_of_isFpqcCovering, AlgebraicGeometry.Space.isPseudoCoherent_of_derivedPullback_of_isFiniteOrderThickening, AlgebraicGeometry.Space.isPerfectRelativeToCanonical_of_pull_of_isThickeningHom, AlgebraicGeometry.Space.isRelativelyPerfect_of_isRelativelyPerfect_closedFibre
statement: formalized
proof: formalized
---

# 76.54 Descent of finiteness properties of complexes

Section 76.54 of the Stacks Project, [Tag 0DL0](https://stacks.math.columbia.edu/tag/0DL0). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DL1, a lemma

[Tag 0DL1](https://stacks.math.columbia.edu/tag/0DL1) in the Stacks Project.

**`AlgebraicGeometry.Space.isPseudoCoherentFrom_iff_forall_derivedPullback_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/FpqcDescent.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/FpqcDescent.lean#L461). The attribute's comment: “the full statement, for an arbitrary fpqc covering of algebraic spaces”.

> **Stacks 0DL1.** Let `{f_i : X_i ⟶ X}` be an fpqc covering of algebraic spaces over a scheme
> `S`, let `E` be an object of `D_QCoh(𝒪_X)` and let `m` be an integer. Then `E` is
> `m`-pseudo-coherent if and only if each `Lf_i^*E` is `m`-pseudo-coherent.
>
> The forward implication is
> `AlgebraicGeometry.Space.isPseudoCoherentFrom_smallEtaleDerivedModulePullback`. For the converse,
> Stacks 0419 refines the covering by morphisms `e_i : T_i ⟶ X_i` out of schemes of the site with
> `{e_i ≫ f_i}` again an fpqc covering; `L(e_i ≫ f_i)^*E ≅ Le_i^*(Lf_i^*E)` (Stacks 0D6D) is
> `m`-pseudo-coherent by the forward implication, as `Lf_i^*E` has quasi-coherent cohomology
> (Stacks 08F4), and
> `AlgebraicGeometry.Space.isPseudoCoherentFrom_of_isFpqcCovering_representable` applies.

```lean
theorem isPseudoCoherentFrom_iff_forall_derivedPullback_of_isFpqcCovering {I : Type v}
    {X : AlgebraicSpaces B S hS} {Xi : I → AlgebraicSpaces B S hS}
    (f : ∀ i, Xi i ⟶ X) (hf : IsFpqcCovering B S hS fun i => (f i).hom)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : ∀ n : ℤ, ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS X.1 X.2) n).obj E).IsQuasicoherentOnSite)
    (m : ℤ) :
    (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherentFrom E m ↔
      ∀ i, (smallEtaleRingedSite B S hS (Xi i).1 (Xi i).2).IsPseudoCoherentFrom
        ((smallEtaleDerivedModulePullback B S hS (f i)).obj E) m
```

## Tag 0DL2, a lemma

[Tag 0DL2](https://stacks.math.columbia.edu/tag/0DL2) in the Stacks Project.

**`AlgebraicGeometry.Space.hasTorAmplitudeCanonical_etaleStalk_iff_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeTorAmplitudeFpqcDescent.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeTorAmplitudeFpqcDescent.lean#L365). The attribute's comment: “tor amplitude in [a, b], at a geometric point”.

> **Stacks 0DL2**, the clause on Tor amplitude in `[a, b]`, at a geometric point.
>
> Let
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> be a cartesian square of algebraic spaces whose two morphisms to the base are Tor independent,
> let `x̄'` be a geometric point of the upper-left corner, with images `x̄` in `X`, `ȳ'` in `Y'` and
> `ȳ` in `Y`, and suppose that the canonical homomorphism `𝒪_{Y, ȳ} → 𝒪_{Y', ȳ'}` of étale local
> rings of Stacks 04NG is faithfully flat — which for a member of an fpqc covering it is, being
> flat by Stacks 04NG and local. Then an object `E` of `D(𝒪_{X, x̄})` has Tor amplitude in `[a, b]`
> over `𝒪_{Y, ȳ}` if and only if its derived base change to
> `𝒪_{X, x̄} ⊗_{𝒪_{Y, ȳ}} 𝒪_{Y', ȳ'}` has Tor amplitude in `[a, b]` over `𝒪_{Y', ȳ'}`.
>
> This is the source's own proof read at the geometric stalks, where the source reads it: a
> relative Tor-amplitude bound is a bound on the stalk complexes over the étale local rings of the
> base (Stacks 0DJJ and 04K5), the stalk of `L(g')^* E` is the derived base change of the stalk of
> `E`, Tor independence identifies that derived base change over `𝒪_{X, x̄}` with the derived base
> change over `𝒪_{Y, ȳ}` by Stacks 0661, and the bound descends along the faithfully flat
> `𝒪_{Y, ȳ} → 𝒪_{Y', ȳ'}` by Stacks 068S. The forward implication is Stacks 0DKD (1) at the
> tensor product.

```lean
theorem hasTorAmplitudeCanonical_etaleStalk_iff_of_cartesian
    {X' X Y' Y : AlgebraicSpaces B S hS} (g' : X' ⟶ X) (f' : X' ⟶ Y')
    (f : X ⟶ Y) (g : Y' ⟶ Y) (hpb : IsPullback g' f' f g)
    (htor : TorIndependent X.2 Y'.2 Y.2 f.hom g.hom)
    (x' : GeometricPoint B S hS X'.1)
    (E : DerivedCategory (ModuleCat.{u + 1}
      ↥(etaleLocalRing B S hS X.1 (geometricPointMap g'.hom x')))) (a b : ℤ) :
    letI : Algebra
        ↥(etaleLocalRing B S hS Y.1 (geometricPointMap f.hom (geometricPointMap g'.hom x')))
        ↥(etaleLocalRing B S hS X.1 (geometricPointMap g'.hom x')) :=
      (etaleLocalRingMap X.2 f.hom (geometricPointMap g'.hom x')).toAlgebra
    letI : Algebra
        ↥(etaleLocalRing B S hS Y.1 (geometricPointMap f.hom (geometricPointMap g'.hom x')))
        ↥(etaleLocalRing B S hS Y'.1 (geometricPointMap f'.hom x')) :=
      ((eqToHom (congrArg (etaleLocalRing B S hS Y.1)
          (congrArg (fun k : X' ⟶ Y => geometricPointMap k.hom x') hpb.w)) ≫
        CommRingCat.ofHom
          (etaleLocalRingMap Y'.2 g.hom (geometricPointMap f'.hom x'))).hom).toAlgebra
    Module.FaithfullyFlat
        ↥(etaleLocalRing B S hS Y.1 (geometricPointMap f.hom (geometricPointMap g'.hom x')))
        ↥(etaleLocalRing B S hS Y'.1 (geometricPointMap f'.hom x')) →
    letI T := TensorProduct
        ↥(etaleLocalRing B S hS Y.1 (geometricPointMap f.hom (geometricPointMap g'.hom x')))
        ↥(etaleLocalRing B S hS X.1 (geometricPointMap g'.hom x'))
        ↥(etaleLocalRing B S hS Y'.1 (geometricPointMap f'.hom x'))
    letI : Algebra ↥(etaleLocalRing B S hS Y'.1 (geometricPointMap f'.hom x')) T :=
      Algebra.TensorProduct.rightAlgebra
    (HasTorAmplitudeCanonical
        ↥(etaleLocalRing B S hS Y.1 (geometricPointMap f.hom (geometricPointMap g'.hom x')))
        ((ModuleCat.restrictScalars
          (etaleLocalRingMap X.2 f.hom
            (geometricPointMap g'.hom x'))).mapDerivedCategory.obj E) a b ↔
      HasTorAmplitudeCanonical ↥(etaleLocalRing B S hS Y'.1 (geometricPointMap f'.hom x'))
        ((ModuleCat.restrictScalars (algebraMap
            ↥(etaleLocalRing B S hS Y'.1 (geometricPointMap f'.hom x')) T)).mapDerivedCategory.obj
          ((totalDerivedExtensionScalars.{u + 1, u + 1, u + 1} (algebraMap
            ↥(etaleLocalRing B S hS X.1 (geometricPointMap g'.hom x')) T)).functor.obj E))
        a b)
```

**`AlgebraicGeometry.Space.hasFiniteTorDimensionCanonical_etaleStalk_iff_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeTorAmplitudeFpqcDescent.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeTorAmplitudeFpqcDescent.lean#L448). The attribute's comment: “finite tor dimension, at a geometric point”.

> **Stacks 0DL2**, the clause on finite Tor dimension, at a geometric point.
>
> Under the hypotheses of `hasTorAmplitudeCanonical_etaleStalk_iff_of_cartesian`, an object `E` of
> `D(𝒪_{X, x̄})` has finite Tor dimension over `𝒪_{Y, ȳ}` if and only if its derived base change to
> `𝒪_{X, x̄} ⊗_{𝒪_{Y, ȳ}} 𝒪_{Y', ȳ'}` has finite Tor dimension over `𝒪_{Y', ȳ'}`. Finite Tor
> dimension is Tor amplitude in some interval, so this is the previous statement for each interval
> separately — the "elementary topology" with which the source reduces the second clause of the
> lemma to the first.

```lean
theorem hasFiniteTorDimensionCanonical_etaleStalk_iff_of_cartesian
    {X' X Y' Y : AlgebraicSpaces B S hS} (g' : X' ⟶ X) (f' : X' ⟶ Y')
    (f : X ⟶ Y) (g : Y' ⟶ Y) (hpb : IsPullback g' f' f g)
    (htor : TorIndependent X.2 Y'.2 Y.2 f.hom g.hom)
    (x' : GeometricPoint B S hS X'.1)
    (E : DerivedCategory (ModuleCat.{u + 1}
      ↥(etaleLocalRing B S hS X.1 (geometricPointMap g'.hom x')))) :
    letI : Algebra
        ↥(etaleLocalRing B S hS Y.1 (geometricPointMap f.hom (geometricPointMap g'.hom x')))
        ↥(etaleLocalRing B S hS X.1 (geometricPointMap g'.hom x')) :=
      (etaleLocalRingMap X.2 f.hom (geometricPointMap g'.hom x')).toAlgebra
    letI : Algebra
        ↥(etaleLocalRing B S hS Y.1 (geometricPointMap f.hom (geometricPointMap g'.hom x')))
        ↥(etaleLocalRing B S hS Y'.1 (geometricPointMap f'.hom x')) :=
      ((eqToHom (congrArg (etaleLocalRing B S hS Y.1)
          (congrArg (fun k : X' ⟶ Y => geometricPointMap k.hom x') hpb.w)) ≫
        CommRingCat.ofHom
          (etaleLocalRingMap Y'.2 g.hom (geometricPointMap f'.hom x'))).hom).toAlgebra
    Module.FaithfullyFlat
        ↥(etaleLocalRing B S hS Y.1 (geometricPointMap f.hom (geometricPointMap g'.hom x')))
        ↥(etaleLocalRing B S hS Y'.1 (geometricPointMap f'.hom x')) →
    letI T := TensorProduct
        ↥(etaleLocalRing B S hS Y.1 (geometricPointMap f.hom (geometricPointMap g'.hom x')))
        ↥(etaleLocalRing B S hS X.1 (geometricPointMap g'.hom x'))
        ↥(etaleLocalRing B S hS Y'.1 (geometricPointMap f'.hom x'))
    letI : Algebra ↥(etaleLocalRing B S hS Y'.1 (geometricPointMap f'.hom x')) T :=
      Algebra.TensorProduct.rightAlgebra
    (HasFiniteTorDimensionCanonical
        ↥(etaleLocalRing B S hS Y.1 (geometricPointMap f.hom (geometricPointMap g'.hom x')))
        ((ModuleCat.restrictScalars
          (etaleLocalRingMap X.2 f.hom
            (geometricPointMap g'.hom x'))).mapDerivedCategory.obj E) ↔
      HasFiniteTorDimensionCanonical
        ↥(etaleLocalRing B S hS Y'.1 (geometricPointMap f'.hom x'))
        ((ModuleCat.restrictScalars (algebraMap
            ↥(etaleLocalRing B S hS Y'.1 (geometricPointMap f'.hom x')) T)).mapDerivedCategory.obj
          ((totalDerivedExtensionScalars.{u + 1, u + 1, u + 1} (algebraMap
            ↥(etaleLocalRing B S hS X.1 (geometricPointMap g'.hom x')) T)).functor.obj E)))
```

**`AlgebraicGeometry.Space.locallyHasFiniteTorDimension_derivedScalarRestriction_iff_forall_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeTorAmplitudeFpqcDescentLocal.lean, line 658](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeTorAmplitudeFpqcDescentLocal.lean#L658). The attribute's comment: “locally finite tor dimension”.

> **Stacks 0DL2**, locally finite Tor dimension.

```lean
theorem locallyHasFiniteTorDimension_derivedScalarRestriction_iff_forall_of_isFpqcCovering
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) :
    LocallyHasFiniteTorDimension.{u + 1, u, u, u + 1}
      (fun U => Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u + 1, u, u + 1}
        ((inverseImageRingedSite B S hS f).over U))
      ((derivedScalarRestriction B S hS f).obj E) ↔
      ∀ i, LocallyHasFiniteTorDimension.{u + 1, u, u, u + 1}
      (fun U => Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u + 1, u, u + 1}
        ((inverseImageRingedSite B S hS (f' i)).over U))
      ((derivedScalarRestriction B S hS (f' i)).obj
        ((smallEtaleDerivedModulePullback B S hS (g' i)).obj E))
```

**`AlgebraicGeometry.Space.hasTorAmplitude_derivedScalarRestriction_iff_forall_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeTorAmplitudeFpqcDescentSheaf.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeTorAmplitudeFpqcDescentSheaf.lean#L228). The attribute's comment: “tor amplitude in [a, b]”.

> Let `{g_i : Y_i ⟶ Y}` be an fpqc covering of
> algebraic spaces over `S`, let `f : X ⟶ Y` be a morphism of algebraic spaces and let
> `X_i = Y_i ×_Y X`, with projections `f_i : X_i ⟶ Y_i` and `g'_i : X_i ⟶ X`.  An object `E` of
> `D(𝒪_X)` has Tor amplitude in `[a, b]` as an object of `D(f⁻¹𝒪_Y)` if and only if every
> `L(g'_i)^* E` has Tor amplitude in `[a, b]` as an object of `D(f_i⁻¹𝒪_{Y_i})`, both measured
> against the derived tensor product of Stacks 06YU.

```lean
theorem hasTorAmplitude_derivedScalarRestriction_iff_forall_of_isFpqcCovering
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) (a b : ℤ) :
    Stacks.SheafOfModules.DerivedTensorProduct.HasTorAmplitude.{u + 1, u, u, u + 1}
        (Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u + 1, u, u + 1}
          (inverseImageRingedSite B S hS f)) ((derivedScalarRestriction B S hS f).obj E) a b ↔
      ∀ i, Stacks.SheafOfModules.DerivedTensorProduct.HasTorAmplitude.{u + 1, u, u, u + 1}
        (Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u + 1, u, u + 1}
          (inverseImageRingedSite B S hS (f' i)))
        ((derivedScalarRestriction B S hS (f' i)).obj
          ((smallEtaleDerivedModulePullback B S hS (g' i)).obj E)) a b
```

## Tag 0DL3, a lemma

[Tag 0DL3](https://stacks.math.columbia.edu/tag/0DL3) in the Stacks Project.

**`AlgebraicGeometry.Space.isPseudoCoherent_of_derivedPullback_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/Thickening.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/Thickening.lean#L135).

> **Stacks 0DL3.** Let `S` be a scheme and let `i : Z ⟶ X'` be a finite-order thickening of
> algebraic spaces over `S`. Let `K'` be an object of `D(𝒪_{X'})` such that `K = Li^*K'` is
> pseudo-coherent. Then `K'` is pseudo-coherent.
>
> The thickening is the inclusion `AlgebraicGeometry.Space.subspaceInclusion` of a closed subspace
> `Z` of `X'` which is a finite-order thickening (Stacks 05ZK), `Li^*` is the derived pullback of
> Stacks 06YY along it, and pseudo-coherence is Stacks 08FT on the small étale ringed sites.

```lean
theorem isPseudoCoherent_of_derivedPullback_of_isFiniteOrderThickening
    {X' : AlgebraicSpaces B S hS} (Z : ClosedSubspaces B S hS X'.1)
    (hZ : IsFiniteOrderThickening B S hS X' Z.1)
    (K' : DerivedCategory (Modules.{u, u} B S hS X'.1 X'.2))
    (hK :
      haveI := hasLeftDerivedFunctor_smallEtaleModulePullbackOnHomotopy B S hS
        (subspaceInclusion B S hS X' Z)
      (smallEtaleRingedSite B S hS Z.1.toFunctor Z.2.1).IsPseudoCoherent
        ((smallEtaleDerivedModulePullback B S hS (subspaceInclusion B S hS X' Z)).obj K')) :
    (smallEtaleRingedSite B S hS X'.1 X'.2).IsPseudoCoherent K'
```

## Tag 0DL4, a lemma

[Tag 0DL4](https://stacks.math.columbia.edu/tag/0DL4) in the Stacks Project.

**`AlgebraicGeometry.Space.isPerfectRelativeToCanonical_of_pull_of_isThickeningHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackThickeningPerfectProved.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackThickeningPerfectProved.lean#L130).

> Consider a cartesian square
> ```
> X --i--> X'
> |f       |f'
> v        v
> Y --j--> Y'
> ```
> of algebraic spaces over `S`. Assume `f'` is flat and locally of finite presentation and `j` is
> a finite-order thickening: `j` is an isomorphism onto its range, which is a finite-order
> thickening of `Y'` (Stacks 05ZK). Let `E' ∈ D(𝒪_{X'})`. If `E = Li^*E'` is `Y`-perfect
> (Stacks 0DKN), then `E'` is `Y'`-perfect.

```lean
theorem isPerfectRelativeToCanonical_of_pull_of_isThickeningHom
    {X X' Y Y' : AlgebraicSpaces B S hS} {i : X ⟶ X'} {f : X ⟶ Y} {f' : X' ⟶ Y'} {j : Y ⟶ Y'}
    (hpb : IsPullback i f f' j) (hj : IsThickeningHom B S hS j)
    (hjfin : IsFiniteOrderThickening B S hS Y' (Subfunctor.range j.hom))
    (hflat : IsFlat B S hS f'.hom) (hlfp : IsLocallyOfFinitePresentation B S hS f'.hom)
    (E' : derivedModules B S hS X')
    (hE : IsPerfectRelativeToCanonical B S hS f
      ((isFlat_isStableUnderBaseChange B S hS).of_isPullback hpb hflat)
      ((isLocallyOfFinitePresentation_isStableUnderBaseChange B S hS).of_isPullback hpb
        hlfp)
      (((smallEtaleDerivedPullbackData B S hS).pull i).obj E')) :
    IsPerfectRelativeToCanonical B S hS f' hflat hlfp E'
```

## Tag 0DL5, a lemma

[Tag 0DL5](https://stacks.math.columbia.edu/tag/0DL5) in the Stacks Project.

**`AlgebraicGeometry.Space.isRelativelyPerfect_of_isRelativelyPerfect_closedFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativelyPerfectClosedFibre.lean, line 637](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativelyPerfectClosedFibre.lean#L637).

> **Stacks 0DL5.** Let `(R, I)` be a ring with an ideal contained in its Jacobson radical, let
> `𝒮 = Spec R` and `𝒮₀ = Spec (R/I)`, and let `f : X ⟶ 𝒮` be a proper and flat morphism of
> algebraic spaces, locally of finite presentation (hence of finite presentation, `f` being proper).
> Let `X₀ = 𝒮₀ ×_𝒮 X`, with projections `i : X₀ ⟶ X` and `f₀ : X₀ ⟶ 𝒮₀`. If a pseudo-coherent object
> `E` of `D(𝒪_X)` has `𝒮₀`-perfect derived restriction `Li^*E` to `X₀`, then `E` is `𝒮`-perfect.
>
> On an affine étale chart `Spec A ⟶ X`, presented by `d` variables over `R`, `E` is `ε^*(P~)` for a
> bounded above complex `P` of finite free `A`-modules, and `Li^*E` is `ε^*((P ⊗_R R/I)~)` on the
> closed fibre of the chart. One interval `[a, b]` bounds the Tor amplitude of the geometric stalks
> of `Li^*E` on the quasi-compact `X₀`, and then `[a - d, b]` bounds those of `E` over the stalks of
> `f⁻¹𝒪_𝒮` (`hasTorAmplitudeCanonical_geometricStalk_of_closedFibre`); a uniform bound at the
> geometric stalks gives locally finite Tor dimension (Stacks 0DJJ, 04K5).
>
> `X₀` is the fibre product in the category of algebraic spaces; flatness and local finite
> presentation of `f₀`, the preconditions of `𝒮₀`-perfectness (Stacks 0DKN), are those of `f` by base
> change.

```lean
theorem isRelativelyPerfect_of_isRelativelyPerfect_closedFibre
    (hI : I ≤ (⊥ : Ideal R).jacobson) (i : X₀ ⟶ X)
    (hpb : IsPullback i f₀ f (representedSpaceMap B S hS (quotientSpecMap B S hS hR gR I hR₀)))
    (hproper : IsProper B S hS f.hom) (hflat : IsFlat B S hS f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent E)
    (hE₀ : haveI := hasLeftDerivedFunctor_smallEtaleModulePullbackOnHomotopy B S hS i
      IsRelativelyPerfect B S hS f₀ (isFlat_snd_of_isPullback B S hS hpb hflat)
        (isLocallyOfFinitePresentation_snd_of_isPullback B S hS hpb hlfp)
        ((smallEtaleDerivedModulePullback B S hS i).obj E)) :
    IsRelativelyPerfect B S hS f hflat hlfp E
```

**`AlgebraicGeometry.Space.isPerfectRelativeTo_of_isPerfectRelativeTo_closedFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativelyPerfectJacobsonFibre.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativelyPerfectJacobsonFibre.lean#L258). The attribute's comment: “the pseudo-coherence clause and the specialization step; Tor clause carried”.

> **Stacks 0DL5.** Let `(R, I)` be a ring with an ideal contained in its Jacobson radical, let
> `𝒮 = Spec R` and `𝒮₀ = Spec (R/I)`, let `f : X ⟶ 𝒮` be a proper, flat, locally finitely
> presented morphism of algebraic spaces and let `X₀ = 𝒮₀ ×_𝒮 X`. A pseudo-coherent object `E` of
> `D(𝒪_X)` whose derived restriction to `X₀` is `𝒮₀`-perfect is `𝒮`-perfect.
>
> The pseudo-coherence clause of the conclusion is the hypothesis on `E`. For the Tor clause,
> properness makes `|X| → |𝒮|` closed and the ideal `I` lying in the Jacobson radical makes every
> nonempty closed subset of `|𝒮|` meet `|𝒮₀|`, so every point of `|X|` specializes into the closed
> fibre; from there the bound is `hTor`.

```lean
theorem isPerfectRelativeTo_of_isPerfectRelativeTo_closedFibre (i : X₀ ⟶ X) (j : 𝒮₀ ⟶ 𝒮)
    [(smallEtaleModulePullbackOnHomotopy B S hS i).HasLeftDerivedFunctor
      (smallEtaleModuleQuasiIso B S hS X)]
    (hflat : IsFlat B S hS f.hom) (hlfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (hflat₀ : IsFlat B S hS f₀.hom) (hlfp₀ : IsLocallyOfFinitePresentation B S hS f₀.hom)
    (T : ∀ U : (inverseImageRingedSite B S hS f).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, e}
        ((inverseImageRingedSite B S hS f).over U))
    (T₀ : ∀ U : (inverseImageRingedSite B S hS f₀).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, e}
        ((inverseImageRingedSite B S hS f₀).over U))
    {R : Type u} [CommRing R] {I : Ideal R} (hI : I ≤ (⊥ : Ideal R).jacobson)
    (eR : points B S hS 𝒮.1 ≃ₜ PrimeSpectrum R)
    (hj : Set.range (pointsMap B S hS 𝒮₀.1 j.hom) =
      eR ⁻¹' PrimeSpectrum.zeroLocus (I : Set R))
    (hproper : IsProper B S hS f.hom) (_hpb : IsPullback i f₀ f j)
    (hTor : LocallyFiniteTorDimensionFromClosedFibre B S hS f f₀ i j hflat₀ hlfp₀ T T₀)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent E)
    (hE₀ : IsPerfectRelativeTo B S hS f₀ hflat₀ hlfp₀ T₀
      ((smallEtaleDerivedModulePullback B S hS i).obj E)) :
    IsPerfectRelativeTo B S hS f hflat hlfp T E
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.54, Tag 0DL0](https://stacks.math.columbia.edu/tag/0DL0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
