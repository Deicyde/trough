---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: AddCommGroup.equiv_free_prod_directSum_zmod
mathlib_file: Mathlib/GroupTheory/FiniteAbelian/Basic.lean
---

# Structure of finitely generated abelian groups

**Structure theorem of finitely generated abelian groups** : Any finitely generated abelian
group is the product of a power of `ℤ` and a direct sum of some `ZMod (p i ^ e i)` for some
prime powers `p i ^ e i`.

```lean
AddCommGroup.equiv_free_prod_directSum_zmod.{u} (G : Type u) [AddCommGroup G] [hG : AddGroup.FG G] :
  ∃ n ι x p,
    ∃ (_ : ∀ (i : ι), Nat.Prime (p i)),
      ∃ e, Nonempty (G ≃+ (Fin n →₀ ℤ) × DirectSum ι fun i => ZMod (p i ^ e i))
```

## Depends on

- [Finitely supported function](../../../data-structures/maps/finitely-supported-function.md)
- [Irreducible element](../../divisibility-in-integral-domains/irreducible-element.md)
- [Module](../../../linear-algebra/fundamentals/module.md)
- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [$\Z$ is a Euclidean ring](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/z-is-a-euclidean-ring.md)
- [Structure theorem](../../../linear-algebra/finitely-generated-modules-over-a-pid/structure-theorem.md)
- [The Fundamental Theorem of Arithmetic](../../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `AddCommGroup.equiv_free_prod_directSum_zmod`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FiniteAbelian/Basic.html#AddCommGroup.equiv_free_prod_directSum_zmod)
- [Source of `AddCommGroup.equiv_free_prod_directSum_zmod` in Mathlib/GroupTheory/FiniteAbelian/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/FiniteAbelian/Basic.lean#L116)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L58)
- [Mathlib undergraduate list: Group Theory › Abelian group](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L95)
