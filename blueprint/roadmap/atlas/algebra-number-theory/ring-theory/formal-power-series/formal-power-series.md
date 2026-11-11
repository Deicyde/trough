---
declaration: section
origin: cited
lean: PowerSeries.taylorFormula
statement: formalized
proof: formalized
---

# Formal power series: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/index.html).

Rings of formal power series in one or several variables and Hahn series, with formal exponentials, derivatives, coefficient operators and Lagrange inversion.

## Taylor's formula for formal power series

Let $R$ be a commutative $\mathbb{Q}$-algebra
and $f$ a formal power series over $R$, with $j$-th formal derivative $f^{(j)}$, and write
$[X^i]h$ for the coefficient of $X^i$ in a power series $h$. In the ring of formal power series
over $R$ in two variables $t$ and $u$,

$$\sum_{i, j \ge 0} \frac{1}{j!}\, [X^i] f^{(j)}\; t^i u^j = f(t + u),$$

where $f(t + u)$ is the substitution of $t + u$ into $f$. In other words, the exponential
generating series $\sum_j f^{(j)}(t)\, u^j / j!$ of the successive derivatives of $f$ is
$f(t + u)$.

## Sources

- Emanuele Munarini, *Combinatorial Identities for the Tricomi Polynomials*, Journal of Integer Sequences 23 (2020), Article 20.9.4, equation (5.32).

Formalized by `PowerSeries.taylorFormula`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/TaylorFormula.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/TaylorFormula.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/index.html#taylor-formula).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Formal power series](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/formal-power-series)
