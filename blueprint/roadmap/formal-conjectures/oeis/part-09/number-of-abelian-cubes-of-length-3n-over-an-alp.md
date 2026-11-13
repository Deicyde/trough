---
declaration: theorem
origin: cited
lean: OeisA141057.conjecture1, OeisA141057.conjecture2
statement: formalized
---

# Number of Abelian cubes of length $3n$ over an alphabet of size 3

> An Abelian cube is a string of the form $x x' x''$ with $|x| = |x'| = |x''|$ and $x$ is a
> permutation of $x'$ and $x''$. The number of Abelian cubes of length $3n$ over an alphabet of
> size 3 is given by
>
> $$a(n) = \sum_{k=0}^n \binom{n}{k}^3 \sum_{j=0}^k \binom{k}{j}^3.$$
>
> *References:*
> - [A141057](https://oeis.org/A141057)

*Quoted from [FormalConjectures/OEIS/141057.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/141057.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 7 test statements, counted here but not shown.

## `OeisA141057.conjecture1`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_a141057_supercongruence_conjecture/Submission/Spec.lean#L955](https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_a141057_supercongruence_conjecture/Submission/Spec.lean#L955).

> Conjecture: the supercongruences $a(n \cdot p^k) \equiv a(n \cdot p^{k-1}) \pmod{p^{3k}}$ hold
> for primes $p \ge 5$ and positive integers $n$ and $k$.

```lean
theorem conjecture1 (p k n : ℕ) (hp : p.Prime) (h_p_ge_5 : 5 ≤ p) (h_k_pos : 1 ≤ k)
    (h_n_pos : 1 ≤ n) :
    (a (n * p ^ k) : ℤ) ≡ a (n * p ^ (k - 1)) [ZMOD (p ^ (3 * k))]
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/141057.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/141057.lean#L65).

## `OeisA141057.conjecture2`

Solved: stated here; a Lean proof is at [https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/proofs/BalaA141057Conjecture.lean#L1416](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/proofs/BalaA141057Conjecture.lean#L1416).

> Conjecture (Peter Bala, 2022):
> The supercongruences $a(n \cdot p^k) \equiv a(n \cdot p^{k-1}) \pmod{p^{3k}}$ hold
> for the integer-indexed extension $a(n)$ for all $n \in \mathbb{Z} \setminus \{0\}$, primes $p \ge 5$,
> and $k \ge 1$.
>
> Proved in Lean by Jensen Kohlmeyer and Liam Kruer, extending the positive-index
> proof by Epoch Research.

```lean
theorem conjecture2 (p k : ℕ) (n : ℤ) (hp : p.Prime) (h_p_ge_5 : 5 ≤ p) (h_k_pos : 1 ≤ k)
    (hn : n ≠ 0) :
    aInt (n * (p ^ k : ℤ)) ≡ aInt (n * (p ^ (k - 1) : ℤ)) [ZMOD (p ^ (3 * k) : ℤ)]
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/141057.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/141057.lean#L102).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/141057.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/141057.lean)
- [A141057](https://oeis.org/A141057)
