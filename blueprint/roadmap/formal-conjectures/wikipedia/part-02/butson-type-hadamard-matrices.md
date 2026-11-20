---
declaration: theorem
origin: cited
lean: ButsonHadamardMatrix.butson_prime_divisibility, ButsonHadamardMatrix.not_forall_odd_prime_mul_exists, ButsonHadamardMatrix.butson_hadamard_fourth_roots_conjecture
statement: formalized
---

# Butson-type Hadamard matrices

> A *Butson-type Hadamard matrix* $H(k, n)$ (also written $\operatorname{BH}(n, k)$) is an
> $n \times n$ complex matrix $M$ whose entries are $k$-th roots of unity ($k > 0$, $M_{ij}^k = 1$)
> and whose rows are mutually orthogonal in $\mathbb{C}^n$, so that $M M^* = n I_n$. At $k = 2$,
> $H(2, n)$ recovers real Hadamard matrices; at $k = 4$, $H(4, n)$ consists of matrices with entries
> in $\{\pm 1, \pm i\}$.
>
> While the Wikipedia article states as a conjecture that $H(p, m p)$ exists for every odd prime
> $p \ge 3$ and integer $m \ge 1$, this fails already at $H(3, 15)$ [dL84, Wi00]. For fourth roots of
> unity ($k = 4$), the complex Hadamard conjecture [Tu70, dLF11] asks whether $H(4, 2m)$ exists for
> every $m \ge 1$.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Butson-type_Hadamard_matrix)
> - [Bu62] Butson, A. T. (1962). *Generalized Hadamard matrices*, Proc. Amer. Math. Soc. 13,
>   894--898.
> - [Tu70] Turyn, R. J. (1970). *Complex Hadamard matrices*, in Combinatorial Structures and their
>   Applications (Calgary, 1969), Gordon and Breach, New York, 435--437.
> - [dL84] de Launey, W. (1984). *On the non-existence of generalised Hadamard matrices*, J. Statist.
>   Plann. Inference 10 (3), 385--396.
> - [Wi00] Winterhof, A. (2000). *On the non-existence of generalized Hadamard matrices*, J. Statist.
>   Plann. Inference 84, 337--342.
> - [dLF11] de Launey, W. and Flannery, D. L. (2011). *Algebraic Design Theory*, Mathematical Surveys
>   and Monographs 175, Amer. Math. Soc.

*Quoted from [FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 3 test statements and 1 API statement, counted here but not shown.

## `ButsonHadamardMatrix.butson_prime_divisibility`

Solved: stated here without proof.

> **Butson's prime divisibility theorem** [Bu62]: if $p$ is prime, $n \ge 2$, and a Butson-type
> Hadamard matrix $H(p, n)$ exists, then $p \mid n$.
>
> The hypothesis $n \ge 2$ excludes the trivial $1 \times 1$ matrix $[1]$, which satisfies
> $H(p, 1)$ for every $p \ge 1$.

```lean
theorem butson_prime_divisibility {p n : ℕ} (hp : p.Prime) (hn : 2 ≤ n)
    (hex : ∃ M, IsButsonHadamard (n := n) p M) :
    p ∣ n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean#L104).

## `ButsonHadamardMatrix.not_forall_odd_prime_mul_exists`

Solved: stated here without proof.

> **Disproof of the odd-prime-multiple existence claim** [dL84, Wi00]: contrary to the conjecture
> stated on [Wikipedia](https://en.wikipedia.org/wiki/Butson-type_Hadamard_matrix#Existence), it is
> not true that a Butson-type Hadamard matrix $H(p, m p)$ exists for every odd prime $p \ge 3$ and
> every positive integer $m \ge 1$ (for instance, no $H(3, 15)$ matrix exists).

```lean
theorem not_forall_odd_prime_mul_exists :
    ¬ ∀ (p m : ℕ), p.Prime → 3 ≤ p → 1 ≤ m →
      ∃ M, IsButsonHadamard (n := m * p) p M
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean#L116).

## `ButsonHadamardMatrix.butson_hadamard_fourth_roots_conjecture`

Open: stated without proof.

> **Complex Hadamard conjecture for fourth roots of unity** [Tu70, dLF11]: for every integer
> $m \ge 1$, there exists a $2m \times 2m$ Butson-type Hadamard matrix $H(4, 2m)$ with entries in
> $\{1, -1, i, -i\}$.
>
> This quaternary conjecture comes from [Tu70, dLF11] (rather than the Wikipedia page above). By
> Turyn's doubling construction [Tu70], an $H(4, 2m)$ matrix yields a real Hadamard matrix
> $H(2, 4m)$, so this conjecture implies Hadamard's conjecture.

```lean
theorem butson_hadamard_fourth_roots_conjecture (m : ℕ) (hm : 1 ≤ m) :
    ∃ M, IsButsonHadamard (n := 2 * m) 4 M
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean#L131).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Wikipedia/ButsonHadamardMatrix.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Butson-type_Hadamard_matrix)
