---
declaration: section
origin: cited
lean: AlgebraicGeometry.isAffine_of_unramified_quasiCompact, AlgebraicGeometry.unramified_quasiCompact_iff_iso_finite_coproduct_spectra_finite_separable, AlgebraicGeometry.exists_iso_spec_finite_separable_of_connected_unramified, AlgebraicGeometry.etale_iff_unramified_over_field, AlgebraicGeometry.FullRankJacobianSituation.unramifiedAt_over, AlgebraicGeometry.FullRankJacobianSituation.numVariables_le_numEquations, AlgebraicGeometry.FullRankJacobianSituation.etaleAt_over_of_square, AlgebraicGeometry.FullRankJacobianSituation.isFlatAt_over_of_square
statement: formalized
proof: formalized
---

# 41.8 Examples of unramified morphisms

Section 41.8 of the Stacks Project, [Tag 024W](https://stacks.math.columbia.edu/tag/024W). 3 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 024X, an example

[Tag 024X](https://stacks.math.columbia.edu/tag/024X) in the Stacks Project.

**`AlgebraicGeometry.isAffine_of_unramified_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/OverField.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/OverField.lean#L119). The attribute's comment: “affineness”. References: EGA IV (17.15.11), “affineness in c)”.

> A quasi-compact unramified scheme over a field is affine.

```lean
public theorem isAffine_of_unramified_quasiCompact
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [StalkwiseUnramified f] [QuasiCompact f] : IsAffine X
```

**`AlgebraicGeometry.unramified_quasiCompact_iff_iso_finite_coproduct_spectra_finite_separable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/OverField.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/OverField.lean#L130). The attribute's comment: “finite separable classification”.

> A morphism to the spectrum of a field is quasi-compact and unramified exactly when its
> source is a finite disjoint union of spectra of finite separable field extensions, compatibly
> with the map to the base field.

```lean
public theorem unramified_quasiCompact_iff_iso_finite_coproduct_spectra_finite_separable
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) :
    ((∃ h : LocallyOfFiniteType f, letI := h; StalkwiseUnramified f) ∧ QuasiCompact f) ↔
      ∃ (I : Type u) (_ : Finite I) (K : I → Type u) (_ : ∀ i, Field (K i))
        (_ : ∀ i, Algebra k (K i)) (_ : ∀ i, Module.Finite k (K i))
        (_ : ∀ i, Algebra.IsSeparable k (K i))
        (e : X ≅ ∐ fun i ↦ Spec (.of (K i))),
        e.hom ≫ Sigma.desc (fun i ↦ Spec.map (CommRingCat.ofHom (algebraMap k (K i)))) = f
```

**`AlgebraicGeometry.exists_iso_spec_finite_separable_of_connected_unramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/OverField.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/OverField.lean#L155). The attribute's comment: “connected case”. References: EGA IV (17.15.11), “connected X, b) => c)”.

> A connected unramified scheme over a field is the spectrum of one finite separable field
> extension, over the base field.

```lean
public theorem exists_iso_spec_finite_separable_of_connected_unramified
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [StalkwiseUnramified f] [ConnectedSpace X] :
    ∃ (K : Type u) (_ : Field K) (_ : Algebra k K) (_ : Module.Finite k K)
      (_ : Algebra.IsSeparable k K) (e : X ≅ Spec (.of K)),
      e.hom ≫ Spec.map (CommRingCat.ofHom (algebraMap k K)) = f
```

**`AlgebraicGeometry.etale_iff_unramified_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/OverField.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/OverField.lean#L196). The attribute's comment: “étale iff unramified”. References: EGA IV (17.15.11), “a) <=> b)”.

> Over a field, a morphism is étale exactly when it is locally of finite type and unramified.

```lean
public theorem etale_iff_unramified_over_field
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) :
    Etale f ↔ ∃ h : LocallyOfFiniteType f, letI := h; StalkwiseUnramified f
```

## Tag 024Y, an example

[Tag 024Y](https://stacks.math.columbia.edu/tag/024Y) in the Stacks Project.

**`AlgebraicGeometry.FullRankJacobianSituation.unramifiedAt_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/SquareJacobian.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/SquareJacobian.lean#L268). The attribute's comment: “unramified_point”.

> A polynomial quotient whose Jacobian has full rank at a prime is unramified over the base at
> the corresponding point of its zero scheme.

```lean
public theorem unramifiedAt_over (S : FullRankJacobianSituation R n m) :
    UnramifiedAt S.over S.point
```

**`AlgebraicGeometry.FullRankJacobianSituation.numVariables_le_numEquations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/SquareJacobian.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/SquareJacobian.lean#L318). The attribute's comment: “enough_equations”.

> A full-rank Jacobian needs at least as many equations as variables.

```lean
public theorem numVariables_le_numEquations (S : FullRankJacobianSituation R n m) : n ≤ m
```

**`AlgebraicGeometry.FullRankJacobianSituation.etaleAt_over_of_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/SquareJacobian.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/SquareJacobian.lean#L325). The attribute's comment: “square_etale”.

> A polynomial quotient with a square, full-rank Jacobian at a prime is étale over the base at
> the corresponding point.

```lean
public theorem etaleAt_over_of_square (S : FullRankJacobianSituation R n m) (h : m = n) :
    EtaleAt S.over S.point
```

**`AlgebraicGeometry.FullRankJacobianSituation.isFlatAt_over_of_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/SquareJacobian.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/SquareJacobian.lean#L361). The attribute's comment: “square_flat”.

> A square system of equations whose Jacobian has full rank at a prime defines a morphism flat
> at the corresponding point of its zero scheme.

```lean
public theorem isFlatAt_over_of_square (S : FullRankJacobianSituation R n n) :
    IsFlatAt S.over.toLRSHom.toShHom S.point
```

**`AlgebraicGeometry.FullRankJacobianSystem.numVariables_le_numEquations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/JacobianCriterion.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/JacobianCriterion.lean#L62). The attribute's comment: “enough_equations”.

> A full-rank Jacobian needs at least as many equations as variables.

```lean
public theorem numVariables_le_numEquations (S : FullRankJacobianSystem R n m) : n ≤ m
```

**`AlgebraicGeometry.FullRankJacobianSystem.unramifiedAt_of_jacobian_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/JacobianCriterion.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/JacobianCriterion.lean#L138). The attribute's comment: “unramified_point”.

> **Stacks Project, Tag 024Y.** Full column rank of the Jacobian at a prime makes the
> corresponding point of the zero scheme unramified over the base.

```lean
public theorem unramifiedAt_of_jacobian_rank (S : FullRankJacobianSystem R n m) :
    UnramifiedAt S.over S.point
```

**`AlgebraicGeometry.FullRankJacobianSystem.etaleAt_of_square_jacobian_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/JacobianCriterion.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/JacobianCriterion.lean#L161). The attribute's comment: “square_etale”.

> **Stacks Project, Tag 024Y.** A polynomial quotient with a square Jacobian of full rank at a
> prime is étale over the base at the corresponding point.

```lean
public theorem etaleAt_of_square_jacobian_rank (S : FullRankJacobianSystem R n m) (h : m = n) :
    EtaleAt S.over S.point
```

**`AlgebraicGeometry.FullRankJacobianSystem.flatAt_of_square_jacobian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/JacobianCriterion.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Examples/JacobianCriterion.lean#L181). The attribute's comment: “square_flat”.

> **Stacks Project, Tag 024Y.** A polynomial quotient with a square Jacobian of full rank at a
> prime is flat over the base at the corresponding point.

```lean
public theorem flatAt_of_square_jacobian (S : FullRankJacobianSystem R n n) :
    IsFlatAt S.over.toLRSHom.toShHom S.point
```

## Tag 024Z, an example

[Tag 024Z](https://stacks.math.columbia.edu/tag/024Z) in the Stacks Project.

**`AlgebraicGeometry.unramifiedAt_iff_ramificationIdx_eq_one_and_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFields.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFields.lean#L112). The attribute's comment: “agreement_of_unramifiedness”.

> **Stacks Project, Tag 024Z.** At a nonzero prime of the larger ring of integers,
> scheme-theoretic unramifiedness is equivalent to ramification index one together with
> separability of the residue extension.

```lean
theorem unramifiedAt_iff_ramificationIdx_eq_one_and_isSeparable
    (K L : Type u) [Field K] [Field L] [NumberField K] [NumberField L] [Algebra K L]
    (q : PrimeSpectrum (RingOfIntegers L)) (hq : q.asIdeal ≠ ⊥) :
    letI : Module.Finite (RingOfIntegers K) (RingOfIntegers L) :=
      IsIntegralClosure.finite (RingOfIntegers K) K L (RingOfIntegers L)
    letI : IsFinite (ringOfIntegersSpecMap K L) := (IsFinite.SpecMap_iff _).2
      (IsIntegralClosure.finite (RingOfIntegers K) K L (RingOfIntegers L))
    letI : LocallyOfFiniteType (ringOfIntegersSpecMap K L) := inferInstance
    StalkwiseUnramifiedAt (ringOfIntegersSpecMap K L) q ↔
      (letI := Localization.AtPrime.algebraOfLiesOver
          (q.asIdeal.under (RingOfIntegers K)) q.asIdeal
       Ideal.ramificationIdx q.asIdeal (RingOfIntegers K) = 1 ∧
        Algebra.IsSeparable (q.asIdeal.under (RingOfIntegers K)).ResidueField
          q.asIdeal.ResidueField)
```

**`AlgebraicGeometry.unramifiedAt_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFields.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFields.lean#L141). The attribute's comment: “agreement_of_unramifiedness”.

> **Stacks Project, Tag 024Z.** The morphism on spectra of rings of integers is unramified at
> the generic point.

```lean
theorem unramifiedAt_genericPoint
    (K L : Type u) [Field K] [Field L] [NumberField K] [NumberField L] [Algebra K L] :
    letI : Module.Finite (RingOfIntegers K) (RingOfIntegers L) :=
      IsIntegralClosure.finite (RingOfIntegers K) K L (RingOfIntegers L)
    letI : IsFinite (ringOfIntegersSpecMap K L) := (IsFinite.SpecMap_iff _).2
      (IsIntegralClosure.finite (RingOfIntegers K) K L (RingOfIntegers L))
    letI : LocallyOfFiniteType (ringOfIntegersSpecMap K L) := inferInstance
    StalkwiseUnramifiedAt (ringOfIntegersSpecMap K L)
      (⟨⊥, inferInstance⟩ : PrimeSpectrum (RingOfIntegers L))
```

**`AlgebraicGeometry.flat_ringOfIntegersSpecMap`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean#L95). The attribute's comment: “the morphism Spec(O_L) -> Spec(O_K) is flat (on all of Spec(O_L), so in particular on X)”.

> The morphism on spectra of rings of integers is flat.

```lean
instance flat_ringOfIntegersSpecMap : Flat (ringOfIntegersSpecMap K L)
```

**`AlgebraicGeometry.stalkwiseUnramifiedAt_ringOfIntegersSpecMap_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean#L104). The attribute's comment: “the points where f is unramified in our sense are the points where f is unramified in the conventional sense, at every point of Spec(O_L)”.

> The points of `Spec(𝒪_L)` where `f : Spec(𝒪_L) → Spec(𝒪_K)` is unramified in the sense of
> schemes are the points where it is unramified in the conventional sense: the generic point, and the
> nonzero primes with ramification index one and separable residue field extension.

```lean
theorem stalkwiseUnramifiedAt_ringOfIntegersSpecMap_iff (q : PrimeSpectrum (𝓞 L)) :
    StalkwiseUnramifiedAt (ringOfIntegersSpecMap K L) q ↔
      (q.asIdeal ≠ ⊥ →
        (letI := Localization.AtPrime.algebraOfLiesOver (q.asIdeal.under (𝓞 K)) q.asIdeal
         Ideal.ramificationIdx q.asIdeal (𝓞 K) = 1 ∧
          Algebra.IsSeparable (q.asIdeal.under (𝓞 K)).ResidueField q.asIdeal.ResidueField))
```

**`AlgebraicGeometry.zeroLocus_differentIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean#L176). The attribute's comment: “in the conventional sense, the locus of ramification in Spec(O_L) is the vanishing set of the different”.

> In the conventional sense, the locus of ramification in `Spec(𝒪_L)` is the vanishing set of the
> different: a point of `Spec(𝒪_L)` lies in the vanishing set of the different exactly when it is a
> nonzero prime whose ramification index is not one or whose residue field extension is not
> separable.

```lean
theorem zeroLocus_differentIdeal :
    zeroLocus (differentIdeal (𝓞 K) (𝓞 L) : Set (𝓞 L)) =
      {q | q.asIdeal ≠ ⊥ ∧
        ¬ (letI := Localization.AtPrime.algebraOfLiesOver (q.asIdeal.under (𝓞 K)) q.asIdeal
           Ideal.ramificationIdx q.asIdeal (𝓞 K) = 1 ∧
            Algebra.IsSeparable (q.asIdeal.under (𝓞 K)).ResidueField
              q.asIdeal.ResidueField)}
```

**`AlgebraicGeometry.algebraDiscriminantIdeal_ringOfIntegers_eq_relNorm_differentIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean#L202). The attribute's comment: “the discriminant is an ideal in O_K, namely it is the norm of the different”.

> The discriminant of `L/K`, an ideal of `𝒪_K` — the discriminant ideal of the finite locally
> free algebra `𝒪_L` over `𝒪_K`, the zeroth Fitting ideal of the cokernel of its trace pairing — is
> the norm of the different.

```lean
theorem algebraDiscriminantIdeal_ringOfIntegers_eq_relNorm_differentIdeal :
    Stacks.Discriminant.algebraDiscriminantIdeal (𝓞 K) (𝓞 L) =
      Ideal.relNorm (𝓞 K) (differentIdeal (𝓞 K) (𝓞 L))
```

**`AlgebraicGeometry.zeroLocus_algebraDiscriminantIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean#L293). The attribute's comment: “the vanishing set of the discriminant is precisely the set of points of Spec(O_K) which ramify in L”.

> The vanishing set of the discriminant is precisely the set of points of `Spec(𝒪_K)` which
> ramify in `L`: the primes of `𝒪_K` lying under a nonzero prime of `𝒪_L` whose ramification index is
> not one or whose residue field extension is not separable.

```lean
theorem zeroLocus_algebraDiscriminantIdeal :
    zeroLocus (Stacks.Discriminant.algebraDiscriminantIdeal (𝓞 K) (𝓞 L) : Set (𝓞 K)) =
      {p | ∃ q : PrimeSpectrum (𝓞 L), comap (algebraMap (𝓞 K) (𝓞 L)) q = p ∧
        q.asIdeal ≠ ⊥ ∧
        ¬ (letI := Localization.AtPrime.algebraOfLiesOver (q.asIdeal.under (𝓞 K)) q.asIdeal
           Ideal.ramificationIdx q.asIdeal (𝓞 K) = 1 ∧
            Algebra.IsSeparable (q.asIdeal.under (𝓞 K)).ResidueField
              q.asIdeal.ResidueField)}
```

**`AlgebraicGeometry.stalkwiseUnramified_flat_and_etale_differentOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean#L318). The attribute's comment: “the morphism X -> Spec(O_K) is unramified, flat, and hence etale”.

> Denote by `X` the complement of the closed subset defined by the different in `Spec(𝒪_L)`. The
> morphism `X → Spec(𝒪_K)` is unramified; it is furthermore flat, and hence it is actually étale.

```lean
theorem stalkwiseUnramified_flat_and_etale_differentOpen :
    StalkwiseUnramified ((differentOpen K L).ι ≫ ringOfIntegersSpecMap K L) ∧
      Flat ((differentOpen K L).ι ≫ ringOfIntegersSpecMap K L) ∧
        Etale ((differentOpen K L).ι ≫ ringOfIntegersSpecMap K L)
```

**`AlgebraicGeometry.isFinite_and_etale_morphismRestrict_discriminantOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFieldsDifferent.lean#L449). The attribute's comment: “if L/K is finite Galois, X is the preimage of Y and X -> Y is finite etale (and surjective): a finite etale covering”.

> If `L/K` is finite Galois and `Y` is the complement of the closed subset defined by the
> discriminant in `Spec(𝒪_K)`, then the preimage of `Y` is the complement `X` of the closed subset
> defined by the different in `Spec(𝒪_L)`, and `X → Y` is a finite étale morphism, which is moreover
> surjective: a finite étale covering.

```lean
theorem isFinite_and_etale_morphismRestrict_discriminantOpen [IsGalois K L] :
    ringOfIntegersSpecMap K L ⁻¹ᵁ discriminantOpen K L = differentOpen K L ∧
      IsFinite (ringOfIntegersSpecMap K L ∣_ discriminantOpen K L) ∧
        Etale (ringOfIntegersSpecMap K L ∣_ discriminantOpen K L) ∧
          Surjective (ringOfIntegersSpecMap K L ∣_ discriminantOpen K L)
```

**`NumberField.differentIdeal_eq_annihilator_kaehlerDifferential_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/DifferentAnnihilatorGeneral.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/NumberTheory/DifferentAnnihilatorGeneral.lean#L261). The attribute's comment: “the different is the annihilator of the module of differentials”.

> **The different of an extension of number rings is the annihilator of the module of
> differentials.** For an arbitrary extension of number fields `L/K`,
>
>   `differentIdeal 𝒪_K 𝒪_L = Module.annihilator 𝒪_L Ω[𝒪_L⁄𝒪_K]`.

```lean
theorem differentIdeal_eq_annihilator_kaehlerDifferential_general :
    differentIdeal (𝓞 K) (𝓞 L) = Module.annihilator (𝓞 L) Ω[(𝓞 L)⁄(𝓞 K)]
```

**`RingHom.Flat.of_injective_of_isDiscreteValuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/FlatExtension.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/FlatExtension.lean#L45). The attribute's comment: “any local homomorphism of discrete valuation rings is flat, in the corrected form for injective local homomorphisms (extensions of discrete valuation rings), proved here for any injective homomorphism from a discrete valuation ring to a domain”. References: EGA 0 (6.3.4), “last assertion, A a DVR”; SGA 6 X (7.15), “special case”.

> **Stacks Project, Tag 024Z.** An injective ring homomorphism from a discrete valuation ring
> to a domain is flat. In particular any extension of discrete valuation rings — an injective local
> homomorphism of discrete valuation rings — is flat.

```lean
theorem RingHom.Flat.of_injective_of_isDiscreteValuationRing {R S : Type*} [CommRing R]
    [IsDomain R] [IsDiscreteValuationRing R] [CommRing S] [IsDomain S] (f : R →+* S)
    (hf : Function.Injective f) : f.Flat
```

Declarations registered for the tag:

- [`Algebra.isUnramifiedAt_bot`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.isUnramifiedAt_bot#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFields.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/NumberFields.lean#L152) (StacksFrontier): “agreement_of_unramifiedness”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.8, Tag 024W](https://stacks.math.columbia.edu/tag/024W)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
