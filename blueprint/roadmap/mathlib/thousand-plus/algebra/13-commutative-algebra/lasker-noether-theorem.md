# Lasker–Noether theorem

Mathlib states this as `Submodule.isPrimary_decomposition_pairwise_ne_radical`.

```lean
Submodule.isPrimary_decomposition_pairwise_ne_radical.{u_1, u_2} {R : Type u_1} {M : Type u_2}
  [CommSemiring R] [AddCommMonoid M] [_root_.Module R M] {N : Submodule R M}
  {s : Finset (Submodule R M)} (hs : s.inf id = N)
  (hs' : ∀ ⦃J : Submodule R M⦄, J ∈ s → J.IsPrimary) :
  ∃ t,
    t.inf id = N ∧
      (∀ ⦃J : Submodule R M⦄, J ∈ t → J.IsPrimary) ∧
        (↑t).Pairwise (Function.onFun (fun x1 x2 => x1 ≠ x2) fun J => (J.colon Set.univ).radical)
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Ideal of a commutative ring](../../../overview/general-algebra/ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `Submodule.isPrimary_decomposition_pairwise_ne_radical`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Lasker.html#Submodule.isPrimary_decomposition_pairwise_ne_radical)
- [Source of `Submodule.isPrimary_decomposition_pairwise_ne_radical` in Mathlib/RingTheory/Lasker.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/Lasker.lean#L62)
- [1000+ theorems list: Q172298](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L72)
- [1000+ theorems project: Q172298](https://1000-plus.github.io/all.html?length=-1#Q172298)
- [Wikipedia: Lasker–Noether theorem](https://en.wikipedia.org/wiki/Lasker%E2%80%93Noether_theorem)
- [Wikidata: Q172298](https://www.wikidata.org/wiki/Q172298)
