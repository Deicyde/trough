---
declaration: section
origin: cited
lean: exists_isPurelyInseparable_and_isSeparableExtension_of_essFiniteType, perfectClosure.isPurelyInseparable, perfectClosure.perfectField, IsPurelyInseparable.instNonemptyAlgHomOfPerfectField, instSubsingletonAlgHomOfIsPurelyInseparable, perfectClosure, Algebra.IsGeometricallyReduced.of_perfectField, PerfectField.isReduced_tensorProduct
statement: formalized
proof: formalized
---

# 10.45 Perfect fields

Section 10.45 of the Stacks Project, [Tag 05DU](https://stacks.math.columbia.edu/tag/05DU). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 030R, a lemma

[Tag 030R](https://stacks.math.columbia.edu/tag/030R) in the Stacks Project.

**`exists_isPurelyInseparable_and_isSeparableExtension_of_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PurelyInseparable/BaseChange.lean, line 979](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/PurelyInseparable/BaseChange.lean#L979). References: EGA 0 (19.6.6).

> Let `K/k` be a finitely generated field extension and let `Ω/K` be a perfect field extension.
> Then inside `Ω` there is a diagram
> ```
> K  →  K'
> ↑     ↑
> k  →  k'
> ```
> with `k'/k` and `K'/K` finite purely inseparable and `K'/k'` separable in the sense of
> [stacks, 030O\](2), in which moreover `K'` is the compositum `k'K` and the canonical map
> `k' ⊗[k] K → K'` is surjective with kernel the nilradical, i.e. `K' = (k' ⊗[k] K)_red`.

```lean
public theorem exists_isPurelyInseparable_and_isSeparableExtension_of_essFiniteType
    (k K Ω : Type*) [Field k] [Field K] [Field Ω] [Algebra k K] [Algebra k Ω] [Algebra K Ω]
    [IsScalarTower k K Ω] [PerfectField Ω] [Algebra.EssFiniteType k K] :
    ∃ (K' : IntermediateField K Ω) (k' : IntermediateField k ↥K'),
      Module.Finite K ↥K' ∧ IsPurelyInseparable K ↥K' ∧
      Module.Finite k ↥k' ∧ IsPurelyInseparable k ↥k' ∧
      Algebra.IsSeparableExtension ↥k' ↥K' ∧
      IntermediateField.adjoin K (k' : Set ↥K') = ⊤ ∧
      Function.Surjective (Algebra.TensorProduct.productMap
        (IsScalarTower.toAlgHom k ↥k' ↥K') (IsScalarTower.toAlgHom k K ↥K')) ∧
      RingHom.ker (Algebra.TensorProduct.productMap
        (IsScalarTower.toAlgHom k ↥k' ↥K') (IsScalarTower.toAlgHom k K ↥K')) =
        nilradical (↥k' ⊗[k] K)
```

## Tag 046W, a lemma

[Tag 046W](https://stacks.math.columbia.edu/tag/046W) in the Stacks Project.

Declarations registered for the tag:

- [`perfectClosure.isPurelyInseparable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=perfectClosure.isPurelyInseparable#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L292) (StacksFrontier): “existence: the perfect closure of `k` in an algebraic closure is purely inseparable”.
- [`perfectClosure.perfectField`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=perfectClosure.perfectField#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L295) (StacksFrontier): “existence: it is perfect (given a perfect ambient field, e.g. `IsAlgClosed.perfectField`)”.
- [`IsPurelyInseparable.instNonemptyAlgHomOfPerfectField`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsPurelyInseparable.instNonemptyAlgHomOfPerfectField#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L298) (StacksFrontier): “uniqueness: a `k`-map into any perfect extension exists”.
- [`instSubsingletonAlgHomOfIsPurelyInseparable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instSubsingletonAlgHomOfIsPurelyInseparable#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L300) (StacksFrontier): “uniqueness: such a `k`-map is unique”. References: EGA I (3.5.8), “special case”.

## Tag 046X, a definition

[Tag 046X](https://stacks.math.columbia.edu/tag/046X) in the Stacks Project.

Declarations registered for the tag:

- [`perfectClosure`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=perfectClosure#doc) registered with `add_to_stacks` in [StacksFrontier/FieldTheory/PerfectClosure.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/PerfectClosure.lean#L20) (StacksFrontier): “the perfect closure of `k`, as the largest purely inseparable subextension of a given extension; the tag's `k^perf` is this taken inside an algebraic closure”.
- [`perfectClosure.perfectField`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=perfectClosure.perfectField#doc) registered with `add_to_stacks` in [StacksFrontier/FieldTheory/PerfectClosure.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/PerfectClosure.lean#L23) (StacksFrontier): “that it is a perfect field”.

## Tag 00I4, a lemma

[Tag 00I4](https://stacks.math.columbia.edu/tag/00I4) in the Stacks Project.

**`Algebra.IsGeometricallyReduced.of_perfectField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyReduced/TensorProduct.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyReduced/TensorProduct.lean#L132). The attribute's comment: “Clause (1): over a perfect field `k` every reduced `k`-algebra is geometrically reduced, stated with Mathlib's `Algebra.IsGeometricallyReduced` (equivalent to the source's Definition 030S by Lemma 030V); the source's form, reducedness of `K ⊗[k] S` for every field extension `K/k`, is `PerfectField.isReduced_tensorProduct_field`.”.

> Over a perfect field `k`, every reduced `k`-algebra is geometrically reduced.

```lean
public theorem Algebra.IsGeometricallyReduced.of_perfectField (k S : Type*) [Field k]
    [PerfectField k] [CommRing S] [Algebra k S] [IsReduced S] :
    Algebra.IsGeometricallyReduced k S
```

**`PerfectField.isReduced_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyReduced/TensorProduct.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyReduced/TensorProduct.lean#L144). The attribute's comment: “Clause (2): over a perfect field `k` the tensor product `R ⊗[k] S` of two reduced `k`-algebras is reduced.”.

> Over a perfect field `k`, the tensor product of two reduced `k`-algebras is reduced.

```lean
public theorem PerfectField.isReduced_tensorProduct (k R S : Type*) [Field k] [PerfectField k]
    [CommRing R] [Algebra k R] [IsReduced R] [CommRing S] [Algebra k S] [IsReduced S] :
    IsReduced (R ⊗[k] S)
```

**`PerfectField.isReduced_tensorProduct_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyReduced/TensorProduct.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyReduced/TensorProduct.lean#L155). The attribute's comment: “Clause (1) in the source's Definition 030S of geometric reducedness: over a perfect field `k`, for a reduced `k`-algebra `S`, the ring `K ⊗[k] S` is reduced for every field extension `K/k`.”.

> Over a perfect field `k`, a reduced `k`-algebra `S` is geometrically reduced in the sense of
> Definition 030S: `K ⊗[k] S` is reduced for every field extension `K/k`.

```lean
public theorem PerfectField.isReduced_tensorProduct_field (k S : Type*) [Field k] [PerfectField k]
    [CommRing S] [Algebra k S] [IsReduced S] (K : Type*) [Field K] [Algebra k K] :
    IsReduced (K ⊗[k] S)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.45, Tag 05DU](https://stacks.math.columbia.edu/tag/05DU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
