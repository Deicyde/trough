---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry11.ramanujan_part1_ch3_entry11
statement: formalized
proof: formalized
---

# Power series and series transformations: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/index.html).

Identities and transformations of power series and exponential-type series: Lagrange inversion and the tree function, Abel- and Jensen-type exponential series, coefficients of exp of a power series and Newton's identities for summable sequences, transformations of factorial series and Taylor-shift transformations, and Touchard / generalized Bell series.

## Recurrence for the coefficients of $e^{f(x)}$

Let $(A_k)_{k \ge 1}$ and $(p_n)_{n \ge 0}$
be sequences of real numbers, let $R > 0$, and let $f : \mathbb{R} \to \mathbb{R}$. Suppose that
for every real $x$ with $|x| < R$ the series $\sum_{k \ge 1} A_k x^k / k$ is summable with sum
$f(x)$ and the series $\sum_{n \ge 0} p_n x^n$ is summable with sum $e^{f(x)}$. Then for every
integer $n \ge 1$,

$$n p_n = \sum_{k=1}^{n} A_k p_{n-k}.$$

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 11, printed p. 66 / PDF p. 76.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry11.ramanujan_part1_ch3_entry11`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry11.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry11.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/index.html#ramanujan-part1-ch3-entry11).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Power series and series transformations](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/power-series)
