---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.HyperbolicShadowingWanted.Dynamics.HyperbolicShadowingProblem.E, MathlibExt.Dynamics.HyperbolicShadowingWanted.Dynamics.HyperbolicShadowingProblem.HyperbolicStructure, MathlibExt.Dynamics.HyperbolicShadowingWanted.Dynamics.HyperbolicShadowingProblem.IsHyperbolic, MathlibExt.Dynamics.HyperbolicShadowingWanted.Dynamics.HyperbolicShadowingProblem.IsPseudoOrbit, MathlibExt.Dynamics.HyperbolicShadowingWanted.Dynamics.HyperbolicShadowingProblem.HasShadowing, MathlibExt.Dynamics.HyperbolicShadowingWanted.Dynamics.HyperbolicShadowingProblem.hyperbolic_has_shadowing
statement: formalized
---

# Shadowing lemma

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/shadowing-lemma/index.html).

## Euclidean model space for the shadowing lemma

For a natural number $d$, $E_d$ is the
Euclidean space $\mathbb{R}^d$, the real $d$-tuples with the Euclidean norm.

Formalized by `MathlibExt.Dynamics.HyperbolicShadowingWanted.Dynamics.HyperbolicShadowingProblem.E`, an abbreviation declared in [WantedExt/Dynamics/HyperbolicShadowingWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/HyperbolicShadowingWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/shadowing-lemma/index.html#e).

## Hyperbolic structure

Let $T : \mathbb{R}^d \to \mathbb{R}^d$ be a homeomorphism and let
$K \subseteq \mathbb{R}^d$. Write $DF_x$ for the derivative of a map $F$ at $x$, $T^n$ for the
$n$-fold iterate of $T$ and $T^{-n}$ for the $n$-fold iterate of $T^{-1}$. A hyperbolic structure
for $T$ on $K$ consists of the following: $T$ and $T^{-1}$ are $C^1$; $T(K) = K$; to every
$x \in \mathbb{R}^d$ are assigned linear subspaces $E^s(x)$ and $E^u(x)$ of $\mathbb{R}^d$ such that
for every $x \in K$ we have $\mathbb{R}^d = E^s(x) \oplus E^u(x)$, $DT_x(E^s(x)) = E^s(T(x))$ and
$DT_x(E^u(x)) = E^u(T(x))$; and there are real numbers $\lambda$ with $0 < \lambda < 1$ and
$C > 0$ such that for every $x \in K$ and every $n \in \mathbb{N}$,
$\|D(T^n)_x v\| \le C \lambda^n \|v\|$ for all $v \in E^s(x)$ and
$\|D(T^{-n})_x v\| \le C \lambda^n \|v\|$ for all $v \in E^u(x)$.

Formalized by `MathlibExt.Dynamics.HyperbolicShadowingWanted.Dynamics.HyperbolicShadowingProblem.HyperbolicStructure`, a structure declared in [WantedExt/Dynamics/HyperbolicShadowingWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/HyperbolicShadowingWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/shadowing-lemma/index.html#hyperbolic-structure).

## Hyperbolic invariant set

Let $T : \mathbb{R}^d \to \mathbb{R}^d$ be a homeomorphism. A set
$K \subseteq \mathbb{R}^d$ is a hyperbolic invariant set for $T$ if there exists a hyperbolic
structure for $T$ on $K$.

Formalized by `MathlibExt.Dynamics.HyperbolicShadowingWanted.Dynamics.HyperbolicShadowingProblem.IsHyperbolic`, a definition declared in [WantedExt/Dynamics/HyperbolicShadowingWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/HyperbolicShadowingWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/shadowing-lemma/index.html#is-hyperbolic).

## Pseudo-orbit

Let $d$ be a natural number, let $\mathbb{R}^d$ carry the Euclidean norm,
let $T : \mathbb{R}^d \to \mathbb{R}^d$ be a map and let $\varepsilon$ be a real number. A
sequence $(x_n)_{n \in \mathbb{N}}$ in $\mathbb{R}^d$ is an $\varepsilon$-pseudo orbit of $T$
if $\|x_{n+1} - T(x_n)\| < \varepsilon$ for every $n \in \mathbb{N}$.

Formalized by `MathlibExt.Dynamics.HyperbolicShadowingWanted.Dynamics.HyperbolicShadowingProblem.IsPseudoOrbit`, a definition declared in [WantedExt/Dynamics/HyperbolicShadowingWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/HyperbolicShadowingWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/shadowing-lemma/index.html#is-pseudo-orbit).

## Shadowing property

Let $T : \mathbb{R}^d \to \mathbb{R}^d$ be a map, write $T^n$ for its
$n$-fold iterate, and let $K \subseteq \mathbb{R}^d$. The set $K$ has the shadowing property for
$T$ if there is an open set $U \subseteq \mathbb{R}^d$ containing $K$ such that for every
$\delta > 0$ there is $\varepsilon > 0$ with the following property: for every $\varepsilon$-pseudo
orbit $(x_n)_{n \in \mathbb{N}}$ of $T$ with $x_n \in U$ for all $n$, there is a point
$y \in \mathbb{R}^d$ with $\|x_n - T^n(y)\| < \delta$ for all $n \in \mathbb{N}$.

Formalized by `MathlibExt.Dynamics.HyperbolicShadowingWanted.Dynamics.HyperbolicShadowingProblem.HasShadowing`, a definition declared in [WantedExt/Dynamics/HyperbolicShadowingWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/HyperbolicShadowingWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/shadowing-lemma/index.html#has-shadowing).

## Anosov–Bowen shadowing lemma

Let $T : \mathbb{R}^d \to \mathbb{R}^d$ be a homeomorphism and
let $K \subseteq \mathbb{R}^d$ be a compact set that is a hyperbolic invariant set for $T$. Then $K$
has the shadowing property for $T$.

## Sources

- D.V. Anosov, 'Geodesic flows on closed Riemannian manifolds with negative curvature', Trudy Mat. Inst. Steklov. 90 (1967); R. Bowen, 'ω-limit sets for Axiom A diffeomorphisms', J. Differential Equations 18 (1975) 333–339. Listed as §67 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `anosov_bowen_shadowing` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.HyperbolicShadowingWanted.Dynamics.HyperbolicShadowingProblem.hyperbolic_has_shadowing` is written with `theorem_wanted` in [WantedExt/Dynamics/HyperbolicShadowingWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/HyperbolicShadowingWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/shadowing-lemma/index.html#hyperbolic-has-shadowing).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shadowing lemma](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/shadowing-lemma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/smooth-dynamics/shadowing-lemma)
