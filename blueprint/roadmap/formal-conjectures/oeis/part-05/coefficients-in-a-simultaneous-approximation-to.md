---
declaration: theorem
origin: cited
lean: OeisA98275.conjecture_1
statement: formalized
---

# Coefficients in a simultaneous approximation to two polylogarithms

> Coefficients in a simultaneous approximation to $\operatorname{Li}_2(-1)$ and
> $\operatorname{Li}_3(-1)$, given by
> $a(n)=\sum_{i,j=0}^{n}\binom{n}{i}^2\binom{n}{j}^2\binom{n+i}{n}\binom{i+j}{i}$.
>
> *References:*
> - [A098275](https://oeis.org/A098275)
> - [Li26] Wentao Li, [A proof of the OEIS A098275 conjecture](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/proofs/new-proofs/A098275/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/98275.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/98275.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA98275.conjecture_1`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewProofs/A098275.lean#L166](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewProofs/A098275.lean#L166).

> Conjecture 1:
> "Conjecture: $a(n)$ is divisible by $n+1$."
> - F. Chapoton, Jan 28 2026.
>
> Proved and formalized in Lean by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture_1 (n : ℕ) : n + 1 ∣ a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/98275.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/98275.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/98275.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/98275.lean)
- [A098275](https://oeis.org/A098275)
