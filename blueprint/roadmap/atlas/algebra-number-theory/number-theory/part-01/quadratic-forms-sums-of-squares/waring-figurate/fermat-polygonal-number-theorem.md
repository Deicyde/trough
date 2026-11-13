---
declaration: section
origin: cited
lean: Nat.exists_eq_add_add_triangular, Nat.exists_sum_four_sq_eq_and_sum_eq_of_odd, MetaMathlibExt.fermat_polygonal_number_theorem
statement: formalized
proof: formalized
---

# Fermat polygonal number theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/fermat-polygonal-number-theorem/index.html).

## Gauss's Eureka theorem and Cauchy's lemma

## Gauss's Eureka theorem

Every natural number $n$ is a sum of three triangular numbers:
there are natural numbers $x, y, z$ with $n = T_x + T_y + T_z$, where $T_m = m(m + 1)/2$ is the
$m$-th triangular ($3$-gonal) number, so that $T_0 = 0$.

## Sources

- C. F. Gauss, *Disquisitiones Arithmeticae* (1801), as cited in Nathanson (1987), whose introduction gives the equivalent form used here: `8n + 3` is a sum of three odd squares.

Formalized by `Nat.exists_eq_add_add_triangular`, a theorem declared in [MathlibExt/NumberTheory/FermatPolygonal.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FermatPolygonal.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/fermat-polygonal-number-theorem/index.html#exists-eq-add-add-triangular).

## Cauchy's lemma

Let $a$ and $b$ be odd natural numbers with $b^2 < 4a$ and
$3a < b^2 + 2b + 4$. Then there are natural numbers $s, t, u, v$ with
$a = s^2 + t^2 + u^2 + v^2$ and $b = s + t + u + v$.

## Sources

- M. B. Nathanson, *A short proof of Cauchy's polygonal number theorem*, Proc. Amer. Math. Soc. 99 (1987), 22-24, "Cauchy's Lemma"; originally Cauchy (1813-15).

Formalized by `Nat.exists_sum_four_sq_eq_and_sum_eq_of_odd`, a theorem declared in [MathlibExt/NumberTheory/FermatPolygonal.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FermatPolygonal.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/fermat-polygonal-number-theorem/index.html#exists-sum-four-sq-eq-and-sum-eq-of-odd).

## Fermat polygonal number theorem

For every natural number $s \ge 3$, every natural
number $n$ is a sum of at most $s$ $s$-gonal numbers: there are a finite set $T$ with at most $s$
elements and natural numbers $k_i$ for $i \in T$ such that $n = \sum_{i \in T} P_s(k_i)$, where
$P_s(m) = (s - 2)\binom{m}{2} + m$ is the $m$-th $s$-gonal number. The $k_i$ may repeat, and
since $P_s(0) = 0$ the case $n = 0$ is the empty sum.

The cases $s = 3$ and $s = 4$ follow from Gauss's three-triangular-number theorem and Lagrange's
four-square theorem. For $s \ge 5$, Cauchy's lemma and Nathanson's argument for
$n \ge 120(s - 2)$ (Nathanson 1987, Theorem 1) are combined with explicit families of
representations for small $n$ and a finite computation for the remaining cases.

## Sources

- https://en.wikipedia.org/wiki/Fermat_polygonal_number_theorem.

Formalized by `MetaMathlibExt.fermat_polygonal_number_theorem`, a theorem declared in [MathlibExt/NumberTheory/FermatPolygonal.lean, line 1077](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FermatPolygonal.lean#L1077). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/fermat-polygonal-number-theorem/index.html#fermat-polygonal-number-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fermat polygonal number theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/fermat-polygonal-number-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/fermat-polygonal-number-theorem)
