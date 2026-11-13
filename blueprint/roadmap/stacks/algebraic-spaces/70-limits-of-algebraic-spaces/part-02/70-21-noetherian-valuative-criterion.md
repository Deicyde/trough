---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_discreteValuationSpecialization, AlgebraicGeometry.Space.ValuativeSquare, AlgebraicGeometry.Space.ValuativeSquare.Lift, AlgebraicGeometry.Space.discreteUniqueness_of_uniqueness, AlgebraicGeometry.Space.codimensionZeroUniqueness_of_discreteUniqueness, AlgebraicGeometry.Space.discreteUniqueness_of_isSeparated, AlgebraicGeometry.Space.codimensionZeroUniqueness_of_isSeparated, AlgebraicGeometry.Space.isSeparated_iff_valuativeCriterion_uniqueness
statement: formalized
proof: formalized
---

# 70.21 Noetherian valuative criterion

Section 70.21 of the Stacks Project, [Tag 0CMB](https://stacks.math.columbia.edu/tag/0CMB). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CMC, a lemma

[Tag 0CMC](https://stacks.math.columbia.edu/tag/0CMC) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_discreteValuationSpecialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeCriterion.lean, line 614](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeCriterion.lean#L614). The attribute's comment: “corrected: the residue-field clause is asserted when f x ≠ y; as printed it is false (the identity of Spec of an algebraically closed field), see errata.md”.

> **Stacks 0CMC.** Let `f : X ⟶ Y` be a morphism of finite type of algebraic spaces over `S`,
> with `Y` locally Noetherian, and let `y` be a point of `Y` in the closure of the image of the
> points of `X`. Then there are a discrete valuation ring `A`, a field-valued point of `X` over its
> fraction field `K`, a morphism `Spec K ⟶ Spec A` over `S` given by the inclusion `A → K`, and an
> `A`-valued point of `Y` forming a commutative square with `f`, the closed point of `Spec A`
> mapping to `y`. Moreover the point `x` of `X` given by `Spec K ⟶ X` is a codimension zero point;
> it satisfies `f x ≠ y` as soon as `y` is in the closure of the set of `f x'` for the codimension
> zero points `x'` of `X` with `f x' ≠ y`; and, when `f x ≠ y`, the morphism `Spec K ⟶ X` factors
> as `Spec K ≅ Spec κ(u) ⟶ U ⟶ X` for a point `u` of a scheme `U` étale over `X`, so that `K` is
> the residue field of `u`. The condition for `f x ≠ y` is also necessary: the square makes `y` a
> specialization of `f x`, so an `x` with `f x ≠ y` is itself such an `x'`.
>
> The residue-field clause is stated under `f x ≠ y` because the source's unconditional clause is
> false. This is
> `AlgebraicGeometry.Space.not_forall_exists_discreteValuationSpecialization_residueField`
> (in `StacksFrontier.AlgebraicGeometry.Spaces.NoetherianValuativeCriterionCounterexample`), whose
> statement is the conclusion of this theorem with the guard `f x ≠ y →` removed from the
> residue-field clause and the clause guaranteeing `f x ≠ y` left out (leaving it out weakens the
> refuted statement, so the refutation is the stronger one):
> ```
> ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
>     (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : X ⟶ Y), IsAlgebraicSpace B S hS X →
>     IsAlgebraicSpace B S hS Y → IsFiniteType B S hS f →
>     HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) →
>     ∀ y : points B S hS Y, y ∈ closure (Set.range (pointsMap B S hS X f)) →
>       ∃ (A : Type u) (_ : CommRing A) (_ : IsDomain A) (_ : IsDiscreteValuationRing A)
>         (K : FieldValuedPoint B S hS X) (_ : Algebra A K.carrier)
>         (_ : IsFractionRing A K.carrier) (A_contained : B.Contains (Spec (.of A)))
>         (s : Spec (.of A) ⟶ S) (j : K.siteObject ⟶ valuationObject B S hS A A_contained s)
>         (g : yoneda.obj (valuationObject B S hS A A_contained s) ⟶ Y),
>         j.left.1 = Scheme.Spec.map (CommRingCat.ofHom (algebraMap A K.carrier)).op ∧
>         yoneda.map j ≫ g = yonedaEquiv.symm K.value ≫ f ∧
>         pointsMap B S hS (yoneda.obj (valuationObject B S hS A A_contained s)) g
>             ((schemePointRepresentative B S hS (valuationObject B S hS A A_contained s)
>                 (⟨IsLocalRing.maximalIdeal A, inferInstance⟩ : PrimeSpectrum A)).class B S hS
>               (yoneda.obj (valuationObject B S hS A A_contained s))) = y ∧
>         localRingDimension B S hS (K.class B S hS X) = 0 ∧
>         ∃ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X)
>           (u : (BigFppfOver.toScheme B S hS).obj U)
>           (e : K.carrier ≃+* ((BigFppfOver.toScheme B S hS).obj U).residueField u)
>           (t : K.siteObject ⟶ U),
>           IsEtale B S hS a ∧
>             t.left.1 = Scheme.Spec.map (CommRingCat.ofHom e.symm.toRingHom).op ≫
>                 ((BigFppfOver.toScheme B S hS).obj U).fromSpecResidueField u ∧
>               a.app (Opposite.op K.siteObject) t = K.value
> ```
> The witness is the identity of `X = Y = S = Spec k` for `k` the algebraic closure of `ℚ`: every
> residue field of a scheme étale over `Spec k` is algebraically closed, being a separable
> extension of `k`, while the fraction field of a discrete valuation ring is not, since a
> uniformizer has no square root in it. The same proof gives the stronger
> `AlgebraicGeometry.Space.not_forall_exists_etale_residueFieldEquiv`, in which `K` is only asked
> to be abstractly isomorphic to such a residue field.
>
> This theorem is therefore the corrected form of Stacks 0CMC, recorded in `errata.md`. The fault
> is inherited from the scheme case, Stacks 0CM2, to which the source's proof reduces: its proof
> applies Stacks 00PH to the image `R` of the local ring at `y` in the residue field at the chosen
> generic point, and 00PH needs `R` not to be a field, which is the case exactly when that generic
> point does not lie over `y`. The guard `f x ≠ y` suffices for the residue-field clause but is not
> necessary: for the affine line over a field `k` mapping to `Spec k`, the generic point lies over
> the only point `y`, and its residue field `k(t)` is the fraction field of `k[t]` localized at
> `(t)`, a discrete valuation ring over `k`.

```lean
theorem exists_discreteValuationSpecialization {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (X_isAlgebraicSpace : IsAlgebraicSpace B S hS X)
    (Y_isAlgebraicSpace : IsAlgebraicSpace B S hS Y) (f_finiteType : IsFiniteType B S hS f)
    (Y_locallyNoetherian :
      HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (y : points B S hS Y) (y_mem_closure : y ∈ closure (Set.range (pointsMap B S hS X f))) :
    ∃ (A : Type u) (_ : CommRing A) (_ : IsDomain A) (_ : IsDiscreteValuationRing A)
      (K : FieldValuedPoint B S hS X) (_ : Algebra A K.carrier) (_ : IsFractionRing A K.carrier)
      (A_contained : B.Contains (Spec (.of A))) (s : Spec (.of A) ⟶ S)
      (j : K.siteObject ⟶ valuationObject B S hS A A_contained s)
      (g : yoneda.obj (valuationObject B S hS A A_contained s) ⟶ Y),
      j.left.1 = Scheme.Spec.map (CommRingCat.ofHom (algebraMap A K.carrier)).op ∧
      yoneda.map j ≫ g = yonedaEquiv.symm K.value ≫ f ∧
      pointsMap B S hS (yoneda.obj (valuationObject B S hS A A_contained s)) g
          ((schemePointRepresentative B S hS (valuationObject B S hS A A_contained s)
              (⟨IsLocalRing.maximalIdeal A, inferInstance⟩ : PrimeSpectrum A)).class B S hS
            (yoneda.obj (valuationObject B S hS A A_contained s))) = y ∧
      localRingDimension B S hS (K.class B S hS X) = 0 ∧
      (y ∈ closure (pointsMap B S hS X f ''
          {x' | localRingDimension B S hS x' = 0 ∧ pointsMap B S hS X f x' ≠ y}) →
        pointsMap B S hS X f (K.class B S hS X) ≠ y) ∧
      (pointsMap B S hS X f (K.class B S hS X) ≠ y →
        ∃ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X)
          (u : (BigFppfOver.toScheme B S hS).obj U)
          (e : K.carrier ≃+* ((BigFppfOver.toScheme B S hS).obj U).residueField u)
          (t : K.siteObject ⟶ U),
          IsEtale B S hS a ∧
            t.left.1 = Scheme.Spec.map (CommRingCat.ofHom e.symm.toRingHom).op ≫
                ((BigFppfOver.toScheme B S hS).obj U).fromSpecResidueField u ∧
              a.app (Opposite.op K.siteObject) t = K.value)
```

## Tag 0H1V, an equation

[Tag 0H1V](https://stacks.math.columbia.edu/tag/0H1V) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.ValuativeSquare`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Criterion.lean#L70), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Criterion.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Criterion.lean#L201) (StacksFrontier): “solid square”.
- [`AlgebraicGeometry.Space.ValuativeSquare.Lift`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Criterion.lean#L106), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Criterion.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Criterion.lean#L202) (StacksFrontier): “dotted arrow”.

## Tag 0H1W, a lemma

[Tag 0H1W](https://stacks.math.columbia.edu/tag/0H1W) in the Stacks Project.

**`AlgebraicGeometry.Space.discreteUniqueness_of_uniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparatedness.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparatedness.lean#L132). The attribute's comment: “(2) implies (3)”.

> **Stacks 0H1W, (2) implies (3).** Testing uniqueness of dotted arrows on all valuation
> rings is stronger than testing it on the discrete ones.

```lean
theorem discreteUniqueness_of_uniqueness {f : X ⟶ Y}
    (hu : ValuativeCriterion.Uniqueness f) : ValuativeCriterion.DiscreteUniqueness f
```

**`AlgebraicGeometry.Space.codimensionZeroUniqueness_of_discreteUniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparatedness.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparatedness.lean#L140). The attribute's comment: “(3) implies (4)”.

> **Stacks 0H1W, (3) implies (4).** Testing uniqueness of dotted arrows on all discrete
> valuation rings is stronger than testing it only on the diagrams whose generic arrow picks out
> a point of codimension zero.

```lean
theorem codimensionZeroUniqueness_of_discreteUniqueness {f : X ⟶ Y}
    (hu : ValuativeCriterion.DiscreteUniqueness f) :
    ValuativeCriterion.CodimensionZeroUniqueness f
```

**`AlgebraicGeometry.Space.discreteUniqueness_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparatedness.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparatedness.lean#L148). The attribute's comment: “(1) implies (3)”.

> **Stacks 0H1W, (1) implies (3).** A separated morphism of algebraic spaces has at most one
> dotted arrow in every valuative diagram with a discrete valuation ring.

```lean
theorem discreteUniqueness_of_isSeparated (f : X ⟶ Y) (hf : IsSeparated B S hS f) :
    ValuativeCriterion.DiscreteUniqueness f
```

**`AlgebraicGeometry.Space.codimensionZeroUniqueness_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparatedness.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparatedness.lean#L156). The attribute's comment: “(1) implies (4)”.

> **Stacks 0H1W, (1) implies (4).** A separated morphism of algebraic spaces has at most one
> dotted arrow in every valuative diagram with a discrete valuation ring whose generic arrow
> picks out a point of codimension zero.

```lean
theorem codimensionZeroUniqueness_of_isSeparated (f : X ⟶ Y) (hf : IsSeparated B S hS f) :
    ValuativeCriterion.CodimensionZeroUniqueness f
```

**`AlgebraicGeometry.Space.isSeparated_iff_valuativeCriterion_uniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparatedness.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparatedness.lean#L163). The attribute's comment: “(1) is equivalent to (2)”.

> **Stacks 0H1W, (1) is equivalent to (2).** A quasi-separated morphism of algebraic spaces
> is separated exactly when it satisfies the uniqueness part of the valuative criterion.

```lean
theorem isSeparated_iff_valuativeCriterion_uniqueness
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hqs : IsQuasiSeparated B S hS f) :
    IsSeparated B S hS f ↔ ValuativeCriterion.Uniqueness f
```

**`AlgebraicGeometry.Space.isSeparated_tfae_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparatednessTFAE.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparatednessTFAE.lean#L78).

> **Stacks 0H1W.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> quasi-separated and locally of finite type, with `Y` locally Noetherian. The following are
> equivalent:
>
> 1. `f` is separated;
> 2. every valuative diagram for `f` has at most one dotted arrow;
> 3. every valuative diagram for `f` whose valuation ring is a discrete valuation ring has at most
>    one dotted arrow;
> 4. every valuative diagram for `f` whose valuation ring is a discrete valuation ring and whose
>    generic arrow picks out a point of codimension zero of `X` has at most one dotted arrow.

```lean
theorem isSeparated_tfae_of_isLocallyOfFiniteType
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hqs : IsQuasiSeparated B S hS f) (hlft : IsLocallyOfFiniteType B S hS f)
    (hnoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T)) :
    List.TFAE
      [ IsSeparated B S hS f,
        ValuativeCriterion.Uniqueness f,
        ValuativeCriterion.DiscreteUniqueness f,
        ValuativeCriterion.CodimensionZeroUniqueness f ]
```

## Tag 0H1X, a lemma

[Tag 0H1X](https://stacks.math.columbia.edu/tag/0H1X) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_tfae_of_isQuasiSeparated_of_codimensionZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeProperCodimensionZero.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeProperCodimensionZero.lean#L496).

> **Stacks 0H1X.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> quasi-separated and of finite type, with `Y` locally Noetherian. The following are equivalent:
> 1. `f` is proper;
> 2. `f` satisfies the valuative criterion (Stacks 03IX);
> 3. every valuative diagram (Stacks 0H1V) for `f` has exactly one dotted arrow;
> 4. every valuative diagram for `f` whose valuation ring is a discrete valuation ring has
>    exactly one dotted arrow;
> 5. every valuative diagram for `f` whose valuation ring is a discrete valuation ring and whose
>    generic arrow `Spec K ⟶ X` picks out a point of codimension zero of `X` has exactly one
>    dotted arrow.
>
> Conditions (1) to (3) are equivalent by Stacks 0A40, and (3) implies (4) implies (5) trivially.
> Given (5), `f` is separated by Stacks 0H1W
> (`AlgebraicGeometry.Space.isSeparated_of_isLocallyOfFiniteType_of_codimensionZeroUniqueness`)
> and universally closed by
> `AlgebraicGeometry.Space.universallyClosed_of_codimensionZeroValuativeExistence`.

```lean
theorem isProper_tfae_of_isQuasiSeparated_of_codimensionZero
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hqs : IsQuasiSeparated B S hS f) (hft : IsFiniteType B S hS f)
    (hNoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T)) :
    List.TFAE
      [ IsProper B S hS f,
        ValuativeCriterion f,
        ∀ q : ValuativeSquare f, Nonempty q.Lift ∧ Subsingleton q.Lift,
        ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
          Nonempty q.Lift ∧ Subsingleton q.Lift,
        ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
          localRingDimension B S hS q.genericPoint = 0 →
            Nonempty q.Lift ∧ Subsingleton q.Lift ]
```

## Tag 0H1Y, a lemma

[Tag 0H1Y](https://stacks.math.columbia.edu/tag/0H1Y) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyClosed_implications_and_tfae_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianUniversallyClosedImplications.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianUniversallyClosedImplications.lean#L173).

> **Stacks 0H1Y, corrected.** Let `f : X ⟶ Y` be a morphism of finite type of algebraic spaces
> over `S`, with `Y` locally Noetherian, and number the conditions of Stacks 0H1Y as in
> `universallyClosed_implications_of_isLocallyNoetherian`:
>
> 1. `f` is universally closed;
> 2. `f` satisfies the existence part of the valuative criterion;
> 3. there are an object `V` of the site and a surjective étale morphism `V ⟶ Y` such that for
>    every `n` the base change of `f` to affine `n`-space over `V` is closed;
> 4. every valuative square for `f` whose valuation ring is a discrete valuation ring acquires a
>    dotted arrow after a finite separable extension of the fraction field and passage to a
>    dominating discrete valuation ring;
> 5. every valuative square for `f` whose valuation ring is a discrete valuation ring acquires a
>    dotted arrow after an extension of the fraction field and passage to a dominating valuation
>    ring.
>
> Then (2) ⇒ (4) ⇒ (5) ⇒ (1) ⇔ (3), and if `f` is decent (for instance quasi-separated) the five
> conditions are equivalent.
>
> **Correction.** The source asserts the equivalence of the five conditions with no hypothesis on
> `f` beyond finite type. That is false, by
> `not_forall_universallyClosed_tfae_of_isLocallyNoetherian`: the structure morphism
> `𝔸¹_ℚ/ℤ ⟶ Spec ℚ` of the quotient of the affine line by the integer translations is of finite
> type over a Noetherian scheme and universally closed (Stacks 03IV), but the `ℚ((t))`-point `1/t`
> extends to no valuation ring dominating `ℚ[[t]]`, so (1) holds and (2) fails; that morphism is
> not decent. The faulty step is the source's appeal to Stacks 03KA for (1) ⇔ (2): Stacks 03KA
> only gives (2) ⇒ (1), and the converse needs decency (Stacks 03M6, `f` being quasi-compact as it
> is of finite type) or quasi-separatedness (Stacks 0A3X). So decency is assumed exactly for the
> full equivalence, which is `universallyClosed_tfae_of_isLocallyNoetherian`, and the remaining
> implications are stated without it, as in
> `universallyClosed_implications_of_isLocallyNoetherian`.

```lean
theorem universallyClosed_implications_and_tfae_of_isLocallyNoetherian
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X_alg : IsAlgebraicSpace B S hS X) (Y_alg : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (ft : IsFiniteType B S hS f)
    (noeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T)) :
    ((ValuativeCriterion.Existence f →
        ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
          ∃ e : q.DominatingExtension,
            IsDiscreteValuationRing e.square.R ∧
              (letI := e.fieldMap.toAlgebra
               Module.Finite q.K e.square.K ∧ Algebra.IsSeparable q.K e.square.K) ∧
              Nonempty e.square.Lift) ∧
      ((∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
          ∃ e : q.DominatingExtension,
            IsDiscreteValuationRing e.square.R ∧
              (letI := e.fieldMap.toAlgebra
               Module.Finite q.K e.square.K ∧ Algebra.IsSeparable q.K e.square.K) ∧
              Nonempty e.square.Lift) →
        ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
          ∃ e : q.DominatingExtension, Nonempty e.square.Lift) ∧
      ((∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
          ∃ e : q.DominatingExtension, Nonempty e.square.Lift) →
        UniversallyClosed B S hS f) ∧
      (UniversallyClosed B S hS f ↔
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
          IsSurjective B S hS g ∧ IsEtale B S hS g ∧
            ∀ n : ℕ, ∃ (W : BigFppfOver B S hS) (a : W ⟶ V),
              IsAffineSpaceOver B S hS V W n a ∧
                IsClosedMorphism B S hS (pullback.fst (yoneda.map a ≫ g) f))) ∧
    (IsDecent B S hS f →
      List.TFAE
        [UniversallyClosed B S hS f,
          ValuativeCriterion.Existence f,
          ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
            IsSurjective B S hS g ∧ IsEtale B S hS g ∧
              ∀ n : ℕ, ∃ (W : BigFppfOver B S hS) (a : W ⟶ V),
                IsAffineSpaceOver B S hS V W n a ∧
                  IsClosedMorphism B S hS (pullback.fst (yoneda.map a ≫ g) f),
          ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
            ∃ e : q.DominatingExtension,
              IsDiscreteValuationRing e.square.R ∧
                (letI := e.fieldMap.toAlgebra
                 Module.Finite q.K e.square.K ∧ Algebra.IsSeparable q.K e.square.K) ∧
                Nonempty e.square.Lift,
          ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
            ∃ e : q.DominatingExtension, Nonempty e.square.Lift])
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.21, Tag 0CMB](https://stacks.math.columbia.edu/tag/0CMB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
