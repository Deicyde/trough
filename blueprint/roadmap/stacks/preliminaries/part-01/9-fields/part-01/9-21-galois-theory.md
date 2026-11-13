---
declaration: section
origin: cited
lean: AlgEquiv, AlgEquiv.aut, IsGalois.of_isNormalClosure, IsGalois.normalClosure', IsGaloisGroup.fixedPoints, IsGalois.fixedField_bijective_and_isGalois_iff_normal, AlgEquiv.ker_restrictNormalHom_eq_image_restrictScalarsHom, AlgEquiv.exists_restrictScalars_eq_of_restrictNormal_eq_one
statement: formalized
proof: formalized
---

# 9.21 Galois theory

Section 9.21 of the Stacks Project, [Tag 09DU](https://stacks.math.columbia.edu/tag/09DU). 5 tags here are carried by 6 declarations of the repository (5 in StacksCore and 1 in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09DV, a definition

[Tag 09DV](https://stacks.math.columbia.edu/tag/09DV) in the Stacks Project.

Declarations registered for the tag:

- [`AlgEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/FieldTheory/GaloisGroup.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/GaloisGroup.lean#L22) (StacksFrontier): “the Galois group as a type”.
- [`AlgEquiv.aut`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgEquiv.aut#doc) registered with `add_to_stacks` in [StacksFrontier/FieldTheory/GaloisGroup.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/GaloisGroup.lean#L23) (StacksFrontier): “its group structure”.

## Tag 0EXM, a lemma

[Tag 0EXM](https://stacks.math.columbia.edu/tag/0EXM) in the Stacks Project.

**`IsGalois.of_isNormalClosure`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Galois/Basic.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Basic.lean#L29). The attribute's comment: “predicate version (absolute)”.

> **Stacks 0EXM** (predicate version, absolute).
> If `K/F` is separable and `L/F` is a normal closure of `K/F` (in the sense of
> `IsNormalClosure F K L`), then `L/F` is Galois.

```lean
theorem IsGalois.of_isNormalClosure (F K L : Type*) [Field F] [Field K] [Field L]
    [Algebra F K] [Algebra F L] [Algebra.IsSeparable F K] [IsNormalClosure F K L] : IsGalois F L
```

**`IsGalois.normalClosure'`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Galois/Basic.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Basic.lean#L40). The attribute's comment: “absolute normal closure”.

> **Stacks 0EXM** (absolute normal closure).
> The (absolute) normal closure `NormalClosure F K` of a separable extension `K/F` is
> Galois over `F`.

```lean
instance IsGalois.normalClosure' (F K : Type*) [Field F] [Field K] [Algebra F K]
    [Algebra.IsSeparable F K] : IsGalois F (NormalClosure F K)
```

## Tag 09I3, a lemma

[Tag 09I3](https://stacks.math.columbia.edu/tag/09I3) in the Stacks Project.

Declarations registered for the tag:

- [`IsGaloisGroup.fixedPoints`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsGaloisGroup.fixedPoints#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Basic.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Basic.lean#L21) (StacksCore): “G is the Galois group”.

## Tag 09DW, a theorem

[Tag 09DW](https://stacks.math.columbia.edu/tag/09DW) in the Stacks Project.

**`IsGalois.fixedField_bijective_and_isGalois_iff_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/Galois/FundamentalTheorem.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/Galois/FundamentalTheorem.lean#L46). The attribute's comment: “the full statement: K = L^G, the bijection H ↦ L^H with inverse M ↦ Gal(L/M), and normal subgroups ↔ Galois subextensions”.

> **Fundamental theorem of Galois theory** (Stacks 09DW). Let `L/K` be a finite Galois
> extension with Galois group `G = Gal(L/K)`. Then `K = L^G`; the map `H ↦ L^H` from subgroups of
> `G` to intermediate fields `L/M/K` is a bijection whose inverse sends `M` to
> `Gal(L/M) = M.fixingSubgroup`; and a subgroup `H` is normal exactly when `L^H/K` is Galois,
> equivalently a subextension `M/K` is Galois exactly when `Gal(L/M)` is normal in `G`.

```lean
theorem fixedField_bijective_and_isGalois_iff_normal [FiniteDimensional K L] [IsGalois K L] :
    fixedField (⊤ : Subgroup Gal(L/K)) = ⊥ ∧
    Function.Bijective (fixedField : Subgroup Gal(L/K) → IntermediateField K L) ∧
    (∀ H : Subgroup Gal(L/K), (fixedField H).fixingSubgroup = H) ∧
    (∀ M : IntermediateField K L, fixedField M.fixingSubgroup = M) ∧
    (∀ H : Subgroup Gal(L/K), H.Normal ↔ IsGalois K (fixedField H)) ∧
    (∀ M : IntermediateField K L, M.fixingSubgroup.Normal ↔ IsGalois K M)
```

## Tag 0BMH, a lemma

[Tag 0BMH](https://stacks.math.columbia.edu/tag/0BMH) in the Stacks Project.

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

Declarations registered for the tag:

- [`IntermediateField.fixingSubgroupEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IntermediateField.fixingSubgroupEquiv#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Basic.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Basic.lean#L15) (StacksCore): “injective”.
- [`AlgEquiv.restrictScalars_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgEquiv.restrictScalars_injective#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Basic.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Basic.lean#L17) (StacksCore): “injective”.
- [`AlgEquiv.restrictNormalHom_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgEquiv.restrictNormalHom_surjective#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Galois/Basic.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Galois/Basic.lean#L19) (StacksCore): “surjective”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.21, Tag 09DU](https://stacks.math.columbia.edu/tag/09DU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
