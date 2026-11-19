---
declaration: theorem
origin: cited
lean: FirstOrder.Language.group.realize_vaughtSentence_of_isFreeGroup
statement: formalized
proof: formalized
---

# Lyndon's theorem, as a universal sentence

every free group satisfies the Vaught sentence
`∀ x y z, x ^ 2 * y ^ 2 * z ^ 2 = 1 → x * y * x⁻¹ * y⁻¹ = 1`.

```lean
FirstOrder.Language.group.realize_vaughtSentence_of_isFreeGroup.{u_2} {G : Type u_2} [Group G]
  [IsFreeGroup G] : G ⊨ FirstOrder.Language.group.vaughtSentence
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lyndon's theorem](../../group-theory/free-group/lyndons-theorem.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.group.realize_vaughtSentence_of_isFreeGroup`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Algebra/Group/FreeGroup.html#FirstOrder.Language.group.realize_vaughtSentence_of_isFreeGroup).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.group.realize_vaughtSentence_of_isFreeGroup`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Algebra/Group/FreeGroup.html#FirstOrder.Language.group.realize_vaughtSentence_of_isFreeGroup)
- [Source of `FirstOrder.Language.group.realize_vaughtSentence_of_isFreeGroup` in TauCeti/ModelTheory/Algebra/Group/FreeGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Algebra/Group/FreeGroup.lean#L97)
