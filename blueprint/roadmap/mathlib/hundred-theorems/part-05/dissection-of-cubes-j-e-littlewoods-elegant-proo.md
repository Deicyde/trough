---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Theorems100.«82».cannot_cube_a_cube
mathlib_file: Archive/Wiedijk100Theorems/CubingACube.lean
---

# Dissection of Cubes (J.E. Littlewood’s ‘elegant’ proof)

**Dissection of Cubes**: A cube cannot be cubed.

```lean
Theorems100.«82».cannot_cube_a_cube {n : ℕ} :
  n ≥ 3 →
    ∀ {s : Set (Theorems100.«82».Cube n)},
      s.Finite →
        s.Nontrivial →
          s.PairwiseDisjoint Theorems100.«82».Cube.toSet →
            ⋃ c ∈ s, c.toSet = Theorems100.«82».Cube.unitCube.toSet →
              Set.InjOn Theorems100.«82».Cube.w s → False
```

## Depends on

- [Real number](../../overview/general-algebra/numbers/real-number.md)
- [Set](../../overview/data-structures/sets/set.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Group](../../overview/general-algebra/group-theory/part-01/group.md)
- [Group morphism](../../overview/general-algebra/group-theory/part-01/group-morphism.md)
- [Invertible elements](../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Order (Real numbers)](../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)
- [Permutation group of a type](../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Product of rings](../../undergraduate/ring-theory/fundamentals/product-of-rings.md)
- [Ring structure $\Z$](../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `Theorems100.«82».cannot_cube_a_cube`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/CubingACube.html#Theorems100.%C2%AB82%C2%BB.cannot_cube_a_cube)
- [Source of `Theorems100.«82».cannot_cube_a_cube` in Archive/Wiedijk100Theorems/CubingACube.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/CubingACube.lean#L537)
- [Freek Wiedijk's 100 theorems, no. 82](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L421)
