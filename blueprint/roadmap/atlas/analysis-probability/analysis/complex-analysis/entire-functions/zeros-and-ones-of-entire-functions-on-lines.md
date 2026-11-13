---
declaration: section
origin: cited
lean: MathlibExt.Analysis.EntireZerosOnesLinesWanted.IsComplexLine, MathlibExt.Analysis.EntireZerosOnesLinesWanted.ZerosOnLine, MathlibExt.Analysis.EntireZerosOnesLinesWanted.OnesOnLine, MathlibExt.Analysis.EntireZerosOnesLinesWanted.conjecture, MathlibExt.Analysis.EntireZerosOnesLinesWanted.conjecture_holds
statement: formalized
---

# Zeros and ones of entire functions on lines

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/zeros-and-ones-of-entire-functions-on-lines/index.html).

## Straight lines in the complex plane

A set $s \subseteq \mathbb{C}$ is a straight line if
there are $a, v \in \mathbb{C}$ with $v \ne 0$ such that $s = \{a + tv : t \in \mathbb{R}\}$.

## Sources

- Research Problems in Function Theory, Problem 2.24 (record AMR-022-2024).

Formalized by `MathlibExt.Analysis.EntireZerosOnesLinesWanted.IsComplexLine`, a definition declared in [WantedExt/Analysis/EntireZerosOnesLinesWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/EntireZerosOnesLinesWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/zeros-and-ones-of-entire-functions-on-lines/index.html#is-complex-line).

## Functions whose zeros lie in a given set

A function $f : \mathbb{C} \to \mathbb{C}$ has
all its zeros in a set $l \subseteq \mathbb{C}$ if every $z \in \mathbb{C}$ with $f(z) = 0$ lies
in $l$.

## Sources

- Research Problems in Function Theory, Problem 2.24 (record AMR-022-2024).

Formalized by `MathlibExt.Analysis.EntireZerosOnesLinesWanted.ZerosOnLine`, a definition declared in [WantedExt/Analysis/EntireZerosOnesLinesWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/EntireZerosOnesLinesWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/zeros-and-ones-of-entire-functions-on-lines/index.html#zeros-on-line).

## Functions whose ones lie in a given set

A function $f : \mathbb{C} \to \mathbb{C}$ has
all its ones in a set $m \subseteq \mathbb{C}$ if every $z \in \mathbb{C}$ with $f(z) = 1$ lies
in $m$.

## Sources

- Research Problems in Function Theory, Problem 2.24 (record AMR-022-2024).

Formalized by `MathlibExt.Analysis.EntireZerosOnesLinesWanted.OnesOnLine`, a definition declared in [WantedExt/Analysis/EntireZerosOnesLinesWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/EntireZerosOnesLinesWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/zeros-and-ones-of-entire-functions-on-lines/index.html#ones-on-line).

## Zeros and ones of an entire function on two distinct lines

This is the statement that
there exist an entire function $f : \mathbb{C} \to \mathbb{C}$ and two distinct straight lines
$l \ne m$ in $\mathbb{C}$ such that every zero of $f$ lies on $l$, every solution of $f(z) = 1$
lies on $m$, and $f$ has infinitely many zeros and infinitely many solutions of $f(z) = 1$. Here
a straight line is a set $\{a + tv : t \in \mathbb{R}\}$ with $a, v \in \mathbb{C}$ and $v \ne 0$.

## Sources

- Research Problems in Function Theory, Problem 2.24 (record AMR-022-2024).

Formalized by `MathlibExt.Analysis.EntireZerosOnesLinesWanted.conjecture`, a definition declared in [WantedExt/Analysis/EntireZerosOnesLinesWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/EntireZerosOnesLinesWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/zeros-and-ones-of-entire-functions-on-lines/index.html#conjecture).

## Entire functions with zeros and ones on two distinct lines exist

There exist an entire
function $f : \mathbb{C} \to \mathbb{C}$ and two distinct straight lines $l \ne m$ in
$\mathbb{C}$ such that every zero of $f$ lies on $l$, every solution of $f(z) = 1$ lies on $m$,
and $f$ has infinitely many zeros and infinitely many solutions of $f(z) = 1$. Here a straight
line is a set $\{a + tv : t \in \mathbb{R}\}$ with $a, v \in \mathbb{C}$ and $v \ne 0$.

For example, $e^z - 1$ has the zeros $2\pi i k$, $k \in \mathbb{Z}$, on the imaginary axis and
the solutions $\log 2 + 2\pi i k$ of $e^z - 1 = 1$ on a parallel line. Baker (Math. Z. 86
(1964)) and Kobayashi (Kodai Math. J. 2 (1979)) showed that for parallel lines the only
transcendental examples are $f = P(e^{az})$ with $P$ a polynomial and $a$ a constant.

## Sources

- Walter Bergweiler, Alexandre Eremenko and Aimo Hinkkanen, Entire functions with two radially distributed values, Math. Proc. Cambridge Philos. Soc. 165 (2018) 93-108, arXiv:1509.03283, https://arxiv.org/abs/1509.03283.

Stated but not proved: `MathlibExt.Analysis.EntireZerosOnesLinesWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/EntireZerosOnesLinesWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/EntireZerosOnesLinesWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/zeros-and-ones-of-entire-functions-on-lines/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zeros and ones of entire functions on lines](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/zeros-and-ones-of-entire-functions-on-lines/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/entire-functions/zeros-and-ones-of-entire-functions-on-lines)
