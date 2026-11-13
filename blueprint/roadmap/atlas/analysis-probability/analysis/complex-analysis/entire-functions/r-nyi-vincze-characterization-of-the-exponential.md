---
declaration: section
origin: cited
lean: MathlibExt.Analysis.HaymanProblem232Wanted.conjecture, MathlibExt.Analysis.HaymanProblem232Wanted.conjecture_refuted
statement: formalized
---

# Rényi–Vincze characterization of the exponential

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/r-nyi-vincze-characterization-of-the-exponential/index.html).

## Hayman Problem 2.32: a non-exponential solution of the Rényi–Vincze conditions

There
exist a function $f : \mathbb{C} \to \mathbb{C}$ and real numbers $a_0, a_1, a_2, \dots$ such that
$f$ is not the function $z \mapsto c\,e^z$ for any real $c > 0$; $a_n \ge 0$ for every $n$;
$a_n \ne 0$ for infinitely many $n$; for every $z \in \mathbb{C}$ the series
$\sum_{n \ge 0} a_n z^n$ has sum $f(z)$; $f$ is entire; and either
$\int_0^\infty a_n x^n / f(x)\,dx = 1$ for every $n \ge 0$ (condition (2.6)), or
$\int_0^\infty f(\rho x) / f(x)\,dx = 1/(1-\rho)$ for every real $\rho$ with $0 < \rho < 1$
(condition (2.6)').

## Sources

- AMR-022-2032, Hayman - Research Problems in Function Theory (2018), Problem 2.32 (https://arxiv.org/abs/1809.07200, source labels 2.6 and 2.6', A. Renyi, St. Vincze).

Formalized by `MathlibExt.Analysis.HaymanProblem232Wanted.conjecture`, a definition declared in [WantedExt/Analysis/HaymanProblem232Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HaymanProblem232Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/r-nyi-vincze-characterization-of-the-exponential/index.html#conjecture).

## No non-exponential solution of the Rényi–Vincze conditions

There are no function
$f : \mathbb{C} \to \mathbb{C}$ and real numbers $a_0, a_1, a_2, \dots$ such that $f$ is not the
function $z \mapsto c\,e^z$ for any real $c > 0$; $a_n \ge 0$ for every $n$; $a_n \ne 0$ for
infinitely many $n$; for every $z \in \mathbb{C}$ the series $\sum_{n \ge 0} a_n z^n$ has sum
$f(z)$; $f$ is entire; and either $\int_0^\infty a_n x^n / f(x)\,dx = 1$ for every $n \ge 0$, or
$\int_0^\infty f(\rho x) / f(x)\,dx = 1/(1-\rho)$ for every real $\rho$ with $0 < \rho < 1$.

Miles and Williamson (J. London Math. Soc. (2) 33 (1986) 110-116) proved that a transcendental
entire $f$ with positive coefficients and $\int_0^\infty a_n x^n / f(x)\,dx = 1$ for all $n$ is
$c\,e^z$. The first integral condition forces every $a_n > 0$, and the second reduces to the
first.

## Sources

- Antonio Greco and Andrea Loi, Radial balanced metrics on the unit disk, arXiv:0803.3711 (2008), https://arxiv.org/abs/0803.3711.

Stated but not proved: `MathlibExt.Analysis.HaymanProblem232Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/HaymanProblem232Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HaymanProblem232Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/r-nyi-vincze-characterization-of-the-exponential/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rényi–Vincze characterization of the exponential](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/r-nyi-vincze-characterization-of-the-exponential/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/entire-functions/r-nyi-vincze-characterization-of-the-exponential)
