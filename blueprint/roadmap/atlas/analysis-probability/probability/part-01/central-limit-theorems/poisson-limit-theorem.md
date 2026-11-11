---
declaration: section
origin: cited
lean: ProbabilityTheory.elem_symm_poly_tendsto_poisson, MathlibExt.Probability.PoissonWeakConvergence.binomialProbMeasure, MathlibExt.Probability.PoissonWeakConvergence.poissonProbMeasure, MathlibExt.Probability.PoissonWeakConvergence.poissonApproxProb, MathlibExt.Probability.PoissonWeakConvergence.binomialPoissonApprox, MathlibExt.Probability.PoissonWeakConvergence.charFun_binomialProbMeasure, MathlibExt.Probability.PoissonWeakConvergence.charFun_poissonProbMeasure, MathlibExt.Probability.PoissonWeakConvergence.tendsto_mul_poissonApproxProb
statement: formalized
proof: formalized
---

# Poisson limit theorem

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/poisson-limit-theorem/index.html).

## Analytic core of Poisson convergence

Let $\lambda \ge 0$ be a real number, let
$k : \mathbb{N} \to \mathbb{N}$, and for each $n$ let $p_{n,i}$, $0 \le i < k(n)$, be real
numbers. Suppose that $p_{n,i} \ge 0$ for all $n$ and $i$, that for every $\varepsilon > 0$
we have $p_{n,i} < \varepsilon$ for all $i < k(n)$ once $n$ is large enough, and that
$\sum_{i < k(n)} p_{n,i} \to \lambda$ as $n \to \infty$. Then for every natural number $j$,
as $n \to \infty$ the Poisson-binomial mass

$$\sum_{|A| = j} \prod_{i \in A} p_{n,i} \prod_{i \notin A} (1 - p_{n,i})$$

tends to $e^{-\lambda} \lambda^j / j!$, where $A$ runs over the $j$-element subsets of
$\{0, \dots, k(n) - 1\}$ and $i \notin A$ ranges over the elements of that set not in $A$.

Without the hypothesis $p_{n,i} \ge 0$ the conclusion can fail.

Formalized by `ProbabilityTheory.elem_symm_poly_tendsto_poisson`, a theorem declared in [MathlibExt/Probability/PoissonConvergenceCore.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/PoissonConvergenceCore.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/poisson-limit-theorem/index.html#elem-symm-poly-tendsto-poisson).

## Binomial law as a probability measure

The binomial law `Bin(n, p)` on `ℝ`, bundled as a probability measure.

Formalized by `MathlibExt.Probability.PoissonWeakConvergence.binomialProbMeasure`, a definition declared in [MathlibExt/Probability/PoissonWeakConvergence.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/PoissonWeakConvergence.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/poisson-limit-theorem/index.html#binomial-prob-measure).

## Poisson law as a probability measure

The Poisson law of rate `λ` on `ℝ`, bundled as a probability measure.

Formalized by `MathlibExt.Probability.PoissonWeakConvergence.poissonProbMeasure`, a definition declared in [MathlibExt/Probability/PoissonWeakConvergence.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/PoissonWeakConvergence.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/poisson-limit-theorem/index.html#poisson-prob-measure).

## Success probability of the binomial approximation to Poisson

The success probability `λ / (n + λ)` used in the binomial approximation to
the Poisson law. It lies in `[0, 1]` for every `n`, and `n * pₙ → λ`.

Formalized by `MathlibExt.Probability.PoissonWeakConvergence.poissonApproxProb`, a definition declared in [MathlibExt/Probability/PoissonWeakConvergence.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/PoissonWeakConvergence.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/poisson-limit-theorem/index.html#poisson-approx-prob).

## Binomial approximation to the Poisson law

The binomial law `Bin(n, λ / (n + λ))` on `ℝ`.

Formalized by `MathlibExt.Probability.PoissonWeakConvergence.binomialPoissonApprox`, a definition declared in [MathlibExt/Probability/PoissonWeakConvergence.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/PoissonWeakConvergence.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/poisson-limit-theorem/index.html#binomial-poisson-approx).

## Characteristic function of a binomial law

`φ_{Bin(n, p)}(t) = ((1 - p) + p * e^{it})ⁿ`.

Formalized by `MathlibExt.Probability.PoissonWeakConvergence.charFun_binomialProbMeasure`, a theorem declared in [MathlibExt/Probability/PoissonWeakConvergence.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/PoissonWeakConvergence.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/poisson-limit-theorem/index.html#char-fun-binomial-prob-measure).

## Characteristic function of a Poisson law

`φ_{Poisson(λ)}(t) = exp(λ * (e^{it} - 1))`.

Formalized by `MathlibExt.Probability.PoissonWeakConvergence.charFun_poissonProbMeasure`, a theorem declared in [MathlibExt/Probability/PoissonWeakConvergence.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/PoissonWeakConvergence.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/poisson-limit-theorem/index.html#char-fun-poisson-prob-measure).

## Mean of the binomial approximation tends to the Poisson rate

The expected number of successes tends to the rate: `n * (λ / (n + λ)) → λ`.

Formalized by `MathlibExt.Probability.PoissonWeakConvergence.tendsto_mul_poissonApproxProb`, a theorem declared in [MathlibExt/Probability/PoissonWeakConvergence.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/PoissonWeakConvergence.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/poisson-limit-theorem/index.html#tendsto-mul-poisson-approx-prob).

## Convergence of characteristic functions to the Poisson law

The characteristic functions of the approximating binomial laws converge
pointwise to the characteristic function of the Poisson law.

Formalized by `MathlibExt.Probability.PoissonWeakConvergence.tendsto_charFun_binomialPoissonApprox`, a theorem declared in [MathlibExt/Probability/PoissonWeakConvergence.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/PoissonWeakConvergence.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/poisson-limit-theorem/index.html#tendsto-char-fun-binomial-poisson-approx).

## Poisson convergence in law (binomial approximation)

The binomial laws
`Bin(n, λ / (n + λ))` converge weakly to the Poisson law of rate `λ`.

Formalized by `MathlibExt.Probability.PoissonWeakConvergence.tendsto_binomialPoissonApprox`, a theorem declared in [MathlibExt/Probability/PoissonWeakConvergence.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/PoissonWeakConvergence.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/poisson-limit-theorem/index.html#tendsto-binomial-poisson-approx).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poisson limit theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/poisson-limit-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/central-limit-theorems/poisson-limit-theorem)
