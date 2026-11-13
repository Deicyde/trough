---
declaration: section
origin: cited
lean: supNormOn, ConvergesNormallyOn, supNormOn_empty, supNormOn_zero, supNormOn_mono, convergesNormallyOn_empty, convergesNormallyOn_zero, ConvergesNormallyOn.mono
statement: formalized
proof: formalized
---

# Normal convergence of series of functions

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html).

## Extended supremum norm on a set

Let $X$ be a type and $E$ a seminormed additive
commutative group. For a function $g : X \to E$ and a set $S \subseteq X$, the supremum norm of
$g$ on $S$ is $\sup_{x \in S} \|g(x)\|$, taken in the extended nonnegative reals $[0, \infty]$;
in particular it is $0$ when $S$ is empty and $\infty$ when $\|g\|$ is unbounded on $S$.

Formalized by `supNormOn`, a definition declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#sup-norm-on).

## Normal convergence of a series of functions on a set

Let $X$ be a type and $E$ a
seminormed additive commutative group. A series of functions $f_n \colon X \to E$
($n \in \mathbb{N}$) converges normally on a set $S \subseteq X$ when the sum
$\sum_{n} \sup_{x \in S} \|f_n(x)\|$ is finite, where each supremum norm and the sum are taken in
the extended nonnegative reals $[0, \infty]$.

Formalized by `ConvergesNormallyOn`, a definition declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#converges-normally-on).

## Supremum norm over the empty set

For every function $g \colon X \to E$ into a seminormed
additive commutative group $E$, the supremum norm of $g$ on the empty set, valued in
$[0, \infty]$, is $0$.

Formalized by `supNormOn_empty`, a theorem declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#sup-norm-on-empty).

## Supremum norm of the zero function

For every set $S \subseteq X$, the supremum norm on
$S$ of the zero function from $X$ to a seminormed additive commutative group $E$ is $0$.

Formalized by `supNormOn_zero`, a theorem declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#sup-norm-on-zero).

## Monotonicity of the supremum norm in the domain

If $T \subseteq S \subseteq X$, then for
every function $g \colon X \to E$ into a seminormed additive commutative group $E$, the supremum
norm of $g$ on $T$ is at most the supremum norm of $g$ on $S$.

Formalized by `supNormOn_mono`, a theorem declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#sup-norm-on-mono).

## Normal convergence on the empty set

Every series of functions $f_n \colon X \to E$
($n \in \mathbb{N}$) with values in a seminormed additive commutative group $E$ converges
normally on the empty set.

Formalized by `convergesNormallyOn_empty`, a theorem declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#converges-normally-on-empty).

## Normal convergence of the zero series

For every set $S \subseteq X$ and every seminormed
additive commutative group $E$, the series of functions $X \to E$ whose terms are all zero
converges normally on $S$.

Formalized by `convergesNormallyOn_zero`, a theorem declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#converges-normally-on-zero).

## Normal convergence passes to subsets

Let $f_n \colon X \to E$ ($n \in \mathbb{N}$) be
functions into a seminormed additive commutative group $E$ and let $T \subseteq S \subseteq X$.
If the series $\sum_n f_n$ converges normally on $S$, then it converges normally on $T$.

Formalized by `ConvergesNormallyOn.mono`, a theorem declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#mono).

## Local normal convergence of a series of functions on a set

Let $X$ be a topological
space and $E$ a seminormed additive commutative group. A series of functions
$f_n \colon X \to E$ ($n \in \mathbb{N}$) converges locally normally on a set $S \subseteq X$ when
every $x \in S$ has a neighbourhood $U$ such that the series converges normally on $U \cap S$.

Formalized by `ConvergesLocallyNormallyOn`, a definition declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#converges-locally-normally-on).

## Local normal convergence gives a neighbourhood of each point of the set

Let $X$ be a
topological space, $E$ a seminormed additive commutative group, $f_n \colon X \to E$
($n \in \mathbb{N}$) functions and $S \subseteq X$. If the series $\sum_n f_n$ converges locally
normally on $S$, then every $x \in S$ has a neighbourhood $U$ such that the series converges
normally on $U \cap S$.

Formalized by `ConvergesLocallyNormallyOn.exists_nhds_inter`, a theorem declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#exists-nhds-inter).

## Local normal convergence on the empty set

Let $X$ be a topological space. Every series
of functions $f_n \colon X \to E$ ($n \in \mathbb{N}$) with values in a seminormed additive
commutative group $E$ converges locally normally on the empty set.

Formalized by `convergesLocallyNormallyOn_empty`, a theorem declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#converges-locally-normally-on-empty).

## Local normal convergence of the zero series

Let $X$ be a topological space and $E$ a
seminormed additive commutative group. For every set $S \subseteq X$, the series of functions
$X \to E$ whose terms are all zero converges locally normally on $S$.

Formalized by `convergesLocallyNormallyOn_zero`, a theorem declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#converges-locally-normally-on-zero).

## Local normal convergence passes to subsets

Let $X$ be a topological space, let
$f_n \colon X \to E$ ($n \in \mathbb{N}$) be functions into a seminormed additive commutative
group $E$ and let $T \subseteq S \subseteq X$. If the series $\sum_n f_n$ converges locally
normally on $S$, then it converges locally normally on $T$.

Formalized by `ConvergesLocallyNormallyOn.mono`, a theorem declared in [MathlibExt/Analysis/Normed/Series/NormalConvergence.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Series/NormalConvergence.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#mono-2).

## Normal convergence gives summable real sup norms

Let $E$ be a seminormed additive
commutative group, $S$ a subset of a type $X$ and $f_n \colon X \to E$ for $n \in \mathbb{N}$.
If the series $\sum_n f_n$ converges normally on $S$, that is
$\sum_n \sup_{x \in S} \|f_n(x)\| < \infty$ with the suprema taken in $[0, \infty]$, then the
sequence of sup norms $\left(\sup_{x \in S} \|f_n(x)\|\right)_n$, viewed as real numbers, is
summable.

Formalized by `ConvergesNormallyOn.summable_toReal_supNormOn`, a theorem declared in [MathlibExt/Analysis/Complex/NormalConvergence.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/NormalConvergence.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#summable-to-real-sup-norm-on).

## Normal convergence implies pointwise absolute convergence

Let $E$ be a seminormed
additive commutative group, $S$ a subset of a type $X$ and $f_n \colon X \to E$ for
$n \in \mathbb{N}$. If the series $\sum_n f_n$ converges normally on $S$, that is
$\sum_n \sup_{x \in S} \|f_n(x)\| < \infty$ with the suprema taken in $[0, \infty]$, then for
every $x \in S$ the series $\sum_n \|f_n(x)\|$ is summable.

Formalized by `ConvergesNormallyOn.summable_norm`, a theorem declared in [MathlibExt/Analysis/Complex/NormalConvergence.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/NormalConvergence.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#summable-norm).

## Local normal convergence implies pointwise absolute convergence

Let $E$ be a seminormed
additive commutative group, $S$ a subset of a topological space $X$ and $f_n \colon X \to E$ for
$n \in \mathbb{N}$. If the series $\sum_n f_n$ converges locally normally on $S$, that is every
$x \in S$ has a neighbourhood $U$ with $\sum_n \sup_{y \in U \cap S} \|f_n(y)\| < \infty$ (suprema
taken in $[0, \infty]$), then for every $x \in S$ the series $\sum_n \|f_n(x)\|$ is summable.

Formalized by `ConvergesLocallyNormallyOn.summable_norm`, a theorem declared in [MathlibExt/Analysis/Complex/NormalConvergence.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/NormalConvergence.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#summable-norm-2).

## Weierstrass M-test: normal convergence implies uniform convergence

Let $E$ be a complete
normed additive commutative group, $S$ a subset of a type $X$ and $f_n \colon X \to E$ for
$n \in \mathbb{N}$. If the series $\sum_n f_n$ converges normally on $S$, that is
$\sum_n \sup_{x \in S} \|f_n(x)\| < \infty$ with the suprema taken in $[0, \infty]$, then the
partial sums $x \mapsto \sum_{n < N} f_n(x)$ converge uniformly on $S$, as $N \to \infty$, to
the pointwise sum $x \mapsto \sum_{n=0}^{\infty} f_n(x)$.

Formalized by `ConvergesNormallyOn.tendstoUniformlyOn_tsum_nat`, a theorem declared in [MathlibExt/Analysis/Complex/NormalConvergence.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/NormalConvergence.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#tendsto-uniformly-on-tsum-nat).

## Derivative series of a locally normally convergent holomorphic series

Let $E$ be a
normed space over $\mathbb{C}$, $S \subseteq \mathbb{C}$ an open set and $f_n \colon \mathbb{C}
\to E$ for $n \in \mathbb{N}$ functions that are complex differentiable on $S$. If the series
$\sum_n f_n$ converges locally normally on $S$, that is every $z \in S$ has a neighbourhood $U$
with $\sum_n \sup_{w \in U \cap S} \|f_n(w)\| < \infty$ (suprema taken in $[0, \infty]$), then
the series of derivatives $\sum_n f_n'$ also converges locally normally on $S$.

Formalized by `ConvergesLocallyNormallyOn.deriv`, a theorem declared in [MathlibExt/Analysis/Complex/NormalConvergence.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/NormalConvergence.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#deriv).

## Local normal convergence implies locally uniform convergence

Let $E$ be a complete
normed additive commutative group, $S$ a subset of a topological space $X$ and
$f_n \colon X \to E$ for $n \in \mathbb{N}$. If the series $\sum_n f_n$ converges locally
normally on $S$, that is every $x \in S$ has a neighbourhood $U$ with
$\sum_n \sup_{y \in U \cap S} \|f_n(y)\| < \infty$ (suprema taken in $[0, \infty]$), then the
partial sums $x \mapsto \sum_{n < N} f_n(x)$ converge locally uniformly on $S$, as
$N \to \infty$, to the pointwise sum $x \mapsto \sum_{n=0}^{\infty} f_n(x)$.

Formalized by `ConvergesLocallyNormallyOn.tendstoLocallyUniformlyOn_tsum_nat`, a theorem declared in [MathlibExt/Analysis/Complex/NormalConvergence.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/NormalConvergence.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#tendsto-locally-uniformly-on-tsum-nat).

## Termwise differentiation of locally normally convergent holomorphic series

Let $E$ be a
complete normed space over $\mathbb{C}$, $S \subseteq \mathbb{C}$ an open set and
$f_n \colon \mathbb{C} \to E$ for $n \in \mathbb{N}$ functions that are complex differentiable
on $S$. If the series $\sum_n f_n$ converges locally normally on $S$, that is every $z \in S$
has a neighbourhood $U$ with $\sum_n \sup_{w \in U \cap S} \|f_n(w)\| < \infty$ (suprema taken
in $[0, \infty]$), then for every $z \in S$ the function $w \mapsto \sum_{n=0}^{\infty} f_n(w)$
has derivative $\sum_{n=0}^{\infty} f_n'(z)$ at $z$.

Formalized by `ConvergesLocallyNormallyOn.hasDerivAt_tsum`, a theorem declared in [MathlibExt/Analysis/Complex/NormalConvergence.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/NormalConvergence.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html#has-deriv-at-tsum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Normal convergence of series of functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/convergence/normal-convergence-of-series-of-functions)
