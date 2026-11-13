---
declaration: theorem
origin: cited
lean: ButsonHadamardMatrix.butson_prime_divisibility, ButsonHadamardMatrix.butson_hadamard_fourth_roots_conjecture
statement: formalized
---

# Butson-type Hadamard matrices

> A *Butson-type Hadamard matrix* $H(k, n)$ (also written $\operatorname{BH}(n, k)$) is an
> $n \times n$ complex matrix $M$ whose entries are $k$-th roots of unity ($M_{ij}^k = 1$) and whose
> rows are mutually orthogonal in $\mathbb{C}^n$, so that $M M^* = n I_n$. At $k = 2$, $H(2, n)$
> recovers real Hadamard matrices; at $k = 4$, $H(4, n)$ consists of matrices with entries in
> $\{\pm 1, \pm i\}$.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Butson-type_Hadamard_matrix)
> - [Bu62] Butson, A. T. (1962). *Generalized Hadamard matrices*, Proc. Amer. Math. Soc. 13,
>   894--898.
> - [Tu70] Turyn, R. J. (1970). *Complex Hadamard matrices*, in Combinatorial Structures and their
>   Applications (Calgary, 1969), Gordon and Breach, New York, 435--437.
> - [Wi00] Winterhof, A. (2000). *On the non-existence of generalized Hadamard matrices*, J. Statist.
>   Plann. Inference 84, 337--342.
> - [dLF11] de Launey, W. and Flannery, D. L. (2011). *Algebraic Design Theory*, Mathematical Surveys
>   and Monographs 175, Amer. Math. Soc.

*Quoted from [FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 2 test statements and 1 API statement, counted here but not shown.

## `ButsonHadamardMatrix.butson_prime_divisibility`

Solved: stated here without proof.

> **Butson's prime divisibility theorem** [Bu62]: if $p$ is prime, $n \ge 2$, and a Butson-type
> Hadamard matrix $H(p, n)$ exists, then $p \mid n$.
>
> The hypothesis $n \ge 2$ excludes the trivial $1 \times 1$ matrix $[1]$, which satisfies
> $H(p, 1)$ for every $p$.

```lean
theorem butson_prime_divisibility {p n : ℕ} (hp : p.Prime) (hn : 2 ≤ n)
    (hex : ∃ M, IsButsonHadamard p n M) :
    p ∣ n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean#L91).

## `ButsonHadamardMatrix.butson_hadamard_fourth_roots_conjecture`

Open: stated without proof.

> **Complex Hadamard conjecture for fourth roots of unity** [Tu70, dLF11]: for every integer
> $m \ge 1$, there exists a $2m \times 2m$ Butson-type Hadamard matrix $H(4, 2m)$ with entries in
> $\{1, -1, i, -i\}$.
>
> By Turyn's doubling construction [Tu70], an $H(4, 2m)$ matrix yields a real Hadamard matrix
> $H(2, 4m)$, so this conjecture implies Hadamard's conjecture.

```lean
theorem butson_hadamard_fourth_roots_conjecture (m : ℕ) (hm : 1 ≤ m) :
    ∃ M, IsButsonHadamard 4 (2 * m) M
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Butson-type_Hadamard_matrix)
