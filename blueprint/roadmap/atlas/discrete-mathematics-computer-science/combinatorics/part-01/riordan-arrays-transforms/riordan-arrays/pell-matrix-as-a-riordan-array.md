---
declaration: section
origin: cited
lean: MetaMathlibExt.pell_riordan_general, MetaMathlibExt.pell_riordan
statement: formalized
proof: formalized
---

# Pell matrix as a Riordan array

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pell-matrix-as-a-riordan-array/index.html).

## Generalized Pell matrix as a Riordan array, for every k

Let $k$ be a natural number
and let $p(n, m)$, for natural numbers $n$ and $m$, be natural numbers such that for every $n$
the power series $\sum_{m \ge 0} p(n, m)\, x^m$ over $\mathbb{Q}$ satisfies
$\left(\sum_{m \ge 0} p(n, m)\, x^m\right)(1 - x)^{n+1} = (1 + x + \dots + x^k)^n$. Then for all
natural numbers $n$ and $m$, the coefficient of $x^n$ in
$\frac{1}{1-x} \left(\frac{x(1 + x + \dots + x^k)}{1-x}\right)^m$ is $p(m, n - m)$ if $m \le n$
and $0$ otherwise. That is, the lower-triangular matrix whose entry in row $n$ and column $m$
is $p(m, n - m)$ is the Riordan array
$\left(\frac{1}{1-x}, \frac{x(1 + x + \dots + x^k)}{1-x}\right)$.

Formalized by `MetaMathlibExt.pell_riordan_general`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PellRiordan.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/PellRiordan.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pell-matrix-as-a-riordan-array/index.html#pell-riordan-general).

## Generalized Pell matrix as a Riordan array

Let $k \ge 2$ be a natural number and let
$p(n, m)$, for natural numbers $n$ and $m$, be natural numbers such that for every $n$ the power
series $\sum_{m \ge 0} p(n, m)\, x^m$ over $\mathbb{Q}$ satisfies
$\left(\sum_{m \ge 0} p(n, m)\, x^m\right)(1 - x)^{n+1} = (1 + x + \dots + x^k)^n$. Then for all
natural numbers $n$ and $m$, the coefficient of $x^n$ in
$\frac{1}{1-x} \left(\frac{x(1 + x + \dots + x^k)}{1-x}\right)^m$ is $p(m, n - m)$ if $m \le n$
and $0$ otherwise. That is, the lower-triangular matrix whose entry in row $n$ and column $m$
is $p(m, n - m)$ is the Riordan array
$\left(\frac{1}{1-x}, \frac{x(1 + x + \dots + x^k)}{1-x}\right)$.

## Sources

- Jhon J. Bravo, Jose L. Herrera, and José L. Ramírez, "Combinatorial Interpretation of Generalized Pell Numbers," Journal of Integer Sequences 23 (2020), Article 20.2.1, Theorem, lines 269–272, https://cs.uwaterloo.ca/journals/JIS/VOL23/Bravo/bravo4.tex It follows from `pell_riordan_general`; the hypothesis `hk` is unused and keeps the source's shape.

Formalized by `MetaMathlibExt.pell_riordan`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PellRiordan.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/PellRiordan.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pell-matrix-as-a-riordan-array/index.html#pell-riordan).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pell matrix as a Riordan array](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pell-matrix-as-a-riordan-array/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pell-matrix-as-a-riordan-array)
