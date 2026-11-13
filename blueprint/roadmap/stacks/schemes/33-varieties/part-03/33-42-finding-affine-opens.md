---
declaration: section
origin: cited
lean: AlgebraicGeometry.isOpenImmersion_of_openCover_source_of_separated_of_genericPoints_injOn, AlgebraicGeometry.exists_isOpenImmersion_res_of_isIso_stalkMap, AlgebraicGeometry.exists_isAffineOpen_containing_image_of_genericPoints_injOn, AlgebraicGeometry.exists_isAffineOpen_containing_of_stalk_krullDimLE_one, Ideal.exists_lift_avoiding_primes, AlgebraicGeometry.exists_isAffineOpen_containing_of_components, AlgebraicGeometry.exists_isAffineOpen_containing_of_stalk_krullDimLE_one_of_finite_components
statement: formalized
proof: formalized
---

# 33.42 Finding affine opens

Section 33.42 of the Stacks Project, [Tag 09NF](https://stacks.math.columbia.edu/tag/09NF). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09NG, a lemma

[Tag 09NG](https://stacks.math.columbia.edu/tag/09NG) in the Stacks Project.

**`AlgebraicGeometry.isOpenImmersion_of_openCover_source_of_separated_of_genericPoints_injOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/FindingAffineOpens/OpenImmersionCriterion.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/FindingAffineOpens/OpenImmersionCriterion.lean#L189).

> **Stacks Project, Tag 09NG.** A separated morphism that is locally an open immersion on
> the source and injective on generic points of irreducible components is an open immersion.

```lean
public theorem isOpenImmersion_of_openCover_source_of_separated_of_genericPoints_injOn
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsSeparated f] (𝒰 : X.OpenCover)
    (h𝒰 : ∀ i, IsOpenImmersion (𝒰.f i ≫ f))
    (hinj : Set.InjOn f (genericPoints X)) :
    IsOpenImmersion f
```

## Tag 09NH, a lemma

[Tag 09NH](https://stacks.math.columbia.edu/tag/09NH) in the Stacks Project.

**`AlgebraicGeometry.exists_isOpenImmersion_res_of_isIso_stalkMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/FindingAffineOpens/LocalIsomorphism.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/FindingAffineOpens/LocalIsomorphism.lean#L81).

> **Stacks Project, Tag 09NH.** If the local-ring map of a locally finite-type morphism
> is an isomorphism at `x`, and the target is reduced with finitely many irreducible
> components, then the morphism is an open immersion near `x`.

```lean
public theorem exists_isOpenImmersion_res_of_isIso_stalkMap
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X)
    [IsReduced S] [LocallyOfFiniteType f]
    (hcomponents : (irreducibleComponents S).Finite)
    (hstalk : IsIso (f.stalkMap x)) :
    ∃ U : X.Opens, x ∈ U ∧ IsOpenImmersion (U.ι ≫ f)
```

## Tag 09NI, a lemma

[Tag 09NI](https://stacks.math.columbia.edu/tag/09NI) in the Stacks Project.

**`AlgebraicGeometry.exists_isAffineOpen_containing_image_of_genericPoints_injOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/FindingAffineOpens/CommonAffineOpenOfStalks.lean, line 420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/FindingAffineOpens/CommonAffineOpenOfStalks.lean#L420).

> **[Stacks, Tag 09NI].** Let `f : T ⟶ X` be a morphism of schemes with `T` affine and `X`
> quasi-separated with finitely many generic points. If `f` carries the generic points of the
> irreducible components of `T` into those of `X` and does so injectively, and if the canonical
> map of local rings at each member of a finite family of points of `T` is an isomorphism, then
> the images of that family lie in a common affine open of `X`.

```lean
public theorem exists_isAffineOpen_containing_image_of_genericPoints_injOn
    {T X : Scheme.{u}} (f : T ⟶ X) [IsAffine T] [QuasiSeparatedSpace X]
    (hX : (genericPoints X).Finite)
    (hgeneric : Set.MapsTo f (genericPoints T) (genericPoints X))
    (hinj : Set.InjOn f (genericPoints T))
    {ι : Type v} [Finite ι] (t : ι → T)
    (hstalk : ∀ i, IsIso (f.stalkMap (t i))) :
    ∃ U : X.Opens, IsAffineOpen U ∧ ∀ i, f (t i) ∈ U
```

## Tag 09NJ, a lemma

[Tag 09NJ](https://stacks.math.columbia.edu/tag/09NJ) in the Stacks Project.

**`AlgebraicGeometry.exists_isAffineOpen_containing_of_stalk_krullDimLE_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/FindingAffineOpens/CommonAffineOpenOfDimensionOnePoints.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/FindingAffineOpens/CommonAffineOpenOfDimensionOnePoints.lean#L179).

> **[Stacks, Tag 09NJ]** A finite family of points on an integral separated scheme,
> whose local rings are Noetherian of Krull dimension at most one, lies in a common affine open.

```lean
theorem exists_isAffineOpen_containing_of_stalk_krullDimLE_one
    (X : Scheme.{u}) [IsIntegral X] [X.IsSeparated]
    {ι : Type v} [Finite ι] (x : ι → X)
    (h_noetherian : ∀ i, IsNoetherianRing (X.presheaf.stalk (x i)))
    (h_dimension : ∀ i, Ring.KrullDimLE 1 (X.presheaf.stalk (x i))) :
    ∃ U : X.Opens, IsAffineOpen U ∧ ∀ i, x i ∈ U
```

## Tag 09NK, a lemma

[Tag 09NK](https://stacks.math.columbia.edu/tag/09NK) in the Stacks Project.

**`Ideal.exists_lift_avoiding_primes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/AvoidingPrimes.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Defs/AvoidingPrimes.lean#L33).

> If an ideal is contained in none of a finite family of prime ideals, every
> class modulo that ideal has a representative outside all of the primes.

```lean
public theorem exists_lift_avoiding_primes
    {A : Type u} [CommRing A] (I : Ideal A) {r : ℕ} (p : Fin r → Ideal A)
    (hp : ∀ i, (p i).IsPrime) (hI : ∀ i, ¬ I ≤ p i) (fbar : A ⧸ I) :
    ∃ f : A, (∀ i, f ∉ p i) ∧ Ideal.Quotient.mk I f = fbar
```

## Tag 09NM, a lemma

[Tag 09NM](https://stacks.math.columbia.edu/tag/09NM) in the Stacks Project.

**`AlgebraicGeometry.exists_isAffineOpen_containing_of_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/FindingAffineOpens/CommonAffineOpenOfComponents.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/FindingAffineOpens/CommonAffineOpenOfComponents.lean#L471).

> **[Stacks, Tag 09NM].** Let `X` be a scheme with finitely many irreducible components and
> `T ⊆ X` a finite set of points. If for every irreducible component `Z` the set `T ∩ Z` is
> contained in an affine open of the reduced induced closed subscheme on `Z`, then `T` is
> contained in an affine open subscheme of `X`.

```lean
public theorem exists_isAffineOpen_containing_of_components
    (X : Scheme.{u}) {T : Set X} (hT : T.Finite)
    (hcomponents : (irreducibleComponents X).Finite)
    (hlocal : ∀ Z : Closeds X, (Z : Set X) ∈ irreducibleComponents X →
      ∃ U : (Scheme.IdealSheafData.vanishingIdeal Z).subscheme.Opens,
        IsAffineOpen U ∧
          T ∩ (Z : Set X) ⊆
            Set.range (U.ι ≫ (Scheme.IdealSheafData.vanishingIdeal Z).subschemeι)) :
    ∃ U : X.Opens, IsAffineOpen U ∧ T ⊆ U
```

## Tag 09NN, a proposition

[Tag 09NN](https://stacks.math.columbia.edu/tag/09NN) in the Stacks Project.

**`AlgebraicGeometry.exists_isAffineOpen_containing_of_stalk_krullDimLE_one_of_finite_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/FindingAffineOpens/CommonAffineOpenOfDimensionOnePointsFiniteComponents.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/FindingAffineOpens/CommonAffineOpenOfDimensionOnePointsFiniteComponents.lean#L80).

> **[Stacks, Tag 09NN]** Let `X` be a separated scheme such that every quasi-compact open of
> `X` has finitely many irreducible components. A finite family of points of `X` whose local rings
> are Noetherian of Krull dimension at most one is contained in an affine open subscheme of `X`.

```lean
theorem exists_isAffineOpen_containing_of_stalk_krullDimLE_one_of_finite_components
    (X : Scheme.{u}) [X.IsSeparated]
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    {ι : Type v} [Finite ι] (x : ι → X)
    (h_noetherian : ∀ i, IsNoetherianRing (X.presheaf.stalk (x i)))
    (h_dimension : ∀ i, Ring.KrullDimLE 1 (X.presheaf.stalk (x i))) :
    ∃ U : X.Opens, IsAffineOpen U ∧ ∀ i, x i ∈ U
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.42, Tag 09NF](https://stacks.math.columbia.edu/tag/09NF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
