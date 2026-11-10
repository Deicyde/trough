---
declaration: section
origin: cited
lean: AlgebraicGeometry.quasiFiniteAt, AlgebraicGeometry.quasiFiniteAt_iff_exists_affineOpens, AlgebraicGeometry.forall_quasiFiniteAt_iff, AlgebraicGeometry.quasiFinite_conditions_iff_isDiscrete_fibers, AlgebraicGeometry.LocallyOfFiniteType, AlgebraicGeometry.LocallyQuasiFinite, AlgebraicGeometry.QuasiCompact, AlgebraicGeometry.isClosed_asFiber_of_isAlgebraic_residueField
statement: formalized
proof: formalized
---

# 29.21 Quasi-finite morphisms

Section 29.21 of the Stacks Project, [Tag 01TC](https://stacks.math.columbia.edu/tag/01TC). 17 tags here are carried by 24 declarations of the repository (all in StacksFrontier) and 11 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01TD, a definition

[Tag 01TD](https://stacks.math.columbia.edu/tag/01TD) in the Stacks Project.

**`AlgebraicGeometry.quasiFiniteAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean#L68). The attribute's comment: “part (1)”.

> A morphism of schemes is quasi-finite at `x` if it is of finite type at `x` and its
> stalk map at `x` is quasi-finite.

```lean
public abbrev quasiFiniteAt {X S : Scheme.{u}} (f : X ⟶ S) (x : X) : Prop
```

**`AlgebraicGeometry.quasiFiniteAt_iff_exists_affineOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean#L75). The attribute's comment: “part (1), affine-neighbourhood characterization”.

> Quasi-finiteness at a point is equivalently witnessed on compatible affine
> neighbourhoods by a finite-type ring map which is quasi-finite at the corresponding
> prime.

```lean
public theorem quasiFiniteAt_iff_exists_affineOpens
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) :
    quasiFiniteAt f x ↔
      ∃ (U : S.affineOpens) (V : X.affineOpens) (hxV : x ∈ V.1)
        (hVU : V.1 ≤ f ⁻¹ᵁ U.1),
        (f.appLE U V hVU).hom.FiniteType ∧
          (f.appLE U V hVU).hom.QuasiFiniteAt
            (V.2.primeIdealOf ⟨x, hxV⟩).asIdeal
```

**`AlgebraicGeometry.forall_quasiFiniteAt_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean#L130). The attribute's comment: “part (2), pointwise characterization”.

> A morphism is quasi-finite at every point exactly when it is locally of finite type
> and locally quasi-finite.

```lean
public theorem forall_quasiFiniteAt_iff {X S : Scheme.{u}} (f : X ⟶ S) :
    (∀ x, quasiFiniteAt f x) ↔
      (AlgebraicGeometry.LocallyOfFiniteType f ∧
        AlgebraicGeometry.LocallyQuasiFinite f)
```

**`AlgebraicGeometry.quasiFinite_conditions_iff_isDiscrete_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean#L154). The attribute's comment: “part (3), fiber characterization”.

> The conditions defining a quasi-finite morphism can be expressed either by local
> quasi-finiteness or by discreteness of every set-theoretic fiber.

```lean
public theorem quasiFinite_conditions_iff_isDiscrete_fibers
    {X S : Scheme.{u}} (f : X ⟶ S) :
    ((LocallyOfFiniteType f ∧ QuasiCompact f) ∧ LocallyQuasiFinite f) ↔
      ((LocallyOfFiniteType f ∧ QuasiCompact f) ∧
        ∀ s, IsDiscrete (f ⁻¹' {s}))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.LocallyOfFiniteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyOfFiniteType#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean#L100) (StacksFrontier): “the local finite-type condition in parts (2) and (3)”. References: EGA I (6.3.1), “partial”; EGA I (6.6.2); EGA IV (1.3.2); SGA 3 VIB (1.3); SGA 4 Vbis (5.2.0), “partial”.
- [`AlgebraicGeometry.LocallyQuasiFinite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyQuasiFinite#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean#L103) (StacksFrontier): “the fiber-isolation condition in parts (2) and (3)”.
- [`AlgebraicGeometry.QuasiCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompact#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean#L106) (StacksFrontier): “the quasi-compact condition in part (3)”. References: EGA 0 (9.1.1), “special case”; EGA I (6.6.1); EGA IV (1.1.1); SGA 1 XIII (1.5); SGA 4 Vbis (4.2.0), “partial”; SGA 6 II (3.0); SGA 7 VII (1.3.8), “partial”.

## Tag 01TE, a lemma

[Tag 01TE](https://stacks.math.columbia.edu/tag/01TE) in the Stacks Project.

**`AlgebraicGeometry.isClosed_asFiber_of_isAlgebraic_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/ResidueField.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/ResidueField.lean#L56). The attribute's comment: “part (1)”.

> A point whose residue field is algebraic over that of its image is closed in its fibre.

```lean
public theorem isClosed_asFiber_of_isAlgebraic_residueField (f : X ⟶ S) (x : X)
    (h : letI := (f.residueFieldMap x).hom.toAlgebra
      Algebra.IsAlgebraic (S.residueField (f x)) (X.residueField x)) :
    IsClosed ({f.asFiber x} : Set (f.fiber (f x)))
```

**`AlgebraicGeometry.isClosed_of_isAlgebraic_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/ResidueField.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/ResidueField.lean#L97). The attribute's comment: “part (2)”. References: EGA I (6.4.2), “sufficiency”.

> If the image of a point is closed and its residue field extension is algebraic, then the
> point is closed.

```lean
public theorem isClosed_of_isAlgebraic_residueField (f : X ⟶ S) (x : X)
    (h : letI := (f.residueFieldMap x).hom.toAlgebra
      Algebra.IsAlgebraic (S.residueField (f x)) (X.residueField x))
    (hs : IsClosed ({f x} : Set S)) : IsClosed ({x} : Set X)
```

## Tag 01TF, a lemma

[Tag 01TF](https://stacks.math.columbia.edu/tag/01TF) in the Stacks Project.

**`AlgebraicGeometry.isClosed_asFiber_iff_finite_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/ResidueField.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/ResidueField.lean#L109).

> A point of a fibre of a locally finite type morphism is closed exactly when its residue
> field is finite over the residue field of its image.

```lean
public theorem isClosed_asFiber_iff_finite_residueField (f : X ⟶ S) [LocallyOfFiniteType f]
    (x : X) :
    IsClosed ({f.asFiber x} : Set (f.fiber (f x))) ↔
      letI := (f.residueFieldMap x).hom.toAlgebra
      Module.Finite (S.residueField (f x)) (X.residueField x)
```

## Tag 053M, a lemma

[Tag 053M](https://stacks.math.columbia.edu/tag/053M) in the Stacks Project.

**`AlgebraicGeometry.isClosed_asFiber_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChange.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChange.lean#L269).

> A point above a point closed in its fibre remains closed in its fibre after
> base change of a locally finite type morphism.

```lean
public theorem isClosed_asFiber_of_isPullback
    {X S S' X' : Scheme.{u}} {f : X ⟶ S} {g : S' ⟶ S}
    {f' : X' ⟶ S'} {g' : X' ⟶ X} [LocallyOfFiniteType f]
    (sq : IsPullback g' f' f g) (x' : X')
    (hx : IsClosed ({f.asFiber (g' x')} : Set (f.fiber (f (g' x'))))) :
    IsClosed ({f'.asFiber x'} : Set (f'.fiber (f' x')))
```

## Tag 01TG, a lemma

[Tag 01TG](https://stacks.math.columbia.edu/tag/01TG) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.finite_residueField_of_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/StalkDimension.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/StalkDimension.lean#L142). The attribute's comment: “the hypothesis is the stalk half `Scheme.Hom.QuasiFiniteAt` of `AlgebraicGeometry.quasiFiniteAt`, so the finite-type half is not used”.

> At a point where a morphism of schemes is quasi-finite, the residue field of the source is a
> finite extension of the residue field of the image: the stalk map is quasi-finite, the residue
> field of the source is a quotient of the source stalk, and a quasi-finite algebra over a field is
> finite.

```lean
theorem Scheme.Hom.finite_residueField_of_quasiFiniteAt {X S : Scheme.{u}} (f : X ⟶ S) (x : X)
    (h : f.QuasiFiniteAt x) :
    letI := (f.residueFieldMap x).hom.toAlgebra
    Module.Finite (S.residueField (f x)) (X.residueField x)
```

## Tag 01TH, a lemma

[Tag 01TH](https://stacks.math.columbia.edu/tag/01TH) in the Stacks Project.

**`AlgebraicGeometry.quasiFiniteAt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Criteria.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Criteria.lean#L94). References: EGA II (6.2.2), “a) <=> c)”; EGA II (6.2.1).

> **Stacks Project, Tag 01TH.** For a morphism locally of finite type, quasi-finiteness at a
> point is equivalent to isolation of that point in the fibre, to the corresponding closedness
> and specialization condition, and to quasi-finiteness at the corresponding prime for every
> compatible pair of affine open neighbourhoods.

```lean
public theorem quasiFiniteAt_tfae {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (x : X) :
    List.TFAE [
      quasiFiniteAt f x,
      IsIsolatedPoint (f.asFiber x),
      IsClosed ({f.asFiber x} : Set (f.fiber (f x))) ∧
        (¬ ∃ x' : f.fiber (f x),
          x' ≠ f.asFiber x ∧ x' ⤳ f.asFiber x),
      ∀ (U : S.affineOpens) (V : X.affineOpens) (hxV : x ∈ V.1)
        (hVU : V.1 ≤ f ⁻¹ᵁ U.1),
        (f.appLE U V hVU).hom.QuasiFiniteAt
          (V.2.primeIdealOf ⟨x, hxV⟩).asIdeal]
```

## Tag 02NG, a lemma

[Tag 02NG](https://stacks.math.columbia.edu/tag/02NG) in the Stacks Project.

**`AlgebraicGeometry.finite_fiber_of_finite_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteFibre.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteFibre.lean#L72). The attribute's comment: “the fibre is finite”.

> **Stacks Project, Tag 02NG.** If the set-theoretic fibre of `f` over `s` is finite, then so
> is the scheme-theoretic fibre: the two are homeomorphic.

```lean
theorem finite_fiber_of_finite_preimage {X S : Scheme.{u}} (f : X ⟶ S) (s : S)
    (hfin : (f ⁻¹' {s}).Finite) : Finite (f.fiber s)
```

**`AlgebraicGeometry.discreteTopology_fiber_of_finite_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteFibre.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteFibre.lean#L81). The attribute's comment: “the fibre is discrete”.

> **Stacks Project, Tag 02NG.** A fibre of a morphism locally of finite type that is finite as
> a set is a discrete topological space: it is locally of finite type over the residue field at the
> base point, hence Jacobson, and a finite Jacobson space is discrete.

```lean
theorem discreteTopology_fiber_of_finite_preimage {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (s : S) (hfin : (f ⁻¹' {s}).Finite) :
    DiscreteTopology (f.fiber s)
```

**`AlgebraicGeometry.quasiFiniteAt_of_finite_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteFibre.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteFibre.lean#L91). The attribute's comment: “quasi-finite at every point over the base point”.

> **Stacks Project, Tag 02NG.** A morphism locally of finite type with finite fibre over `s` is
> quasi-finite at every point lying over `s`: the point is isolated in the fibre, because the fibre
> is discrete.

```lean
theorem quasiFiniteAt_of_finite_preimage {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (s : S) (hfin : (f ⁻¹' {s}).Finite) (x : X) (hx : f x = s) : quasiFiniteAt f x
```

## Tag 01TJ, a lemma

[Tag 01TJ](https://stacks.math.columbia.edu/tag/01TJ) in the Stacks Project.

Declarations registered for the tag:

- [`and_right_comm`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=and_right_comm#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean#L109) (StacksFrontier).

## Tag 02NH, a lemma

[Tag 02NH](https://stacks.math.columbia.edu/tag/02NH) in the Stacks Project.

**`AlgebraicGeometry.quasiFinite_conditions_iff_finite_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteFibre.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteFibre.lean#L100).

> **Stacks Project, Tag 02NH.** A morphism of schemes is quasi-finite exactly when it is
> locally of finite type, quasi-compact and all of its set-theoretic fibres are finite.

```lean
theorem quasiFinite_conditions_iff_finite_fibers {X S : Scheme.{u}} (f : X ⟶ S) :
    ((LocallyOfFiniteType f ∧ QuasiCompact f) ∧ LocallyQuasiFinite f) ↔
      ((LocallyOfFiniteType f ∧ QuasiCompact f) ∧ ∀ s, (f ⁻¹' {s}).Finite)
```

**`AlgebraicGeometry.exists_isOpen_finite_preimage_inter_of_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedLocallyFiniteCharts.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedLocallyFiniteCharts.lean#L49). The attribute's comment: “the preimage of a locally finite set under a locally quasi-finite morphism”.

> Let `f : X ⟶ Y` be a morphism of schemes, locally of finite type and locally quasi-finite, and
> let `Z` be a set of points of `Y` such that every point of `Y` has an open neighbourhood meeting
> `Z` in a finite set. Then every point of `X` has an open neighbourhood meeting `f⁻¹ Z` in a
> finite set.

```lean
theorem exists_isOpen_finite_preimage_inter_of_locallyQuasiFinite {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [LocallyQuasiFinite f] {Z : Set Y}
    (hZ : ∀ y : Y, ∃ W : Y.Opens, y ∈ W ∧ (Z ∩ (W : Set Y)).Finite) (x : X) :
    ∃ Ω : X.Opens, x ∈ Ω ∧ (f.base ⁻¹' Z ∩ (Ω : Set X)).Finite
```

## Tag 01TK, a lemma

[Tag 01TK](https://stacks.math.columbia.edu/tag/01TK) in the Stacks Project.

**`AlgebraicGeometry.locallyQuasiFinite_conditions_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean#L186). The attribute's comment: “equivalence of (1), (2), (3) and (4)”.

> **Stacks Project, Tag 01TK.** Local quasi-finiteness can be checked on all pairs of affine
> opens, on open coverings of the target and of the preimages, or on affine such coverings; on
> affine opens it is the condition that the ring map be quasi-finite, that is of finite type and
> quasi-finite at every prime.

```lean
public theorem locallyQuasiFinite_conditions_tfae {X S : Scheme.{u}} (f : X ⟶ S) :
    List.TFAE [
      LocallyOfFiniteType f ∧ LocallyQuasiFinite f,
      ∀ (V : S.affineOpens) (U : X.affineOpens) (e : U.1 ≤ f ⁻¹ᵁ V.1),
        (f.appLE V U e).hom.FiniteType ∧ (f.appLE V U e).hom.QuasiFinite,
      ∃ 𝒱 : Set S.Opens, sSup 𝒱 = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.Opens, sSup 𝒰 = f ⁻¹ᵁ V ∧
        ∀ U ∈ 𝒰, ∃ e : U ≤ f ⁻¹ᵁ V,
          LocallyOfFiniteType (f.resLE V U e) ∧ LocallyQuasiFinite (f.resLE V U e),
      ∃ 𝒱 : Set S.affineOpens, (⨆ V ∈ 𝒱, V.1) = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.affineOpens,
        (⨆ U ∈ 𝒰, U.1) = f ⁻¹ᵁ V.1 ∧ ∀ U ∈ 𝒰, ∃ e : U.1 ≤ f ⁻¹ᵁ V.1,
          (f.appLE V U e).hom.FiniteType ∧ (f.appLE V U e).hom.QuasiFinite]
```

**`AlgebraicGeometry.locallyQuasiFinite_conditions_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Defs.lean#L252). The attribute's comment: “moreover: restriction to open subschemes”.

> **Stacks Project, Tag 01TK.** If `f` is locally quasi-finite then so is its restriction
> `U → V` to any opens `U ⊆ X`, `V ⊆ S` with `f(U) ⊆ V`.

```lean
public theorem locallyQuasiFinite_conditions_resLE {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : LocallyOfFiniteType f ∧ LocallyQuasiFinite f) (V : S.Opens) (U : X.Opens)
    (e : U ≤ f ⁻¹ᵁ V) :
    LocallyOfFiniteType (f.resLE V U e) ∧ LocallyQuasiFinite (f.resLE V U e)
```

## Tag 01TL, a lemma

[Tag 01TL](https://stacks.math.columbia.edu/tag/01TL) in the Stacks Project.

**`AlgebraicGeometry.locallyQuasiFinite_conditions_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Composition.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Composition.lean#L47). The attribute's comment: “locally quasi-finite morphisms”.

> **Stacks Project, Tag 01TL.** The composition of two locally quasi-finite morphisms is
> locally quasi-finite.

```lean
theorem locallyQuasiFinite_conditions_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    [LocallyOfFiniteType f] [LocallyQuasiFinite f]
    [LocallyOfFiniteType g] [LocallyQuasiFinite g] :
    LocallyOfFiniteType (f ≫ g) ∧ LocallyQuasiFinite (f ≫ g)
```

**`AlgebraicGeometry.quasiFinite_conditions_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Composition.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Composition.lean#L56). The attribute's comment: “quasi-finite morphisms”.

> **Stacks Project, Tag 01TL.** The composition of two quasi-finite morphisms is
> quasi-finite.

```lean
theorem quasiFinite_conditions_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    [LocallyOfFiniteType f] [QuasiCompact f] [LocallyQuasiFinite f]
    [LocallyOfFiniteType g] [QuasiCompact g] [LocallyQuasiFinite g] :
    (LocallyOfFiniteType (f ≫ g) ∧ QuasiCompact (f ≫ g)) ∧ LocallyQuasiFinite (f ≫ g)
```

## Tag 01TM, a lemma

[Tag 01TM](https://stacks.math.columbia.edu/tag/01TM) in the Stacks Project.

**`AlgebraicGeometry.quasiFiniteLocus_eq_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChange.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChange.lean#L452). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 01TM.** In a cartesian square, the quasi-finite locus of the
> base-changed morphism is the inverse image of the quasi-finite locus of the original
> morphism.

```lean
public theorem quasiFiniteLocus_eq_preimage_of_isPullback {X S S' X' : Scheme.{u}} {f : X ⟶ S}
    {g : S' ⟶ S} {f' : X' ⟶ S'} {g' : X' ⟶ X} [LocallyOfFiniteType f]
    (sq : IsPullback g' f' f g) : quasiFiniteLocus f' = g' ⁻¹ᵁ quasiFiniteLocus f
```

Declarations registered for the tag:

- [`AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChange.lean, line 460](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChange.lean#L460) (StacksFrontier): “parts (2) and (3), local finite-type condition”. References: EGA I (10.13.5), “(ii)”; EGA I (6.3.4), “clause (iv)”; EGA I (6.6.6); EGA II (3.5.5), “partial”; EGA IV (1.3.4); EGA IV (2.7.1), “(iii)”; SGA 3 VIB (2.1.2), “partial”.
- [`AlgebraicGeometry.instIsStableUnderBaseChangeSchemeLocallyQuasiFinite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instIsStableUnderBaseChangeSchemeLocallyQuasiFinite#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChange.lean, line 463](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChange.lean#L463) (StacksFrontier): “parts (2) and (3), fiber-isolation condition”. References: EGA II (6.2.4), “(iii)”; SGA 3 V (7.4), “special case”; SGA 3 VIB (10.1), “sufficiency”; SGA 3 VIB (2.8), “(i) ⇒ (ii), partial”.
- [`AlgebraicGeometry.quasiCompact_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiCompact_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChange.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChange.lean#L473) (StacksFrontier): “part (3), quasi-compact condition”. References: EGA I (6.3.4), “clause (iv)”; EGA I (6.6.4); EGA III (6.9.1), “partial”; EGA III (6.9.4), “more general”; EGA III (7.7.2), “quasi-compactness of f'”; EGA IV (1.1.2); EGA IV (2.3.7), “(i)”; EGA IV (2.6.4), “necessity in (v)”; SGA 1 VIII (3.3), “quasi-compact clause”; SGA 4 VI (1.8), “(ii), special case”; SGA 4 VI (1.9.1), “(ii), special case”; SGA 4 VIII (5.1), “partial”; SGA 7 VII (1.3.8), “partial”.

## Tag 0AAY, a lemma

[Tag 0AAY](https://stacks.math.columbia.edu/tag/0AAY) in the Stacks Project.

**`AlgebraicGeometry.finite_setOf_mapsTo_and_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Fibre.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Fibre.lean#L51).

> For a finite-type morphism of schemes, the set of points over a fixed point at which the
> morphism is quasi-finite is finite.

```lean
public theorem finite_setOf_mapsTo_and_quasiFiniteAt
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f] (s : S) :
    {x : X | f x = s ∧ quasiFiniteAt f x}.Finite
```

## Tag 0CT8, a lemma

[Tag 0CT8](https://stacks.math.columbia.edu/tag/0CT8) in the Stacks Project.

**`AlgebraicGeometry.isSeparated_and_locallyQuasiFinite_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Monomorphism.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Monomorphism.lean#L56).

> A monomorphism of schemes which is locally of finite type is separated and locally
> quasi-finite.

```lean
theorem isSeparated_and_locallyQuasiFinite_of_mono {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [Mono f] :
    IsSeparated f ∧ LocallyQuasiFinite f
```

## Tag 01TN, a lemma

[Tag 01TN](https://stacks.math.columbia.edu/tag/01TN) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.instLocallyQuasiFiniteOfIsImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instLocallyQuasiFiniteOfIsImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L287) (StacksFrontier): “quasi-finite fibres; Mathlib's `LocallyQuasiFinite` leaves out the finite-type condition built into Stacks' definition (01TD)”. References: EGA II (6.2.4), “(i)”.
- [`AlgebraicGeometry.IsImmersion.instLocallyOfFiniteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion.instLocallyOfFiniteType#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L291) (StacksFrontier): “locally of finite type, the other half of Stacks' locally quasi-finite”. References: EGA I (6.3.4), “(i)”; EGA I (6.3.5), “partial”; EGA I (6.6.6), “(i), for immersions”; EGA IV (1.3.4), “(i), immersions”; EGA IV (1.5.4), “(i)”.

## Tag 03WR, a lemma

[Tag 03WR](https://stacks.math.columbia.edu/tag/03WR) in the Stacks Project.

**`AlgebraicGeometry.quasiFiniteAt_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Permanence.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Permanence.lean#L115). The attribute's comment: “quasi-finite at a point”.

> **Stacks Project, Tag 03WR.** If a composite is quasi-finite at a point of its
> source, then its first factor is quasi-finite there.

```lean
public theorem quasiFiniteAt_of_comp {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    (x : X) (h : quasiFiniteAt (f ≫ g) x) :
    quasiFiniteAt f x
```

Declarations registered for the tag:

- [`AlgebraicGeometry.locallyOfFiniteType_of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFiniteType_of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Permanence.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Permanence.lean#L92) (StacksFrontier): “local finite-type part of locally quasi-finite”. References: EGA I (6.3.4), “clause (v)”; EGA I (6.3.6), “local finite type of f”; EGA I (6.6.6); EGA IV (1.3.4); EGA IV (1.5.6), “partial”; EGA IV (6.11.9), “The induced morphism v”; SGA 3 V (6.1), “partial”.
- [`AlgebraicGeometry.LocallyQuasiFinite.of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyQuasiFinite.of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Permanence.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Permanence.lean#L102) (StacksFrontier): “fiberwise part of locally quasi-finite”. References: EGA II (6.2.4), “(v)”.

## Tag 0GWS, a lemma

[Tag 0GWS](https://stacks.math.columbia.edu/tag/0GWS) in the Stacks Project.

**`AlgebraicGeometry.locallyQuasiFinite_of_comp_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Permanence.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Permanence.lean#L169).

> **Stacks Project, Tag 0GWS.** If `f` is surjective, `f ≫ g` is locally
> quasi-finite, and `g` is locally of finite type, then `g` is locally quasi-finite.

```lean
public theorem locallyQuasiFinite_of_comp_surjective
    {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [Surjective f]
    [LocallyOfFiniteType (f ≫ g)]
    [LocallyQuasiFinite (f ≫ g)]
    [LocallyOfFiniteType g] :
    LocallyQuasiFinite g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.21, Tag 01TC](https://stacks.math.columbia.edu/tag/01TC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
