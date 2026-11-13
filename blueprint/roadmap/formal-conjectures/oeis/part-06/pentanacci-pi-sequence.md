---
declaration: theorem
origin: cited
lean: OeisA100478.conjecture
statement: formalized
---

# Pentanacci $\pi$ sequence

> Start with $a(1)=a(2)=a(3)=a(4)=a(5)=1$ and
> for $n>5$, $a(n) = \pi(\sum_{j=1}^5 a(n-j))$ where $\pi = A000720$.
>
> *References:*
> - [A100478](https://oeis.org/A100478)

*Quoted from [FormalConjectures/OEIS/100478.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100478.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA100478.conjecture`

Solved: stated here without proof.

> Starting with other values of $a(1)$, $a(2)$, $a(3)$, $a(4)$, $a(5)$ what behaviors are possible?
> Does the sequence always stick at a single integer after some point, or can it go into a loop,
> or is there a third pattern?
>
> KitaKen1 showed the sequence either becomes constant or goes into a loop,
> see https://github.com/KitaKen1/oeis-a100478-eventual-periodicity/blob/642eed0ffee26415528ab8c48c5181826be04860/lean/OeisA100478FC.lean#L158-L168.
>
> tadamcz showed the sequence always becomes constant, see
> https://tadamcz.com/fc-review-results/aea251bb26/#/f/OEIS/100478.

```lean
theorem conjecture:
  ∀ v : Fin 5 → ℕ, (∀ i, 0 < v i) → ∃ c ∈ ({66, 67, 68, 70, 71, 72} : Finset ℕ),
  ∀ᶠ n in Filter.atTop, aGeneral v n = c
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/100478.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100478.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/100478.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100478.lean)
- [A100478](https://oeis.org/A100478)
