---
declaration: section
origin: cited
lean: DirectLimit.instIsGeometricallyReduced, geometricallyReduced_localization, geometricallyReduced_polynomial, not_isReduced_of_not_isReduced, exists_zerodivisor_of_exists_zerodivisor, exists_idempotent_of_exists_idempotent, Algebra.IsGeometricallyReduced.isReduced_tensorProduct, Algebra.isReduced_tensorProduct_of_isSeparableExtension_or_isSeparablyGenerated
statement: formalized
proof: formalized
---

# 10.43 Geometrically reduced algebras

Section 10.43 of the Stacks Project, [Tag 05DS](https://stacks.math.columbia.edu/tag/05DS). 8 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 030T, a lemma

[Tag 030T](https://stacks.math.columbia.edu/tag/030T) in the Stacks Project.

**`DirectLimit.instIsGeometricallyReduced`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyReduced/DirectLimit.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyReduced/DirectLimit.lean#L303). The attribute's comment: “Part (3): a directed colimit of geometrically reduced algebras is geometrically reduced, stated for `DirectLimit` of a directed system of algebras over a commutative base ring. Parts (1) and (2) are `Algebra.IsGeometricallyReduced.of_injective` and `Algebra.IsGeometricallyReduced.of_forall_fg`; part (4) is Lemma 04KN.”.

> **Stacks 030T (3).** A directed colimit of geometrically reduced `R`-algebras is geometrically
> reduced over `R`.

```lean
public instance instIsGeometricallyReduced
    {R : Type*} [CommRing R] {ι : Type*} [Preorder ι] [IsDirectedOrder ι] [Nonempty ι]
    {G : ι → Type*} [∀ i, Ring (G i)] [∀ i, Algebra R (G i)]
    {T : ∀ ⦃i j : ι⦄, i ≤ j → Type*} {f : ∀ i j (h : i ≤ j), T h}
    [∀ i j (h : i ≤ j), FunLike (T h) (G i) (G j)]
    [∀ i j (h : i ≤ j), AlgHomClass (T h) R (G i) (G j)]
    [DirectedSystem G (f · · ·)]
    [∀ i, Algebra.IsGeometricallyReduced R (G i)] :
    Algebra.IsGeometricallyReduced R (DirectLimit G f)
```

## Tag 04KN, a lemma

[Tag 04KN](https://stacks.math.columbia.edu/tag/04KN) in the Stacks Project.

**`geometricallyReduced_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyReduced/Basic.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyReduced/Basic.lean#L188). The attribute's comment: “(1)”. References: EGA IV (7.3.9), “(ii)”.

> If `R` is geometrically reduced over the field `k` and `A` is a localization of `R` at a
> multiplicative subset `M ⊆ R`, carrying the induced `k`-algebra structure, then `A` is
> geometrically reduced over `k`.
>
> Fix a field extension `K/k`; then `K ⊗[k] R` is reduced. The key base-change fact is that
> `K ⊗[k] A` is isomorphic to a localization of `K ⊗[k] R`: viewing `K ⊗[k] R` as an
> `R`-algebra, `(K ⊗[k] R) ⊗[R] A` is a localization of `K ⊗[k] R` at the image submonoid
> `Algebra.algebraMapSubmonoid (K ⊗[k] R) M`, and cancelling the base change gives a
> `K`-algebra isomorphism `(K ⊗[k] R) ⊗[R] A ≃ₐ[K] K ⊗[k] A`. A localization of a reduced ring
> is reduced, so `(K ⊗[k] R) ⊗[R] A` is reduced and reducedness transfers back to `K ⊗[k] A`
> along that isomorphism. As `K/k` was arbitrary, `A` is geometrically reduced over `k`.

```lean
theorem geometricallyReduced_localization
    (k : Type u) [Field k] (R : Type v) [CommRing R] [Algebra k R]
    (M : Submonoid R) (A : Type v) [CommRing A] [Algebra R A] [IsLocalization M A]
    [Algebra k A] [IsScalarTower k R A]
    (hR : GeometricallyReduced.{u, v, w} k R) :
    GeometricallyReduced.{u, v, w} k A
```

**`geometricallyReduced_polynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyReduced/Basic.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyReduced/Basic.lean#L220). The attribute's comment: “(2)”. References: EGA IV (4.6.21), “4.6.21(ii), special case”; EGA IV (4.6.5), “(ii), special case”.

> If `R` is geometrically reduced over the field `k`, then so is the polynomial ring `R[x]`
> in one variable.
>
> Fix a field extension `K/k`. Then `K ⊗[k] R` is reduced, hence so is the polynomial ring
> `(K ⊗[k] R)[X]`, and transferring reducedness backward along the ring isomorphism
> `K ⊗[k] R[X] ≃+* (K ⊗[k] R)[X]` shows `K ⊗[k] R[X]` is reduced. As `K/k` was arbitrary,
> `R[X]` is geometrically reduced.

```lean
theorem geometricallyReduced_polynomial
    (k : Type u) [Field k] (R : Type v) [CommRing R] [Algebra k R]
    (hR : GeometricallyReduced.{u, v, w} k R) :
    GeometricallyReduced.{u, v, w} k (Polynomial R)
```

## Tag 00I3, a lemma

[Tag 00I3](https://stacks.math.columbia.edu/tag/00I3) in the Stacks Project.

**`not_isReduced_of_not_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TensorProduct/Reduced.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/TensorProduct/Reduced.lean#L122). The attribute's comment: “nonreduced”.

> **Stacks 00I3** (part 1). If `R ⊗[k] S` is nonreduced, then there exist finitely generated
> subalgebras `R' ⊆ R`, `S' ⊆ S` such that `R' ⊗[k] S'` is not reduced.

```lean
theorem not_isReduced_of_not_isReduced (h : ¬ IsReduced (R ⊗[k] S)) :
    ∃ (R' : Subalgebra k R) (S' : Subalgebra k S), R'.FG ∧ S'.FG ∧
      ¬ IsReduced (R' ⊗[k] S')
```

**`exists_zerodivisor_of_exists_zerodivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TensorProduct/Reduced.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/TensorProduct/Reduced.lean#L144). The attribute's comment: “zerodivisor”.

> **Stacks 00I3** (part 2). If `R ⊗[k] S` contains a nonzero zerodivisor, then there exist
> finitely generated subalgebras `R' ⊆ R`, `S' ⊆ S` such that `R' ⊗[k] S'` contains a nonzero
> zerodivisor.

```lean
theorem exists_zerodivisor_of_exists_zerodivisor
    (h : ∃ x : R ⊗[k] S, x ≠ 0 ∧ ∃ y : R ⊗[k] S, y ≠ 0 ∧ x * y = 0) :
    ∃ (R' : Subalgebra k R) (S' : Subalgebra k S), R'.FG ∧ S'.FG ∧
      ∃ x : R' ⊗[k] S', x ≠ 0 ∧ ∃ y : R' ⊗[k] S', y ≠ 0 ∧ x * y = 0
```

**`exists_idempotent_of_exists_idempotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TensorProduct/Reduced.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/TensorProduct/Reduced.lean#L167). The attribute's comment: “idempotent”.

> **Stacks 00I3** (part 3). If `R ⊗[k] S` contains a nontrivial idempotent, then there exist
> finitely generated subalgebras `R' ⊆ R`, `S' ⊆ S` such that `R' ⊗[k] S'` contains a nontrivial
> idempotent.

```lean
theorem exists_idempotent_of_exists_idempotent
    (h : ∃ e : R ⊗[k] S, e * e = e ∧ e ≠ 0 ∧ e ≠ 1) :
    ∃ (R' : Subalgebra k R) (S' : Subalgebra k S), R'.FG ∧ S'.FG ∧
      ∃ e : R' ⊗[k] S', e * e = e ∧ e ≠ 0 ∧ e ≠ 1
```

## Tag 034N, a lemma

[Tag 034N](https://stacks.math.columbia.edu/tag/034N) in the Stacks Project.

**`Algebra.IsGeometricallyReduced.isReduced_tensorProduct`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyReduced/TensorProduct.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyReduced/TensorProduct.lean#L113). The attribute's comment: “Stated with Mathlib's `Algebra.IsGeometricallyReduced` in place of the source's Definition 030S, the two being equivalent by Lemma 030V; as an instance, since both hypotheses are classes.”.

> The tensor product of a reduced `k`-algebra `R` with a geometrically reduced `k`-algebra `S`
> is reduced.

```lean
public instance Algebra.IsGeometricallyReduced.isReduced_tensorProduct
    (k R S : Type*) [Field k] [CommRing R] [Algebra k R] [IsReduced R]
    [CommRing S] [Algebra k S] [Algebra.IsGeometricallyReduced k S] :
    IsReduced (R ⊗[k] S)
```

## Tag 030U, a lemma

[Tag 030U](https://stacks.math.columbia.edu/tag/030U) in the Stacks Project.

**`Algebra.isReduced_tensorProduct_of_isSeparableExtension_or_isSeparablyGenerated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyReduced/TensorProduct.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyReduced/TensorProduct.lean#L194). The attribute's comment: “Stated with the two notions of Definition 030O as a disjunctive hypothesis, as in the source: separably generated implies separable is Lemma 030X, whose proof uses this lemma.”. References: EGA 0 (23.1.7), “partial”; EGA IV (4.3.5), “more general”; EGA IV (4.3.6), “special case”.

> Let `k` be a field, let `S` be a reduced `k`-algebra and let `K/k` be a field extension which
> is either separable or separably generated. Then `K ⊗[k] S` is reduced.

```lean
public theorem Algebra.isReduced_tensorProduct_of_isSeparableExtension_or_isSeparablyGenerated
    {k K S : Type*} [Field k] [Field K] [Algebra k K] [CommRing S] [Algebra k S] [IsReduced S]
    (hK : Algebra.IsSeparableExtension k K ∨ Algebra.IsSeparablyGenerated k K) :
    IsReduced (K ⊗[k] S)
```

## Tag 07K2, a lemma

[Tag 07K2](https://stacks.math.columbia.edu/tag/07K2) in the Stacks Project.

**`Algebra.IsGeometricallyReduced.of_forall_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nilpotent/GeometricallyReduced.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/GeometricallyReduced.lean#L131). The attribute's comment: “Stated with Mathlib's `Algebra.IsGeometricallyReduced` in place of the source's Definition 030S, the two being equivalent by Lemma 030V, and with the concrete localization `Localization.AtPrime p` for the source's `S_𝔭`.”.

> Let `k` be a field and let `S` be a reduced `k`-algebra such that the localization
> `Localization.AtPrime p` is geometrically reduced over `k` for every minimal prime `p` of `S`. Then
> `S` is geometrically reduced over `k`.

```lean
public theorem Algebra.IsGeometricallyReduced.of_forall_minimalPrimes {k : Type u} {S : Type v}
    [Field k] [CommRing S] [Algebra k S] [IsReduced S]
    (H : ∀ (p : Ideal S) [p.IsPrime], p ∈ minimalPrimes S →
      Algebra.IsGeometricallyReduced k (Localization.AtPrime p)) :
    Algebra.IsGeometricallyReduced k S
```

## Tag 0C2X, a lemma

[Tag 0C2X](https://stacks.math.columbia.edu/tag/0C2X) in the Stacks Project.

**`exists_isLocalization_lmul'_of_isSeparable_isAlgebraic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/SeparableAlgebraic/Localization.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/SeparableAlgebraic/Localization.lean#L94).

> Stacks Tag 0C2X (Lemma 10.43.8), primary `IsLocalization` formulation.
> For a separable algebraic field extension `k'/k`, equipping `k'` with the
> `(k' ⊗_k k')`-algebra structure given by the multiplication map
> `m = Algebra.TensorProduct.lmul' k`, there is a submonoid `S ⊆ k' ⊗_k k'` such
> that `k'` is the localization of `k' ⊗_k k'` at `S`.

```lean
theorem exists_isLocalization_lmul'_of_isSeparable_isAlgebraic
    (k k' : Type*) [Field k] [Field k'] [Algebra k k']
    [Algebra.IsAlgebraic k k'] [Algebra.IsSeparable k k'] :
    letI : Algebra (k' ⊗[k] k') k' :=
      RingHom.toAlgebra (Algebra.TensorProduct.lmul' (R := k) (S := k')).toRingHom
    ∃ S : Submonoid (k' ⊗[k] k'), IsLocalization S k'
```

## Tag 0C2Y, a lemma

[Tag 0C2Y](https://stacks.math.columbia.edu/tag/0C2Y) in the Stacks Project.

**`Algebra.isGeometricallyReduced_iff_of_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyReduced/Separable.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyReduced/Separable.lean#L47).

> **Stacks 0C2Y.** For a separable algebraic field extension `k'/k`, a `k'`-algebra is
> geometrically reduced over `k` if and only if it is geometrically reduced over `k'`.

```lean
theorem Algebra.isGeometricallyReduced_iff_of_isSeparable (k k' A : Type*) [Field k] [Field k']
    [CommRing A] [Algebra k k'] [Algebra k' A] [Algebra k A] [IsScalarTower k k' A]
    [Algebra.IsSeparable k k'] :
    Algebra.IsGeometricallyReduced k A ↔ Algebra.IsGeometricallyReduced k' A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.43, Tag 05DS](https://stacks.math.columbia.edu/tag/05DS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
