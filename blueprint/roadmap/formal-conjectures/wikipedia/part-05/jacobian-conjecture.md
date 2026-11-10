---
declaration: theorem
origin: cited
lean: JacobianConjecture.jacobian_conjecture, JacobianConjecture.jacobian_conjecture_two_variables
statement: formalized
---

# Jacobian conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Jacobian_conjecture)

*Quoted from [FormalConjectures/Wikipedia/JacobianConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/JacobianConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement and 5 API statements, counted here but not shown.

## `JacobianConjecture.jacobian_conjecture`

Proved here.

> The **Jacobian Conjecture**: any regular function
> (i.e. vector valued polynomial function from) `kⁿ → kᵐ`
> whose Jacobian is a non-zero constant has an inverse that
> is given by a regular function, where `k` is a field of characteristic `0`.
>
> This is false: `F` has Jacobian determinant `1` but identifies
> two distinct points, so it admits no inverse. This counterexample works in all characteristics.

```lean
theorem jacobian_conjecture {k : Type} [CommRing k] [Nontrivial k] :
    ¬ ∀ {σ : Type} [Fintype σ] [DecidableEq σ], JacobianConjectureProp k σ
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/JacobianConjecture.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/JacobianConjecture.lean#L105).

## `JacobianConjecture.jacobian_conjecture_two_variables`

Open: stated without proof.

> Does the Jacobian conjecture hold in the two variable case?

```lean
theorem jacobian_conjecture_two_variables :
    ∀ {k : Type} [Field k] [CharZero k], JacobianConjectureProp k (Fin 2)
```

Category `research open`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/JacobianConjecture.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/JacobianConjecture.lean#L118).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/JacobianConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/JacobianConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Jacobian_conjecture)
