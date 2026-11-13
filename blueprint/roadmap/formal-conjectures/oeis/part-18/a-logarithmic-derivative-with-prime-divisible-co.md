---
declaration: theorem
origin: cited
lean: OeisA381355.conjecture
statement: formalized
---

# A logarithmic derivative with prime-divisible coefficients

> Let $F(x)$ be the generating function of A381353, with $F(0)=1$, $[x]F(x)=1$, and
> $[x^n]F(x)^{p_n}=0$ for $n>1$, where $p_n$ is the $n$-th prime.
> The sequence is defined by $\sum_{n\ge1}a(n)x^n=xF'(x)/F(x)$.
>
> *References:*
> - [A381355](https://oeis.org/A381355)
> - [A381353](https://oeis.org/A381353)
> - [Li26] Wentao Li, [Prime divisibility of logarithmic-derivative coefficients](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/proofs/new-proofs/A381355/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/381355.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/381355.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA381355.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewProofs/A381355.lean#L380](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewProofs/A381355.lean#L380).

> "Conjecture: $a(n)$ is divisible by $\operatorname{prime}(n)$ for $n > 1$."
> - Paul D. Hanna, Mar 11 2025.
>
> Proved and formalized in Lean by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture (n : ℕ) (hn : 1 < n) : (primeN n : ℤ) ∣ a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/381355.lean, line 235](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/381355.lean#L235).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/381355.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/381355.lean)
- [A381355](https://oeis.org/A381355)
