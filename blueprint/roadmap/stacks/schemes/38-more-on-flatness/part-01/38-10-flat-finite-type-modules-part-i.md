---
declaration: section
origin: cited
lean: Algebra.closedFiberIdeal_isPrime, Module.freeMapAtResidueField, Module.flat_localizedModule_tfae, Module.CompleteDevissageAt.finitePresentation_free_linearEquiv_directSum_of_flat, AlgebraicGeometry.existsElementaryEtaleNeighborhoodFinitePresentationFlatOver, AlgebraicGeometry.isOpen_isFlatOverAt_fiber, AlgebraicGeometry.isOpen_isFlatOverAt_fiber_of_locallyOfFiniteType, AlgebraicGeometry.ElementaryEtaleFlatness.exists_elementaryEtaleNeighborhood_open_flat
statement: formalized
proof: formalized
---

# 38.10 Flat finite type modules, Part I

Section 38.10 of the Stacks Project, [Tag 05I2](https://stacks.math.columbia.edu/tag/05I2). 10 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05I3, a lemma

[Tag 05I3](https://stacks.math.columbia.edu/tag/05I3) in the Stacks Project.

**`Algebra.closedFiberIdeal_isPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/CompleteDevissageStep.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/CompleteDevissageStep.lean#L92). The attribute's comment: “the generic point of the closed fibre”.

> **Stacks Project, Tag 05I3, the generic point of the closed fibre.** If the fibres of
> `Spec S ⟶ Spec R` are geometrically integral, the ideal extending the maximal ideal of the
> local ring `R` is prime.

```lean
public theorem Algebra.closedFiberIdeal_isPrime
    (R : Type u) (S : Type u) [CommRing R] [CommRing S] [IsLocalRing R] [Algebra R S]
    [GeometricallyIntegral (Spec.map (CommRingCat.ofHom (algebraMap R S)))] :
    (Algebra.closedFiberIdeal R S).IsPrime
```

**`Module.freeMapAtResidueField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/CompleteDevissageStep.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/CompleteDevissageStep.lean#L112). The attribute's comment: “construction of the free map”.

> **Stacks Project, Tag 05I3, construction of the free map.** For a finite module and a prime
> ideal `p`, some map from a finite free module becomes an isomorphism after tensoring with the
> residue field at `p`.

```lean
public noncomputable def Module.freeMapAtResidueField
    (S : Type u) [CommRing S] (p : Ideal S) [p.IsPrime]
    (N : Type v) [AddCommGroup N] [Module S N] [Module.Finite S N] :
    Σ r : ℕ, { alpha : (Fin r → S) →ₗ[S] N //
      Function.Bijective (alpha.rTensor p.ResidueField) }
```

**`Module.flat_localizedModule_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/DevissageFlatTfae.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/DevissageFlatTfae.lean#L193). The attribute's comment: “the five equivalent conditions”.

> **Stacks Project, Tag 05I3, the five equivalent conditions**, with the universe of the module
> independent of that of the base ring and the algebra.
>
> Every hypothesis of the source is present and no others: `R` is local, `R → S` is flat of finite
> presentation with geometrically integral fibres, `q` lies over the maximal ideal, `N` is a finite
> `S`-module and `alpha` becomes an isomorphism over the residue field of `𝔪S`. Projectivity of
> `S` over `R`, which the source invokes to run the argument, is Stacks 05FT
> (`Algebra.projective_of_geometricallyIntegral_fibres`) applied to the geometrically integral
> fibres.

```lean
public theorem flat_localizedModule_tfae
    (R : Type u) (S : Type u) [CommRing R] [CommRing S] [IsLocalRing R] [Algebra R S]
    [Algebra.FinitePresentation R S] [Module.Flat R S]
    [AlgebraicGeometry.GeometricallyIntegral
      (AlgebraicGeometry.Spec.map (CommRingCat.ofHom (algebraMap R S)))]
    [(Algebra.closedFiberIdeal R S).IsPrime]
    (q : Ideal S) [q.IsPrime]
    (hq : q.comap (algebraMap R S) = IsLocalRing.maximalIdeal R)
    (N : Type w) [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [Module.Finite S N]
    (r : ℕ) (alpha : (Fin r → S) →ₗ[S] N)
    (halpha : Function.Bijective (alpha.rTensor (Algebra.closedFiberIdeal R S).ResidueField)) :
    List.TFAE [
      Module.Flat R (LocalizedModule q.primeCompl N),
      Stacks.UniversalInjectivity.LocalizationCriteria.UniversallyInjective.{max u w}
        (alpha.restrictScalars R) ∧
        Module.Flat R (LocalizedModule q.primeCompl (N ⧸ LinearMap.range alpha)),
      Function.Injective alpha ∧
        Module.Flat R (LocalizedModule q.primeCompl (N ⧸ LinearMap.range alpha)),
      Function.Bijective
          (LocalizedModule.map (Algebra.closedFiberIdeal R S).primeCompl alpha) ∧
        Module.Flat R (LocalizedModule q.primeCompl (N ⧸ LinearMap.range alpha)),
      Function.Injective (LocalizedModule.map q.primeCompl alpha) ∧
        Module.Flat R (LocalizedModule q.primeCompl (N ⧸ LinearMap.range alpha))]
```

## Tag 05I4, a lemma

[Tag 05I4](https://stacks.math.columbia.edu/tag/05I4) in the Stacks Project.

**`Module.CompleteDevissageAt.finitePresentation_free_linearEquiv_directSum_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/DevissageProjectiveStages.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/DevissageProjectiveStages.lean#L441).

> **Stacks Project, Tag 05I4.** Let `(R, 𝔪)` be a local ring, let `R → S` be a ring map of
> finite presentation, let `N` be a finite `S`-module and let `q` be a prime of `S` lying over `𝔪`.
> Assume that `N_q` is flat over `R` and that `D` is a complete dévissage of `N/S/R` at `q`. Then `N`
> is a finitely presented `S`-module, free as an `R`-module, and there is an isomorphism of
> `R`-modules `N ≅ B₁^{⊕ r₁} ⊕ … ⊕ Bₙ^{⊕ rₙ}`, where `B₁, …, Bₙ` are the lower algebras of `D` and
> each `Bᵢ` is a smooth `R`-algebra with geometrically irreducible fibres.

```lean
public theorem finitePresentation_free_linearEquiv_directSum_of_flat [IsLocalRing R] [Module R N]
    [IsScalarTower R S N] [Algebra.FinitePresentation R S]
    (D : CompleteDevissageAt R S N q) (hq : q.under R = IsLocalRing.maximalIdeal R)
    (hflat : Module.Flat R (LocalizedModule q.primeCompl N)) :
    Module.FinitePresentation S N ∧ Module.Free R N ∧
      (∀ i : Fin D.length, Algebra.Smooth R (D.lowerAlgebra i) ∧
        GeometricallyIrreducible
          (Spec.map (CommRingCat.ofHom (algebraMap R (D.lowerAlgebra i))))) ∧
      Nonempty (N ≃ₗ[R] ⨁ i : Fin D.length, (Fin (D.multiplicity i) →₀ D.lowerAlgebra i))
```

## Tag 05I5, a proposition

[Tag 05I5](https://stacks.math.columbia.edu/tag/05I5) in the Stacks Project.

**`AlgebraicGeometry.existsElementaryEtaleNeighborhoodFinitePresentationFlatOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhoodFlatness.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhoodFlatness.lean#L392).

> **Stacks Project, Tag 05I5.** For `f` locally of finite presentation and `F` quasi-coherent of
> finite type and flat over `S` at `x`, there is an elementary étale neighbourhood `(S', s')` of
> `(S, f x)` and an open subscheme of `X ×_S Spec 𝒪_{S', s'}` containing the unique point over `x`
> on which the pullback of `F` is of finite presentation and flat over `𝒪_{S', s'}`.
>
> Here `U` is the elementary étale neighbourhood `(S', s')`, the base change is along the composite
> `Spec 𝒪_{S', s'} ⟶ S' ⟶ S`, `V` is the open subscheme and `v` the point of `V` over `x`; the
> first clause says that `v` is the only point of `X ×_S Spec 𝒪_{S', s'}` over `x`. Its type is
> the body of `AlgebraicGeometry.ExistsElementaryEtaleNeighborhoodFinitePresentationFlatOver`,
> written out.
>
> The pointwise form above composed with
> `AlgebraicGeometry.ExistsElementaryEtaleNeighborhoodFinitePresentationFlatOver.of_mem`, which
> supplies the uniqueness of the point over `x`.

```lean
theorem existsElementaryEtaleNeighborhoodFinitePresentationFlatOver
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f] (F : X.Modules)
    [F.IsQuasicoherent] [F.IsFiniteType] (x : X)
    (hflat : IsFlatOverAt f.toLRSHom.toShHom F x) :
    ∃ (U : EtaleNeighborhood S (f x)) (_ : U.IsElementary)
      (V : (pullback f (U.scheme.fromSpecStalk U.point ≫ U.toBase)).Opens) (v : V),
      (pullback.fst f (U.scheme.fromSpecStalk U.point ≫ U.toBase) ⁻¹' {x} = {V.ι v}) ∧
      ((Scheme.Modules.pullback
        (V.ι ≫ pullback.fst f (U.scheme.fromSpecStalk U.point ≫ U.toBase))).obj
          F).IsFinitePresentation ∧
      IsFlatOver
        (LocallyRingedSpace.forgetToSheafedSpace.map
          (V.ι ≫ pullback.snd f (U.scheme.fromSpecStalk U.point ≫ U.toBase)).toLRSHom)
        ((Scheme.Modules.pullback
          (V.ι ≫ pullback.fst f (U.scheme.fromSpecStalk U.point ≫ U.toBase))).obj F)
```

## Tag 05M9, a lemma

[Tag 05M9](https://stacks.math.columbia.edu/tag/05M9) in the Stacks Project.

**`AlgebraicGeometry.isOpen_isFlatOverAt_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FlatFiniteTypeModules.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FlatFiniteTypeModules.lean#L340). The attribute's comment: “for f locally of finite presentation”.

> **Stacks Project, Tag 05M9** for a morphism locally of finite presentation: in every fibre of
> `f`, the locus where a finite type quasi-coherent `𝒪_X`-module is flat over the base is open.
>
> The source states this for `f` locally of finite type, and deduces it from Tag 05I5, which
> assumes locally of finite presentation. For `f` only locally of finite type the same argument
> needs Tag 05KT in place of Tag 05I5; that deduction is
> `AlgebraicGeometry.isOpen_isFlatOverAt_fiber_of_exists`.

```lean
theorem isOpen_isFlatOverAt_fiber {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFinitePresentation f] (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (s : S) :
    IsOpen {w : f.fiber s | IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s w)}
```

**`AlgebraicGeometry.isOpen_isFlatOverAt_fiber_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FlatFiniteTypeNeighborhood.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FlatFiniteTypeNeighborhood.lean#L382).

> In every fibre of a morphism locally of finite type, the locus where a quasi-coherent module of
> finite type is flat over the base is open.

```lean
theorem isOpen_isFlatOverAt_fiber_of_locallyOfFiniteType {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (s : S) :
    IsOpen {w : f.fiber s | IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s w)}
```

## Tag 05KT, a lemma

[Tag 05KT](https://stacks.math.columbia.edu/tag/05KT) in the Stacks Project.

**`AlgebraicGeometry.ElementaryEtaleFlatness.exists_elementaryEtaleNeighborhood_open_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FlatnessAtPoint.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FlatnessAtPoint.lean#L71).

> **Stacks Project, Tag 05KT.** Flatness at a point of a finite type quasi-coherent module
> spreads to an open neighbourhood after base change to the local scheme of a suitable
> elementary étale neighbourhood of the image point.

```lean
theorem exists_elementaryEtaleNeighborhood_open_flat
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (x : X)
    (hF : AlgebraicGeometry.IsFlatOverAt f.toLRSHom.toShHom F x) :
    ∃ (U : AlgebraicGeometry.EtaleNeighborhood S (f x)) (_ : U.IsElementary),
      let g := U.scheme.fromSpecStalk U.point ≫ U.toBase
      let P : Scheme.{u} := pullback f g
      ∃ (z : P) (_ : pullback.fst f g z = x)
      (_ : ∀ z' : P, pullback.fst f g z' = x → z' = z) (V : P.Opens),
      z ∈ V ∧
        AlgebraicGeometry.IsFlatOver
          (((V.ι : V.toScheme ⟶ P) ≫ pullback.snd f g).toLRSHom.toShHom)
          ((Scheme.Modules.pullback
            ((V.ι : V.toScheme ⟶ P) ≫ pullback.fst f g)).obj F)
```

**`AlgebraicGeometry.existsElementaryEtaleNeighborhoodFlatOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FlatFiniteTypeNeighborhood.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FlatFiniteTypeNeighborhood.lean#L372).

> For a morphism `f : X ⟶ S` locally of finite type and a quasi-coherent `𝒪_X`-module `F` of
> finite type which is flat over `S` at `x`, there is an elementary étale neighbourhood `(S', s')` of
> `(S, f x)` and an open subscheme of `X ×_S Spec 𝒪_{S', s'}` containing the unique point over `x` on
> which the pullback of `F` is flat over `𝒪_{S', s'}`.

```lean
theorem existsElementaryEtaleNeighborhoodFlatOver :
    ExistsElementaryEtaleNeighborhoodFlatOver.{u}
```

## Tag 05KU, a lemma

[Tag 05KU](https://stacks.math.columbia.edu/tag/05KU) in the Stacks Project.

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_isFinitePresentation_isFlatOver_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FlatOverFibre.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FlatOverFibre.lean#L330).

> **Stacks Project, Tag 05KU.** Let `f : X ⟶ S` be of finite presentation, let `F` be a
> quasi-coherent `𝒪_X`-module of finite type, and let `s` be a point of `S` such that `F` is flat
> over `S` at every point of the fibre `X_s`. Then there are an elementary étale neighbourhood
> `(S', s')` of `(S, s)` and an open `V ⊆ X ×_S Spec 𝒪_{S', s'}` containing the whole fibre
> `X_s = X ×_S s'` such that the pullback of `F` to `V` is of finite presentation as an
> `𝒪_V`-module and flat over `𝒪_{S', s'}`.
>
> The fibre `X ×_S s'` is read as the set of points of `X ×_S Spec 𝒪_{S', s'}` whose image in `X`
> lies over `s`.

```lean
theorem exists_elementaryEtaleNeighborhood_isFinitePresentation_isFlatOver_fiber
    {X S : Scheme.{u}} (f : X ⟶ S) (hf : FinitePresentation f) (F : X.Modules)
    [F.IsQuasicoherent] [F.IsFiniteType] (s : S)
    (hflat : ∀ x : X, f x = s → IsFlatOverAt f.toLRSHom.toShHom F x) :
    ∃ (U : EtaleNeighborhood S s) (_ : U.IsElementary)
      (V : (pullback f (U.scheme.fromSpecStalk U.point ≫ U.toBase)).Opens),
      (∀ z : ↑(pullback f (U.scheme.fromSpecStalk U.point ≫ U.toBase)),
          f (pullback.fst f (U.scheme.fromSpecStalk U.point ≫ U.toBase) z) = s → z ∈ V) ∧
      ((Scheme.Modules.pullback (V.ι ≫ pullback.fst f
          (U.scheme.fromSpecStalk U.point ≫ U.toBase))).obj F).IsFinitePresentation ∧
      IsFlatOver
        (V.ι ≫ pullback.snd f
          (U.scheme.fromSpecStalk U.point ≫ U.toBase)).toLRSHom.toShHom
        ((Scheme.Modules.pullback (V.ι ≫ pullback.fst f
          (U.scheme.fromSpecStalk U.point ≫ U.toBase))).obj F)
```

## Tag 05KV, a lemma

[Tag 05KV](https://stacks.math.columbia.edu/tag/05KV) in the Stacks Project.

**`AlgebraicGeometry.ElementaryEtaleFlatness.exists_elementaryEtaleNeighborhood_open_flat_along_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FlatnessAlongFibre.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FlatnessAlongFibre.lean#L528).

> **Stacks Project, Tag 05KV.** Flatness of a finite type quasi-coherent module along
> a fibre spreads to an open neighbourhood of that fibre after passing to the local scheme
> of an elementary étale neighbourhood of the base point.

```lean
theorem exists_elementaryEtaleNeighborhood_open_flat_along_fibre
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (s : S)
    (hF : ∀ x : X, f x = s → AlgebraicGeometry.IsFlatOverAt f.toLRSHom.toShHom F x) :
    ∃ (U : AlgebraicGeometry.EtaleNeighborhood S s) (_ : U.IsElementary),
      let g := U.scheme.fromSpecStalk U.point ≫ U.toBase
      let P : Scheme.{u} := pullback f g
      ∃ (V : P.Opens),
        (∀ z : P, pullback.snd f g z = IsLocalRing.closedPoint _ → z ∈ V) ∧
          AlgebraicGeometry.IsFlatOver
            (((V.ι : V.toScheme ⟶ P) ≫ pullback.snd f g).toLRSHom.toShHom)
            ((Scheme.Modules.pullback
              ((V.ι : V.toScheme ⟶ P) ≫ pullback.fst f g)).obj F)
```

## Tag 05I6, a lemma

[Tag 05I6](https://stacks.math.columbia.edu/tag/05I6) in the Stacks Project.

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_flat_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FlatFiniteTypeSchemeNeighborhood.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FlatFiniteTypeSchemeNeighborhood.lean#L236).

> **Stacks Project, Tag 05I6.** Let `X` be locally of finite type over `S` and let `x ∈ X` be a
> point at which `X` is flat over `S`. Then there is an elementary étale neighbourhood `(S', s')`
> of `(S, f x)` and an open subscheme of `X ×_S Spec 𝒪_{S', s'}` containing the unique point over
> `x` which is flat and of finite presentation over `Spec 𝒪_{S', s'}`.

```lean
theorem exists_elementaryEtaleNeighborhood_flat_finitePresentation {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] (x : X) (hflat : IsFlatAt f.toLRSHom.toShHom x) :
    ∃ (U : EtaleNeighborhood S (f x)) (_ : U.IsElementary),
      let b : Spec (U.scheme.presheaf.stalk U.point) ⟶ S :=
        U.scheme.fromSpecStalk U.point ≫ U.toBase
      ∃ (V : (pullback f b).Opens) (v : V),
        (pullback.fst f b ⁻¹' {x} = {V.ι v}) ∧
        Flat (V.ι ≫ pullback.snd f b) ∧
        FinitePresentation (V.ι ≫ pullback.snd f b)
```

## Tag 05I7, a lemma

[Tag 05I7](https://stacks.math.columbia.edu/tag/05I7) in the Stacks Project.

**`Stacks.Flatness.finitePresentation_stalk_of_isFlatOverAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/StalkFinitePresentation.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/StalkFinitePresentation.lean#L86).

> **Stacks Project, Tag 05I7, from Stacks Project, Tag 05I5.** Let `f : X ⟶ S` be locally of
> finite presentation and let `F` be a finite type quasi-coherent `𝒪_X`-module. If `F` is flat over
> `S` at `x`, then the stalk `F_x` is a finitely presented `𝒪_{X,x}`-module.
>
> Stacks 05I5 is `AlgebraicGeometry.existsElementaryEtaleNeighborhoodFinitePresentationFlatOver`.
> The neighbourhood it produces maps to `X` by a flat morphism, the pullback of `F` to it is
> finitely presented, so its stalk is finitely presented
> (`Stacks.StalkFiniteType.finitePresentation_stalk`), and finite presentation descends along the
> flat local homomorphism of local rings that the stalk map is
> (`Stacks.StalkFiniteType.finitePresentation_stalk_of_flat`).

```lean
theorem finitePresentation_stalk_of_isFlatOverAt
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f] (F : X.Modules)
    [F.IsQuasicoherent] [F.IsFiniteType] (x : X)
    (hflat : IsFlatOverAt f.toLRSHom.toShHom F x) :
    Module.FinitePresentation (ToType (X.presheaf.stalk x))
      (ToType (TopCat.Presheaf.stalk F.val.presheaf x))
```

## Tag 05I8, a lemma

[Tag 05I8](https://stacks.math.columbia.edu/tag/05I8) in the Stacks Project.

**`AlgebraicGeometry.isEssentiallyOfFinitePresentation_stalkMap_of_flatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/StalkEssentiallyFinitePresentation.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/StalkEssentiallyFinitePresentation.lean#L151).

> **Stacks Project, Tag 05I8.** If `f : X ⟶ S` is locally of finite type and flat at `x`, then
> the local ring `𝒪_{X,x}` is essentially of finite presentation over `𝒪_{S,f x}`.

```lean
theorem isEssentiallyOfFinitePresentation_stalkMap_of_flatAt
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (x : X) (hflat : AlgebraicGeometry.IsFlatAt f.toLRSHom.toShHom x) :
    IsEssentiallyOfFinitePresentation
      (S.presheaf.stalk (f x)) (X.presheaf.stalk x) (f.stalkMap x).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.10, Tag 05I2](https://stacks.math.columbia.edu/tag/05I2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
