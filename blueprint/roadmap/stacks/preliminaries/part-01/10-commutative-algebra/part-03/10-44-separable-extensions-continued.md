---
declaration: section
origin: cited
lean: Algebra.isSeparableExtension_tfae, exists_isTranscendenceBasis_and_isSeparable_of_isSeparable_adjoin_of_essFiniteType, Algebra.isGeometricallyReduced_tfae
statement: formalized
proof: formalized
---

# 10.44 Separable extensions, continued

Section 10.44 of the Stacks Project, [Tag 05DT](https://stacks.math.columbia.edu/tag/05DT). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 030W, a lemma

[Tag 030W](https://stacks.math.columbia.edu/tag/030W) in the Stacks Project.

**`Algebra.isSeparableExtension_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/Separable/TFAE.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/Separable/TFAE.lean#L194). The attribute's comment: “Stated for the exponential characteristic, so that characteristic zero is the case `p = 1`, where all four conditions hold; the source assumes `p > 0`. Condition (2) quantifies over arbitrary, not just finite, linearly independent subsets. See the module docstring.”.

> **Stacks 030W.** Let `k` be a field of exponential characteristic `p` and let `K/k` be a field
> extension. The following are equivalent: `K` is separable over `k` (Definition
> [Stacks 030O](https://stacks.math.columbia.edu/tag/030O)); for every `k`-linearly independent
> subset `s` of `K` the set of `p`-th powers of elements of `s` is `k`-linearly independent; the ring
> `K ⊗_k k^{1/p}` is reduced; and `K` is geometrically reduced over `k`.

```lean
public theorem Algebra.isSeparableExtension_tfae (k K : Type*) [Field k] [Field K] [Algebra k K]
    (p : ℕ) [ExpChar k p] :
    List.TFAE
      [Algebra.IsSeparableExtension k K,
        ∀ s : Set K, LinearIndepOn k _root_.id s → LinearIndepOn k (· ^ p) s,
        IsReduced (K ⊗[k] AdjoinPthRoots k),
        Algebra.IsGeometricallyReduced k K]
```

## Tag 030X, a lemma

[Tag 030X](https://stacks.math.columbia.edu/tag/030X) in the Stacks Project.

**`exists_isTranscendenceBasis_and_isSeparable_of_isSeparable_adjoin_of_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/Separable/Basic.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/Separable/Basic.lean#L88).

> A separably generated field extension is separable. Let `K/k` be a field extension with a
> separating transcendence basis `s`, that is, a transcendence basis of `K/k` such that `K` is
> separable algebraic over `k(s)`. Then every subextension `k ⊆ L ⊆ K` which is finitely generated
> over `k` again has a separating transcendence basis: there is a finite transcendence basis `t` of
> `L/k` such that `L` is separable algebraic over `k(t)`.

```lean
public theorem exists_isTranscendenceBasis_and_isSeparable_of_isSeparable_adjoin_of_essFiniteType
    {k K L : Type*} [Field k] [Field K] [Field L] [Algebra k K] [Algebra k L] [Algebra L K]
    [IsScalarTower k L K] [Algebra.EssFiniteType k L] {s : Set K}
    (hs : IsTranscendenceBasis k ((↑) : s → K))
    (hsep : Algebra.IsSeparable (IntermediateField.adjoin k s) K) :
    ∃ t : Finset L,
      IsTranscendenceBasis k ((↑) : t → L) ∧
        Algebra.IsSeparable (IntermediateField.adjoin k (t : Set L)) L
```

## Tag 030V, a lemma

[Tag 030V](https://stacks.math.columbia.edu/tag/030V) in the Stacks Project.

**`Algebra.isGeometricallyReduced_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyReduced/TFAE.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyReduced/TFAE.lean#L198). The attribute's comment: “The source's five conditions in its order, with its definition of geometric reducedness spelled out as item (5), plus item (6), Mathlib's `Algebra.IsGeometricallyReduced`; `k^{1/p}` is `AdjoinPthRoots k`, and the perfect and algebraic closures are taken abstractly, as `IsPerfectClosure` and `IsAlgClosure`.”.

> Let `k` be a field of exponential characteristic `p` and let `S` be a
> commutative `k`-algebra. The following are equivalent:
> (1) `k' ⊗[k] S` is reduced for every finite purely inseparable extension `k'/k`;
> (2) `k^{1/p} ⊗[k] S` is reduced, where `k^{1/p} = AdjoinPthRoots k`;
> (3) `k^{perf} ⊗[k] S` is reduced for a perfect closure `k^{perf}` of `k`;
> (4) `K ⊗[k] S` is reduced for an algebraic closure `K` of `k`;
> (5) `L ⊗[k] S` is reduced for every field extension `L/k`;
> (6) `Algebra.IsGeometricallyReduced k S`.

```lean
public theorem isGeometricallyReduced_tfae
    (k : Type u) [Field k] (p : ℕ) [ExpChar k p] (S : Type v) [CommRing S] [Algebra k S]
    (kperf : Type w) [Field kperf] [Algebra k kperf] [ExpChar kperf p] [PerfectRing kperf p]
    [IsPerfectClosure (algebraMap k kperf) p]
    (K : Type w') [Field K] [Algebra k K] [IsAlgClosure k K] :
    [∀ (k' : Type u) [Field k'] [Algebra k k'] [FiniteDimensional k k']
        [IsPurelyInseparable k k'], IsReduced (k' ⊗[k] S),
      IsReduced (AdjoinPthRoots k ⊗[k] S),
      IsReduced (kperf ⊗[k] S),
      IsReduced (K ⊗[k] S),
      ∀ (L : Type u) [Field L] [Algebra k L], IsReduced (L ⊗[k] S),
      IsGeometricallyReduced k S].TFAE
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.44, Tag 05DT](https://stacks.math.columbia.edu/tag/05DT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
