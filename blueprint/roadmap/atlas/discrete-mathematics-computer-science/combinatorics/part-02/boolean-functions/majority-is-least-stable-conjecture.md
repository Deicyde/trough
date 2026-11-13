---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MajorityIsLeastStableAMR127Problem0009Wanted.IsLinearThresholdFunction, MathlibExt.Combinatorics.MajorityIsLeastStableAMR127Problem0009Wanted.majority, MathlibExt.Combinatorics.MajorityIsLeastStableAMR127Problem0009Wanted.noiseStability, MathlibExt.Combinatorics.MajorityIsLeastStableAMR127Problem0009Wanted.MajorityIsLeastStableFor, MathlibExt.Combinatorics.MajorityIsLeastStableAMR127Problem0009Wanted.majorityIsLeastStableForSomeOddAtLeastFive, MathlibExt.Combinatorics.MajorityIsLeastStableAMR127Problem0009Wanted.majorityIsLeastStableForSomeOddAtLeastFive_refuted
statement: formalized
---

# Majority is least stable conjecture

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/majority-is-least-stable-conjecture/index.html).

## Linear threshold function

A function $f : \{-1, 1\}^n \to \mathbb{R}$ is a linear
threshold function if there are reals $w_0, w_1, \dots, w_n$ such that for every
$x \in \{-1, 1\}^n$ we have $f(x) = \operatorname{sgn}(w_0 + w_1 x_1 + \dots + w_n x_n)$, where
$x_i \in \{-1, 1\}$ is the $i$-th coordinate of $x$, $\operatorname{sgn} z = 1$ for $z \ge 0$ and
$\operatorname{sgn} z = -1$ for $z < 0$.

Formalized by `MathlibExt.Combinatorics.MajorityIsLeastStableAMR127Problem0009Wanted.IsLinearThresholdFunction`, a definition declared in [WantedExt/Combinatorics/MajorityIsLeastStableAMR127Problem0009Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MajorityIsLeastStableAMR127Problem0009Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/majority-is-least-stable-conjecture/index.html#is-linear-threshold-function).

## Majority function

For $n \in \mathbb{N}$, the majority function
$\mathrm{Maj}_n : \{-1, 1\}^n \to \mathbb{R}$ is given by $\mathrm{Maj}_n(x) = 1$ if
$x_1 + \dots + x_n \ge 0$ and $\mathrm{Maj}_n(x) = -1$ otherwise, where $x_i \in \{-1, 1\}$ is the
$i$-th coordinate of $x$.

Formalized by `MathlibExt.Combinatorics.MajorityIsLeastStableAMR127Problem0009Wanted.majority`, a definition declared in [WantedExt/Combinatorics/MajorityIsLeastStableAMR127Problem0009Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MajorityIsLeastStableAMR127Problem0009Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/majority-is-least-stable-conjecture/index.html#majority).

## Noise stability

For a real number $\rho$ and a function $f : \{-1, 1\}^n \to \mathbb{R}$,
the noise stability of $f$ at $\rho$ is
$\mathrm{Stab}_\rho[f] = \sum_{S \subseteq \{1, \dots, n\}} \rho^{|S|} \hat f(S)^2$, where
$\hat f(S)$ is the Fourier coefficient of $f$ at $S$.

For $-1 \le \rho \le 1$ this is the Fourier expansion of $\mathbb{E}[f(x) f(y)]$ for uniform $x$
and a $\rho$-correlated copy $y$ of $x$.

Formalized by `MathlibExt.Combinatorics.MajorityIsLeastStableAMR127Problem0009Wanted.noiseStability`, a definition declared in [WantedExt/Combinatorics/MajorityIsLeastStableAMR127Problem0009Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MajorityIsLeastStableAMR127Problem0009Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/majority-is-least-stable-conjecture/index.html#noise-stability).

## Majority Is Least Stable conjecture in $n$ variables

For $n \in \mathbb{N}$, this is the
statement that every linear threshold function $f : \{-1, 1\}^n \to \mathbb{R}$ satisfies
$\mathrm{Stab}_\rho[f] \ge \mathrm{Stab}_\rho[\mathrm{Maj}_n]$ for every real $\rho$ with
$0 \le \rho \le 1$, where $\mathrm{Stab}_\rho$ is the noise stability and $\mathrm{Maj}_n$ is the
majority function.

Formalized by `MathlibExt.Combinatorics.MajorityIsLeastStableAMR127Problem0009Wanted.MajorityIsLeastStableFor`, a definition declared in [WantedExt/Combinatorics/MajorityIsLeastStableAMR127Problem0009Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MajorityIsLeastStableAMR127Problem0009Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/majority-is-least-stable-conjecture/index.html#majority-is-least-stable-for).

## Majority Is Least Stable in some odd dimension at least five

There is an odd natural
number $n \ge 5$ for which the Majority Is Least Stable conjecture in $n$ variables holds: every
linear threshold function $f : \{-1, 1\}^n \to \mathbb{R}$ satisfies
$\mathrm{Stab}_\rho[f] \ge \mathrm{Stab}_\rho[\mathrm{Maj}_n]$ for every real $\rho$ with
$0 \le \rho \le 1$, where $\mathrm{Stab}_\rho$ is the noise stability and $\mathrm{Maj}_n$ is the
majority function.

Formalized by `MathlibExt.Combinatorics.MajorityIsLeastStableAMR127Problem0009Wanted.majorityIsLeastStableForSomeOddAtLeastFive`, a definition declared in [WantedExt/Combinatorics/MajorityIsLeastStableAMR127Problem0009Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MajorityIsLeastStableAMR127Problem0009Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/majority-is-least-stable-conjecture/index.html#majority-is-least-stable-for-some-odd-at).

## Majority Is Least Stable fails in every odd dimension at least five

For every odd natural
number $n \ge 5$, the Majority Is Least Stable conjecture in $n$ variables fails: there are a
linear threshold function $f : \{-1, 1\}^n \to \mathbb{R}$ and a real number $\rho$ with
$0 \le \rho \le 1$ such that $\mathrm{Stab}_\rho[f] < \mathrm{Stab}_\rho[\mathrm{Maj}_n]$, where
$\mathrm{Stab}_\rho$ is the noise stability and $\mathrm{Maj}_n$ is the majority function.

Biswas and Sarkar exhibit, for every odd $n \ge 5$, a linear threshold function $g_n$ with
$\mathrm{Stab}_\rho[g_n] < \mathrm{Stab}_\rho[\mathrm{Maj}_n]$ for all small $\rho > 0$. The
conjecture holds for $n = 1$ and $n = 3$.

## Sources

- R. O'Donnell, Open problems in analysis of Boolean functions, arXiv:1204.6447 (2012), 'Majority Is Least Stable Conjecture' (Benjamini, Kalai, Schramm); resolution: A. Biswas, P. Sarkar, On the "majority is least stable" conjecture, Inform. Process. Lett. 179 (2023), 106295, arXiv:2202.09024, Theorem 2 of arXiv:2202.09024v2: the conjecture is true for n = 1 and n = 3 and false for every odd n ≥ 5; for odd n ≥ 5 the linear threshold function g_n(x) = sgn(2(x₁ + ⋯ + x_{n-3}) + x_{n-2} + x_{n-1} + x_n) has W⁰[g_n] = 0 and W¹[g_n] < W¹[Maj_n] (Lemmas 3 and 4), hence Stab_ρ[g_n] < Stab_ρ[Maj_n] for all small ρ > 0 (Lemma 1); the case n = 5 is V. Jain, arXiv:1703.07657, https://doi.org/10.1016/j.ipl.2022.106295.

Stated but not proved: `MathlibExt.Combinatorics.MajorityIsLeastStableAMR127Problem0009Wanted.majorityIsLeastStableForSomeOddAtLeastFive_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/MajorityIsLeastStableAMR127Problem0009Wanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MajorityIsLeastStableAMR127Problem0009Wanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/majority-is-least-stable-conjecture/index.html#majority-is-least-stable-for-some-odd-at-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Majority is least stable conjecture](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/majority-is-least-stable-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/majority-is-least-stable-conjecture)
