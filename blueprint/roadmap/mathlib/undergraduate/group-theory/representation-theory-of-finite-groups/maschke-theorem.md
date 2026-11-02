---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MonoidAlgebra.Submodule.exists_isCompl
mathlib_file: Mathlib/RepresentationTheory/Maschke.lean
---

# Maschke theorem

Mathlib states this as `MonoidAlgebra.Submodule.exists_isCompl`.

```lean
MonoidAlgebra.Submodule.exists_isCompl.{u_1, u_2, u_3} {k : Type u_1} [Field k] {G : Type u_2}
  [Finite G] [NeZero ↑(Nat.card G)] [Group G] {V : Type u_3} [AddCommGroup V]
  [_root_.Module (MonoidAlgebra k G) V] (p : Submodule (MonoidAlgebra k G) V) : ∃ q, IsCompl p q
```

## Depends on

- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Finitely supported function](../../../overview/data-structures/maps/finitely-supported-function.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Ring morphism](../../../overview/general-algebra/rings/ring-morphism.md)
- [Sum of subspaces](../../linear-algebra/fundamentals/sum-of-subspaces.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Kernel of a linear map](../../linear-algebra/fundamentals/kernel-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `MonoidAlgebra.Submodule.exists_isCompl`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Maschke.html#MonoidAlgebra.Submodule.exists_isCompl)
- [Source of `MonoidAlgebra.Submodule.exists_isCompl` in Mathlib/RepresentationTheory/Maschke.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RepresentationTheory/Maschke.lean#L159)
- [Mathlib undergraduate list: Group Theory › Representation theory of finite groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L114)
- [1000+ theorems list: Q656198](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L691)
- [1000+ theorems project: Q656198](https://1000-plus.github.io/?length=-1#Q656198)
- [Wikipedia: Maschke's theorem](https://en.wikipedia.org/wiki/Maschke's_theorem)
- [Wikidata: Q656198](https://www.wikidata.org/wiki/Q656198)
