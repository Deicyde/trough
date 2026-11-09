---
declaration: theorem
origin: cited
lean: OeisA368635.conjecture
statement: formalized
---

# The generating function $A(x)=1+3xA(x)^2-2xA(-x)^2$

> The sequence consists of the coefficients of
> $A(x)=1+3xA(x)^2-2xA(-x)^2$.
>
> *References:*
> - [A368635](https://oeis.org/A368635)
> - [Li26] Wentao Li, [Generating-function bridge and parity for A368635](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/9d4a205da2a4094800f9c600a7b0b5223eda51ce/proofs/new-formalization/A368635/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/368635.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/368635.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements and 1 API statement, counted here but not shown.

## `OeisA368635.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/9d4a205da2a4094800f9c600a7b0b5223eda51ce/LeanOeisProofs/NewFormalization/A368635.lean#L433](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/9d4a205da2a4094800f9c600a7b0b5223eda51ce/LeanOeisProofs/NewFormalization/A368635.lean#L433).

> "Conjecture: $a(n)$ is odd when $n = 2^k - 1$ for $k \ge 0$, and even elsewhere."
> - Paul D. Hanna, Jan 12 2024.
>
> Lean proof by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture (n : ℕ) : Odd (a n) ↔ ∃ k : ℕ, n = 2 ^ k - 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/368635.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/368635.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/368635.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/368635.lean)
- [A368635](https://oeis.org/A368635)
