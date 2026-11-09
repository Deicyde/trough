---
declaration: theorem
origin: cited
lean: OeisA220119.conjecture_1
statement: formalized
---

# A double sum of five binomial factors

> The sequence is defined by
> $a(n)=\sum_{j,k=0}^{n}\binom{n}{j}^2\binom{n}{k}^2\binom{n+j}{n}\binom{n+k}{n}\binom{j+k}{n}$.
>
> *References:*
> - [A220119](https://oeis.org/A220119)
> - [Li26] Wentao Li, [A proof of the OEIS A220119 conjecture](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/proofs/new-proofs/A220119/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/220119.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/220119.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA220119.conjecture_1`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewProofs/A220119.lean#L1702](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewProofs/A220119.lean#L1702).

> Conjecture 1:
> "Conjecture: For $n > 0$, $a(n)$ is always divisible by $(n+1) * (n+2)$."
> - F. Chapoton, Apr 23 2026.
>
> The restriction $n > 0$ is necessary since $a(0) = 1$.
> Proved and formalized in Lean by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture_1 (n : ℕ) (hn : 0 < n) : (n + 1) * (n + 2) ∣ a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/220119.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/220119.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/220119.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/220119.lean)
- [A220119](https://oeis.org/A220119)
