---
declaration: theorem
origin: cited
lean: OeisA375439.conjecture
statement: formalized
---

# A cubic generating function with ternary substitution

> The coefficients of the generating function
> $A(x)=x+x^2+(2A(x)^3+A(x^3))/3$, with constant term $a(0)=0$.
>
> *References:*
> - [A375439](https://oeis.org/A375439)
> - [A038754](https://oeis.org/A038754)
> - [Li26] Wentao Li, [Parity of A375439](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/proofs/new-proofs/A375439/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/375439.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/375439.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 7 test statements and 1 API statement, counted here but not shown.

## `OeisA375439.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewProofs/A375439.lean#L382](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewProofs/A375439.lean#L382).

> "Conjecture: $a(n)$ is odd iff $n$ is in A038754, which consists of numbers of the form
> $3^k$ and $2*3^k$."
> - Paul D. Hanna, Aug 21 2024.
>
> Lean proof by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture (n : ℕ) (hn : 1 ≤ n) :
    Odd (a n) ↔ ∃ k : ℕ, n = 3 ^ k ∨ n = 2 * 3 ^ k
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/375439.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/375439.lean#L115).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/375439.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/375439.lean)
- [A375439](https://oeis.org/A375439)
