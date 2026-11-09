# Jacobson density theorem

Mathlib states this as `jacobson_density`.

```lean
jacobson_density.{u_2, u_4} {R : Type u_2} [Ring R] {M : Type u_4} [AddCommGroup M]
  [_root_.Module R M] [IsSemisimpleModule R M] (f : Module.End (Module.End R M) M) (s : Finset M) :
  ∃ r, ∀ m ∈ s, f m = r • m
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Proof depends on

- [Finitely supported function](../../../overview/data-structures/maps/finitely-supported-function.md)
- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Quotient space (Fundamentals)](../../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `jacobson_density`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/SimpleModule/Basic.html#jacobson_density)
- [Source of `jacobson_density` in Mathlib/RingTheory/SimpleModule/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/SimpleModule/Basic.lean#L562)
- [1000+ theorems list: Q17098298](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L4145)
- [1000+ theorems project: Q17098298](https://1000-plus.github.io/all.html?length=-1#Q17098298)
- [Wikipedia: Jacobson density theorem](https://en.wikipedia.org/wiki/Jacobson_density_theorem)
- [Wikidata: Q17098298](https://www.wikidata.org/wiki/Q17098298)
