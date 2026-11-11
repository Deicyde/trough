---
declaration: section
origin: cited
lean: MathlibExt.Geometry.Manifold.MorseTheoryWanted.morseQuadratic, MathlibExt.Geometry.Manifold.MorseTheoryWanted.morseQuadratic_zero, MathlibExt.Geometry.Manifold.MorseTheoryWanted.contDiff_morseQuadratic, MathlibExt.Geometry.Manifold.MorseTheoryWanted.morseQuadratic_zero_index, MathlibExt.Geometry.Manifold.MorseTheoryWanted.morseQuadratic_of_le, MathlibExt.Geometry.Manifold.ReebSphereWanted.IsMorseFunction, MathlibExt.Geometry.Manifold.MorseLemmaWanted.morse_lemma, MathlibExt.Geometry.Manifold.MorseExistenceWanted.morse_function_exists
statement: formalized
---

# Morse theory

11 results, 9 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html).

## Morse quadratic form

For natural numbers $k$ and $n$, the Morse quadratic form of index
$k$ on $\mathbb{R}^n$, with coordinates $v_0, \dots, v_{n-1}$, is the function
$Q_{k,n} \colon \mathbb{R}^n \to \mathbb{R}$ given by
$Q_{k,n}(v) = \sum_{i=0}^{n-1} \varepsilon_i v_i^2$, where $\varepsilon_i = -1$ if $i < k$ and
$\varepsilon_i = 1$ if $i \ge k$. In particular, if $k \ge n$ every coefficient is $-1$.

Formalized by `MathlibExt.Geometry.Manifold.MorseTheoryWanted.morseQuadratic`, a definition declared in [MathlibExt/Geometry/Manifold/MorseTheory.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/MorseTheory.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html#morse-quadratic).

## The Morse quadratic form vanishes at the origin

For all natural numbers $k$ and $n$, the
Morse quadratic form $Q_{k,n}$ of index $k$ on $\mathbb{R}^n$ satisfies $Q_{k,n}(0) = 0$.

Formalized by `MathlibExt.Geometry.Manifold.MorseTheoryWanted.morseQuadratic_zero`, a lemma declared in [MathlibExt/Geometry/Manifold/MorseTheory.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/MorseTheory.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html#morse-quadratic-zero).

## Smoothness of the Morse quadratic form

For all natural numbers $k$ and $n$, the Morse
quadratic form $Q_{k,n} \colon \mathbb{R}^n \to \mathbb{R}$ of index $k$ is $C^\infty$.

Formalized by `MathlibExt.Geometry.Manifold.MorseTheoryWanted.contDiff_morseQuadratic`, a lemma declared in [MathlibExt/Geometry/Manifold/MorseTheory.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/MorseTheory.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html#cont-diff-morse-quadratic).

## The Morse quadratic form of index zero

For every natural number $n$, the Morse quadratic
form $Q_{0,n}$ of index $0$ on $\mathbb{R}^n$ satisfies $Q_{0,n}(v) = \|v\|^2$ for every
$v \in \mathbb{R}^n$, where $\|v\|$ is the Euclidean norm of $v$.

Formalized by `MathlibExt.Geometry.Manifold.MorseTheoryWanted.morseQuadratic_zero_index`, a lemma declared in [MathlibExt/Geometry/Manifold/MorseTheory.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/MorseTheory.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html#morse-quadratic-zero-index).

## The Morse quadratic form when the index is at least the dimension

If $n \le k$, then the
Morse quadratic form $Q_{k,n}$ of index $k$ on $\mathbb{R}^n$ satisfies $Q_{k,n}(v) = -\|v\|^2$
for every $v \in \mathbb{R}^n$, where $\|v\|$ is the Euclidean norm of $v$.

Formalized by `MathlibExt.Geometry.Manifold.MorseTheoryWanted.morseQuadratic_of_le`, a lemma declared in [MathlibExt/Geometry/Manifold/MorseTheory.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/MorseTheory.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html#morse-quadratic-of-le).

## Morse function

Let $M$ be a $C^\infty$ manifold without boundary modelled on a real
normed space of finite dimension $d$. A function $f \colon M \to \mathbb{R}$ is a Morse function
if it is $C^\infty$ and, for every critical point $p$ of $f$ (a point where the differential
$df_p$ is zero), there exist an integer $0 \le k \le d$, a map $\varphi \colon M \to \mathbb{R}^d$
that is a local $C^\infty$ diffeomorphism at $p$ with $\varphi(p) = 0$, and an open set $U$
containing $p$ such that $f(q) = f(p) + Q_k(\varphi(q))$ for all $q \in U$. Here $Q_k$ is the
Morse quadratic form $Q_k(y) = -y_1^2 - \dots - y_k^2 + y_{k+1}^2 + \dots + y_d^2$ on
$\mathbb{R}^d$.

Formalized by `MathlibExt.Geometry.Manifold.ReebSphereWanted.IsMorseFunction`, a definition declared in [MathlibExt/Geometry/Manifold/MorseFunction.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/MorseFunction.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html#is-morse-function).

## Morse lemma

Let $f \colon \mathbb{R}^n \to \mathbb{R}$ be a $C^\infty$ function with
$Df(0) = 0$ whose Hessian at $0$ is nondegenerate: if $v \in \mathbb{R}^n$ satisfies
$D^2 f(0)(v, w) = 0$ for all $w \in \mathbb{R}^n$, then $v = 0$. Then there exist an integer
$0 \le k \le n$, a map $\varphi \colon \mathbb{R}^n \to \mathbb{R}^n$ that is a local $C^\infty$
diffeomorphism at $0$ with $\varphi(0) = 0$, and an open set $U$ containing $0$ such that
$f(x) = f(0) + Q_k(\varphi(x))$ for all $x \in U$. Here $Q_k$ is the Morse quadratic form
$Q_k(y) = -y_1^2 - \dots - y_k^2 + y_{k+1}^2 + \dots + y_n^2$ on $\mathbb{R}^n$.

## Sources

- J. Milnor, Morse Theory, Ann. of Math. Studies 51 (1963) Lemma 2.2; M. Hirsch, Differential Topology; J. Lee, Intro to Smooth Manifolds, 2nd ed., Morse lemma; Lean states Euclidean origin finite-dimensional specialization with corrected nondegeneracy grouping `(∀ w, (fderiv (fderiv f) 0 v) w = 0) → v = 0`.

Formalized by `MathlibExt.Geometry.Manifold.MorseLemmaWanted.morse_lemma`, a theorem declared in [MathlibExt/Geometry/Manifold/MorseLemma.lean, line 1463](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/MorseLemma.lean#L1463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html#morse-lemma).

## Existence of Morse functions

Every Hausdorff, second-countable $C^\infty$ manifold $M$
without boundary, modelled on a finite-dimensional real normed space, admits a Morse function
$f \colon M \to \mathbb{R}$.

## Sources

- J. Milnor, Morse Theory, Ann. of Math. Studies 51 (1963); M. Hirsch, Differential Topology; J. Lee, Intro to Smooth Manifolds, 2nd ed.; Lean states boundaryless finite-dimensional second-countable specialization.

Formalized by `MathlibExt.Geometry.Manifold.MorseExistenceWanted.morse_function_exists`, a theorem declared in [MathlibExt/Geometry/Manifold/MorseExistence.lean, line 1373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/MorseExistence.lean#L1373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html#morse-function-exists).

## Alternating partial sum

For a sequence $a_0, a_1, a_2, \dots$ of natural numbers and
$k \in \mathbb{N}$, the alternating partial sum of $a$ up to $k$ is the integer
$\sum_{j=0}^{k} (-1)^{k-j} a_j$.

Formalized by `MathlibExt.Geometry.MorseInequalitiesWanted.Geometry.MorseInequalities.alternatingPartialSum`, a definition declared in [WantedExt/Geometry/MorseInequalitiesWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MorseInequalitiesWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html#alternating-partial-sum).

## Morse inequalities

Let $M$ be a compact Hausdorff smooth manifold without boundary,
modelled on a finite-dimensional real normed space, and let $f : M \to \mathbb{R}$ be a Morse
function: $f$ is $C^\infty$, has finitely many critical points, and the Hessian of $f$ at each
critical point, computed in the preferred chart, is a nondegenerate bilinear form. The Morse index
of a critical point is the largest dimension of a subspace on which this Hessian is negative
definite. For $j \in \mathbb{N}$ let $c_j$ be the number of critical points of $f$ of Morse index
$j$, and let $b_j$ be the dimension of the singular homology $H_j(M; \mathbb{R})$ (taken to be $0$
if infinite). Then for every $k \in \mathbb{N}$,

$$\sum_{j=0}^{k} (-1)^{k-j} b_j \le \sum_{j=0}^{k} (-1)^{k-j} c_j.$$

## Sources

- M. Morse, The Calculus of Variations in the Large, AMS Colloq. Publ. 18 (1934). Listed as §40 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `morse_inequality` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.MorseInequalitiesWanted.Geometry.MorseInequalities.morse_inequality` is written with `theorem_wanted` in [WantedExt/Geometry/MorseInequalitiesWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MorseInequalitiesWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html#morse-inequality).

## Weak Morse inequalities

Let $M$ be a compact Hausdorff smooth ($C^\infty$) manifold
without boundary, modelled on a finite-dimensional real normed space, and let
$f \colon M \to \mathbb{R}$ be a Morse function, that is, a smooth function with finitely many
critical points, all of them non-degenerate. Then for every $k \in \mathbb{N}$ the $k$-th Betti
number of $M$, the real dimension of the singular homology $H_k(M; \mathbb{R})$, is at most the
number of critical points of $f$ of Morse index $k$.

## Sources

- M. Morse, The Calculus of Variations in the Large, AMS Colloq. Publ. 18 (1934). Listed as §40 additional statement in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `weak_morse_inequality` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.WeakMorseInequalityWanted.Geometry.WeakMorseInequality.weak_morse_inequality` is written with `theorem_wanted` in [WantedExt/Geometry/WeakMorseInequalityWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/WeakMorseInequalityWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html#weak-morse-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Morse theory](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/morse-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/differential-topology/morse-theory)
