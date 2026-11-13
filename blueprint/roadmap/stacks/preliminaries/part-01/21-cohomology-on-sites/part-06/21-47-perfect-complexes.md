---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.IsPerfectComplex, AlgebraicGeometry.RingedSite.IsPerfect, AlgebraicGeometry.RingedSite.isPerfect_of_coveringFamily_strictlyPerfect, AlgebraicGeometry.RingedSite.isPerfect_of_coveringFamily_strictlyPerfect_general, AlgebraicGeometry.RingedSite.isPerfectComplex_of_isPerfect_representation, Stacks.SheafOfModules.DerivedTensorProduct.torAmplitudePerfectnessCriterion, Stacks.SheafOfModules.DerivedTensorProduct.isPerfect_iff_isPseudoCoherent_and_locallyHasFiniteTorDimension, Stacks.Cohomology.TorAmplitude.hasFiniteTorDimension_of_ringedSite_isPerfect
statement: formalized
proof: formalized
---

# 21.47 Perfect complexes

Section 21.47 of the Stacks Project, [Tag 08G4](https://stacks.math.columbia.edu/tag/08G4). 8 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08G5, a definition

[Tag 08G5](https://stacks.math.columbia.edu/tag/08G5) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.IsPerfectComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/PerfectObjects.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/PerfectObjects.lean#L66). The attribute's comment: “perfect complexes”.

> **Stacks 08G5, perfect complexes.** A complex `E` of `O`-modules is *perfect* if every
> object `U` of the site admits a covering `{V → U}` over each member of which there are a
> strictly perfect complex `P` of `O|_V`-modules and a quasi-isomorphism `P ⟶ E|_V`.

```lean
noncomputable def IsPerfectComplex
    (E : CochainComplex (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) :
    Prop
```

**`AlgebraicGeometry.RingedSite.IsPerfect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/PerfectObjects.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/PerfectObjects.lean#L113). The attribute's comment: “perfect derived-category objects”.

> **Stacks 08G5, perfect objects of the derived category.** An object of `D(O)` is *perfect*
> if it is isomorphic to the image of a perfect complex.

```lean
noncomputable def IsPerfect
    [HasDerivedCategory.{d} (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    (K : DerivedCategory (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    Prop
```

## Tag 08G6, a lemma

[Tag 08G6](https://stacks.math.columbia.edu/tag/08G6) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isPerfect_of_coveringFamily_strictlyPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/LocalModels.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/LocalModels.lean#L250). The attribute's comment: “local\_strictly\_perfect\_implies\_perfect”.

> **Stacks 08G6, part (1).** Let `(C, O)` be a ringed site whose underlying category has a
> final object `T` and let `E` be an object of `D(O)`. If there are a covering `{V → T}`, strictly
> perfect complexes `P_V` of `O|_V`-modules and isomorphisms `P_V ≅ E|_V` in `D(O|_V)`, then `E` is
> perfect.

```lean
theorem isPerfect_of_coveringFamily_strictlyPerfect
    (T : X.C) (hT : IsTerminal T)
    (E : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (h : ∃ S : Presieve T, Sieve.generate S ∈ X.J T ∧
      ∀ ⦃V : X.C⦄ (f : V ⟶ T), S f →
        ∃ P : CochainComplex
            (SheafOfModules.{w} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over V)) ℤ,
          IsStrictlyPerfect ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over V) P ∧
            Nonempty (DerivedCategory.Q.obj P ≅
              (SheafOfModules.overFunctor.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
                V).mapDerivedCategory.obj E)) :
    X.IsPerfect E
```

**`AlgebraicGeometry.RingedSite.isPerfect_of_coveringFamily_strictlyPerfect_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/LocalModelsGeneral.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/LocalModelsGeneral.lean#L152). The attribute's comment: “local\_strictly\_perfect\_implies\_perfect”.

> Let `(C, O)` be a ringed site whose underlying category has a final object `T` and let `E` be
> an object of `D(O)`. If there are a covering `{V → T}`, strictly perfect complexes `P_V` of
> `O|_V`-modules and isomorphisms `P_V ≅ E|_V` in `D(O|_V)`, then `E` is perfect.

```lean
theorem isPerfect_of_coveringFamily_strictlyPerfect_general
    (T : X.C) (hT : IsTerminal T)
    (E : DerivedCategory (SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf.{u, v, w} X.O)))
    (h : ∃ S : Presieve T, Sieve.generate S ∈ X.J T ∧
      ∀ ⦃V : X.C⦄ (f : V ⟶ T), S f →
        ∃ P : CochainComplex
            (SheafOfModules.{w} ((Stacks.SheafOfModules.Tensor.ringSheaf.{u, v, w} X.O).over V)) ℤ,
          IsStrictlyPerfect ((Stacks.SheafOfModules.Tensor.ringSheaf.{u, v, w} X.O).over V) P ∧
            Nonempty (DerivedCategory.Q.obj P ≅
              (SheafOfModules.overFunctor.{w} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, v, w} X.O)
                V).mapDerivedCategory.obj E)) :
    X.IsPerfect E
```

**`AlgebraicGeometry.RingedSite.isPerfectComplex_of_isPerfect_representation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/Representatives.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/Representatives.lean#L100). The attribute's comment: “perfect\_independent\_of\_representative”.

> **Stacks 08G6, part (2).** Let `(C, O)` be a ringed site and let `K` be a perfect object of
> `D(O)`. Then every complex of `O`-modules representing `K` is a perfect complex.

```lean
theorem isPerfectComplex_of_isPerfect_representation
    {K : DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (hK : X.IsPerfect K)
    {F : CochainComplex (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ}
    (hF : Nonempty (DerivedCategory.Q.obj F ≅ K)) :
    X.IsPerfectComplex F
```

## Tag 08G7, a lemma

[Tag 08G7](https://stacks.math.columbia.edu/tag/08G7) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedTensorProduct.torAmplitudePerfectnessCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/PerfectnessCriterion.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/PerfectnessCriterion.lean#L288). References: SGA 6 I (5.8), “(ii) ⟹ (i)”.

> **Stacks 08G7.** Let `(C, O)` be a ringed site and let `T` be a derived tensor product on
> `D(O)`. An object of `D(O)` with Tor amplitude in `[a, b]` for `T`, with `a ≤ b`, which is
> `(a - 1)`-pseudo-coherent, is perfect.
>
> The proof reads Tor amplitude on each slice `(C/U, O|_U)`, which needs a derived tensor product
> there; that is the derived tensor product of Stacks 06YU,
> `Stacks.SheafOfModules.canonicalDerivedTensorProduct`, which exists on each slice under the
> hypotheses already in force, so it is not a parameter of the statement.

```lean
theorem torAmplitudePerfectnessCriterion
    (T : DerivedTensorProduct.{0, 0, 0, d} Z) :
    TorAmplitudePerfectnessCriterion T
```

## Tag 08G8, a lemma

[Tag 08G8](https://stacks.math.columbia.edu/tag/08G8) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedTensorProduct.isPerfect_iff_isPseudoCoherent_and_locallyHasFiniteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/PerfectnessCriterion.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/PerfectnessCriterion.lean#L195). References: SGA 6 I (5.8.1).

> Let `(C, O)` be a ringed site. An object of `D(O)` is perfect if and only if it is
> pseudo-coherent and locally has finite Tor dimension, measured on each slice `(C/U, O|_U)` against
> the derived tensor product `Stacks.SheafOfModules.canonicalDerivedTensorProduct`.

```lean
theorem isPerfect_iff_isPseudoCoherent_and_locallyHasFiniteTorDimension
    (E : RingedSite.DerivedModules.{0, 0, 0, d} Z) :
    Z.IsPerfect E ↔ Z.IsPseudoCoherent E ∧
      LocallyHasFiniteTorDimension
        (fun U : Z.C => canonicalDerivedTensorProduct.{0, 0, d} (Z.over U)) E
```

**`Stacks.Cohomology.TorAmplitude.hasFiniteTorDimension_of_ringedSite_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/FiniteTorDimensionOfAPerfectObject.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/FiniteTorDimensionOfAPerfectObject.lean#L180). The attribute's comment: “a perfect object has finite tor dimension, globally on a quasi-compact space”. References: SGA 6 0 (3.1), “partial”; SGA 6 I (8.5), “partial”; SGA 6 III (4.2), “special case”.

> **Stacks 08G8 globally, on a quasi-compact ringed space.** An object of `D(O_X)` which is
> perfect for the site of opens of `X` has finite Tor dimension against any derived tensor product
> datum of Stacks 06YU on that site.
>
> Perfectness is transported to the ringed-space spelling by
> `Stacks.Cohomology.PerfectComplexes.isPerfect_of_ringedSite`, which is what makes the
> Tor-amplitude machinery applicable; `locallyHasFiniteTorDimension_of_isPerfect` then supplies the
> local intervals, quasi-compactness makes them one interval, and the bridge reads it against
> `T`.

```lean
theorem hasFiniteTorDimension_of_ringedSite_isPerfect [CompactSpace X.carrier]
    (T : Stacks.SheafOfModules.DerivedTensorProduct.{u, u, u, d}
      (AlgebraicGeometry.RingedSpace.ringedSite X))
    (E : DerivedCategory (OXMod.{u, u} X))
    (hE : (AlgebraicGeometry.RingedSpace.ringedSite X).IsPerfect E) :
    Stacks.SheafOfModules.DerivedTensorProduct.HasFiniteTorDimension
      (X := AlgebraicGeometry.RingedSpace.ringedSite X) T E
```

## Tag 08H6, a lemma

[Tag 08H6](https://stacks.math.columbia.edu/tag/08H6) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.Hom.isPerfect_derivedPullback_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedPullbackAlongRingedTopoi.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedPullbackAlongRingedTopoi.lean#L274). The attribute's comment: “for a morphism of ringed sites in the sense of 00X1, with no finite limits on either site”.

> **Stacks 08H6.** Let `f : (C, O_C) ⟶ (D, O_D)` be a morphism of ringed sites and let `E` be
> an object of `D(O_D)`. If `E` is perfect, then `Lf^* E` is perfect in `D(O_C)`.
>
> The morphism of ringed sites is the one of Stacks 00X1: a continuous functor `u : D ⥤ C` whose
> `u_s` is exact. Neither site is assumed to have finite limits and `u` is not assumed to preserve
> them.
>
> Stacks 08H2 makes the objects `u(W)` cover the final object of `Sh(C)`, and
> `CategoryTheory.GrothendieckTopology.coversTop_obj_subtype` refines that covering to the `u(W)`
> over which `K` carries a strictly perfect derived model. Over such an object the pullback of the
> model is a strictly perfect derived model of `(Lf^* E)|_{u(W)}`
> (`hasStrictlyPerfectModel_image`, through the derived localization square
> `AlgebraicGeometry.RingedSite.Hom.nonempty_derivedPullbackLocalizedIso_of_noFiniteLimits`), and
> it descends along any arrow into `u(W)` by exactness of restriction
> (`hasStrictlyPerfectModel_of_hom`), which is what the arrows of that covering supply; Stacks
> 08G6 (1) assembles.

```lean
theorem Hom.isPerfect_derivedPullback_of_isPerfect
    (E : DerivedCategory
      (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf (ringedTopos Y).O)))
    (hE : Y.IsPerfect E) :
    X.IsPerfect ((derivedPullback f.toRingedToposSiteHom).obj E)
```

## Tag 08G9, a lemma

[Tag 08G9](https://stacks.math.columbia.edu/tag/08G9) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isPerfect_obj₃_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DistinguishedTriangles.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DistinguishedTriangles.lean#L233). The attribute's comment: “third object”.

> **Stacks 08G9, third object.** In a distinguished triangle of `D(O)`, the third object is
> perfect if the first two are.

```lean
theorem isPerfect_obj₃_of_distinguished
    (T : Triangle
      (DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hT : T ∈ distinguishedTriangles)
    (h₁ : X.IsPerfect T.obj₁) (h₂ : X.IsPerfect T.obj₂) :
    X.IsPerfect T.obj₃
```

**`AlgebraicGeometry.RingedSite.isPerfect_obj₂_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DistinguishedTriangles.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DistinguishedTriangles.lean#L280). The attribute's comment: “second object”.

> **Stacks 08G9, second object.** In a distinguished triangle of `D(O)`, the second object is
> perfect if the other two are.

```lean
theorem isPerfect_obj₂_of_distinguished
    (T : Triangle
      (DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hT : T ∈ distinguishedTriangles)
    (h₁ : X.IsPerfect T.obj₁) (h₃ : X.IsPerfect T.obj₃) :
    X.IsPerfect T.obj₂
```

**`AlgebraicGeometry.RingedSite.isPerfect_obj₁_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DistinguishedTriangles.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DistinguishedTriangles.lean#L292). The attribute's comment: “first object”.

> **Stacks 08G9, first object.** In a distinguished triangle of `D(O)`, the first object is
> perfect if the other two are.

```lean
theorem isPerfect_obj₁_of_distinguished
    (T : Triangle
      (DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hT : T ∈ distinguishedTriangles)
    (h₂ : X.IsPerfect T.obj₂) (h₃ : X.IsPerfect T.obj₃) :
    X.IsPerfect T.obj₁
```

## Tag 09JB, a lemma

[Tag 09JB](https://stacks.math.columbia.edu/tag/09JB) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isPerfect_derivedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedTensorProduct.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedTensorProduct.lean#L282).

> **Stacks 09JB.** Let `(C, O)` be a ringed site.  If `K` and `L` are perfect objects of
> `D(O)`, then so is `K ⊗^{𝐋}_O L`.
>
> Representatives of the two objects are replaced by resolutions `A` and `B` which are K-flat on
> the site and on every slice of it, so that `K ⊗^{𝐋} L` is the class of `Tot(A ⊗_O B)`.  Above
> an object of the site lying under a member of the covering that the perfectness of the first
> factor supplies and a member of the one the second supplies, both factors have strictly perfect
> models; the total tensor complex of those models is strictly perfect and is a local model of
> `Tot(A ⊗_O B)`.  Stacks 08G6 (1) turns that family of local models into perfectness.
>
> Stated for an arbitrary derived tensor product of Stacks 06YU, since only its `comparison`
> field is used.

```lean
theorem isPerfect_derivedTensorProduct
    (T : Stacks.DerivedTensor.RingedSite.DerivedTensorProduct X.O)
    (K L : DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K) (hL : X.IsPerfect L) :
    X.IsPerfect ((T.tensor.obj K).obj L)
```

**`AlgebraicGeometry.RingedSite.isPerfect_tensor_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/TensorOfPerfectObjects.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/TensorOfPerfectObjects.lean#L240). The attribute's comment: “if K, L are perfect objects of D(O), then so is K ⊗^L\_O L, on any ringed site RingedSite.\{u,u,u}”.

> **Stacks 09JB.** Let `(C, O)` be a ringed site whose objects, morphisms and sections lie in
> one universe.  If `K` and `L` are perfect objects of `D(O)`, then so is `K ⊗^{𝐋}_O L`.
>
> Representatives of the two objects are replaced by resolutions `A` and `B` which are K-flat on
> the site and on every slice of it, so that `K ⊗^{𝐋} L` is the class of `Tot(A ⊗_O B)`.  Above
> an object of the site lying under a member of the covering that the perfectness of the first
> factor supplies and a member of the one the second supplies, both factors have strictly perfect
> models; the total tensor complex of those models is strictly perfect and is a local model of
> `Tot(A ⊗_O B)`.  Stacks 08G6 (1) turns that family of local models into perfectness.
>
> Stated for an arbitrary derived tensor product of Stacks 06YU, since only its `comparison`
> field is used.

```lean
theorem isPerfect_tensor_of_isPerfect
    (T : Stacks.DerivedTensor.RingedSite.DerivedTensorProduct X.O)
    (K L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K) (hL : X.IsPerfect L) :
    X.IsPerfect ((T.tensor.obj K).obj L)
```

## Tag 08GA, a lemma

[Tag 08GA](https://stacks.math.columbia.edu/tag/08GA) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedTensorProduct.isPerfect_left_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DirectSummands.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DirectSummands.lean#L188). The attribute's comment: “first summand”.

> **Stacks 08GA.** Let `(C, O)` be a ringed site and let `K` and `L` be objects of `D(O)`. If
> `K ⊞ L` is perfect, then so is `K`.
>
> By Stacks 08G8 the biproduct is pseudo-coherent and locally has finite Tor dimension; Stacks
> 08FW gives the first condition for `K` and Stacks 08G3 the second, and Stacks 08G8 read
> backwards gives perfectness. Stacks 08G8 is read against the derived tensor product of Stacks
> 06YU on the slices and on the iterated slices; neither occurs in the statement.

```lean
theorem isPerfect_left_of_biprod
    (K L : RingedSite.DerivedModules.{0, 0, 0, d} Z) (h : Z.IsPerfect (K ⊞ L)) :
    Z.IsPerfect K
```

**`Stacks.SheafOfModules.DerivedTensorProduct.isPerfect_right_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DirectSummands.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DirectSummands.lean#L201). The attribute's comment: “second summand”.

> **Stacks 08GA.** If `K ⊞ L` is perfect, then so is `L`.

```lean
theorem isPerfect_right_of_biprod
    (K L : RingedSite.DerivedModules.{0, 0, 0, d} Z) (h : Z.IsPerfect (K ⊞ L)) :
    Z.IsPerfect L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.47, Tag 08G4](https://stacks.math.columbia.edu/tag/08G4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
