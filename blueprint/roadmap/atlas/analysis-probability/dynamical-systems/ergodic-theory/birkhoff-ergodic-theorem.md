---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.Ergodic.BirkhoffWanted.maximal_ergodic, MathlibExt.Dynamics.Ergodic.BirkhoffWanted.DickSet, MathlibExt.Dynamics.Ergodic.BirkhoffWanted.dick_measurable, MathlibExt.Dynamics.Ergodic.BirkhoffWanted.dick_mem, MathlibExt.Dynamics.Ergodic.BirkhoffWanted.dick_inv, MathlibExt.Dynamics.Ergodic.BirkhoffWanted.dick_iter, MathlibExt.Dynamics.Ergodic.BirkhoffWanted.dick_sum_in, MathlibExt.Dynamics.Ergodic.BirkhoffWanted.dick_sum_out
statement: formalized
proof: formalized
---

# Birkhoff ergodic theorem

38 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html).

## Hopf maximal ergodic theorem

Let $\mu$ be a finite measure on a measurable space $\alpha$,
let $T : \alpha \to \alpha$ preserve $\mu$, and let $f : \alpha \to \mathbb{R}$ be measurable and
$\mu$-integrable. For a natural number $n$ write $S_n f(x) = \sum_{k=0}^{n-1} f(T^k x)$. Then the
integral of $f$ with respect to $\mu$ over the set of points $x \in \alpha$ such that
$S_n f(x) > 0$ for some natural number $n$ is nonnegative.

Formalized by `MathlibExt.Dynamics.Ergodic.BirkhoffWanted.maximal_ergodic`, a theorem declared in [MathlibExt/Dynamics/Ergodic/Birkhoff.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/Birkhoff.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#maximal-ergodic).

## Maximal divergence set

Let $\alpha$ be a measurable space, $T : \alpha \to \alpha$ a map,
$g : \alpha \to \mathbb{R}$ a function and $c$ a real number. The maximal divergence set of $T$,
$g$ and $c$ is the set of points $x \in \alpha$ for which there is a rational number $q > c$ such
that $n q < \sum_{k=0}^{n-1} g(T^k x)$ for infinitely many natural numbers $n$.

Formalized by `MathlibExt.Dynamics.Ergodic.BirkhoffWanted.DickSet`, a definition declared in [MathlibExt/Dynamics/Ergodic/Birkhoff.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/Birkhoff.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#dick-set).

## Measurability of the maximal divergence set

Let $\mu$ be a measure on a measurable space
$\alpha$, let $T : \alpha \to \alpha$ preserve $\mu$, and let $g : \alpha \to \mathbb{R}$ be
measurable. Then for every real number $c$, the maximal divergence set of $T$, $g$ and $c$ is a
measurable set.

Formalized by `MathlibExt.Dynamics.Ergodic.BirkhoffWanted.dick_measurable`, a theorem declared in [MathlibExt/Dynamics/Ergodic/Birkhoff.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/Birkhoff.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#dick-measurable).

## Membership in the maximal divergence set

Let $\alpha$ be a measurable space,
$T : \alpha \to \alpha$ a map, $g : \alpha \to \mathbb{R}$ a function, $c$ a real number and
$x \in \alpha$. Then $x$ lies in the maximal divergence set of $T$, $g$ and $c$ if and only if
there is a rational number $q > c$ such that for every natural number $N$ there is a natural
number $n \ge N$ with $n q < \sum_{k=0}^{n-1} g(T^k x)$.

Formalized by `MathlibExt.Dynamics.Ergodic.BirkhoffWanted.dick_mem`, a theorem declared in [MathlibExt/Dynamics/Ergodic/Birkhoff.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/Birkhoff.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#dick-mem).

## Invariance of the maximal divergence set

Let $\alpha$ be a measurable space. For every map
$T : \alpha \to \alpha$, every function $g : \alpha \to \mathbb{R}$ and every real number $c$, the
preimage under $T$ of the maximal divergence set of $T$, $g$ and $c$ equals that set.

Formalized by `MathlibExt.Dynamics.Ergodic.BirkhoffWanted.dick_inv`, a theorem declared in [MathlibExt/Dynamics/Ergodic/Birkhoff.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/Birkhoff.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#dick-inv).

## Invariance of the maximal divergence set under iterates

Let $\alpha$ be a measurable
space, $T : \alpha \to \alpha$ a map, $g : \alpha \to \mathbb{R}$ a function and $c$ a real number.
For every natural number $k$ and every $x \in \alpha$, the point $T^k x$ lies in the maximal
divergence set of $T$, $g$ and $c$ if and only if $x$ does.

Formalized by `MathlibExt.Dynamics.Ergodic.BirkhoffWanted.dick_iter`, a theorem declared in [MathlibExt/Dynamics/Ergodic/Birkhoff.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/Birkhoff.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#dick-iter).

## Birkhoff sums of a function cut off to an invariant set, inside the set

Let $\alpha$ be a
measurable space, $T : \alpha \to \alpha$ a map, $g : \alpha \to \mathbb{R}$ a function, $c$ a real
number, and $D \subseteq \alpha$ a set such that for every natural number $k$ and every
$x \in \alpha$, $T^k x \in D$ if and only if $x \in D$. Let $h : \alpha \to \mathbb{R}$ satisfy
$h(y) = g(y) - c$ for $y \in D$ and $h(y) = 0$ for $y \notin D$. Then for every $x \in D$ and
every natural number $n$, $\sum_{k=0}^{n-1} h(T^k x) = \sum_{k=0}^{n-1} g(T^k x) - n c$.

Formalized by `MathlibExt.Dynamics.Ergodic.BirkhoffWanted.dick_sum_in`, a theorem declared in [MathlibExt/Dynamics/Ergodic/Birkhoff.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/Birkhoff.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#dick-sum-in).

## Birkhoff sums of a function cut off to an invariant set, outside the set

Let $\alpha$ be
a measurable space, $T : \alpha \to \alpha$ a map, $g : \alpha \to \mathbb{R}$ a function, $c$ a
real number, and $D \subseteq \alpha$ a set such that for every natural number $k$ and every
$x \in \alpha$, $T^k x \in D$ if and only if $x \in D$. Let $h : \alpha \to \mathbb{R}$ satisfy
$h(y) = g(y) - c$ for $y \in D$ and $h(y) = 0$ for $y \notin D$. Then for every $x \notin D$ and
every natural number $n$, $\sum_{k=0}^{n-1} h(T^k x) = 0$.

Formalized by `MathlibExt.Dynamics.Ergodic.BirkhoffWanted.dick_sum_out`, a theorem declared in [MathlibExt/Dynamics/Ergodic/Birkhoff.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/Birkhoff.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#dick-sum-out).

## Birkhoff pointwise ergodic theorem (ergodic case)

Let $\mu$ be a probability measure on a
measurable space $\alpha$, let $T : \alpha \to \alpha$ be ergodic with respect to $\mu$ (in
particular $T$ preserves $\mu$), and let $g : \alpha \to \mathbb{R}$ be $\mu$-integrable. Then for
$\mu$-almost every $x \in \alpha$, the Birkhoff averages $\frac{1}{n} \sum_{k=0}^{n-1} g(T^k x)$
converge to $\int g \, d\mu$ as $n \to \infty$.

## Sources

- G. D. Birkhoff, Proc. Natl. Acad. Sci. USA 17 (1931); Walters, Intro to Ergodic Theory; Lean states ergodic case for ℝ-valued integrable functions while general theorem gives conditional expectation onto invariant σ-algebra.

Formalized by `MathlibExt.Dynamics.Ergodic.BirkhoffWanted.birkhoff_pointwise_ergodic`, a theorem declared in [MathlibExt/Dynamics/Ergodic/Birkhoff.lean, line 509](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/Birkhoff.lean#L509). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#birkhoff-pointwise-ergodic).

## Integrability of Birkhoff sums

Let $\mu$ be a measure on a measurable space $\alpha$,
let $T : \alpha \to \alpha$ preserve $\mu$, and let $g : \alpha \to \mathbb{R}$ be
$\mu$-integrable. Then for every $n \in \mathbb{N}$ the Birkhoff sum
$x \mapsto \sum_{k=0}^{n-1} g(T^k x)$ is $\mu$-integrable.

Formalized by `MathlibExt.Probability.BirkhoffErgodicL1.integrable_birkhoffSum_of_measurePreserving`, a theorem declared in [MathlibExt/Probability/BirkhoffErgodicL1.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BirkhoffErgodicL1.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#integrable-birkhoff-sum-of-measure-prese).

## Integrability of Birkhoff averages

Let $\mu$ be a measure on a measurable space
$\alpha$, let $T : \alpha \to \alpha$ preserve $\mu$, and let $g : \alpha \to \mathbb{R}$ be
$\mu$-integrable. Then for every $n \in \mathbb{N}$ the Birkhoff average
$x \mapsto \frac{1}{n} \sum_{k=0}^{n-1} g(T^k x)$ is $\mu$-integrable (for $n = 0$ it is the
zero function).

Formalized by `MathlibExt.Probability.BirkhoffErgodicL1.integrable_birkhoffAverage_of_measurePreserving`, a theorem declared in [MathlibExt/Probability/BirkhoffErgodicL1.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BirkhoffErgodicL1.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#integrable-birkhoff-average-of-measure-p).

## Invariance of the integral under iterates

Let $\mu$ be a measure on a measurable space
$\alpha$, let $T : \alpha \to \alpha$ preserve $\mu$, and let $u : \alpha \to \mathbb{R}$ be
$\mu$-integrable. Then for every $k \in \mathbb{N}$, writing $T^k$ for the $k$-th iterate of
$T$, we have $\int u(T^k x) \, d\mu(x) = \int u \, d\mu$.

Formalized by `MathlibExt.Probability.BirkhoffErgodicL1.integral_comp_iterate_of_measurePreserving`, a theorem declared in [MathlibExt/Probability/BirkhoffErgodicL1.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BirkhoffErgodicL1.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#integral-comp-iterate-of-measure-preserv).

## Birkhoff averages preserve the integral

Let $\mu$ be a measure on a measurable space
$\alpha$, let $T : \alpha \to \alpha$ preserve $\mu$, and let $u : \alpha \to \mathbb{R}$ be
$\mu$-integrable. Then for every $n \ge 1$,
$\int \frac{1}{n} \sum_{k=0}^{n-1} u(T^k x) \, d\mu(x) = \int u \, d\mu$.

Formalized by `MathlibExt.Probability.BirkhoffErgodicL1.integral_birkhoffAverage_of_measurePreserving`, a theorem declared in [MathlibExt/Probability/BirkhoffErgodicL1.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BirkhoffErgodicL1.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#integral-birkhoff-average-of-measure-pre).

## Triangle inequality for Birkhoff averages

Let $T : \alpha \to \alpha$ be a map. For
$f : \alpha \to \mathbb{R}$ and $n \ge 1$ write $A_n f(x) = \frac{1}{n} \sum_{k=0}^{n-1} f(T^k x)$
for the $n$-th Birkhoff average of $f$, and $A_0 f = 0$. Then for every
$u : \alpha \to \mathbb{R}$, every $n \in \mathbb{N}$ and every $x \in \alpha$, writing $|u|$ for
the function $y \mapsto |u(y)|$, we have $|A_n u(x)| \le A_n |u|(x)$.

Formalized by `MathlibExt.Probability.BirkhoffErgodicL1.norm_birkhoffAverage_le_birkhoffAverage_norm`, a theorem declared in [MathlibExt/Probability/BirkhoffErgodicL1.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BirkhoffErgodicL1.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#norm-birkhoff-average-le-birkhoff-averag).

## Monotonicity of Birkhoff averages

Let $T : \alpha \to \alpha$ be a map. For
$u : \alpha \to \mathbb{R}$, $n \ge 1$ and $x \in \alpha$, write
$A_n u(x) = \frac{1}{n} \sum_{k=0}^{n-1} u(T^k x)$ for the $n$-th Birkhoff average of $u$ at
$x$, and $A_0 u(x) = 0$. If $u, v : \alpha \to \mathbb{R}$ satisfy $u(y) \le v(y)$ for every
$y \in \alpha$, then $A_n u(x) \le A_n v(x)$ for every $n \in \mathbb{N}$ and every
$x \in \alpha$.

Formalized by `MathlibExt.Probability.BirkhoffErgodicL1.birkhoffAverage_le_birkhoffAverage`, a theorem declared in [MathlibExt/Probability/BirkhoffErgodicL1.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BirkhoffErgodicL1.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#birkhoff-average-le-birkhoff-average).

## Birkhoff averages of a bounded function are bounded

Let $T : \alpha \to \alpha$ be a
map, let $M \ge 0$, and let $g : \alpha \to \mathbb{R}$ satisfy $|g(x)| \le M$ for every
$x \in \alpha$. Then for every $n \in \mathbb{N}$ and every $x \in \alpha$, the Birkhoff average
$\frac{1}{n} \sum_{k=0}^{n-1} g(T^k x)$ (taken to be $0$ for $n = 0$) has absolute value at
most $M$.

Formalized by `MathlibExt.Probability.BirkhoffErgodicL1.norm_birkhoffAverage_le_of_bounded`, a theorem declared in [MathlibExt/Probability/BirkhoffErgodicL1.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BirkhoffErgodicL1.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#norm-birkhoff-average-le-of-bounded).

## Birkhoff averages are $L^1$-contractions

Let $\mu$ be a measure on a measurable space
$\alpha$, let $T : \alpha \to \alpha$ preserve $\mu$, and let $g, h : \alpha \to \mathbb{R}$ be
$\mu$-integrable. For a function $f : \alpha \to \mathbb{R}$ and $n \ge 1$ write
$A_n f(x) = \frac{1}{n} \sum_{k=0}^{n-1} f(T^k x)$, and $A_0 f = 0$. Then for every
$n \in \mathbb{N}$,
$\int |A_n g(x) - A_n h(x)| \, d\mu(x) \le \int |g(x) - h(x)| \, d\mu(x)$.

Formalized by `MathlibExt.Probability.BirkhoffErgodicL1.integral_norm_birkhoffAverage_sub_le`, a theorem declared in [MathlibExt/Probability/BirkhoffErgodicL1.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BirkhoffErgodicL1.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#integral-norm-birkhoff-average-sub-le).

## Birkhoff's ergodic theorem in $L^1$ for bounded functions

Let $\mu$ be a probability
measure on a measurable space $\alpha$, let $T : \alpha \to \alpha$ be ergodic with respect to
$\mu$ (in particular $T$ preserves $\mu$), let $M \ge 0$, and let $g : \alpha \to \mathbb{R}$ be
$\mu$-integrable with $|g(x)| \le M$ for every $x \in \alpha$. For $n \ge 1$ let
$A_n g(x) = \frac{1}{n} \sum_{k=0}^{n-1} g(T^k x)$. Then
$\int \left| A_n g(x) - \int g \, d\mu \right| d\mu(x) \to 0$ as $n \to \infty$.

This follows from the almost-everywhere ergodic theorem and dominated convergence.

Formalized by `MathlibExt.Probability.BirkhoffErgodicL1.tendsto_integral_norm_birkhoffAverage_of_bounded`, a theorem declared in [MathlibExt/Probability/BirkhoffErgodicL1.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BirkhoffErgodicL1.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#tendsto-integral-norm-birkhoff-average-o).

## Birkhoff's ergodic theorem in $L^1$ (ergodic case)

Let $\mu$ be a probability measure
on a measurable space $\alpha$, let $T : \alpha \to \alpha$ be ergodic with respect to $\mu$ (in
particular $T$ preserves $\mu$), and let $g : \alpha \to \mathbb{R}$ be $\mu$-integrable. For
$n \ge 1$ let $A_n g(x) = \frac{1}{n} \sum_{k=0}^{n-1} g(T^k x)$ be the Birkhoff averages of
$g$. Then $\int \left| A_n g(x) - \int g \, d\mu \right| d\mu(x) \to 0$ as $n \to \infty$; that
is, the Birkhoff averages of $g$ converge to the constant $\int g \, d\mu$ in $L^1(\mu)$.

Formalized by `MathlibExt.Probability.BirkhoffErgodicL1.birkhoff_ergodic_theorem_L1`, a theorem declared in [MathlibExt/Probability/BirkhoffErgodicL1.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BirkhoffErgodicL1.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#birkhoff-ergodic-theorem-l1).

## Maximal Birkhoff partial sum

The maximal Birkhoff sum `max_{1 ≤ n ≤ N} ∑_{k<n} f (T^[k] x)` over the first `N` times.

Formalized by `StatMech.GarsiaMax.maxPartialSum`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/MaximalErgodic.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/MaximalErgodic.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#max-partial-sum).

## Maximal ergodic theorem

**Maximal ergodic theorem** (E. Hopf, 1954), in the finite form of A. M. Garsia, *A simple
proof of E. Hopf's maximal ergodic theorem*, 1965: for measure-preserving `T` and integrable `f`,
the integral of `f` over `{max_{1 ≤ n ≤ N} S_n f > 0}` is nonnegative. See also
`MathlibExt.Dynamics.Ergodic.BirkhoffWanted.maximal_ergodic`, the limiting form for measurable
`f`.

Formalized by `StatMech.GarsiaMax.garsia_maximal_inequality`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/MaximalErgodic.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/MaximalErgodic.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#garsia-maximal-inequality).

## Invariant set of a map

`E` is invariant under `T`: `x ∈ E ↔ T x ∈ E`, i.e. `T ⁻¹' E = E`
(see `isInvariantSet_iff_preimage_eq`).

Formalized by `StatMech.BirkhoffAE.IsInvariantSet`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#is-invariant-set).

## Invariant set as a set equal to its preimage

`IsInvariantSet T E` is the condition `T ⁻¹' E = E` used by Mathlib's `PreErgodic` and
`MeasurableSpace.invariants`.

Formalized by `StatMech.BirkhoffAE.isInvariantSet_iff_preimage_eq`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#is-invariant-set-iff-preimage-eq).

## Invariant set is invariant under every iterate

An invariant set is invariant under every iterate.

Formalized by `StatMech.BirkhoffAE.IsInvariantSet.iterate`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#iterate).

## Upper limit of Birkhoff averages

The upper limit `limsup_n A_n f x` of the Birkhoff averages, in `EReal`.

Formalized by `StatMech.BirkhoffAE.fStar`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#f-star).

## Lower limit of Birkhoff averages

The lower limit `liminf_n A_n f x` of the Birkhoff averages, in `EReal`.

Formalized by `StatMech.BirkhoffAE.fStarLow`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#f-star-low).

## Upper limit of Birkhoff averages is invariant

The upper limit of the Birkhoff averages is `T`-invariant.

Formalized by `StatMech.BirkhoffAE.fStar_comp`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#f-star-comp).

## Maximal ergodic inequality on an invariant set

The maximal inequality on an invariant set: if every point of the invariant set `E` has
some positive Birkhoff sum of `g`, then `∫_E g dμ ≥ 0`.

Formalized by `StatMech.BirkhoffAE.setIntegral_nonneg_of_invariant`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#set-integral-nonneg-of-invariant).

## Oscillation set of Birkhoff averages

The invariant set `{f_* < a} ∩ {b < f*}` where the Birkhoff averages oscillate across
`[a, b]`.

Formalized by `StatMech.BirkhoffAE.levelSet`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#level-set).

## Oscillation set of Birkhoff averages is null

For `a < b` the oscillation set `levelSet T f a b` is null.

Formalized by `StatMech.BirkhoffAE.measure_levelSet_eq_zero`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#measure-level-set-eq-zero).

## Birkhoff limit of a function

The limit of the Birkhoff averages of `f` (defined as `f*` cast to `ℝ`; it is the limit
almost everywhere by `tendsto_birkhoffAverage_ae`).

Formalized by `StatMech.BirkhoffAE.birkhoffLimit`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 553](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L553). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#birkhoff-limit).

## Birkhoff averages converge almost everywhere to the Birkhoff limit

The Birkhoff averages of an integrable `f` converge a.e. to `birkhoffLimit T f`.

Formalized by `StatMech.BirkhoffAE.tendsto_birkhoffAverage_ae`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 556](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L556). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#tendsto-birkhoff-average-ae).

## Birkhoff averages are L1 contractions

Birkhoff averages are `L¹`-contractions. See also
`MathlibExt.Probability.BirkhoffErgodicL1.integral_norm_birkhoffAverage_sub_le`, the same bound
for differences, stated with integrals of norms.

Formalized by `StatMech.BirkhoffAE.eLpNorm_birkhoffAverage_le`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 583](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L583). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#e-lp-norm-birkhoff-average-le).

## Integrability of the Birkhoff limit

The Birkhoff limit of an integrable function is integrable.

Formalized by `StatMech.BirkhoffAE.integrable_birkhoffLimit`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 619](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L619). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#integrable-birkhoff-limit).

## Birkhoff limit preserves integrals over invariant sets

On every measurable invariant set `E`, `∫_E birkhoffLimit T f dμ = ∫_E f dμ`.

Formalized by `StatMech.BirkhoffAE.setIntegral_birkhoffLimit`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#set-integral-birkhoff-limit).

## Birkhoff limit is a conditional expectation on invariant sets

The Birkhoff limit is the conditional expectation of `f` given the invariant σ-algebra.

Formalized by `StatMech.BirkhoffAE.birkhoffLimit_ae_eq_condExp`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 781](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L781). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#birkhoff-limit-ae-eq-cond-exp).

## Birkhoff's pointwise ergodic theorem

**Birkhoff's pointwise ergodic theorem** (G. D. Birkhoff, *Proof of the ergodic theorem*,
1931): for `T` preserving a finite measure `μ` and integrable `f`, the averages
`(1/n) ∑_{k<n} f ∘ T^k` converge `μ`-a.e. to `μ[f | MeasurableSpace.invariants T]`. See also
`MathlibExt.Dynamics.Ergodic.BirkhoffWanted.birkhoff_pointwise_ergodic`, the ergodic case, and
`birkhoffLimit_ae_eq_integral_of_ergodic`.

Formalized by `StatMech.BirkhoffAE.tendsto_birkhoffAverage_condExp_ae`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 823](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L823). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#tendsto-birkhoff-average-cond-exp-ae).

## Birkhoff limit of an ergodic map is the space average

For ergodic `T` on a probability space the Birkhoff limit is the constant `∫ f dμ`; this is
`MathlibExt.Dynamics.Ergodic.BirkhoffWanted.birkhoff_pointwise_ergodic` combined with
`tendsto_birkhoffAverage_ae`.

Formalized by `StatMech.BirkhoffAE.birkhoffLimit_ae_eq_integral_of_ergodic`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean, line 834](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/BirkhoffPointwise.lean#L834). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html#birkhoff-limit-ae-eq-integral-of-ergodic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Birkhoff ergodic theorem](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/ergodic-theory/birkhoff-ergodic-theorem)
