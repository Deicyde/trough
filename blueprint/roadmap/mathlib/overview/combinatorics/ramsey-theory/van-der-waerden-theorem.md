# Van der Waerden theorem

A generalization of Van der Waerden's theorem: if `M` is a finitely colored commutative
monoid, and `S` is a finite subset, then there exists a monochromatic homothetic copy of `S`.

```lean
Combinatorics.exists_mono_homothetic_copy.{u_5, u_6} {M : Type u_5} {κ : Type u_6} [AddCommMonoid M]
  (S : Finset M) [Finite κ] (C : M → κ) : ∃ a > 0, ∃ b c, ∀ s ∈ S, C (a • s + b) = c
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [Hales-Jewett theorem](hales-jewett-theorem.md)

## Sources

- [Mathlib documentation: `Combinatorics.exists_mono_homothetic_copy`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/HalesJewett.html#Combinatorics.exists_mono_homothetic_copy)
- [Source of `Combinatorics.exists_mono_homothetic_copy` in Mathlib/Combinatorics/HalesJewett.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatorics/HalesJewett.lean#L458)
- [Mathlib overview: Combinatorics › Ramsey theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L534)
- [1000+ theorems list: Q764287](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L857)
- [1000+ theorems project: Q764287](https://1000-plus.github.io/all.html?length=-1#Q764287)
- [Wikipedia: Van der Waerden's theorem](https://en.wikipedia.org/wiki/Van_der_Waerden's_theorem)
- [Wikidata: Q764287](https://www.wikidata.org/wiki/Q764287)
