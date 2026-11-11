---
declaration: section
origin: cited
lean: MetaMathlibExt.weyl_criterion
statement: formalized
proof: formalized
---

# Uniform distribution and metric approximation: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/index.html).

Weyl equidistribution, three-gap theorem, Duffin–Schaeffer, normal numbers, Beatty sequences, discrepancy, lattice points and Minkowski-type theorems.

## Weyl's equidistribution criterion

Let $(x_n)_{n \ge 0}$ be a sequence of real numbers and
write $\operatorname{frac}(t) = t - \lfloor t \rfloor$ for the fractional part of a real number
$t$. Then the following are equivalent:
(i) for all real numbers $a < b$ with $0 \le a$ and $b \le 1$,
$\frac{1}{N} \#\{n < N : a \le \operatorname{frac}(x_n) < b\} \to b - a$ as $N \to \infty$;
(ii) for every nonzero integer $h$,
$\frac{1}{N} \sum_{n=0}^{N-1} e^{2\pi i h x_n} \to 0$ as $N \to \infty$.

## Sources

- https://en.wikipedia.org/wiki/Equidistribution_theorem.

Formalized by `MetaMathlibExt.weyl_criterion`, a theorem declared in [MathlibExt/NumberTheory/DiophantineApproximation/WeylCriterion.lean, line 1211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DiophantineApproximation/WeylCriterion.lean#L1211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/index.html#weyl-criterion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Uniform distribution and metric approximation](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric)
