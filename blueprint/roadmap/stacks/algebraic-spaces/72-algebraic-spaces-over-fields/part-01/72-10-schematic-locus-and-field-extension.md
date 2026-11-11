---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isRepresentable_of_isPurelyInseparable_of_isRepresentable, AlgebraicGeometry.Space.exists_finite_separable_isRepresentable_relocalizeRestrict, AlgebraicGeometry.Space.isRepresentable_relocalizeRestrict_algebraicClosure, AlgebraicGeometry.Space.isAlgebraicSpace_extensionBaseChange, AlgebraicGeometry.Space.isFreeOnNonemptyPoints_extensionBaseChange, AlgebraicGeometry.Space.isIso_extensionBaseChangeQuotientLift, AlgebraicGeometry.Space.mem_schematicLocus_actionQuotient_iff, AlgebraicGeometry.Space.mem_schematicLocus_orbitQuotient_iff
statement: formalized
proof: formalized
---

# 72.10 Schematic locus and field extension

Section 72.10 of the Stacks Project, [Tag 0B82](https://stacks.math.columbia.edu/tag/0B82). 9 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B83, a lemma

[Tag 0B83](https://stacks.math.columbia.edu/tag/0B83) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_isPurelyInseparable_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PurelyInseparableSchemeDescent.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PurelyInseparableSchemeDescent.lean#L304).

> **Stacks 0B83.** Let `k` be a field and let `X` be an algebraic space over `k`. If there
> exists a purely inseparable field extension `k'/k` such that the base change `X_{k'}` is a
> scheme, then `X` is a scheme.
>
> The projection `X_{k'} ⟶ X` is integral, surjective and universally injective, hence integral
> and bijective on the points of Stacks 03BU, so the proof of Stacks 07VV,
> `AlgebraicGeometry.Space.isRepresentable_of_isIntegralHom_of_bijective_of_isAffineSpace`,
> applies once every open subspace `W ⊆ X` with affine preimage `W_{k'}` is known to be affine.
> That preimage is a base change of `W` along `Spec k' ⟶ Spec k`, so `W` is affine by
> `AlgebraicGeometry.Space.isAffineSpace_of_isPullback_specExtensionToBase`, which descends
> affineness along the fpqc covering `Spec k' ⟶ Spec k` by Stacks 041Z; this replaces the appeal
> to Stacks 07VT in the proof of Stacks 07VV.
>
> The spectrum of `k'` lies in the chosen big fppf site as soon as the spectrum of `k` does, by
> `AlgebraicGeometry.Space.contains_spec_of_isAlgebraic`; membership of the site is a
> proposition, so the statement is unchanged if another proof of it is substituted.

```lean
theorem isRepresentable_of_isPurelyInseparable_of_isRepresentable [IsPurelyInseparable k k']
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (hXk' : (extensionBaseChange k k' B hk
      (contains_spec_of_isAlgebraic B k k' hk) X).IsRepresentable) :
    X.IsRepresentable
```

## Tag 0B84, a lemma

[Tag 0B84](https://stacks.math.columbia.edu/tag/0B84) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_finite_separable_isRepresentable_relocalizeRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OverFields/AlgClosureSchemeDescent.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OverFields/AlgClosureSchemeDescent.lean#L418). The attribute's comment: “part (2)”.

> **[Stacks, Tag 0B84] part (2).** Let `k` be a field and let `X` be a quasi-compact and
> quasi-separated algebraic space over `k`. If there is a field extension `K/k` such that the base
> change `X_K` is a scheme, then there is a *finite separable* extension `k'/k` such that `X_{k'}`
> is a scheme.
>
> The proof is the source's. `K` is the filtered union of its finitely generated `k`-subalgebras
> `A`, and [Stacks, Tag 07SR] makes one of the base changes `X_A` a scheme; this is
> `AlgebraicGeometry.Space.exists_fgSubalgebra_isRepresentable_relocalizeRestrict`. A residue
> field `k₁` of `A` at a maximal ideal is finite over `k` by the Nullstellensatz, `X_{k₁}` is a
> scheme, and the separable closure `k'` of `k` in `k₁` is finite separable over `k` with `k₁/k'`
> purely inseparable, so `X_{k'}` is a scheme by the finite case of [Stacks, Tag 0B83],
> `AlgebraicGeometry.Space.isRepresentable_of_isRepresentable_extensionBaseChange_of_finite`.

```lean
theorem exists_finite_separable_isRepresentable_relocalizeRestrict (k K : Type u) [Field k]
    [Field K] [Algebra k K] (B : BigFppfSite.{u}) (hk : B.Contains (Spec (.of k)))
    (hK : B.Contains (Spec (.of K))) (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (hXqc : IsQuasiCompactSpace B (Spec (.of k)) hk X)
    (hXqs : IsAbsolutelyQuasiSeparated B (Spec (.of k)) hk B.contains_terminal X)
    (hXK : ((OverShriek.relocalizeRestrict (specExtensionHom k K B hk hK)).obj
      X).IsRepresentable) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k') (_ : Module.Finite k k')
      (_ : Algebra.IsSeparable k k') (hk' : B.Contains (Spec (.of k'))),
      ((OverShriek.relocalizeRestrict (specExtensionHom k k' B hk hk')).obj
        X).IsRepresentable
```

**`AlgebraicGeometry.Space.isRepresentable_relocalizeRestrict_algebraicClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OverFields/AlgClosureSchemeDescent.lean, line 597](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OverFields/AlgClosureSchemeDescent.lean#L597). The attribute's comment: “part (1)”.

> **[Stacks, Tag 0B84] part (1).** Let `k` be a field with algebraic closure `k̄` and let `X`
> be a quasi-separated algebraic space over `k`. If there is a field extension `K/k` such that the
> base change `X_K` is a scheme, then `X_{k̄}` is a scheme.
>
> The source reduces this to part (2) by covering `X` with quasi-compact open subspaces and omits
> the details; they are supplied in
> `AlgebraicGeometry.Space.isRepresentable_relocalizeRestrict_of_isAlgClosed`. The spectrum of the
> algebraic closure lies in the site automatically.

```lean
theorem isRepresentable_relocalizeRestrict_algebraicClosure (k K : Type u) [Field k] [Field K]
    [Algebra k K] (B : BigFppfSite.{u}) (hk : B.Contains (Spec (.of k)))
    (hK : B.Contains (Spec (.of K))) (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (hXqs : IsAbsolutelyQuasiSeparated B (Spec (.of k)) hk B.contains_terminal X)
    (hXK : ((OverShriek.relocalizeRestrict (specExtensionHom k K B hk hK)).obj
      X).IsRepresentable) :
    ((OverShriek.relocalizeRestrict (specExtensionHom k (AlgebraicClosure k) B hk
      (contains_spec_of_isAlgebraic B k (AlgebraicClosure k) hk))).obj X).IsRepresentable
```

## Tag 0B86, a lemma

[Tag 0B86](https://stacks.math.columbia.edu/tag/0B86) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_extensionBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GaloisBaseChangeQuotient.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GaloisBaseChangeQuotient.lean#L164). The attribute's comment: “the base change is an algebraic space”.

> **Stacks 0B86**, the algebraicity of the base change: the base change of an algebraic space
> over `k` along a field extension `k'/k` is, viewed over `k`, an algebraic space.

```lean
theorem isAlgebraicSpace_extensionBaseChange
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) :
    IsAlgebraicSpace B (Spec (.of k)) hk (extensionBaseChange k k' B hk hk' X)
```

**`AlgebraicGeometry.Space.isFreeOnNonemptyPoints_extensionBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GaloisBaseChangeQuotient.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GaloisBaseChangeQuotient.lean#L271). The attribute's comment: “the Galois group acts freely on the base change”.

> **Stacks 0B86**, the freeness assertion: the group of `k`-automorphisms of `k'` acts freely
> on `X_{k'}`.  For a finite Galois extension this is the first half of the tag; freeness in fact
> needs no assumption on the extension.

```lean
theorem isFreeOnNonemptyPoints_extensionBaseChange :
    IsFreeOnNonemptyPoints B (Spec (.of k)) hk (k' ≃ₐ[k] k')
      (extensionBaseChange k k' B hk hk' X)
```

**`AlgebraicGeometry.Space.isIso_extensionBaseChangeQuotientLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GaloisBaseChangeQuotient.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GaloisBaseChangeQuotient.lean#L635). The attribute's comment: “X = X\_\{k'}/G”.

> **Stacks 0B86**, the quotient assertion: for a finite Galois extension `k'/k` with Galois
> group `G`, an algebraic space `X` over `k` is the quotient `X_{k'}/G`.

```lean
theorem isIso_extensionBaseChangeQuotientLift [FiniteDimensional k k'] [IsGalois k k']
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) :
    IsIso (extensionBaseChangeQuotientLift k k' B hk hk' X hX.isSheaf)
```

## Tag 0B87, a lemma

[Tag 0B87](https://stacks.math.columbia.edu/tag/0B87) in the Stacks Project.

**`AlgebraicGeometry.Space.mem_schematicLocus_actionQuotient_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FiniteFreeActionSchematicLocus.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FiniteFreeActionSchematicLocus.lean#L292). The attribute's comment: “for a free action of a finite group on an object of the big fppf site over `S` in place of an action on an arbitrary algebraic space, the quotient being the quotient sheaf of the graph relation of the action as in the library's form of Tag 071S, freeness being read on the points over the test schemes with nonempty underlying space, and the affine open of condition (2) being presented as in the library's form of Tag 0BA1, by an open immersion into the functor of points of the scheme acted on out of an affine object of the site”.

> **Stacks 0B87.** Let a finite group `G` act freely on an object `V` of a big fppf site over
> a scheme `S` and let `y` be a point of the quotient `V/G`. Then `y` lies in the schematic locus
> of `V/G` if and only if there is an affine object `U` of the site and an open immersion
> `i : h_U ⟶ h_V` whose point set contains every point of `h_V` above `y`.
>
> The quotient map is surjective and finite locally free after every representable base change,
> so this is Stacks 0BA1 for it, read on the chart `h_V ⟶ V/G` bundled as a morphism of
> algebraic spaces over `S`.

```lean
theorem mem_schematicLocus_actionQuotient_iff [Finite G]
    (ha : ActsFreelyOnNonemptyPoints (underlyingOver B hS V) G a)
    (y : points B S hS (actionQuotient G B hS V a)) :
    y ∈ Set.range (pointsMap B S hS
        (schematicLocus B S hS (actionQuotient G B hS V a)).toFunctor
        (schematicLocus B S hS (actionQuotient G B hS V a)).ι) ↔
      ∃ (U : BigFppfOver B S hS) (i : yoneda.obj U ⟶ yoneda.obj V),
        IsAffine ((BigFppfOver.toScheme B S hS).obj U) ∧ IsOpenImmersion B S hS i ∧
        ∀ x : points B S hS (yoneda.obj V),
          pointsMap B S hS (yoneda.obj V) (freeActionQuotientMap G B S hS V a ha) x = y →
            x ∈ Set.range (pointsMap B S hS (yoneda.obj U) i)
```

**`AlgebraicGeometry.Space.mem_schematicLocus_orbitQuotient_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionSpaceSchematicLocus.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionSpaceSchematicLocus.lean#L495).

> **Stacks 0B87.** Let `S` be a scheme, let `X` be an algebraic space over `S`, let `G` be a
> finite group acting freely on `X` and let `Y = X/G` be the quotient of Tag 071S. For a point
> `y` of `Y` the following are equivalent:
>
> 1. `y` lies in the schematic locus of `Y` — the point set of
>    `AlgebraicGeometry.Space.schematicLocus`, the largest open subspace of `Y` which is a
>    scheme (Tag 03JH); and
> 2. there is an affine open subspace of `X`, presented as an open immersion `i : h_V ⟶ X` from
>    an affine object `V` of the site, whose point set contains the whole fibre of `y`.
>
> The quotient map `X ⟶ X/G` is surjective and finite locally free after every representable
> base change, so this is Stacks 0BA1 for it. Freeness is read on the points over the test
> objects with nonempty underlying scheme, which is how the library's form of Tag 071S — the form
> producing the quotient here — reads it.

```lean
theorem mem_schematicLocus_orbitQuotient_iff
    (hnat : IsNaturalAction B S hS G X) (hX : IsAlgebraicSpace B S hS X)
    (hfree : IsFreeOnNonemptyPoints B S hS G X)
    (y : points B S hS (orbitQuotientSheaf B S hS G X hnat).obj) :
    y ∈ Set.range (pointsMap B S hS
        (schematicLocus B S hS (orbitQuotientSheaf B S hS G X hnat).obj).toFunctor
        (schematicLocus B S hS (orbitQuotientSheaf B S hS G X hnat).obj).ι) ↔
      ∃ (V : BigFppfOver B S hS) (i : yoneda.obj V ⟶ X),
        IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧ IsOpenImmersion B S hS i ∧
        ∀ x : points B S hS X,
          pointsMap B S hS X (toOrbitQuotient B S hS G X hnat) x = y →
            x ∈ Set.range (pointsMap B S hS (yoneda.obj V) i)
```

## Tag 0B85, a lemma

[Tag 0B85](https://stacks.math.columbia.edu/tag/0B85) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_isRepresentable_purelyTranscendental_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OverFields/PurelyTranscendentalDescent/Descent.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OverFields/PurelyTranscendentalDescent/Descent.lean#L239).

> **Stacks 0B85.** Let `k` be a field and `X` a quasi-separated algebraic space over `k`. If
> there is a purely transcendental field extension `K/k` such that `X_K` is a scheme, then `X` is a
> scheme. Here `X_K` is the restriction of `X` to the big fppf site over `Spec K`.

```lean
theorem isRepresentable_of_isRepresentable_purelyTranscendental_baseChange
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    [PurelyTranscendental k K]
    (B : AlgebraicGeometry.BigFppfSite.{u})
    (hk : B.Contains (Spec (.of k))) (hK : B.Contains (Spec (.of K)))
    (F : (AlgebraicGeometry.BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hF : AlgebraicGeometry.IsAlgebraicSpace B (Spec (.of k)) hk F)
    (hqs : AlgebraicGeometry.Space.IsQuasiSeparatedOver B (Spec (.of k)) hk F)
    (hbase : ((OverShriek.relocalizeRestrict
      (ObjectProperty.homMk
        (Spec.map (CommRingCat.ofHom (algebraMap k K))) :
          B.obj hK ⟶ B.obj hk)).obj F).IsRepresentable) :
    F.IsRepresentable
```

## Tag 0BA7, a remark

[Tag 0BA7](https://stacks.math.columbia.edu/tag/0BA7) in the Stacks Project.

**`Algebra.IsGeometricallyIrreducible.finiteField_remark`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyIrreducibleFiniteFieldDescent.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyIrreducibleFiniteFieldDescent.lean#L171).

> **Stacks 0BA7.** Let `k` be a finite field and `K/k` a geometrically irreducible field
> extension.
> 1. `K` is the directed union of geometrically irreducible `k`-subalgebras of finite type.
> 2. For every geometrically irreducible `k`-algebra `A` of finite type there is `N` such that
>    for every finite extension `k'/k` of degree `n ≥ N` there is a `k`-algebra map `A → k'`.
> 3. If `X` is a quasi-separated algebraic space over `k` and `X_K` is a scheme, then `X` is a
>    scheme.

```lean
theorem finiteField_remark (k K : Type u) [Field k] [Finite k] [Field K] [Algebra k K]
    (hK : Algebra.IsGeometricallyIrreducible k K) :
    (∃ (ι : Type u) (A : ι → Subalgebra k K), Directed (· ≤ ·) A ∧ (⨆ i, A i) = ⊤ ∧
      ∀ i, Algebra.FiniteType k (A i) ∧ Algebra.IsGeometricallyIrreducible k (A i)) ∧
    (∀ (A : Type u) [CommRing A] [Algebra k A] [Algebra.FiniteType k A],
      Algebra.IsGeometricallyIrreducible k A →
      ∃ N : ℕ, ∀ (k' : Type u) [Field k'] [Algebra k k'] [FiniteDimensional k k'],
        N ≤ finrank k k' → Nonempty (A →ₐ[k] k')) ∧
    (∀ (B : BigFppfSite.{u}) (hk : B.Contains (Spec (.of k))) (hK' : B.Contains (Spec (.of K)))
      (F : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u),
      IsAlgebraicSpace B (Spec (.of k)) hk F →
      IsQuasiSeparatedOver B (Spec (.of k)) hk F →
      ((OverShriek.relocalizeRestrict
        (ObjectProperty.homMk (Spec.map (CommRingCat.ofHom (algebraMap k K))) :
          B.obj hK' ⟶ B.obj hk)).obj F).IsRepresentable →
      F.IsRepresentable)
```

## Tag 0B88, a lemma

[Tag 0B88](https://stacks.math.columbia.edu/tag/0B88) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_isAlgClosure_finite_rationalPoints_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OverFields/DecentFiniteTypeScheme.lean, line 916](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OverFields/DecentFiniteTypeScheme.lean#L916). The attribute's comment: “all three hypotheses of the source, none dropped, weakened or added”.

> **Stacks 0B88.** Let `k` be a field with algebraic closure `K = k̄` and let `X` be an
> algebraic space over `k`.  Assume
>
> 1. `X` is decent and locally of finite type over `k`,
> 2. `X_{k̄}` is a scheme, and
> 3. any finite set of `k̄`-rational points of `X_{k̄}` is contained in an affine.
>
> Then `X` is a scheme.
>
> All three source hypotheses are present and none is weakened: `hdecent` together with
> `hfinite` is hypothesis (1), `hbase` is hypothesis (2), and `haffine` is hypothesis (3).
>
> `X_{k̄}` is the restriction of `X` to the big fppf site over `Spec k̄` along the morphism
> `g : Spec k̄ ⟶ Spec k` of the site, a `k̄`-rational point of it is a section over the terminal
> object `Spec k̄` of that site, and an affine open is presented by an open immersion out of an
> affine object, as in the library's form of Tag 0BA1. The structure morphism of `X` over `Spec k`
> is given explicitly as `f`, the base `Spec k` being terminal in its own big fppf site.
>
> Being decent and locally of finite type over a field, `|X|` is a Jacobson space (Tag 0BA6 and
> Tag 0BA3), so it is enough to put every closed point of `|X|` in the schematic locus of
> Tag 03JH, and then Tag 03KE in the case `(θ)` finishes.  A closed point is represented by a
> closed immersion `Spec l ⟶ X` (Tag 0AHB) with `l/k` finite (Tag 03XG and the Hilbert
> Nullstellensatz), so `Spec l ×_X X_{k̄}` is a finite scheme over an algebraically closed field
> and hypothesis (3) gives an affine open of `X_{k̄}` through which it factors.  The projection
> `π : X_{k̄} ⟶ X` is a base change of the affine, flat, surjective morphism
> `Spec k̄ ⟶ Spec k`, hence universally closed and quasi-compact, and closedness converts the
> fibrewise containment into a quasi-compact open neighbourhood `N` of the point whose base
> change to `k̄` is quasi-affine over `Spec k̄`.  Tag 0423 descends quasi-affineness along that
> fpqc covering and Tag 03WM makes `N` a scheme, so the point is in the schematic locus.

```lean
theorem isRepresentable_of_isAlgClosure_finite_rationalPoints_isAffine
    (k K : Type u) [Field k] [Field K] [Algebra k K] [IsAlgClosure k K]
    (B : BigFppfSite.{u})
    (hk : B.Contains (Spec (.of k))) (hK : B.Contains (Spec (.of K)))
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (hdecent : IsDecentSpace B (Spec (.of k)) hk X)
    (f : X ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hk))))
    (hfinite : IsLocallyOfFiniteType B (Spec (.of k)) hk f)
    (hbase : ((OverShriek.relocalizeRestrict
      (ObjectProperty.homMk (Spec.map (CommRingCat.ofHom (algebraMap k K))) :
        B.obj hK ⟶ B.obj hk)).obj X).IsRepresentable)
    (haffine :
      let Xbase := (OverShriek.relocalizeRestrict
        (ObjectProperty.homMk (Spec.map (CommRingCat.ofHom (algebraMap k K))) :
          B.obj hK ⟶ B.obj hk)).obj X
      ∀ s : Finset (Xbase.obj (op (Over.mk (𝟙 (B.obj hK))))),
        ∃ (U : BigFppfOver B (Spec (.of K)) hK) (i : yoneda.obj U ⟶ Xbase),
          IsAffine ((BigFppfOver.toScheme B (Spec (.of K)) hK).obj U) ∧
          IsOpenImmersion B (Spec (.of K)) hK i ∧
          ∀ x ∈ s, x ∈ Set.range (i.app (op (Over.mk (𝟙 (B.obj hK)))))) :
    X.IsRepresentable
```

## Tag 06S0, a lemma

[Tag 06S0](https://stacks.math.columbia.edu/tag/06S0) in the Stacks Project.

**`AlgebraicGeometry.Space.tfae_isLocallyQuasiFinite_to_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocallyQuasiFiniteOverFieldTfae.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LocallyQuasiFiniteOverFieldTfae.lean#L84).

> **Stacks 06S0.** Let `k` be a field and `X` an algebraic space over `k`, presented as an
> algebraic space over `S` with a morphism `g : X ⟶ h_K` to an object `K` of the site whose
> underlying scheme is `Spec k`. The following are equivalent:
> 1. `X` is locally quasi-finite over `k`;
> 2. `X` is locally of finite type over `k` and has dimension `0`;
> 3. `X` is a scheme and is locally quasi-finite over `k`;
> 4. `X` is a scheme, is locally of finite type over `k` and has dimension `0`;
> 5. `X` is a disjoint union of spectra of Artinian local `k`-algebras `A` with
>    `dim_k A < ∞`, over `k`.
>
> "Dimension `0`" is read as `≤ 0`, since the empty space has dimension `⊥` and satisfies (1).

```lean
theorem tfae_isLocallyQuasiFinite_to_field {k : Type u} [Field k]
    {K : BigFppfOver B S hS} (e : (BigFppfOver.toScheme B S hS).obj K ≅ Spec (.of k))
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (g : X ⟶ yoneda.obj K) :
    [IsLocallyQuasiFinite B S hS g,
      IsLocallyOfFiniteType B S hS g ∧ dimension B S hS X hX ≤ 0,
      X.IsRepresentable ∧ IsLocallyQuasiFinite B S hS g,
      X.IsRepresentable ∧ IsLocallyOfFiniteType B S hS g ∧ dimension B S hS X hX ≤ 0,
      ∃ (Y : BigFppfOver B S hS) (eX : yoneda.obj Y ≅ X) (I : Type u) (A : I → Type u)
        (_ : ∀ i, CommRing (A i)) (_ : ∀ i, Algebra k (A i)) (_ : ∀ i, IsLocalRing (A i))
        (_ : ∀ i, IsArtinianRing (A i)) (_ : ∀ i, Module.Finite k (A i))
        (eY : (BigFppfOver.toScheme B S hS).obj Y ≅ ∐ fun i ↦ Spec (.of (A i))),
        eY.hom ≫ Sigma.desc (fun i ↦ Spec.map (CommRingCat.ofHom (algebraMap k (A i)))) =
          (BigFppfOver.toScheme B S hS).map (yoneda.preimage (eX.hom ≫ g)) ≫ e.hom].TFAE
```

## Tag 06S1, a lemma

[Tag 06S1](https://stacks.math.columbia.edu/tag/06S1) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_of_mono_of_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MonoLocallyQuasiFiniteOverField.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MonoLocallyQuasiFiniteOverField.lean#L68).

> **Stacks 06S1.** Let `k` be a field and `f : X ⟶ Y` a monomorphism of algebraic spaces over
> `k`. If `Y` is locally quasi-finite over `k`, so is `X`.

```lean
theorem isLocallyQuasiFinite_of_mono_of_isLocallyQuasiFinite {k : Type u} [Field k]
    (e : S ≅ Spec (.of k)) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) [Mono f]
    (hYk : IsLocallyQuasiFinite B S hS ((isTerminal_yoneda_obj_base B S hS).from Y)) :
    IsLocallyQuasiFinite B S hS ((isTerminal_yoneda_obj_base B S hS).from X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.10, Tag 0B82](https://stacks.math.columbia.edu/tag/0B82)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
