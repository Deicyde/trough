---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.rademacherSign, MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.rademacherSign_eq_one_of, MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.rademacherSign_eq_neg_one_of, MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.norm_rademacherSign, MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.card_sign_vectors, MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.sum_rademacher_sq_norm_eq, MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.average_rademacher_sq_norm_eq, MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.rademacher_type_two
statement: formalized
---

# Rademacher type and cotype

21 results, 20 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html).

## Rademacher sign of a coordinate

The Rademacher sign attached to a coordinate: `1` for `true`, `-1`
for `false`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.rademacherSign`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#rademacher-sign).

## Rademacher sign on a true coordinate is one

The sign is `1` on a `true` coordinate.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.rademacherSign_eq_one_of`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#rademacher-sign-eq-one-of).

## Rademacher sign on a false coordinate is minus one

The sign is `-1` on a `false` coordinate.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.rademacherSign_eq_neg_one_of`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#rademacher-sign-eq-neg-one-of).

## Rademacher signs have norm one

Every Rademacher sign has norm `1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.norm_rademacherSign`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#norm-rademacher-sign).

## Number of sign vectors of length n

Number of sign vectors: `Fin n → Bool` has `2 ^ n` elements.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.card_sign_vectors`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#card-sign-vectors).

## Second moment of a Rademacher sum in a Hilbert space

Exact second moment of a Rademacher sum in a Hilbert space:
the sum over all sign vectors of `‖∑ᵢ εᵢ • xᵢ‖²` equals
`2 ^ n * ∑ᵢ ‖xᵢ‖²`. Cross terms cancel: the induction step pairs the
two values of the last sign and applies the parallelogram law.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.sum_rademacher_sq_norm_eq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#sum-rademacher-sq-norm-eq).

## Average squared norm of a Rademacher sum

The average (uniform over sign vectors) of `‖∑ᵢ εᵢ • xᵢ‖²` is exactly
`∑ᵢ ‖xᵢ‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.average_rademacher_sq_norm_eq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#average-rademacher-sq-norm-eq).

## Hilbert spaces have Rademacher type 2

Rademacher type 2 with constant `1`: the average of the squared
Rademacher sums is at most `∑ᵢ ‖xᵢ‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.rademacher_type_two`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#rademacher-type-two).

## Hilbert spaces have Rademacher cotype 2

Rademacher cotype 2 with constant `1`: `∑ᵢ ‖xᵢ‖²` is at most the
average of the squared Rademacher sums.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.rademacher_cotype_two`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#rademacher-cotype-two).

## Square-root form of the Rademacher second moment

Square-root form of the exact second moment.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.sqrt_average_rademacher_sq_norm_eq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#sqrt-average-rademacher-sq-norm-eq).

## Bound on the average Rademacher norm

The average Rademacher norm is at most `(∑ᵢ ‖xᵢ‖²)^{1/2}`
(Cauchy–Schwarz for the finite average, plus the exact second moment).

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.average_rademacher_norm_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#average-rademacher-norm-le).

## Average squared Rademacher sum of unit vectors

For unit vectors, the average squared Rademacher sum equals `n`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.average_rademacher_sq_norm_eq_of_norm_eq_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#average-rademacher-sq-norm-eq-of-norm-eq).

## Second moment of a real Rademacher sum

Scalar real form: the second moment of `∑ᵢ ±aᵢ` over all sign choices
is `2 ^ n * ∑ᵢ aᵢ²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RademacherTypeCotype.sum_rademacher_sq_real`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RademacherTypeCotype.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#sum-rademacher-sq-real).

## Rademacher distribution

The Rademacher distribution is the measure on $\{-1, 1\}$,
viewed as a subset of $\mathbb{Z}$, that gives mass $1/2$ to each of $1$ and $-1$.

Formalized by `MathlibExt.Analysis.RademacherEnfloTypeWanted.RademacherEnfloType.rademacherDistribution`, a definition declared in [WantedExt/Analysis/RademacherEnfloTypeWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RademacherEnfloTypeWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#rademacher-distribution).

## Product Rademacher distribution

For an index type $\iota$, this is the product over
$\iota$ of copies of the Rademacher distribution: the joint law of a family
$(\varepsilon_i)_{i \in \iota}$ of independent Rademacher random variables, as a measure on the
functions $\iota \to \{-1, 1\}$.

Formalized by `MathlibExt.Analysis.RademacherEnfloTypeWanted.RademacherEnfloType.rademacherProductDistribution`, a definition declared in [WantedExt/Analysis/RademacherEnfloTypeWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RademacherEnfloTypeWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#rademacher-product-distribution).

## Discrete partial derivative on the Rademacher cube

Let $X$ be a real Banach space, $n$ a
natural number and $f : \{-1, 1\}^n \to X$. For $j \in \{1, \dots, n\}$ and
$\varepsilon = (\varepsilon_1, \dots, \varepsilon_n) \in \{-1, 1\}^n$, the discrete partial
derivative of $f$ in direction $j$ at $\varepsilon$ is

$$
D_j f(\varepsilon) = \frac{1}{2}\bigl(f(\varepsilon) -
f(\varepsilon_1, \dots, -\varepsilon_j, \dots, \varepsilon_n)\bigr),
$$

where only the $j$-th coordinate of $\varepsilon$ is negated in the second term.

Formalized by `MathlibExt.Analysis.RademacherEnfloTypeWanted.RademacherEnfloType.D`, a definition declared in [WantedExt/Analysis/RademacherEnfloTypeWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RademacherEnfloTypeWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#d).

## Rademacher type

Let $X$ be a real Banach space, $C \in [0, \infty]$ and $p$ a real
number. We say that $X$ has Rademacher type $p$ with constant $C$ if for every $n \ge 1$ and all
$x_1, \dots, x_n \in X$,

$$
\mathbb{E}\Bigl\|\sum_{j=1}^n \varepsilon_j x_j\Bigr\|^p \le C^p \sum_{j=1}^n \|x_j\|^p,
$$

where $\varepsilon_1, \dots, \varepsilon_n$ are independent Rademacher random variables. Both
sides are computed in $[0, \infty]$.

Formalized by `MathlibExt.Analysis.RademacherEnfloTypeWanted.RademacherEnfloType.IsRademacherType`, a definition declared in [WantedExt/Analysis/RademacherEnfloTypeWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RademacherEnfloTypeWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#is-rademacher-type).

## Rademacher type constant

For a real Banach space $X$ and a real number $p$,
$T^R_p(X)$ is the infimum in $[0, \infty]$ of all $C \in [0, \infty]$ such that $X$ has
Rademacher type $p$ with constant $C$.

Formalized by `MathlibExt.Analysis.RademacherEnfloTypeWanted.RademacherEnfloType.TR`, a definition declared in [WantedExt/Analysis/RademacherEnfloTypeWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RademacherEnfloTypeWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#tr).

## Enflo type

Let $X$ be a real Banach space, $C \in [0, \infty]$ and $p$ a real number. We
say that $X$ has Enflo type $p$ with constant $C$ if for every $n \ge 1$ and every function
$f : \{-1, 1\}^n \to X$,

$$
\mathbb{E}\Bigl\|\frac{f(\varepsilon) - f(-\varepsilon)}{2}\Bigr\|^p \le
C^p \sum_{j=1}^n \mathbb{E}\,\|D_j f(\varepsilon)\|^p,
$$

where $\varepsilon = (\varepsilon_1, \dots, \varepsilon_n)$ is a sequence of independent
Rademacher random variables, $-\varepsilon = (-\varepsilon_1, \dots, -\varepsilon_n)$, and
$D_j f$ is the discrete partial derivative of $f$ in direction $j$. Both sides are computed in
$[0, \infty]$.

Formalized by `MathlibExt.Analysis.RademacherEnfloTypeWanted.RademacherEnfloType.IsEnfloType`, a definition declared in [WantedExt/Analysis/RademacherEnfloTypeWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RademacherEnfloTypeWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#is-enflo-type).

## Enflo type constant

For a real Banach space $X$ and a real number $p$, $T^E_p(X)$ is
the infimum in $[0, \infty]$ of all $C \in [0, \infty]$ such that $X$ has Enflo type $p$ with
constant $C$.

Formalized by `MathlibExt.Analysis.RademacherEnfloTypeWanted.RademacherEnfloType.TE`, a definition declared in [WantedExt/Analysis/RademacherEnfloTypeWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RademacherEnfloTypeWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#te).

## Comparison of Rademacher and Enflo type constants

For every real Banach space $X$ and every
real number $p$ with $1 \le p \le 2$, the Rademacher type constant and the Enflo type constant
of $X$ satisfy $T^R_p(X) \le T^E_p(X) \le \frac{\pi}{\sqrt{2}}\, T^R_p(X)$.

## Sources

- P. Ivanisvili, R. van Handel, and A. Volberg, `Rademacher type and Enflo type coincide`, Annals of Math, 192 (2) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_rademacher_enflo_type` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.RademacherEnfloTypeWanted.RademacherEnfloType.theorem_1_1` is written with `theorem_wanted` in [WantedExt/Analysis/RademacherEnfloTypeWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RademacherEnfloTypeWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rademacher type and cotype](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/rademacher-type-and-cotype)
