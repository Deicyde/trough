---
declaration: section
origin: cited
lean: jacobson_check_irreducible_closed, main_theorem02I7, jacobsonSpace_iff_of_isOpenCover, closedPoints_eq_iUnion_image_closedPoints_of_isOpenCover, jacobson_of_iUnion_isLocallyClosed, jacobson_of_isLocallyClosed, jacobson_of_isOpen, jacobson_of_isClosed
statement: formalized
proof: formalized
---

# 5.18 Jacobson spaces

Section 5.18 of the Stacks Project, [Tag 005T](https://stacks.math.columbia.edu/tag/005T). 7 tags here are carried by 16 declarations of the repository (1 in StacksCore and 15 in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 005V, a lemma

[Tag 005V](https://stacks.math.columbia.edu/tag/005V) in the Stacks Project.

**`jacobson_check_irreducible_closed`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Jacobson/Criterion.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Jacobson/Criterion.lean#L25).

> **Stacks 005V**. Let `X` be a topological space and `X₀` its set of closed
> points. If for every point `x` the intersection `X₀ ∩ closure {x}` is dense in
> `closure {x}` (equivalently, `closure (closedPoints X ∩ closure {x}) = closure {x}`),
> then `X` is a Jacobson space.

```lean
theorem jacobson_check_irreducible_closed
    {X : Type*} [TopologicalSpace X]
    (h : ∀ x : X, closure (closedPoints X ∩ closure ({x} : Set X)) = closure ({x} : Set X)) :
    JacobsonSpace X
```

## Tag 02I7, a lemma

[Tag 02I7](https://stacks.math.columbia.edu/tag/02I7) in the Stacks Project.

**`main_theorem02I7`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/CounterexampleQuasiCompact.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/CounterexampleQuasiCompact.lean#L55). References: EGA IV (10.4.5.1), “sufficiency”.

> **Stacks 02I7**. If `X` is a Kolmogorov topological space with a basis of quasi-compact open
> sets and `X` is not Jacobson, then there exists a point `x ∈ X` such that `{x}` is not closed
> in `X` and `{x}` is locally closed in `X`.

```lean
theorem main_theorem02I7
    (X : Type*) [TopologicalSpace X] [T0Space X]
    (hB : PrespectralSpace X) (hJ : ¬ JacobsonSpace X) :
    ∃ x : X, ¬ IsClosed ({x} : Set X) ∧ IsLocallyClosed ({x} : Set X)
```

## Tag 005W, a lemma

[Tag 005W](https://stacks.math.columbia.edu/tag/005W) in the Stacks Project.

**`jacobsonSpace_iff_of_isOpenCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/OpenCover.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/OpenCover.lean#L53). References: EGA IV (10.3.3); EGA IV (10.3.2), “special case”.

> For an open covering `U : ι → TopologicalSpace.Opens X` of a topological space `X`, the space
> `X` is Jacobson if and only if each `U i`, with the subspace topology, is Jacobson.

```lean
theorem jacobsonSpace_iff_of_isOpenCover
    {X : Type*} [TopologicalSpace X]
    {ι : Type*} {U : ι → TopologicalSpace.Opens X}
    (hU : TopologicalSpace.IsOpenCover U) :
    JacobsonSpace X ↔ ∀ i, JacobsonSpace (U i)
```

**`closedPoints_eq_iUnion_image_closedPoints_of_isOpenCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/OpenCover.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/OpenCover.lean#L64). References: EGA IV (10.4.7), “open immersions”; EGA IV (10.9.2), “special case”.

> For an open covering `U : ι → TopologicalSpace.Opens X` of a Jacobson space `X`, the set of
> closed points of `X` is the union over `i` of the images of the closed points of `U i` under the
> inclusion `Subtype.val : ↥(U i) → X`.

```lean
theorem closedPoints_eq_iUnion_image_closedPoints_of_isOpenCover
    {X : Type*} [TopologicalSpace X]
    {ι : Type*} {U : ι → TopologicalSpace.Opens X}
    (hU : TopologicalSpace.IsOpenCover U)
    [JacobsonSpace X] :
    closedPoints X = ⋃ i, (Subtype.val : ↥(U i) → X) '' closedPoints ↥(U i)
```

## Tag 005X, a lemma

[Tag 005X](https://stacks.math.columbia.edu/tag/005X) in the Stacks Project.

**`jacobson_of_iUnion_isLocallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/Subspace.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/Subspace.lean#L183). References: EGA IV (10.3.2); EGA IV (10.3.3), “necessity”; EGA IV (10.4.3), “more general”.

> **Stacks 005X**. A (possibly infinite) union of locally closed subsets of a Jacobson space
> is Jacobson, and its closed points are closed in the ambient space.

```lean
theorem jacobson_of_iUnion_isLocallyClosed
    {X : Type u} [TopologicalSpace X] [JacobsonSpace X]
    {ι : Type v} {L : ι → Set X} (hL : ∀ i, IsLocallyClosed (L i)) :
    JacobsonSpace (⋃ i, L i : Set X) ∧
      (closedPoints (⋃ i, L i : Set X) ⊆ Subtype.val ⁻¹' closedPoints X)
```

**`jacobson_of_isLocallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/Subspace.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/Subspace.lean#L198). References: EGA IV (10.3.2), “locally closed case”; EGA IV (10.3.3), “necessity”; EGA IV (10.4.3), “more general”; EGA IV (10.4.7), “special case”; EGA IV (10.9.2), “special case”.

> **Stacks 005X**. A locally closed subset of a Jacobson space is Jacobson, and its closed
> points are closed in the ambient space.

```lean
theorem jacobson_of_isLocallyClosed
    {X : Type u} [TopologicalSpace X] [JacobsonSpace X]
    {T : Set X} (hT : IsLocallyClosed T) :
    JacobsonSpace T ∧ (closedPoints T ⊆ Subtype.val ⁻¹' closedPoints X)
```

**`jacobson_of_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/Subspace.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/Subspace.lean#L216). References: EGA IV (10.3.2), “special case”; EGA IV (10.3.3), “necessity”; EGA IV (10.4.3), “Open subpreschemes”; EGA IV (10.9.2), “special case”.

> **Stacks 005X**. An open subset of a Jacobson space is Jacobson, and its closed points are
> closed in the ambient space.

```lean
theorem jacobson_of_isOpen
    {X : Type u} [TopologicalSpace X] [JacobsonSpace X]
    {T : Set X} (hT : IsOpen T) :
    JacobsonSpace T ∧ (closedPoints T ⊆ Subtype.val ⁻¹' closedPoints X)
```

**`jacobson_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/Subspace.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/Subspace.lean#L228). References: EGA IV (10.3.2), “closed subspace case”; EGA IV (10.4.3), “Closed subpreschemes”; EGA IV (10.4.7), “closed subschemes”.

> **Stacks 005X**. A closed subset of a Jacobson space is Jacobson, and its closed points are
> closed in the ambient space.

```lean
theorem jacobson_of_isClosed
    {X : Type u} [TopologicalSpace X] [JacobsonSpace X]
    {T : Set X} (hT : IsClosed T) :
    JacobsonSpace T ∧ (closedPoints T ⊆ Subtype.val ⁻¹' closedPoints X)
```

**`jacobson_of_isFiniteUnionLocallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/Subspace.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/Subspace.lean#L237). References: EGA IV (10.3.2), “special case”.

> **Stacks 005X**. A finite union of locally closed subsets of a Jacobson space is Jacobson,
> and its closed points are closed in the ambient space.

```lean
theorem jacobson_of_isFiniteUnionLocallyClosed
    {X : Type u} [TopologicalSpace X] [JacobsonSpace X]
    {T : Set X} (hT : IsFiniteUnionLocallyClosed T) :
    JacobsonSpace T ∧ (closedPoints T ⊆ Subtype.val ⁻¹' closedPoints X)
```

**`jacobson_of_isLocallyUnionOfLocallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/Subspace.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/Subspace.lean#L252). References: EGA IV (10.3.2), “more general”; EGA IV (10.3.3), “necessity”; EGA IV (10.4.3), “more general”; EGA IV (10.4.7), “special case”.

> **Stacks 005X**. A subset of a Jacobson space which locally on `X` is a union of locally
> closed subsets is Jacobson, and its closed points are closed in the ambient space.

```lean
theorem jacobson_of_isLocallyUnionOfLocallyClosed
    {X : Type u} [TopologicalSpace X] [JacobsonSpace X]
    {T : Set X} (hT : IsLocallyUnionOfLocallyClosed T) :
    JacobsonSpace T ∧ (closedPoints T ⊆ Subtype.val ⁻¹' closedPoints X)
```

## Tag 07JU, a lemma

[Tag 07JU](https://stacks.math.columbia.edu/tag/07JU) in the Stacks Project.

Declarations registered for the tag:

- [`instDiscreteTopologyOfFiniteOfJacobsonSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instDiscreteTopologyOfFiniteOfJacobsonSpace#doc) registered with `add_to_stacks` in [StacksCore/Topology/Jacobson/FinitelyManyClosedPoints.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Jacobson/FinitelyManyClosedPoints.lean#L20) (StacksCore): “a finite Jacobson space is discrete”.
- [`JacobsonSpace.discreteTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=JacobsonSpace.discreteTopology#doc) registered with `add_to_stacks` in [StacksCore/Topology/Jacobson/FinitelyManyClosedPoints.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Jacobson/FinitelyManyClosedPoints.lean#L21) (StacksCore): “a Jacobson space with finitely many closed points is discrete”.

## Tag 005Z, a lemma

[Tag 005Z](https://stacks.math.columbia.edu/tag/005Z) in the Stacks Project.

**`jacobsonSpace_locallyClosed_bijection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/LocallyClosedUnion.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/LocallyClosedUnion.lean#L252). References: EGA IV (10.1.2), “a′ ⇒ c and c′, a′ ⇒ c″”; EGA IV (10.2.7), “special case”; EGA IV (10.3.1), “Forward direction”; EGA IV (10.9.1), “more general”; EGA IV (10.9.2), “partial”.

> **Stacks 005Z**. Let `X` be a Jacobson topological space, and let `X₀ = closedPoints X`
> carry the subspace topology. There exists a bijection `Φ` between the finite unions of locally
> closed subsets of `X` and of `X₀`, given by pullback `E ↦ Subtype.val ⁻¹' E`, that is,
> `E ↦ E ∩ X₀`, which preserves inclusion in both directions and restricts to bijections on the
> locally closed, the open, and the closed subsets.

```lean
theorem jacobsonSpace_locallyClosed_bijection
    (X : Type*) [TopologicalSpace X] [JacobsonSpace X] :
    ∃ Φ : {s : Set X // IsFiniteUnionLocallyClosed s} ≃
          {s : Set ↥(closedPoints X) // IsFiniteUnionLocallyClosed s},
      (∀ E, (Φ E).1 = Subtype.val ⁻¹' E.1) ∧
      (∀ E E', E.1 ⊆ E'.1 ↔ (Φ E).1 ⊆ (Φ E').1) ∧
      (∀ E, IsLocallyClosed E.1 ↔ IsLocallyClosed (Φ E).1) ∧
      (∀ E, IsOpen E.1 ↔ IsOpen (Φ E).1) ∧
      (∀ E, IsClosed E.1 ↔ IsClosed (Φ E).1)
```

## Tag 005Y, a lemma

[Tag 005Y](https://stacks.math.columbia.edu/tag/005Y) in the Stacks Project.

**`JacobsonSpace.isConstructible_restrictToClosedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/ConstructibleClosedPoints.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/ConstructibleClosedPoints.lean#L187). The attribute's comment: “well-defined”. References: EGA IV (10.4.10), “partial”.

> The correspondence of Stacks 005Y is well defined: for a constructible subset `E` of a
> Jacobson space `X`, the subset `E ∩ X₀` of the space of closed points is constructible.
>
> Restriction to the closed points is continuous and preserves retrocompactness of opens, so this
> is Mathlib's `Topology.IsConstructible.preimage`.

```lean
theorem isConstructible_restrictToClosedPoints [JacobsonSpace X] {E : Set X}
    (hE : IsConstructible E) : IsConstructible (restrictToClosedPoints E)
```

**`JacobsonSpace.subset_iff_restrictToClosedPoints_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/ConstructibleClosedPoints.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/ConstructibleClosedPoints.lean#L202). The attribute's comment: “inclusion-preserving”. References: EGA IV (10.2.7), “special case”; EGA IV (10.4.10), “partial”; EGA IV (8.1.3), “more general”.

> The correspondence of Stacks 005Y reflects inclusions: constructible subsets `E, F` of a
> Jacobson space satisfy `E ⊆ F` if and only if `E ∩ X₀ ⊆ F ∩ X₀`.
>
> Only the backward direction has content: `E \ F` is constructible, so if it is nonempty it
> contains a closed point, which then witnesses the failure of `E ∩ X₀ ⊆ F ∩ X₀`.

```lean
theorem subset_iff_restrictToClosedPoints_subset [JacobsonSpace X] {E F : Set X}
    (hE : IsConstructible E) (hF : IsConstructible F) :
    E ⊆ F ↔ restrictToClosedPoints E ⊆ restrictToClosedPoints F
```

**`JacobsonSpace.restrictToClosedPoints_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/ConstructibleClosedPoints.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/ConstructibleClosedPoints.lean#L227). The attribute's comment: “bijective correspondence”. References: EGA IV (10.4.10), “special case”.

> Stacks 005Y: on a Jacobson space `X`, restriction to the closed points is a bijection from
> the constructible subsets of `X` onto the constructible subsets of `X₀ = closedPoints X`.
>
> Injectivity is the inclusion-reflecting property applied twice. Surjectivity is proved by the
> Boolean induction `Topology.IsConstructible.empty_union_induction`: a retrocompact open of `X₀` is
> the restriction of an open of `X`, which is retrocompact by
> `JacobsonSpace.isRetrocompact_iff_isRetrocompact_restrictToClosedPoints`, and restriction
> commutes with unions and complements.

```lean
theorem restrictToClosedPoints_bijective [JacobsonSpace X] :
    Function.Bijective
      (fun E : {E : Set X // IsConstructible E} =>
        (⟨restrictToClosedPoints E.1, isConstructible_restrictToClosedPoints E.2⟩ :
          {F : Set (closedPoints X) // IsConstructible F}))
```

**`JacobsonSpace.isOpen_and_isRetrocompact_iff_on_closedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/ConstructibleClosedPoints.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/ConstructibleClosedPoints.lean#L262). The attribute's comment: “preserves retrocompact opens”.

> Stacks 005Y: the correspondence matches the retrocompact opens of `X` with the retrocompact
> opens of `X₀`. A constructible subset `E` of a Jacobson space is a retrocompact open if and only
> if `E ∩ X₀` is a retrocompact open of the space of closed points.
>
> The backward direction writes `E ∩ X₀` as the restriction of an open `U ⊆ X`, which is
> retrocompact and hence constructible; both `U` and `E` are then constructible with the same
> restriction, so `U = E` by `JacobsonSpace.subset_iff_restrictToClosedPoints_subset`.

```lean
theorem isOpen_and_isRetrocompact_iff_on_closedPoints [JacobsonSpace X] {E : Set X}
    (hE : IsConstructible E) :
    (IsOpen E ∧ IsRetrocompact E) ↔
      (IsOpen (restrictToClosedPoints E) ∧ IsRetrocompact (restrictToClosedPoints E))
```

**`JacobsonSpace.isOpen_compl_and_isRetrocompact_compl_iff_on_closedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Jacobson/ConstructibleClosedPoints.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Jacobson/ConstructibleClosedPoints.lean#L282). The attribute's comment: “preserves complements of retrocompact opens”.

> Stacks 005Y: the correspondence matches the complements of retrocompact opens of `X` with the
> complements of retrocompact opens of `X₀`. This is the previous statement applied to `Eᶜ`, which
> is constructible, together with the fact that restriction to the closed points commutes with
> complementation.

```lean
theorem isOpen_compl_and_isRetrocompact_compl_iff_on_closedPoints [JacobsonSpace X] {E : Set X}
    (hE : IsConstructible E) :
    (IsOpen Eᶜ ∧ IsRetrocompact Eᶜ) ↔
      (IsOpen (restrictToClosedPoints E)ᶜ ∧ IsRetrocompact (restrictToClosedPoints E)ᶜ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.18, Tag 005T](https://stacks.math.columbia.edu/tag/005T)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
