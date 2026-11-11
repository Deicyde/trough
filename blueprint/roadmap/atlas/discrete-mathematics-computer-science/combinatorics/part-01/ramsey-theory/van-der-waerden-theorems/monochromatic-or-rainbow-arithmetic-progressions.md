---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosRainbowAPGrowthWanted.HasGoodAP, MathlibExt.Combinatorics.ErdosRainbowAPGrowthWanted.H, MathlibExt.Combinatorics.ErdosRainbowAPGrowthWanted.conjecture, MathlibExt.Combinatorics.ErdosRainbowAPGrowthWanted.conjecture_holds
statement: formalized
---

# Monochromatic or rainbow arithmetic progressions

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-or-rainbow-arithmetic-progressions/index.html).

## Good arithmetic progressions

Let $f : \mathbb{N} \to \mathbb{N}$ be a colouring and let
$N$ and $k$ be natural numbers. The colouring $f$ has a good $k$-term arithmetic progression below
$N$ if there are natural numbers $a$ and $d > 0$ with $a + d(k - 1) < N$, where $k - 1$ is
natural-number subtraction (so it is $0$ when $k = 0$), such that the colours $f(a + di)$ for
$i < k$ are either all equal (the progression is monochromatic) or pairwise distinct (it is
rainbow). For $k \ge 1$ the condition $a + d(k - 1) < N$ says that every term $a + di$ with
$i < k$ lies in $\{0, \dots, N - 1\}$.

Formalized by `MathlibExt.Combinatorics.ErdosRainbowAPGrowthWanted.HasGoodAP`, a definition declared in [WantedExt/Combinatorics/ErdosRainbowAPGrowthWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosRainbowAPGrowthWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-or-rainbow-arithmetic-progressions/index.html#has-good-ap).

## Monochromatic-or-rainbow progression number

For a natural number $k$, $H(k)$ is the least
natural number $N$ such that every colouring $f : \mathbb{N} \to \mathbb{N}$ has a good $k$-term
arithmetic progression below $N$, that is, there are natural numbers $a$ and $d > 0$ with
$a + d(k - 1) < N$, where $k - 1$ is natural-number subtraction, such that the colours $f(a + di)$
for $i < k$ are all equal or pairwise distinct. If no such $N$ exists, then $H(k) = 0$.

Formalized by `MathlibExt.Combinatorics.ErdosRainbowAPGrowthWanted.H`, a definition declared in [WantedExt/Combinatorics/ErdosRainbowAPGrowthWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosRainbowAPGrowthWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-or-rainbow-arithmetic-progressions/index.html#h).

## Erdős Problem 190 on monochromatic or rainbow progressions

For a natural number $k$, let
$H(k)$ be the least natural number $N$ such that every colouring $f : \mathbb{N} \to \mathbb{N}$
has a good $k$-term arithmetic progression below $N$, that is, there are natural numbers $a$ and
$d > 0$ with $a + d(k - 1) < N$, where $k - 1$ is natural-number subtraction, such that the colours
$f(a + di)$ for $i < k$ are all equal or pairwise distinct; let $H(k) = 0$ if no such $N$ exists.
The proposition asserts that $H(k)^{1/k}/k \to \infty$ as $k \to \infty$.

Formalized by `MathlibExt.Combinatorics.ErdosRainbowAPGrowthWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosRainbowAPGrowthWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosRainbowAPGrowthWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-or-rainbow-arithmetic-progressions/index.html#conjecture).

## Solution of Erdős Problem 190 on monochromatic or rainbow progressions

For a natural number
$k$, let $H(k)$ be the least natural number $N$ such that every colouring
$f : \mathbb{N} \to \mathbb{N}$ has a good $k$-term arithmetic progression below $N$, that is,
there are natural numbers $a$ and $d > 0$ with $a + d(k - 1) < N$, where $k - 1$ is natural-number
subtraction, such that the colours $f(a + di)$ for $i < k$ are all equal or pairwise distinct;
let $H(k) = 0$ if no such $N$ exists. Then $H(k)^{1/k}/k \to \infty$ as $k \to \infty$.

This answers Erdős Problem 190 affirmatively; it was proved by Bae and, independently, by Fox and
Hunter.

## Sources

- T. F. Bloom, Erdős Problem #190, erdosproblems.com (live page, LaTeX source and forum threads read 2026-10-22), https://www.erdosproblems.com/190; J. H. Bae, A resolution of Erdős Problem #190 via Erdős-Lovász, BCT, and Baker-Harman-Pintz, arXiv:2604.20588 (2026), https://arxiv.org/abs/2604.20588; J. Fox and Z. Hunter, Three-color van der Waerden numbers grow super-exponentially, arXiv:2606.02541 (2026), https://arxiv.org/abs/2606.02541.

Stated but not proved: `MathlibExt.Combinatorics.ErdosRainbowAPGrowthWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosRainbowAPGrowthWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosRainbowAPGrowthWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-or-rainbow-arithmetic-progressions/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monochromatic or rainbow arithmetic progressions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-or-rainbow-arithmetic-progressions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-or-rainbow-arithmetic-progressions)
