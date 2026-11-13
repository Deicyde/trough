---
declaration: theorem
origin: cited
lean: OeisA112521.conjecture
statement: formalized
---

# Sequence related to NOR bracketings

> $$a(n) = \sum_{j=0}^{n-1} (-1)^j \binom{2j}{j} \binom{2n-j-2}{n-j-1}$$
>
> *References:*
> - [A112521](https://oeis.org/A112521)

*Quoted from [FormalConjectures/OEIS/112521.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/112521.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements, counted here but not shown.

## `OeisA112521.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a112521-formal-conjectures/blob/d4ee80e997c20209a1f18b7b9aa3521150d5474d/lean/OeisA112521Proof.lean#L876-L885](https://github.com/KitaKen1/oeis-a112521-formal-conjectures/blob/d4ee80e997c20209a1f18b7b9aa3521150d5474d/lean/OeisA112521Proof.lean#L876-L885).

> Conjecture: Starting with $n=1$, $a(n)$ is the main diagonal of the array $T(n, k)$.

```lean
theorem conjecture : ∀ (n : ℕ), n ≥ 1 → (a n : ℤ) = T n n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/112521.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/112521.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/112521.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/112521.lean)
- [A112521](https://oeis.org/A112521)
