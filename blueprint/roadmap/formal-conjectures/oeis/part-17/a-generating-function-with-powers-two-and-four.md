---
declaration: theorem
origin: cited
lean: OeisA368628.conjecture
statement: formalized
---

# A generating function with powers two and four

> The sequence consists of the coefficients of
> $A(x)=1+x(A(x)^2-A(-x)^2)/2+x(A(x)^4+A(-x)^4)/2$.
>
> *References:*
> - [A368628](https://oeis.org/A368628)
> - [Li26] Wentao Li, [Generating-function bridge and parity for A368628](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/b5eabe63ce276d12170d18f91b5b7327130c4cbe/proofs/new-formalization/A368628/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/368628.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/368628.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements and 1 API statement, counted here but not shown.

## `OeisA368628.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/b5eabe63ce276d12170d18f91b5b7327130c4cbe/LeanOeisProofs/NewFormalization/A368628.lean#L523](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/b5eabe63ce276d12170d18f91b5b7327130c4cbe/LeanOeisProofs/NewFormalization/A368628.lean#L523).

> "Conjecture: $a(n)$ is odd when $n = (4^k - 1)/3$ for $k \ge 0$, and even elsewhere."
> - Paul D. Hanna, Jan 10 2024.
>
> Lean formalization by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture (n : ℕ) : Odd (a n) ↔ ∃ k : ℕ, n = (4 ^ k - 1) / 3
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/368628.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/368628.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/368628.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/368628.lean)
- [A368628](https://oeis.org/A368628)
