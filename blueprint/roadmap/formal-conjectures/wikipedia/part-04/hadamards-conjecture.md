---
declaration: theorem
origin: cited
lean: Hadamard.HadamardConjecture, Hadamard.HadamardConjecture.variants.first_cases, Hadamard.HadamardConjecture.variants.«167»
statement: formalized
---

# Hadamard's conjecture

> *References:*
>  - [Wikipedia](https://en.wikipedia.org/wiki/Hadamard_matrix#Hadamard_conjecture)
>  - [Tao's optimization constant 23a](https://teorth.github.io/optimizationproblems/constants/23a.html)
>  - [Résolution d'une question relative aux déterminants](https://gallica.bnf.fr/ark:/12148/bpt6k486252g/f400.image.r) by *Jacques Hadamard*,  Bull. des sciences math., p.245, 1893

*Quoted from [FormalConjectures/Wikipedia/Hadamard.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Hadamard.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 3 test statements, counted here but not shown.

## `Hadamard.HadamardConjecture`

Open: stated without proof.

> There exists a Hadamard matrix for all $n = 4k$.

```lean
theorem HadamardConjecture (k : ℕ) : ∃ M, IsHadamard (n := 4 * k) M
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Wikipedia/Hadamard.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Hadamard.lean#L91).

## `Hadamard.HadamardConjecture.variants.first_cases`

Solved: stated here without proof.

> For all $k ≤ 166$, it is known there that there is a Hadamard matrix of size $4 * k$.
> So `hadamardConstant` is at least $668$.

```lean
theorem HadamardConjecture.variants.first_cases : 668 ≤ hadamardConstant
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Wikipedia/Hadamard.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Hadamard.lean#L142).

## `Hadamard.HadamardConjecture.variants.«167»`

Open: stated without proof.

> The smallest order for which no Hadamard matrix is presently known is $668 = 4 * 167$.
> Is `hadamardConstant` larger than $668$?

```lean
theorem HadamardConjecture.variants.«167» : 668 < hadamardConstant
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Wikipedia/Hadamard.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Hadamard.lean#L150).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Hadamard.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Hadamard.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Hadamard_matrix#Hadamard_conjecture)
