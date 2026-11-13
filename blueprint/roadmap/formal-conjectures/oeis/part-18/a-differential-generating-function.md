---
declaration: theorem
origin: cited
lean: OeisA397588.conjecture_parity, OeisA397588.three_dvd_a
statement: formalized
---

# A differential generating function

> The generating function satisfies $A(x)=x+(xA(x)^2)'$. Its constant term is zero.
> Seiichi Manyama's recurrence is $a(1)=1$ and
> $a(n)=(n+1)\sum_{k=1}^{n-1}a(k)a(n-k)$ for $n>1$.
>
> *References:*
> - [A397588](https://oeis.org/A397588)
> - [Li26] Wentao Li, [Parity and divisibility for A397588](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/proofs/new-formalization/A397588/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/397588.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/397588.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 6 test statements and 2 API statements, counted here but not shown.

## `OeisA397588.conjecture_parity`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewFormalization/A397588.lean#L211](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewFormalization/A397588.lean#L211).

> "Conjecture: $a(n)$ is odd iff $n$ is a power of $2$ for $n \ge 1$."
> - Paul D. Hanna, Jul 03 2026.
>
> Lean formalization by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture_parity (n : ℕ) (hn : 1 ≤ n) :
    Odd (a n) ↔ ∃ k : ℕ, n = 2 ^ k
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/397588.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/397588.lean#L107).

## `OeisA397588.three_dvd_a`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewFormalization/A397588.lean#L325](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewFormalization/A397588.lean#L325).

> "$a(n)$ divisible by $3$ for $n > 1$."
> - Paul D. Hanna, Jul 03 2026.
>
> Lean formalization by Wentao Li, with AI assistance; see [Li26].

```lean
theorem three_dvd_a (n : ℕ) (hn : 1 < n) : 3 ∣ a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/397588.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/397588.lean#L120).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/397588.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/397588.lean)
- [A397588](https://oeis.org/A397588)
