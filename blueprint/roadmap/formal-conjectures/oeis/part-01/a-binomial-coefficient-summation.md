---
declaration: theorem
origin: cited
lean: OeisA3162.a_is_integer, OeisA3162.conjecture
statement: formalized
---

# A binomial coefficient summation

> A binomial coefficient summation: $a(n) = S(3, n) / S(1, n)$, where for a positive integer $r$
> we define
>
> $$S(r,n) = \sum_{k=0}^{\lfloor n/2 \rfloor} \left( \binom{n}{k} - \binom{n}{k-1} \right)^r$$
>
> with $\binom{n}{-1} = 0$.
>
> *References:*
> - [A003162](https://oeis.org/A003162)
> - H. W. Gould, Problem E2384 (proposal), Amer. Math. Monthly, 81 (1974), 170-171
> - [Li26] Wentao Li, [A supercongruence for A003162](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/41f7b2ba762827a74f1651e76a2ad6d77be6a021/proofs/new-formalization/A003162/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/3162.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/3162.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 solved and 1 textbook result. It also has 5 test statements, counted here but not shown.

## `OeisA3162.a_is_integer`

Textbook result, stated without proof. A Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/41f7b2ba762827a74f1651e76a2ad6d77be6a021/LeanOeisProofs/NewFormalization/A003162.lean#L72](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/41f7b2ba762827a74f1651e76a2ad6d77be6a021/LeanOeisProofs/NewFormalization/A003162.lean#L72).

> $a(n)$ is an integer for all $n \ge 0$.
>
> Gould proposed this as Monthly Problem E2384. The 1974 reference in the module docstring
> is that proposal, not a solution to it.
>
> Lean formalization by Wentao Li, with AI assistance; see [Li26].

```lean
theorem a_is_integer (n : ℕ) : (a n).den = 1
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/3162.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/3162.lean#L84).

## `OeisA3162.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/41f7b2ba762827a74f1651e76a2ad6d77be6a021/LeanOeisProofs/NewFormalization/A003162.lean#L115](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/41f7b2ba762827a74f1651e76a2ad6d77be6a021/LeanOeisProofs/NewFormalization/A003162.lean#L115).

> "Conjecture: Let $b(n) = a(2n-1)$. Then the supercongruence
> $b(np^k) \equiv b(np^{k-1}) \pmod{p^{3k}}$ holds for positive integers $n$ and $k$
> and all primes $p \ge 5$."
> - Peter Bala, Mar 26 2023.
>
> Lean formalization by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture (n k p : ℕ) (hn : 0 < n) (hk : 0 < k) (hp : p.Prime) (hp_ge : 5 ≤ p) :
    (b (n * p ^ k)).num ≡ (b (n * p ^ (k - 1))).num [ZMOD (p : ℤ) ^ (3 * k)]
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/3162.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/3162.lean#L98).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/3162.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/3162.lean)
- [A003162](https://oeis.org/A003162)
