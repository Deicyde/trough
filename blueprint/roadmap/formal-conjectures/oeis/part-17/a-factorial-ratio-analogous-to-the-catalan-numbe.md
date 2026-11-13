---
declaration: theorem
origin: cited
lean: OeisA361033.conjecture_1
statement: formalized
---

# A factorial ratio analogous to the Catalan numbers

> The sequence is defined by $a(n)=3(4n)!/(n!((n+1)!)^3)$ for $n \ge 0$.
>
> *References:*
> - [A361033](https://oeis.org/A361033)
> - [Li26] Wentao Li, [Integrality and parity of a factorial ratio](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/proofs/new-formalization/A361033/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/361033.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/361033.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA361033.conjecture_1`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewFormalization/A361033.lean#L380](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewFormalization/A361033.lean#L380).

> The parity conjecture:
> "Conjecture: $a(n)$ is odd iff $n = 2^k - 1$ for some $k \ge 0$."
> - Peter Bala, Mar 01 2023.
>
> Proved and formalized in Lean by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture_1 (n : ℕ) : Odd (a n) ↔ ∃ k : ℕ, n = 2 ^ k - 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/361033.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/361033.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/361033.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/361033.lean)
- [A361033](https://oeis.org/A361033)
