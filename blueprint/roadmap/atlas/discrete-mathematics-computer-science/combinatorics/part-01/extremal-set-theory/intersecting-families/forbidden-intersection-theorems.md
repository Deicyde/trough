---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ForbiddenIntersectionErdosProblem703Wanted.forbiddenIntersectionExponentialGap, MathlibExt.Combinatorics.ForbiddenIntersectionErdosProblem703Wanted.forbiddenIntersectionExponentialGap_holds
statement: formalized
---

# Forbidden intersection theorems

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/forbidden-intersection-theorems/index.html).

## Erdős Problem 703: exponential gap for a forbidden intersection size

The proposition that
for every $\varepsilon > 0$ there is $\delta > 0$ such that for all natural numbers $n$ and $r$ with
$\varepsilon n < r < (1/2 - \varepsilon) n$, every family $\mathcal{F}$ of subsets of
$\{1, \dots, n\}$ with $|A \cap B| \ne r$ for all $A, B \in \mathcal{F}$ (including $A = B$) has
$|\mathcal{F}| < (2 - \delta)^n$. Equivalently, $T(n, r) < (2 - \delta)^n$, where $T(n, r)$ is the
largest size of such a family.

Formalized by `MathlibExt.Combinatorics.ForbiddenIntersectionErdosProblem703Wanted.forbiddenIntersectionExponentialGap`, a definition declared in [WantedExt/Combinatorics/ForbiddenIntersectionErdosProblem703Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ForbiddenIntersectionErdosProblem703Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/forbidden-intersection-theorems/index.html#forbidden-intersection-exponential-gap).

## Frankl–Rödl forbidden intersection theorem

For every $\varepsilon > 0$ there is $\delta > 0$
such that for all natural numbers $n$ and $r$ with $\varepsilon n < r < (1/2 - \varepsilon) n$,
every family $\mathcal{F}$ of subsets of $\{1, \dots, n\}$ with $|A \cap B| \ne r$ for all
$A, B \in \mathcal{F}$ (including $A = B$) has $|\mathcal{F}| < (2 - \delta)^n$. This answers the
second question of Erdős Problem 703 in the affirmative.

## Sources

- T. F. Bloom, Erdős Problems, Problem #703, https://www.erdosproblems.com/703 (status PROVED (LEAN)); resolution: P. Frankl and V. Rödl, Forbidden intersections, Trans. Amer. Math. Soc. 300 (1987), 259-286, erdosproblems.com/703: 'The answer to the second question is yes, proved by Frankl and Rödl', https://www.erdosproblems.com/703.

Stated but not proved: `MathlibExt.Combinatorics.ForbiddenIntersectionErdosProblem703Wanted.forbiddenIntersectionExponentialGap_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ForbiddenIntersectionErdosProblem703Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ForbiddenIntersectionErdosProblem703Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/forbidden-intersection-theorems/index.html#forbidden-intersection-exponential-gap-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Forbidden intersection theorems](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/forbidden-intersection-theorems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/intersecting-families/forbidden-intersection-theorems)
