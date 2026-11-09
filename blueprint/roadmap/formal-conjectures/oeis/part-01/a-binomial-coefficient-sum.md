---
declaration: theorem
origin: cited
lean: OeisA3161.conjecture
statement: formalized
---

# A binomial coefficient sum

> A binomial coefficient sum:
> $$a(n) = \sum_{k=0}^{\lfloor n/2 \rfloor} \left( \binom{n}{k} - \binom{n}{k-1} \right)^3$$
> where $\binom{n}{-1} = 0$.
>
> *References:*
> - [A003161](https://oeis.org/A003161)
> - [Li26] Wentao Li, [A supercongruence for A003161](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/41f7b2ba762827a74f1651e76a2ad6d77be6a021/proofs/new-formalization/A003161/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/3161.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/3161.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA3161.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/41f7b2ba762827a74f1651e76a2ad6d77be6a021/LeanOeisProofs/NewFormalization/A003161.lean#L1717](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/41f7b2ba762827a74f1651e76a2ad6d77be6a021/LeanOeisProofs/NewFormalization/A003161.lean#L1717).

> "Conjecture: Let $b(n) = a(2n-1)$. Then the supercongruence
> $b(np^k) \equiv b(np^{k-1}) \pmod{p^{3k}}$ holds for positive integers $n$ and $k$
> and all primes $p \ge 5$."
> - Peter Bala, Mar 20 2023.
>
> Lean formalization by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture (n k p : ℕ) (hn : 0 < n) (hk : 0 < k) (hp : p.Prime) (hp_ge : 5 ≤ p) :
    (b (n * p ^ k) : ℤ) ≡ (b (n * p ^ (k - 1)) : ℤ) [ZMOD (p : ℤ) ^ (3 * k)]
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/3161.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/3161.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/3161.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/3161.lean)
- [A003161](https://oeis.org/A003161)
