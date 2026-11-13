---
declaration: theorem
origin: cited
lean: OeisA368634.conjecture
statement: formalized
---

# A generating function with signed square terms

> The sequence consists of the coefficients of
> $A(x)=1+x(3A(x)^2-A(-x)^2)/2$.
>
> *References:*
> - [A368634](https://oeis.org/A368634)
> - [Li26] Wentao Li, [Generating-function bridge and parity for A368634](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/9d4a205da2a4094800f9c600a7b0b5223eda51ce/proofs/new-proofs/A368634/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/368634.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/368634.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements and 1 API statement, counted here but not shown.

## `OeisA368634.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/9d4a205da2a4094800f9c600a7b0b5223eda51ce/LeanOeisProofs/NewProofs/A368634.lean#L407](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/9d4a205da2a4094800f9c600a7b0b5223eda51ce/LeanOeisProofs/NewProofs/A368634.lean#L407).

> "Conjecture: $a(n)$ is odd when $n = 2^k - 1$ for $k \ge 0$ and even elsewhere."
> - Paul D. Hanna, Jan 12 2024.
>
> Lean proof by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture (n : ℕ) : Odd (a n) ↔ ∃ k : ℕ, n = 2 ^ k - 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/368634.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/368634.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/368634.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/368634.lean)
- [A368634](https://oeis.org/A368634)
