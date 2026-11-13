---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSpace.CertifiedDerivedSheafTensoring.HasTorAmplitudeIn, AlgebraicGeometry.RingedSpace.CertifiedDerivedSheafTensoring.HasFiniteTorDimension, AlgebraicGeometry.RingedSpace.CertifiedDerivedSheafTensoring.HasTorDimensionLE, AlgebraicGeometry.RingedSpace.LocallyHasFiniteTorDimension, CategoryTheory.DerivedCategory.HasTorAmplitudeIn, Stacks.Cohomology.TorAmplitude.HasTorAmplitude, Stacks.Cohomology.TorAmplitude.HasFiniteTorDimension, Stacks.Cohomology.TorAmplitude.HasTorDimensionLE
statement: formalized
proof: formalized
---

# 20.48 Tor dimension

Section 20.48 of the Stacks Project, [Tag 08CF](https://stacks.math.columbia.edu/tag/08CF). 8 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08CG, a definition

[Tag 08CG](https://stacks.math.columbia.edu/tag/08CG) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.CertifiedDerivedSheafTensoring.HasTorAmplitudeIn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/TorDimension.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/TorDimension.lean#L174). The attribute's comment: “tor amplitude in an interval”. References: SGA 6 I (5.2), “Tor-amp(F) ⊂ [m,n]”; SGA 4½ Rapport (4.5), “sheaf tor-dimension ≤ r”; SGA 4 XVII (4.1.9), “ringed space, (i)”.

> **Stacks 08CG (1).** An object `E` of `D(𝒪_X)` *has Tor amplitude in `[a, b]`* if, for every
> `𝒪_X`-module `ℱ` and every integer `i` outside `[a, b]`, the cohomology sheaf
> `H^i(E ⊗^{L}_{𝒪_X} ℱ)` vanishes.
>
> The derived tensor product is the one carried by `D`; see the implementation notes of this file
> for what the certificate buys and for why the interval is not assumed nonempty.

```lean
public def HasTorAmplitudeIn (D : CertifiedDerivedSheafTensoring.{d, u} X)
    (E : DerivedCategory (OXMod.{u, u} X)) (a b : ℤ) : Prop
```

**`AlgebraicGeometry.RingedSpace.CertifiedDerivedSheafTensoring.HasFiniteTorDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/TorDimension.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/TorDimension.lean#L196). The attribute's comment: “finite tor dimension”. References: SGA 6 I (5.2), “finite flat amplitude”; SGA 4½ Rapport (4.5), “sheaf case, finite”.

> **Stacks 08CG (2).** An object `E` of `D(𝒪_X)` *has finite Tor dimension* if it has Tor
> amplitude in some interval `[a, b]`.

```lean
public def HasFiniteTorDimension (D : CertifiedDerivedSheafTensoring.{d, u} X)
    (E : DerivedCategory (OXMod.{u, u} X)) : Prop
```

**`AlgebraicGeometry.RingedSpace.CertifiedDerivedSheafTensoring.HasTorDimensionLE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/TorDimension.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/TorDimension.lean#L205). The attribute's comment: “tor dimension of a module”. References: SGA 4½ Rapport (4.5), “sheaf module case”; SGA 4 XVII (4.1.9), “ringed space, module”.

> **The last sentence of Stacks 08CG.** An `𝒪_X`-module `ℱ` *has Tor dimension at most `n`* if
> `ℱ[0]`, viewed in `D(𝒪_X)`, has Tor amplitude in `[-n, 0]`.

```lean
public def HasTorDimensionLE (D : CertifiedDerivedSheafTensoring.{d, u} X)
    (F : OXMod.{u, u} X) (n : ℤ) : Prop
```

**`AlgebraicGeometry.RingedSpace.LocallyHasFiniteTorDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/TorDimension.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/TorDimension.lean#L233). The attribute's comment: “locally finite tor dimension”.

> **Stacks 08CG (3).** An object `E` of `D(𝒪_X)` *locally has finite Tor dimension* if there is
> an open covering `X = ⋃ U i` such that `E|_{U i}` has finite Tor dimension for every `i`.
>
> A derived tensor product is needed on each open subspace, so the certificate is a family `D`
> indexed by the opens of `X`; `E|_{U i}` is
> `AlgebraicGeometry.RingedSpace.derivedRestrictModules`.

```lean
public def LocallyHasFiniteTorDimension
    (D : ∀ U : Opens X.carrier,
      CertifiedDerivedSheafTensoring.{d', u} (X.restrict U.isOpenEmbedding))
    (E : DerivedCategory (OXMod.{u, u} X)) : Prop
```

**`CategoryTheory.DerivedCategory.HasTorAmplitudeIn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/TorAmplitudeStalkwise.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/TorAmplitudeStalkwise.lean#L143). The attribute's comment: “tor amplitude in an interval, for a derived tensor bifunctor T over an arbitrary abelian category: H^i(E ⊗^L F) = 0 for every object F in degree 0 and every i outside [a, b]; at the derivedTensor of AlgebraicGeometry.RingedSpace.CertifiedDerivedSheafTensoring it is CertifiedDerivedSheafTensoring.HasTorAmplitudeIn by Iff.rfl”.

> **Stacks 08CG (1)**, for a derived tensor product given as a bifunctor on `D(A)`. An object
> `E` of `D(A)` *has Tor amplitude in `[a, b]`* when `H^i(E ⊗^{L} F) = 0` for every object `F` of
> `A` and every `i` outside `[a, b]`, the object `F` being read in degree `0`.
>
> On `A = OXMod X` this is
> `AlgebraicGeometry.RingedSpace.CertifiedDerivedSheafTensoring.HasTorAmplitudeIn` with `T` the
> certificate's `derivedTensor`, and the identification is `Iff.rfl`;
> `hasTorAmplitudeIn_iff_hasTorAmplitude` identifies it with the `TorAmplitude.HasTorAmplitude` of
> Stacks 08CJ.
>
> This form is stated for a bifunctor `T` on the derived category of an arbitrary abelian
> category. `AlgebraicGeometry.RingedSpace.CertifiedDerivedSheafTensoring.HasTorAmplitudeIn`
> (`StacksFrontier/AlgebraicGeometry/Perfect/TorDimension.lean`) is the same clause for a bundle that
> also records an underived tensor product, a comparison and an `IsLeftDerivedFunctor` field, and
> `Stacks.Cohomology.TorAmplitude.HasTorAmplitude`
> (`StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/OnARingedSpace.lean`) is the clause for
> the derived tensor product of Stacks 06YU.

```lean
public def HasTorAmplitudeIn
    (T : DerivedCategory A ⥤ DerivedCategory A ⥤ DerivedCategory A)
    (E : DerivedCategory A) (a b : ℤ) : Prop
```

**`Stacks.Cohomology.TorAmplitude.HasTorAmplitude`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/OnARingedSpace.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/OnARingedSpace.lean#L113). The attribute's comment: “tor amplitude in an interval, at the derived tensor product of Tag 06YU”. References: SGA 6 I (5.2), “Tor-amp(F) ⊂ [m,n]”; SGA 4½ Rapport (4.5), “sheaf tor-dimension ≤ r”; SGA 4 XVII (4.1.9), “ringed space, (i)”.

> An object of `D(O_X)` has Tor amplitude in `[a, b]` when its derived tensor product with
> every `O_X`-module, placed in degree `0`, has vanishing cohomology in every degree outside
> `[a, b]`.

```lean
def HasTorAmplitude (X : RingedSpace.{u, u}) [HasDerivedCategory.{d} (OXMod.{u} X)]
    (E : DerivedCategory (OXMod.{u} X)) (a b : ℤ) : Prop
```

**`Stacks.Cohomology.TorAmplitude.HasFiniteTorDimension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/OnARingedSpace.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/OnARingedSpace.lean#L125). The attribute's comment: “finite tor dimension, at the derived tensor product of Tag 06YU”. References: SGA 6 I (5.2), “finite flat amplitude”; SGA 4½ Rapport (4.5), “sheaf case, finite”.

> An object of `D(O_X)` has finite Tor dimension when it has Tor amplitude in some interval
> `[a, b]`.

```lean
abbrev HasFiniteTorDimension (X : RingedSpace.{u, u}) [HasDerivedCategory.{d} (OXMod.{u} X)]
    (E : DerivedCategory (OXMod.{u} X)) : Prop
```

**`Stacks.Cohomology.TorAmplitude.HasTorDimensionLE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/OnARingedSpace.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/OnARingedSpace.lean#L134). The attribute's comment: “tor dimension of a module, at the derived tensor product of Tag 06YU”. References: SGA 4½ Rapport (4.5), “sheaf module case”; SGA 4 XVII (4.1.9), “ringed space, module”.

> An `O_X`-module `F` has Tor dimension at most `n` when `F[0]`, viewed in `D(O_X)`, has Tor
> amplitude in `[-n, 0]`.

```lean
def HasTorDimensionLE (X : RingedSpace.{u, u}) [HasDerivedCategory.{d} (OXMod.{u} X)]
    (F : OXMod.{u} X) (n : ℤ) : Prop
```

**`Stacks.Cohomology.TorAmplitude.LocallyHasFiniteTorDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/OnARingedSpace.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/OnARingedSpace.lean#L165). The attribute's comment: “locally finite tor dimension, at the Tag 06YU tensor on each open subspace”.

> An object of `D(O_X)` locally has finite Tor dimension when its restriction to each member of
> some open cover has finite Tor dimension.

```lean
def LocallyHasFiniteTorDimension (X : RingedSpace.{u, u})
    [HasDerivedCategory.{d} (OXMod.{u} X)]
    [∀ U : Opens X.carrier,
      HasDerivedCategory.{d'} (OXMod.{u} (X.restrict U.isOpenEmbedding))]
    (E : DerivedCategory (OXMod.{u} X)) : Prop
```

## Tag 08CH, a lemma

[Tag 08CH](https://stacks.math.columbia.edu/tag/08CH) in the Stacks Project.

**`Stacks.Cohomology.TorAmplitude.FlatCokernel.isFlat_cokernel_of_hasTorAmplitude`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/FlatCokernel.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/FlatCokernel.lean#L203).

> **Tag 08CH.** The cokernel of the differential into the lowest degree of the Tor-amplitude
> interval of a bounded above complex of flat `O_X`-modules is a flat `O_X`-module.
>
> The complex is K-flat by Tag 06YQ, so the Tor-amplitude hypothesis makes the three-term
> complex `K^{a-2} ⊗ F ⟶ K^{a-1} ⊗ F ⟶ K^a ⊗ F` exact for every `O_X`-module `F`. Hence
> `Coker(d^{a-1}) ⊗ -` preserves monomorphisms, and being right exact as well it is exact.

```lean
theorem isFlat_cokernel_of_hasTorAmplitude
    (K : CochainComplex (Modules X) ℤ) (a b : ℤ)
    (hbound : ∃ n : ℤ, K.IsStrictlyLE n)
    (hflat : ∀ i : ℤ,
      AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.sheaf) (K.X i))
    (hamp : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X (DerivedCategory.Q.obj K) a b) :
    AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.sheaf)
      (cokernel (K.d (a - 1) a))
```

## Tag 08CI, a lemma

[Tag 08CI](https://stacks.math.columbia.edu/tag/08CI) in the Stacks Project.

**`Stacks.Cohomology.TorAmplitude.BoundedFlatRepresentative.hasTorAmplitude_iff_exists_flat_representative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/BoundedFlatRepresentative.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/BoundedFlatRepresentative.lean#L280). References: SGA 4 XVII (4.1.9), “(i), (iii)”; SGA 6 I (5.1), “ringed space case”.

> An object of `D(O_X)` has Tor amplitude in `[a, b]` exactly when some complex
> of flat `O_X`-modules vanishing in every degree outside `[a, b]` represents it.

```lean
theorem hasTorAmplitude_iff_exists_flat_representative (E : DerivedCategory (Modules X))
    (a b : ℤ) (hab : a ≤ b) :
    Stacks.Cohomology.TorAmplitude.HasTorAmplitude X E a b ↔
      ∃ K : CochainComplex (Modules X) ℤ,
        (∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u}
          (O := X.sheaf) (K.X i)) ∧
        (∀ i : ℤ, i ∉ Set.Icc a b → IsZero (K.X i)) ∧
        Nonempty (DerivedCategory.Q.obj K ≅ E)
```

## Tag 09U8, a lemma

[Tag 09U8](https://stacks.math.columbia.edu/tag/09U8) in the Stacks Project.

**`Stacks.Cohomology.TorAmplitude.Pullback.hasTorAmplitude_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/DerivedPullback.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/DerivedPullback.lean#L96).

> **Tag 09U8.** Derived pullback along a morphism of ringed spaces preserves Tor amplitude in
> a fixed interval.
>
> A degenerate interval is replaced by a one-point interval above the degree under
> consideration, which is weaker, and `hasTorAmplitude_derivedPullback_of_le` applies.

```lean
theorem hasTorAmplitude_derivedPullback (E : DerivedCategory (OXMod.{u} Y)) (a b : ℤ)
    (hE : HasTorAmplitude Y E a b) :
    HasTorAmplitude X
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f).obj E) a b
```

## Tag 09U9, a lemma

[Tag 09U9](https://stacks.math.columbia.edu/tag/09U9) in the Stacks Project.

**`Stacks.Cohomology.TorAmplitude.hasTorAmplitude_iff_forall_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/DerivedTensorStalk.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/DerivedTensorStalk.lean#L465). The attribute's comment: “Tor amplitude in [a, b] on a ringed space holds exactly when it holds at every stalk, for the derived tensor product of Stacks 06YU on D(O\_X) and the canonical derived tensor product of Stacks 0BYI over each stalk ring; the derived form of Stacks 01CB that the source proof cites is derivedTensorStalkIso in this file.”. References: SGA 6 I (5.6.2), “ringed space case”; SGA 4 XVII (4.2.8), “clause (iii)”.

> **Stacks 09U9.** Let `(X, 𝒪_X)` be a ringed space and `E` an object of `D(𝒪_X)`. Then `E`
> has Tor amplitude in `[a, b]` if and only if, for every point `x` of `X`, the stalk `E_x` has
> Tor amplitude in `[a, b]` as an object of `D(𝒪_{X, x})`.
>
> Both sides are read against *the* derived tensor product and against nothing else:
> `Stacks.Cohomology.TorAmplitude.HasTorAmplitude` is the Stacks 08CG predicate at
> `Stacks.Cohomology.TorAmplitude.derTensor`, the derived tensor product of Stacks 06YU on
> `D(𝒪_X)`, and the stalk side is the Stacks 08CG predicate at
> `Stacks.SheafOfModules.DerivedTensorStalk.stalkDerivedTensor`, the canonical derived tensor
> product of Stacks 0BYI over the stalk ring. What the Stacks proof cites — Stacks 01CB and
> exactness of stalks — is `Stacks.SheafOfModules.DerivedTensorStalk.derivedTensorStalkIso`.
>
> The two steps are both `Iff`s of the same proposition read in two vocabularies:
> `AlgebraicGeometry.RingedSpace.hasTorAmplitudeIn_canonicalCertified_iff` says the Stacks 08CG
> predicate at the canonical derived tensor product is this one, and
> `AlgebraicGeometry.RingedSpace.hasTorAmplitudeIn_canonicalCertified_iff_forall_stalk` is
> `Stacks.SheafOfModules.DerivedTensorStalk.hasTorAmplitudeIn_canonical_iff_forall_stalk`, the
> stalkwise criterion, at that derived tensor product.
>
> `AlgebraicGeometry.SheafOfModules.hasTorAmplitudeIn_iff_forall_stalk` is the engine: the same
> equivalence for derived tensor products supplied as bare bifunctors on `D(𝒪_X)` and on each
> `D(𝒪_{X, x})`, together with the isomorphism identifying them on stalks.

```lean
theorem hasTorAmplitude_iff_forall_stalk
    (E : DerivedCategory (OXMod.{u, u} X)) (a b : ℤ) :
    HasTorAmplitude X E a b ↔
      ∀ x : X.carrier, CategoryTheory.DerivedCategory.HasTorAmplitudeIn
        (Stacks.SheafOfModules.DerivedTensorStalk.stalkDerivedTensor X.sheaf x)
        ((AlgebraicGeometry.SheafOfModules.stalkFunctor (structureSheafOfRings X) x
          ).mapDerivedCategory.obj E) a b
```

**`Stacks.Cohomology.TorAmplitude.hasTorAmplitude_iff_forall_hasTorAmplitudeCanonical_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/StalkwiseCriterion.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/StalkwiseCriterion.lean#L87). References: SGA 4 XVII (4.2.8), “(iii), special case”.

> **Stacks 09U9.** Let `(X, 𝒪_X)` be a ringed space and `E` an object of `D(𝒪_X)`. Then `E`
> has Tor amplitude in `[a, b]` if and only if, for every point `x` of `X`, the stalk `E_x` has
> Tor amplitude in `[a, b]` as an object of `D(𝒪_{X, x})`.
>
> The left side is the Tor amplitude of Stacks 08CG for the derived tensor product of Stacks 06YU,
> `Stacks.Cohomology.TorAmplitude.HasTorAmplitude`; the right side is the Tor amplitude of
> Stacks 0652 over the ring `𝒪_{X, x}` for its derived tensor product of Stacks 0BYI,
> `StacksDraft.TorAmplitude.HasTorAmplitudeCanonical`. The stalk `E_x` is the image of `E` under
> the exact stalk functor `Mod(𝒪_X) ⥤ Mod(𝒪_{X, x})`.

```lean
theorem hasTorAmplitude_iff_forall_hasTorAmplitudeCanonical_stalk
    (E : DerivedCategory (OXMod.{u, u} X)) (a b : ℤ) :
    HasTorAmplitude X E a b ↔
      ∀ x : X.carrier, StacksDraft.TorAmplitude.HasTorAmplitudeCanonical
        (TopCat.Presheaf.stalk (C := RingCat.{u}) (X.presheaf ⋙ forget₂ CommRingCat RingCat) x)
        ((SheafOfModules.stalkFunctor (structureSheafOfRings X) x).mapDerivedCategory.obj E)
        a b
```

## Tag 08CJ, a lemma

[Tag 08CJ](https://stacks.math.columbia.edu/tag/08CJ) in the Stacks Project.

**`Stacks.Cohomology.TorAmplitude.FlatOpcycles.hasTorAmplitude_obj₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/TwoTermResolution.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/Transform/TwoTermResolution.lean#L143). The attribute's comment: “(1), at the ringed-space Tor-amplitude predicate”.

> **Tag 08CJ (1) at the ringed-space Tor-amplitude predicate.** In a distinguished triangle
> `K ⟶ L ⟶ M ⟶ K[1]` of `D(O_X)`, if `K` has Tor amplitude in `[a + 1, b + 1]` and `L` has Tor
> amplitude in `[a, b]`, then `M` has Tor amplitude in `[a, b]`.
>
> This is `TorAmplitude.hasTorAmplitude_obj₃` read through
> `Stacks.Cohomology.TorAmplitude.FlatOpcycles.tensorSingleFunctor`, exactly as
> `Stacks.Cohomology.TorAmplitude.FlatOpcycles.hasTorAmplitude_obj₁` reads part (3) through it; the
> only content is the translation between the two encodings of "outside `[a, b]`".

```lean
theorem hasTorAmplitude_obj₃
    (T : Triangle (DerivedCategory (RingedSpace.KFlatDerivedPullback.Modules X)))
    (hT : T ∈ distinguishedTriangles) (a b : ℤ)
    (hK : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X T.obj₁ (a + 1) (b + 1))
    (hL : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X T.obj₂ a b) :
    Stacks.Cohomology.TorAmplitude.HasTorAmplitude X T.obj₃ a b
```

**`Stacks.Cohomology.TorAmplitude.FlatOpcycles.hasTorAmplitude_obj₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/MiddleTwoOutOfThree.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/MiddleTwoOutOfThree.lean#L67). The attribute's comment: “(2), at the ringed-space Tor-amplitude predicate”.

> **[Stacks, Tag 08CJ] (2) at the ringed-space Tor-amplitude predicate.** In a distinguished
> triangle `K ⟶ L ⟶ M ⟶ K[1]` of `D(O_X)`, if `K` has Tor amplitude in `[a, b]` and `M` has Tor
> amplitude in `[a, b]`, then `L` has Tor amplitude in `[a, b]`.
>
> This is `TorAmplitude.hasTorAmplitude_obj₂` read through `tensorSingleFunctor`; the only content
> is the translation between the two encodings of "outside `[a, b]`".

```lean
theorem hasTorAmplitude_obj₂ (T : Triangle (DerivedCategory (Modules X)))
    (hT : T ∈ distinguishedTriangles) (a b : ℤ)
    (hK : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X T.obj₁ a b)
    (hM : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X T.obj₃ a b) :
    Stacks.Cohomology.TorAmplitude.HasTorAmplitude X T.obj₂ a b
```

**`TorAmplitude.hasTorAmplitude_obj₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/Triangles.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/Triangles.lean#L91). The attribute's comment: “(1)”. References: SGA 6 I (5.3), “partial”; SGA 6 III (3.2), “Triangulatedness clause”.

> Stacks Tag 08CJ (1): in a distinguished triangle `K → L → M → K[1]`, if `K` has
> tor-amplitude in `[a+1, b+1]` and `L` has tor-amplitude in `[a, b]`, then `M` has
> tor-amplitude in `[a, b]`.

```lean
theorem hasTorAmplitude_obj₃ (T : Triangle (DerivedCategory M))
    (hT : T ∈ distinguishedTriangles) (a b : ℤ)
    (hK : HasTorAmplitude derTensor T.obj₁ (a + 1) (b + 1))
    (hL : HasTorAmplitude derTensor T.obj₂ a b) :
    HasTorAmplitude derTensor T.obj₃ a b
```

**`TorAmplitude.hasTorAmplitude_obj₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/Triangles.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/Triangles.lean#L114). The attribute's comment: “(2)”. References: SGA 6 I (5.3), “partial”; SGA 6 III (3.2), “Triangulatedness clause”.

> Stacks Tag 08CJ (2): in a distinguished triangle `K → L → M → K[1]`, if `K` and `M`
> both have tor-amplitude in `[a, b]`, then `L` has tor-amplitude in `[a, b]`.

```lean
theorem hasTorAmplitude_obj₂ (T : Triangle (DerivedCategory M))
    (hT : T ∈ distinguishedTriangles) (a b : ℤ)
    (hK : HasTorAmplitude derTensor T.obj₁ a b)
    (hM : HasTorAmplitude derTensor T.obj₃ a b) :
    HasTorAmplitude derTensor T.obj₂ a b
```

**`TorAmplitude.hasTorAmplitude_obj₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/Triangles.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/Triangles.lean#L137). The attribute's comment: “(3)”. References: SGA 6 I (5.3), “partial”; SGA 6 III (3.2), “Triangulatedness clause”.

> Stacks Tag 08CJ (3): in a distinguished triangle `K → L → M → K[1]`, if `L` has
> tor-amplitude in `[a+1, b+1]` and `M` has tor-amplitude in `[a, b]`, then `K` has
> tor-amplitude in `[a+1, b+1]`.

```lean
theorem hasTorAmplitude_obj₁ (T : Triangle (DerivedCategory M))
    (hT : T ∈ distinguishedTriangles) (a b : ℤ)
    (hL : HasTorAmplitude derTensor T.obj₂ (a + 1) (b + 1))
    (hM : HasTorAmplitude derTensor T.obj₃ a b) :
    HasTorAmplitude derTensor T.obj₁ (a + 1) (b + 1)
```

## Tag 09J4, a lemma

[Tag 09J4](https://stacks.math.columbia.edu/tag/09J4) in the Stacks Project.

**`Stacks.Cohomology.TorAmplitude.Tensor.hasTorAmplitude_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/TensorProduct.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/TensorProduct.lean#L157).

> If `K` has Tor amplitude in `[a, b]` and `L` has Tor amplitude in `[c, d]`, then
> `K ⊗^L_{O_X} L` has Tor amplitude in `[a + c, b + d]`.

```lean
theorem hasTorAmplitude_derivedTensor (K L : DerivedCategory (Modules X)) (a b c d : ℤ)
    (hK : HasTorAmplitude X K a b)
    (hL : HasTorAmplitude X L c d) :
    HasTorAmplitude X
      (((derTensor X).tensor.obj K).obj L) (a + c) (b + d)
```

## Tag 08CK, a lemma

[Tag 08CK](https://stacks.math.columbia.edu/tag/08CK) in the Stacks Project.

**`Stacks.Cohomology.TorAmplitude.hasTorAmplitude_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/BiproductSum.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/BiproductSum.lean#L68). The attribute's comment: “from the summands to the sum, at the ringed-space Tor-amplitude predicate”.

> **[Stacks, Tag 08CK], from the summands to the sum.** If `K` and `L` have Tor amplitude in
> `[a, b]` then so does `K ⊞ L`.
>
> The split triangle `K ⟶ K ⊞ L ⟶ L ⟶ K⟦1⟧` is distinguished, so this is clause (2) of
> [Stacks, Tag 08CJ].

```lean
theorem hasTorAmplitude_biprod (a b : ℤ) (K L : DerivedCategory (OXMod.{u, u} X))
    (hK : HasTorAmplitude X K a b) (hL : HasTorAmplitude X L a b) :
    HasTorAmplitude X (K ⊞ L) a b
```

**`Stacks.Cohomology.TorAmplitude.hasFiniteTorDimension_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/BiproductSum.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/BiproductSum.lean#L78). The attribute's comment: “finite Tor dimension, from the summands to the sum”.

> **Finite Tor dimension passes from two summands to their sum.** The two intervals are
> merged.

```lean
theorem hasFiniteTorDimension_biprod (K L : DerivedCategory (OXMod.{u, u} X))
    (hK : HasFiniteTorDimension X K) (hL : HasFiniteTorDimension X L) :
    HasFiniteTorDimension X (K ⊞ L)
```

**`Stacks.TorAmplitude.hasTorAmplitude_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/Defs.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/Defs.lean#L190).

> **Statement 1 (Tag 08CK / Lemma 20.48.8).**  Let `(X, 𝒪_X)` be a ringed space
> and `a ≤ b`.  We work with THE derived tensor product `- ⊗^L_{𝒪_X} -` on
> `D(𝒪_X)`: it is given as a bifunctor `derivedTensor` whose flips
> `- ⊗^L F = derivedTensor.flip.obj (single F)` are, together with the comparison
> natural transformation `derivedTensorComparison F`, the **total left derived
> functors** (`IsLeftDerivedFunctor`) of the underived tensor products `- ⊗ F`.
> This universal property determines `derivedTensor` up to canonical isomorphism, so
> it is genuinely the derived tensor product (introduced here as hypotheses rather
> than as `axiom`s).
>
> If the direct sum `K ⊕ L` (categorical biproduct `K ⊞ L`) has tor-amplitude in
> `[a,b]`, then both `K` and `L` have tor-amplitude in `[a,b]`.

```lean
theorem hasTorAmplitude_of_biprod
    (derivedTensor : DOX X ⥤ DOX X ⥤ DOX X)
    (a b : ℤ)
    (K L : DOX X) (h : HasTorAmplitude derivedTensor a b (K ⊞ L)) :
    HasTorAmplitude derivedTensor a b K ∧ HasTorAmplitude derivedTensor a b L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.48, Tag 08CF](https://stacks.math.columbia.edu/tag/08CF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
