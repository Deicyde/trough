---
declaration: theorem
origin: cited
lean: Mathoverflow507128.exists_isFractionRing_self_ideal_ne_top_invertible
statement: formalized
---

# Mathoverflow 507128

> *Reference:* [mathoverflow/507128](https://mathoverflow.net/questions/507128/embeddability-order-on-picard-groups)
> asked by user [*Junyan Xu*](https://mathoverflow.net/users/3332/junyan-xu)

*Quoted from [FormalConjectures/Mathoverflow/507128.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/507128.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Mathoverflow507128.exists_isFractionRing_self_ideal_ne_top_invertible`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/mo507128-lean/blob/e9507429c01c4288089e4af1c92a03b7d1e17f74/MO507128.lean#L265](https://github.com/KitaKen1/mo507128-lean/blob/e9507429c01c4288089e4af1c92a03b7d1e17f74/MO507128.lean#L265).

> There exists a proper ideal `I` in a (commutative) total ring `R` of fractions that is an invertible module.
> If `I ⊊ R` is such an example, `I` must have infinite order in the Picard group.
> Moreover, `R` must not be Noetherian (otherwise it must be semi-local and therefore have trivial Picard group).
>
> The linked formal proof gives the following explicit construction.
>
> Let `D = ℂ[X, Y] / (Y² - X³)` be the coordinate ring of the cuspidal cubic.
> Let `P = (X - 1, Y - 1)`, which is an invertible ideal.
> Let `M` be the direct sum of the evaluation fibres at cusp parameters `r ≠ 1`.
> Form the idealization `R = D ⋉ M`.
> The desired ideal is the range of the multiplication map `R ⊗[D] P → R`.

```lean
theorem exists_isFractionRing_self_ideal_ne_top_invertible :
    ∃ (R : Type) (_ : CommRing R) (_ : IsFractionRing R R) (I : Ideal R),
      I ≠ ⊤ ∧ Module.Invertible R I
```

Category `research solved`; AMS [13 Commutative algebra](../by-subject/part-01/13-commutative-algebra/README.md). Declared in [FormalConjectures/Mathoverflow/507128.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/507128.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/507128.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/507128.lean)
- [mathoverflow/507128](https://mathoverflow.net/questions/507128/embeddability-order-on-picard-groups)
