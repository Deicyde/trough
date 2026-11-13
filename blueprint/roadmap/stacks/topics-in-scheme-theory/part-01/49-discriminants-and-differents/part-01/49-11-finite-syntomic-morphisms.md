---
declaration: section
origin: cited
lean: AlgebraicGeometry.finite_syntomic_tfae, AlgebraicGeometry.flat_and_isLocalCompleteIntersectionMorphism_of_finite_syntomic, AlgebraicGeometry.locallyOfFinitePresentation_and_lci_fibers_of_finite_flat_lci, AlgebraicGeometry.finite_syntomic_of_finite_flat_lci_fibers, AlgebraicGeometry.finite_syntomic_of_hasAffineSquarePresentation, AlgebraicGeometry.hasAffineSquarePresentation_of_finite_syntomic, AlgebraicGeometry.finite_flat_lfp_and_hasTorAmplitude_of_finite_syntomic, AlgebraicGeometry.finite_flat_lfp_and_isPerfect_and_hasTorAmplitude_of_finite_syntomic
statement: formalized
proof: formalized
---

# 49.11 Finite syntomic morphisms

Section 49.11 of the Stacks Project, [Tag 0FKX](https://stacks.math.columbia.edu/tag/0FKX). 7 tags here are carried by 30 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FKY, a lemma

[Tag 0FKY](https://stacks.math.columbia.edu/tag/0FKY) in the Stacks Project.

**`AlgebraicGeometry.finite_syntomic_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Finite.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Finite.lean#L148). The attribute's comment: “the equivalence of (1), (2) and (3). Parts (5) and (6), the conditions on the naive cotangent complex, are not among the three conditions of this equivalence; for those see `StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiniteNaiveCotangent.lean`.”.

> For a morphism of schemes `f : Y ⟶ X` the following are equivalent:
>
> 1. `f` is finite and syntomic;
> 2. `f` is finite, flat, and a local complete intersection morphism;
> 3. `f` is finite, flat, locally of finite presentation, and all the fibres of `f` are local
>    complete intersections over the residue fields of their base points.

```lean
theorem finite_syntomic_tfae {Y X : Scheme.{u}} (f : Y ⟶ X) :
    List.TFAE [
      IsFinite f ∧ Syntomic f,
      (IsFinite f ∧ Flat f) ∧ IsLocalCompleteIntersectionMorphism f,
      ((IsFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
        ∀ x : X, IsLocalCompleteIntersectionOverField (f.fiberToSpecResidueField x)]
```

**`AlgebraicGeometry.flat_and_isLocalCompleteIntersectionMorphism_of_finite_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Finite.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Finite.lean#L169). The attribute's comment: “the implication (1) ⟹ (2)”.

> A finite syntomic morphism of schemes is flat and a local complete intersection morphism.

```lean
theorem flat_and_isLocalCompleteIntersectionMorphism_of_finite_syntomic {Y X : Scheme.{u}}
    {f : Y ⟶ X} (h : IsFinite f ∧ Syntomic f) :
    (IsFinite f ∧ Flat f) ∧ IsLocalCompleteIntersectionMorphism f
```

**`AlgebraicGeometry.locallyOfFinitePresentation_and_lci_fibers_of_finite_flat_lci`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Finite.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Finite.lean#L178). The attribute's comment: “the implication (2) ⟹ (3)”. References: SGA 6 VIII (1.4), “special case”.

> A finite flat local complete intersection morphism of schemes is locally of finite presentation
> and all of its fibres are local complete intersections over the residue fields of their base
> points.

```lean
theorem locallyOfFinitePresentation_and_lci_fibers_of_finite_flat_lci {Y X : Scheme.{u}}
    {f : Y ⟶ X} (h : (IsFinite f ∧ Flat f) ∧ IsLocalCompleteIntersectionMorphism f) :
    ((IsFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
      ∀ x : X, IsLocalCompleteIntersectionOverField (f.fiberToSpecResidueField x)
```

**`AlgebraicGeometry.finite_syntomic_of_finite_flat_lci_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Finite.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Finite.lean#L188). The attribute's comment: “the implication (3) ⟹ (1)”.

> A finite flat morphism of schemes which is locally of finite presentation and all of whose
> fibres are local complete intersections over the residue fields of their base points is
> syntomic.

```lean
theorem finite_syntomic_of_finite_flat_lci_fibers {Y X : Scheme.{u}} {f : Y ⟶ X}
    (h : ((IsFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
      ∀ x : X, IsLocalCompleteIntersectionOverField (f.fiberToSpecResidueField x)) :
    IsFinite f ∧ Syntomic f
```

**`AlgebraicGeometry.finite_syntomic_of_hasAffineSquarePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Finite.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Finite.lean#L199). The attribute's comment: “the implication (4) ⟹ (1)”.

> A finite morphism of schemes whose preimages of suitable affine opens of the target are cut out
> by as many equations as variables is syntomic.

```lean
theorem finite_syntomic_of_hasAffineSquarePresentation {Y X : Scheme.{u}} {f : Y ⟶ X}
    (h : IsFinite f ∧ HasAffineSquarePresentation f) : IsFinite f ∧ Syntomic f
```

**`AlgebraicGeometry.hasAffineSquarePresentation_of_finite_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Finite.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Finite.lean#L249). The attribute's comment: “the implication (1) ⟹ (4)”.

> A finite syntomic morphism of schemes is, over a suitable affine open neighbourhood of every
> point of the target, cut out of a polynomial ring by as many equations as variables.

```lean
theorem hasAffineSquarePresentation_of_finite_syntomic {Y X : Scheme.{u}} {f : Y ⟶ X}
    (h : IsFinite f ∧ Syntomic f) : IsFinite f ∧ HasAffineSquarePresentation f
```

**`AlgebraicGeometry.finite_flat_lfp_and_hasTorAmplitude_of_finite_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiniteNaiveCotangent.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiniteNaiveCotangent.lean#L92). The attribute's comment: “the implication (1) ⟹ (5)”.

> **Stacks Project, Tag 0FKY, the implication (1) ⟹ (5).** A finite syntomic morphism of
> schemes is finite, flat and locally of finite presentation, and `NL_{Y/X}` has Tor amplitude in
> `[-1, 0]`.

```lean
theorem finite_flat_lfp_and_hasTorAmplitude_of_finite_syntomic {Y X : Scheme.{u}} {f : Y ⟶ X}
    (h : IsFinite f ∧ Syntomic f) :
    ((IsFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
      Stacks.Cohomology.TorAmplitude.HasTorAmplitude Y.toRingedSpace
        (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0
```

**`AlgebraicGeometry.finite_flat_lfp_and_isPerfect_and_hasTorAmplitude_of_finite_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiniteNaiveCotangent.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiniteNaiveCotangent.lean#L105). The attribute's comment: “the implication (1) ⟹ (6)”.

> **Stacks Project, Tag 0FKY, the implication (1) ⟹ (6).** A finite syntomic morphism of schemes
> is finite, flat and locally of finite presentation, and `NL_{Y/X}` is a perfect object of
> `D(𝒪_Y)` of rank zero with Tor amplitude in `[-1, 0]`.

```lean
theorem finite_flat_lfp_and_isPerfect_and_hasTorAmplitude_of_finite_syntomic {Y X : Scheme.{u}}
    {f : Y ⟶ X} (h : IsFinite f ∧ Syntomic f) :
    ((IsFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
      (Stacks.Cohomology.PerfectComplexes.IsPerfect (X := Y.toRingedSpace)
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
        DeterminantTwoTerm.IsRankZeroScheme
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
        Stacks.Cohomology.TorAmplitude.HasTorAmplitude Y.toRingedSpace
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0)
```

**`AlgebraicGeometry.finite_syntomic_of_finite_flat_lfp_of_hasTorAmplitude`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiniteNaiveCotangent.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiniteNaiveCotangent.lean#L163). The attribute's comment: “the implication (5) ⟹ (1)”.

> **Stacks Project, Tag 0FKY, the implication (5) ⟹ (1).** A finite flat morphism of schemes
> which is locally of finite presentation and whose naive cotangent complex has Tor amplitude in
> `[-1, 0]` is syntomic.
>
> A finite morphism is affine, so the preimage of an affine open `U` of the target is an affine
> open `V`; there the hypotheses say that `Γ(Y, U) → Γ(X, V)` is flat of finite presentation with
> `NL_{Γ(X, V)/Γ(Y, U)}` of Tor amplitude in `[-1, 0]`, and that map is syntomic by Stacks
> 0FJV.

```lean
theorem finite_syntomic_of_finite_flat_lfp_of_hasTorAmplitude {Y X : Scheme.{u}} {f : Y ⟶ X}
    (h : ((IsFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
      Stacks.Cohomology.TorAmplitude.HasTorAmplitude Y.toRingedSpace
        (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0) :
    IsFinite f ∧ Syntomic f
```

**`AlgebraicGeometry.finite_syntomic_iff_hasTorAmplitude_naiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiniteNaiveCotangent.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiniteNaiveCotangent.lean#L202). The attribute's comment: “the equivalence of (1) and (5)”.

> **Stacks Project, Tag 0FKY, the equivalence of (1) and (5).** A morphism of schemes is finite
> and syntomic if and only if it is finite, flat and locally of finite presentation with `NL_{Y/X}`
> of Tor amplitude in `[-1, 0]`.

```lean
theorem finite_syntomic_iff_hasTorAmplitude_naiveCotangentComplex {Y X : Scheme.{u}}
    (f : Y ⟶ X) :
    (IsFinite f ∧ Syntomic f) ↔
      (((IsFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
        Stacks.Cohomology.TorAmplitude.HasTorAmplitude Y.toRingedSpace
          (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0)
```

**`AlgebraicGeometry.finite_syntomic_iff_isPerfect_and_hasTorAmplitude_naiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiniteNaiveCotangent.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiniteNaiveCotangent.lean#L217). The attribute's comment: “the equivalence of (1) and (6)”. References: SGA 6 0 (4.3), “special case”; SGA 6 VIII (2.4), “Forward direction”.

> **Stacks Project, Tag 0FKY, the equivalence of (1) and (6).** A morphism of schemes is finite
> and syntomic if and only if it is finite, flat and locally of finite presentation with `NL_{Y/X}`
> a perfect object of `D(𝒪_Y)` of rank zero with Tor amplitude in `[-1, 0]`.

```lean
theorem finite_syntomic_iff_isPerfect_and_hasTorAmplitude_naiveCotangentComplex
    {Y X : Scheme.{u}} (f : Y ⟶ X) :
    (IsFinite f ∧ Syntomic f) ↔
      (((IsFinite f ∧ Flat f) ∧ LocallyOfFinitePresentation f) ∧
        (Stacks.Cohomology.PerfectComplexes.IsPerfect (X := Y.toRingedSpace)
            (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
          DeterminantTwoTerm.IsRankZeroScheme
            (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) ∧
          Stacks.Cohomology.TorAmplitude.HasTorAmplitude Y.toRingedSpace
            (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0))
```

## Tag 0FKZ, an example

[Tag 0FKZ](https://stacks.math.columbia.edu/tag/0FKZ) in the Stacks Project.

**`AlgebraicGeometry.universalAlgebraStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/AlgebraAxioms.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/AlgebraAxioms.lean#L79). The attribute's comment: “algebra\_axioms”.

> The defining relations on the universal structure constants equip `B_d`
> with its prescribed commutative `A_d`-algebra structure.

```lean
noncomputable def universalAlgebraStructure (d : ℕ) [NeZero d] :
    UniversalAlgebraStructure d
```

**`AlgebraicGeometry.universalFamily_isFiniteLocallyFreeOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/Rank.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/Rank.lean#L159). The attribute's comment: “finite\_free\_rank”.

> The universal affine family of rank-`d` commutative algebras is finite
> locally free of rank `d`.

```lean
theorem universalFamily_isFiniteLocallyFreeOfRank (d : ℕ) [NeZero d] :
    Stacks.Morphisms.IsFiniteLocallyFreeOfRank
      (universalFamily.{u} d (universalAlgebraStructure d)) d
```

**`AlgebraicGeometry.UniversalFiniteFreeModule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean#L96). The attribute's comment: “universal\_finite\_free\_family”.

> The free carrier `B_d`, written using its coefficients in the distinguished basis.

```lean
structure UniversalFiniteFreeModule (d : ℕ) [NeZero d]
```

**`AlgebraicGeometry.universalBasisVector`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean#L103). The attribute's comment: “universal\_finite\_free\_family”.

> The distinguished basis vector `e_i`.

```lean
def universalBasisVector (d : ℕ) [NeZero d] (i : Fin d) :
    UniversalFiniteFreeModule d
```

**`AlgebraicGeometry.universalUnit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean#L109). The attribute's comment: “universal\_finite\_free\_family”.

> The prescribed unit `e_1` (indexed by `0` in `Fin d`).

```lean
def universalUnit (d : ℕ) [NeZero d] : UniversalFiniteFreeModule d
```

**`AlgebraicGeometry.universalMultiplication`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean#L114). The attribute's comment: “universal\_finite\_free\_family”.

> Multiplication on `B_d` prescribed by the universal structure constants.

```lean
def universalMultiplication (d : ℕ) [NeZero d]
    (x y : UniversalFiniteFreeModule d) : UniversalFiniteFreeModule d
```

**`AlgebraicGeometry.universalTotalScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean#L153). The attribute's comment: “universal\_finite\_free\_family”.

> The affine total space `Y_d = Spec(B_d)`, after equipping the prescribed
> multiplication table with its commutative-ring structure.

```lean
def universalTotalScheme (d : ℕ) [NeZero d] (s : UniversalAlgebraStructure d) :
    Scheme.{u}
```

**`AlgebraicGeometry.universalFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean#L160). The attribute's comment: “universal\_finite\_free\_family”.

> The affine morphism `pi_d : Y_d ⟶ X_d` induced by the universal algebra map.

```lean
def universalFamily (d : ℕ) [NeZero d] (s : UniversalAlgebraStructure d) :
    universalTotalScheme.{u} d s ⟶
      scheme.{u} d
```

Declarations registered for the tag:

- [`universalRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=universalRing#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean#L53) (StacksFrontier): “universal\_finite\_free\_family”.
- [`scheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=scheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalFamily.lean#L54) (StacksFrontier): “universal\_finite\_free\_family”.

## Tag 0FL0, a lemma

[Tag 0FL0](https://stacks.math.columbia.edu/tag/0FL0) in the Stacks Project.

**`AlgebraicGeometry.universalSyntomicOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalSyntomicOpen.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalSyntomicOpen.lean#L90). The attribute's comment: “the open subscheme”.

> **Stacks Project, Tag 0FL0.** The open subscheme of the base `X_d` of the universal finite
> free family of rank `d` over which the family is syntomic.
>
> It is the interior of `AlgebraicGeometry.universalSyntomicLocus`; that set is already open, by
> `AlgebraicGeometry.universalSyntomicLocus_isOpen`.

```lean
def universalSyntomicOpen : (scheme.{u} d).Opens
```

**`AlgebraicGeometry.factorsThrough_universalSyntomicOpen_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalSyntomicOpen.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalSyntomicOpen.lean#L120). The attribute's comment: “universal property”.

> **Stacks Project, Tag 0FL0.** A morphism `g : T ⟶ X_d` to the base of the universal finite
> free family of rank `d` factors through the open subscheme
> `AlgebraicGeometry.universalSyntomicOpen` exactly when the base change of the family along `g` is
> syntomic.

```lean
theorem factorsThrough_universalSyntomicOpen_iff (T : Scheme.{u})
    (g : T ⟶ scheme.{u} d) :
    (∃ ĝ : T ⟶ (universalSyntomicOpen.{u} d).toScheme,
        ĝ ≫ (universalSyntomicOpen.{u} d).ι = g) ↔
      Syntomic (pullback.snd (universalFamily.{u} d (universalAlgebraStructure d)) g)
```

## Tag 0FL1, a lemma

[Tag 0FL1](https://stacks.math.columbia.edu/tag/0FL1) in the Stacks Project.

**`AlgebraicGeometry.universalSyntomicOpen_smooth_uLift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalSmooth.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalSmooth.lean#L237).

> **Stacks Project, Tag 0FL1.** The open subscheme `U_d` of the base of the universal finite
> free family of rank `d` over which that family is syntomic (Tag 0FL0) is smooth over the
> terminal scheme `Spec(ULift ZZ)`, which is `Spec(ZZ)` in the universe of the test schemes.

```lean
public instance universalSyntomicOpen_smooth_uLift (d : ℕ) [NeZero d] :
    Smooth (specULiftZIsTerminal.from (universalSyntomicOpen.{u} d).toScheme)
```

**`AlgebraicGeometry.universalSyntomicOpen_smooth`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalSmooth.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalSmooth.lean#L290).

> **Stacks Project, Tag 0FL1.** The open subscheme `U_d` of Tag 0FL0 is smooth over
> `Spec(ZZ)`, in the literal form of the source: the structure morphism to the spectrum of the
> integers themselves.

```lean
public instance universalSyntomicOpen_smooth (d : ℕ) [NeZero d] :
    Smooth (specZIsTerminal.from (universalSyntomicOpen d).toScheme)
```

## Tag 0FL2, a lemma

[Tag 0FL2](https://stacks.math.columbia.edu/tag/0FL2) in the Stacks Project.

**`AlgebraicGeometry.universalEtaleOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalEtaleOpen.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalEtaleOpen.lean#L267). The attribute's comment: “the étale open subscheme”.

> **Stacks Project, Tag 0FL2.** The open subscheme `U'_d` of the base `X_d` of the universal
> finite free family of rank `d` over which the family is étale.
>
> It is the interior of `AlgebraicGeometry.universalEtaleLocus`; that set is already open, by
> `AlgebraicGeometry.universalEtaleLocus_isOpen`.

```lean
def universalEtaleOpen : (scheme.{u} d).Opens
```

**`AlgebraicGeometry.factorsThrough_universalEtaleOpen_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalEtaleOpen.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalEtaleOpen.lean#L299). The attribute's comment: “universal property of the étale open”.

> **Stacks Project, Tag 0FL2.** A morphism `g : T ⟶ X_d` to the base of the universal finite
> free family of rank `d` factors through the open subscheme
> `AlgebraicGeometry.universalEtaleOpen` exactly when the base change of the family along `g` is
> étale.

```lean
theorem factorsThrough_universalEtaleOpen_iff (T : Scheme.{u}) (g : T ⟶ scheme.{u} d) :
    (∃ ĝ : T ⟶ (universalEtaleOpen.{u} d).toScheme,
        ĝ ≫ (universalEtaleOpen.{u} d).ι = g) ↔
      Etale (pullback.snd (universalFamily.{u} d (universalAlgebraStructure d)) g)
```

**`AlgebraicGeometry.universalEtaleOpen_le_universalSyntomicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalEtaleOpen.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalEtaleOpen.lean#L339). The attribute's comment: “containment in the syntomic open”.

> **Stacks Project, Tag 0FL2.** The open subscheme over which the universal finite free family
> of rank `d` is étale is contained in the open subscheme over which it is syntomic, because the
> family is syntomic at every point at which it is étale.

```lean
theorem universalEtaleOpen_le_universalSyntomicOpen :
    universalEtaleOpen.{u} d ≤ universalSyntomicOpen.{u} d
```

**`AlgebraicGeometry.dense_universalEtaleOpen_in_universalSyntomicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalEtaleOpen.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalEtaleOpen.lean#L502). The attribute's comment: “density in the syntomic open”.

> **Stacks Project, Tag 0FL2.** The open subscheme `U'_d` of the base of the universal finite
> free family of rank `d` over which that family is étale is dense in the open subscheme `U_d` over
> which it is syntomic.

```lean
theorem dense_universalEtaleOpen_in_universalSyntomicOpen :
    Dense ((universalSyntomicOpen.{u} d).ι ⁻¹'
      (↑(universalEtaleOpen.{u} d) : Set (scheme.{u} d)))
```

## Tag 0FL3, a remark

[Tag 0FL3](https://stacks.math.columbia.edu/tag/0FL3) in the Stacks Project.

**`AlgebraicGeometry.universalSyntomicPreimage_smooth_and_not_smooth_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalSectionNotSmooth.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/UniversalSectionNotSmooth.lean#L125). The attribute's comment: “V\_d = pi\_d^\{-1}(U\_d) is smooth over Spec(Z), for the universal finite free family pi\_d of rank d of Tag 0FKZ and the open U\_d of Tag 0FL0; and for d ≥ 2 the morphism V\_d → U\_d, the restriction of pi\_d over U\_d, is not smooth. The deformation problem of the remark is Algebra.exists\_finite\_syntomic\_section\_lift.”.

> **Stacks Project, Tag 0FL3.** Let `pi_d : Y_d ⟶ X_d` be the universal finite free family of
> rank `d` (Tag 0FKZ) and `U_d ⊆ X_d` the maximal open over which it is finite syntomic (Tag 0FL0).
> Then `V_d = pi_d^{-1}(U_d)` is smooth over `Spec(ZZ)`, while for `d ≥ 2` the morphism
> `V_d ⟶ U_d` is not smooth.

```lean
theorem universalSyntomicPreimage_smooth_and_not_smooth_restrict (d : ℕ) [NeZero d] :
    Smooth (specZIsTerminal.from (universalSyntomicPreimage d).toScheme) ∧
      (2 ≤ d → ¬ Smooth (universalFamily d (universalAlgebraStructure d) ∣_
        universalSyntomicOpen d))
```

**`Algebra.exists_finite_syntomic_section_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Syntomic/SectionedDeformation.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Syntomic/SectionedDeformation.lean#L401). The attribute's comment: “the deformation problem the remark reduces the smoothness of V\_d over Z to, and the remark's solution of it: along a surjection C' → C with nilpotent kernel onto a nonzero artinian ring (a small extension of artinian local rings in particular) a finite syntomic C-algebra with a section lifts to a finite syntomic C'-algebra with a section whose tensor product with C recovers it, the reduction being a surjection B' → B with kernel I·B' that matches the two sections.”.

> **Stacks Project, Tag 0FL3,** the deformation problem the remark reduces the smoothness of
> `V_d` over `Z` to, and its solution. Along a surjection `C' → C` with nilpotent kernel `I` onto a
> nonzero artinian ring — a small extension, in particular — a finite syntomic `C`-algebra `B` with
> a section `B → C` lifts to a finite syntomic `C'`-algebra `B'` with a section `B' → C'`, together
> with a surjection `B' → B` with kernel `IB'` carrying the one section to the other: the tensor
> product of `B' → C'` with `C` is `B → C`.

```lean
theorem Algebra.exists_finite_syntomic_section_lift
    {C' C B : Type u} [CommRing C'] [CommRing C] [CommRing B] [Algebra C' C] [Algebra C B]
    [IsArtinianRing C] [Nontrivial C] [Algebra.Syntomic C B] [Module.Finite C B]
    (hsurj : Function.Surjective (algebraMap C' C))
    (hnil : IsNilpotent (RingHom.ker (algebraMap C' C)))
    (σ : B →ₐ[C] C) :
    ∃ (B' : Type u) (_ : CommRing B') (_ : Algebra C' B'),
      Algebra.Syntomic C' B' ∧ Module.Finite C' B' ∧
        ∃ (sec : B' →ₐ[C'] C') (φ : B' →+* B),
          Function.Surjective φ ∧
          RingHom.ker φ = Ideal.map (algebraMap C' B') (RingHom.ker (algebraMap C' C)) ∧
          (∀ c : C', φ (algebraMap C' B' c) = algebraMap C B (algebraMap C' C c)) ∧
          (∀ b : B', σ (φ b) = algebraMap C' C (sec b))
```

## Tag 0FL4, a lemma

[Tag 0FL4](https://stacks.math.columbia.edu/tag/0FL4) in the Stacks Project.

**`AlgebraicGeometry.exists_isPullback_universalFamily_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/LocalStructure.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/FiniteSyntomicMorphisms/LocalStructure.lean#L147). The attribute's comment: “the diagram, at a point of the image of `f`: the integer `d`, the open `U ∋ x` with `V = f⁻¹(U)`, the morphism `U ⟶ U_d` into the open subscheme of Lemma 0FL0, and the cartesian middle square over the restriction of `π_d` of Example 0FKZ to `V_d = π_d⁻¹(U_d)`. A point outside the image of `f` is excluded, and must be: the local rank of `f` there is `0`, whereas Example 0FKZ has `d ≥ 1`, so `π_d` is surjective and no base change of it along a morphism out of a nonempty `U` has empty fibres.”.

> **Stacks Project, Tag 0FL4.** For a finite syntomic morphism `f : Y ⟶ X` and a point `x` of
> `X` in the image of `f` there are an integer `d ≥ 1`, an open `U ∋ x` with preimage
> `V = f⁻¹(U)`, and a morphism `U ⟶ U_d` into the open subscheme of Tag 0FL0, for which the middle
> square of the source's diagram — `V ⟶ V_d = π_d^{-1}(U_d)` over `U ⟶ U_d` — is cartesian.

```lean
theorem exists_isPullback_universalFamily_restrict (hf : IsFinite f ∧ Syntomic f) (x : X)
    (hx : ∃ y : Y, f.base y = x) :
    ∃ (d : ℕ) (_ : NeZero d) (U : X.Opens) (_ : x ∈ U)
      (gU : U.toScheme ⟶ (universalSyntomicOpen.{u} d).toScheme)
      (q : (f ⁻¹ᵁ U).toScheme ⟶ (universalFamily.{u} d (universalAlgebraStructure d) ⁻¹ᵁ
        universalSyntomicOpen.{u} d).toScheme),
      IsPullback q (f ∣_ U)
        (universalFamily.{u} d (universalAlgebraStructure d) ∣_
          universalSyntomicOpen.{u} d) gU
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.11, Tag 0FKX](https://stacks.math.columbia.edu/tag/0FKX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
