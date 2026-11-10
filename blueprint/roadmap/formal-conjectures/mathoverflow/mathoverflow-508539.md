---
declaration: theorem
origin: cited
lean: Mathoverflow508539.mathoverflow_508539
statement: formalized
---

# MathOverflow 508539

> Edge-vertex inequality $EV \geq 4^{n-1}$.
>
> *References:*
> - [MathOverflow 508539](https://mathoverflow.net/questions/508539), asked by
>   [Paata Ivanisvili](https://mathoverflow.net/users/50901/paata-ivanisvili).
> - [DIRX26] Durcik, P., Ivanisvili, P., Roos, J., and Xie, X.,
>   *Sharp isoperimetric inequalities on the Hamming cube II: The critical exponent* (2026),
>   [arXiv:2602.20462](https://arxiv.org/abs/2602.20462), inequality (1.2).

*Quoted from [FormalConjectures/Mathoverflow/508539.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/508539.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 2 test statements, counted here but not shown.

## `Mathoverflow508539.mathoverflow_508539`

Solved: stated here without proof.

> For any set $A \subset \{0,1\}^n$ of half size $2^{n-1}$, we have $EV \geq 4^{n-1}$,
> where $E$ denotes the edge boundary (the number of edges between $A$ and its complement), and
> $V$ denotes the inner vertex boundary (the number of points in $A$ having a neighbor outside $A$).
>
> This is the half-size case of [DIRX26, (1.2)]. The hypothesis $n > 0$ is necessary: in dimension
> zero the cardinality hypothesis allows the whole cube, whose boundaries are empty.

```lean
theorem mathoverflow_508539 {n : ℕ} (A : Finset (Fin n → Bool))
    (hA : #A = 2 ^ (n - 1)) (hn : 0 < n) :
    4 ^ (n - 1) ≤ #((hypercube n).edgeBoundary A) *
      #((hypercube n).innerVertexBoundary A)
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Mathoverflow/508539.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/508539.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/508539.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/508539.lean)
- [MathOverflow 508539](https://mathoverflow.net/questions/508539)
