---
declaration: section
origin: cited
lean: IsSimpleRing.wedderburn_artin_divisionring_unique, IsBrauerEquivalent.equivalence_and_iff_of_algEquiv, IsBrauerEquivalent.iff_nonempty_algEquiv_of_algEquiv_matrix, IsBrauerEquivalent.exists_divisionRing_unique, IsBrauerEquivalent, BrauerGroup.instCommGroup, BrauerGroup.instUniqueOfIsAlgClosed, Algebra.IsCentralSimple.isSquare_finrank
statement: formalized
proof: formalized
---

# 11.5 The Brauer group of a field

Section 11.5 of the Stacks Project, [Tag 074J](https://stacks.math.columbia.edu/tag/074J). 4 tags here are carried by 7 declarations of the repository (4 in StacksCore and 3 in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 074K, a lemma

[Tag 074K](https://stacks.math.columbia.edu/tag/074K) in the Stacks Project.

**`IsSimpleRing.wedderburn_artin_divisionring_unique`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/SimpleModule/WedderburnArtin.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/SimpleModule/WedderburnArtin.lean#L25). The attribute's comment: “part (ii) and (iii)”.

```lean
theorem wedderburn_artin_divisionring_unique {n n' : ℕ} [NeZero n] [NeZero n']
    {D : Type w} [DivisionRing D] [Algebra k D] {D' : Type w} [DivisionRing D'] [Algebra k D']
    (wdb : A ≃ₐ[k] Matrix (Fin n) (Fin n) D) (wdb' : A ≃ₐ[k] Matrix (Fin n') (Fin n') D') :
    Nonempty (D ≃ₐ[k] D')
```

**`IsBrauerEquivalent.equivalence_and_iff_of_algEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/BrauerGroup/Similarity.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/BrauerGroup/Similarity.lean#L45). The attribute's comment: “part (1): similarity is an equivalence relation on the isomorphism classes of finite central simple k-algebras (an equivalence on `CSA k` invariant under isomorphism)”.

> **Stacks 074K (1).** Similarity is an equivalence relation on finite central simple
> `k`-algebras, and whether `A` and `B` are similar depends only on the isomorphism classes of `A`
> and `B`. Together these say that similarity is an equivalence relation on the set of isomorphism
> classes of finite central simple `k`-algebras.

```lean
theorem equivalence_and_iff_of_algEquiv :
    Equivalence (IsBrauerEquivalent (K := k)) ∧
      ∀ {A A' B B' : CSA.{u, v} k}, Nonempty (A ≃ₐ[k] A') → Nonempty (B ≃ₐ[k] B') →
        (IsBrauerEquivalent A B ↔ IsBrauerEquivalent A' B')
```

**`IsBrauerEquivalent.iff_nonempty_algEquiv_of_algEquiv_matrix`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/BrauerGroup/Similarity.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/BrauerGroup/Similarity.lean#L59). The attribute's comment: “part (3): for A ≃ Mat(n × n, K) and B ≃ Mat(m × m, K') with K, K' skew fields over k, A and B are similar iff K ≃ K' as k-algebras”.

> **Stacks 074K (3).** Let `A ≃ₐ[k] Mₙ(K)` and `B ≃ₐ[k] Mₘ(K')` be finite central simple
> `k`-algebras presented as matrix algebras over division algebras `K` and `K'` over `k`. Then `A`
> and `B` are similar if and only if `K ≃ₐ[k] K'`. The division algebras are automatically finite
> and central over `k`, since `A` and `B` are, so no such hypothesis is needed on them.

```lean
theorem iff_nonempty_algEquiv_of_algEquiv_matrix {A B : CSA.{u, v} k}
    {K : Type w} [DivisionRing K] [Algebra k K] {K' : Type w} [DivisionRing K'] [Algebra k K']
    {n m : ℕ} [NeZero n] [NeZero m]
    (eA : A ≃ₐ[k] Matrix (Fin n) (Fin n) K) (eB : B ≃ₐ[k] Matrix (Fin m) (Fin m) K') :
    IsBrauerEquivalent A B ↔ Nonempty (K ≃ₐ[k] K')
```

**`IsBrauerEquivalent.exists_divisionRing_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/BrauerGroup/Similarity.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/BrauerGroup/Similarity.lean#L85). The attribute's comment: “part (2): every similarity class contains a finite central skew field over k, unique up to isomorphism”.

> **Stacks 074K (2).** Every similarity class of finite central simple `k`-algebras contains a
> finite central division algebra `D` over `k`, and `D` is unique up to isomorphism: every finite
> central division algebra over `k` similar to `A` is isomorphic to `D`.

```lean
theorem exists_divisionRing_unique (A : CSA.{u, v} k) :
    ∃ (D : Type v) (_ : DivisionRing D) (_ : Algebra k D) (_ : Algebra.IsCentral k D)
      (_ : FiniteDimensional k D), IsBrauerEquivalent A ⟨.of k D⟩ ∧
        ∀ (D' : Type v) [DivisionRing D'] [Algebra k D'] [Algebra.IsCentral k D']
          [FiniteDimensional k D'], IsBrauerEquivalent A ⟨.of k D'⟩ → Nonempty (D ≃ₐ[k] D')
```

Declarations registered for the tag:

- [`IsBrauerEquivalent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsBrauerEquivalent#doc) registered with `add_to_stacks` in [StacksCore/Algebra/BrauerGroup/Basic.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/BrauerGroup/Basic.lean#L24) (StacksCore): “part i”.

## Tag 074L, a definition

[Tag 074L](https://stacks.math.columbia.edu/tag/074L) in the Stacks Project.

**`BrauerGroup.instCommGroup`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/Algebra/BrauerGroup/Basic.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/BrauerGroup/Basic.lean#L214). References: SGA 4½ Arcata (3.1), “abelian group structure”.

```lean
instance instCommGroup : CommGroup (BrauerGroup k)
```

## Tag 074M, a lemma

[Tag 074M](https://stacks.math.columbia.edu/tag/074M) in the Stacks Project.

**`BrauerGroup.instUniqueOfIsAlgClosed`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/Algebra/BrauerGroup/AlgClosed.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/BrauerGroup/AlgClosed.lean#L28). References: SGA 4½ Arcata (3.2.2), “special case”.

```lean
instance instUniqueOfIsAlgClosed : Unique (BrauerGroup k)
```

## Tag 074N, a lemma

[Tag 074N](https://stacks.math.columbia.edu/tag/074N) in the Stacks Project.

**`Algebra.IsCentralSimple.isSquare_finrank`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Split/Basic.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Split/Basic.lean#L155).

> The dimension of a central simple algebra is a perfect square.

```lean
theorem isSquare_finrank [IsSimpleRing A] [Algebra.IsCentral K A] [FiniteDimensional K A] :
    IsSquare (Module.finrank K A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 11.5, Tag 074J](https://stacks.math.columbia.edu/tag/074J)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
