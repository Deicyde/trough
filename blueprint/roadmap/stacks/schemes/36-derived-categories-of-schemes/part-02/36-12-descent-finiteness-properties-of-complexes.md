---
declaration: section
origin: cited
lean: Stacks.Cohomology.TorAmplitude.FlatDescent.hasTorAmplitude_derivedPullback_iff, Stacks.Cohomology.PseudoCoherence.FpqcDescent.isPseudoCoherentFrom_iff_forall_fpqc, Stacks.Cohomology.PseudoCoherence.FlatDescent.isPseudoCoherentFrom_iff_forall_fppf, Stacks.Cohomology.PerfectComplexes.FpqcDescent.isPerfect_iff_forall_isPerfect_derivedPullback, AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_derivedPushforwardOXMod, AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_of_derivedPushforwardOXMod, AlgebraicGeometry.isPseudoCoherentFrom_iff_derivedPushforward_of_isFinite
statement: formalized
proof: formalized
---

# 36.12 Descent finiteness properties of complexes

Section 36.12 of the Stacks Project, [Tag 09UC](https://stacks.math.columbia.edu/tag/09UC). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09UD, a lemma

[Tag 09UD](https://stacks.math.columbia.edu/tag/09UD) in the Stacks Project.

**`Stacks.Cohomology.TorAmplitude.FlatDescent.hasTorAmplitude_derivedPullback_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/FlatSurjectiveDescent.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/FlatSurjectiveDescent.lean#L229).

> Let `f : X ⟶ Y` be a surjective flat morphism of locally ringed spaces, let `E` be an
> object of `D(𝒪_Y)` and let `a, b` be integers.  Then `E` has Tor amplitude in `[a, b]` if and
> only if `Lf^*E` has Tor amplitude in `[a, b]`.

```lean
theorem hasTorAmplitude_derivedPullback_iff {X Y : LocallyRingedSpace.{u}} (f : X ⟶ Y)
    (hsurj : Function.Surjective f.base) (hflat : AlgebraicGeometry.IsFlat f.toShHom)
    (E : DerivedCategory (OXMod.{u, u} Y.toRingedSpace)) (a b : ℤ) :
    HasTorAmplitude Y.toRingedSpace E a b ↔
      HasTorAmplitude X.toRingedSpace
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f.toShHom).obj E)
        a b
```

## Tag 09UE, a lemma

[Tag 09UE](https://stacks.math.columbia.edu/tag/09UE) in the Stacks Project.

**`Stacks.Cohomology.PseudoCoherence.FpqcDescent.isPseudoCoherentFrom_iff_forall_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/FpqcDescent.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/FpqcDescent.lean#L595).

> **Stacks 09UE.**

```lean
public theorem isPseudoCoherentFrom_iff_forall_fpqc {X : Scheme.{u}} {I : Type v}
    (Y : I → Scheme.{u}) (f : ∀ i, Y i ⟶ X)
    (hf : Presieve.ofArrows Y f ∈ Scheme.fpqcPrecoverage X)
    (E : Stacks.Duality.quasiCoherentDerivedCategory X) (m : ℤ) :
    IsPseudoCoherentFrom E.obj m ↔
      ∀ i : I, IsPseudoCoherentFrom
        ((Stacks.Duality.quasiCoherentDerivedPullback' (f i)).obj E).obj m
```

## Tag 09UF, a lemma

[Tag 09UF](https://stacks.math.columbia.edu/tag/09UF) in the Stacks Project.

**`Stacks.Cohomology.PseudoCoherence.FlatDescent.isPseudoCoherentFrom_iff_forall_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/FppfDescent.lean, line 441](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/FppfDescent.lean#L441).

> Let `{f_i : X_i ⟶ X}` be an fppf covering of schemes, let `E` be an object of `D(𝒪_X)` and
> let `m` be an integer. Then `E` is `m`-pseudo-coherent if and only if each `Lf_i^*E` is
> `m`-pseudo-coherent.

```lean
public theorem isPseudoCoherentFrom_iff_forall_fppf {X : Scheme.{u}} {I : Type v}
    (Y : I → Scheme.{u}) (f : ∀ i, Y i ⟶ X)
    (hf : Presieve.ofArrows Y f ∈ Scheme.fppfPrecoverage X)
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace)) (m : ℤ) :
    IsPseudoCoherentFrom E m ↔
      ∀ i : I, IsPseudoCoherentFrom
        ((derivedPullback (f i).toLRSHom.toShHom).obj E) m
```

## Tag 09UG, a lemma

[Tag 09UG](https://stacks.math.columbia.edu/tag/09UG) in the Stacks Project.

**`Stacks.Cohomology.PerfectComplexes.FpqcDescent.isPerfect_iff_forall_isPerfect_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/FpqcDescent.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/FpqcDescent.lean#L157).

> **Stacks 09UG.** Let `{f_i : Y_i ⟶ X}` be an fpqc covering of schemes and let
> `E ∈ D(𝒪_X)`. Then `E` is perfect if and only if each derived pullback `Lf_i^*E` is perfect.

```lean
public theorem isPerfect_iff_forall_isPerfect_derivedPullback {X : Scheme.{u}} {I : Type v}
    (Y : I → Scheme.{u}) (f : ∀ i, Y i ⟶ X)
    (hf : Presieve.ofArrows Y f ∈ Scheme.fpqcPrecoverage X)
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace)) :
    IsPerfect (X := X.toRingedSpace) E ↔
      ∀ i, IsPerfect (X := (Y i).toRingedSpace)
        ((derivedPullback (f i).toLRSHom.toShHom).obj E)
```

## Tag 09VA, a lemma

[Tag 09VA](https://stacks.math.columbia.edu/tag/09VA) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_derivedPushforwardOXMod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/DerivedPushforwardPseudoCoherent.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/DerivedPushforwardPseudoCoherent.lean#L116). The attribute's comment: “E m-pseudo-coherent implies Ri\_*E m-pseudo-coherent”. References: SGA 6 III (1.1.1), “necessity: E ⇒ Ri\_*E”.

> **The forward half of Stacks 09VA.** Let `i : Z ⟶ X` be a morphism of ringed spaces whose
> underlying continuous map is a closed immersion and such that `i_*𝒪_Z` is pseudo-coherent as an
> `𝒪_X`-module. If `E ∈ D(𝒪_Z)` is `m`-pseudo-coherent then so is `Ri_*E`.
>
> Pseudo-coherence is local on `X`. Away from the image of `i` the restriction of `Ri_*E` vanishes.
> Around a point `i(z)` of the image, a strictly perfect approximation `𝒫 ⟶ 𝒦|_{i⁻¹U}` of a
> complex `𝒦` representing `E` is pushed forward degreewise along `i|_{i⁻¹U}`; exactness of
> pushforward preserves the two cohomological conditions, `(i|_{i⁻¹U})_*𝒫` is `m`-pseudo-coherent
> because its terms are direct summands of powers of `(i|_{i⁻¹U})_*𝒪` and it is bounded, and the
> target is `(Ri_*E)|_U`. Stacks 08CC part (1) in the form
> `AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_of_approximation` finishes.

```lean
public theorem isPseudoCoherentFrom_derivedPushforwardOXMod
    (hi : Topology.IsClosedEmbedding i.hom.base)
    (hO : IsPseudoCoherent ((DerivedCategory.singleFunctor (OXMod.{u, u} X) 0).obj
      (pushforwardStructureModule i)))
    (m : ℤ) (E : DerivedCategory (OXMod.{u, u} Z)) (hE : IsPseudoCoherentFrom E m) :
    IsPseudoCoherentFrom ((derivedPushforwardOXMod i hi).obj E) m
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_of_derivedPushforwardOXMod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/PushforwardReflectPseudoCoherent.lean, line 372](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/PushforwardReflectPseudoCoherent.lean#L372). The attribute's comment: “Ri\_*E m-pseudo-coherent implies E m-pseudo-coherent”. References: SGA 6 III (1.1.1), “sufficiency: Ri\_*E ⇒ E”.

> **The converse half of Stacks 09VA.** Let `i : Z ⟶ X` be a morphism of ringed spaces whose
> underlying continuous map is a closed embedding and such that `i_*𝒪_Z` is pseudo-coherent as an
> `𝒪_X`-module. If `Ri_*E` is `m`-pseudo-coherent for `E ∈ D(𝒪_Z)` then so is `E`.
>
> Pseudo-coherence is local on `Z`, and the opens `i⁻¹W` for `W` open in `X` are a fundamental
> system of neighbourhoods of a point of `Z`, so it is enough to produce, for each `z`, an open `W`
> of `X` containing `i(z)` on which `E` becomes `m`-pseudo-coherent. Take for `W` an open on which
> the cohomology of `Ri_*E` is bounded above
> (`AlgebraicGeometry.RingedSpace.exists_isZero_homology_gt_derivedRestrict`); then the cohomology
> of `E|_{i⁻¹W}` is bounded above as well, because `i_*` reflects zero objects
> (`AlgebraicGeometry.RingedSpace.isZero_homology_of_isZero_homology_derivedPushforward`), and
> `AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_Q_of_derivedPushforwardOXMod_of_bounded'`
> applies to `i|_{i⁻¹W} : Z|_{i⁻¹W} ⟶ X|_W`.

```lean
public theorem isPseudoCoherentFrom_of_derivedPushforwardOXMod {Z X : RingedSpace.{u, u}}
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u} Z)]
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u} X)]
    [∀ V : Opens X.carrier,
      HasDerivedCategory.{w} (StrictlyPerfect.OXMod.{u, u} (X.restrict V.isOpenEmbedding))]
    [∀ V : Opens Z.carrier,
      HasDerivedCategory.{w} (StrictlyPerfect.OXMod.{u, u} (Z.restrict V.isOpenEmbedding))]
    (i : Z ⟶ X) (hi : Topology.IsClosedEmbedding i.hom.base)
    (hO : IsPseudoCoherent ((DerivedCategory.singleFunctor (StrictlyPerfect.OXMod.{u, u} X) 0).obj
      (pushforwardStructureModule i)))
    (m : ℤ) (E : DerivedCategory (StrictlyPerfect.OXMod.{u, u} Z))
    (hE : IsPseudoCoherentFrom ((derivedPushforwardOXMod i hi).obj E) m) :
    IsPseudoCoherentFrom E m
```

## Tag 09VB, a lemma

[Tag 09VB](https://stacks.math.columbia.edu/tag/09VB) in the Stacks Project.

**`AlgebraicGeometry.isPseudoCoherentFrom_iff_derivedPushforward_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/FinitePushforwardDescent.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/FinitePushforwardDescent.lean#L74).

> Let `f : X ⟶ Y` be a finite morphism of schemes such that `f_*𝒪_X` is pseudo-coherent as an
> `𝒪_Y`-module, that is, such that the object of `D(𝒪_Y)` it determines in degree zero is
> pseudo-coherent in the sense of Stacks 08CB. Let `E` be an object of `D_{QCoh}(𝒪_X)`. Then `E` is
> `m`-pseudo-coherent if and only if `Rf_*E` is `m`-pseudo-coherent.

```lean
theorem isPseudoCoherentFrom_iff_derivedPushforward_of_isFinite {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsFinite f]
    (hf : RingedSpace.IsPseudoCoherent (X := Y.toRingedSpace)
      ((DerivedCategory.singleFunctor Y.Modules 0).obj
        ((Scheme.Modules.pushforward f).obj (SheafOfModules.unit X.ringCatSheaf))))
    (E : DerivedCategory X.Modules)
    (hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj E).IsQuasicoherent)
    (m : ℤ) :
    RingedSpace.IsPseudoCoherentFrom (X := X.toRingedSpace) E m ↔
      RingedSpace.IsPseudoCoherentFrom (X := Y.toRingedSpace)
        ((RingedSpace.derivedPushforward f.toLRSHom.toShHom).obj E) m
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.12, Tag 09UC](https://stacks.math.columbia.edu/tag/09UC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
