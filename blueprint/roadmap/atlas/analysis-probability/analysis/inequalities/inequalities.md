---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.ReciprocalDifferenceSqrtBoundWanted.one_div_one_add_sub_one_div_one_add_mul_le, MetaMathlibExt.hardy_inequality, MetaMathlibExt.hermite_hadamard, MathlibExt.Analysis.SquareSummableComplexInequalityWanted.conjecture_holds, MathlibExt.Analysis.Calculus.OpialTypeIntegralInequalityWanted.integral_abs_mul_deriv_le_of_eq_zero_left, MetaMathlibExt.wirtinger_inequality
statement: formalized
---

# Inequalities: its own results

6 results, 3 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/index.html).

Classical inequalities for sums, sequences, means and integrals of real or complex numbers: Hardy, Hilbert, Carleman, Wirtinger, Opial, Landau–Kolmogorov, Hermite–Hadamard, Kantorovich and Popoviciu, power-sum and elementary log/exp bounds; inequalities stated with Sobolev norms go to Function spaces, eigenvalue inequalities to Operator theory.

## A bound on a difference of reciprocals

For all real numbers $a > 1$ and $x \ge 1$,

$$
\frac{1}{1+x}-\frac{1}{1+ax}\le \frac{\sqrt{a}-1}{\sqrt{a}+1}.
$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Inequalities in real analysis), problem `ma_proofbench_l1_01`.

Stated but not proved: `MathlibExt.Analysis.Calculus.ReciprocalDifferenceSqrtBoundWanted.one_div_one_add_sub_one_div_one_add_mul_le` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/ReciprocalDifferenceSqrtBoundWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/ReciprocalDifferenceSqrtBoundWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/index.html#one-div-one-add-sub-one-div-one-add-mul).

## Hardy's inequality

Let $p > 1$ be a real number and let $(a_n)_{n \ge 0}$ be a sequence
of nonnegative real numbers such that $\sum_n a_n^p$ converges. Write
$A_n = \frac{1}{n+1} \sum_{i=0}^{n} a_i$ for the average of $a_0, \dots, a_n$. Then
$\sum_n A_n^p$ converges and

$$\sum_{n=0}^{\infty} A_n^p \le \left(\frac{p}{p-1}\right)^p \sum_{n=0}^{\infty} a_n^p.$$

Proof: Elliott's finite telescoping argument is combined with Young's and Hölder's inequalities,
following E. B. Elliott (1926) as presented in Hardy--Littlewood--Pólya, *Inequalities*,
Theorem 326.

## Sources

- G. H. Hardy, *Note on a theorem of Hilbert*, Mathematische Zeitschrift 6 (1920), 314-317: the discrete series form with constant `(p / (p - 1)) ^ p` for `p > 1`.

Formalized by `MetaMathlibExt.hardy_inequality`, a theorem declared in [MathlibExt/Analysis/Series/HardyInequality.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Series/HardyInequality.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/index.html#hardy-inequality).

## Hermite–Hadamard inequality

Let $a < b$ be real numbers and let
$f \colon \mathbb{R} \to \mathbb{R}$ be convex on $[a, b]$. Then
$f\left(\frac{a+b}{2}\right) \le \frac{1}{b-a} \int_a^b f(x)\,dx$ and
$\frac{1}{b-a} \int_a^b f(x)\,dx \le \frac{f(a) + f(b)}{2}$.

## Sources

- <https://en.wikipedia.org/wiki/Hermite%E2%80%93Hadamard_inequality>.

Formalized by `MetaMathlibExt.hermite_hadamard`, a theorem declared in [MathlibExt/Analysis/Convex/HermiteHadamard.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/HermiteHadamard.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/index.html#hermite-hadamard).

## Inequality for square-summable complex sequences

Let $(\alpha_n)_{n \ge 1}$ be complex
numbers with $\sum_{n \ge 1} |\alpha_n|^2 < \infty$, and for $k \ge 0$ put
$\beta_k = \sum_{l \ge 0} \alpha_{2^k(2l+1)} / (l+1)$. Then each series defining $\beta_k$
converges absolutely, $\sum_{k \ge 0} |\beta_k|^2 < \infty$, and

$$\sum_{n \ge 1} |\alpha_n|^2 \ge \frac{6}{\pi^2} \sum_{k \ge 0} |\beta_k|^2.$$

The inequality follows from the Cauchy–Schwarz inequality.

## Sources

- Open Problem Garden solution comment 73221, https://www.openproblemgarden.org/op/inequality_for_square_summable_complex_series#comment-73221.

Stated but not proved: `MathlibExt.Analysis.SquareSummableComplexInequalityWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/SquareSummableComplexInequalityWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SquareSummableComplexInequalityWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/index.html#conjecture-holds).

## Opial's inequality with one boundary condition

Let $\alpha \le \beta$ be real numbers and
let $f : \mathbb{R} \to \mathbb{R}$ be continuously differentiable on $[\alpha, \beta]$ with
$f(\alpha) = 0$. Then

$$\int_\alpha^\beta |f(x) f'(x)|\,dx \le \frac{\beta - \alpha}{2} \int_\alpha^\beta |f'(x)|^2\,dx.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Inequalities in real analysis), problem `ma_proofbench_l1_76`.

Stated but not proved: `MathlibExt.Analysis.Calculus.OpialTypeIntegralInequalityWanted.integral_abs_mul_deriv_le_of_eq_zero_left` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/OpialTypeIntegralInequalityWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/OpialTypeIntegralInequalityWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/index.html#integral-abs-mul-deriv-le-of-eq-zero-lef).

## Wirtinger's inequality

Let $f, f' : \mathbb{R} \to \mathbb{R}$ be functions such that
for every $x \in [0, \pi]$ the function $f$ has derivative $f'(x)$ at $x$ within $[0, \pi]$, $f'$
is continuous on $[0, \pi]$, and $f(0) = f(\pi) = 0$. Then
$\int_0^\pi f(x)^2 \, dx \le \int_0^\pi f'(x)^2 \, dx$.

Proof: A Picone-type comparison. For `0 < c < 1` the weight `h x = -c * tan (c * (x - π / 2))` is
smooth on `[0, π]` with `h' + h ^ 2 = -c ^ 2`, so integrating
`f' ^ 2 = (f' - h * f) ^ 2 + (h * f ^ 2)' + c ^ 2 * f ^ 2` gives `c ^ 2 * ∫ f ^ 2 ≤ ∫ f' ^ 2`;
then let `c` tend to one.

## Sources

- G. H. Hardy, J. E. Littlewood, and G. Pólya, *Inequalities*, second edition, Cambridge University Press, 1952, §7.7 (the endpoint-zero form on `[0, L]`).

Formalized by `MetaMathlibExt.wirtinger_inequality`, a theorem declared in [MathlibExt/Analysis/Calculus/Wirtinger.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/Wirtinger.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/index.html#wirtinger-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inequalities](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/inequalities)
