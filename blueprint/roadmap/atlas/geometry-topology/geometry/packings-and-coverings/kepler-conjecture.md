---
declaration: section
origin: cited
lean: MathlibExt.Geometry.KeplerConjectureWanted.Geometry.KeplerConjectureProblem.E, MathlibExt.Geometry.KeplerConjectureWanted.Geometry.KeplerConjectureProblem.IsPacking, MathlibExt.Geometry.KeplerConjectureWanted.Geometry.KeplerConjectureProblem.coveredFraction, MathlibExt.Geometry.KeplerConjectureWanted.Geometry.KeplerConjectureProblem.density, MathlibExt.Geometry.KeplerConjectureWanted.Geometry.KeplerConjectureProblem.Δ, MathlibExt.Geometry.KeplerConjectureWanted.Geometry.KeplerConjectureProblem.kepler_conjecture
statement: formalized
---

# Kepler conjecture

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/kepler-conjecture/index.html).

## Euclidean space for sphere packings

For a natural number $d$, $\mathbb{R}^d$ denotes the
$d$-dimensional real Euclidean space: $d$-tuples of real numbers with the Euclidean norm.

Formalized by `MathlibExt.Geometry.KeplerConjectureWanted.Geometry.KeplerConjectureProblem.E`, an abbreviation declared in [WantedExt/Geometry/KeplerConjectureWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/KeplerConjectureWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/kepler-conjecture/index.html#e).

## Unit sphere packing

For a natural number $d$, a set $X \subseteq \mathbb{R}^d$ is the
centre set of a unit sphere packing if the open balls of radius $1$ centred at any two distinct
points of $X$ are disjoint.

Formalized by `MathlibExt.Geometry.KeplerConjectureWanted.Geometry.KeplerConjectureProblem.IsPacking`, a definition declared in [WantedExt/Geometry/KeplerConjectureWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/KeplerConjectureWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/kepler-conjecture/index.html#is-packing).

## Covered fraction of a ball

For a natural number $d$, a set $X \subseteq \mathbb{R}^d$ and a
real number $R$, the covered fraction of $X$ at radius $R$ is

$$\frac{\operatorname{vol}\bigl(B_R(0) \cap \bigcup_{x \in X} B_1(x)\bigr)}
{\operatorname{vol}(B_R(0))},$$

where $B_r(y)$ is the open ball of radius $r$ about $y$ and $\operatorname{vol}$ is Lebesgue
measure; it equals $0$ when $R \le 0$.

Formalized by `MathlibExt.Geometry.KeplerConjectureWanted.Geometry.KeplerConjectureProblem.coveredFraction`, a definition declared in [WantedExt/Geometry/KeplerConjectureWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/KeplerConjectureWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/kepler-conjecture/index.html#covered-fraction).

## Density of a sphere packing

For a natural number $d$, the density of a set
$X \subseteq \mathbb{R}^d$ is the limit superior, as $R \to \infty$, of the covered fraction of $X$
at radius $R$: the fraction of the open ball of radius $R$ about the origin covered by the open
unit balls centred at points of $X$.

Formalized by `MathlibExt.Geometry.KeplerConjectureWanted.Geometry.KeplerConjectureProblem.density`, a definition declared in [WantedExt/Geometry/KeplerConjectureWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/KeplerConjectureWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/kepler-conjecture/index.html#density).

## Optimal sphere packing density

For a natural number $d$, $\Delta(d)$ is the supremum of
the densities of all unit sphere packings in $\mathbb{R}^d$.

Formalized by `MathlibExt.Geometry.KeplerConjectureWanted.Geometry.KeplerConjectureProblem.Δ`, a definition declared in [WantedExt/Geometry/KeplerConjectureWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/KeplerConjectureWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/kepler-conjecture/index.html#untitled).

## Kepler conjecture

Let $\Delta(3)$ be the supremum of the densities of all unit sphere
packings in $\mathbb{R}^3$. Then $\Delta(3) = \pi / \sqrt{18}$.

## Sources

- Kepler conjecture 1611 (J. Kepler, *Strena seu de Nive Sexangula*); proof T. Hales, 'A proof of the Kepler conjecture', Ann. of Math. (2) 162 (2005) 1065–1185; formal verification in HOL Light + Isabelle by the Flyspeck project (T. Hales et al., completed August 2014), Forum Math. Pi 5 (2017) e2. Wiedijk-1000 #209; listed as §96 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `kepler_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.KeplerConjectureWanted.Geometry.KeplerConjectureProblem.kepler_conjecture` is written with `theorem_wanted` in [WantedExt/Geometry/KeplerConjectureWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/KeplerConjectureWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/kepler-conjecture/index.html#kepler-conjecture).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kepler conjecture](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/kepler-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/packings-and-coverings/kepler-conjecture)
