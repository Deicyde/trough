---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.IsPerfectRelativeTo, AlgebraicGeometry.Scheme.Hom.IsRelativelyPerfect, AlgebraicGeometry.isPerfectRelativeTo_dualNumberResidueComplex_and_not_isPerfect, AlgebraicGeometry.isBounded_and_isPseudoCoherent_iff_boundedCoherent, AlgebraicGeometry.isPerfectRelativeTo_canonical_iff_isBounded_and_isPseudoCoherent, AlgebraicGeometry.isPerfectRelativeTo_canonical_iff_boundedCoherent, AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_tfae, AlgebraicGeometry.pseudoCoherent_derivedSections_tfae
statement: formalized
proof: formalized
---

# 36.35 Relatively perfect objects

Section 36.35 of the Stacks Project, [Tag 0DHZ](https://stacks.math.columbia.edu/tag/0DHZ). 15 tags here are carried by 35 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DHZ, the section

[Tag 0DHZ](https://stacks.math.columbia.edu/tag/0DHZ) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsPerfectRelativeTo`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectObject.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectObject.lean#L83). The attribute's comment: “the notion of a relatively perfect object, for a morphism flat and locally of finite presentation, generalised to an arbitrary family of certificates”. References: SGA 6 III (4.1), “flat, l.f.p. case”.

> **A generalisation of Stacks 0DI0.** An object `E` of `D(𝒪_X)` is perfect relative to `S`
> when it is pseudo-coherent and, after restriction of scalars along `f^{-1}𝒪_S ⟶ 𝒪_X`, locally
> has finite Tor dimension on the inverse-image ringed space `(X, f^{-1}𝒪_S)`.
>
> The derived tensor product is read off the family of certificates `D`, one on each open subspace
> of the inverse-image ringed space, as in part (3) of Stacks 08CG. Since the underived half of a
> certificate is free data, this is weaker than Stacks 0DI0 at a general `D`, and it is
> Stacks 0DI0 — `AlgebraicGeometry.Scheme.Hom.IsRelativelyPerfect` — exactly when `D` is pinned to
> the tensor product of sheaves of modules; see
> `AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_iff_isRelativelyPerfect`.

```lean
public def IsPerfectRelativeTo [Flat f] [LocallyOfFinitePresentation f]
    (D : ∀ U : TopologicalSpace.Opens
        (RingedSpace.inverseImage S.toRingedSpace f.base).carrier,
      RingedSpace.CertifiedDerivedSheafTensoring.{d', u}
        ((RingedSpace.inverseImage S.toRingedSpace f.base).restrict U.isOpenEmbedding))
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace)) : Prop
```

## Tag 0DI0, a definition

[Tag 0DI0](https://stacks.math.columbia.edu/tag/0DI0) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsRelativelyPerfect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectObjectCanonical.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectObjectCanonical.lean#L90).

> An object `E` of `D(𝒪_X)` is perfect relative to `S` when it is pseudo-coherent and, after
> restriction of scalars along `f^{-1}𝒪_S ⟶ 𝒪_X`, locally has finite Tor dimension on the
> inverse-image ringed space `(X, f^{-1}𝒪_S)`.
>
> Pseudo-coherence is part (3) of Stacks 08CB, and local finiteness of the Tor dimension is part (3)
> of Stacks 08CG taken against the derived tensor product `- ⊗^{L}_{f^{-1}𝒪_S} -` of Stacks 06YU on
> each open subspace, the total left derived functor of the tensor product of sheaves of modules.

```lean
public def IsRelativelyPerfect [Flat f] [LocallyOfFinitePresentation f]
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace)) : Prop
```

## Tag 0DI1, an example

[Tag 0DI1](https://stacks.math.columbia.edu/tag/0DI1) in the Stacks Project.

**`AlgebraicGeometry.isPerfectRelativeTo_dualNumberResidueComplex_and_not_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectNotFibrewise.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectNotFibrewise.lean#L149). The attribute's comment: “relative perfectness over a field is not perfectness on the fibres”.

> **Stacks 0DI1, the closing warning.** Over a field, relative perfectness is not perfectness
> on the fibres: the residue field of the dual numbers, sheafified and placed in degree zero, is
> `Spec k`-perfect on the scheme `Spec k[ε]` — which is of finite presentation over `k`, and whose
> only fibre over `Spec k` is itself — and it is not a perfect object of `D(𝒪_{Spec k[ε]})`.
>
> The first half is Stacks 0DI1 itself,
> `AlgebraicGeometry.isPerfectRelativeTo_canonical_iff_boundedCoherent`, applied to a coherent
> module in degree zero. The second is Stacks 08EB,
> `AlgebraicGeometry.isPerfect_tilde_iff`, against
> `AlgebraicGeometry.not_isPerfectModule_residueField_dualNumber`.

```lean
public theorem isPerfectRelativeTo_dualNumberResidueComplex_and_not_isPerfect (k : Type u)
    [Field k] :
    (dualNumberStructureMap k).IsPerfectRelativeTo
        (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
          (RingedSpace.inverseImage (Spec (CommRingCat.of k)).toRingedSpace
            (dualNumberStructureMap k).base))
        (dualNumberResidueComplex k) ∧
      ¬ Stacks.Cohomology.PerfectComplexes.IsPerfect
          (X := (Spec (CommRingCat.of (DualNumber k))).toRingedSpace)
          (dualNumberResidueComplex k)
```

**`AlgebraicGeometry.isBounded_and_isPseudoCoherent_iff_boundedCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectOverField.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectOverField.lean#L461). The attribute's comment: “bounded pseudo-coherent objects are the bounded coherent ones”.

> **Stacks 0DI1, second equivalence, via Stacks 08E8.** On a Noetherian scheme an object of
> `D(𝒪_X)` is bounded and pseudo-coherent if and only if it lies in `D^b_Coh(𝒪_X)`, that is,
> if and only if it is bounded and all of its cohomology sheaves are coherent.
>
> Together with
> `AlgebraicGeometry.isPerfectRelativeTo_canonical_iff_isBounded_and_isPseudoCoherent` and
> `AlgebraicGeometry.isNoetherian_of_finitePresentation_over_field` this identifies the objects of
> `D(𝒪_X)` perfect relative to a field with `D^b_Coh(𝒪_X)`; see
> `AlgebraicGeometry.isPerfectRelativeTo_canonical_iff_boundedCoherent`.
>
> Stacks 08E8 cuts `D^b_Coh(𝒪_X)` out inside `D_QCoh(𝒪_X)`, and both sides here
> imply quasi-coherence of the cohomology sheaves: on the left it is Stacks 08E5 for a pseudo-coherent
> object,
> `AlgebraicGeometry.isQuasicoherentDerived_of_isPseudoCoherent`, and on the right it is Stacks
> 01BW, `isQuasicoherent_of_isCoherent`, applied degreewise.

```lean
public theorem isBounded_and_isPseudoCoherent_iff_boundedCoherent (X : Scheme.{u})
    [IsNoetherian X] (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace)) :
    (DerivedCategoryB.IsBounded E ∧ RingedSpace.IsPseudoCoherent E) ↔
      DerivedCategoryB.derivedCategoryBBounded
        (fun M : OXMod.{u, u} X.toRingedSpace => M.IsCoherent) E
```

**`AlgebraicGeometry.isPerfectRelativeTo_canonical_iff_isBounded_and_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectOverField.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectOverField.lean#L503). The attribute's comment: “first equivalence: at the 06YU derived tensor product, relative perfectness over a field is boundedness and pseudo-coherence”.

> **Stacks 0DI1, first equivalence, at the genuine derived tensor product.** Let `k` be a field
> and let `X` be a scheme of finite presentation over `k`. An object `E` of `D(𝒪_X)` is perfect
> relative to `Spec k` — read at the derived tensor product of Stacks 06YU on each open subspace of
> `(X, f⁻¹𝒪_{Spec k})`, which is
> `AlgebraicGeometry.RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily` — if and only if it
> is bounded and pseudo-coherent.
>
> This is `AlgebraicGeometry.isPerfectRelativeTo_iff_isBounded_and_isPseudoCoherent` at the
> canonical family, whose underived operation *is* `- ⊗_{f⁻¹𝒪_{Spec k}} -` by `rfl`.

```lean
public theorem isPerfectRelativeTo_canonical_iff_isBounded_and_isPseudoCoherent (k : Type u)
    [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [LocallyOfFinitePresentation f]
    [QuasiCompact f] (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace)) :
    f.IsPerfectRelativeTo
        (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
          (RingedSpace.inverseImage (Spec (.of k)).toRingedSpace f.base)) E ↔
      (DerivedCategoryB.IsBounded E ∧ RingedSpace.IsPseudoCoherent E)
```

**`AlgebraicGeometry.isPerfectRelativeTo_canonical_iff_boundedCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectOverField.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectOverField.lean#L523). The attribute's comment: “the `Spec k`-perfect objects are exactly `D^b_Coh(𝒪_X)`”.

> **Stacks 0DI1.** Let `k` be a field and let `X` be a scheme of finite presentation over `k`.
> An object `E` of `D(𝒪_X)` is `Spec k`-perfect if and only if it lies in `D^b_Coh(𝒪_X)`, that is,
> if and only if it is bounded with coherent cohomology sheaves.
>
> This is the example in one statement: relative perfectness is read at the derived tensor product
> of Stacks 06YU, and the cohomology sheaves are quasi-coherent by Stacks 08E5 and 01BW. It is the
> composite of
> `AlgebraicGeometry.isPerfectRelativeTo_canonical_iff_isBounded_and_isPseudoCoherent` with
> `AlgebraicGeometry.isBounded_and_isPseudoCoherent_iff_boundedCoherent`, the scheme being
> Noetherian by `AlgebraicGeometry.isNoetherian_of_finitePresentation_over_field`.

```lean
public theorem isPerfectRelativeTo_canonical_iff_boundedCoherent (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [LocallyOfFinitePresentation f] [QuasiCompact f]
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace)) :
    f.IsPerfectRelativeTo
        (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
          (RingedSpace.inverseImage (Spec (.of k)).toRingedSpace f.base)) E ↔
      DerivedCategoryB.derivedCategoryBBounded
        (fun M : OXMod.{u, u} X.toRingedSpace => M.IsCoherent) E
```

## Tag 0DI2, a lemma

[Tag 0DI2](https://stacks.math.columbia.edu/tag/0DI2) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectAffineCriterion.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectAffineCriterion.lean#L72).

> **Stacks 0DI2.** Let `f : X ⟶ S` be a morphism of schemes which is flat and locally of finite
> presentation, and let `E` be an object of the derived category of `𝒪_X`-modules all of whose
> cohomology sheaves are quasi-coherent. The following are equivalent:
>
> 1. `E` is `S`-perfect;
> 2. for every affine open `U ⊆ X` mapping into an affine open `V ⊆ S`, the complex `RΓ(U, E)` is
>    `𝒪_S(V)`-perfect;
> 3. there are an affine open covering `S = ⋃ V i` and, for each `i`, an affine open covering
>    `f⁻¹(V i) = ⋃ U i j` such that `RΓ(U i j, E)` is `𝒪_S(V i)`-perfect.
>
> `S`-perfectness is read at the derived tensor product of Stacks 06YU on the open subspaces of
> `(X, f⁻¹𝒪_S)`, and `𝒪_S(V)`-perfectness of `RΓ(U, E)` is Stacks 0DHS for the chart ring map
> `f.appLE V U e`, which is flat and of finite presentation.

```lean
public theorem isPerfectRelativeTo_tfae [Flat f] [LocallyOfFinitePresentation f]
    (E : DerivedCategory X.Modules)
    (hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj E).IsQuasicoherent) :
    List.TFAE
      [IsPerfectRelativeTo f
          (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
            (RingedSpace.inverseImage S.toRingedSpace f.base)) E,
        ∀ (U : X.Opens) (hU : IsAffineOpen U) (V : S.Opens) (hV : IsAffineOpen V)
          (e : U ≤ f ⁻¹ᵁ V), SectionsRelativelyPerfect f E hV hU e,
        ∃ (ι : Type u) (V : ι → S.affineOpens),
          (⨆ i, (V i : S.Opens)) = ⊤ ∧
            ∀ i, ∃ (κ : Type u) (U : κ → X.affineOpens) (hle : ∀ j, (U j).1 ≤ f ⁻¹ᵁ (V i).1),
              (⨆ j, (U j : X.Opens)) = f ⁻¹ᵁ (V i).1 ∧
                ∀ j, SectionsRelativelyPerfect f E (V i).2 (U j).2 (hle j)]
```

**`AlgebraicGeometry.pseudoCoherent_derivedSections_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectDerivedSections.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectDerivedSections.lean#L150). The attribute's comment: “the pseudo-coherence clause”.

> **Stacks 0DI2, the pseudo-coherence clause.** Let `f : X ⟶ S` be a morphism of schemes and
> let `E` be an object of the derived category of `𝒪_X`-modules all of whose cohomology sheaves are
> quasi-coherent. Then the following are equivalent:
>
> 1. `E` is a pseudo-coherent object of `D(𝒪_X)`;
> 2. for every affine open `U ⊆ X` whose image lies in an affine open `V ⊆ S`, the complex of
>    `Γ(X, U)`-modules `RΓ(U, E)` is pseudo-coherent;
> 3. there are an affine open covering of `S` and, over each of its members `V i`, an affine open
>    covering of `f ⁻¹ᵁ V i` such that `RΓ(U, E)` is pseudo-coherent for each member `U` of the
>    latter.
>
> This is the first of the two clauses of relative perfectness, with the part of the source's
> proof that concerns it: pseudo-coherence of `E` is the pseudo-coherence over `Γ(X, U)` of
> `RΓ(U, E)`, by Stacks 08E7 and the affine presentation of `E|_U` of Stacks 06Z0, and the
> condition is local on `X`. Together with the second clause, locally finite Tor dimension over
> `f^{-1}𝒪_S`, this is assembled into Stacks 0DI2 in
> `AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_tfae`.

```lean
public theorem pseudoCoherent_derivedSections_tfae (f : X ⟶ S)
    (E : DerivedCategory X.Modules)
    (hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj E).IsQuasicoherent) :
    List.TFAE
      [RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E,
        ∀ (U : X.Opens), IsAffineOpen U → ∀ (V : S.Opens), IsAffineOpen V → U ≤ f ⁻¹ᵁ V →
          StacksDraft.PseudoCoherence.IsPseudoCoherent ((derivedSectionsUnbounded X U).obj E),
        ∃ (ι : Type u) (V : ι → S.affineOpens),
          (⨆ i, (V i : S.Opens)) = ⊤ ∧
            ∀ i, ∃ (κ : Type u) (U : κ → X.affineOpens),
              (⨆ j, (U j : X.Opens)) = f ⁻¹ᵁ (V i).1 ∧
                ∀ j, StacksDraft.PseudoCoherence.IsPseudoCoherent
                  ((derivedSectionsUnbounded X (U j).1).obj E)]
```

**`AlgebraicGeometry.Scheme.Hom.exists_affineCovering_sectionsRelativelyPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectSectionsChart.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectSectionsChart.lean#L143). The attribute's comment: “the implication (2) implies (3), at the source's own module-side condition and for BOTH of its conjuncts at once: if the complex of sections over every affine open U of X mapping into an affine open V of S is O_S(V)-perfect, then there are an affine open covering of S and, over each member V, an affine open covering of the preimage of V on whose members the same condition holds. The whole three-way equivalence is AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_tfae”.

> **Stacks 0DI2**, the implication (2) ⟹ (3): if `RΓ(U, E)` is `Γ(S, V)`-perfect for every affine
> open `U ⊆ X` mapping into an affine open `V ⊆ S`, then there are an affine open covering of `S`
> and, over each of its members `V`, an affine open covering of `f⁻¹(V)` on whose members the
> condition holds.

```lean
public theorem exists_affineCovering_sectionsRelativelyPerfect [Flat f]
    [LocallyOfFinitePresentation f] (E : DerivedCategory X.Modules)
    (h : ∀ (U : X.Opens) (hU : IsAffineOpen U) (V : S.Opens) (hV : IsAffineOpen V)
      (e : U ≤ f ⁻¹ᵁ V), SectionsRelativelyPerfect f E hV hU e) :
    ∃ (ι : Type u) (V : ι → S.affineOpens),
      (⨆ i, (V i : S.Opens)) = ⊤ ∧
        ∀ i, ∃ (κ : Type u) (U : κ → X.affineOpens) (hle : ∀ j, (U j).1 ≤ f ⁻¹ᵁ (V i).1),
          (⨆ j, (U j : X.Opens)) = f ⁻¹ᵁ (V i).1 ∧
            ∀ j, SectionsRelativelyPerfect f E (V i).2 (U j).2 (hle j)
```

**`AlgebraicGeometry.Scheme.Hom.chartHasFiniteTorDimension_of_locallyHasFiniteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/TorDimensionNestedRestriction.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/TorDimensionNestedRestriction.lean#L266). The attribute's comment: “the Tor-dimension clause, the implication (1) implies (2): if E locally has finite Tor dimension over f^{-1}O_S then its restriction to every affine open U of X has finite Tor dimension over f^{-1}O_S, for the derived tensor product of Stacks 06YU. The whole three-way equivalence, at the source's module-side conditions, is AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_tfae”.

> **The implication (1) ⟹ (2) of the Tor-dimension clause of Stacks 0DI2.** If `E` locally has
> finite Tor dimension over `f⁻¹𝒪_S`, then for every affine open `U ⊆ X` the restriction `E|_U` has
> finite Tor dimension over `f⁻¹𝒪_S`.
>
> The three steps are: the certificate-carrying predicate at the canonical family is the pinned one
> (`AlgebraicGeometry.RingedSpace.locallyHasFiniteTorDimension_canonicalCertificate_iff`, which is
> `Iff.rfl`); locally finite Tor dimension is inherited by `X|_U`
> (`Stacks.Cohomology.TorAmplitude.locallyHasFiniteTorDimension_derivedRestrictModules`); and on
> `X|_U`, which is quasi-compact because `U` is affine, locally finite Tor dimension is finite Tor
> dimension (`locallyHasFiniteTorDimension_iff_hasFiniteTorDimension` of
> `AlgebraicGeometry.AffineRelativeTorAmplitude`).
>
> **The certificate family is named, not quantified.** Unlike the two implications *into* condition
> (1) of `AlgebraicGeometry.Scheme.Hom.locallyHasFiniteTorDimension_of_forall_chart` and
> `AlgebraicGeometry.Scheme.Hom.locallyHasFiniteTorDimension_of_exists_affineCovering`, this
> implication is not available for an arbitrary family: the premise is tested against the
> certificates at the members of some covering and the conclusion against the certificate at `U`,
> and a family carries no relation between its members, so at an arbitrary family the two sides
> measure Tor amplitude against unrelated operations. It is stated at the genuine derived tensor
> product of Stacks 06YU, which is what the source means; a consumer holding another family with
> the same underived halves may use
> `AlgebraicGeometry.RingedSpace.locallyHasFiniteTorDimension_iff_of_tensor_eq`.
>
> **Affineness is used only through quasi-compactness**, so the statement holds verbatim for a
> quasi-compact open; it is stated for an affine open because that is the chart condition of the
> source. The affine open `V ⊆ S` that clause (2) asks the chart to map into does not appear,
> because the sheaf-side condition does not refer to it; its module-side counterpart
> `AlgebraicGeometry.Scheme.Hom.SectionsRelativelyPerfect` does.

```lean
theorem chartHasFiniteTorDimension_of_locallyHasFiniteTorDimension
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
    (h : RingedSpace.LocallyHasFiniteTorDimension
      (RingedSpace.inverseImage S.toRingedSpace f.base)
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base))
      ((derivedScalarRestriction f).obj E))
    (U : TopologicalSpace.Opens
      (RingedSpace.inverseImage S.toRingedSpace f.base).carrier)
    (hU : IsAffineOpen (X := X) U) :
    ChartHasFiniteTorDimension f
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base)) E U
```

## Tag 0DI3, a lemma

[Tag 0DI3](https://stacks.math.columbia.edu/tag/0DI3) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isClosedUnderIsomorphisms_isPerfectRelativeTo_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectTriangulatedCanonical.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectTriangulatedCanonical.lean#L227). The attribute's comment: “the strict fullness clause, at the genuine derived tensor product”.

> **Stacks 0DI3.** Strict fullness of the `S`-perfect objects, at the derived tensor product
> of Stacks 06YU.
>
> This is `AlgebraicGeometry.Scheme.Hom.isClosedUnderIsomorphisms_isPerfectRelativeTo`, which
> holds for an arbitrary certificate family, read at the canonical one.

```lean
public theorem isClosedUnderIsomorphisms_isPerfectRelativeTo_canonical :
    (isPerfectRelativeTo f
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base))).IsClosedUnderIsomorphisms
```

**`AlgebraicGeometry.Scheme.Hom.isSaturated_isPerfectRelativeTo_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectTriangulatedCanonical.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectTriangulatedCanonical.lean#L239). The attribute's comment: “the saturation clause, at the genuine derived tensor product”.

> **Stacks 0DI3.** Saturation of the `S`-perfect objects, at the derived tensor product of
> Stacks 06YU: a direct summand of an `S`-perfect object is `S`-perfect.
>
> This is `AlgebraicGeometry.Scheme.Hom.isSaturated_isPerfectRelativeTo`, which holds for an
> arbitrary certificate family, read at the canonical one.

```lean
public theorem isSaturated_isPerfectRelativeTo_canonical :
    (isPerfectRelativeTo f
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base))).IsSaturated
```

**`AlgebraicGeometry.Scheme.Hom.isTriangulated_isPerfectRelativeTo_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectTriangulatedCanonical.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectTriangulatedCanonical.lean#L264). The attribute's comment: “the triangulated clause, at the genuine derived tensor product”.

> **Stacks 0DI3.** For a flat, locally finitely presented morphism `f : X ⟶ S` of schemes, the
> `S`-perfect objects of `D(𝒪_X)` — read at the derived tensor product of Stacks 06YU on each open
> subspace of `(X, f^{-1}𝒪_S)`, which is
> `AlgebraicGeometry.RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily` — form a
> *triangulated* subcategory: the property contains the zero object, is stable under all shifts,
> and is closed under extensions.
>
> This is `AlgebraicGeometry.Scheme.Hom.isTriangulated_isPerfectRelativeTo` at the canonical
> family: there each `- ⊗^{L} ℱ[0]` commutes with the shift and is exact, these being fields of the
> derived tensor product, and finite Tor dimension restricts to smaller opens by Tag 09U8 at the
> inclusion of one open subspace in another.
>
> The other two assertions of Stacks 0DI3 — strict fullness and saturation — hold for an arbitrary
> certificate family, and are
> `AlgebraicGeometry.Scheme.Hom.isClosedUnderIsomorphisms_isPerfectRelativeTo` and
> `AlgebraicGeometry.Scheme.Hom.isSaturated_isPerfectRelativeTo`; at the canonical family they are
> `AlgebraicGeometry.Scheme.Hom.isClosedUnderIsomorphisms_isPerfectRelativeTo_canonical` and
> `AlgebraicGeometry.Scheme.Hom.isSaturated_isPerfectRelativeTo_canonical`.

```lean
public theorem isTriangulated_isPerfectRelativeTo_canonical :
    (isPerfectRelativeTo f
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base))).IsTriangulated
```

**`AlgebraicGeometry.Scheme.Hom.isSaturated_and_isTriangulated_isPerfectRelativeTo_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectTriangulatedCanonical.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectTriangulatedCanonical.lean#L279). The attribute's comment: “the whole statement: for f flat and locally of finite presentation, the S-perfect objects of D(O_X) form a strictly full, saturated, triangulated subcategory”.

> **Stacks 0DI3.** Let `f : X ⟶ S` be a morphism of schemes which is flat and locally of finite
> presentation. The `S`-perfect objects of `D(𝒪_X)`, read at the derived tensor product of
> Stacks 06YU on each open subspace of `(X, f^{-1}𝒪_S)`, form a strictly full, saturated,
> triangulated subcategory of `D(𝒪_X)`.

```lean
public theorem isSaturated_and_isTriangulated_isPerfectRelativeTo_canonical :
    (isPerfectRelativeTo f
        (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
          (RingedSpace.inverseImage S.toRingedSpace f.base))).IsClosedUnderIsomorphisms ∧
      (isPerfectRelativeTo f
        (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
          (RingedSpace.inverseImage S.toRingedSpace f.base))).IsSaturated ∧
      (isPerfectRelativeTo f
        (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
          (RingedSpace.inverseImage S.toRingedSpace f.base))).IsTriangulated
```

## Tag 0DI4, a lemma

[Tag 0DI4](https://stacks.math.columbia.edu/tag/0DI4) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectPerfectObjects.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectPerfectObjects.lean#L333). The attribute's comment: “a perfect object is perfect relative to the base”.

> For a flat, locally finitely presented morphism of schemes `f : X ⟶ S`, every perfect object
> of `D(𝒪_X)` is perfect relative to `S`.

```lean
public theorem isPerfectRelativeTo_of_isPerfect
    (hamp : FlatRepresentativeBounds f D) (hflat : ScalarRestrictionFlat f)
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace)) (hE : RingedSpace.IsPerfect E) :
    f.IsPerfectRelativeTo D E
```

**`AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectPerfectObjects.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectPerfectObjects.lean#L503). The attribute's comment: “tensoring an S-perfect object with a perfect object”.

> For a flat, locally finitely presented morphism of schemes `f : X ⟶ S`, the derived tensor
> product of a perfect object `K` of `D(𝒪_X)` with an `S`-perfect object `M` is perfect relative
> to `S`.

```lean
public theorem isPerfectRelativeTo_derivedTensor
    (hrestricts : RingedSpace.FiniteTorDimensionRestricts
      (RingedSpace.inverseImage S.toRingedSpace f.base) D)
    (hind : StrictlyPerfectInduction.{u + 1, u})
    (hcl : Stacks.Cohomology.PseudoCoherentTensor.ComplexLevel.{u})
    (K M : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
    (Θ : ∀ (V : TopologicalSpace.Opens
          (RingedSpace.inverseImage S.toRingedSpace f.base).carrier)
        (W : TopologicalSpace.Opens X.toRingedSpace.carrier), (∀ x, x ∈ V → x ∈ W) →
      DerivedCategory (OXMod.{u, u} (X.toRingedSpace.restrict W.isOpenEmbedding)) ⥤
        DerivedCategory (OXMod.{u, u}
          ((RingedSpace.inverseImage S.toRingedSpace f.base).restrict V.isOpenEmbedding)))
    (ΘcommShift : ∀ V W h, (Θ V W h).CommShift ℤ)
    (Θtriangulated : ∀ V W h, letI := ΘcommShift V W h; (Θ V W h).IsTriangulated)
    (Θunit : ∀ V W h, (Θ V W h).obj ((DerivedCategory.singleFunctor
        (OXMod.{u, u} (X.toRingedSpace.restrict W.isOpenEmbedding)) 0).obj
          (structureModule (X.toRingedSpace.restrict W.isOpenEmbedding))) ≅
      (RingedSpace.derivedRestrictModules
        (RingedSpace.inverseImage S.toRingedSpace f.base) V).obj
          ((derivedScalarRestriction f).obj M))
    (Θtensor : ∀ (V W h) (A : DerivedCategory (OXMod.{u, u} X.toRingedSpace)),
      (Θ V W h).obj ((RingedSpace.derivedRestrictModules X.toRingedSpace W).obj A) ≅
        (RingedSpace.derivedRestrictModules
          (RingedSpace.inverseImage S.toRingedSpace f.base) V).obj
            ((derivedScalarRestriction f).obj
          (((Stacks.Cohomology.PseudoCoherentTensor.derivedTensorProduct
            X.toRingedSpace).tensor.obj A).obj M)))
    (hK : RingedSpace.IsPerfect.{u, u + 1} K)
    (hM : f.IsPerfectRelativeTo D M) :
    f.IsPerfectRelativeTo D
      (((Stacks.Cohomology.PseudoCoherentTensor.derivedTensorProduct
        X.toRingedSpace).tensor.obj K).obj M)
```

**`AlgebraicGeometry.Scheme.Hom.isRelativelyPerfect_of_isPerfect_and_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectPerfectObjectsGenuine.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectPerfectObjectsGenuine.lean#L92).

> **Stacks 0DI4.** Let `f : X ⟶ S` be a morphism of schemes which is flat and locally of finite
> presentation. A perfect object of `D(𝒪_X)` is `S`-perfect. If `K, M ∈ D(𝒪_X)`, then
> `K ⊗^{L}_{𝒪_X} M` is `S`-perfect if `K` is perfect and `M` is `S`-perfect.
>
> Here `S`-perfect is Stacks 0DI0, `AlgebraicGeometry.Scheme.Hom.IsRelativelyPerfect`, and the
> derived tensor product is the one of Stacks 06YU.

```lean
theorem isRelativelyPerfect_of_isPerfect_and_derivedTensor :
    (∀ E : DerivedCategory (OXMod.{u, u} X.toRingedSpace),
        RingedSpace.IsPerfect E → f.IsRelativelyPerfect E) ∧
      ∀ K M : DerivedCategory (OXMod.{u, u} X.toRingedSpace),
        RingedSpace.IsPerfect K → f.IsRelativelyPerfect M →
          f.IsRelativelyPerfect
            (((Stacks.Cohomology.PseudoCoherentTensor.derivedTensorProduct
              X.toRingedSpace).tensor.obj K).obj M)
```

## Tag 0DI5, a lemma

[Tag 0DI5](https://stacks.math.columbia.edu/tag/0DI5) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherent_derivedPullback_of_isPerfectRelativeTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectBaseChange.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectBaseChange.lean#L117). The attribute's comment: “the pseudo-coherence conjunct of the conclusion”.

> **The pseudo-coherence conjunct of Stacks 0DI5.** For `f : X ⟶ S` flat and locally of finite
> presentation, `g : S' ⟶ S` arbitrary, `X' = S' ×_S X` with projection `g' : X' ⟶ X`, and `K` an
> `S`-perfect object of `D(𝒪_X)`, the derived pullback `L(g')^*K` is pseudo-coherent.
>
> Only the pseudo-coherence conjunct of `AlgebraicGeometry.Scheme.Hom.IsPerfectRelativeTo` is used,
> so the family of derived tensor products on the inverse-image ringed space plays no role and is
> left arbitrary.

```lean
public theorem isPseudoCoherent_derivedPullback_of_isPerfectRelativeTo
    {X S S' X' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) (g' : X' ⟶ X) (f' : X' ⟶ S')
    [Flat f] [LocallyOfFinitePresentation f] (_hpb : IsPullback g' f' f g)
    (D : ∀ U : TopologicalSpace.Opens
        (RingedSpace.inverseImage S.toRingedSpace f.base).carrier,
      RingedSpace.CertifiedDerivedSheafTensoring.{u + 1, u}
        ((RingedSpace.inverseImage S.toRingedSpace f.base).restrict U.isOpenEmbedding))
    (K : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
    (hK : f.IsPerfectRelativeTo D K) :
    RingedSpace.IsPseudoCoherent (X := X'.toRingedSpace)
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        g'.toLRSHom.toShHom).obj K)
```

**`AlgebraicGeometry.Scheme.Hom.isRelativelyPerfect_derivedPullback_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectBaseChangeCartesian.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectBaseChangeCartesian.lean#L138).

> **Stacks 0DI5.** Let `f : X ⟶ S` be a morphism of schemes which is flat and locally of finite
> presentation, let `g : S' ⟶ S` be a morphism of schemes, and let `X'` with `g' : X' ⟶ X` and
> `f' : X' ⟶ S'` be a fibre product `S' ×_S X`. If `K` in `D(𝒪_X)` is `S`-perfect, then `L(g')^*K`
> is `S'`-perfect.
>
> Relative perfectness is `AlgebraicGeometry.Scheme.Hom.IsRelativelyPerfect`, Stacks 0DI0 at the
> derived tensor product of Stacks 06YU, on both sides. `Flat f'` and
> `LocallyOfFinitePresentation f'`, which the conclusion needs in order to be stated, are the base
> changes of the corresponding properties of `f` along `g`.

```lean
public theorem isRelativelyPerfect_derivedPullback_of_isPullback
    {X S S' X' : Scheme.{u}} {f : X ⟶ S} {g : S' ⟶ S} {g' : X' ⟶ X} {f' : X' ⟶ S'}
    (hpb : IsPullback g' f' f g) [Flat f] [LocallyOfFinitePresentation f]
    (K : DerivedCategory (OXMod.{u, u} X.toRingedSpace)) :
    haveI : Flat f' := MorphismProperty.of_isPullback (P := @Flat) hpb inferInstance
    haveI : LocallyOfFinitePresentation f' :=
      MorphismProperty.of_isPullback (P := @LocallyOfFinitePresentation) hpb inferInstance
    f.IsRelativelyPerfect K →
      f'.IsRelativelyPerfect
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          g'.toLRSHom.toShHom).obj K)
```

**`AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectBaseChangeFull.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectBaseChangeFull.lean#L81).

> **Stacks 0DI5.** Let `f : X ⟶ S` be flat and locally of finite presentation, `g : S' ⟶ S` a
> morphism of schemes, and `X'` with `g' : X' ⟶ X`, `f' : X' ⟶ S'` the base change of `f` along `g`.
> If `K` in `D(𝒪_X)` is `S`-perfect, then `L(g')^*K` is `S'`-perfect.
>
> Relative perfectness is read at the derived tensor product of Stacks 06YU on the open subspaces
> of the inverse-image ringed spaces.

```lean
theorem isPerfectRelativeTo_derivedPullback [Flat f] [LocallyOfFinitePresentation f]
    (hpb : IsPullback g' f' f g) (K : DerivedCategory X.Modules)
    (hK : f.IsPerfectRelativeTo
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base)) K) :
    haveI : Flat f' := MorphismProperty.of_isPullback (P := @Flat) hpb (inferInstance : Flat f)
    haveI : LocallyOfFinitePresentation f' :=
      MorphismProperty.of_isPullback (P := @LocallyOfFinitePresentation) hpb
        (inferInstance : LocallyOfFinitePresentation f)
    f'.IsPerfectRelativeTo
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S'.toRingedSpace f'.base))
      ((derivedPullback g'.toLRSHom.toShHom).obj K)
```

## Tag 0DI6, a situation

[Tag 0DI6](https://stacks.math.columbia.edu/tag/0DI6) in the Stacks Project.

**`AlgebraicGeometry.RelativeDescentSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfect.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfect.lean#L45).

> The relative descent situation: a directed inverse limit of
> quasi-compact, quasi-separated schemes with affine transition maps, together with a flat
> morphism of finite presentation over a fixed stage.

```lean
structure RelativeDescentSituation (I : Type v) [Preorder I] [IsDirected I (· ≤ ·)]
```

## Tag 0DI7, a lemma

[Tag 0DI7](https://stacks.math.columbia.edu/tag/0DI7) in the Stacks Project.

**`AlgebraicGeometry.RelativeDescentSituation.homDescent_of_isPseudoCoherent_of_locallyHasFiniteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeDescentCapstone.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativeDescentCapstone.lean#L105).

> **Stacks 0DI7.** In Situation 0DI6, let `K₀` and `L₀` be objects of `D(𝒪_{X₀})` with `K₀`
> pseudo-coherent and `L₀` in `D_QCoh(𝒪_{X₀})` of locally finite Tor dimension as an object of
> `D((X₀ ⟶ S₀)⁻¹𝒪_{S₀})`. Then
> `colim_i Hom_{D(𝒪_{Xᵢ})}(Lf_{i0}^*K₀, Lf_{i0}^*L₀) ⟶ Hom_{D(𝒪_X)}(Lf₀^*K₀, Lf₀^*L₀)`
> is bijective.

```lean
theorem homDescent_of_isPseudoCoherent_of_locallyHasFiniteTorDimension
    (hK₀ : RingedSpace.IsPseudoCoherent (X := D.X₀.left.toRingedSpace) K₀)
    (hL₀qc : ∀ n : ℤ,
      ((DerivedCategory.homologyFunctor D.X₀.left.Modules n).obj L₀).IsQuasicoherent)
    (hL₀tor : RingedSpace.LocallyHasFiniteTorDimension
      (RingedSpace.inverseImage (D.descent.system.obj (op D.descent.base)).toRingedSpace
        D.X₀.hom.base)
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily _)
      ((Scheme.Hom.derivedScalarRestriction D.X₀.hom).obj L₀)) :
    D.HomDescent K₀ L₀
```

## Tag 0DI8, a lemma

[Tag 0DI8](https://stacks.math.columbia.edu/tag/0DI8) in the Stacks Project.

**`AlgebraicGeometry.AffinePerfectDescent.exists_isPerfectRelativeTo_stage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeDescentAffineEssentialSurjectivity.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativeDescentAffineEssentialSurjectivity.lean#L342). The attribute's comment: “essential surjectivity only, and only in the affine case of the filtered system of rings of Stacks 0DHX. Full faithfulness (Stacks 0DI7) is not reproved, and nothing is proved for a general Situation 0DI6; see the implementation notes.”.

> **The affine case of the essential-surjectivity half of Stacks 0DI8.** Let `R₀` be a ring,
> let `i ↦ Rᵢ` be a filtered diagram of `R₀`-algebras with colimit `R`, and let `A₀` be a flat
> `R₀`-algebra of finite presentation. Put `A = R ⊗_{R₀} A₀` and `Aᵢ = Rᵢ ⊗_{R₀} A₀`. Then every
> object of `D(𝒪_{Spec A})` perfect relative to `Spec R` is, for some stage `i`, the derived
> pullback along `Spec(Aᵢ → A)` of an object of `D(𝒪_{Spec Aᵢ})` perfect relative to `Spec Rᵢ`.
>
> Relative perfectness is Stacks 0DI0 at the canonical certificate family on both sides. The
> object has quasi-coherent cohomology by Stacks 08E5, so Stacks 06Z0 presents it as the derived
> sheafification of a complex of `A`-modules; `isPerfectRelativeTo_tildeObj_iff` makes that complex
> perfect relative to `R`; Stacks 0DHX descends it to a stage; and `derivedPullbackTildeObjIso`,
> the affine comparison square of Stacks 08DW, identifies the derived pullback of the
> sheafification at that stage with the sheafification of the derived extension of scalars.
>
> Stacks 0DI8 itself is
> `AlgebraicGeometry.RelativeDescentSituation.isPerfectRelativeTo_colimit`.

```lean
theorem exists_isPerfectRelativeTo_stage
    (E : DerivedCategory (OXMod.{u, u}
      (Spec (CommRingCat.of (c.pt ⊗[R₀] A₀))).toRingedSpace))
    (hE : (specMap c.pt (c.pt ⊗[R₀] A₀)).IsPerfectRelativeTo
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily _) E) :
    ∃ (i : I) (Ei : DerivedCategory (OXMod.{u, u}
        (Spec (CommRingCat.of (PseudoCoherence.stageAlgebra F A₀ i))).toRingedSpace)),
      (specMap (F.obj i) (PseudoCoherence.stageAlgebra F A₀ i)).IsPerfectRelativeTo
          (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily _) Ei ∧
        Nonempty ((derivedPullback (Spec.map (CommRingCat.ofHom
          (PseudoCoherence.stageToLimitMap c A₀ i))).toLRSHom.toShHom).obj Ei ≅ E)
```

**`AlgebraicGeometry.RelativeDescentSituation.isPerfectRelativeTo_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeDescentPerfectColimit.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativeDescentPerfectColimit.lean#L219).

> **Stacks 0DI8.** In Situation 0DI6 the category of `S`-perfect objects of `D(𝒪_X)` is the
> colimit of the categories of `Sᵢ`-perfect objects of `D(𝒪_{Xᵢ})`: the transition functors
> `Lf_{ji}^*` and the comparison functors `Lfᵢ^*` carry relatively perfect objects to relatively
> perfect objects, the comparison out of the colimit is fully faithful, and it is essentially
> surjective.

```lean
theorem isPerfectRelativeTo_colimit :
    (∀ {i j : D.LaterIndex} (h : i.1 ≤ j.1)
        (E : DerivedCategory (OXMod.{u, u} (D.schemeAt i).toRingedSpace)),
        D.IsPerfectAt i E →
          D.IsPerfectAt j ((derivedPullback (D.transition h).toLRSHom.toShHom).obj E)) ∧
      (∀ (i : D.LaterIndex) (E : DerivedCategory (OXMod.{u, u} (D.schemeAt i).toRingedSpace)),
        D.IsPerfectAt i E →
          letI : Flat D.X₀.hom := D.flat
          letI : LocallyOfFinitePresentation D.X₀.hom :=
            D.finitePresentation.locallyOfFinitePresentation
          D.structureMapLimit.IsPerfectRelativeTo D.canonicalLimitCertificates
            ((derivedPullback (D.projection i).toLRSHom.toShHom).obj E)) ∧
      (∀ (i : D.LaterIndex) (K L : DerivedCategory (OXMod.{u, u} (D.schemeAt i).toRingedSpace)),
        D.IsPerfectAt i K → D.IsPerfectAt i L → D.HomDescentAt i K L) ∧
      D.PerfectEssentiallySurjectiveCanonical
```

## Tag 0DJT, a lemma

[Tag 0DJT](https://stacks.math.columbia.edu/tag/0DJT) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativelyPerfectProperPushforward.isPerfect_derivedPushforward_of_isPerfectRelativeTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectProperPushforward.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectProperPushforward.lean#L256). The attribute's comment: “the perfectness clause only, over a Noetherian base: Rf_*E is perfect for E S-perfect and f proper, flat, locally of finite presentation. Three inputs are granted: Tag 02O5 (haff), quasi-coherence of the H^i(E) (hqc), and the Tor-dimension half of Tag 08EV quantified over the source complex (htor). The base-change clause is not proved here”.

> **[Stacks, Tag 0DJT], the perfectness clause, over a Noetherian base.** Let `S` be a
> Noetherian scheme, let `f : X ⟶ S` be a proper, flat morphism of finite presentation and let `E`
> be an `S`-perfect object of `D(𝒪_X)` with quasi-coherent cohomology sheaves. Then `Rf_*E` is a
> perfect object of `D(𝒪_S)`.
>
> This is the converse implication of [Stacks, Tag 08CQ] applied to the pseudo-coherence proved
> above. The base-change clause of the tag — invertibility of the canonical derived base-change
> comparison — is a separate assertion and is not proved here.
>
> The hypothesis `htor` is `PushforwardTorDimensionResidue`, the Tor-dimension half of
> [Stacks, Tag 08EV] quantified over the source complex, which is the half of that proof this
> library cannot carry out; `haff` is its named form of [Stacks, Tag 02O5]; and `hqc` is
> quasi-coherence of the cohomology sheaves of `E`.

```lean
theorem isPerfect_derivedPushforward_of_isPerfectRelativeTo (D : TensorFamily f)
    (hD : IsGenuineTensorFamily f D) (E : DerivedCategory X.Modules)
    (hE : f.IsPerfectRelativeTo D E)
    (hqc : ∀ j : ℤ, ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsQuasicoherent)
    (haff : AlgebraicGeometry.ProperCoherentImage.HigherDirectImageIsCoherentOverAffineBase.{u})
    (htor : PushforwardTorDimensionResidue f D) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect (X := S.toRingedSpace)
      ((derivedPushforwardModules f).obj E)
```

**`Stacks.AlgebraicGeometry.RelativelyPerfectProperPushforward.isPerfect_derivedPushforward_and_isIso_derivedBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectProperPushforwardBaseChange.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectProperPushforwardBaseChange.lean#L238).

> **[Stacks, Tag 0DJT].** Let `f : X ⟶ S` be a morphism of schemes which is flat, proper and of
> finite presentation, and let `E ∈ D(𝒪_X)` be `S`-perfect. Then `Rf_*E` is a perfect object of
> `D(𝒪_S)` and its formation commutes with arbitrary base change: for every cartesian square
> `X' = X ×_S S'` the base change map `Lg^*Rf_*E ⟶ Rf'_*L(g')^*E` of [Stacks, Tag 08HY] is an
> isomorphism.

```lean
theorem isPerfect_derivedPushforward_and_isIso_derivedBaseChangeMap {X S : Scheme.{u}}
    (f : X ⟶ S) [Flat f] [IsProper f] [LocallyOfFinitePresentation f]
    (E : DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace))
    (hE : f.IsPerfectRelativeTo
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily.{u + 1, u} _) E) :
    IsPerfect (X := S.toRingedSpace) ((derivedPushforwardModules f).obj E) ∧
      ∀ {X' S' : Scheme.{u}} (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
        (sq : IsPullback g' f' f g),
        IsIso (Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap g'.toLRSHom.toShHom
          f'.toLRSHom.toShHom f.toLRSHom.toShHom g.toLRSHom.toShHom (comp_toShHom_of_comm sq.w)
          E)
```

## Tag 0DJU, a lemma

[Tag 0DJU](https://stacks.math.columbia.edu/tag/0DJU) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeDerivedHomDual.exists_isPseudoCoherent_pushforward_sheafHom_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeDerivedHomDual.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativeDerivedHomDual.lean#L333).

> **[Stacks, Tag 0DJU].** Let `f : X ⟶ S` be a morphism of schemes and `E, K ∈ D(𝒪_X)`. Assume
> `S` is quasi-compact and quasi-separated, `f` is proper, flat and of finite presentation, `E` is
> `S`-perfect and `K` is pseudo-coherent. Then there is a pseudo-coherent `L ∈ D(𝒪_S)` with
>
> `Rf_* R𝓗om(K, E) ≅ R𝓗om(L, 𝒪_S)`,
>
> and the same holds after arbitrary base change: for every cartesian square
> `g' ≫ f = f' ≫ g` with `g : S' ⟶ S`,
>
> `Rf'_* R𝓗om(L(g')^*K, L(g')^*E) ≅ R𝓗om(Lg^*L, 𝒪_{S'})`.
>
> The derived categories are read at the standard model `CategoryTheory.HasDerivedCategory.standard`
> (`DStd`), at which the derived direct image `pushStd`, the derived pullback `pullStd`, the derived
> internal Hom `Stacks.SheafOfModules.derivedSheafHom` and the structure sheaf in degree zero
> `unitObj` are taken; "of finite presentation" is `LocallyOfFinitePresentation` together with the
> quasi-compactness and quasi-separatedness that properness contains. `L = hocolim Lₙ` for the
> duals `Lₙ = (Rf_* R𝓗om(Kₙ, E))^∨` of an approximation `K = hocolim Kₙ` by perfect objects; see
> `exists_construction_isPseudoCoherent`.

```lean
theorem exists_isPseudoCoherent_pushforward_sheafHom_iso [CompactSpace S] [QuasiSeparatedSpace S]
    [IsProper f] [Flat f] [LocallyOfFinitePresentation f] (E K : DStd X) (hE : IsRelPerfect f E)
    (hK : IsPseudoCoherentStd K) :
    ∃ L : DStd S, IsPseudoCoherentStd L ∧
      Nonempty ((pushStd f).obj (((derivedSheafHom X.sheaf).obj (op K)).obj E) ≅
        ((derivedSheafHom S.sheaf).obj (op L)).obj (unitObj S)) ∧
      ∀ {X' S' : Scheme.{u}} (g' : X' ⟶ X) (f' : X' ⟶ S') (g : S' ⟶ S), IsPullback g' f' f g →
        Nonempty ((pushStd f').obj (((derivedSheafHom X'.sheaf).obj
            (op ((pullStd g').obj K))).obj ((pullStd g').obj E)) ≅
          ((derivedSheafHom S'.sheaf).obj (op ((pullStd g).obj L))).obj (unitObj S'))
```

## Tag 0DJV, a remark

[Tag 0DJV](https://stacks.math.columbia.edu/tag/0DJV) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeExtCharacterization.exists_unique_relativeExt_representative_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeExtCharacterization/AffineModuleLevel.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativeExtCharacterization/AffineModuleLevel.lean#L78). The attribute's comment: “module-level uniqueness, for S = Spec R affine: the complex L of Tag 0DJU is determined, up to an isomorphism inducing the identifications, among pseudo-coherent complexes L' by functorial isomorphisms Ext^i(L', F) = Ext^i(K, E (x)^L Lf^*F), F quasi-coherent, compatible with boundary maps. Proved for affine S only; the module-level form over a general quasi-compact quasi-separated S is open (see the module docstring)”.

> **[Stacks, Tag 0DJV], for `S = Spec R` affine, with the module-level uniqueness.** Let
> `f : X ⟶ Spec R` be proper, flat and of finite presentation, `E ∈ D(𝒪_X)` perfect relative to
> `Spec R` and `K ∈ D(𝒪_X)` pseudo-coherent. The pseudo-coherent complex `L` on `Spec R` of
> [Stacks, Tag 0DJU], with `Rf_*R𝓗om(K, E) ≅ R𝓗om(L, 𝒪)`, carries isomorphisms
> `Ext^i(L, ℱ) ≃ Ext^i(K, E ⊗^L Lf^*ℱ)` for quasi-coherent `ℱ`, functorial in `ℱ` and compatible
> with the boundary maps, induced by a natural identification `θ` on `D^+_{QCoh}` that
> characterizes `L` (all as in
> `Stacks.AlgebraicGeometry.RelativeExtCharacterization.exists_unique_relativeExt_representative`).
> Moreover `L` is characterized by the `Ext` isomorphisms alone, which is the module-level
> uniqueness of the remark: any pseudo-coherent `L'` with
> isomorphisms `ε'_{ℱ,i} : Ext^i(L', ℱ) ≃ Ext^i(K, E ⊗^L Lf^*ℱ)` for quasi-coherent `ℱ`,
> functorial in `ℱ` and compatible with the boundary maps, is isomorphic to `L` by an isomorphism
> `g : L' ≅ L` with `ε'(g ∘ x) = ε(x)`.

```lean
theorem exists_unique_relativeExt_representative_spec [IsProper f] [Flat f]
    [LocallyOfFinitePresentation f] (E K : DStd X) (hE : IsRelPerfect f E)
    (hK : IsPseudoCoherentStd K) :
    ∃ L : DStd (Spec R), IsPseudoCoherentStd L ∧
      Nonempty ((pushStd f).obj (rhom K E) ≅ rhom L (unitObj (Spec R))) ∧
      ∃ θ : ShiftedHom.NaturalHomIdentification (𝟭 (DStd (Spec R))) (tensorPull f E) L K
          (boundedBelowQCoh (Spec R)),
        (∀ {F F' : (Spec R).Modules} (hF : F.IsQuasicoherent) (hF' : F'.IsQuasicoherent)
            (g : F ⟶ F') (i : ℤ)
            (x : ShiftedHom L ((RelativeDerivedHomDual.singleStd (Spec R) 0).obj F) i),
          extEquiv θ F' hF' i (x ≫ ((RelativeDerivedHomDual.singleStd (Spec R) 0).map g)⟦i⟧') =
            extEquiv θ F hF i x ≫
              ((tensorPull f E).map ((RelativeDerivedHomDual.singleStd (Spec R) 0).map g))⟦i⟧') ∧
        (∀ {T : ShortComplex (Spec R).Modules} (hT : T.ShortExact) (h₁ : T.X₁.IsQuasicoherent)
            (h₃ : T.X₃.IsQuasicoherent) (i j : ℤ) (hij : 1 + i = j)
            (x : ShiftedHom L ((RelativeDerivedHomDual.singleStd (Spec R) 0).obj T.X₃) i),
          extEquiv θ T.X₁ h₁ j (ShiftedHom.comp x (singleδStd hT) hij) =
            (extEquiv θ T.X₃ h₃ i x).comp (ShiftedHom.map (singleδStd hT) (tensorPull f E))
              hij) ∧
        (∀ (L' : DStd (Spec R)), IsPseudoCoherentStd L' →
          ∀ θ' : ShiftedHom.NaturalHomIdentification (𝟭 (DStd (Spec R))) (tensorPull f E) L' K
            (boundedBelowQCoh (Spec R)),
          ∃ φ : L' ≅ L, ∀ (N : DStd (Spec R)) (hN : boundedBelowQCoh (Spec R) N) (x : L ⟶ N),
            θ'.equiv N hN (φ.hom ≫ x) = θ.equiv N hN x) ∧
        ∀ (L' : DStd (Spec R)), IsPseudoCoherentStd L' →
          ∀ ε' : ∀ (F : (Spec R).Modules), F.IsQuasicoherent → ∀ i : ℤ,
              ShiftedHom L' ((RelativeDerivedHomDual.singleStd (Spec R) 0).obj F) i ≃+
                ShiftedHom K
                  ((tensorPull f E).obj ((RelativeDerivedHomDual.singleStd (Spec R) 0).obj F)) i,
          (∀ {F F' : (Spec R).Modules} (hF : F.IsQuasicoherent) (hF' : F'.IsQuasicoherent)
              (g : F ⟶ F') (i : ℤ)
              (x : ShiftedHom L' ((RelativeDerivedHomDual.singleStd (Spec R) 0).obj F) i),
            ε' F' hF' i (x ≫ ((RelativeDerivedHomDual.singleStd (Spec R) 0).map g)⟦i⟧') =
              ε' F hF i x ≫
                ((tensorPull f E).map ((RelativeDerivedHomDual.singleStd (Spec R) 0).map g))⟦i⟧') →
          (∀ {T : ShortComplex (Spec R).Modules} (hT : T.ShortExact) (h₁ : T.X₁.IsQuasicoherent)
              (h₃ : T.X₃.IsQuasicoherent) (i j : ℤ) (hij : 1 + i = j)
              (x : ShiftedHom L' ((RelativeDerivedHomDual.singleStd (Spec R) 0).obj T.X₃) i),
            ε' T.X₁ h₁ j (ShiftedHom.comp x (singleδStd hT) hij) =
              (ε' T.X₃ h₃ i x).comp (ShiftedHom.map (singleδStd hT) (tensorPull f E)) hij) →
          ∃ g : L' ≅ L, ∀ (F : (Spec R).Modules) (hF : F.IsQuasicoherent) (i : ℤ)
            (x : ShiftedHom L ((RelativeDerivedHomDual.singleStd (Spec R) 0).obj F) i),
            ε' F hF i (g.hom ≫ x) = extEquiv θ F hF i x
```

**`Stacks.AlgebraicGeometry.RelativeExtCharacterization.exists_unique_relativeExt_representative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeExtCharacterization/Statement.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativeExtCharacterization/Statement.lean#L89). The attribute's comment: “the characterization of the complex L of Tag 0DJU by functorial isomorphisms Ext^i(L, F) = Ext^i(K, E (x)^L Lf^*F) for F quasi-coherent, compatible with boundary maps: their existence, induced by a natural identification Hom(L, N) = Hom(K, E (x)^L Lf^*N) on D^+_QCoh(O_S), and uniqueness of L among pseudo-coherent complexes carrying such an identification. Proved: existence in the source's shape, and uniqueness among L' carrying the D^+_QCoh identification. Open: the remark's module-level uniqueness (from the Ext delta-functor on QCoh alone), which is an Adams-type realizability question; see the module docstring”.

> **[Stacks, Tag 0DJV].** Let `S` be quasi-compact and quasi-separated, `f : X ⟶ S` proper,
> flat and of finite presentation, `E ∈ D(𝒪_X)` perfect relative to `S` and `K ∈ D(𝒪_X)`
> pseudo-coherent. The pseudo-coherent complex `L` on `S` of [Stacks, Tag 0DJU], with
> `Rf_*R𝓗om(K, E) ≅ R𝓗om(L, 𝒪_S)`, carries isomorphisms
>
> `Ext^i_{𝒪_S}(L, ℱ) ≃ Ext^i_{𝒪_X}(K, E ⊗^L_{𝒪_X} Lf^*ℱ)`
>
> for all `i` and all quasi-coherent `ℱ`, functorial in `ℱ` and compatible with the boundary maps
> of short exact sequences of quasi-coherent modules (on the left, composition with the
> connecting morphism `ℱ₃ ⟶ ℱ₁[1]`; on the right, composition with its image under
> `E ⊗^L Lf^*(-)`, the third morphism of a distinguished triangle by
> `tensorPull_mapTriangle_singleTriangle`). These isomorphisms are induced by a natural
> identification `θ_N : Hom(L, N) ≃ Hom(K, E ⊗^L Lf^*N)` for `N` in `D^+_{QCoh}(𝒪_S)` (the `ℱ[i]`
> being such `N`), and `L` is characterized by it: any pseudo-coherent `L'` carrying a natural
> identification `θ'` of the same kind is isomorphic to `L`, by an isomorphism `φ` with
> `θ'(φ ∘ x) = θ(x)`.
>
> The source leaves the statement imprecise ("If we ever need this we will formulate a precise
> result here"); the above is the precise form proved. Uniqueness from the module-level
> `δ`-functor alone, i.e. from natural isomorphisms of the `Ext^i(-, ℱ)` on quasi-coherent `ℱ`
> compatible with boundary maps but not coming from an identification on `D^+_{QCoh}(𝒪_S)`, is
> **not** asserted: at `f = 𝟙` and `E = 𝒪` it is the statement that a pseudo-coherent complex on
> a quasi-compact quasi-separated scheme is determined by its `δ`-functor `ℱ ↦ Ext^*(L, ℱ)` on
> quasi-coherent modules, which is neither proved nor refuted here.

```lean
theorem exists_unique_relativeExt_representative [CompactSpace S] [QuasiSeparatedSpace S]
    [IsProper f] [Flat f] [LocallyOfFinitePresentation f] (E K : DStd X)
    (hE : IsRelPerfect f E) (hK : IsPseudoCoherentStd K) :
    ∃ L : DStd S, IsPseudoCoherentStd L ∧
      Nonempty ((pushStd f).obj (rhom K E) ≅ rhom L (unitObj S)) ∧
      ∃ θ : ShiftedHom.NaturalHomIdentification (𝟭 (DStd S)) (tensorPull f E) L K
          (boundedBelowQCoh S),
        (∀ {F F' : S.Modules} (hF : F.IsQuasicoherent) (hF' : F'.IsQuasicoherent)
            (g : F ⟶ F') (i : ℤ)
            (x : ShiftedHom L ((RelativeDerivedHomDual.singleStd S 0).obj F) i),
          extEquiv θ F' hF' i (x ≫ ((RelativeDerivedHomDual.singleStd S 0).map g)⟦i⟧') =
            extEquiv θ F hF i x ≫
              ((tensorPull f E).map ((RelativeDerivedHomDual.singleStd S 0).map g))⟦i⟧') ∧
        (∀ {T : ShortComplex S.Modules} (hT : T.ShortExact) (h₁ : T.X₁.IsQuasicoherent)
            (h₃ : T.X₃.IsQuasicoherent) (i j : ℤ) (hij : 1 + i = j)
            (x : ShiftedHom L ((RelativeDerivedHomDual.singleStd S 0).obj T.X₃) i),
          extEquiv θ T.X₁ h₁ j (ShiftedHom.comp x (singleδStd hT) hij) =
            (extEquiv θ T.X₃ h₃ i x).comp (ShiftedHom.map (singleδStd hT) (tensorPull f E))
              hij) ∧
        ∀ (L' : DStd S), IsPseudoCoherentStd L' →
          ∀ θ' : ShiftedHom.NaturalHomIdentification (𝟭 (DStd S)) (tensorPull f E) L' K
            (boundedBelowQCoh S),
          ∃ φ : L' ≅ L, ∀ (N : DStd S) (hN : boundedBelowQCoh S N) (x : L ⟶ N),
            θ'.equiv N hN (φ.hom ≫ x) = θ.equiv N hN x
```

## Tag 0GEH, a lemma

[Tag 0GEH](https://stacks.math.columbia.edu/tag/0GEH) in the Stacks Project.

**`AlgebraicGeometry.isLocallyBoundedBelow_of_isPerfectRelativeTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectBoundedBelow.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectBoundedBelow.lean#L186). The attribute's comment: “condition (1) implies the first clause of condition (2): an `S`-perfect object is locally bounded below”.

> **Stacks 0GEH, condition (1) implies the first clause of condition (2).** Let `f : X ⟶ S` be
> flat and locally of finite presentation. An object of `D(𝒪_X)` perfect relative to `S` is locally
> bounded below.
>
> Relative perfectness gives an open covering of `X` on each member of which `E`, read over
> `f⁻¹𝒪_S`, has Tor amplitude in some interval `[a, b]`. The structure sheaf of the inverse-image
> ringed space is the unit of its tensor product, so that interval already bounds the cohomology
> of `E|_U` read over `f⁻¹𝒪_S`, and restriction of scalars along `f⁻¹𝒪_S ⟶ 𝒪_X` leaves the
> underlying sheaves unchanged.
>
> The derived tensor product is a family of certificates, one on each open subspace of the
> inverse-image ringed space, pinned by the hypothesis that its underived tensor product is the
> genuine `- ⊗_{f⁻¹𝒪_S} -`.

```lean
public theorem isLocallyBoundedBelow_of_isPerfectRelativeTo {X S : Scheme.{u}} (f : X ⟶ S)
    [Flat f] [LocallyOfFinitePresentation f]
    [HasDerivedCategory.{d} (OXMod.{u, u} X.toRingedSpace)]
    [HasDerivedCategory.{d'} (OXMod.{u, u} (RingedSpace.inverseImage S.toRingedSpace f.base))]
    [∀ U : Opens (RingedSpace.inverseImage S.toRingedSpace f.base).carrier,
      HasDerivedCategory.{d'}
        (OXMod.{u, u} ((RingedSpace.inverseImage S.toRingedSpace f.base).restrict
          U.isOpenEmbedding))]
    (D : ∀ U : Opens (RingedSpace.inverseImage S.toRingedSpace f.base).carrier,
      RingedSpace.CertifiedDerivedSheafTensoring.{d', u}
        ((RingedSpace.inverseImage S.toRingedSpace f.base).restrict U.isOpenEmbedding))
    (hD : ∀ U : Opens (RingedSpace.inverseImage S.toRingedSpace f.base).carrier,
      (D U).tensor = Stacks.SheafOfModules.Tensor.sheafTensor
        ((RingedSpace.inverseImage S.toRingedSpace f.base).restrict U.isOpenEmbedding).sheaf)
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
    (hE : f.IsPerfectRelativeTo D E) :
    RingedSpace.IsLocallyBoundedBelow X.toRingedSpace E
```

**`AlgebraicGeometry.isPerfectRelativeTo_iff_isLocallyBoundedBelow_and_fibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectFibres.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectFibres.lean#L521).

> **Stacks 0GEH.** Let `f : X ⟶ S` be a morphism of schemes which is flat and locally of finite
> presentation, and let `E` be a pseudo-coherent object of `D(𝒪_X)`. The following are equivalent:
>
> 1. `E` is `S`-perfect (Stacks 0DI0);
> 2. `E` is locally bounded below and for every point `s ∈ S` the derived fibre `L(X_s ⟶ X)^*E` of
>    `D(𝒪_{X_s})` is locally bounded below, where `X_s = X ×_S Spec κ(s)`.
>
> Relative perfectness is read at the canonical certificate family
> `AlgebraicGeometry.RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily`, the genuine
> derived tensor product over `f⁻¹𝒪_S`.

```lean
theorem isPerfectRelativeTo_iff_isLocallyBoundedBelow_and_fibres
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
    (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E) :
    f.IsPerfectRelativeTo (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily _) E ↔
      RingedSpace.IsLocallyBoundedBelow X.toRingedSpace E ∧
        ∀ s : S, RingedSpace.IsLocallyBoundedBelow
          (pullback f (S.fromSpecResidueField s)).toRingedSpace
          ((derivedPullback (pullback.fst f (S.fromSpecResidueField s)).toLRSHom.toShHom).obj
            E)
```

**`AlgebraicGeometry.Scheme.Hom.isRelativelyPerfect_of_isLocallyBoundedBelow_of_fibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectFromFibres.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectFromFibres.lean#L58). The attribute's comment: “condition (2) implies condition (1): for f flat and locally of finite presentation and E pseudo-coherent, if E is locally bounded below and every derived fibre L(X_s ⟶ X)^*E is locally bounded below, then E is S-perfect”.

> **Stacks 0GEH, condition (2) implies condition (1).** Let `f : X ⟶ S` be flat and locally of
> finite presentation and let `E` be a pseudo-coherent object of `D(𝒪_X)`. If `E` is locally
> bounded below and for every point `s` of `S` the derived pullback `L(X_s ⟶ X)^*E` of `E` to the
> fibre `X_s = X ×_S Spec κ(s)` is locally bounded below, then `E` is `S`-perfect.

```lean
public theorem isRelativelyPerfect_of_isLocallyBoundedBelow_of_fibres
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    (E : DerivedCategory X.Modules)
    (hpc : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E)
    (hE : RingedSpace.IsLocallyBoundedBelow X.toRingedSpace E)
    (hfib : ∀ s : S, RingedSpace.IsLocallyBoundedBelow
      (Limits.pullback f (S.fromSpecResidueField s)).toRingedSpace
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (Limits.pullback.fst f (S.fromSpecResidueField s)).toLRSHom.toShHom).obj E)) :
    f.IsRelativelyPerfect E
```

## Tag 0DI9, a remark

[Tag 0DI9](https://stacks.math.columbia.edu/tag/0DI9) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isRelativelyPerfect_iff_isLocallyBoundedFlatFinitePresentation_and_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectLieblich.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectLieblich.lean#L572). References: SGA 6 III (4.2), “(B)”.

> **Stacks 0DI9.** Let `f : X ⟶ S` be a morphism of schemes.
>
> 1. If `f` is flat and locally of finite presentation (so that Definition 0DI0 applies), an object
>    `E` of `D(𝒪_X)` is `S`-perfect exactly when it satisfies Lieblich's condition (A): locally on
>    `X`, `E` is quasi-isomorphic to a finite complex of `S`-flat, finitely presented
>    `𝒪_X`-modules.
> 2. If `f` is locally of finite type, condition (B) — `E` is pseudo-coherent relative to `S` and
>    locally has finite Tor dimension as an object of `D(f⁻¹𝒪_S)` — defines a strictly full
>    triangulated subcategory of `D(𝒪_X)`.
> 3. Condition (B) is the natural generalisation of Definition 0DI0: when `f` is flat and locally of
>    finite presentation, (B) holds exactly for the `S`-perfect objects.

```lean
theorem isRelativelyPerfect_iff_isLocallyBoundedFlatFinitePresentation_and_isTriangulated :
    (∀ [Flat f] [LocallyOfFinitePresentation f]
        (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace)),
      f.IsRelativelyPerfect E ↔ f.IsLocallyBoundedFlatFinitePresentation E) ∧
    (∀ [LocallyOfFiniteType f],
      f.isPseudoCoherentOfLocallyFiniteTorDimensionOver.IsClosedUnderIsomorphisms ∧
        f.isPseudoCoherentOfLocallyFiniteTorDimensionOver.IsTriangulated) ∧
    (∀ [Flat f] [LocallyOfFinitePresentation f]
        (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace)),
      f.isPseudoCoherentOfLocallyFiniteTorDimensionOver E ↔ f.IsRelativelyPerfect E)
```

**`AlgebraicGeometry.Scheme.Hom.isClosedUnderIsomorphisms_isPseudoCoherentOfFiniteTorDimensionRelativeTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectTriangulated.lean, line 647](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectTriangulated.lean#L647). The attribute's comment: “condition (B) defines a triangulated subcategory”.

> **Stacks 0DI9, condition (B).** For a morphism of schemes `f : X ⟶ S` which is only assumed
> locally of finite type, the objects of `D(𝒪_X)` satisfying condition (B) form a *strictly full*
> subcategory: both clauses are invariant under isomorphism in `D(𝒪_X)`.

```lean
public theorem isClosedUnderIsomorphisms_isPseudoCoherentOfFiniteTorDimensionRelativeTo :
    (isPseudoCoherentOfFiniteTorDimensionRelativeTo f D).IsClosedUnderIsomorphisms
```

**`AlgebraicGeometry.Scheme.Hom.isTriangulated_isPseudoCoherentOfFiniteTorDimensionRelativeTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectTriangulated.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectTriangulated.lean#L719). The attribute's comment: “condition (B) defines a triangulated subcategory”.

> **Stacks 0DI9, condition (B).** For a morphism of schemes `f : X ⟶ S` which is only assumed
> locally of finite type — neither flat nor locally of finite presentation — the objects of
> `D(𝒪_X)` that are pseudo-coherent relative to `S` and of locally finite Tor dimension in
> `D(f⁻¹𝒪_S)` form a *triangulated* subcategory: the property contains the zero object, is stable
> under all shifts, and is closed under extensions.
>
> Both clauses are triangulated subcategories separately — relative pseudo-coherence by Stacks
> 09UL, finite Tor dimension by Stacks 08CJ — and their intersection is one again. Exactness of
> each `- ⊗^{L} ℱ[0]` and locality of finite Tor dimension are hypotheses, both of them properties
> of the genuine derived tensor product that an arbitrary certificate need not have.

```lean
public theorem isTriangulated_isPseudoCoherentOfFiniteTorDimensionRelativeTo :
    (isPseudoCoherentOfFiniteTorDimensionRelativeTo f D).IsTriangulated
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.35, Tag 0DHZ](https://stacks.math.columbia.edu/tag/0DHZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
