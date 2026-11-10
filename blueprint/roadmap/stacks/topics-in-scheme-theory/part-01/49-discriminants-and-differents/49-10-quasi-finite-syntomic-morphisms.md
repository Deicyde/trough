---
declaration: section
origin: cited
lean: AlgebraicGeometry.hasLocalSquareRelativeGlobalCompleteIntersection_of_locallyQuasiFinite_syntomic, AlgebraicGeometry.locallyQuasiFinite_of_hasLocalSquareRelativeGlobalCompleteIntersection, AlgebraicGeometry.syntomic_of_hasLocalSquareRelativeGlobalCompleteIntersection, AlgebraicGeometry.hasLocalSquarePresentation_of_hasLocalSquareRelativeGlobalCompleteIntersection, AlgebraicGeometry.hasLocalSquareRelativeGlobalCompleteIntersection_of_hasLocalSquarePresentation, AlgebraicGeometry.locallyQuasiFinite_syntomic_tfae, AlgebraicGeometry.flat_and_isLocalCompleteIntersectionMorphism_of_locallyQuasiFinite_syntomic, AlgebraicGeometry.locallyOfFinitePresentation_and_lci_fibers_of_locallyQuasiFinite_flat_lci
statement: formalized
proof: formalized
---

# 49.10 Quasi-finite syntomic morphisms

Section 49.10 of the Stacks Project, [Tag 0DWJ](https://stacks.math.columbia.edu/tag/0DWJ). 7 tags here are carried by 44 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BWE, a lemma

[Tag 0BWE](https://stacks.math.columbia.edu/tag/0BWE) in the Stacks Project.

**`AlgebraicGeometry.hasLocalSquareRelativeGlobalCompleteIntersection_of_locallyQuasiFinite_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L248). The attribute's comment: “the implication (1) ⟹ (5)”.

> A locally quasi-finite syntomic morphism of schemes has, around every point of its source, a
> square relative global complete intersection presentation.

```lean
theorem hasLocalSquareRelativeGlobalCompleteIntersection_of_locallyQuasiFinite_syntomic
    {Y X : Scheme.{u}} {f : Y ⟶ X} (hqf : LocallyQuasiFinite f) (hf : Syntomic f) :
    HasLocalSquareRelativeGlobalCompleteIntersection f
```

**`AlgebraicGeometry.locallyQuasiFinite_of_hasLocalSquareRelativeGlobalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L283). The attribute's comment: “the implication (5) ⟹ (1), the locally-quasi-finite conjunct”.

> A morphism of schemes with square relative global complete intersection presentations around
> every point of its source is locally quasi-finite.

```lean
theorem locallyQuasiFinite_of_hasLocalSquareRelativeGlobalCompleteIntersection
    {Y X : Scheme.{u}} {f : Y ⟶ X} (h : HasLocalSquareRelativeGlobalCompleteIntersection f) :
    LocallyQuasiFinite f
```

**`AlgebraicGeometry.syntomic_of_hasLocalSquareRelativeGlobalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L298). The attribute's comment: “the implication (5) ⟹ (1), the syntomic conjunct”.

> A morphism of schemes with square relative global complete intersection presentations around
> every point of its source is syntomic.

```lean
theorem syntomic_of_hasLocalSquareRelativeGlobalCompleteIntersection {Y X : Scheme.{u}}
    {f : Y ⟶ X} (h : HasLocalSquareRelativeGlobalCompleteIntersection f) : Syntomic f
```

**`AlgebraicGeometry.hasLocalSquarePresentation_of_hasLocalSquareRelativeGlobalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L312). The attribute's comment: “the implication (5) ⟹ (4), the presentation conjunct”.

> A morphism of schemes which is locally a square relative global complete intersection
> `B = A[x_1, …, x_n]/(f_1, …, f_n)` is locally of the form `B = A[x_1, …, x_n, 1/h]/(f_1, …, f_n)`,
> with `h = 1`.

```lean
theorem hasLocalSquarePresentation_of_hasLocalSquareRelativeGlobalCompleteIntersection
    {Y X : Scheme.{u}} {f : Y ⟶ X} (h : HasLocalSquareRelativeGlobalCompleteIntersection f) :
    HasLocalSquarePresentation f
```

**`AlgebraicGeometry.hasLocalSquareRelativeGlobalCompleteIntersection_of_hasLocalSquarePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L325). The attribute's comment: “the implication (4) ⟹ (5)”.

> A locally quasi-finite morphism of schemes which is locally of the form
> `B = A[x_1, …, x_n, 1/h]/(f_1, …, f_n)` is locally a square relative global complete
> intersection.

```lean
theorem hasLocalSquareRelativeGlobalCompleteIntersection_of_hasLocalSquarePresentation
    {Y X : Scheme.{u}} {f : Y ⟶ X} (hqf : LocallyQuasiFinite f)
    (h : HasLocalSquarePresentation f) :
    HasLocalSquareRelativeGlobalCompleteIntersection f
```

**`AlgebraicGeometry.locallyQuasiFinite_syntomic_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L350). The attribute's comment: “the equivalence of (1), (2), (3), (4) and (5)”.

> For a morphism of schemes `f : Y ⟶ X` the following are equivalent:
>
> 1. `f` is locally quasi-finite and syntomic;
> 2. `f` is locally quasi-finite, flat, and a local complete intersection morphism;
> 3. `f` is locally quasi-finite, flat, locally of finite presentation, and all the fibres of `f`
>    are local complete intersections over the residue fields of their base points;
> 4. `f` is locally quasi-finite and, around every point of its source, there are affine opens
>    `y ∈ V = Spec(B) ⊆ Y` and `U = Spec(A) ⊆ X` with `f(V) ⊆ U`, an integer `n` and
>    `h, f_1, …, f_n ∈ A[x_1, …, x_n]` with `B = A[x_1, …, x_n, 1/h]/(f_1, …, f_n)`;
> 5. around every point of the source there are such affine opens with `A → B` a relative global
>    complete intersection of the form `B = A[x_1, …, x_n]/(f_1, …, f_n)`.

```lean
theorem locallyQuasiFinite_syntomic_tfae {Y X : Scheme.{u}} (f : Y ⟶ X) :
    List.TFAE [
      LocallyQuasiFinite f ∧ Syntomic f,
      (LocallyQuasiFinite f ∧ Flat f) ∧ IsLocalCompleteIntersectionMorphism f,
      ((LocallyQuasiFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
        ∀ x : X, IsLocalCompleteIntersectionOverField (f.fiberToSpecResidueField x),
      LocallyQuasiFinite f ∧ HasLocalSquarePresentation f,
      HasLocalSquareRelativeGlobalCompleteIntersection f]
```

**`AlgebraicGeometry.flat_and_isLocalCompleteIntersectionMorphism_of_locallyQuasiFinite_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L384). The attribute's comment: “the implication (1) ⟹ (2)”.

> A locally quasi-finite syntomic morphism of schemes is locally quasi-finite, flat, and a local
> complete intersection morphism.

```lean
theorem flat_and_isLocalCompleteIntersectionMorphism_of_locallyQuasiFinite_syntomic
    {Y X : Scheme.{u}} {f : Y ⟶ X} (h : LocallyQuasiFinite f ∧ Syntomic f) :
    (LocallyQuasiFinite f ∧ Flat f) ∧ IsLocalCompleteIntersectionMorphism f
```

**`AlgebraicGeometry.locallyOfFinitePresentation_and_lci_fibers_of_locallyQuasiFinite_flat_lci`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L393). The attribute's comment: “the implication (2) ⟹ (3)”. References: SGA 6 VIII (1.4), “special case”.

> A locally quasi-finite flat local complete intersection morphism of schemes is locally of
> finite presentation and all of its fibres are local complete intersections over the residue fields
> of their base points.

```lean
theorem locallyOfFinitePresentation_and_lci_fibers_of_locallyQuasiFinite_flat_lci
    {Y X : Scheme.{u}} {f : Y ⟶ X}
    (h : (LocallyQuasiFinite f ∧ Flat f) ∧ IsLocalCompleteIntersectionMorphism f) :
    ((LocallyQuasiFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
      ∀ x : X, IsLocalCompleteIntersectionOverField (f.fiberToSpecResidueField x)
```

**`AlgebraicGeometry.locallyQuasiFinite_and_hasLocalSquarePresentation_of_lci_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L404). The attribute's comment: “the implication (3) ⟹ (4)”.

> A locally quasi-finite flat morphism of schemes which is locally of finite presentation and
> all of whose fibres are local complete intersections over the residue fields of their base points
> is, around every point of its source, of the form `B = A[x_1, …, x_n, 1/h]/(f_1, …, f_n)`.

```lean
theorem locallyQuasiFinite_and_hasLocalSquarePresentation_of_lci_fibers {Y X : Scheme.{u}}
    {f : Y ⟶ X}
    (h : ((LocallyQuasiFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
      ∀ x : X, IsLocalCompleteIntersectionOverField (f.fiberToSpecResidueField x)) :
    LocallyQuasiFinite f ∧ HasLocalSquarePresentation f
```

**`AlgebraicGeometry.locallyQuasiFinite_and_syntomic_of_hasLocalSquarePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L414). The attribute's comment: “the implication (4) ⟹ (1)”.

> A locally quasi-finite morphism of schemes which is locally of the form
> `B = A[x_1, …, x_n, 1/h]/(f_1, …, f_n)`, with as many relations as variables, is syntomic.

```lean
theorem locallyQuasiFinite_and_syntomic_of_hasLocalSquarePresentation {Y X : Scheme.{u}}
    {f : Y ⟶ X} (h : LocallyQuasiFinite f ∧ HasLocalSquarePresentation f) :
    LocallyQuasiFinite f ∧ Syntomic f
```

**`AlgebraicGeometry.locallyQuasiFinite_and_syntomic_of_lci_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L423). The attribute's comment: “the implication (3) ⟹ (1)”.

> A locally quasi-finite flat morphism of schemes which is locally of finite presentation and
> all of whose fibres are local complete intersections over the residue fields of their base points
> is syntomic.

```lean
theorem locallyQuasiFinite_and_syntomic_of_lci_fibers {Y X : Scheme.{u}} {f : Y ⟶ X}
    (h : ((LocallyQuasiFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
      ∀ x : X, IsLocalCompleteIntersectionOverField (f.fiberToSpecResidueField x)) :
    LocallyQuasiFinite f ∧ Syntomic f
```

**`AlgebraicGeometry.hasLocalSquareRelativeGlobalCompleteIntersection_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L432). The attribute's comment: “the equivalence of (1) and (5)”.

> A morphism of schemes has a square relative global complete intersection presentation around
> every point of its source if and only if it is locally quasi-finite and syntomic.

```lean
theorem hasLocalSquareRelativeGlobalCompleteIntersection_iff {Y X : Scheme.{u}} (f : Y ⟶ X) :
    HasLocalSquareRelativeGlobalCompleteIntersection f ↔
      LocallyQuasiFinite f ∧ Syntomic f
```

**`AlgebraicGeometry.locallyQuasiFinite_flat_lfp_and_hasTorAmplitude_of_locallyQuasiFinite_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFiniteNaiveCotangent.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFiniteNaiveCotangent.lean#L181). The attribute's comment: “the implication (1) ⟹ (6)”.

> A locally quasi-finite syntomic morphism of schemes is locally quasi-finite, flat and locally
> of finite presentation, and its naive cotangent complex `NL_{Y/X}` has Tor amplitude in
> `[-1, 0]`.

```lean
theorem locallyQuasiFinite_flat_lfp_and_hasTorAmplitude_of_locallyQuasiFinite_syntomic
    {Y X : Scheme.{u}} {f : Y ⟶ X} (h : LocallyQuasiFinite f ∧ Syntomic f) :
    ((LocallyQuasiFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
      Stacks.Cohomology.TorAmplitude.HasTorAmplitude Y.toRingedSpace
        (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0
```

**`AlgebraicGeometry.locallyQuasiFinite_syntomic_of_flat_lfp_of_hasTorAmplitude`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFiniteNaiveCotangent.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFiniteNaiveCotangent.lean#L192). The attribute's comment: “the implication (6) ⟹ (1)”.

> A locally quasi-finite flat morphism of schemes which is locally of finite presentation and
> whose naive cotangent complex has Tor amplitude in `[-1, 0]` is syntomic.

```lean
theorem locallyQuasiFinite_syntomic_of_flat_lfp_of_hasTorAmplitude {Y X : Scheme.{u}}
    {f : Y ⟶ X}
    (h : ((LocallyQuasiFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
      Stacks.Cohomology.TorAmplitude.HasTorAmplitude Y.toRingedSpace
        (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0) :
    LocallyQuasiFinite f ∧ Syntomic f
```

**`AlgebraicGeometry.flat_lfp_and_isPerfect_and_hasTorAmplitude_of_locallyQuasiFinite_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFiniteNaiveCotangent.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFiniteNaiveCotangent.lean#L206). The attribute's comment: “the implication (1) ⟹ (7)”. References: SGA 6 0 (4.3), “special case”; SGA 6 VIII (2.4), “partial”.

> A locally quasi-finite syntomic morphism of schemes is flat and locally of finite
> presentation, and its naive cotangent complex `NL_{Y/X}` is a perfect object of `D(𝒪_Y)` of rank
> zero with Tor amplitude in `[-1, 0]`.

```lean
theorem flat_lfp_and_isPerfect_and_hasTorAmplitude_of_locallyQuasiFinite_syntomic
    {Y X : Scheme.{u}} {f : Y ⟶ X} (h : LocallyQuasiFinite f ∧ Syntomic f) :
    (Flat f ∧ LocallyOfFinitePresentation f) ∧
      (Stacks.Cohomology.PerfectComplexes.IsPerfect (X := Y.toRingedSpace)
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
        DeterminantTwoTerm.IsRankZeroScheme
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
        Stacks.Cohomology.TorAmplitude.HasTorAmplitude Y.toRingedSpace
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0)
```

**`AlgebraicGeometry.locallyQuasiFinite_syntomic_of_flat_lfp_of_isPerfect_of_isRankZeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFiniteNaiveCotangent.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFiniteNaiveCotangent.lean#L224). The attribute's comment: “the implication (7) ⟹ (1)”.

> A flat morphism of schemes which is locally of finite presentation and whose naive cotangent
> complex `NL_{Y/X}` is a perfect object of `D(𝒪_Y)` of rank zero with Tor amplitude in `[-1, 0]`
> is locally quasi-finite and syntomic.

```lean
theorem locallyQuasiFinite_syntomic_of_flat_lfp_of_isPerfect_of_isRankZeroScheme
    {Y X : Scheme.{u}} {f : Y ⟶ X}
    (h : (Flat f ∧ LocallyOfFinitePresentation f) ∧
      (Stacks.Cohomology.PerfectComplexes.IsPerfect (X := Y.toRingedSpace)
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
        DeterminantTwoTerm.IsRankZeroScheme
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
        Stacks.Cohomology.TorAmplitude.HasTorAmplitude Y.toRingedSpace
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0)) :
    LocallyQuasiFinite f ∧ Syntomic f
```

**`AlgebraicGeometry.locallyQuasiFinite_syntomic_tfae_naiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFiniteNaiveCotangent.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFiniteNaiveCotangent.lean#L255).

> For a morphism of schemes `f : Y ⟶ X` the following are equivalent:
>
> 1. `f` is locally quasi-finite and syntomic;
> 2. `f` is locally quasi-finite, flat, and a local complete intersection morphism;
> 3. `f` is locally quasi-finite, flat, locally of finite presentation, and all the fibres of `f`
>    are local complete intersections over the residue fields of their base points;
> 4. `f` is locally quasi-finite and, around every point of its source, there are affine opens
>    `y ∈ V = Spec(B) ⊆ Y` and `U = Spec(A) ⊆ X` with `f(V) ⊆ U`, an integer `n` and
>    `h, f_1, …, f_n ∈ A[x_1, …, x_n]` with `B = A[x_1, …, x_n, 1/h]/(f_1, …, f_n)`;
> 5. around every point of the source there are such affine opens with `A → B` a relative global
>    complete intersection of the form `B = A[x_1, …, x_n]/(f_1, …, f_n)`;
> 6. `f` is locally quasi-finite, flat, locally of finite presentation, and `NL_{Y/X}` has Tor
>    amplitude in `[-1, 0]`;
> 7. `f` is flat and locally of finite presentation, and `NL_{Y/X}` is a perfect object of
>    `D(𝒪_Y)` of rank zero with Tor amplitude in `[-1, 0]`.

```lean
theorem locallyQuasiFinite_syntomic_tfae_naiveCotangentComplex {Y X : Scheme.{u}}
    (f : Y ⟶ X) :
    List.TFAE [
      LocallyQuasiFinite f ∧ Syntomic f,
      (LocallyQuasiFinite f ∧ Flat f) ∧ IsLocalCompleteIntersectionMorphism f,
      ((LocallyQuasiFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
        ∀ x : X, IsLocalCompleteIntersectionOverField (f.fiberToSpecResidueField x),
      LocallyQuasiFinite f ∧ HasLocalSquarePresentation f,
      HasLocalSquareRelativeGlobalCompleteIntersection f,
      ((LocallyQuasiFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
        Stacks.Cohomology.TorAmplitude.HasTorAmplitude Y.toRingedSpace
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0,
      (Flat f ∧ LocallyOfFinitePresentation f) ∧
        (Stacks.Cohomology.PerfectComplexes.IsPerfect (X := Y.toRingedSpace)
            (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
          DeterminantTwoTerm.IsRankZeroScheme
            (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
          Stacks.Cohomology.TorAmplitude.HasTorAmplitude Y.toRingedSpace
            (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0)]
```

## Tag 0DWK, a lemma

[Tag 0DWK](https://stacks.math.columbia.edu/tag/0DWK) in the Stacks Project.

**`Stacks.Discriminant.dualizingModule_invertible_iff_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleInvertibility.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleInvertibility.lean#L299). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0DWK**, part (1). For a quasi-finite flat homomorphism of Noetherian
> rings, the relative dualizing module is invertible over the target if and only if the relative
> dualizing module of the fibre `B ⊗_A κ(p)` over `κ(p)` is invertible for every prime `p` of the
> base.

```lean
theorem dualizingModule_invertible_iff_fibers
    {A : Type u} {B : Type v}
    [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [Algebra.FiniteType A B] [Algebra.QuasiFinite A B]
    [Module.Flat A B]
    (F : FiniteOpenFactorization.{u, v, w} A B) :
    Module.Invertible B (dualizingModule F) ↔
      ∀ (p : PrimeSpectrum A),
        letI : Algebra p.asIdeal.ResidueField (p.asIdeal.Fiber B) :=
          Algebra.TensorProduct.leftAlgebra
        ∀ (G : FiniteOpenFactorization.{u, max u v, max u w}
            p.asIdeal.ResidueField (p.asIdeal.Fiber B)),
          Module.Invertible (p.asIdeal.Fiber B) (dualizingModule G)
```

**`Stacks.Discriminant.relativeDualizingModuleData_isInvertible_iff_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleInvertibility.lean, line 818](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleInvertibility.lean#L818). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0DWK**, part (2). For a quasi-finite flat morphism `f : Y ⟶ X` of
> Noetherian schemes, the relative dualizing module `ω_{Y/X}` of Tag 0BVG is an invertible
> `𝒪_Y`-module if and only if the relative dualizing module `ω_{Y_x/x}` of the fibre
> `Y_x → Spec κ(x)` is invertible for every point `x` of `X`. Both modules are the ones constructed
> by `Stacks.Discriminant.relativeDualizingModuleData`.

```lean
theorem relativeDualizingModuleData_isInvertible_iff_fibers :
    Stacks.SheafOfModules.IsInvertible Y.presheaf
        (structureSheafRing Y.toRingedSpace).property (relativeDualizingModuleData f).sheaf ↔
      ∀ x : X, Stacks.SheafOfModules.IsInvertible (f.fiber x).presheaf
        (structureSheafRing (f.fiber x).toRingedSpace).property
          (relativeDualizingModuleData (f.fiberToSpecResidueField x)).sheaf
```

## Tag 0DWL, a lemma

[Tag 0DWL](https://stacks.math.columbia.edu/tag/0DWL) in the Stacks Project.

**`Stacks.Discriminant.dualizingModule_invertible_of_isGlobalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleCompleteIntersection.lean, line 642](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleCompleteIntersection.lean#L642).

> **Stacks Project, Tag 0DWL.** Let `k` be a field and let `B` be a global complete
> intersection over `k` of dimension `0`. Then the relative dualizing module `ω_{B/k}` is an
> invertible `B`-module.
>
> The dualizing module is computed from an arbitrary finite-open factorization of `k → B`; the
> choice is immaterial by `Stacks.Discriminant.dualizingModuleEquiv`.

```lean
theorem dualizingModule_invertible_of_isGlobalCompleteIntersection
    {k : Type u} {B : Type v} [Field k] [CommRing B] [Algebra k B]
    (F : FiniteOpenFactorization.{u, v, w} k B)
    (hB : IsGlobalCompleteIntersection k B) (hdim : ringKrullDim B = 0) :
    Module.Invertible B (dualizingModule F)
```

## Tag 0BWF, a lemma

[Tag 0BWF](https://stacks.math.columbia.edu/tag/0BWF) in the Stacks Project.

**`Stacks.Discriminant.dualizingModule_invertible_of_squarePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleQuasiFiniteSyntomic.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleQuasiFiniteSyntomic.lean#L110). The attribute's comment: “the affine case: a square relative global complete intersection presentation, which is part (5) of Stacks 0BWE”.

> **Stacks Project, Tag 0BWF**, the affine case the source reduces to. Let `A → B` be a
> quasi-finite flat homomorphism of Noetherian rings with a presentation
> `B = A[x_1, …, x_n]/(f_1, …, f_n)` by as many relations as variables. Then the relative
> dualizing module `ω_{B/A}` is an invertible `B`-module.

```lean
theorem dualizingModule_invertible_of_squarePresentation
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [IsNoetherianRing B] [Algebra.QuasiFinite A B] [Module.Flat A B]
    {n : ℕ} (P : Algebra.Presentation A B (Fin n) (Fin n))
    (F : FiniteOpenFactorization.{u, v, w} A B) :
    Module.Invertible B (dualizingModule F)
```

**`Stacks.Discriminant.exists_chart_dualizingModule_invertible_of_locallyQuasiFinite_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleQuasiFiniteSyntomic.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleQuasiFiniteSyntomic.lean#L135). The attribute's comment: “the scheme-level statement, stated at the charts of `f`: every point of `Y` has an affine open `V = Spec B` over an affine open `U = Spec A` of `X` on which `ω_{B/A}` is invertible. This is condition (4) of Stacks 0C16, which `Stacks.Discriminant.isInvertible_iff_exists_chart_dualizingModule_invertible` identifies with invertibility of `ω_{Y/X}` as a sheaf.”.

> **Stacks Project, Tag 0BWF.** Let `f : Y ⟶ X` be a locally quasi-finite syntomic morphism of
> locally Noetherian schemes. Then every point of `Y` has an affine open neighbourhood
> `V = Spec B` lying over an affine open `U = Spec A` of `X` for which the algebraic relative
> dualizing module `ω_{B/A}` is an invertible `B`-module.

```lean
theorem exists_chart_dualizingModule_invertible_of_locallyQuasiFinite_syntomic
    (hf : Syntomic f) :
    ∀ y : Y, ∃ (U : X.affineOpens) (V : Y.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1), y ∈ V.1 ∧
      letI : Algebra Γ(X, U.1) Γ(Y, V.1) := (f.appLE U V hVU).hom.toAlgebra
      ∀ F : FiniteOpenFactorization.{u, u, u} Γ(X, U.1) Γ(Y, V.1),
        Module.Invertible Γ(Y, V.1) (dualizingModule F)
```

## Tag 0FK8, an example

[Tag 0FK8](https://stacks.math.columbia.edu/tag/0FK8) in the Stacks Project.

**`AlgebraicGeometry.MultiIndex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L64). The attribute's comment: “the multi-index set”.

> The finite set of multi-indices in `n` variables having total degree at most `d`.

```lean
abbrev MultiIndex (n d : ℕ)
```

**`AlgebraicGeometry.universalCoefficientRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L80). The attribute's comment: “the universal coefficient ring”.

> The polynomial ring `A = ℤ[a_{i,E}]` of universal coefficients.

```lean
abbrev universalCoefficientRing (n d : ℕ)
```

**`AlgebraicGeometry.universalPolynomial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L90). The attribute's comment: “the universal polynomials”.

> The universal polynomial `f_i = ∑_E a_{i,E} x^E`.

```lean
def universalPolynomial (n d : ℕ) (i : Fin n) :
    MvPolynomial (Fin n) (universalCoefficientRing n d)
```

**`AlgebraicGeometry.universalQuotientRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L102). The attribute's comment: “the universal quotient algebra”.

> The universal quotient algebra `B = A[x₁, …, xₙ]/(f₁, …, fₙ)`.

```lean
abbrev universalQuotientRing (n d : ℕ)
```

**`AlgebraicGeometry.universalBaseScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L107). The attribute's comment: “the coefficient scheme X\_\{n,d}”.

> The coefficient scheme `X_{n,d} = Spec(A)`.

```lean
def universalBaseScheme (n d : ℕ) [NeZero n] [NeZero d] : Scheme
```

**`AlgebraicGeometry.universalAmbientScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L112). The attribute's comment: “the ambient scheme Spec(B)”.

> The affine scheme `Spec(B)` before restriction to its quasi-finite locus.

```lean
def universalAmbientScheme (n d : ℕ) [NeZero n] [NeZero d] : Scheme
```

**`AlgebraicGeometry.universalAmbientMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L117). The attribute's comment: “the ambient morphism Spec(B) ⟶ Spec(A)”.

> The morphism `Spec(B) ⟶ Spec(A)` induced by the universal algebra structure.

```lean
def universalAmbientMorphism (n d : ℕ) [NeZero n] [NeZero d] :
    universalAmbientScheme n d ⟶ universalBaseScheme n d
```

**`AlgebraicGeometry.universalQuasiFiniteOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L132). The attribute's comment: “the maximal quasi-finite open”.

> The maximal open of `Spec(B)` on which the universal algebra is quasi-finite over `A`.

```lean
def universalQuasiFiniteOpen (n d : ℕ) [NeZero n] [NeZero d] :
    (universalAmbientScheme n d).Opens
```

**`AlgebraicGeometry.mem_universalQuasiFiniteOpen_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L139). The attribute's comment: “the points of the maximal quasi-finite open”.

> A point lies in the universal quasi-finite open exactly when the ambient morphism is
> quasi-finite at that point in the sense of Tag 01TD.

```lean
theorem mem_universalQuasiFiniteOpen_iff
    (n d : ℕ) [NeZero n] [NeZero d] (x : universalAmbientScheme n d) :
    x ∈ universalQuasiFiniteOpen n d ↔
      quasiFiniteAt (universalAmbientMorphism n d) x
```

**`AlgebraicGeometry.universalQuasiFiniteScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L157). The attribute's comment: “the open subscheme Y\_\{n,d}”.

> The universal open subscheme `Y_{n,d}`.

```lean
def universalQuasiFiniteScheme (n d : ℕ) [NeZero n] [NeZero d] : Scheme
```

**`AlgebraicGeometry.universalQuasiFiniteMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L162). The attribute's comment: “the morphism Y\_\{n,d} ⟶ X\_\{n,d}”.

> The restriction `Y_{n,d} ⟶ X_{n,d}` of the universal affine family.

```lean
def universalQuasiFiniteMorphism (n d : ℕ) [NeZero n] [NeZero d] :
    universalQuasiFiniteScheme n d ⟶ universalBaseScheme n d
```

**`AlgebraicGeometry.universalQuasiFiniteMorphism_locallyOfFiniteType`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L168). The attribute's comment: “the restricted morphism is locally of finite type”.

> The morphism `Y_{n,d} ⟶ X_{n,d}` is locally of finite type.

```lean
instance universalQuasiFiniteMorphism_locallyOfFiniteType
    (n d : ℕ) [NeZero n] [NeZero d] :
    LocallyOfFiniteType (universalQuasiFiniteMorphism n d)
```

**`AlgebraicGeometry.universalQuasiFiniteMorphism_quasiCompact`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L177). The attribute's comment: “the restricted morphism is quasi-compact”.

> The morphism `Y_{n,d} ⟶ X_{n,d}` is quasi-compact.

```lean
instance universalQuasiFiniteMorphism_quasiCompact
    (n d : ℕ) [NeZero n] [NeZero d] :
    QuasiCompact (universalQuasiFiniteMorphism n d)
```

**`AlgebraicGeometry.universalQuasiFiniteMorphism_locallyQuasiFinite`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L193). The attribute's comment: “the restricted morphism is locally quasi-finite”.

> The morphism `Y_{n,d} ⟶ X_{n,d}` is locally quasi-finite.

```lean
instance universalQuasiFiniteMorphism_locallyQuasiFinite
    (n d : ℕ) [NeZero n] [NeZero d] :
    LocallyQuasiFinite (universalQuasiFiniteMorphism n d)
```

**`AlgebraicGeometry.universalQuasiFiniteOpen_greatest`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L203). The attribute's comment: “maximality of the quasi-finite open”.

> `Y_{n,d}` is the greatest open subscheme of `Spec(B)` on which the restriction of
> the ambient morphism is locally quasi-finite.

```lean
theorem universalQuasiFiniteOpen_greatest
    (n d : ℕ) [NeZero n] [NeZero d] (U : (universalAmbientScheme n d).Opens)
    [LocallyQuasiFinite (U.ι ≫ universalAmbientMorphism n d)] :
    U ≤ universalQuasiFiniteOpen n d
```

## Tag 0FK9, a lemma

[Tag 0FK9](https://stacks.math.columbia.edu/tag/0FK9) in the Stacks Project.

**`AlgebraicGeometry.universalBaseScheme_irreducibleSpace`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean#L77). The attribute's comment: “x\_irreducible”.

> The universal coefficient scheme `X_{n,d}` is irreducible.

```lean
instance universalBaseScheme_irreducibleSpace (n d : ℕ) [NeZero n] [NeZero d] :
    IrreducibleSpace (universalBaseScheme n d)
```

**`AlgebraicGeometry.universalBaseScheme_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean#L84). The attribute's comment: “x\_regular”.

> The universal coefficient scheme `X_{n,d}` is regular.

```lean
theorem universalBaseScheme_isRegular (n d : ℕ) [NeZero n] [NeZero d] :
    IsRegular (universalBaseScheme n d)
```

**`AlgebraicGeometry.universalQuasiFiniteScheme_irreducibleSpace`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean#L95). The attribute's comment: “y\_irreducible”.

> The universal quasi-finite open subscheme `Y_{n,d}` is irreducible.

```lean
instance universalQuasiFiniteScheme_irreducibleSpace
    (n d : ℕ) [NeZero n] [NeZero d] :
    IrreducibleSpace (universalQuasiFiniteScheme n d)
```

**`AlgebraicGeometry.universalQuasiFiniteScheme_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean#L420). The attribute's comment: “y\_regular”.

> The universal quasi-finite open subscheme `Y_{n,d}` is regular.

```lean
theorem universalQuasiFiniteScheme_isRegular (n d : ℕ) [NeZero n] [NeZero d] :
    IsRegular (universalQuasiFiniteScheme n d)
```

**`AlgebraicGeometry.universalQuasiFiniteMorphism_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean#L426). The attribute's comment: “syntomic”.

> The universal quasi-finite family `Y_{n,d} ⟶ X_{n,d}` is syntomic.

```lean
theorem universalQuasiFiniteMorphism_syntomic (n d : ℕ) [NeZero n] [NeZero d] :
    Syntomic (universalQuasiFiniteMorphism n d)
```

**`AlgebraicGeometry.exists_dense_opens_etale_universalQuasiFiniteMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean#L433). The attribute's comment: “dense\_etale\_open”.

> There is a dense open subscheme `V ⊆ Y_{n,d}` on which the universal quasi-finite family
> restricts to an étale morphism `V ⟶ X_{n,d}`.

```lean
theorem exists_dense_opens_etale_universalQuasiFiniteMorphism
    (n d : ℕ) [NeZero n] [NeZero d] :
    ∃ V : (universalQuasiFiniteScheme n d).Opens,
      Dense (V : Set (universalQuasiFiniteScheme n d)) ∧
        Etale (V.ι ≫ universalQuasiFiniteMorphism n d)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.universalQuasiFiniteMorphism_locallyQuasiFinite`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamily.lean#L193), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyProperties.lean#L72) (StacksFrontier): “locally\_quasi\_finite”.

## Tag 0FKA, a lemma

[Tag 0FKA](https://stacks.math.columbia.edu/tag/0FKA) in the Stacks Project.

**`AlgebraicGeometry.exists_isPullback_universalQuasiFiniteMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyBaseChange.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/QuasiFiniteSyntomic/UniversalFamilyBaseChange.lean#L261). The attribute's comment: “stated for schemes in the universe of the universal family `Y_{n, d} ⟶ X_{n, d}` of Example 0FK8, which is built from a polynomial ring over `ℤ` and so lives in `Scheme.{0}`.”.

> **Stacks Project, Tag 0FKA.** Let `f : Y ⟶ X` be a morphism of schemes satisfying the
> equivalent conditions of Stacks 0BWE. Then every point `y` of `Y` has opens `y ∈ V ⊆ Y` and
> `U ⊆ X` with `f(V) ⊆ U`, together with positive integers `n` and `d` and a commutative diagram
> whose right-hand square, over the family `Y_{n, d} ⟶ X_{n, d}` of Example 0FK8, is cartesian.

```lean
theorem exists_isPullback_universalQuasiFiniteMorphism {Y X : Scheme.{0}} {f : Y ⟶ X}
    (hqf : LocallyQuasiFinite f) (hsyn : Syntomic f) (y : Y) :
    ∃ (U : X.Opens) (V : Y.Opens) (_ : y ∈ V) (hVU : V ≤ f ⁻¹ᵁ U) (n d : ℕ)
      (_ : NeZero n) (_ : NeZero d) (p : U.toScheme ⟶ universalBaseScheme n d)
      (q : V.toScheme ⟶ universalQuasiFiniteScheme n d),
      IsPullback (f.resLE U V hVU) q p (universalQuasiFiniteMorphism n d)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.10, Tag 0DWJ](https://stacks.math.columbia.edu/tag/0DWJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
