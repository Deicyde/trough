---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_opens_isKoszulRegularImmersion_comp_iff, AlgebraicGeometry.KoszulAt, AlgebraicGeometry.IsLocalCompleteIntersectionMorphism, AlgebraicGeometry.isKoszulRegularImmersion_of_koszul, AlgebraicGeometry.perfect_of_isLocalCompleteIntersectionMorphism, AlgebraicGeometry.pseudoCoherent_of_isLocalCompleteIntersectionMorphism, AlgebraicGeometry.locallyOfFinitePresentation_of_isLocalCompleteIntersectionMorphism, AlgebraicGeometry.isLocalCompleteIntersectionMorphism_iff_appTop
statement: formalized
proof: formalized
---

# 37.62 Local complete intersection morphisms

Section 37.62 of the Stacks Project, [Tag 068E](https://stacks.math.columbia.edu/tag/068E). 23 tags here are carried by 42 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 069E, a lemma

[Tag 069E](https://stacks.math.columbia.edu/tag/069E) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_opens_isKoszulRegularImmersion_comp_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothEmbeddingIndependence.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothEmbeddingIndependence.lean#L81).

> **Stacks 069E.** Let `i : U ⟶ P` and `i' : U ⟶ P'` be immersions over `S` of schemes smooth
> over `S`. Then `i` is a Koszul-regular immersion in a neighbourhood of `u : U` if and only if
> `i'` is.

```lean
theorem exists_opens_isKoszulRegularImmersion_comp_iff
    {S U P P' : Scheme.{u}} (f : U ⟶ S) (p : P ⟶ S) (p' : P' ⟶ S)
    (i : U ⟶ P) (i' : U ⟶ P') [IsImmersion i] [IsImmersion i'] [Smooth p] [Smooth p']
    (hi : i ≫ p = f) (hi' : i' ≫ p' = f) (u : U) :
    (∃ V : U.Opens, u ∈ V ∧ IsKoszulRegularImmersion (V.ι ≫ i)) ↔
      ∃ V : U.Opens, u ∈ V ∧ IsKoszulRegularImmersion (V.ι ≫ i')
```

## Tag 069F, a definition

[Tag 069F](https://stacks.math.columbia.edu/tag/069F) in the Stacks Project.

**`AlgebraicGeometry.KoszulAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Defs.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Defs.lean#L66). The attribute's comment: “part (1): Koszul at a point”. References: SGA 6 VIII (1.1), “at a point”.

> **Stacks 069F, part (1).** A morphism of schemes `f : X ⟶ S` is *Koszul at* `x : X` if it is
> of finite type at `x` and there are an open neighbourhood `U` of `x`, a scheme `P` smooth over
> `S` and a Koszul-regular immersion `i : U ⟶ P` through which the restriction of `f` to `U`
> factors.

```lean
def KoszulAt {X S : Scheme.{u}} (f : X ⟶ S) (x : X) : Prop
```

**`AlgebraicGeometry.IsLocalCompleteIntersectionMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Defs.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Defs.lean#L76). The attribute's comment: “part (2): local complete intersection morphism”. References: SGA 6 VIII (1.1).

> **Stacks 069F, part (2).** A *local complete intersection morphism*, also called a *Koszul
> morphism*, is a morphism of schemes that is Koszul at every point of its source.

```lean
def IsLocalCompleteIntersectionMorphism {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

## Tag 069G, a lemma

[Tag 069G](https://stacks.math.columbia.edu/tag/069G) in the Stacks Project.

**`AlgebraicGeometry.isKoszulRegularImmersion_of_koszul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/LocalCompleteIntersectionAffine.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/LocalCompleteIntersectionAffine.lean#L129). References: SGA 6 VIII (1.2).

> **Stacks 069G**, unconditionally: an immersion over `S` of an open of the source of a local
> complete intersection morphism into a scheme smooth over `S` is Koszul-regular.

```lean
theorem isKoszulRegularImmersion_of_koszul {X S P : Scheme.{u}} (f : X ⟶ S) (π : P ⟶ S)
    [Smooth π] (U : X.Opens) (i : U.toScheme ⟶ P) [IsImmersion i]
    (hf : IsLocalCompleteIntersectionMorphism f) (hi : U.ι ≫ f = i ≫ π) :
    IsKoszulRegularImmersion i
```

## Tag 069H, a lemma

[Tag 069H](https://stacks.math.columbia.edu/tag/069H) in the Stacks Project.

**`AlgebraicGeometry.perfect_of_isLocalCompleteIntersectionMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Perfect.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Perfect.lean#L146). The attribute's comment: “part (3): perfect”. References: SGA 6 III (4.1.1); SGA 6 VIII (1.7); SGA 6 X (7.1), “partial”.

> **Stacks 069H, part (3).** A local complete intersection morphism of schemes is perfect.
>
> Perfectness is Zariski-local on the source, and on a neighbourhood of each point the morphism
> factors as a Koszul-regular immersion followed by a smooth morphism; the first is perfect by
> Stacks 068C, the second is flat and locally of finite presentation and hence perfect by
> Stacks 068A, and perfectness is stable under composition by Stacks 0689.

```lean
theorem perfect_of_isLocalCompleteIntersectionMorphism {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : IsLocalCompleteIntersectionMorphism f) : Perfect f
```

**`AlgebraicGeometry.pseudoCoherent_of_isLocalCompleteIntersectionMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Perfect.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Perfect.lean#L161). The attribute's comment: “part (2): pseudo-coherent”. References: SGA 6 VIII (1.7), “partial”.

> **Stacks 069H, part (2).** A local complete intersection morphism of schemes is
> pseudo-coherent, because it is perfect and a perfect morphism is pseudo-coherent.

```lean
theorem pseudoCoherent_of_isLocalCompleteIntersectionMorphism {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : IsLocalCompleteIntersectionMorphism f) : PseudoCoherent f
```

**`AlgebraicGeometry.locallyOfFinitePresentation_of_isLocalCompleteIntersectionMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Perfect.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Perfect.lean#L170). The attribute's comment: “part (1): locally of finite presentation”.

> **Stacks 069H, part (1).** A local complete intersection morphism of schemes is locally of
> finite presentation, because it is pseudo-coherent and a pseudo-coherent morphism is locally of
> finite presentation by Stacks 0682.

```lean
theorem locallyOfFinitePresentation_of_isLocalCompleteIntersectionMorphism
    {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : IsLocalCompleteIntersectionMorphism f) : LocallyOfFinitePresentation f
```

## Tag 07DB, a lemma

[Tag 07DB](https://stacks.math.columbia.edu/tag/07DB) in the Stacks Project.

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_iff_appTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Affine.lean, line 537](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Affine.lean#L537).

> **Stacks 07DB.** A morphism of affine schemes is a local complete intersection morphism
> exactly when the induced homomorphism of the rings of global sections is a local complete
> intersection homomorphism.

```lean
theorem isLocalCompleteIntersectionMorphism_iff_appTop {X S : Scheme.{u}} [IsAffine X]
    [IsAffine S] (f : X ⟶ S) :
    IsLocalCompleteIntersectionMorphism f ↔ f.appTop.hom.IsLocalCompleteIntersection
```

## Tag 069I, a lemma

[Tag 069I](https://stacks.math.columbia.edu/tag/069I) in the Stacks Project.

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/FlatBaseChange.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/FlatBaseChange.lean#L92). References: SGA 6 VIII (1.6), “flat base change stable”.

> A flat base change of a local complete intersection morphism is a local
> complete intersection morphism.

```lean
public theorem isLocalCompleteIntersectionMorphism_pullback_snd
    {X S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) [Flat g]
    (hf : IsLocalCompleteIntersectionMorphism f) :
    IsLocalCompleteIntersectionMorphism (pullback.snd f g)
```

## Tag 069J, a lemma

[Tag 069J](https://stacks.math.columbia.edu/tag/069J) in the Stacks Project.

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Composition.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Composition.lean#L126).

> **Stacks 069J.** A composition of local complete intersection morphisms is a local complete
> intersection morphism.

```lean
theorem isLocalCompleteIntersectionMorphism_comp {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    (hf : IsLocalCompleteIntersectionMorphism f)
    (hg : IsLocalCompleteIntersectionMorphism g) :
    IsLocalCompleteIntersectionMorphism (f ≫ g)
```

## Tag 069K, a lemma

[Tag 069K](https://stacks.math.columbia.edu/tag/069K) in the Stacks Project.

**`AlgebraicGeometry.flat_and_isLocalCompleteIntersectionMorphism_of_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Syntomic.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Syntomic.lean#L118). The attribute's comment: “(2) ⇒ (1): a syntomic morphism is flat and a local complete intersection morphism”.

> **Stacks 069K, the implication (2) ⇒ (1).** A syntomic morphism of schemes is flat and a
> local complete intersection morphism.

```lean
theorem flat_and_isLocalCompleteIntersectionMorphism_of_syntomic {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : Syntomic f) : Flat f ∧ IsLocalCompleteIntersectionMorphism f
```

**`AlgebraicGeometry.syntomic_iff_flat_and_isLocalCompleteIntersectionMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Syntomic.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/Syntomic.lean#L147). The attribute's comment: “the equivalence of (1) and (2)”.

> **Stacks 069K.** A morphism of schemes is syntomic if and only if it is flat and a local
> complete intersection morphism.

```lean
theorem syntomic_iff_flat_and_isLocalCompleteIntersectionMorphism {X S : Scheme.{u}} (f : X ⟶ S) :
    Syntomic f ↔ Flat f ∧ IsLocalCompleteIntersectionMorphism f
```

## Tag 069L, a lemma

[Tag 069L](https://stacks.math.columbia.edu/tag/069L) in the Stacks Project.

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_of_isKoszulRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/RegularImmersion.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/RegularImmersion.lean#L49). The attribute's comment: “Koszul-regular immersion”. References: SGA 5 III (6.8), “Direction”.

> **Stacks 069L.** A Koszul-regular immersion of schemes is a local complete intersection
> morphism.

```lean
theorem isLocalCompleteIntersectionMorphism_of_isKoszulRegularImmersion {X S : Scheme.{u}}
    (i : X ⟶ S) [IsImmersion i] (hi : IsKoszulRegularImmersion i) :
    IsLocalCompleteIntersectionMorphism i
```

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_of_isRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/RegularImmersion.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/RegularImmersion.lean#L68). The attribute's comment: “regular immersion”. References: SGA 5 III (6.8), “Direction”.

> **Stacks 069L.** A regular immersion of schemes is a local complete intersection
> morphism.

```lean
theorem isLocalCompleteIntersectionMorphism_of_isRegularImmersion {X S : Scheme.{u}}
    (i : X ⟶ S) [IsImmersion i] (hi : IsRegularImmersion i) :
    IsLocalCompleteIntersectionMorphism i
```

## Tag 069M, a lemma

[Tag 069M](https://stacks.math.columbia.edu/tag/069M) in the Stacks Project.

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_of_comp_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/SmoothTarget.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/SmoothTarget.lean#L75).

> **Stacks 069M.**  In a commutative triangle of morphisms of schemes with `g : Y ⟶ S` smooth,
> if the composite `f ≫ g` is a local complete intersection morphism then so is `f : X ⟶ Y`.

```lean
theorem isLocalCompleteIntersectionMorphism_of_comp_of_smooth {X Y S : Scheme.{u}} (f : X ⟶ Y)
    (g : Y ⟶ S) [Smooth g] (h : IsLocalCompleteIntersectionMorphism (f ≫ g)) :
    IsLocalCompleteIntersectionMorphism f
```

## Tag 0E9K, a lemma

[Tag 0E9K](https://stacks.math.columbia.edu/tag/0E9K) in the Stacks Project.

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/RegularSchemes.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/RegularSchemes.lean#L77).

> A morphism of schemes which is locally of finite type and whose source and target are
> regular is a local complete intersection morphism.

```lean
theorem isLocalCompleteIntersectionMorphism_of_isRegular {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] (hX : IsRegular X) (hY : IsRegular Y) :
    IsLocalCompleteIntersectionMorphism f
```

## Tag 09RL, a lemma

[Tag 09RL](https://stacks.math.columbia.edu/tag/09RL) in the Stacks Project.

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/PerfectOverBase.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/PerfectOverBase.lean#L301). The attribute's comment: “the morphism to the intermediate scheme is a local complete intersection morphism”.

> **Stacks 09RL, the relative conclusion.**  Let `X ⟶ Y ⟶ S` be a commutative triangle of
> morphisms of schemes with `S` locally Noetherian and `Y ⟶ S` locally of finite type.  If
> `f : X ⟶ Y` is perfect and `X ⟶ S` is a local complete intersection morphism, then `f` is a local
> complete intersection morphism.

```lean
theorem isLocalCompleteIntersectionMorphism_of_perfect {X Y S : Scheme.{u}} (f : X ⟶ Y)
    (g : Y ⟶ S) {h : X ⟶ S} (hcomm : f ≫ g = h) [IsLocallyNoetherian S] [LocallyOfFiniteType g]
    [AlgebraicGeometry.Perfect f] (hh : IsLocalCompleteIntersectionMorphism h) :
    IsLocalCompleteIntersectionMorphism f
```

**`AlgebraicGeometry.koszulAt_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/PerfectOverBase.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/PerfectOverBase.lean#L310). The attribute's comment: “the intermediate scheme is Koszul over the base at every point of the image”.

> **Stacks 09RL, the conclusion on the base.**  In the same situation, `g : Y ⟶ S` is Koszul at
> the image of every point of `X`.

```lean
theorem koszulAt_of_perfect {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S) {h : X ⟶ S}
    (hcomm : f ≫ g = h) [IsLocallyNoetherian S] [LocallyOfFiniteType g]
    [AlgebraicGeometry.Perfect f] (hh : IsLocalCompleteIntersectionMorphism h) (x : X) :
    KoszulAt g (f.base x)
```

## Tag 0FJ2, a lemma

[Tag 0FJ2](https://stacks.math.columbia.edu/tag/0FJ2) in the Stacks Project.

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_of_isRegular_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/RegularTarget.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/RegularTarget.lean#L54). The attribute's comment: “f is a local complete intersection morphism”.

> Let `X ⟶ Y ⟶ S` be a commutative triangle of morphisms of schemes with `S` locally
> Noetherian, `Y ⟶ S` locally of finite type and `Y` regular. If `X ⟶ S` is a local complete
> intersection morphism, then so is `f : X ⟶ Y`.

```lean
theorem isLocalCompleteIntersectionMorphism_of_isRegular_target {X Y S : Scheme.{u}} (f : X ⟶ Y)
    (g : Y ⟶ S) {h : X ⟶ S} (hcomm : f ≫ g = h) [IsLocallyNoetherian S] [LocallyOfFiniteType g]
    (hY : IsRegular Y) (hh : IsLocalCompleteIntersectionMorphism h) :
    IsLocalCompleteIntersectionMorphism f
```

**`AlgebraicGeometry.koszulAt_of_isRegular_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/RegularTarget.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/RegularTarget.lean#L66). The attribute's comment: “Y ⟶ S is Koszul at the image of every point of X”.

> Let `X ⟶ Y ⟶ S` be a commutative triangle of morphisms of schemes with `S` locally
> Noetherian, `Y ⟶ S` locally of finite type and `Y` regular. If `X ⟶ S` is a local complete
> intersection morphism, then `g : Y ⟶ S` is Koszul at the image of every point of `X`.

```lean
theorem koszulAt_of_isRegular_target {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S) {h : X ⟶ S}
    (hcomm : f ≫ g = h) [IsLocallyNoetherian S] [LocallyOfFiniteType g] (hY : IsRegular Y)
    (hh : IsLocalCompleteIntersectionMorphism h) (x : X) : KoszulAt g (f.base x)
```

## Tag 0FK1, a lemma

[Tag 0FK1](https://stacks.math.columbia.edu/tag/0FK1) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isRegularImmersion_of_perfect_of_conormalSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/PerfectLocallyFreeConormal.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/PerfectLocallyFreeConormal.lean#L354).

> **Stacks tag 0FK1.**  An immersion `i : X ⟶ Y` which is perfect, whose target is locally
> Noetherian and whose conormal sheaf is finite locally free, is a regular immersion.

```lean
theorem isRegularImmersion_of_perfect_of_conormalSheaf (i : X ⟶ Y) [IsImmersion i]
    [AlgebraicGeometry.Perfect i] [IsLocallyNoetherian Y]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
      (Stacks.Conormal.conormalSheaf i)] :
    IsRegularImmersion i
```

## Tag 0FV6, a lemma

[Tag 0FV6](https://stacks.math.columbia.edu/tag/0FV6) in the Stacks Project.

**`AlgebraicGeometry.isPerfect_and_hasTorAmplitude_naiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean#L454). The attribute's comment: “both halves: NL_{X/Y} of a local complete intersection morphism is perfect and has tor-amplitude in [-1,0]”. References: SGA 6 VIII (2.4), “more general”; SGA 6 XIV (2.1).

> **Stacks 0FV6.** The naive cotangent complex of a local complete intersection morphism is a
> perfect object of `D(𝒪_X)` of Tor amplitude in `[-1, 0]`.
>
> Near a point of the source the morphism restricts to a morphism of affine schemes whose map on
> sections is a local complete intersection homomorphism, and there `NL_{X/Y}` is the derived
> pullback of the derived sheafification of the naive cotangent complex of that homomorphism; both
> conditions hold on it by Stacks 0FV0 and descend to the restriction by Stacks 08E9 and Stacks
> 08EB. Both conditions are local on the source, so they hold on `X`.

```lean
theorem isPerfect_and_hasTorAmplitude_naiveCotangentComplex {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : IsLocalCompleteIntersectionMorphism f) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace)
        (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
      Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
        (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0
```

## Tag 0FK2, a lemma

[Tag 0FK2](https://stacks.math.columbia.edu/tag/0FK2) in the Stacks Project.

**`AlgebraicGeometry.hasTorAmplitude_naiveCotangentComplex_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean#L500). The attribute's comment: “(1) ⇒ (2): for a perfect morphism of locally Noetherian schemes which is a local complete intersection morphism, NL_{X/Y} has tor-amplitude in [-1,0]”.

> **Stacks 0FK2, the implication (1) ⇒ (2).** If a perfect morphism of locally Noetherian
> schemes is a local complete intersection morphism, then `NL_{X/Y}` has Tor amplitude in
> `[-1, 0]`.
>
> The three standing hypotheses are not used: Tor amplitude in `[-1, 0]` holds for the naive
> cotangent complex of any local complete intersection morphism.

```lean
theorem hasTorAmplitude_naiveCotangentComplex_of_perfect {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsLocallyNoetherian X] [IsLocallyNoetherian Y] [Perfect f]
    (hf : IsLocalCompleteIntersectionMorphism f) :
    Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
      (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0
```

**`AlgebraicGeometry.isPerfect_and_hasTorAmplitude_naiveCotangentComplex_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean#L517). The attribute's comment: “(1) ⇒ (3): for a perfect morphism of locally Noetherian schemes which is a local complete intersection morphism, NL_{X/Y} is perfect with tor-amplitude in [-1,0]”. References: SGA 6 VIII (2.4), “partial”; SGA 6 XIV (2.1), “special case”.

> **Stacks 0FK2, the implication (1) ⇒ (3).** If a perfect morphism of locally Noetherian
> schemes is a local complete intersection morphism, then `NL_{X/Y}` is perfect with Tor amplitude
> in `[-1, 0]`.
>
> The three standing hypotheses are not used: both conditions hold for the naive cotangent complex
> of any local complete intersection morphism.

```lean
theorem isPerfect_and_hasTorAmplitude_naiveCotangentComplex_of_perfect {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsLocallyNoetherian X] [IsLocallyNoetherian Y] [Perfect f]
    (hf : IsLocalCompleteIntersectionMorphism f) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace)
        (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
      Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
        (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0
```

**`AlgebraicGeometry.naiveCotangentComplex_tfae_isLocalCompleteIntersectionMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangentConverse.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangentConverse.lean#L225). References: SGA 6 VIII (2.4), “partial”; SGA 6 XIV (2.1), “(1) ⇒ (3), special case”.

> **Stacks 0FK2.** Let `f : X ⟶ Y` be a perfect morphism of locally Noetherian schemes. The
> following are equivalent:
>
> 1. `f` is a local complete intersection morphism;
> 2. `NL_{X/Y}` has Tor amplitude in `[-1, 0]`;
> 3. `NL_{X/Y}` is perfect with Tor amplitude in `[-1, 0]`.
>
> Here `NL_{X/Y}` is `AlgebraicGeometry.Scheme.naiveCotangentComplex`, Stacks 0D0H, read at its
> class in `D(𝒪_X)`; Tor amplitude is `Stacks.Cohomology.TorAmplitude.HasTorAmplitude`, Stacks
> 08CG, taken against the canonical derived tensor product of a ringed space, and perfectness is
> `Stacks.Cohomology.PerfectComplexes.IsPerfect`, Stacks 08CM. Both are stated at the underlying
> ringed space of `X`, with the standard derived category, as they are for Stacks 08E9 and Stacks
> 08EB.
>
> Rendered on sections over a compatible pair of affine opens the statement is Stacks 0FJT; the
> translation is Stacks 07DB and Stacks 0D0I together with Stacks 08E9 and Stacks 08EB.

```lean
theorem naiveCotangentComplex_tfae_isLocalCompleteIntersectionMorphism {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsLocallyNoetherian X] [IsLocallyNoetherian Y] [Perfect f] :
    List.TFAE
      [IsLocalCompleteIntersectionMorphism f,
        Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0,
        Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace)
            (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
          Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
            (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0]
```

## Tag 0FK3, a lemma

[Tag 0FK3](https://stacks.math.columbia.edu/tag/0FK3) in the Stacks Project.

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_iff_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean#L132). The attribute's comment: “(1) ⇔ (2): a flat morphism of finite presentation is a local complete intersection morphism iff it is syntomic”.

> **Stacks 0FK3, the equivalence of (1) and (2).** A flat morphism of finite presentation is a
> local complete intersection morphism exactly when it is syntomic.
>
> Finite presentation is a standing hypothesis of the source and is not used: the equivalence holds
> for any flat morphism, by Stacks 069K.

```lean
theorem isLocalCompleteIntersectionMorphism_iff_syntomic {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Flat f] (_hfp : FinitePresentation f) :
    IsLocalCompleteIntersectionMorphism f ↔ Syntomic f
```

**`AlgebraicGeometry.hasTorAmplitude_naiveCotangentComplex_of_isPerfect_of_hasTorAmplitude`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean#L149). The attribute's comment: “(4) ⇒ (3), which is a projection: NL_{X/Y} perfect with tor-amplitude in [-1,0] has tor-amplitude in [-1,0]. Fixes which library predicates conditions (3) and (4) are read at”.

> **Stacks 0FK3, the implication (4) ⇒ (3).** If `NL_{X/Y}` is perfect with Tor amplitude in
> `[-1, 0]`, then it has Tor amplitude in `[-1, 0]`.
>
> The implication is a projection, as it is in the source. The declaration's purpose is to pin
> conditions (3) and (4) of the tag to `Stacks.Cohomology.TorAmplitude.HasTorAmplitude` of Stacks
> 08CG, taken against the canonical derived tensor product of Stacks 06YU, and to
> `Stacks.Cohomology.PerfectComplexes.IsPerfect` of Stacks 08CM; the tree carries several further
> spellings of each. The tag's standing hypotheses are not needed, so the statement is made for an
> arbitrary morphism of schemes.

```lean
theorem hasTorAmplitude_naiveCotangentComplex_of_isPerfect_of_hasTorAmplitude
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace)
        (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
      Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
        (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0) :
    Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
      (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0
```

**`AlgebraicGeometry.hasTorAmplitude_naiveCotangentComplex_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean, line 470](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean#L470). The attribute's comment: “(1) ⇒ (3): for a flat morphism of finite presentation which is a local complete intersection morphism, NL_{X/Y} has tor-amplitude in [-1,0]”.

> **Stacks 0FK3, the implication (1) ⇒ (3).** If a flat morphism of finite presentation is a
> local complete intersection morphism, then `NL_{X/Y}` has Tor amplitude in `[-1, 0]`.
>
> The two standing hypotheses are not used: Tor amplitude in `[-1, 0]` holds for the naive
> cotangent complex of any local complete intersection morphism.

```lean
theorem hasTorAmplitude_naiveCotangentComplex_of_flat {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Flat f] (_hfp : FinitePresentation f) (hf : IsLocalCompleteIntersectionMorphism f) :
    Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
      (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0
```

**`AlgebraicGeometry.isPerfect_and_hasTorAmplitude_naiveCotangentComplex_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean#L483). The attribute's comment: “(1) ⇒ (4): for a flat morphism of finite presentation which is a local complete intersection morphism, NL_{X/Y} is perfect with tor-amplitude in [-1,0]”.

> **Stacks 0FK3, the implication (1) ⇒ (4).** If a flat morphism of finite presentation is a
> local complete intersection morphism, then `NL_{X/Y}` is perfect with Tor amplitude in `[-1, 0]`.
>
> The two standing hypotheses are not used: both conditions hold for the naive cotangent complex
> of any local complete intersection morphism.

```lean
theorem isPerfect_and_hasTorAmplitude_naiveCotangentComplex_of_flat {X Y : Scheme.{u}}
    (f : X ⟶ Y) [Flat f] (_hfp : FinitePresentation f)
    (hf : IsLocalCompleteIntersectionMorphism f) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace)
        (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
      Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
        (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0
```

**`AlgebraicGeometry.syntomic_of_hasTorAmplitude_naiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean#L536). The attribute's comment: “(3) ⇒ (2): a flat morphism of finite presentation whose naive cotangent complex has tor-amplitude in [-1,0] is syntomic”.

> **Stacks 0FK3, the implication (3) ⇒ (2).** A flat morphism of finite presentation whose
> naive cotangent complex has Tor amplitude in `[-1, 0]` is syntomic.
>
> Syntomicity is a condition at each point of the source, asking for affine opens `V ∋ x` of `X`
> and `U` of `Y` with `V ⊆ f⁻¹(U)` over which the morphism is syntomic on sections. On such a pair
> the hypothesis descends to Tor amplitude in `[-1, 0]` of `NL_{Γ(X, V)/Γ(Y, U)}` in
> `D(Γ(X, V))`, and `Γ(Y, U) → Γ(X, V)` is flat of finite presentation, so Stacks 0FJV makes it
> syntomic. Quasi-compactness and quasi-separatedness are not used.

```lean
theorem syntomic_of_hasTorAmplitude_naiveCotangentComplex {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Flat f] (hfp : FinitePresentation f)
    (hamp : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
      (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0) :
    Syntomic f
```

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_of_hasTorAmplitude_naiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean#L560). The attribute's comment: “(3) ⇒ (1): a flat morphism of finite presentation whose naive cotangent complex has tor-amplitude in [-1,0] is a local complete intersection morphism”.

> **Stacks 0FK3, the implication (3) ⇒ (1).** A flat morphism of finite presentation whose
> naive cotangent complex has Tor amplitude in `[-1, 0]` is a local complete intersection
> morphism: it is syntomic, and a syntomic morphism is Koszul by Stacks 069K.

```lean
theorem isLocalCompleteIntersectionMorphism_of_hasTorAmplitude_naiveCotangentComplex
    {X Y : Scheme.{u}} (f : X ⟶ Y) [Flat f] (hfp : FinitePresentation f)
    (hamp : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
      (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0) :
    IsLocalCompleteIntersectionMorphism f
```

**`AlgebraicGeometry.naiveCotangentComplex_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/NaiveCotangent.lean#L572).

> **Stacks 0FK3.** For a flat morphism of finite presentation `f : X ⟶ Y` the following are
> equivalent: `f` is a local complete intersection morphism; `f` is syntomic; `NL_{X/Y}` has Tor
> amplitude in `[-1, 0]`; `NL_{X/Y}` is perfect with Tor amplitude in `[-1, 0]`.

```lean
theorem naiveCotangentComplex_tfae {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Flat f] (hfp : FinitePresentation f) :
    List.TFAE
      [IsLocalCompleteIntersectionMorphism f,
        Syntomic f,
        Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0,
        Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace)
            (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
          Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
            (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0]
```

## Tag 0FDP, a lemma

[Tag 0FDP](https://stacks.math.columbia.edu/tag/0FDP) in the Stacks Project.

**`AlgebraicGeometry.smooth_tfae_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/SmoothDiagonal.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/SmoothDiagonal.lean#L331). References: SGA 1 II (4.18), “(1) ⇒ (2), special case”; SGA 6 VII (1.10), “special case”.

> **Stacks 0FDP.** Let `f : X ⟶ Y` be a morphism of finite type between locally Noetherian
> schemes and let `Δ : X ⟶ X ×_Y X` be its diagonal. The following are equivalent:
>
> 1. `f` is smooth;
> 2. `f` is flat and `Δ` is a regular immersion;
> 3. `f` is flat and `Δ` is a local complete intersection morphism;
> 4. `f` is flat and `Δ` is perfect.
>
> A smooth morphism is flat and its diagonal is a section of the smooth first projection, hence a
> regular immersion by Stacks 067R; a regular immersion is a local complete intersection morphism
> by Stacks 069L; such a morphism is perfect by Stacks 069H; and the interesting implication back
> to smoothness is `AlgebraicGeometry.smooth_of_flat_of_perfect_diagonal`, which runs Stacks 0FCX
> on affine charts.

```lean
theorem smooth_tfae_diagonal {X Y : Scheme.{u}} (f : X ⟶ Y) [IsLocallyNoetherian X]
    [IsLocallyNoetherian Y] [LocallyOfFiniteType f] [QuasiCompact f] :
    List.TFAE
      [Smooth f,
        Flat f ∧ Stacks.AlgebraicGeometry.RegularIdealSheaf.IsRegularImmersion
          (pullback.diagonal f),
        Flat f ∧ IsLocalCompleteIntersectionMorphism (pullback.diagonal f),
        Flat f ∧ Perfect (pullback.diagonal f)]
```

## Tag 069N, a lemma

[Tag 069N](https://stacks.math.columbia.edu/tag/069N) in the Stacks Project.

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_isLocalAtTarget_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/FpqcLocalAtTarget.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/FpqcLocalAtTarget.lean#L118). References: SGA 2 XII (4.10), “partial”.

> **Stacks 069N.** Being a local complete intersection morphism of schemes is fpqc local on the
> target: a morphism is Koszul if and only if its base change along every member of an fpqc
> covering of its target is Koszul.

```lean
theorem isLocalCompleteIntersectionMorphism_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (@IsLocalCompleteIntersectionMorphism : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 069P, a lemma

[Tag 069P](https://stacks.math.columbia.edu/tag/069P) in the Stacks Project.

**`AlgebraicGeometry.isLocalAtSource_syntomic_isLocalCompleteIntersectionMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/LocalCompleteIntersectionAffine.lean, line 1044](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/LocalCompleteIntersectionAffine.lean#L1044).

> **Stacks 069P.** The property of being a local complete intersection morphism of schemes is
> syntomic local on the source: a morphism is Koszul exactly when its composites with the members
> of a syntomic covering of its source are.
>
> All four inputs of the syntomic case of Stacks 036H are supplied: Zariski locality on the source
> and on the target and preservation under precomposition with a syntomic morphism come from
> `StacksFrontier.AlgebraicGeometry.Descent.LocalOnSourceTopologies.LocalCompleteIntersection`, and
> the affine descent is
> `AlgebraicGeometry.isLocalCompleteIntersectionMorphism_of_surjective_syntomic_of_isAffine`.

```lean
theorem isLocalAtSource_syntomic_isLocalCompleteIntersectionMorphism :
    MorphismProperty.IsLocalAtSource
      (@IsLocalCompleteIntersectionMorphism.{u} : MorphismProperty Scheme.{u})
      (Scheme.precoverage (@Syntomic.{u}))
```

**`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_isLocalAtSource_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/LocalCompleteIntersectionEtale.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/LocalCompleteIntersectionEtale.lean#L163). The attribute's comment: “the étale case, unconditionally: the Koszul property of morphisms of schemes is local on the source for the étale topology. The syntomic statement of the tag is not claimed here”.

> **Stacks 069P, restricted to étale coverings.** The property of being a local complete
> intersection morphism of schemes is local on the source for the étale topology: a morphism is
> Koszul exactly when its composites with the members of an étale covering of its source are.
>
> All four inputs of the étale case of Stacks 036H are available: Zariski locality on the source
> and on the target come from
> `StacksFrontier.AlgebraicGeometry.Descent.LocalOnSourceTopologies.LocalCompleteIntersection`,
> preservation under precomposition with an étale morphism is
> `AlgebraicGeometry.respectsLeft_etale_isLocalCompleteIntersectionMorphism`, and the affine
> descent is
> `AlgebraicGeometry.isLocalCompleteIntersectionMorphism_of_surjective_smooth_of_isAffine` read at
> an étale `g`.

```lean
theorem isLocalCompleteIntersectionMorphism_isLocalAtSource_etale :
    MorphismProperty.IsLocalAtSource
      (@IsLocalCompleteIntersectionMorphism.{u} : MorphismProperty Scheme.{u})
      Scheme.etalePrecoverage
```

## Tag 06B8, a lemma

[Tag 06B8](https://stacks.math.columbia.edu/tag/06B8) in the Stacks Project.

**`AlgebraicGeometry.isOpen_koszulAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/KoszulLocus.lean, line 868](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/KoszulLocus.lean#L868). The attribute's comment: “the Koszul locus is open”.

> **The Koszul locus is open.** A witness for `KoszulAt f x` — an open `U ∋ x` on which `f`
> factors through a Koszul-regular immersion into a scheme smooth over the target — witnesses
> `KoszulAt f z` for every `z` in `U`, because Koszul-regularity is a condition on the immersion
> and not on the point. Intersecting `U` with the affine open witnessing finite type at `x` gives
> a neighbourhood of `x` inside the locus.

```lean
public theorem isOpen_koszulAt {X Y : Scheme.{u}} (f : X ⟶ Y) :
    IsOpen {x : X | KoszulAt f x}
```

**`AlgebraicGeometry.koszulAt_baseChange_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/KoszulLocus.lean, line 882](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/KoszulLocus.lean#L882). The attribute's comment: “formation of the Koszul locus commutes with arbitrary base change”.

> **The formation of the Koszul locus commutes with arbitrary base change.** Let `f : X ⟶ Y`
> be a morphism of schemes over `S` with `X` and `Y` both flat and locally of finite presentation
> over `S`. For any `g : S' ⟶ S`, the base change of `f` is Koszul at a point of `X ×_S S'`
> exactly when `f` is Koszul at its image in `X`.

```lean
public theorem koszulAt_baseChange_iff {X Y S S' : Scheme.{u}} (f : X ⟶ Y) (p : X ⟶ S)
    (q : Y ⟶ S) (h : f ≫ q = p) [Flat p] [Flat q] [LocallyOfFinitePresentation p]
    [LocallyOfFinitePresentation q] (g : S' ⟶ S) (x' : (pullback p g : Scheme.{u})) :
    KoszulAt (pullback.map p g q g f (𝟙 _) (𝟙 _)
        (by simpa only [Category.comp_id] using h.symm) (by simp)) x' ↔
      KoszulAt f ((pullback.fst p g).base x')
```

## Tag 06B9, a lemma

[Tag 06B9](https://stacks.math.columbia.edu/tag/06B9) in the Stacks Project.

**`AlgebraicGeometry.unramified_iff_formallyUnramified_of_isLocalCompleteIntersectionMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/UnramifiedConormal.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/UnramifiedConormal.lean#L84). The attribute's comment: “the equivalence: a local complete intersection morphism is unramified if and only if it is formally unramified”.

> A local complete intersection morphism of schemes is unramified if and only if it is
> formally unramified.

```lean
theorem unramified_iff_formallyUnramified_of_isLocalCompleteIntersectionMorphism
    {X S : Scheme.{u}} {f : X ⟶ S} (hf : IsLocalCompleteIntersectionMorphism f) :
    Unramified f ↔ FormallyUnramified f
```

**`AlgebraicGeometry.isFiniteLocallyFree_universalConormalSheaf_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/UnramifiedConormal.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/UnramifiedConormal.lean#L158). The attribute's comment: “finite local freeness of the conormal sheaf of a local complete intersection morphism. Tag 063H is NOT needed: the Koszul-regular factor is quasi-regular, and condition (2) of Tag 063M is available for those”.

> The conormal sheaf of a formally unramified local complete intersection morphism of schemes
> is finite locally free.

```lean
theorem isFiniteLocallyFree_universalConormalSheaf_of_isLocalCompleteIntersection
    {X S : Scheme.{u}} (f : X ⟶ S) [FormallyUnramified f]
    (hf : IsLocalCompleteIntersectionMorphism f) :
    SheafOfModules.IsFiniteLocallyFree.{u, u, u} (universalConormalSheaf f)
```

## Tag 06BA, a lemma

[Tag 06BA](https://stacks.math.columbia.edu/tag/06BA) in the Stacks Project.

**`Stacks.Thickenings.mono_transitivityConormalLeftMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormalShortExact.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormalShortExact.lean#L200). The attribute's comment: “the left arrow of the sequence of Stacks 06AE is a monomorphism”.

> **The first arrow of the conormal sequence of part (2) of [Stacks Project, Tag 06AE] is a
> monomorphism** when `Z ⟶ Y` is a local complete intersection morphism.

```lean
theorem mono_transitivityConormalLeftMap (hi : IsLocalCompleteIntersectionMorphism i) :
    Mono (transitivityConormalLeftMap i p tZ tY)
```

**`Stacks.Thickenings.transitivityConormalShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormalShortExact.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormalShortExact.lean#L241). The attribute's comment: “the conormal sequence of Stacks 06AE is short exact”. References: SGA 6 VIII (2.6), “partial”.

> Let `Z --i--→ Y --p--→ X` be morphisms of schemes with universal first-order thickenings
> `Z ⊂ Z'` of `Z` over `X` and `Y ⊂ Y'` of `Y` over `X`, and assume `i` is a local complete
> intersection morphism. Then the conormal sequence
> ```
> 0 ⟶ i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y} ⟶ 0
> ```
> of part (2) of [Stacks Project, Tag 06AE] is **short exact**: its left arrow is a monomorphism,
> it is exact at the middle term, and its right arrow is an epimorphism.

```lean
theorem transitivityConormalShortComplex_shortExact
    (hi : IsLocalCompleteIntersectionMorphism i) :
    (transitivityConormalShortComplex i p tZ tY).ShortExact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.62, Tag 068E](https://stacks.math.columbia.edu/tag/068E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
