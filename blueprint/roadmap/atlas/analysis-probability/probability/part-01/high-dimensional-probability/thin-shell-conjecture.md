---
declaration: section
origin: cited
lean: MathlibExt.Probability.ThinShell.IsLogConcaveDensity, MathlibExt.Probability.ThinShell.IsIsotropicLogConcave, MathlibExt.Probability.ThinShell.normalizedRadiusVariance, MathlibExt.Probability.ThinShell.thinShellVarianceConstant, MathlibExt.Probability.ThinShell.thinShellWidth, MathlibExt.Probability.ThinShell.radius_deviation_sq_le, MathlibExt.Probability.ThinShell.radius_fluctuation_le_normalized_variance, MathlibExt.Probability.ThinShell.normalizedRadiusVariance_le_constant
statement: formalized
---

# Thin-shell conjecture

30 results, 13 proved and 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html).

## Log-concave densities

A function $f : \mathbb{R}^n \to \mathbb{R}$ is a log-concave
density when it is measurable, $f(x) \ge 0$ for every $x$, and
$f(x)^{1-t} f(y)^t \le f((1-t)x + ty)$ for all $x, y \in \mathbb{R}^n$ and every real $t$
with $0 < t < 1$.

No integrability or normalization of $f$ is required.

Formalized by `MathlibExt.Probability.ThinShell.IsLogConcaveDensity`, a definition declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#is-log-concave-density).

## Isotropic log-concave probability measures

A measure $\mu$ on $\mathbb{R}^n$ is
isotropic log-concave when it is a probability measure, it has density $f$ with respect to
Lebesgue measure for some log-concave density $f$, and for all coordinates $i, j$ the
functions $x \mapsto x_i$ and $x \mapsto x_i x_j$ are $\mu$-integrable with
$\int x_i \, d\mu(x) = 0$ and $\int x_i x_j \, d\mu(x) = \delta_{ij}$, that is, $1$ if $i = j$
and $0$ otherwise.

Formalized by `MathlibExt.Probability.ThinShell.IsIsotropicLogConcave`, a definition declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#is-isotropic-log-concave).

## Normalized radius variance

For a measure $\mu$ on $\mathbb{R}^n$, the normalized radius
variance of $\mu$ is $\frac{1}{n} \int (\|x\|^2 - n)^2 \, d\mu(x)$, computed in $[0, \infty]$,
where $\|x\|$ is the Euclidean norm (for $n = 0$ the integral is $0$ and so is the value).

When $\mu$ is a probability measure with $\int \|x\|^2 \, d\mu(x) = n$, as for an isotropic
one, this is the variance of $\|x\|^2$ divided by $n$.

Formalized by `MathlibExt.Probability.ThinShell.normalizedRadiusVariance`, a definition declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#normalized-radius-variance).

## Thin-shell variance constant

Write $|x|$ for the Euclidean norm. The thin-shell
variance constant is the supremum, taken in $[0, \infty]$, of the normalized radius variance
$\frac{1}{n} \int (|x|^2 - n)^2 \, d\mu(x)$ over all dimensions $n \ge 1$ and all isotropic
log-concave probability measures $\mu$ on $\mathbb{R}^n$.

Formalized by `MathlibExt.Probability.ThinShell.thinShellVarianceConstant`, a definition declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#thin-shell-variance-constant).

## Thin-shell width

Write $|x|$ for the Euclidean norm. For $n \in \mathbb{N}$, the
thin-shell width in dimension $n$ is the square root of the supremum, taken in $[0, \infty]$, of
$\int (|x| - \sqrt{n})^2 \, d\mu(x)$ over all isotropic log-concave probability measures $\mu$ on
$\mathbb{R}^n$, with $\sqrt{\infty} = \infty$.

Formalized by `MathlibExt.Probability.ThinShell.thinShellWidth`, a definition declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#thin-shell-width).

## Elementary radius deviation bound

For all real numbers $r \ge 0$ and $d > 0$,
$(r - \sqrt{d})^2 \le (r^2 - d)^2 / d$.

Formalized by `MathlibExt.Probability.ThinShell.radius_deviation_sq_le`, a theorem declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#radius-deviation-sq-le).

## Radius fluctuation is bounded by the normalized radius variance

For every $n > 0$ and
every measure $\mu$ on $\mathbb{R}^n$, the integral $\int (\|x\| - \sqrt{n})^2 \, d\mu(x)$,
taken in $[0, \infty]$ with $\|x\|$ the Euclidean norm, is at most the normalized radius
variance of $\mu$.

The bound holds even when the moments are infinite.

Formalized by `MathlibExt.Probability.ThinShell.radius_fluctuation_le_normalized_variance`, a theorem declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#radius-fluctuation-le-normalized-varianc).

## The thin-shell variance constant bounds the normalized radius variance of isotropic log-concave measures

**The thin-shell variance constant bounds the normalized radius variance of isotropic
log-concave measures.** For every $n > 0$ and every isotropic log-concave probability measure
$\mu$ on $\mathbb{R}^n$, the normalized radius variance of $\mu$ is at most the thin-shell
variance constant.

Formalized by `MathlibExt.Probability.ThinShell.normalizedRadiusVariance_le_constant`, a theorem declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#normalized-radius-variance-le-constant).

## Characterization of bounds on the thin-shell variance constant

For every
$C \in [0, \infty]$, the thin-shell variance constant is at most $C$ if and only if, for every
$n > 0$ and every isotropic log-concave probability measure $\mu$ on $\mathbb{R}^n$, the
normalized radius variance of $\mu$ is at most $C$.

Formalized by `MathlibExt.Probability.ThinShell.thinShellVarianceConstant_le_iff`, a theorem declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#thin-shell-variance-constant-le-iff).

## The thin-shell variance constant bounds the radius fluctuation

For every $n > 0$ and
every isotropic log-concave probability measure $\mu$ on $\mathbb{R}^n$, the integral
$\int (\|x\| - \sqrt{n})^2 \, d\mu(x)$, taken in $[0, \infty]$ with $\|x\|$ the Euclidean
norm, is at most the thin-shell variance constant.

Formalized by `MathlibExt.Probability.ThinShell.radius_fluctuation_le_constant`, a theorem declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#radius-fluctuation-le-constant).

## The thin-shell variance constant is nonnegative

The thin-shell variance constant, a
value in $[0, \infty]$, is at least $0$.

Formalized by `MathlibExt.Probability.ThinShell.thinShellVarianceConstant_nonneg`, a theorem declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#thin-shell-variance-constant-nonneg).

## Thin-shell width is at most the square root of the variance constant

For every
dimension $n \ge 1$, the thin-shell width in dimension $n$ is at most the square root of the
thin-shell variance constant, computed in $[0, \infty]$ with $\sqrt{\infty} = \infty$.

Formalized by `MathlibExt.Probability.ThinShell.thinShellWidth_le_sqrt_constant`, a theorem declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#thin-shell-width-le-sqrt-constant).

## A uniform variance bound makes the thin-shell variance constant finite

If $C$ is a real
number such that for every $n > 0$ and every isotropic log-concave probability measure $\mu$
on $\mathbb{R}^n$ the normalized radius variance of $\mu$ is at most $\max(C, 0)$, then the
thin-shell variance constant is finite.

Formalized by `MathlibExt.Probability.ThinShell.thinShellVarianceConstant_lt_top_of_bound`, a theorem declared in [MathlibExt/Probability/Geometry/ThinShell.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/ThinShell.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#thin-shell-variance-constant-lt-top-of-b).

## Klartag's first thin-shell bound

There are a real $C > 0$ and a natural number
$N \ge 3$ such that for every natural number $n \ge N$ the thin-shell width
$\sigma_n \in [0, \infty]$ of dimension $n$ satisfies $\sigma_n \le C \sqrt{n / \log n}$.

This is Klartag's first bound in the weaker form tabulated by the optimization catalogue.

## Sources

- Klartag, Invent. Math. 168 (2007), 91--131; catalogue `constants/20a.md`.

Stated but not proved: `MathlibExt.Probability.ThinShell.klartag2007a_width_bound` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#klartag2007a-width-bound).

## Klartag's power-law thin-shell bound

For every $\varepsilon > 0$ there are a constant
$C > 0$ and an integer $N \ge 3$ such that for every dimension $n \ge N$ the thin-shell width
$\sigma_n \in [0, \infty]$ satisfies $\sigma_n \le C n^{2/5 + \varepsilon}$. Here $\sigma_n$ is
the square root of the supremum of $\mathbb{E}\,(|X| - \sqrt{n})^2$ over isotropic log-concave
random vectors $X$ in $\mathbb{R}^n$.

## Sources

- Klartag, J. Funct. Anal. 245 (2007), 284--310; catalogue `constants/20a.md`.

Stated but not proved: `MathlibExt.Probability.ThinShell.klartag2007b_width_bound` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#klartag2007b-width-bound).

## Fleury's thin-shell bound

There are a real $C > 0$ and a natural number $N \ge 3$ such
that for every natural number $n \ge N$ the thin-shell width $\sigma_n \in [0, \infty]$ of
dimension $n$ satisfies $\sigma_n \le C n^{3/8}$.

## Sources

- Fleury, J. Funct. Anal. 259 (2010), 832--841; catalogue `constants/20a.md`.

Stated but not proved: `MathlibExt.Probability.ThinShell.fleury2010_width_bound` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#fleury2010-width-bound).

## Guédon–Milman thin-shell bound

There are a real $C > 0$ and a natural number $N \ge 3$
such that for every natural number $n \ge N$ the thin-shell width $\sigma_n \in [0, \infty]$ of
dimension $n$ satisfies $\sigma_n \le C n^{1/3}$.

## Sources

- Guedon and Milman, GAFA 21 (2011), 1043--1068; catalogue `constants/20a.md`.

Stated but not proved: `MathlibExt.Probability.ThinShell.guedonMilman2011_width_bound` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#guedon-milman2011-width-bound).

## Lee–Vempala thin-shell bound

There are a constant $C > 0$ and an integer $N \ge 3$
such that for every dimension $n \ge N$ the thin-shell width $\sigma_n \in [0, \infty]$ satisfies
$\sigma_n \le C n^{1/4}$. Here $\sigma_n$ is the square root of the supremum of
$\mathbb{E}\,(|X| - \sqrt{n})^2$ over isotropic log-concave random vectors $X$ in $\mathbb{R}^n$.

## Sources

- Lee and Vempala, FOCS 2017, 998--1007; catalogue `constants/20a.md`.

Stated but not proved: `MathlibExt.Probability.ThinShell.leeVempala2017_width_bound` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#lee-vempala2017-width-bound).

## Chen's thin-shell bound

For every real $\varepsilon > 0$ there is a natural number
$N \ge 3$ such that for every natural number $n \ge N$ the thin-shell width
$\sigma_n \in [0, \infty]$ of dimension $n$ satisfies
$\sigma_n \le \exp\big((\log n)^{1/2 + \varepsilon}\big)$.

There is no constant multiplier inside the exponential.

## Sources

- Chen, GAFA 31 (2021), 34--61; catalogue `constants/20a.md`.

Stated but not proved: `MathlibExt.Probability.ThinShell.chen2021_width_bound` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#chen2021-width-bound).

## Klartag–Lehec polylogarithmic thin-shell bound

There are a real $C > 0$ and a natural
number $N \ge 3$ such that for every natural number $n \ge N$ the thin-shell width
$\sigma_n \in [0, \infty]$ of dimension $n$ satisfies $\sigma_n \le C (\log n)^4$.

## Sources

- Klartag and Lehec, GAFA 32 (2022), 1134--1159; catalogue `constants/20a.md`.

Stated but not proved: `MathlibExt.Probability.ThinShell.klartagLehec2022_width_bound` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#klartag-lehec2022-width-bound).

## Jambulapati–Lee–Vempala thin-shell bound

Let
$\alpha = \big(1 + 7\sqrt{2} + \sqrt{53 - 4\sqrt{2}}\big)/8$. There are a real $C > 0$ and a
natural number $N \ge 3$ such that for every natural number $n \ge N$ the thin-shell width
$\sigma_n \in [0, \infty]$ of dimension $n$ satisfies $\sigma_n \le C (\log n)^{\alpha}$.

The exponent $\alpha$ is algebraic, not rational; the paper bounds it by $2.2226$. The paper
proves this bound for the square root of the normalized variance of the squared radius, which
bounds the thin-shell width from above.

## Sources

- Jambulapati, Lee and Vempala, arXiv:2208.11644v1, Theorem 22.

Stated but not proved: `MathlibExt.Probability.ThinShell.jambulapatiLeeVempala2022_width_bound` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#jambulapati-lee-vempala2022-width-bound).

## Klartag's square-root-logarithmic thin-shell bound

There are a constant $C > 0$ and an
integer $N \ge 3$ such that for every dimension $n \ge N$ the thin-shell width
$\sigma_n \in [0, \infty]$ satisfies $\sigma_n \le C \sqrt{\log n}$. Here $\sigma_n$ is the square
root of the supremum of $\mathbb{E}\,(|X| - \sqrt{n})^2$ over isotropic log-concave random
vectors $X$ in $\mathbb{R}^n$, and $\log$ is the natural logarithm.

## Sources

- Klartag, Ars Inveniendi Analytica (2023), Paper 4; catalogue `constants/20a.md`.

Stated but not proved: `MathlibExt.Probability.ThinShell.klartag2023_width_bound` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#klartag2023-width-bound).

## Guan's thin-shell bound

There are a real $C > 0$ and a natural number $N \ge 3$ such
that for every natural number $n \ge N$ the thin-shell width $\sigma_n \in [0, \infty]$ of
dimension $n$ satisfies $\sigma_n \le C \log \log n$.

## Sources

- Guan, arXiv:2412.09075; catalogue `constants/20a.md`.

Stated but not proved: `MathlibExt.Probability.ThinShell.guan2024_width_bound` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#guan2024-width-bound).

## Klartag–Lehec thin-shell variance bound

There is a real $C > 0$ such that for every
natural number $n \ge 1$ and every isotropic log-concave measure $\mu$ on $\mathbb{R}^n$, the
normalized radius variance $\frac{1}{n} \int (|x|^2 - n)^2 \, d\mu(x)$ is at most $C$.

## Sources

- arXiv:2507.15495v1, Theorem 1.1. The constant is not optimized or made explicit.

Stated but not proved: `MathlibExt.Probability.ThinShell.klartagLehec2025_variance_bound` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#klartag-lehec2025-variance-bound).

## Klartag–Lehec bounded thin-shell width

There is a real $C > 0$ such that for every
natural number $n \ge 1$ the thin-shell width $\sigma_n \in [0, \infty]$ of dimension $n$
satisfies $\sigma_n \le C$.

## Sources

- Klartag and Lehec, arXiv:2507.15495v1, Introduction and Theorem 1.1.

Stated but not proved: `MathlibExt.Probability.ThinShell.klartagLehec2025_width_bound` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#klartag-lehec2025-width-bound).

## The thin-shell variance constant is finite

The thin-shell variance constant, the
supremum in $[0, \infty]$ of the normalized radius variances
$\frac{1}{n} \int (|x|^2 - n)^2 \, d\mu(x)$ over all dimensions $n \ge 1$ and all isotropic
log-concave probability measures $\mu$ on $\mathbb{R}^n$, is finite.

## Sources

- Klartag and Lehec, arXiv:2507.15495v1, Theorem 1.1.

Stated but not proved: `MathlibExt.Probability.ThinShell.thinShellVarianceConstant_lt_top` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#thin-shell-variance-constant-lt-top).

## The standard Gaussian has normalized radius variance 2

For every dimension $n \ge 1$,
the standard Gaussian measure $\gamma_n$ on $\mathbb{R}^n$ is isotropic log-concave (a probability
measure with a log-concave Lebesgue density, mean $0$ and identity covariance), and its normalized
radius variance $\frac{1}{n} \int (|x|^2 - n)^2 \, d\gamma_n(x)$ equals $2$.

## Sources

- Klartag--Lehec, arXiv:2507.15495v1, Introduction.

Stated but not proved: `MathlibExt.Probability.ThinShell.stdGaussian_isotropic_variance` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#std-gaussian-isotropic-variance).

## The isotropic cube has normalized radius variance 4/5

For every dimension $n \ge 1$, let
$\mu$ be the uniform probability measure on the cube $[-\sqrt{3}, \sqrt{3}]^n \subset \mathbb{R}^n$
(Lebesgue measure restricted to the cube and divided by its volume). Then $\mu$ is isotropic
log-concave (a probability measure with a log-concave Lebesgue density, mean $0$ and identity
covariance), and its normalized radius variance $\frac{1}{n} \int (|x|^2 - n)^2 \, d\mu(x)$
equals $4/5$.

The cube is scaled to covariance identity, so this is the unit-variance convention.

## Sources

- Klartag--Lehec, arXiv:2507.15495v1, Introduction.

Stated but not proved: `MathlibExt.Probability.ThinShell.uniformCube_isotropic_variance` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#uniform-cube-isotropic-variance).

## Cube lower bound for the thin-shell variance constant

The thin-shell variance constant,
an element of $[0, \infty]$, is at least $4/5$.

The value $4/5$ is the exact normalized radius variance of the uniform law on a cube scaled to
identity covariance.

## Sources

- Klartag and Lehec, arXiv:2507.15495v1, Introduction.

Stated but not proved: `MathlibExt.Probability.ThinShell.fourFifths_le_thinShellVarianceConstant` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#four-fifths-le-thin-shell-variance-const).

## The thin-shell variance constant is at least 2

The thin-shell variance constant, the
supremum in $[0, \infty]$ of the normalized radius variances
$\frac{1}{n} \int (|x|^2 - n)^2 \, d\mu(x)$ over all dimensions $n \ge 1$ and all isotropic
log-concave probability measures $\mu$ on $\mathbb{R}^n$, is at least $2$.

The lower bound comes from the standard Gaussian, whose normalized radius variance is $2$ in
every dimension.

## Sources

- Klartag and Lehec, arXiv:2507.15495v1, Introduction.

Stated but not proved: `MathlibExt.Probability.ThinShell.two_le_thinShellVarianceConstant` is written with `theorem_wanted` in [WantedExt/Probability/ThinShellBoundsWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ThinShellBoundsWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html#two-le-thin-shell-variance-constant).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Thin-shell conjecture](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/high-dimensional-probability/thin-shell-conjecture)
