---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.MuntzSzaszWanted.muntz_szasz_nat, MathlibExt.Analysis.RungeWanted.ComplexAnalysis.runge, MetaMathlibExt.universal_approximation
statement: formalized
---

# Approximation theory: its own results

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/index.html).

Approximation and interpolation of functions: Chebyshev equioscillation, best approximation, Lagrange interpolation, Bernstein polynomials and Voronovskaya, Korovkin, Müntz–Szász, Runge, Kolmogorov superposition, universal approximation.

## Müntz–Szász theorem for integer exponents

Let $\Lambda : \mathbb{N} \to \mathbb{N}$ be
strictly increasing with $\Lambda(0) = 0$. The real linear span of the monomials
$x \mapsto x^{\Lambda(n)}$, $n \in \mathbb{N}$, restricted to $[0, 1]$, is dense in
$C([0, 1], \mathbb{R})$ with the uniform norm if and only if the series
$\sum_{n \ge 0} 1/\Lambda(n+1)$ diverges, that is, the sequence
$(1/\Lambda(n+1))_{n \in \mathbb{N}}$ is not summable.

## Sources

- C. Müntz, Festschrift H. A. Schwarz 1914 303-312 and O. Szász, Math. Ann. 77 (1916) 482-496, Müntz-Szász theorem; Rudin Real & Complex; Lean states integer-exponent `ℕ→ℕ` `StrictMono` with `0∈range` case as closure `= ⊤` iff non-summable reciprocals.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.MuntzSzaszWanted.muntz_szasz_nat`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/MuntzSzasz.lean, line 1172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/MuntzSzasz.lean#L1172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/index.html#muntz-szasz-nat).

## Runge's theorem

Let $K \subseteq \mathbb{C}$ be compact, let $U \subseteq \mathbb{C}$ be
open with $K \subseteq U$, and let $f : \mathbb{C} \to \mathbb{C}$ be analytic at every point of
$U$. Then for every real $\varepsilon > 0$ there are complex polynomials $p$ and $q$ such that
$q(z) \ne 0$ for every $z \in K$ and $|f(z) - p(z)/q(z)| < \varepsilon$ for every $z \in K$.

## Sources

- C. Runge, *Zur Theorie der eindeutigen analytischen Funktionen*, Acta Math. 6 (1885), 229-244. Listed as §64 (additional statement 3) in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `runge_theorem` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.RungeWanted.ComplexAnalysis.runge` is written with `theorem_wanted` in [WantedExt/Analysis/RungeWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RungeWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/index.html#runge).

## Universal approximation theorem

Let $n$ be a natural number, let $\mathbb{R}^n$ carry its
standard inner product $\langle \cdot, \cdot \rangle$, let $K \subseteq \mathbb{R}^n$ be compact,
and let $\sigma : \mathbb{R} \to \mathbb{R}$ be continuous and not a polynomial, that is, there is
no real polynomial $p$ with $\sigma(x) = p(x)$ for all real $x$. Then for every function
$f : \mathbb{R}^n \to \mathbb{R}$ that is continuous on $K$ and every $\varepsilon > 0$ there exist
$m \in \mathbb{N}$, real numbers $c_1, \dots, c_m$ and $b_1, \dots, b_m$, and vectors
$w_1, \dots, w_m \in \mathbb{R}^n$ such that
$\left| f(x) - \sum_{i=1}^{m} c_i \, \sigma(\langle w_i, x \rangle + b_i) \right| < \varepsilon$
for every $x \in K$.

In words: single-hidden-layer feedforward networks with a continuous, non-polynomial activation
approximate every continuous function uniformly on every compact set.

## Sources

- `universal-approximation-s1` from https://en.wikipedia.org/wiki/Universal_approximation_theorem; the continuous-activation case of M. Leshno, V. Ya. Lin, A. Pinkus and S. Schocken, *Multilayer feedforward networks with a nonpolynomial activation function can approximate any function*, Neural Networks 6(6) (1993), 861–867, doi:10.1016/S0893-6080(05)80131-5, which allows any locally bounded, piecewise continuous activation that is not almost everywhere equal to a polynomial; for continuous activations this is the same as the pointwise non-polynomial hypothesis.

Formalized by `MetaMathlibExt.universal_approximation`, a theorem declared in [MathlibExt/Analysis/Approximation/UniversalApproximation.lean, line 1067](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Approximation/UniversalApproximation.lean#L1067). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/index.html#universal-approximation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Approximation theory](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/approximation-theory)
