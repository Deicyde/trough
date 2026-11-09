---
declaration: theorem
origin: cited
lean: Erdos406.erdos_406, Erdos406.erdos_406.variants.one_two
statement: formalized
---

# Erdős Problem 406

> *Reference:* [erdosproblems.com/406](https://www.erdosproblems.com/406)

*Quoted from [FormalConjectures/ErdosProblems/406.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/406.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/406](https://www.erdosproblems.com/406).

The file states 2 research or textbook statements: 2 open.

## `Erdos406.erdos_406`

Open: stated without proof.

> Is it true that there are only finitely many powers of $2$ which have only the digits $0$
> and $1$ when written in base $3$?

```lean
theorem erdos_406 : { n | n.isPowerOfTwo ∧ Nat.digits 3 n ⊆ [0, 1] }.Finite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/406.lean, line 35](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/406.lean#L35).

## `Erdos406.erdos_406.variants.one_two`

Open: stated without proof.

> If we only allow the digits $1$ and $2$ then $2^{15}$ seems to be the largest such power
> of $2$.

```lean
theorem erdos_406.variants.one_two :
    IsGreatest { n | n.isPowerOfTwo ∧ Nat.digits 3 n ⊆ [1, 2] } (2 ^ 15)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/406.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/406.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/406.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/406.lean)
- [erdosproblems.com/406](https://www.erdosproblems.com/406)
