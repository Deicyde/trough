---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsBirational, AlgebraicGeometry.Space.isDominant_of_isBirational, AlgebraicGeometry.Space.isIso_pullback_snd_fromGenericStalk_of_isBirational, AlgebraicGeometry.Space.exists_dense_isOpenSubspace_isIso_of_isBirational, AlgebraicGeometry.Space.exists_isDenseOpenSubspace_isIso_pullback_snd_of_isBirational, AlgebraicGeometry.Space.isDecentSpace_pullback_of_isEtale, AlgebraicGeometry.Space.finite_irreducibleComponents_pullback_of_isEtale, AlgebraicGeometry.Space.isBirational_pullback_snd_of_isEtale
statement: formalized
proof: formalized
---

# 68.22 Birational morphisms

Section 68.22 of the Stacks Project, [Tag 0ACU](https://stacks.math.columbia.edu/tag/0ACU). 9 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ACV, a definition

[Tag 0ACV](https://stacks.math.columbia.edu/tag/0ACV) in the Stacks Project.

**`AlgebraicGeometry.Space.IsBirational`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalMorphism/IsBirational.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalMorphism/IsBirational.lean#L605). References: EGA I (2.2.9), “more general”.

> **Stacks 0ACV.** A morphism of decent algebraic spaces with finitely many irreducible
> components is birational when it bijects the generic points of the irreducible components and
> induces isomorphisms on their schematic-locus local rings.

```lean
def IsBirational
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (hdecX : IsDecentSpace B S hS X)
    (hdecY : IsDecentSpace B S hS Y)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (hfiniteY : (letI := pointTopology B S hS Y
      (irreducibleComponents (points B S hS Y)).Finite))
    (f : X ⟶ Y) : Prop
```

## Tag 0ACW, a lemma

[Tag 0ACW](https://stacks.math.columbia.edu/tag/0ACW) in the Stacks Project.

**`AlgebraicGeometry.Space.isDominant_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/BirationalDominant.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/BirationalDominant.lean#L57). References: EGA I (2.2.9), “more general”.

> **Stacks 0ACW.** A birational morphism of decent algebraic spaces over `S` with finitely
> many irreducible components is dominant: it maps the generic points of the irreducible
> components of the source onto those of the target, and those are dense in a quasi-sober
> space.

```lean
theorem isDominant_of_isBirational (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (hdecX : IsDecentSpace B S hS X)
    (hdecY : IsDecentSpace B S hS Y)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (hfiniteY : (letI := pointTopology B S hS Y
      (irreducibleComponents (points B S hS Y)).Finite))
    {f : X ⟶ Y}
    (hf : IsBirational B S hS hX hY hdecX hdecY hfiniteX hfiniteY f) :
    IsDominant B S hS f
```

## Tag 0BBD, a lemma

[Tag 0BBD](https://stacks.math.columbia.edu/tag/0BBD) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_pullback_snd_fromGenericStalk_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalGenericStalk.lean, line 817](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalGenericStalk.lean#L817).

> **Stacks 0BBD.** A birational morphism of decent algebraic spaces with finitely many
> irreducible components becomes an isomorphism after base change to the spectrum of the local
> ring of the target at a generic point.

```lean
theorem isIso_pullback_snd_fromGenericStalk_of_isBirational
    (hdecentY : IsDecentSpace B S hS Y)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hdecentX : IsDecentSpace B S hS X)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (f : X ⟶ Y)
    (hf : IsBirational B S hS hX hY hdecentX hdecentY hfiniteX hfiniteY f) :
    IsIso (pullback.snd f (fromGenericStalk B S hS hY
      (hasDenseRepresentableOpenSubspace_of_isDecentSpace B S hS hY hdecentY)
      hfiniteY y hy))
```

## Tag 0BBE, a lemma

[Tag 0BBE](https://stacks.math.columbia.edu/tag/0BBE) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_dense_isOpenSubspace_isIso_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalDenseOpenIso.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalDenseOpenIso.lean#L405).

> **Stacks 0BBE.** A birational morphism of decent algebraic spaces over `S` with finitely
> many irreducible components restricts to an isomorphism between dense open subspaces, provided
> it is locally of finite type with reduced target or locally of finite presentation.
>
> The source reduces the statement to schemes and quotes Stacks 0BAC there; the reduction is
> carried out on representable open charts with dense point sets, see the module docstring.

```lean
theorem exists_dense_isOpenSubspace_isIso_of_isBirational
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hdecentX : IsDecentSpace B S hS X) (hdecentY : IsDecentSpace B S hS Y)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (hfiniteY : (letI := pointTopology B S hS Y
      (irreducibleComponents (points B S hS Y)).Finite))
    (f : X ⟶ Y)
    (hbir : IsBirational B S hS hX hY hdecentX hdecentY hfiniteX hfiniteY f)
    (hfin : (IsLocallyOfFiniteType B S hS f ∧
        HasEtaleLocalProperty B S hS Y
          (fun Z : Scheme.{u} => _root_.AlgebraicGeometry.IsReduced Z)) ∨
      IsLocallyOfFinitePresentation B S hS f) :
    ∃ (U : Subfunctor X) (V : Subfunctor Y) (ψ : U.toFunctor ⟶ V.toFunctor),
      IsOpenSubspace B S hS U ∧ IsOpenSubspace B S hS V ∧
        DenseRange (pointsMap B S hS U.toFunctor U.ι) ∧
        DenseRange (pointsMap B S hS V.toFunctor V.ι) ∧
        ψ ≫ V.ι = U.ι ≫ f ∧ IsIso ψ
```

## Tag 0BBF, a lemma

[Tag 0BBF](https://stacks.math.columbia.edu/tag/0BBF) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isDenseOpenSubspace_isIso_pullback_snd_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalIsoOverDenseOpen.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalIsoOverDenseOpen.lean#L262).

> **Stacks 0BBF.** Let `f : X ⟶ Y` be a birational morphism of algebraic spaces over a
> scheme `S` which are decent and have finitely many irreducible components. Assume that `f` is
> quasi-compact or separated, and that `f` is locally of finite type with `Y` reduced or locally
> of finite presentation. Then there is a dense open subspace `V ⊂ Y` such that `f^{-1}(V) ⟶ V`
> is an isomorphism.
>
> The source shrinks `Y` to a dense open over which `f` is finite, by Stacks 0BBC, and
> separately to a dense open over which `f` restricts to an isomorphism of dense opens, by
> Stacks 0BBE; the intersection of the two is the open subspace produced here. See the module
> docstring.

```lean
theorem exists_isDenseOpenSubspace_isIso_pullback_snd_of_isBirational
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hdecentX : IsDecentSpace B S hS X) (hdecentY : IsDecentSpace B S hS Y)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (hfiniteY : (letI := pointTopology B S hS Y
      (irreducibleComponents (points B S hS Y)).Finite))
    (f : X ⟶ Y)
    (hbir : IsBirational B S hS hX hY hdecentX hdecentY hfiniteX hfiniteY f)
    (hqc_or_sep : IsQuasiCompact B S hS f ∨ IsSeparated B S hS f)
    (hfin : (IsLocallyOfFiniteType B S hS f ∧
        HasEtaleLocalProperty B S hS Y
          (fun Z : Scheme.{u} => _root_.AlgebraicGeometry.IsReduced Z)) ∨
      IsLocallyOfFinitePresentation B S hS f) :
    ∃ V : Subfunctor Y,
      IsOpenSubspace B S hS V ∧
        Dense (Set.range (pointsMap B S hS V.toFunctor V.ι)) ∧
          IsIso (pullback.snd f V.ι)
```

## Tag 0B4D, a lemma

[Tag 0B4D](https://stacks.math.columbia.edu/tag/0B4D) in the Stacks Project.

**`AlgebraicGeometry.Space.isDecentSpace_pullback_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalEtaleLocalization.lean, line 562](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalEtaleLocalization.lean#L562). The attribute's comment: “decent”.

> **Stacks 0B4D, decency.** The base change of a decent algebraic space along an étale
> morphism from a representable presheaf is decent.

```lean
theorem isDecentSpace_pullback_of_isEtale
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hdecentX : IsDecentSpace B S hS X)
    (V : BigFppfOver B S hS)
    (f : X ⟶ Y) (g : yoneda.obj V ⟶ Y) (hg : IsEtale B S hS g) :
    IsDecentSpace B S hS (pullback f g)
```

**`AlgebraicGeometry.Space.finite_irreducibleComponents_pullback_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalEtaleLocalization.lean, line 730](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalEtaleLocalization.lean#L730). The attribute's comment: “finitely many irreducible components”.

> **Stacks 0B4D, finitely many irreducible components.** An affine étale localization of a
> birational morphism of decent algebraic spaces with finitely many irreducible components has
> a source with finitely many irreducible components.

```lean
theorem finite_irreducibleComponents_pullback_of_isEtale
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hdecentX : IsDecentSpace B S hS X) (hdecentY : IsDecentSpace B S hS Y)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (hfiniteY : (letI := pointTopology B S hS Y
      (irreducibleComponents (points B S hS Y)).Finite))
    (f : X ⟶ Y)
    (hf : IsBirational B S hS hX hY hdecentX hdecentY hfiniteX hfiniteY f)
    (V : BigFppfOver B S hS) [IsAffine ((BigFppfOver.toScheme B S hS).obj V)]
    (g : yoneda.obj V ⟶ Y) (hg : IsEtale B S hS g) :
    letI := pointTopology B S hS (pullback f g)
    (irreducibleComponents (points B S hS (pullback f g))).Finite
```

**`AlgebraicGeometry.Space.isBirational_pullback_snd_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalEtaleLocalization.lean, line 949](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalEtaleLocalization.lean#L949). The attribute's comment: “birational”. References: EGA IV (6.15.4.1), “étale affine case”.

> **Stacks 0B4D, birationality.** An affine étale localization of a birational morphism of
> decent algebraic spaces with finitely many irreducible components is birational.

```lean
theorem isBirational_pullback_snd_of_isEtale
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hdecentX : IsDecentSpace B S hS X) (hdecentY : IsDecentSpace B S hS Y)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (hfiniteY : (letI := pointTopology B S hS Y
      (irreducibleComponents (points B S hS Y)).Finite))
    (f : X ⟶ Y)
    (hf : IsBirational B S hS hX hY hdecentX hdecentY hfiniteX hfiniteY f)
    (V : BigFppfOver B S hS) [IsAffine ((BigFppfOver.toScheme B S hS).obj V)]
    (g : yoneda.obj V ⟶ Y) (hg : IsEtale B S hS g) :
    IsBirational B S hS
      (isAlgebraicSpace_pullback B S hS f g hX (isAlgebraicSpace_yoneda B S hS V) hY)
      (isAlgebraicSpace_yoneda B S hS V)
      (isDecentSpace_pullback_of_isEtale B S hS hX hY hdecentX V f g hg)
      (isDecentSpace_of_isEtale B S hS g (isAlgebraicSpace_yoneda B S hS V) hY hg hdecentY)
      (finite_irreducibleComponents_pullback_of_isEtale B S hS hX hY hdecentX hdecentY
        hfiniteX hfiniteY f hf V g hg)
      (finite_irreducibleComponents_of_isEtale_of_isAffine B S hS hY hdecentY hfiniteY V g hg)
      (pullback.snd f g)
```

## Tag 0BBG, a lemma

[Tag 0BBG](https://stacks.math.columbia.edu/tag/0BBG) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_lift_normalization_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalNormalization.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalNormalization.lean#L173). The attribute's comment: “the commutative square, as a unique factorization through the target normalization”.

> **The commutative square of Stacks 0BBG, for given normalizations.** Let `f : X ⟶ Y` be a
> birational morphism of decent algebraic spaces over `S` with finitely many irreducible
> components, and let `X^ν ⟶ X` and `Y^ν ⟶ Y` be normalizations. Then `X^ν ⟶ X ⟶ Y` factors
> through `Y^ν ⟶ Y` by a unique morphism `X^ν ⟶ Y^ν`, so that the square it closes commutes.
>
> The factorization is the universal property of the normalization of `Y`, part (4) of
> Stacks 0BB4. Its two hypotheses on the composite `X^ν ⟶ X ⟶ Y` are normality of `X^ν`, part (1)
> of Stacks 0BB4, and preservation of codimension-zero points, which holds for `X^ν ⟶ X` by
> part (3) of Stacks 0BB4 and for `f` by
> `AlgebraicGeometry.Space.localRingDimension_eq_zero_of_isBirational`.
>
> The normalizations are hypotheses here, whereas the source asserts their existence; that
> existence is `AlgebraicGeometry.Space.nonempty_normalizationData_of_isDecentSpace`, and the
> whole lemma, which quantifies over no normalization data at all, is
> `AlgebraicGeometry.Space.exists_normalizationData_isBirational_lift_of_isBirational`. The
> statement here is the stronger one for the
> square — it holds for *every* choice of the two normalizations, not just the ones the
> existence theorem produces — and it is what the rest of the development consumes.

```lean
theorem existsUnique_lift_normalization_of_isBirational (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (hfiniteY : (letI := pointTopology B S hS Y
      (irreducibleComponents (points B S hS Y)).Finite))
    (hXdec : IsDecentSpace B S hS X) (hYdec : IsDecentSpace B S hS Y)
    (DX : NormalizationData B S hS X) (DY : NormalizationData B S hS Y) {f : X ⟶ Y}
    (hf : IsBirational B S hS hX hY hXdec hYdec hfiniteX hfiniteY f) :
    ∃! g : DX.space ⟶ DY.space, g ≫ DY.hom = DX.hom ≫ f
```

**`AlgebraicGeometry.Space.isBirational_lift_normalization_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalNormalization.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalNormalization.lean#L467). The attribute's comment: “birationality of the induced morphism of normalizations”.

> **Birationality of the induced morphism, for given normalizations.** Let `f : X ⟶ Y` be a
> birational morphism of decent algebraic spaces over `S` with finitely many irreducible
> components, and
> let `X^ν ⟶ X` and `Y^ν ⟶ Y` be normalizations. Then any morphism `X^ν ⟶ Y^ν` closing the
> square over `f` is birational.
>
> The two normalizations are again decent with finitely many irreducible components, and their
> normalization morphisms biject generic points, so the induced morphism does too. At a generic
> point `z` of `X^ν` the local-ring map is computed on charts: the chart map of `X^ν ⟶ X` is
> surjective on local rings at `z` by
> `AlgebraicGeometry.Space.NormalizationData.surjective_stalkMap_of_genericChart`, and the
> chart map of `f` is an isomorphism there by birationality, so the chart map of `X^ν ⟶ Y^ν`
> followed by that of `Y^ν ⟶ Y` is surjective, whence the chart map of `X^ν ⟶ Y^ν` is
> surjective. It is injective because its source — the local ring of the normal space `Y^ν` at
> a point of codimension zero — is a field.
>
> The normalizations are hypotheses here, as at
> `AlgebraicGeometry.Space.existsUnique_lift_normalization_of_isBirational`.

```lean
theorem isBirational_lift_normalization_of_isBirational (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hXdec : IsDecentSpace B S hS X)
    (hYdec : IsDecentSpace B S hS Y)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (hfiniteY : (letI := pointTopology B S hS Y
      (irreducibleComponents (points B S hS Y)).Finite))
    (DX : NormalizationData B S hS X) (DY : NormalizationData B S hS Y) {f : X ⟶ Y}
    (hf : IsBirational B S hS hX hY hXdec hYdec hfiniteX hfiniteY f)
    (g : DX.space ⟶ DY.space) (hg : g ≫ DY.hom = DX.hom ≫ f) :
    IsBirational B S hS DX.isAlgebraicSpace DY.isAlgebraicSpace
      (DX.isDecentSpace hX hXdec) (DY.isDecentSpace hY hYdec)
      (DX.finite_irreducibleComponents hX hXdec hfiniteX)
      (DY.finite_irreducibleComponents hY hYdec hfiniteY) g
```

**`AlgebraicGeometry.Space.exists_isBirational_lift_normalization_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalNormalization.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalNormalization.lean#L499). The attribute's comment: “the commutative square together with the birationality of the induced morphism of normalizations”.

> **The square and the birationality together, for given normalizations.** Let `f : X ⟶ Y`
> be a birational morphism of decent algebraic spaces over `S` with finitely many irreducible
> components, and let `X^ν ⟶ X` and `Y^ν ⟶ Y` be normalizations. Then `X^ν ⟶ X ⟶ Y` factors
> through `Y^ν ⟶ Y`, and the factoring morphism `X^ν ⟶ Y^ν` is birational.
>
> The factorization is
> `AlgebraicGeometry.Space.existsUnique_lift_normalization_of_isBirational` and its
> birationality is
> `AlgebraicGeometry.Space.isBirational_lift_normalization_of_isBirational`.
>
> The normalizations are hypotheses here; the whole lemma, with their existence, is
> `AlgebraicGeometry.Space.exists_normalizationData_isBirational_lift_of_isBirational`.

```lean
theorem exists_isBirational_lift_normalization_of_isBirational
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hXdec : IsDecentSpace B S hS X) (hYdec : IsDecentSpace B S hS Y)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (hfiniteY : (letI := pointTopology B S hS Y
      (irreducibleComponents (points B S hS Y)).Finite))
    (DX : NormalizationData B S hS X) (DY : NormalizationData B S hS Y) {f : X ⟶ Y}
    (hf : IsBirational B S hS hX hY hXdec hYdec hfiniteX hfiniteY f) :
    ∃ g : DX.space ⟶ DY.space, g ≫ DY.hom = DX.hom ≫ f ∧
      IsBirational B S hS DX.isAlgebraicSpace DY.isAlgebraicSpace
        (DX.isDecentSpace hX hXdec) (DY.isDecentSpace hY hYdec)
        (DX.finite_irreducibleComponents hX hXdec hfiniteX)
        (DY.finite_irreducibleComponents hY hYdec hfiniteY) g
```

**`AlgebraicGeometry.Space.nonempty_normalizationData_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalNormalizationExistence.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalNormalizationExistence.lean#L82). The attribute's comment: “the existence of the normalizations”.

> **Stacks 0BBG, the existence of the normalizations.** A decent algebraic space over `S`
> whose space of points has finitely many irreducible components has normalization data: an
> algebraic space `F^ν` over `S` with a morphism `F^ν ⟶ F` whose base change along every
> surjective étale scheme chart of `F` is the normalization of that chart.
>
> This is the first clause of Stacks 0BBG, and the source proves it the same way: the hypotheses
> give the equivalent conditions of Stacks 0BB1 by Stacks 0BB9
> (`AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_of_isDecentSpace`), and under
> those conditions the normalization exists by the existence half of Stacks 07U4,
> `AlgebraicGeometry.Space.nonempty_normalizationData`. Applied to the source and the target of
> a birational morphism it is the assertion that `X^ν ⟶ X` and `Y^ν ⟶ Y` exist.

```lean
theorem nonempty_normalizationData_of_isDecentSpace
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (hFdec : IsDecentSpace B S hS F)
    (hfinite : (letI := pointTopology B S hS F
      (irreducibleComponents (points B S hS F)).Finite)) :
    Nonempty (NormalizationData B S hS F)
```

**`AlgebraicGeometry.Space.exists_normalizationData_isBirational_lift_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalNormalizationExistence.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalNormalizationExistence.lean#L112).

> **Stacks 0BBG.** Let `f : X ⟶ Y` be a birational morphism between algebraic spaces over
> `S` which are decent and have finitely many irreducible components. Then the normalizations
> `X^ν ⟶ X` and `Y^ν ⟶ Y` exist and there is a commutative diagram with rows `X^ν ⟶ Y^ν` and
> `X ⟶ Y` and columns the two normalization morphisms, and the morphism `X^ν ⟶ Y^ν` is
> birational.
>
> Nothing is assumed about the normalizations: they are produced by
> `AlgebraicGeometry.Space.nonempty_normalizationData_of_isDecentSpace` from decency and the
> finiteness of the irreducible components, which is the source's own route through Stacks 0BB9
> and Stacks 0BB1. The square is then
> `AlgebraicGeometry.Space.existsUnique_lift_normalization_of_isBirational` and the
> birationality of the morphism closing it is
> `AlgebraicGeometry.Space.isBirational_lift_normalization_of_isBirational`, both of which hold
> for an arbitrary choice of the two normalizations.
>
> The decency of `X^ν` and `Y^ν` and the finiteness of their irreducible components, which the
> conclusion's `AlgebraicGeometry.Space.IsBirational` is parameterised by, are
> `AlgebraicGeometry.Space.NormalizationData.isDecentSpace` and
> `AlgebraicGeometry.Space.NormalizationData.finite_irreducibleComponents`; the source records
> them in its second paragraph, citing Stacks 0ABT.

```lean
theorem exists_normalizationData_isBirational_lift_of_isBirational
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hXdec : IsDecentSpace B S hS X) (hYdec : IsDecentSpace B S hS Y)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (hfiniteY : (letI := pointTopology B S hS Y
      (irreducibleComponents (points B S hS Y)).Finite))
    {f : X ⟶ Y}
    (hf : IsBirational B S hS hX hY hXdec hYdec hfiniteX hfiniteY f) :
    ∃ (DX : NormalizationData B S hS X) (DY : NormalizationData B S hS Y)
      (g : DX.space ⟶ DY.space), g ≫ DY.hom = DX.hom ≫ f ∧
        IsBirational B S hS DX.isAlgebraicSpace DY.isAlgebraicSpace
          (DX.isDecentSpace hX hXdec) (DY.isDecentSpace hY hYdec)
          (DX.finite_irreducibleComponents hX hXdec hfiniteX)
          (DY.finite_irreducibleComponents hY hYdec hfiniteY) g
```

## Tag 0B4E, a lemma

[Tag 0B4E](https://stacks.math.columbia.edu/tag/0B4E) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_of_isIntegralHom_of_isBirational_of_isNormal_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralBirationalOverNormal.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralBirationalOverNormal.lean#L467). References: EGA IV (8.12.10.1).

> **Stacks 0B4E.** An integral birational morphism from a reduced algebraic space to a normal
> algebraic space is an isomorphism, provided both are decent with finitely many irreducible
> components.
>
> Being an isomorphism is checked on the jointly locally surjective family of affine étale charts
> `V i → Y` supplied by
> `AlgebraicGeometry.exists_affine_etale_family_isLocallySurjective`. Integrality of `f`
> represents the base change `X ×_Y V i` by an affine object `W` of the site, so the chart base
> change is a morphism of schemes `W → V i`; it is birational by Stacks 0B4D together with
> `AlgebraicGeometry.isBirational_toScheme_map_of_yonedaIso`, its source is reduced and its
> target normal with finitely many irreducible components, whence it is an isomorphism by
> `AlgebraicGeometry.isIso_of_isReduced_of_isBirational_of_isNormal`.

```lean
theorem isIso_of_isIntegralHom_of_isBirational_of_isNormal_of_isReduced
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hdecentX : IsDecentSpace B S hS X) (hdecentY : IsDecentSpace B S hS Y)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (hfiniteY : (letI := pointTopology B S hS Y
      (irreducibleComponents (points B S hS Y)).Finite))
    (f : X ⟶ Y)
    (hintegral : IsIntegralHom B S hS f)
    (hbirational : IsBirational B S hS hX hY hdecentX hdecentY hfiniteX hfiniteY f)
    (hnormalY : IsNormal B S hS Y)
    (hreducedX : HasEtaleLocalProperty B S hS X
      (fun Z : Scheme.{u} => _root_.AlgebraicGeometry.IsReduced Z)) :
    IsIso f
```

## Tag 0BBH, a lemma

[Tag 0BBH](https://stacks.math.columbia.edu/tag/0BBH) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_factorization_normalization_of_isIntegralHom_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BirationalNormalization.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BirationalNormalization.lean#L533).

> **Stacks 0BBH.** Let `f : X ⟶ Y` be an integral birational morphism of decent algebraic
> spaces over `S` with finitely many irreducible components, and let `X^ν ⟶ X` and `Y^ν ⟶ Y` be
> normalizations. Then the normalization morphism of `Y` factors as `Y^ν ⟶ X ⟶ Y`, and the
> first leg `Y^ν ⟶ X` is the normalization of `X`: it is the normalization morphism `X^ν ⟶ X`
> precomposed with an isomorphism `Y^ν ≅ X^ν` over `X`.
>
> The induced morphism `X^ν ⟶ Y^ν` of Stacks 0BBG is integral by Stacks 081Z, part (2): its
> composite with the normalization morphism of `Y` is the composite of the normalization
> morphism of `X` with `f`, both integral, and the normalization morphism of `Y` is integral
> hence separated. It is birational by Stacks 0BBG, its source is reduced — being normal — and
> its target is normal, both normalizations are decent with finitely many irreducible
> components, so Stacks 0B4E makes it an isomorphism. Its inverse is the asserted
> factorization.

```lean
theorem exists_factorization_normalization_of_isIntegralHom_of_isBirational
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hXdec : IsDecentSpace B S hS X) (hYdec : IsDecentSpace B S hS Y)
    (hfiniteX : (letI := pointTopology B S hS X
      (irreducibleComponents (points B S hS X)).Finite))
    (hfiniteY : (letI := pointTopology B S hS Y
      (irreducibleComponents (points B S hS Y)).Finite))
    (DX : NormalizationData B S hS X) (DY : NormalizationData B S hS Y) {f : X ⟶ Y}
    (hfint : IsIntegralHom B S hS f)
    (hf : IsBirational B S hS hX hY hXdec hYdec hfiniteX hfiniteY f) :
    ∃ (h : DY.space ⟶ X) (e : DY.space ≅ DX.space),
      h ≫ f = DY.hom ∧ h = e.hom ≫ DX.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.22, Tag 0ACU](https://stacks.math.columbia.edu/tag/0ACU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
