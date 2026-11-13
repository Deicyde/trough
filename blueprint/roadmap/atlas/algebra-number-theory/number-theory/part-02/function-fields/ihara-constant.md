---
declaration: section
origin: cited
lean: MathlibExt.Analysis.iharaRatio, MathlibExt.Analysis.iharaConstantOf, MathlibExt.Analysis.iharaConstantOf_le_of_eventually_ratio_le, MathlibExt.Analysis.le_iharaConstantOf_of_frequently_ratio_le, MathlibExt.Analysis.iharaRatio_le_of_le_mul, MathlibExt.Analysis.le_iharaRatio_of_mul_le, MathlibExt.Analysis.iharaConstantOf_le_of_eventually_le, MathlibExt.Analysis.iharaConstantOf_le_of_eventually_le_add
statement: formalized
proof: formalized
---

# Ihara constant

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html).

## Normalized Ihara ratio

For a sequence $N : \mathbb{N} \to \mathbb{N}$ and
$g \in \mathbb{N}$, the normalized ratio of $N$ at $g$ is the extended nonnegative real $N(g)/g$
when $g > 0$, and $0$ when $g = 0$.

Formalized by `MathlibExt.Analysis.iharaRatio`, a definition declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#ihara-ratio).

## Abstract Ihara constant of a sequence

For a sequence $N : \mathbb{N} \to \mathbb{N}$,
the abstract Ihara constant of $N$ is $\limsup_{g \to \infty} N(g)/g \in [0, \infty]$, the limit
superior as $g \to \infty$ of the normalized ratios of $N$.

Formalized by `MathlibExt.Analysis.iharaConstantOf`, a definition declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#ihara-constant-of).

## Eventual ratio bounds bound the abstract Ihara constant

Let
$N : \mathbb{N} \to \mathbb{N}$ and $c \in [0, \infty]$. If the normalized ratio of $N$ at $g$ is
at most $c$ for all sufficiently large $g$, then the abstract Ihara constant of $N$ is at most
$c$.

Formalized by `MathlibExt.Analysis.iharaConstantOf_le_of_eventually_ratio_le`, a theorem declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#ihara-constant-of-le-of-eventually-ratio).

## Lower bound for the Ihara constant from the normalized ratios

Let
$N : \mathbb{N} \to \mathbb{N}$, let $c \in [0, \infty]$, and for each $g \in \mathbb{N}$ let
$r_N(g) \in [0, \infty]$ be the normalized ratio $N(g)/g$, with $r_N(0) = 0$. If $c \le r_N(g)$
for infinitely many $g$, then $c \le \limsup_{g \to \infty} r_N(g)$, the Ihara constant of $N$.

Formalized by `MathlibExt.Analysis.le_iharaConstantOf_of_frequently_ratio_le`, a theorem declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#le-ihara-constant-of-of-frequently-ratio).

## Linear upper bound on a normalized ratio

Let $N : \mathbb{N} \to \mathbb{N}$,
$g \in \mathbb{N}$ and $c \in [0, \infty]$. If $N(g) \le c \cdot g$ in $[0, \infty]$, then the
normalized ratio of $N$ at $g$ is at most $c$.

Formalized by `MathlibExt.Analysis.iharaRatio_le_of_le_mul`, a theorem declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#ihara-ratio-le-of-le-mul).

## Lower bound for one normalized Ihara ratio

Let $N : \mathbb{N} \to \mathbb{N}$,
$c \in [0, \infty]$ and $g > 0$ an integer. If $c \cdot g \le N(g)$ in $[0, \infty]$, then
$c \le N(g)/g$, where the normalized ratio $N(g)/g$ is taken in $[0, \infty]$.

Formalized by `MathlibExt.Analysis.le_iharaRatio_of_mul_le`, a theorem declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#le-ihara-ratio-of-mul-le).

## Eventual linear upper bound on the abstract Ihara constant

Let
$N : \mathbb{N} \to \mathbb{N}$ and $c \in [0, \infty]$. If $N(g) \le c \cdot g$ in $[0, \infty]$
for all sufficiently large $g$, then the abstract Ihara constant of $N$ is at most $c$.

Formalized by `MathlibExt.Analysis.iharaConstantOf_le_of_eventually_le`, a theorem declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#ihara-constant-of-le-of-eventually-le).

## Eventual affine upper bound on the abstract Ihara constant

Let
$N : \mathbb{N} \to \mathbb{N}$, $c \in [0, \infty]$ and $d \in [0, \infty)$. If
$N(g) \le c \cdot g + d$ in $[0, \infty]$ for all sufficiently large $g$, then the abstract Ihara
constant of $N$ is at most $c$.

Formalized by `MathlibExt.Analysis.iharaConstantOf_le_of_eventually_le_add`, a theorem declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#ihara-constant-of-le-of-eventually-le-ad).

## Lower bound for the Ihara constant from a linear bound

Let $N : \mathbb{N} \to \mathbb{N}$
and $c \in [0, \infty]$. If there are infinitely many integers $g > 0$ with $c \cdot g \le N(g)$
in $[0, \infty]$, then $c \le \limsup_{g \to \infty} N(g)/g$, the Ihara constant of $N$, where the
ratio $N(g)/g$ is taken in $[0, \infty]$ and set to $0$ at $g = 0$.

Formalized by `MathlibExt.Analysis.le_iharaConstantOf_of_frequently_le`, a theorem declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#le-ihara-constant-of-of-frequently-le).

## Monotonicity of the normalized ratio

Let $N, M : \mathbb{N} \to \mathbb{N}$ and
$g \in \mathbb{N}$. If $N(g) \le M(g)$, then the normalized ratio of $N$ at $g$ is at most the
normalized ratio of $M$ at $g$.

Formalized by `MathlibExt.Analysis.iharaRatio_mono`, a theorem declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#ihara-ratio-mono).

## Monotonicity of the abstract Ihara constant

Let $N, M : \mathbb{N} \to \mathbb{N}$. If
$N(g) \le M(g)$ for all sufficiently large $g$, then the abstract Ihara constant of $N$ is at
most that of $M$.

Formalized by `MathlibExt.Analysis.iharaConstantOf_mono_of_eventually_le`, a theorem declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#ihara-constant-of-mono-of-eventually-le).

## The abstract Ihara constant ignores finitely many values

Let
$N, M : \mathbb{N} \to \mathbb{N}$. If $N(g) = M(g)$ for all sufficiently large $g$, then $N$ and
$M$ have the same abstract Ihara constant. In particular, changing finitely many values of $N$
does not change its abstract Ihara constant.

Formalized by `MathlibExt.Analysis.iharaConstantOf_congr`, a theorem declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#ihara-constant-of-congr).

## Agreement from an index onward preserves the abstract Ihara constant

Let
$N, M : \mathbb{N} \to \mathbb{N}$ and $G \in \mathbb{N}$. If $N(g) = M(g)$ for every $g \ge G$,
then $N$ and $M$ have the same abstract Ihara constant.

Formalized by `MathlibExt.Analysis.iharaConstantOf_eq_of_eventually_eq`, a theorem declared in [MathlibExt/Analysis/IharaConstantOf.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/IharaConstantOf.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html#ihara-constant-of-eq-of-eventually-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ihara constant](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/ihara-constant/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/function-fields/ihara-constant)
