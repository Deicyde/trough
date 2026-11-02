---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: hahnEmbedding_isOrderedAddMonoid
mathlib_file: Mathlib/RingTheory/HahnSeries/HahnEmbedding.lean
---

# Hahn embedding theorem

**Hahn embedding theorem**

For a linearly ordered additive group `M`, there exists an injective `OrderAddMonoidHom` from `M` to
`Lex ℝ⟦FiniteArchimedeanClass M⟧` that sends each `a : M` to an element of the `a`-Archimedean class
of the Hahn series.

```lean
hahnEmbedding_isOrderedAddMonoid.{u_1} (M : Type u_1) [AddCommGroup M] [LinearOrder M]
  [IsOrderedAddMonoid M] :
  ∃ f,
    Function.Injective ⇑f ∧
      ∀ (a : M),
        ArchimedeanClass.mk a = (FiniteArchimedeanClass.withTopOrderIso M) (ofLex (f a)).orderTop
```

## Depends on

- [Real number](../../../overview/general-algebra/numbers/real-number.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Field of fractions of an integral domain](../../../overview/general-algebra/field-theory/field-of-fractions-of-an-integral-domain.md)
- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `hahnEmbedding_isOrderedAddMonoid`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/HahnSeries/HahnEmbedding.html#hahnEmbedding_isOrderedAddMonoid)
- [Source of `hahnEmbedding_isOrderedAddMonoid` in Mathlib/RingTheory/HahnSeries/HahnEmbedding.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/HahnSeries/HahnEmbedding.lean#L53)
- [1000+ theorems list: Q5638886](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3323)
- [1000+ theorems project: Q5638886](https://1000-plus.github.io/all.html?length=-1#Q5638886)
- [Wikipedia: Hahn embedding theorem](https://en.wikipedia.org/wiki/Hahn_embedding_theorem)
- [Wikidata: Q5638886](https://www.wikidata.org/wiki/Q5638886)
