---
declaration: section
origin: cited
lean: AlgebraicGeometry.faithful_finiteEtaleBaseChange_of_isDominant, AlgebraicGeometry.fullyFaithful_finiteEtaleBaseChange_to_puncturedSpectrum, AlgebraicGeometry.fullyFaithful_finiteEtaleBaseChange_of_dense_of_noetherianSpace, AlgebraicGeometry.fullyFaithful_finiteEtaleBaseChange_of_quasiCompact_of_isClosed_compl, AlgebraicGeometry.fullyFaithful_finiteEtaleBaseChange_of_finite_irreducibleComponents, AlgebraicGeometry.isExactSequence_etaleFundamentalGroupMap_puncturedSpectrum_of_quasiCompact, AlgebraicGeometry.connectedSpace_puncturedSpectrum_of_isStrictHenselization, AlgebraicGeometry.etaleFundamentalGroupMap_comp_eq_one_puncturedSpectrum
statement: formalized
proof: formalized
---

# 58.10 Local connectedness

Section 58.10 of the Stacks Project, [Tag 0BQD](https://stacks.math.columbia.edu/tag/0BQD). 9 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BQE, a lemma

[Tag 0BQE](https://stacks.math.columbia.edu/tag/0BQE) in the Stacks Project.

**`AlgebraicGeometry.faithful_finiteEtaleBaseChange_of_isDominant`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/Basic.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/Basic.lean#L123).

> **Stacks Project, Tag 0BQE.** Pullback of finite étale schemes along a
> dominant morphism of schemes is faithful.

```lean
public lemma faithful_finiteEtaleBaseChange_of_isDominant
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsDominant f] :
    (MorphismProperty.Over.pullback
      ((@IsFinite ⊓ @Etale) : MorphismProperty Scheme.{u}) ⊤ f).Faithful
```

## Tag 0BLQ, a lemma

[Tag 0BLQ](https://stacks.math.columbia.edu/tag/0BLQ) in the Stacks Project.

**`AlgebraicGeometry.fullyFaithful_finiteEtaleBaseChange_to_puncturedSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/PuncturedSpectrum.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/PuncturedSpectrum.lean#L292).

> Restriction from the spectrum of a local ring `A` to its punctured spectrum is fully faithful
> on finite étale covers, provided the punctured spectrum of a strict henselization of `A` is
> connected.

```lean
theorem fullyFaithful_finiteEtaleBaseChange_to_puncturedSpectrum
    (A : Type u) [CommRing A] [IsLocalRing A]
    (κsep : Type u) [Field κsep]
    [Algebra (maximalIdeal A).ResidueField κsep]
    [IsSepClosure (maximalIdeal A).ResidueField κsep]
    (Ash : Type u) [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash]
    (hAsh : Stacks.StrictHenselization.IsStrictHenselization A κsep Ash)
    (hconnected : _root_.IsConnected ({closedPoint Ash}ᶜ : Set (PrimeSpectrum Ash))) :
    Nonempty (finiteEtaleBaseChange (puncturedSpectrum A).ι).FullyFaithful
```

## Tag 0BQF, a lemma

[Tag 0BQF](https://stacks.math.columbia.edu/tag/0BQF) in the Stacks Project.

**`AlgebraicGeometry.fullyFaithful_finiteEtaleBaseChange_of_dense_of_noetherianSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/DenseOpen.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/DenseOpen.lean#L719). References: SGA 7 II (2.3.1), “partial”.

> Let `U` be a dense open of a scheme `X` with Noetherian underlying space, and suppose that for
> every point `x` of `X` outside `U` the punctured spectrum of every strict henselization of
> `𝒪_{X, x}` is connected.  Then base change of finite étale covers along `U ⟶ X` is fully
> faithful.

```lean
theorem fullyFaithful_finiteEtaleBaseChange_of_dense_of_noetherianSpace
    (X : Scheme.{u}) (U : X.Opens) [NoetherianSpace X] (hU : Dense (U : Set X))
    (hconn : ∀ x : X, x ∉ U →
      IsConnectedPuncturedStrictHenselization (X.presheaf.stalk x)) :
    Nonempty (finiteEtaleBaseChange U.ι).FullyFaithful
```

## Tag 0BSA, a lemma

[Tag 0BSA](https://stacks.math.columbia.edu/tag/0BSA) in the Stacks Project.

**`AlgebraicGeometry.fullyFaithful_finiteEtaleBaseChange_of_quasiCompact_of_isClosed_compl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/DenseOpenClosedComplement.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/DenseOpenClosedComplement.lean#L330).

> Let `j : U ⟶ X` be a dense open immersion of schemes which is quasi-compact, and assume that
> every point of `X ∖ U` is closed and that the punctured spectrum of every strict henselization of
> its local ring is connected. Then restriction of finite étale covers along `j` is fully
> faithful.

```lean
public theorem fullyFaithful_finiteEtaleBaseChange_of_quasiCompact_of_isClosed_compl
    {U X : Scheme.{u}} (j : U ⟶ X) [IsOpenImmersion j] [IsDominant j]
    [QuasiCompact j]
    (hclosed : ∀ x : X, x ∉ Set.range j.base → IsClosed ({x} : Set X))
    (hconnected : ∀ x : X, x ∉ Set.range j.base →
      IsConnectedPuncturedStrictHenselization (X.presheaf.stalk x)) :
    Nonempty (finiteEtaleBaseChange j).FullyFaithful
```

## Tag 0BQG, a lemma

[Tag 0BQG](https://stacks.math.columbia.edu/tag/0BQG) in the Stacks Project.

**`AlgebraicGeometry.fullyFaithful_finiteEtaleBaseChange_of_finite_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/DenseOpenFinitelyManyComponents.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/DenseOpenFinitelyManyComponents.lean#L606). References: SGA 7 II (2.3.1), “partial”.

> **Stacks Project, Tag 0BQG.** Let `U` be a dense open subscheme of a scheme `X` such that
> every quasi-compact open of `X` has only finitely many irreducible components, and such that for
> every point `x` of `X` outside `U` the punctured spectrum of every strict henselization of
> `𝒪_{X, x}` is connected.  Then base change of finite étale covers along `U ⟶ X` is fully
> faithful.
>
> Faithfulness holds because a dense open inclusion is dominant (Stacks 0BQE).  For fullness, a
> morphism between the restrictions to `U` of two covers `Y` and `Z` is a section over `U` of the
> finite étale internal Hom scheme `Hom_X(Y, Z)`; that section extends to a section over `X`, which
> is read back as a morphism of covers over `X`.

```lean
theorem fullyFaithful_finiteEtaleBaseChange_of_finite_irreducibleComponents
    (X : Scheme.{u}) (U : X.Opens)
    (hfinite : ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite)
    (hU : Dense (U : Set X))
    (hconn : ∀ x : X, x ∉ U →
      IsConnectedPuncturedStrictHenselization (X.presheaf.stalk x)) :
    Nonempty (finiteEtaleBaseChange U.ι).FullyFaithful
```

## Tag 0BSB, a lemma

[Tag 0BSB](https://stacks.math.columbia.edu/tag/0BSB) in the Stacks Project.

**`AlgebraicGeometry.isExactSequence_etaleFundamentalGroupMap_puncturedSpectrum_of_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/PuncturedSpectrumDescent/Exact.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/PuncturedSpectrumDescent/Exact.lean#L559). The attribute's comment: “the full exact sequence, with the descent half discharged”.

> **Stacks Project, Tag 0BSB.** Let `(A, 𝔪)` be a local ring whose punctured spectrum
> `U = Spec A ∖ {𝔪}` is retrocompact, let `Aˢʰ` be a strict henselization of `A` whose punctured
> spectrum `Uˢʰ` is connected, and let `ū` be a geometric point of `Uˢʰ`. Then
>
> ```
> π₁(Uˢʰ, ū) → π₁(U, ū) → π₁(X, ū) → 1
> ```
>
> is exact: `π₁(U) → π₁(X)` is surjective, the composite is trivial, and the kernel of
> `π₁(U) → π₁(X)` is the smallest closed normal subgroup containing the image of `π₁(Uˢʰ)`.

```lean
theorem isExactSequence_etaleFundamentalGroupMap_puncturedSpectrum_of_quasiCompact
    (hAsh : Stacks.StrictHenselization.IsStrictHenselization A κsep Ash)
    (hconnected : _root_.IsConnected ({closedPoint Ash}ᶜ : Set (PrimeSpectrum Ash)))
    [QuasiCompact (puncturedSpectrum A).ι]
    (w : GeometricPoint
      (Spec.map (CommRingCat.ofHom (algebraMap A Ash)) ⁻¹ᵁ puncturedSpectrum A).toScheme) :
    letI : ConnectedSpace (Spec (CommRingCat.of A)) := connectedSpace_spec_of_isLocalRing A
    letI : ConnectedSpace (puncturedSpectrum A).toScheme :=
      connectedSpace_puncturedSpectrum_of_isStrictHenselization A κsep Ash hAsh hconnected
    letI : ConnectedSpace
        (Spec.map (CommRingCat.ofHom (algebraMap A Ash)) ⁻¹ᵁ puncturedSpectrum A) :=
      connectedSpace_preimage_puncturedSpectrum_of_isStrictHenselization A κsep Ash hAsh
        hconnected
    IsExactSequence
      (etaleFundamentalGroupMap
        (Spec.map (CommRingCat.ofHom (algebraMap A Ash)) ∣_ puncturedSpectrum A) w)
      (etaleFundamentalGroupMap (puncturedSpectrum A).ι
        (w.map (Spec.map (CommRingCat.ofHom (algebraMap A Ash)) ∣_ puncturedSpectrum A)))
```

**`AlgebraicGeometry.connectedSpace_puncturedSpectrum_of_isStrictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/PuncturedSpectrumExactSequence.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/PuncturedSpectrumExactSequence.lean#L166). The attribute's comment: “connectedness of `U`, implicit since `π₁(U, ū)` appears in the statement”.

> **Connectedness of `U` in Stacks Project, Tag 0BSB.** The punctured spectrum of `A` is
> connected as soon as the punctured spectrum of a strict henselization `Aˢʰ` is: the latter is the
> preimage of the former under the faithfully flat `Spec Aˢʰ ⟶ Spec A`, so the restriction
> `Uˢʰ ⟶ U` is surjective and connectedness transfers along it. This is implicit in the statement
> of the tag, since `π₁(U, ū)` appears in it.

```lean
theorem connectedSpace_puncturedSpectrum_of_isStrictHenselization
    (hAsh : Stacks.StrictHenselization.IsStrictHenselization A κsep Ash)
    (hconnected : _root_.IsConnected ({closedPoint Ash}ᶜ : Set (PrimeSpectrum Ash))) :
    ConnectedSpace (puncturedSpectrum A).toScheme
```

**`AlgebraicGeometry.etaleFundamentalGroupMap_comp_eq_one_puncturedSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/PuncturedSpectrumExactSequence.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/PuncturedSpectrumExactSequence.lean#L251). The attribute's comment: “triviality of the composite `π₁(Uˢʰ) → π₁(U) → π₁(X)` only”.

> **Triviality of the composite in Stacks Project, Tag 0BSB.** Let `(A, 𝔪)` be a local ring,
> `X = Spec A`, `U = X ∖ {𝔪}` the punctured spectrum, `Aˢʰ` a strict henselization of `A` and
> `Uˢʰ` its punctured spectrum, presented as the preimage of `U`. If `Uˢʰ` is connected then the
> composite
>
> ```
> π₁(Uˢʰ, ū) ⟶ π₁(U, ū) ⟶ π₁(X, ū)
> ```
>
> is the trivial homomorphism. This is the complex condition of the exact sequence asserted by the
> tag; it is Stacks 0BS8 applied to the composite base-change functor, which lands in finite
> coproducts of copies of `Uˢʰ` by
> `AlgebraicGeometry.isFiniteCoproductOfTerminal_finiteEtaleBaseChange_puncturedSpectrum`.
>
> The quasi-compactness of `U` assumed by the tag is not needed for this assertion; it enters only
> the descent half of the source's proof, which is the remaining obligation of
> `AlgebraicGeometry.isExactSequence_etaleFundamentalGroupMap_puncturedSpectrum`.

```lean
theorem etaleFundamentalGroupMap_comp_eq_one_puncturedSpectrum
    (hAsh : Stacks.StrictHenselization.IsStrictHenselization A κsep Ash)
    (hconnected : _root_.IsConnected ({closedPoint Ash}ᶜ : Set (PrimeSpectrum Ash)))
    (w : GeometricPoint
      (Spec.map (CommRingCat.ofHom (algebraMap A Ash)) ⁻¹ᵁ puncturedSpectrum A).toScheme) :
    letI : ConnectedSpace (Spec (.of A)) := connectedSpace_spec_of_isLocalRing A
    letI : ConnectedSpace (puncturedSpectrum A).toScheme :=
      connectedSpace_puncturedSpectrum_of_isStrictHenselization A κsep Ash hAsh hconnected
    letI : ConnectedSpace
        (Spec.map (CommRingCat.ofHom (algebraMap A Ash)) ⁻¹ᵁ puncturedSpectrum A) :=
      connectedSpace_preimage_puncturedSpectrum_of_isStrictHenselization A κsep Ash hAsh
        hconnected
    (etaleFundamentalGroupMap (puncturedSpectrum A).ι
          (w.map (Spec.map (CommRingCat.ofHom (algebraMap A Ash)) ∣_
            puncturedSpectrum A))).toMonoidHom.comp
        (etaleFundamentalGroupMap
          (Spec.map (CommRingCat.ofHom (algebraMap A Ash)) ∣_ puncturedSpectrum A)
          w).toMonoidHom = 1
```

**`AlgebraicGeometry.surjective_etaleFundamentalGroupMap_puncturedSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/PuncturedSpectrumExactSequence.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/PuncturedSpectrumExactSequence.lean#L293). The attribute's comment: “surjectivity of `π₁(U) → π₁(X)`, the `→ 1` of the sequence, only”.

> **Surjectivity in Stacks Project, Tag 0BSB.** Let `(A, 𝔪)` be a local ring, `X = Spec A`,
> `U = X ∖ {𝔪}` the punctured spectrum, and `Aˢʰ` a strict henselization of `A` whose punctured
> spectrum is connected. Then for every geometric point `ū` of `U` the induced homomorphism
>
> ```
> π₁(U, ū) ⟶ π₁(X, ū)
> ```
>
> is surjective. This is the criterion of Stacks 0BN6, whose second condition is full faithfulness
> of `FÉt_X ⥤ FÉt_U`, which is Stacks 0BLQ
> (`AlgebraicGeometry.fullyFaithful_finiteEtaleBaseChange_to_puncturedSpectrum`); the transport
> between the abstract automorphism groups of that criterion and the étale fundamental groups is
> `AlgebraicGeometry.autMulEquivEtaleFundamentalGroup_galoisFunctorData_hom`.
>
> The quasi-compactness of `U` assumed by the tag is not needed for this assertion; it enters only
> the descent half of the source's proof, which is the remaining obligation of
> `AlgebraicGeometry.isExactSequence_etaleFundamentalGroupMap_puncturedSpectrum`.

```lean
theorem surjective_etaleFundamentalGroupMap_puncturedSpectrum
    (hAsh : Stacks.StrictHenselization.IsStrictHenselization A κsep Ash)
    (hconnected : _root_.IsConnected ({closedPoint Ash}ᶜ : Set (PrimeSpectrum Ash)))
    (u : GeometricPoint (puncturedSpectrum A).toScheme) :
    letI : ConnectedSpace (Spec (.of A)) := connectedSpace_spec_of_isLocalRing A
    letI : ConnectedSpace (puncturedSpectrum A).toScheme :=
      connectedSpace_puncturedSpectrum_of_isStrictHenselization A κsep Ash hAsh hconnected
    Function.Surjective (etaleFundamentalGroupMap (puncturedSpectrum A).ι u)
```

## Tag 0BQH, an equation

[Tag 0BQH](https://stacks.math.columbia.edu/tag/0BQH) in the Stacks Project.

**`AlgebraicGeometry.galoisToFundamentalGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GenericPoint.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GenericPoint.lean#L44). References: SGA 7 XIX (1.4), “partial”.

> The canonical continuous homomorphism from the absolute Galois group of the function field of
> an irreducible scheme to its étale fundamental group, based at a geometric generic point.

```lean
def galoisToFundamentalGroup
    (X : Scheme.{u}) [IrreducibleSpace X]
    (L Ω : Type u) [Field L] [Field Ω]
    [Algebra (X.residueField (genericPoint X)) L]
    [IsSepClosure (X.residueField (genericPoint X)) L]
    [Algebra L Ω] [Algebra (X.residueField (genericPoint X)) Ω]
    [IsScalarTower (X.residueField (genericPoint X)) L Ω]
    [IsAlgClosed Ω]
    [Algebra.IsAlgebraic (X.residueField (genericPoint X)) Ω] :
    Gal(L / X.residueField (genericPoint X)) →ₜ*
      EtaleFundamentalGroup X
        ((algebraicClosureGeometricPoint
          (X.residueField (genericPoint X)) Ω).map
          (X.fromSpecResidueField (genericPoint X)))
```

## Tag 0BQI, a lemma

[Tag 0BQI](https://stacks.math.columbia.edu/tag/0BQI) in the Stacks Project.

**`AlgebraicGeometry.surjective_etaleFundamentalGroupMap_opensι_of_isGeometricallyUnibranch`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/GeometricallyUnibranch.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/GeometricallyUnibranch.lean#L349). The attribute's comment: “the claim for a nonempty open subscheme, that π₁(U, ū) → π₁(X, ū) is surjective; the claim for the generic point is `surjective_galoisToFundamentalGroup_of_isGeometricallyUnibranch`”.

> Let `X` be an irreducible, geometrically unibranch
> scheme, let `U ⊆ X` be a nonempty open subscheme and let `ū` be a geometric point of `U`. The
> canonical homomorphism
>
> ```
> π₁(U, ū) ⟶ π₁(X, ū)
> ```
>
> of étale fundamental groups is surjective. Equivalently, every connected finite étale cover of `X`
> stays connected over `U`.

```lean
theorem surjective_etaleFundamentalGroupMap_opensι_of_isGeometricallyUnibranch
    (X : Scheme.{u}) [IrreducibleSpace X] (hX : IsGeometricallyUnibranch X)
    (U : X.Opens) [Nonempty U] (x : GeometricPoint U.toScheme) :
    Function.Surjective (etaleFundamentalGroupMap U.ι x)
```

**`AlgebraicGeometry.surjective_galoisToFundamentalGroup_of_isGeometricallyUnibranch`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/GeometricallyUnibranch.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/GeometricallyUnibranch.lean#L450). The attribute's comment: “the claim for the generic point, that the map π₁(η, η̄) → π₁(X, η̄) of Tag 0BQH is surjective; the claim for a nonempty open subscheme is `surjective_etaleFundamentalGroupMap_opensι_of_isGeometricallyUnibranch`”. References: SGA 1 V (8.2), “special case”.

> Let `X` be an irreducible, geometrically unibranch
> scheme with function field `K = κ(η)` at its generic point `η`, let `L` be a separable closure of
> `K` and let `Ω` be an algebraically closed algebraic extension of `K` containing `L`. The
> canonical continuous homomorphism
>
> ```
> Gal(L / K) = π₁(η, η̄) ⟶ π₁(X, η̄)
> ```
>
> is surjective.

```lean
theorem surjective_galoisToFundamentalGroup_of_isGeometricallyUnibranch
    (X : Scheme.{u}) [IrreducibleSpace X] (hX : IsGeometricallyUnibranch X)
    (L Ω : Type u) [Field L] [Field Ω]
    [Algebra (X.residueField (genericPoint X)) L]
    [IsSepClosure (X.residueField (genericPoint X)) L]
    [Algebra L Ω] [Algebra (X.residueField (genericPoint X)) Ω]
    [IsScalarTower (X.residueField (genericPoint X)) L Ω]
    [IsAlgClosed Ω] [Algebra.IsAlgebraic (X.residueField (genericPoint X)) Ω] :
    Function.Surjective (galoisToFundamentalGroup X L Ω)
```

## Tag 0BSC, a lemma

[Tag 0BSC](https://stacks.math.columbia.edu/tag/0BSC) in the Stacks Project.

**`AlgebraicGeometry.surjective_etaleFundamentalGroupMap_of_finite_isClosed_compl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/FinitelyManyClosedPoints.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/FinitelyManyClosedPoints.lean#L170). The attribute's comment: “the surjectivity clause `π₁(U) → π₁(X)` for `U` the complement of finitely many closed points, under hypotheses (1) and (2); the kernel description is not proved here”.

> **Surjectivity of `π₁(U) → π₁(X)` for the complement of finitely many closed points.** Let
> `X` be a connected scheme, let
> `x₁, …, xₙ ∈ X` be finitely many closed points, and let `U = X ∖ {x₁, …, xₙ}`, presented as an
> open immersion `j : U ⟶ X` whose image has finite complement consisting of closed points.
> Assume that
>
> 1. `U` is connected and retrocompact in `X` — `[ConnectedSpace U]` and `[QuasiCompact j]`;
> 2. for each `i` the punctured spectrum of the strict henselization of `𝒪_{X,xᵢ}` is connected —
>    `hconnected`.
>
> Then for every geometric point `ū` of `U` the induced continuous homomorphism
>
> ```
> π₁(U, ū) ⟶ π₁(X, ū)
> ```
>
> is surjective; equivalently, every connected finite étale cover of `X` stays connected over `U`.

```lean
theorem surjective_etaleFundamentalGroupMap_of_finite_isClosed_compl
    {U X : Scheme.{u}} (j : U ⟶ X) [ConnectedSpace U] [ConnectedSpace X] [IsOpenImmersion j]
    [QuasiCompact j]
    (hfinite : ((Set.range j.base)ᶜ : Set X).Finite)
    (hclosed : ∀ x : X, x ∉ Set.range j.base → IsClosed ({x} : Set X))
    (hconnected : ∀ x : X, x ∉ Set.range j.base →
      IsConnectedPuncturedStrictHenselization (X.presheaf.stalk x))
    (u : GeometricPoint U) :
    Function.Surjective (etaleFundamentalGroupMap j u)
```

**`AlgebraicGeometry.ker_etaleFundamentalGroupMap_eq_closedNormalClosure_biUnion_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/FinitePointKernel.lean, line 705](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/FinitePointKernel.lean#L705). The attribute's comment: “the kernel clause, in union-of-images form, with the factorisation `Uᵢˢʰ ⟶ U` proved; the removed points are assumed pairwise distinct, and hypothesis (2) is stated at the stalks of the stages of the chain, where it is used”. References: SGA 7 II (2.3.1), “partial”.

> **The kernel of `π₁(U) ⟶ π₁(X)`.** Let `X` be a connected scheme, let
> `x₀, …, xₙ₋₁ ∈ X` be pairwise distinct closed points and let `U = X ∖ {x₀, …, xₙ₋₁}`, assumed
> connected and retrocompact in `X`. Let `Aᵢˢʰ` be a strict henselization of the local ring at `xᵢ`
> and let `Uᵢˢʰ` be the preimage of the complement of `xᵢ` in `Spec Aᵢˢʰ`, that is, the punctured
> spectrum of `Aᵢˢʰ`; assume every punctured spectrum of every strict henselization of that local
> ring is connected. Let `ū` be a geometric point of `U`, let `ūᵢ` be a geometric point of `Uᵢˢʰ`
> and let `s i` compare the geometric fibre functors of `U` at the image of `ūᵢ` and at `ū`. Then
>
> ```
> ker (π₁(U, ū) ⟶ π₁(X, ū))
> ```
>
> is the smallest closed normal subgroup of `π₁(U, ū)` containing the images of the maps
> `π₁(Uᵢˢʰ, ūᵢ) ⟶ π₁(U, ū)`, each read through `s i`.

```lean
theorem ker_etaleFundamentalGroupMap_eq_closedNormalClosure_biUnion_range
    [ConnectedSpace X] [ConnectedSpace (chainOpen x hclosed 0).toScheme]
    [QuasiCompact (chainOpen x hclosed 0).ι]
    (hconn : ∀ (j : ℕ) (y : (chainOpen x hclosed (j + 1)).toScheme),
      y ∉ Set.range (chainStep x hclosed j).base →
        IsConnectedPuncturedStrictHenselization
          ↥((chainOpen x hclosed (j + 1)).toScheme.presheaf.stalk y))
    (κsep : Fin n → Type u) [∀ i, Field (κsep i)]
    [∀ i, Algebra (maximalIdeal ↥(chainStalk x hclosed hinj i)).ResidueField (κsep i)]
    [∀ i, IsSepClosure (maximalIdeal ↥(chainStalk x hclosed hinj i)).ResidueField (κsep i)]
    (Ash : Fin n → Type u) [∀ i, CommRing (Ash i)] [∀ i, IsLocalRing (Ash i)]
    [∀ i, Algebra ↥(chainStalk x hclosed hinj i) (Ash i)]
    (hAsh : ∀ i, Stacks.StrictHenselization.IsStrictHenselization
      ↥(chainStalk x hclosed hinj i) (κsep i) (Ash i))
    (u : GeometricPoint (chainOpen x hclosed 0).toScheme)
    (w : ∀ i, GeometricPoint (chainLocalPunctured x hclosed hinj i (Ash i)).toScheme)
    (s : ∀ i, finiteEtaleFiberFunctor ((w i).map (chainLocalLift x hclosed hinj i (Ash i))) ≅
      finiteEtaleFiberFunctor u) :
    letI : ∀ i : Fin n, ConnectedSpace (chainLocalPunctured x hclosed hinj i (Ash i)) :=
      fun i ↦ connectedSpace_preimage_puncturedOpen_of_isStrictHenselization
        (isClosed_chainRemovedPoint x hclosed hinj i) (κsep i) (Ash i) (hAsh i)
        (hconn (i : ℕ) (chainRemovedPoint x hclosed hinj i)
          (notMem_range_chainStep x hclosed hinj i) (κsep i) (Ash i) (hAsh i))
    MonoidHom.ker (etaleFundamentalGroupMap (chainOpen x hclosed 0).ι u).toMonoidHom =
      (Subgroup.normalClosure (⋃ i : Fin n, Set.range
        ((etaleFundamentalGroupChange (s i)).comp
          (etaleFundamentalGroupMap (chainLocalLift x hclosed hinj i (Ash i))
            (w i))))).topologicalClosure
```

**`AlgebraicGeometry.surjective_and_ker_etaleFundamentalGroupMap_of_finite_isClosed_compl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/FinitePointKernel.lean, line 888](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalConnectedness/FinitePointKernel.lean#L888). The attribute's comment: “both clauses, surjectivity and the kernel, under one set of hypotheses; the removed points are assumed pairwise distinct, and hypothesis (2) is stated at the stalks of the stages of the chain, where it is used”.

> Let `X` be a connected scheme, let
> `x₀, …, xₙ₋₁ ∈ X` be pairwise distinct closed points and let `U = X ∖ {x₀, …, xₙ₋₁}`, which is
> `AlgebraicGeometry.chainOpen x hclosed 0`. Assume
>
> 1. `U` is connected and retrocompact in `X` — `[ConnectedSpace (chainOpen x hclosed 0).toScheme]`
>    and `[QuasiCompact (chainOpen x hclosed 0).ι]`;
> 2. for each `i` the punctured spectrum `Uᵢˢʰ` of the strict henselization of the local ring at
>    `xᵢ` is connected — `hconn`.
>
> Then for every geometric point `ū` of `U` the map `π₁(U, ū) ⟶ π₁(X, ū)` is surjective, and its
> kernel is the smallest closed normal subgroup of `π₁(U, ū)` containing the images of the maps
> `π₁(Uᵢˢʰ, ūᵢ) ⟶ π₁(U, ū)` for `i = 0, …, n - 1`.

```lean
theorem surjective_and_ker_etaleFundamentalGroupMap_of_finite_isClosed_compl
    [ConnectedSpace X] [ConnectedSpace (chainOpen x hclosed 0).toScheme]
    [QuasiCompact (chainOpen x hclosed 0).ι]
    (hconn : ∀ (j : ℕ) (y : (chainOpen x hclosed (j + 1)).toScheme),
      y ∉ Set.range (chainStep x hclosed j).base →
        IsConnectedPuncturedStrictHenselization
          ↥((chainOpen x hclosed (j + 1)).toScheme.presheaf.stalk y))
    (κsep : Fin n → Type u) [∀ i, Field (κsep i)]
    [∀ i, Algebra (maximalIdeal ↥(chainStalk x hclosed hinj i)).ResidueField (κsep i)]
    [∀ i, IsSepClosure (maximalIdeal ↥(chainStalk x hclosed hinj i)).ResidueField (κsep i)]
    (Ash : Fin n → Type u) [∀ i, CommRing (Ash i)] [∀ i, IsLocalRing (Ash i)]
    [∀ i, Algebra ↥(chainStalk x hclosed hinj i) (Ash i)]
    (hAsh : ∀ i, Stacks.StrictHenselization.IsStrictHenselization
      ↥(chainStalk x hclosed hinj i) (κsep i) (Ash i))
    (u : GeometricPoint (chainOpen x hclosed 0).toScheme)
    (w : ∀ i, GeometricPoint (chainLocalPunctured x hclosed hinj i (Ash i)).toScheme)
    (s : ∀ i, finiteEtaleFiberFunctor ((w i).map (chainLocalLift x hclosed hinj i (Ash i))) ≅
      finiteEtaleFiberFunctor u) :
    letI : ∀ i : Fin n, ConnectedSpace (chainLocalPunctured x hclosed hinj i (Ash i)) :=
      fun i ↦ connectedSpace_preimage_puncturedOpen_of_isStrictHenselization
        (isClosed_chainRemovedPoint x hclosed hinj i) (κsep i) (Ash i) (hAsh i)
        (hconn (i : ℕ) (chainRemovedPoint x hclosed hinj i)
          (notMem_range_chainStep x hclosed hinj i) (κsep i) (Ash i) (hAsh i))
    Function.Surjective (etaleFundamentalGroupMap (chainOpen x hclosed 0).ι u) ∧
      MonoidHom.ker (etaleFundamentalGroupMap (chainOpen x hclosed 0).ι u).toMonoidHom =
        (Subgroup.normalClosure (⋃ i : Fin n, Set.range
          ((etaleFundamentalGroupChange (s i)).comp
            (etaleFundamentalGroupMap (chainLocalLift x hclosed hinj i (Ash i))
              (w i))))).topologicalClosure
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.10, Tag 0BQD](https://stacks.math.columbia.edu/tag/0BQD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
