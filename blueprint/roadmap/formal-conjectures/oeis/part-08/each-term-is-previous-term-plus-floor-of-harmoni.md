---
declaration: theorem
origin: cited
lean: OeisA114831.conjecture3
statement: formalized
---

# Each term is previous term plus floor of harmonic mean of two previous terms.

> $a(1) = 1, a(2) = 2$ and
> $a(n) = a(n-1) + \lfloor \frac{2 a(n-1) a(n-2)}{a(n-1) + a(n-2)} \rfloor$ for $n \ge 3$.
>
> *References:*
> - [A114831](https://oeis.org/A114831)

*Quoted from [FormalConjectures/OEIS/114831.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/114831.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 4 test statements, counted here but not shown.

## `OeisA114831.conjecture3`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a114831-asymptotic/blob/54cdeeed2ef5838e3aa61a3a228e6867802d20df/lean/OeisA114831FC.lean#L252-L285](https://github.com/KitaKen1/oeis-a114831-asymptotic/blob/54cdeeed2ef5838e3aa61a3a228e6867802d20df/lean/OeisA114831FC.lean#L252-L285).

> Conjecture based on OEIS A114831: What is this sequence, asymptotically?
> If the limit exists, the ratio of consecutive terms must tend to $\sqrt{3}$:
>
> $$ \lim_{n \to \infty} \frac{a(n+1)}{a(n)} = \sqrt{3}. $$
>
> That's because $a(n)$ is positive, monotonically increasing ($a(n) > a(n-1)$)
> and $a(n+2) \geq a(n+1) + a(n)$.
> So $a(n)$ grows exponentially, at least as fast as the Fibonnaci numbers.
> Assuming $\frac{a(n+1)}{a(n)}$ tend to a limit L, solving for L in the definition of $a(n)$
> gives $L=\sqrt{3}$.

```lean
theorem conjecture3 :
    Tendsto (fun n ↦ (a (n + 1) : ℝ) / (a n : ℝ)) atTop (nhds (Real.sqrt 3))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/114831.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/114831.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/114831.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/114831.lean)
- [A114831](https://oeis.org/A114831)
