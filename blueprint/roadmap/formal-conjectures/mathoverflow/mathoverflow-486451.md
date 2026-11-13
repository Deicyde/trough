---
declaration: theorem
origin: cited
lean: Mathoverflow486451.exists_semiring_unique_left_maximal_not_unique_right_maximal, Mathoverflow486451.exists_semiring_unique_left_right_maximal_ne
statement: formalized
---

# Mathoverflow 486451

> *Reference:* [mathoverflow/486451](https://mathoverflow.net/questions/486451)
> asked by user [*Junyan Xu*](https://mathoverflow.net/users/3332/junyan-xu)

*Quoted from [FormalConjectures/Mathoverflow/486451.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/486451.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved.

## `Mathoverflow486451.exists_semiring_unique_left_maximal_not_unique_right_maximal`

Solved: stated here without proof.

> There exists a semiring with a unique left maximal ideal but more than one right maximal ideals.

```lean
theorem exists_semiring_unique_left_maximal_not_unique_right_maximal :
    ∃ (R : Type) (_ : Semiring R), (∃! I : Ideal R, I.IsMaximal) ∧
      ∃ I J : Ideal Rᵐᵒᵖ, I.IsMaximal ∧ J.IsMaximal ∧ I ≠ J
```

Category `research solved`; AMS [16 Associative rings and algebras](../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Mathoverflow/486451.lean, line 32](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/486451.lean#L32).

## `Mathoverflow486451.exists_semiring_unique_left_right_maximal_ne`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/f7502b9ed3e32d193ab8fee53d2e28f7d67f2dc3/FormalConjectures/Mathoverflow/486451.lean#L333](https://github.com/google-deepmind/formal-conjectures/blob/f7502b9ed3e32d193ab8fee53d2e28f7d67f2dc3/FormalConjectures/Mathoverflow/486451.lean#L333).

> There exists a semiring with a unique left maximal ideal and a unique right maximal ideal
> which are not the same as sets.
>
> This has been shown by Goran Žužić and Moritz Firsching using an experimental pipeline:
> An example is the monoid algebra of the monoid of maps from $\mathbb{N}$ to $\mathbb{N}$
> over $\mathbb{N}$.

```lean
theorem exists_semiring_unique_left_right_maximal_ne :
    ∃ (R : Type) (_ : Semiring R) (hI : ∃! I : Ideal R, I.IsMaximal)
      (hJ : ∃! J : Ideal Rᵐᵒᵖ, J.IsMaximal),
        (hI.choose : Set R) ≠ MulOpposite.op ⁻¹' hJ.choose
```

Category `research solved`; AMS [16 Associative rings and algebras](../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Mathoverflow/486451.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/486451.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/486451.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/486451.lean)
- [mathoverflow/486451](https://mathoverflow.net/questions/486451)
