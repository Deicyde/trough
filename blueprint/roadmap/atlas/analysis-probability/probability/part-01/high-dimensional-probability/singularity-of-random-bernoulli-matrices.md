---
declaration: section
origin: cited
lean: MathlibExt.Probability.RandomBernoulliMatricesWanted.RandomBernoulliMatrices.σ_min, MathlibExt.Probability.RandomBernoulliMatricesWanted.RandomBernoulliMatrices.rademacherMeasure, MathlibExt.Probability.RandomBernoulliMatricesWanted.RandomBernoulliMatrices.theorem_A, MathlibExt.Probability.RandomBernoulliMatricesWanted.RandomBernoulliMatrices.corollary_1, MathlibExt.Probability.RandomBernoulliMatricesWanted.RandomBernoulliMatrices.corollary_2
statement: formalized
---

# Singularity of random Bernoulli matrices

5 results, 2 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/singularity-of-random-bernoulli-matrices/index.html).

## Smallest singular value of a matrix

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and
let $M$ be a matrix over $\mathbb{K}$ whose rows and columns are indexed by finite sets $n$ and $m$.
Its smallest singular value is the real number
$\sigma_{\min}(M) = \inf_{x \in \mathbb{K}^m,\ \lVert x \rVert_2 = 1} \lVert Mx \rVert_2$, where
$\lVert \cdot \rVert_2$ is the Euclidean norm. When $m$ is empty there are no unit vectors, and
$\sigma_{\min}(M) = 0$.

Formalized by `MathlibExt.Probability.RandomBernoulliMatricesWanted.RandomBernoulliMatrices.σ_min`, a definition declared in [WantedExt/Probability/RandomBernoulliMatricesWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/RandomBernoulliMatricesWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/singularity-of-random-bernoulli-matrices/index.html#min).

## Rademacher measure on the real line

The Rademacher measure is the probability measure on
$\mathbb{R}$ that assigns mass $1/2$ to $1$ and mass $1/2$ to $-1$.

Formalized by `MathlibExt.Probability.RandomBernoulliMatricesWanted.RandomBernoulliMatrices.rademacherMeasure`, a definition declared in [WantedExt/Probability/RandomBernoulliMatricesWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/RandomBernoulliMatricesWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/singularity-of-random-bernoulli-matrices/index.html#rademacher-measure).

## Tikhomirov's Theorem A: smallest singular value of shifted Bernoulli matrices

Let
$0 < p \le 1/2$ and $\varepsilon > 0$, and write $\sigma_{\min}(A)$ for the smallest singular value
of a real square matrix $A$. There exist a natural number $N > 0$ and a real number $C > 0$ such
that for every $n \ge N$ the following holds. Let $B$ be a random $n \times n$ real matrix on a
probability space $(\Omega, P)$ whose $n^2$ entries are mutually independent and each equal to $1$
with probability $p$ and to $0$ with probability $1 - p$, and let $J$ be the $n \times n$ matrix
all of whose entries are $1$. Then for every $s \in [-1, 0]$ and every real $t > 0$,

$$P\bigl(\sigma_{\min}(B + sJ) \le t / \sqrt{n}\bigr) \le (1 - p + \varepsilon)^n + C t.$$

## Sources

- K. Tikhomirov, `Singularity of random Bernoulli matrices`, Annals of Math, 191 (2) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_random_bernoulli_matrices` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Probability.RandomBernoulliMatricesWanted.RandomBernoulliMatrices.theorem_A` is written with `theorem_wanted` in [WantedExt/Probability/RandomBernoulliMatricesWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/RandomBernoulliMatricesWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/singularity-of-random-bernoulli-matrices/index.html#theorem-a).

## Singularity probability of Bernoulli matrices

Let $0 < p \le 1/2$. For each $n$, let $B_n$ be
a random $n \times n$ real matrix on a probability space $(\Omega_n, P_n)$ whose $n^2$ entries are
mutually independent and each equal to $1$ with probability $p$ and to $0$ with probability $1 - p$.
Then there is a function $o : \mathbb{N} \to \mathbb{R}$ with $o(n) \to 0$ as $n \to \infty$ such
that $P_n(\det B_n = 0) = (1 - p + o(n))^n$ for every $n \ge 1$.

## Sources

- K. Tikhomirov, `Singularity of random Bernoulli matrices`, Annals of Math, 191 (2) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_random_bernoulli_matrices` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Probability.RandomBernoulliMatricesWanted.RandomBernoulliMatrices.corollary_1` is written with `theorem_wanted` in [WantedExt/Probability/RandomBernoulliMatricesWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/RandomBernoulliMatricesWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/singularity-of-random-bernoulli-matrices/index.html#corollary-1).

## Singularity probability of Rademacher matrices

For each $n$, let $M_n$ be a random
$n \times n$ real matrix on a probability space $(\Omega_n, P_n)$ whose $n^2$ entries are mutually
independent and each have the Rademacher law, with mass $1/2$ at each of $1$ and $-1$. Then there
is a function $o : \mathbb{N} \to \mathbb{R}$ with $o(n) \to 0$ as $n \to \infty$ such that
$P_n(\det M_n = 0) = (1/2 + o(n))^n$ for every $n \ge 1$.

## Sources

- K. Tikhomirov, `Singularity of random Bernoulli matrices`, Annals of Math, 191 (2) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_random_bernoulli_matrices` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Probability.RandomBernoulliMatricesWanted.RandomBernoulliMatrices.corollary_2` is written with `theorem_wanted` in [WantedExt/Probability/RandomBernoulliMatricesWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/RandomBernoulliMatricesWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/singularity-of-random-bernoulli-matrices/index.html#corollary-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Singularity of random Bernoulli matrices](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/singularity-of-random-bernoulli-matrices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/high-dimensional-probability/singularity-of-random-bernoulli-matrices)
