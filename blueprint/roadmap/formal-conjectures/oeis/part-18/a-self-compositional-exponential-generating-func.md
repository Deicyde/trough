---
declaration: theorem
origin: cited
lean: OeisA368630.conjecture_mod_three, OeisA368630.conjecture_even, OeisA368630.conjecture_odd
statement: formalized
---

# A self-compositional exponential generating function

> The normalized exponential generating function of OEIS A368630 satisfies
> $A(x/A(x)^2)=\exp(xA(x))$, with $A(0)=1$.
>
> *References:*
> - [A368630](https://oeis.org/A368630), Paul D. Hanna, 2024.
> - [Li26] Wentao Li, [Congruences of the exponential generating sequence](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/e0e499973c3398f08ed91b39618f1948fe1804a5/proofs/new-proofs/A368630/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/368630.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/368630.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved. It also has 5 test statements and 2 API statements, counted here but not shown.

## `OeisA368630.conjecture_mod_three`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000013](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000013).

> For every $n \ge 0$, "a(n) == 1 (mod 3)".
> - Paul D. Hanna, Jan 02 2024.
>
> Proved by Wentao Li with OpenAI Codex assistance; see [Li26].

```lean
theorem conjecture_mod_three (n : ℕ) : a n % 3 = 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/368630.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/368630.lean#L89).

## `OeisA368630.conjecture_even`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000013](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000013).

> For every $n \ge 0$, "a(2*n) == 1 (mod 2)".
> - Paul D. Hanna, Jan 02 2024.
>
> Proved by Wentao Li with OpenAI Codex assistance; see [Li26].

```lean
theorem conjecture_even (n : ℕ) : a (2 * n) % 2 = 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/368630.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/368630.lean#L100).

## `OeisA368630.conjecture_odd`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000013](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000013).

> For every $n \ge 1$, "a(2*n+1) == 0 (mod 2)". The term $a(1)=1$ is excluded.
> - Paul D. Hanna, Jan 02 2024.
>
> Proved by Wentao Li with OpenAI Codex assistance; see [Li26].

```lean
theorem conjecture_odd (n : ℕ) (hn : 1 ≤ n) : a (2 * n + 1) % 2 = 0
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/368630.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/368630.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/368630.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/368630.lean)
- [A368630](https://oeis.org/A368630)
