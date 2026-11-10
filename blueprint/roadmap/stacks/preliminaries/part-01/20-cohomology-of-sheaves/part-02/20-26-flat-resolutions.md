---
declaration: section
origin: cited
lean: main_left, main_right, Stacks.SheafOfModules.IsKFlat, Stacks.SheafOfModules.IsKFlat.quasiIso_le_inverseImage, Stacks.SheafOfModules.IsKFlat.quasiIso_rightTensorComplex_map, Stacks.SheafOfModules.KFlatStalkCriterion.kFlat_iff_stalkwise, Stacks.SheafOfModules.kFlat_tensorComplex, Stacks.SheafOfModules.kFlat_of_second_third
statement: formalized
proof: formalized
---

# 20.26 Flat resolutions

Section 20.26 of the Stacks Project, [Tag 06Y7](https://stacks.math.columbia.edu/tag/06Y7). 17 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06Y8, a lemma

[Tag 06Y8](https://stacks.math.columbia.edu/tag/06Y8) in the Stacks Project.

**`main_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TensorComplex/ExactFunctor/IsTriangulated.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TensorComplex/ExactFunctor/IsTriangulated.lean#L39). References: SGA 4 XVII (7.3.3), “special case”.

> **Statement 1.**  For a fixed complex `G`, the functor
> `Tleft G : F ↦ Tot(G ⊗ F)` on `K(Mod(O_X))` can be equipped with a functorial isomorphism
> `ξ` (a `CommShift ℤ` datum) making it an *exact functor of triangulated categories* (Stacks
> Tag 06Y8, left version).
>
> Here `ξ` is the canonical comparison isomorphism `Tot(G ⊗ F[1]) ≅ Tot(G ⊗ F)[1]` of Stacks
> Tag 0FNG, and `Functor.IsTriangulated` packages exactly the requirement of Definition 3: the
> `CommShift` natural isomorphism together with preservation of distinguished triangles.
>
> Note the descent of the functor to `K(Mod(O_X))` is *asserted as content* (via `Tleft`,
> which is built from `TleftCochain_preservesHomotopyRel`), not assumed as a hypothesis.

```lean
theorem main_left (G : CochainComplex C ℤ) :
    ∃ e : (Tleft G).CommShift ℤ,
      @Functor.IsTriangulated _ _ _ _ _ _ (Tleft G) e _ _ _ _ _ _ _ _
```

**`main_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TensorComplex/ExactFunctor/IsTriangulated.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TensorComplex/ExactFunctor/IsTriangulated.lean#L52). References: SGA 4 XVII (7.3.3), “special case”.

> **Statement 2.**  For a fixed complex `G`, the functor
> `Tright G : F ↦ Tot(F ⊗ G)` on `K(Mod(O_X))` can be equipped with a functorial isomorphism
> `ξ` making it an exact functor of triangulated categories (Stacks Tag 06Y8, right version).
> This is genuinely distinct from `main_left` (the two differ by the commutativity isomorphism
> with its sign `(-1)^{pq}`).

```lean
theorem main_right (G : CochainComplex C ℤ) :
    ∃ e : (Tright G).CommShift ℤ,
      @Functor.IsTriangulated _ _ _ _ _ _ (Tright G) e _ _ _ _ _ _ _ _
```

## Tag 06Y9, a definition

[Tag 06Y9](https://stacks.math.columbia.edu/tag/06Y9) in the Stacks Project.

**`Stacks.SheafOfModules.IsKFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/Defs.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/Defs.lean#L66).

> A cochain complex `K` of sheaves of `R`-modules is **K-flat** if `Tot(F ⊗_R K)` is acyclic
> for every acyclic cochain complex `F`.

```lean
abbrev IsKFlat
    (K : CochainComplex (SheafOfModules (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ) : Prop
```

## Tag 06YA, a lemma

[Tag 06YA](https://stacks.math.columbia.edu/tag/06YA) in the Stacks Project.

**`Stacks.SheafOfModules.IsKFlat.quasiIso_le_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean#L100). The attribute's comment: “on the homotopy category, as the tag states it”.

> **[Stacks, Tag 06YA].** For a K-flat complex `K` of `𝒪`-modules, the exact functor
> `F ↦ Tot(F ⊗_𝒪 K)` of `K(Mod(𝒪))` carries quasi-isomorphisms to quasi-isomorphisms.

```lean
theorem IsKFlat.quasiIso_le_inverseImage
    (K : CochainComplex (SheafOfModules (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ)
    (hK : IsKFlat R K) :
    HomotopyCategory.quasiIso
        (SheafOfModules (Stacks.SheafOfModules.Tensor.ringSheaf R)) (ComplexShape.up ℤ) ≤
      (HomotopyCategory.quasiIso
          (SheafOfModules (Stacks.SheafOfModules.Tensor.ringSheaf R))
          (ComplexShape.up ℤ)).inverseImage
        (Stacks.SheafOfModules.Tensor.Reduction.bifunctorPhiR
          (Stacks.SheafOfModules.Tensor.sheafTensor R) K)
```

**`Stacks.SheafOfModules.IsKFlat.quasiIso_rightTensorComplex_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean#L124). The attribute's comment: “at the level of complexes rather than of the homotopy category”.

> **[Stacks, Tag 06YA] at the level of complexes.** For a K-flat complex `K` of `𝒪`-modules
> and a quasi-isomorphism `f : F₁ ⟶ F₂` of complexes of `𝒪`-modules, the induced morphism
> `Tot(F₁ ⊗_𝒪 K) ⟶ Tot(F₂ ⊗_𝒪 K)` is a quasi-isomorphism.
>
> The hypothesis is explicit rather than an instance: with the tensor-total functor applied to a
> consumer's own factorization, an instance argument is synthesized at a different spelling of the
> same type.

```lean
theorem IsKFlat.quasiIso_rightTensorComplex_map
    (K : CochainComplex (SheafOfModules (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ)
    (hK : IsKFlat R K)
    {F₁ F₂ : CochainComplex (SheafOfModules (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ}
    (f : F₁ ⟶ F₂) (hf : QuasiIso f) :
    QuasiIso ((Stacks.SheafOfModules.Tensor.rightTensorComplex R K).map f)
```

## Tag 06YB, a lemma

[Tag 06YB](https://stacks.math.columbia.edu/tag/06YB) in the Stacks Project.

**`Stacks.SheafOfModules.KFlatStalkCriterion.kFlat_iff_stalkwise`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/StalkCriterion.lean, line 567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/StalkCriterion.lean#L567).

> **Stacks 06YB.** A complex of sheaves of modules on a ringed space is K-flat if and only if
> its complex of stalks at every point is K-flat over the stalk of the structure sheaf.

```lean
theorem kFlat_iff_stalkwise
    (K : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} R)) ℤ)
      :
    letI := fun (left : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf R)) =>
      Stacks.SheafOfModules.Tensor.sheafTensor_obj_additive.{u, u, u, u, u} R left
    letI : ∀ (left right : CochainComplex
        (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ),
        HomologicalComplex.HasMapBifunctor left right
          (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} R) (ComplexShape.up ℤ) :=
      fun left right => Stacks.SheafOfModules.Tensor.hasMapBifunctor_sheafTensor R left right
    Stacks.SheafOfModules.KFlat.KFlat.{u, u, u} R K ↔ KFlatStalkwise R K
```

## Tag 079R, a lemma

[Tag 079R](https://stacks.math.columbia.edu/tag/079R) in the Stacks Project.

**`Stacks.SheafOfModules.kFlat_tensorComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/TensorProduct.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/TensorProduct.lean#L513).

> **Stacks 079R.** The total tensor product of two K-flat complexes of sheaves of modules is
> K-flat.

```lean
theorem kFlat_tensorComplex
    {K L : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ}
    (hK : Stacks.SheafOfModules.IsKFlat R K) (hL : Stacks.SheafOfModules.IsKFlat R L) :
    Stacks.SheafOfModules.IsKFlat R (((Stacks.SheafOfModules.Tensor.tensorComplex R).obj K).obj L)
```

## Tag 079S, a lemma

[Tag 079S](https://stacks.math.columbia.edu/tag/079S) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.SheafOfModules.kFlat_of_second_third`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/DistinguishedTriangles.lean#L79), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/TwoOutOfThree.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/TwoOutOfThree.lean#L52) (StacksFrontier): “ringed space case of the ringed site statement, first vertex”.
- [`Stacks.SheafOfModules.kFlat_of_first_third`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/DistinguishedTriangles.lean#L97), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/TwoOutOfThree.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/TwoOutOfThree.lean#L55) (StacksFrontier): “ringed space case of the ringed site statement, second vertex”.
- [`Stacks.SheafOfModules.kFlat_of_first_second`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/DistinguishedTriangles.lean#L115), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/TwoOutOfThree.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/TwoOutOfThree.lean#L58) (StacksFrontier): “ringed space case of the ringed site statement, third vertex”.

## Tag 0G6U, a lemma

[Tag 0G6U](https://stacks.math.columbia.edu/tag/0G6U) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.SheafOfModules.isKFlat_two_out_of_three`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TwoOutOfThree.lean#L337), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/TwoOutOfThree.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/TwoOutOfThree.lean#L61) (StacksFrontier): “ringed space case of the ringed site statement”.

## Tag 06YC, a lemma

[Tag 06YC](https://stacks.math.columbia.edu/tag/06YC) in the Stacks Project.

**`Stacks.SheafOfModules.KFlatPullback.kFlat_pullback_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/PullbackFromTheStalkCriterion.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/PullbackFromTheStalkCriterion.lean#L61).

> **Stacks 06YC.** The degreewise pullback of a K-flat complex of `𝒪_Y`-modules along
> a morphism of ringed spaces is a K-flat complex of `𝒪_X`-modules.

```lean
theorem kFlat_pullback_unconditional {X Y : AlgebraicGeometry.RingedSpace.{u, u}} (f : X ⟶ Y)
    (K : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.sheaf)) ℤ)
    (hK : Stacks.SheafOfModules.IsKFlat Y.sheaf K) :
    Stacks.SheafOfModules.IsKFlat X.sheaf
      (((RingedSpaceModuleAdjunction.modulePullback f).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj K)
```

## Tag 06YD, a lemma

[Tag 06YD](https://stacks.math.columbia.edu/tag/06YD) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.SheafOfModules.kFlat_of_boundedAbove_of_flat`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/BoundedAboveFlatComplexes.lean#L328), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/BoundedAboveFlatComplexes.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/BoundedAboveFlatComplexes.lean#L46) (StacksFrontier): “ringed space case of the ringed site statement”.

## Tag 06YE, a lemma

[Tag 06YE](https://stacks.math.columbia.edu/tag/06YE) in the Stacks Project.

**`Stacks.SheafOfModules.kFlat_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/SequentialColimits.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/SequentialColimits.lean#L85).

> A sequential colimit of K-flat complexes of sheaves of modules is K-flat.

```lean
theorem kFlat_colimit
    (K : ℕ ⥤ CochainComplex (SheafOfModules (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ)
    (hK : ∀ n : ℕ, IsKFlat R (K.obj n)) :
    IsKFlat R (colimit K)
```

## Tag 079T, a lemma

[Tag 079T](https://stacks.math.columbia.edu/tag/079T) in the Stacks Project.

**`Stacks.Cohomology.SpaceResolutionByExtensionsByZero.exists_resolutionByDirectSumsExtensionsByZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RecoveryA/SpaceResolutionByExtensionsByZero.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RecoveryA/SpaceResolutionByExtensionsByZero.lean#L354).

> Every cochain complex `G` of `O`-modules on a ringed space admits a compatible system of
> bounded-above resolutions of its canonical truncations `τ_{≤ n+1} G` whose terms and successive
> cokernels are direct sums of extensions by zero `j_{U!} O_U`, and whose colimit maps
> quasi-isomorphically to `G`.

```lean
theorem exists_resolutionByDirectSumsExtensionsByZero
    (G : CochainComplex (SheafOfModules.{u} O) ℤ) :
    Nonempty (ResolutionByDirectSumsExtensionsByZero O G)
```

## Tag 06YF, a lemma

[Tag 06YF](https://stacks.math.columbia.edu/tag/06YF) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.exists_isKFlat_isFlat_quasiIso_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RingedSpace/FlatKFlatResolution.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RingedSpace/FlatKFlatResolution.lean#L64).

> **Stacks 06YF.** Every cochain complex `G` of `𝒪_X`-modules on a ringed space receives a
> termwise surjective quasi-isomorphism from a K-flat complex whose terms are flat `𝒪_X`-modules.
>
> A ringed space is a ringed site, and this is the resolution built there
> ([Stacks, Tag 06YS]).

```lean
public theorem exists_isKFlat_isFlat_quasiIso_epi
    (G : CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ) :
    ∃ (K : CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ)
      (s : K ⟶ G),
      Stacks.SheafOfModules.IsKFlat X.sheaf K ∧
      (∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.sheaf) (K.X i)) ∧
      QuasiIso s ∧ ∀ i : ℤ, Epi (s.f i)
```

## Tag 06YG, a lemma

[Tag 06YG](https://stacks.math.columbia.edu/tag/06YG) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.SheafOfModules.quasiIso_mapBifunctorMap_id_of_kFlat_right`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionIndependence.lean#L87), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/QuasiIsoOfKFlatComplexes.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/QuasiIsoOfKFlatComplexes.lean#L45) (StacksFrontier): “ringed space case of the ringed site statement”.
- [`Stacks.SheafOfModules.quasiIso_tensorComplex_obj_map_of_kFlat`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionIndependence.lean#L130), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/QuasiIsoOfKFlatComplexes.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/QuasiIsoOfKFlatComplexes.lean#L48) (StacksFrontier): “ringed space case, tensorComplex spelling”.

## Tag 06YH, a definition

[Tag 06YH](https://stacks.math.columbia.edu/tag/06YH) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.Cohomology.TorAmplitude.derTensor`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/TorAmplitude/OnARingedSpace.lean#L103), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedTensor/OnARingedSpace.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedTensor/OnARingedSpace.lean#L40) (StacksFrontier): “the derived tensor product on a ringed space, with its exactness”.

## Tag 08BP, a definition

[Tag 08BP](https://stacks.math.columbia.edu/tag/08BP) in the Stacks Project.

**`Stacks.Cohomology.tor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedTensor/Tor.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedTensor/Tor.lean#L83). References: SGA 4½ Etat 0 (6.2), “Tor\_i, ringed space”; SGA 4 XVII (4.1.8), “modules, not complexes”.

> **Tag 08BP.** The `O_X`-module `Tor_p^{O_X}(F, G) = H^{-p}(F ⊗_{O_X}^{L} G)`.

```lean
def tor (p : ℤ) (F G : OXMod.{u} X) : OXMod.{u} X
```

## Tag 08BQ, a lemma

[Tag 08BQ](https://stacks.math.columbia.edu/tag/08BQ) in the Stacks Project.

**`Stacks.Cohomology.flat_iff_forall_isZero_tor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedTensor/TorFlatness.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedTensor/TorFlatness.lean#L373). The attribute's comment: “(1) ⟺ (2) for a ringed space, with clause (2) stated in the source's own terms: the vanishing of the sheaf Tor\_1^\{O\_X}(F, G) = H^\{-1}(F ⊗^L\_\{O\_X} G) of Tag 08BP, for every O\_X-module G, and clause (1) sheaf-level flatness of Tag 05ND.”.

> **Tag 08BQ: Tor measures the deviation of flatness.** Let `(X, 𝒪_X)` be a ringed space and
> `ℱ` an `𝒪_X`-module. The following are equivalent:
>
> 1. `ℱ` is a flat `𝒪_X`-module, and
> 2. `Tor_1^{𝒪_X}(ℱ, 𝒢) = 0` for every `𝒪_X`-module `𝒢`.
>
> Clause (1) is `OXModule.Flat`, Definition Tag 05ND: the genuine sheaf tensor endofunctor
> `- ⊗_{𝒪_X} ℱ` preserves monomorphisms, hence is exact. Clause (2) is the source's own `Tor_1`,
> the sheaf `Stacks.Cohomology.tor X 1 ℱ 𝒢` of Tag 08BP, which is `H^{-1}(ℱ ⊗^{L}_{𝒪_X} 𝒢)` —
> not a stalkwise substitute for it.
>
> *Proof.* Tag 05NE (`OXModule.flat_iff_flat_stalk`) replaces clause (1) by flatness of every
> stalk, and `AlgebraicGeometry.SheafOfModules.flat_stalk_ringCat_iff_commRingCat` reads that over
> the stalk ring the derived tensor product is formed relative to. Over that ring
> `OXModule.module_flat_iff_tor1` turns flatness of a stalk into the vanishing of the
> module-theoretic `Tor_1` against every module over it, every such module being a stalk by
> `AlgebraicGeometry.SheafOfModules.stalkFunctor_essSurj`; and
> `isZero_derivedTensorHomology_iff_forall_isZero_tor` turns the vanishing of those stalkwise
> `Tor_1` into the vanishing of the sheaf `Tor_1`, which is clause (2).
>
> No intermediate statement of stalkwise flatness over the `RingCat`-valued stalk ring is written
> down, and that is deliberate: writing `Module.Flat Λ M` for that ring forces the `Semiring Λ`
> inside the `Module` instance to be the one derived from
> `StacksDraft.StalkTensor.commRing_stalk`, while the `ModuleCat Λ` that `M` lives in carries the
> one derived from `RingCat`'s own `Ring`. The two are definitionally equal but not syntactically,
> so instance synthesis fails on the resulting `Module Λ M` goal. Going through
> `OXModule.module_flat_iff_tor1`, whose `ModuleCat` is formed from its own `CommRing` binder,
> keeps the instances internally consistent.

```lean
theorem flat_iff_forall_isZero_tor (F : OXMod.{u, u} X) :
    OXModule.Flat F ↔ ∀ G : OXMod.{u, u} X, IsZero (tor X 1 F G)
```

**`OXModule.flat_iff_tor1_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/FlatModuleSheavesAndStalks/FlatIffTorOne.lean, line 506](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/FlatModuleSheavesAndStalks/FlatIffTorOne.lean#L506). The attribute's comment: “(1) ⟺ (2) with clause (2) read stalkwise: Tor\_1 here is the module-theoretic Tor\_1^\{O\_\{X,x}}(F\_x, G\_x) at every point, not the sheaf Tor\_1 of Tag 08BP. The tag's clause (2) in the source's own terms — the vanishing of Stacks.Cohomology.tor X 1 F G — is Stacks.Cohomology.flat\_iff\_forall\_isZero\_tor in StacksFrontier/Topology/Sheaves/Cohomology/DerivedTensor/TorFlatness.lean, and the two readings are identified there by isZero\_derivedTensorHomology\_iff\_forall\_isZero\_tor.”. References: SGA 6 I (5.1.1), “special case”.

> **Theorem (Stacks Tag 08BQ — "Tor measures the deviation of flatness").**
> Let `(X, O_X)` be a ringed space and `F` an `O_X`-module.  Then `F` is flat
> (Definition 2: the genuine tensor endofunctor `- ⊗_{O_X} F` is exact) if and
> only if `Tor_1^{O_X}(F, G)` is the zero `O_X`-module for every `O_X`-module
> `G`.
>
> The tensor product (Definition 1) is formalized directly as the sheafification
> of the presheaf tensor product, and `Flat` is the genuine sheaf-level exactness
> of this tensor, so the left-hand side is the source's own notion (Tag 05ND).
>
> The right-hand side is the **stalk-level** reading: `Tor1IsZero F G` says that
> the classical module-theoretic `Tor_1^{O_{X,x}}(F_x, G_x)` vanishes at every
> `x`.  It is not the expression `Stacks.Cohomology.tor X 1 F G` (Tag 08BP), the
> genuine `H^{-1}(F ⊗^{L}_{O_X} G)`, which is what the tag's clause (2) is about;
> and `tor1IsZero_iff_stalk` is `Iff.rfl`, so it supplies no part of the
> comparison.
>
> The two readings are nevertheless **the same statement**, and that is now a
> theorem rather than a gap: `Stacks.Cohomology.flat_iff_forall_isZero_tor` in
> `StacksFrontier/Topology/Sheaves/Cohomology/DerivedTensor/TorFlatness.lean` states
> Tag 08BQ with clause (2) in the source's own terms, and
> `Stacks.SheafOfModules.DerivedTensorStalk.isZero_derivedTensorHomology_iff_forall_isZero_tor`
> there is the identification itself: the sheaf `Tor_p` of Tag 08BP vanishes
> exactly when the stalkwise module-theoretic `Tor_p` vanishes at every point.
> Its four ingredients are
> `AlgebraicGeometry.SheafOfModules.isZero_iff_forall_isZero_stalkFunctor_obj`
> (vanishing is stalkwise, Tag 01AG),
> `CategoryTheory.Functor.mapDerivedCategoryHomologyIso` (the exact stalk functor
> commutes with `H^{-1}`),
> `Stacks.SheafOfModules.DerivedTensorStalk.derivedTensorStalkIso` (the derived
> form of Tag 01CB) — all three of which already existed — and
> `Stacks.DerivedTensor.homologyIsoTor`
> (`StacksFrontier/Homology/Tor/DerivedTensorTor.lean`), the identification of
> `H^{-p}` of a derived tensor product of two modules over a commutative ring
> with their `Tor_p`, which is the one that had to be supplied.
>
> So this declaration is the stalk-level half of the tag, kept because the rest of
> this file is written in the stalkwise vocabulary; the tag's own statement is the
> one in `StacksFrontier/Topology/Sheaves/Cohomology/DerivedTensor/TorFlatness.lean`.
>
> *Proof.*  By `flat_iff_flat_stalk` (Tag 05NE) sheaf flatness is equivalent to
> stalk-wise flatness `F.FlatStalkwise`, and by `flatStalkwise_iff_forall_tor1`
> the latter is equivalent to the vanishing of all stalk-wise `Tor₁`.

```lean
theorem flat_iff_tor1_eq_zero (F : OXModule X) :
    F.Flat ↔ ∀ G : OXModule X, F.Tor1IsZero G
```

## Tag 0G6V, a lemma

[Tag 0G6V](https://stacks.math.columbia.edu/tag/0G6V) in the Stacks Project.

**`Stacks.SheafOfModules.exists_isKFlat_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/Factorization.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/Factorization.lean#L117). The attribute's comment: “the K-flat factorization”.

> **Tag 0G6V.** A map `a : K^• ⟶ L^•` of complexes of `O`-modules with `K^•` K-flat factors,
> up to homotopy, through a K-flat complex `N^•` which maps to `L^•` by a quasi-isomorphism.

```lean
theorem exists_isKFlat_factorization
    {K L : CochainComplex
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.O)) ℤ}
    (a : K ⟶ L) (hK : IsKFlat X.O K) :
    ∃ (N : CochainComplex
        (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.O)) ℤ)
      (b : K ⟶ N) (c : N ⟶ L),
      IsKFlat X.O N ∧ QuasiIso c ∧ Nonempty (Homotopy a (b ≫ c))
```

**`Stacks.SheafOfModules.exists_isKFlat_isFlat_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/Factorization.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/Factorization.lean#L132). The attribute's comment: “the factorization with flat terms”.

> **Tag 0G6V, second half.** If in addition the terms of `K^•` are flat `O`-modules, then the
> intermediate complex of the factorization can be chosen with flat terms as well.

```lean
theorem exists_isKFlat_isFlat_factorization
    {K L : CochainComplex
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.O)) ℤ}
    (a : K ⟶ L) (hK : IsKFlat X.O K)
    (hKflat : ∀ i : ℤ,
      AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.O) (K.X i)) :
    ∃ (N : CochainComplex
        (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.O)) ℤ)
      (b : K ⟶ N) (c : N ⟶ L),
      IsKFlat X.O N ∧
        (∀ i : ℤ,
          AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.O) (N.X i)) ∧
        QuasiIso c ∧ Nonempty (Homotopy a (b ≫ c))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.26, Tag 06Y7](https://stacks.math.columbia.edu/tag/06Y7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
