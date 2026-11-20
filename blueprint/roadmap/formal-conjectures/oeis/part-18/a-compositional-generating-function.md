---
declaration: theorem
origin: cited
lean: OeisA396843.conjecture
statement: formalized
---

# A compositional generating function

> The ordinary generating function satisfies $A(xA(x)-3xA(x)^2)=x^2$,
> with $A(0)=0$ and $a(1)=1$. Its coefficients form OEIS A396843.
>
> *References:*
> - [A396843](https://oeis.org/A396843), Paul D. Hanna, 2026.
> - ElonSG / the-omega-institute/trureturing, [Earlier Lean proof](https://github.com/the-omega-institute/trureturing/pull/6773).
> - [Li26] Wentao Li, [Integral construction and oddness](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/1cc54d7f3ecfdcea49625ce31c8df3e22d4c6146/proofs/independent-formalization/A396843/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/396843.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/396843.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements and 2 API statements, counted here but not shown.

## `OeisA396843.conjecture`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000016](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000016).

> "Conjecture: all terms are odd."
> - Paul D. Hanna, Jul 01 2026.
>
> An earlier Lean parity proof appears in `the-omega-institute/trureturing` PR #6773.
> Wentao Li's formalization also proves integral existence and uniqueness; see [Li26].
> AI assistance was used for development and verification.

```lean
theorem conjecture (n : ℕ) (hn : 1 ≤ n) : Odd (a n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/396843.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/396843.lean#L92).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/396843.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/396843.lean)
- [A396843](https://oeis.org/A396843)
