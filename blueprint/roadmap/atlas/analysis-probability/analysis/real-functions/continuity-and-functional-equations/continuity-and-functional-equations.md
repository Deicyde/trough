---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.NowhereDifferentiable.exists_continuous_nowhere_differentiable, MathlibExt.MeasureTheory.StrictLiminfGapFiniteSetCountableWanted.countable_setOf_lt_top_of_lt_liminf, MetaMathlibExt.blumberg_theorem, MathlibExt.Analysis.Calculus.MidpointConvexContinuousConvexWanted.convexOn_Ioo_of_continuousOn_of_midpoint_le, MathlibExt.Analysis.Complex.ScottishBook39Wanted.exists_discontinuous_subadditive_multiplicative, MathlibExt.Analysis.Calculus.GraphNonAccumulationPointsCountableWanted.countable_diff_setOf_exists_seq_tendsto_and_tendsto_apply, MathlibExt.Analysis.ScottishBook181Wanted.steinhaus181_periodization_one
statement: formalized
---

# Continuity, regularity and functional equations: its own results

7 results, 2 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/index.html).

Fine structure of real functions: Blumberg's theorem, continuous nowhere-differentiable functions (Weierstrass, Takagi), the rising sun lemma, approximate continuity, midpoint convexity, and the Cauchy, exponential and almost-additive functional equations including Hyers–Ulam stability.

## A continuous nowhere differentiable function

There exists a continuous function
$f : \mathbb{R} \to \mathbb{R}$ that is differentiable at no point of $\mathbb{R}$.

## Sources

- K. Weierstrass, 1872 lecture; P. du Bois-Reymond, J. Reine Angew. Math. 79 (1875), 21-37, DOI 10.1515/crll.1875.79.21.

Formalized by `MathlibExt.Analysis.Calculus.NowhereDifferentiable.exists_continuous_nowhere_differentiable`, a theorem declared in [MathlibExt/Analysis/Calculus/NowhereDifferentiable.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/NowhereDifferentiable.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/index.html#exists-continuous-nowhere-differentiable).

## A strict liminf gap at every finite value forces countably many finite values

Let
$f : [0,1] \to [0,\infty]$ be such that for every $y \in [0,1]$ with $f(y) \ne \infty$,

$$
\liminf_{x \to y,\ x \ne y} f(x) > f(y),
$$

where $x$ ranges over $[0,1]$. Then the set $\{y\in[0,1] : f(y) < \infty\}$ is countable.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Real functions; Functions of one variable), problem `ma_proofbench_l2_32`.

Stated but not proved: `MathlibExt.MeasureTheory.StrictLiminfGapFiniteSetCountableWanted.countable_setOf_lt_top_of_lt_liminf` is written with `theorem_wanted` in [WantedExt/MeasureTheory/StrictLiminfGapFiniteSetCountableWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/StrictLiminfGapFiniteSetCountableWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/index.html#countable-set-of-lt-top-of-lt-liminf).

## Blumberg's theorem

For every function $f : \mathbb{R} \to \mathbb{R}$ there is a dense
set $D \subseteq \mathbb{R}$ such that the restriction of $f$ to $D$ is continuous.

## Sources

- https://en.wikipedia.org/wiki/Blumberg_theorem.

Formalized by `MetaMathlibExt.blumberg_theorem`, a theorem declared in [MathlibExt/Analysis/Blumberg.lean, line 945](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Blumberg.lean#L945). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/index.html#blumberg-theorem).

## Continuous midpoint-convex functions are convex

Let $a < b$ be real numbers and let
$\varphi : \mathbb{R} \to \mathbb{R}$ be continuous on $(a, b)$ and satisfy
$\varphi\bigl(\frac{x+y}{2}\bigr) \le \frac{\varphi(x) + \varphi(y)}{2}$ for all $x, y \in (a, b)$.
Then $\varphi$ is convex on $(a, b)$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_61`.

Stated but not proved: `MathlibExt.Analysis.Calculus.MidpointConvexContinuousConvexWanted.convexOn_Ioo_of_continuousOn_of_midpoint_le` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/MidpointConvexContinuousConvexWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/MidpointConvexContinuousConvexWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/index.html#convex-on-ioo-of-continuous-on-of-midpoi).

## Discontinuous subadditive multiplicative functions on $\mathbb{C}$

There is a function
$\varphi : \mathbb{C} \to \mathbb{R}$ that is not continuous, satisfies $\varphi(x) \ge 0$ for
all $x \in \mathbb{C}$, is not identically $0$ and not identically $1$, and satisfies
$\varphi(x + y) \le \varphi(x) + \varphi(y)$ and $\varphi(xy) = \varphi(x)\varphi(y)$ for all
$x, y \in \mathbb{C}$.

This answers Problem 39 of the Scottish Book (Auerbach), which notes that the continuous
functions with these properties are exactly $\varphi(x) = |x|^\alpha$ with $0 < \alpha \le 1$ and
asks whether discontinuous ones exist. Mazur's answer is $\varphi(x) = |f(x)|$ for a
discontinuous field automorphism $f$ of $\mathbb{C}$.

## Sources

- H. Auerbach, Problem 39 of the Scottish Book; addendum of S. Mazur, 10 April 1937, in the Scottish Book, via Lebesgue's theorem on the existence of a discontinuous automorphism of `ℂ` (Kamke); see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Analysis.Complex.ScottishBook39Wanted.exists_discontinuous_subadditive_multiplicative` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/ScottishBook39Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/ScottishBook39Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/index.html#exists-discontinuous-subadditive-multipl).

## Isolated points of a graph are countable

Let $E \subseteq \mathbb{R}^n$, let
$f : \mathbb{R}^n \to \mathbb{R}^n$, and let $F$ be the set of $x\in E$ for which there is a
sequence $(x_k)$ in $E\setminus\{x\}$ with $x_k \to x$ and $f(x_k) \to f(x)$. Then $E \setminus F$
is countable.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Real functions; Functions of several variables), problem `ma_proofbench_l2_63`.

Stated but not proved: `MathlibExt.Analysis.Calculus.GraphNonAccumulationPointsCountableWanted.countable_diff_setOf_exists_seq_tendsto_and_tendsto_apply` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/GraphNonAccumulationPointsCountableWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/GraphNonAccumulationPointsCountableWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/index.html#countable-diff-set-of-exists-seq-tendsto).

## Steinhaus's periodization problem (Scottish Book Problem 181)

There is a continuous function
$f : \mathbb{R} \to \mathbb{R}$ with $f(x) > 0$ for every real $x$ such that, for every real $x$,
the series $\sum_{n \in \mathbb{Z}} f(x + n)$ converges and its sum is $1$.

## Sources

- H. Steinhaus, Problem 181 of the Scottish Book; the addendum Ad 181 records that the Gaussian `(1 / √π) exp (-x ^ 2)` does not have the property, while Mazur's note gives a construction, taking a positive continuous `g` with finite periodization and dividing `g` by that periodization (e.g. `g(x) = exp (-x ^ 2)`). See the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Analysis.ScottishBook181Wanted.steinhaus181_periodization_one` is written with `theorem_wanted` in [WantedExt/Analysis/ScottishBook181Wanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ScottishBook181Wanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/index.html#steinhaus181-periodization-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Continuity, regularity and functional equations](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations)
