---
declaration: section
origin: cited
lean: isOpen_krullTopology_apply_eq, isOpen_krullTopology_apply_eq', continuous_krullTopology, krullTopology.isTopologicalGroup_and_compactSpace_and_t2Space_and_totallyDisconnectedSpace, krullTopology.isGreatest_and_continuous_and_profinite, AlgEquiv.continuous_restrictNormalHom, AlgEquiv.restrictNormalHom, AlgEquiv.restrictNormalHom_surjective
statement: formalized
proof: formalized
---

# 9.22 Infinite Galois theory

Section 9.22 of the Stacks Project, [Tag 0BMI](https://stacks.math.columbia.edu/tag/0BMI). 5 tags here are carried by 14 declarations of the repository (11 in StacksCore and 3 in StacksFrontier) and 12 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BMJ, a lemma

[Tag 0BMJ](https://stacks.math.columbia.edu/tag/0BMJ) in the Stacks Project.

**`isOpen_krullTopology_apply_eq`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/KrullTopology.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/KrullTopology.lean#L17). The attribute's comment: “continuous”.

> **Stacks 0BMJ** (action is continuous).
> For `x : L` and `y : L` algebraic over `K`, the set of `σ ∈ Gal(L/K)` sending `x` to `y` is
> open in the Krull topology.

```lean
theorem isOpen_krullTopology_apply_eq (K : Type*) {L : Type*} [Field K] [Field L] [Algebra K L]
    (x : L) {y : L} (hy : IsAlgebraic K y) : IsOpen {σ : Gal(L/K) | σ x = y}
```

**`isOpen_krullTopology_apply_eq'`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/KrullTopology.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/KrullTopology.lean#L32). The attribute's comment: “continuous”.

> **Stacks 0BMJ** (action is continuous, algebraic extension).
> For an algebraic extension `L/K` and any `x y : L`, the set of `σ ∈ Gal(L/K)` sending `x`
> to `y` is open in the Krull topology.

```lean
theorem isOpen_krullTopology_apply_eq' (K : Type*) {L : Type*} [Field K] [Field L] [Algebra K L]
    [Algebra.IsAlgebraic K L] (x y : L) : IsOpen {σ : Gal(L/K) | σ x = y}
```

**`continuous_krullTopology`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/KrullTopology.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/KrullTopology.lean#L63). The attribute's comment: “universal property”.

> **Stacks 0BMJ** (universal property of the Krull topology).
> A map `f : X → Gal(L/K)` from a topological space `X` is continuous whenever the induced
> action `X × L → L` is continuous, expressed here as: for every `x : L` and `y : L`,
> the set `{i ∈ X | f i x = y}` is open.

```lean
theorem continuous_krullTopology {K L X : Type*} [Field K] [Field L] [Algebra K L]
    [TopologicalSpace X] {f : X → Gal(L/K)} (hf : ∀ x y, IsOpen {i | f i x = y}) : Continuous f
```

**`krullTopology.isTopologicalGroup_and_compactSpace_and_t2Space_and_totallyDisconnectedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/KrullTopologyProfinite.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/KrullTopologyProfinite.lean#L46). The attribute's comment: “(2): Gal(L/K) is a profinite topological group”.

> **Stacks 0BMJ** (2). For a Galois extension `L/K`, the Krull topology makes `Gal(L/K)` a
> profinite topological group: a topological group which is compact, Hausdorff and totally
> disconnected.

```lean
theorem isTopologicalGroup_and_compactSpace_and_t2Space_and_totallyDisconnectedSpace
    [IsGalois K L] :
    IsTopologicalGroup Gal(L/K) ∧ CompactSpace Gal(L/K) ∧ T2Space Gal(L/K) ∧
      TotallyDisconnectedSpace Gal(L/K)
```

**`krullTopology.isGreatest_and_continuous_and_profinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/KrullTopologyProfinite.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/KrullTopologyProfinite.lean#L60). The attribute's comment: “coarsest topology making the action continuous; (1) universal property; (2) profinite topological group”.

> **Stacks 0BMJ**. Let `L/K` be a Galois extension and give `L` the discrete topology.
> The Krull topology is the coarsest topology on `Gal(L/K)` for which the action
> `Gal(L/K) × L → L` is continuous, and with it
> (1) a map `f : X → Gal(L/K)` from a topological space `X` is continuous whenever the induced
> action `X × L → L` is continuous, and
> (2) `Gal(L/K)` is a profinite topological group.

```lean
theorem isGreatest_and_continuous_and_profinite [IsGalois K L] :
    IsGreatest {t : TopologicalSpace Gal(L/K) |
        @Continuous (Gal(L/K) × L) L (@instTopologicalSpaceProd _ L t ⊥) ⊥ fun p ↦ p.1 p.2}
      (krullTopology K L) ∧
    (∀ (X : Type*) [TopologicalSpace X] (f : X → Gal(L/K)),
      @Continuous (X × L) L (@instTopologicalSpaceProd X L _ ⊥) ⊥ (fun p ↦ f p.1 p.2) →
        Continuous f) ∧
    (IsTopologicalGroup Gal(L/K) ∧ CompactSpace Gal(L/K) ∧ T2Space Gal(L/K) ∧
      TotallyDisconnectedSpace Gal(L/K))
```

## Tag 0BMK, a lemma

[Tag 0BMK](https://stacks.math.columbia.edu/tag/0BMK) in the Stacks Project.

**`AlgEquiv.continuous_restrictNormalHom`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Galois/Infinite.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Infinite.lean#L48). The attribute's comment: “continuous”.

> **Stacks 0BMK** (the restriction is continuous).
> For a tower `L/M/K` with `L/K` algebraic and `M/K` normal, the restriction
> `Gal(L/K) → Gal(M/K)` is continuous for the Krull topologies.

```lean
theorem continuous_restrictNormalHom [Normal K M] [Algebra.IsAlgebraic K L] :
    Continuous (restrictNormalHom M : Gal(L/K) →* Gal(M/K))
```

Declarations registered for the tag:

- [`AlgEquiv.restrictNormalHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgEquiv.restrictNormalHom#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Infinite.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Infinite.lean#L25) (StacksCore): “homomorphism”.
- [`AlgEquiv.restrictNormalHom_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgEquiv.restrictNormalHom_surjective#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Infinite.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Infinite.lean#L26) (StacksCore): “surjective”.
- [`InfiniteGalois.restrictNormalHom_continuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=InfiniteGalois.restrictNormalHom_continuous#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Infinite.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Infinite.lean#L27) (StacksCore): “continuous, for an intermediate field”.

## Tag 0BU2, a lemma

[Tag 0BU2](https://stacks.math.columbia.edu/tag/0BU2) in the Stacks Project.

**`FiniteGaloisIntermediateField.isDirected_isColimit_galoisGroup_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/Galois/InfiniteGaloisLimit.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/Galois/InfiniteGaloisLimit.lean#L49).

> **Stacks 0BU2**. Let `K/k` be a Galois extension, and let `Λ` be the set of finite Galois
> subextensions `K/L/k`, ordered by inclusion. Then
> 1. `Λ` is a (nonempty) directed partially ordered set;
> 2. the `L ∈ Λ` form a system of `k`-algebras over `Λ` and `K = colim L` (in the category of
>   `k`-algebras);
> 3. the Galois groups `Gal(L/k)` form an inverse system of finite groups over `Λ` with surjective
>   transition maps, and the restriction maps identify `Gal(K/k)` with `lim Gal(L/k)` as a
>   profinite group;
> 4. each projection `Gal(K/k) → Gal(L/k)` is continuous and surjective.

```lean
theorem isDirected_isColimit_galoisGroup_isLimit [IsGalois k K] :
    (Nonempty (FiniteGaloisIntermediateField k K) ∧
      IsDirected (FiniteGaloisIntermediateField k K) (· ≤ ·)) ∧
    Nonempty (IsColimit (algCatCocone k K)) ∧
    ((∀ ⦃L₁ L₂ : (FiniteGaloisIntermediateField k K)ᵒᵖ⦄ (f : L₁ ⟶ L₂),
        Function.Surjective ((finGaloisGroupFunctor k K).map f).hom) ∧
      ∃ e : Gal(K/k) ≃ₜ* ProfiniteGrp.limit (InfiniteGalois.asProfiniteGaloisGroupFunctor k K),
        ∀ (L : FiniteGaloisIntermediateField k K) (σ : Gal(K/k)),
          InfiniteGalois.proj L (e σ) = AlgEquiv.restrictNormalHom L σ) ∧
    ∀ L : FiniteGaloisIntermediateField k K,
      Continuous (AlgEquiv.restrictNormalHom (F := k) (K₁ := K) L) ∧
      Function.Surjective (AlgEquiv.restrictNormalHom (F := k) (K₁ := K) L)
```

Declarations registered for the tag:

- [`FiniteGaloisIntermediateField.instLattice`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FiniteGaloisIntermediateField.instLattice#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/GaloisClosure.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/GaloisClosure.lean#L17) (StacksCore): “1”.
- [`FiniteGaloisIntermediateField.adjoin`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FiniteGaloisIntermediateField.adjoin#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/GaloisClosure.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/GaloisClosure.lean#L18) (StacksCore): “2”.
- [`AlgEquiv.restrictNormalHom_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgEquiv.restrictNormalHom_surjective#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/GaloisClosure.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/GaloisClosure.lean#L19) (StacksCore): “3, 4”.

## Tag 0BML, a theorem

[Tag 0BML](https://stacks.math.columbia.edu/tag/0BML) in the Stacks Project.

Declarations registered for the tag:

- [`InfiniteGalois.IntermediateFieldEquivClosedSubgroup`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=InfiniteGalois.IntermediateFieldEquivClosedSubgroup#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Infinite.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Infinite.lean#L21) (StacksCore).
- [`InfiniteGalois.isOpen_iff_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=InfiniteGalois.isOpen_iff_finite#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Infinite.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Infinite.lean#L22) (StacksCore): “finite subextension ↔ open subgroup”.
- [`InfiniteGalois.normal_iff_isGalois`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=InfiniteGalois.normal_iff_isGalois#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Infinite.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Infinite.lean#L23) (StacksCore): “Galois subextension ↔ normal closed subgroup”.

## Tag 0BMM, a lemma

[Tag 0BMM](https://stacks.math.columbia.edu/tag/0BMM) in the Stacks Project.

**`AlgEquiv.ker_restrictNormalHom_eq_image_restrictScalarsHom`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Galois/Basic.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Basic.lean#L56). The attribute's comment: “exact at the middle”.

> **Stacks 0BMH** (exactness at the middle term).
> For a tower `F ⊂ K ⊂ L` with `K/F` normal, the kernel of the restriction map
> `Gal(L/F) →* Gal(K/F)` equals the image of the scalar-restriction map
> `Gal(L/K) →* Gal(L/F)`.

```lean
theorem AlgEquiv.ker_restrictNormalHom_eq_image_restrictScalarsHom
    (F K L : Type*) [Field F] [Field K] [Field L]
    [Algebra F K] [Algebra K L] [Algebra F L] [IsScalarTower F K L] [Normal F K] :
    (AlgEquiv.restrictNormalHom K).ker =
      (AlgEquiv.restrictScalarsHom F (S := K) (A := L)).range
```

**`AlgEquiv.exists_restrictScalars_eq_of_restrictNormal_eq_one`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Galois/Basic.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Basic.lean#L74). The attribute's comment: “exact at the middle -- lift kernel to image”.

> **Stacks 0BMH** (exactness at the middle term, lift kernel to image).
> For a tower `F ⊂ K ⊂ L` with `K/F` normal, any `σ ∈ Gal(L/F)` whose restriction to `K`
> is the identity is the restriction of scalars of some `τ ∈ Gal(L/K)`.

```lean
theorem AlgEquiv.exists_restrictScalars_eq_of_restrictNormal_eq_one
    {F K L : Type*} [Field F] [Field K] [Field L]
    [Algebra F K] [Algebra K L] [Algebra F L] [IsScalarTower F K L]
    [Normal F K] {σ : Gal(L/F)} (hσ : σ.restrictNormal K = 1) :
    ∃ τ : Gal(L/K), τ.restrictScalars F = σ
```

**`AlgEquiv.restrictNormal_restrictScalars`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Galois/Basic.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Basic.lean#L86). The attribute's comment: “composition is 0”.

> **Stacks 0BMH** (composition is trivial).
> For a tower `F ⊂ K ⊂ L` with `K/F` normal, restricting an element of `Gal(L/K)` to
> `K` via the scalar-restriction `Gal(L/K) → Gal(L/F)` followed by `restrictNormal K`
> yields the identity.

```lean
theorem AlgEquiv.restrictNormal_restrictScalars {F K L : Type*} [Field F] [Field K] [Field L]
    [Algebra F K] [Algebra K L] [Algebra F L] [IsScalarTower F K L]
    [Normal F K] (σ : Gal(L/K)) :
    (σ.restrictScalars F).restrictNormal K = 1
```

**`AlgEquiv.continuous_restrictScalarsHom`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Galois/Infinite.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Infinite.lean#L39). The attribute's comment: “continuous”.

> **Stacks 0BMM** (the inclusion is continuous).
> For a tower `L/M/K` with `L/K` algebraic, the inclusion `Gal(L/M) → Gal(L/K)` is continuous for
> the Krull topologies.

```lean
theorem continuous_restrictScalarsHom [Algebra.IsAlgebraic K L] :
    Continuous (restrictScalarsHom K : Gal(L/M) →* Gal(L/K))
```

**`AlgEquiv.continuous_restrictNormalHom`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Galois/Infinite.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Infinite.lean#L48). The attribute's comment: “continuous”.

> **Stacks 0BMK** (the restriction is continuous).
> For a tower `L/M/K` with `L/K` algebraic and `M/K` normal, the restriction
> `Gal(L/K) → Gal(M/K)` is continuous for the Krull topologies.

```lean
theorem continuous_restrictNormalHom [Normal K M] [Algebra.IsAlgebraic K L] :
    Continuous (restrictNormalHom M : Gal(L/K) →* Gal(M/K))
```

**`AlgEquiv.isClosedEmbedding_restrictScalarsHom`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Galois/Infinite.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Infinite.lean#L60). The attribute's comment: “closed embedding”.

> **Stacks 0BMM** (`Gal(L/M)` is a closed subgroup).
> For a tower `L/M/K` with `L/K` Galois, the inclusion `Gal(L/M) → Gal(L/K)` is a closed
> embedding.

```lean
theorem isClosedEmbedding_restrictScalarsHom [IsGalois K L] :
    Topology.IsClosedEmbedding (restrictScalarsHom K : Gal(L/M) →* Gal(L/K))
```

**`AlgEquiv.isQuotientMap_restrictNormalHom`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Galois/Infinite.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Infinite.lean#L69). The attribute's comment: “quotient map”.

> **Stacks 0BMM** (`Gal(M/K)` carries the quotient topology).
> For a tower `L/M/K` with `L/K` Galois and `M/K` normal, the restriction `Gal(L/K) → Gal(M/K)` is
> a quotient map.

```lean
theorem isQuotientMap_restrictNormalHom [IsGalois K L] [Normal K M] :
    Topology.IsQuotientMap (restrictNormalHom M : Gal(L/K) →* Gal(M/K))
```

Declarations registered for the tag:

- [`IntermediateField.fixingSubgroupEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IntermediateField.fixingSubgroupEquiv#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Basic.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Basic.lean#L16) (StacksCore): “injective”.
- [`AlgEquiv.restrictScalars_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgEquiv.restrictScalars_injective#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Basic.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Basic.lean#L18) (StacksCore): “injective”.
- [`AlgEquiv.restrictNormalHom_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgEquiv.restrictNormalHom_surjective#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Basic.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Basic.lean#L20) (StacksCore): “surjective”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.22, Tag 0BMI](https://stacks.math.columbia.edu/tag/0BMI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
