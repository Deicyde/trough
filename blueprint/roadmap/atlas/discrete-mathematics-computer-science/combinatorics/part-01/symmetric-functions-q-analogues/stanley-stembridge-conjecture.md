---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.StanleyStembridgeEPositivityAMR156Problem0022Wanted.IsThreePlusOneFree, MathlibExt.Combinatorics.StanleyStembridgeEPositivityAMR156Problem0022Wanted.incomparabilityGraph, MathlibExt.Combinatorics.StanleyStembridgeEPositivityAMR156Problem0022Wanted.chromaticSymmetricPoly, MathlibExt.Combinatorics.StanleyStembridgeEPositivityAMR156Problem0022Wanted.IsEPositive, MathlibExt.Combinatorics.StanleyStembridgeEPositivityAMR156Problem0022Wanted.stanleyStembridge, MathlibExt.Combinatorics.StanleyStembridgeEPositivityAMR156Problem0022Wanted.stanleyStembridge_holds
statement: formalized
---

# Stanley–Stembridge conjecture

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/stanley-stembridge-conjecture/index.html).

## $(3+1)$-free posets

A partially ordered set $P$ is $(3+1)$-free when there are no
elements $a, b, c, d \in P$ with $a < b < c$ such that $d$ is incomparable to each of $a$, $b$
and $c$ (neither $d \le x$ nor $x \le d$ for $x = a, b, c$).

Formalized by `MathlibExt.Combinatorics.StanleyStembridgeEPositivityAMR156Problem0022Wanted.IsThreePlusOneFree`, a definition declared in [WantedExt/Combinatorics/StanleyStembridgeEPositivityAMR156Problem0022Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StanleyStembridgeEPositivityAMR156Problem0022Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/stanley-stembridge-conjecture/index.html#is-three-plus-one-free).

## Incomparability graph of a poset

The incomparability graph $\operatorname{inc}(P)$ of a
partially ordered set $P$ is the simple graph on $P$ in which two distinct elements $x$ and $y$ are
adjacent when they are incomparable, that is, neither $x \le y$ nor $y \le x$.

Formalized by `MathlibExt.Combinatorics.StanleyStembridgeEPositivityAMR156Problem0022Wanted.incomparabilityGraph`, a definition declared in [WantedExt/Combinatorics/StanleyStembridgeEPositivityAMR156Problem0022Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StanleyStembridgeEPositivityAMR156Problem0022Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/stanley-stembridge-conjecture/index.html#incomparability-graph).

## Chromatic symmetric function in as many variables as vertices

For a simple graph $G$ on
a finite vertex set $V$ with $n = |V|$ elements, $X_G$ is the polynomial with integer coefficients
in the variables $x_0, \dots, x_{n-1}$ given by $X_G = \sum_{\kappa} \prod_{v \in V} x_{\kappa(v)}$,
where $\kappa$ ranges over the proper colourings $\kappa : V \to \{0, \dots, n - 1\}$ of $G$, that
is, the maps with $\kappa(u) \ne \kappa(v)$ whenever $u$ and $v$ are adjacent.

Formalized by `MathlibExt.Combinatorics.StanleyStembridgeEPositivityAMR156Problem0022Wanted.chromaticSymmetricPoly`, a definition declared in [WantedExt/Combinatorics/StanleyStembridgeEPositivityAMR156Problem0022Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StanleyStembridgeEPositivityAMR156Problem0022Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/stanley-stembridge-conjecture/index.html#chromatic-symmetric-poly).

## $e$-positive polynomials

A polynomial $f$ with integer coefficients in the $n$ variables
$x_0, \dots, x_{n-1}$ is $e$-positive when $f = \sum_{\lambda} c_\lambda e_\lambda$ for some
natural numbers $c_\lambda$, where $\lambda = (\lambda_1, \dots, \lambda_k)$ ranges over the
partitions of $n$ and $e_\lambda = e_{\lambda_1} \cdots e_{\lambda_k}$ is the product of the
elementary symmetric polynomials $e_{\lambda_i}$ in $x_0, \dots, x_{n-1}$.

Formalized by `MathlibExt.Combinatorics.StanleyStembridgeEPositivityAMR156Problem0022Wanted.IsEPositive`, a definition declared in [WantedExt/Combinatorics/StanleyStembridgeEPositivityAMR156Problem0022Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StanleyStembridgeEPositivityAMR156Problem0022Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/stanley-stembridge-conjecture/index.html#is-epositive).

## Statement of the Stanley–Stembridge conjecture

The proposition that for every finite
$(3+1)$-free partially ordered set $P$, the chromatic symmetric function in $|P|$ variables of the
incomparability graph of $P$ is $e$-positive.

Formalized by `MathlibExt.Combinatorics.StanleyStembridgeEPositivityAMR156Problem0022Wanted.stanleyStembridge`, a definition declared in [WantedExt/Combinatorics/StanleyStembridgeEPositivityAMR156Problem0022Wanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StanleyStembridgeEPositivityAMR156Problem0022Wanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/stanley-stembridge-conjecture/index.html#stanley-stembridge).

## Hikita's theorem: the Stanley–Stembridge conjecture holds

For every finite $(3+1)$-free
partially ordered set $P$, the chromatic symmetric function in $|P|$ variables of the
incomparability graph of $P$ is $e$-positive.

## Sources

- R. P. Stanley, Positivity Problems and Conjectures in Algebraic Combinatorics (1999), Problem 21 (Stanley-Stembridge conjecture; Stanley and Stembridge, J. Combin. Theory Ser. A 62 (1993), Conjecture 5.5); resolution: T. Hikita, A proof of the Stanley-Stembridge conjecture, J. Amer. Math. Soc., published online (Early View) 2026-08-28, doi:10.1090/jams/1090, https://www.ams.org/jams/earlyview/#jams1090; arXiv:2410.12758, Abstract: a probabilistic interpretation of the coefficients of the elementary symmetric function expansion of the chromatic quasisymmetric function of every unit interval graph, 'As a corollary, we prove the Stanley-Stembridge conjecture'; Section 1.1: the positivity of these coefficients 'is sufficient to conclude that the original Stanley-Stembridge conjecture is true', https://doi.org/10.1090/jams/1090.

Stated but not proved: `MathlibExt.Combinatorics.StanleyStembridgeEPositivityAMR156Problem0022Wanted.stanleyStembridge_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/StanleyStembridgeEPositivityAMR156Problem0022Wanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StanleyStembridgeEPositivityAMR156Problem0022Wanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/stanley-stembridge-conjecture/index.html#stanley-stembridge-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stanley–Stembridge conjecture](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/stanley-stembridge-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/symmetric-functions-q-analogues/stanley-stembridge-conjecture)
