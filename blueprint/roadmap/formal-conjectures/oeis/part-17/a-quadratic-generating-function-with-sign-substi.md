---
declaration: theorem
origin: cited
lean: OeisA368633.conjecture_1
statement: formalized
---

# A quadratic generating function with sign substitution

> The sequence consists of the coefficients of $A(x)=1+2xA(x)^2-xA(-x)^2$.
>
> *References:*
> - [A368633](https://oeis.org/A368633)
> - [Li26] Wentao Li, [Catalan parity for A368633](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/proofs/new-formalization/A368633/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/368633.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/368633.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements and 1 API statement, counted here but not shown.

## `OeisA368633.conjecture_1`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewFormalization/A368633.lean#L166](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewFormalization/A368633.lean#L166).

> The parity conjecture (Conjecture 1):
> "Conjecture: $a(n)$ is odd when $n = 2^k - 1$ for $k \ge 0$ and even elsewhere."
> - Paul D. Hanna, Jan 11 2024.
>
> Lean formalization by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture_1 (n : ℕ) : Odd (a n) ↔ ∃ k : ℕ, n + 1 = 2 ^ k
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/368633.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/368633.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/368633.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/368633.lean)
- [A368633](https://oeis.org/A368633)
