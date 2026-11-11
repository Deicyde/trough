---
declaration: section
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.ofLE, Bundle.ContMDiffRiemannianMetric.ofLE_inner, Bundle.ContMDiffRiemannianMetric.conformalScale, Bundle.ContMDiffRiemannianMetric.conformalScale_inner_apply, Bundle.ContMDiffRiemannianMetric.pos_of_inner_eq_mul, Manifold.conformalClass, Manifold.mem_conformalClass_iff_exp, Manifold.self_mem_conformalClass
statement: formalized
proof: formalized
---

# Conformal classes of Riemannian metrics

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html).

## Bundle

## Lowering the smoothness of a Riemannian metric

Let $E$ be a real vector bundle over a
manifold $B$, let $m \le n$ be smoothness exponents in $\mathbb{N} \cup \{\infty, \omega\}$, and
let $g$ be a $C^n$ Riemannian metric on $E$. Then $g$, with the same inner product on every
fiber, is a $C^m$ Riemannian metric on $E$.

Formalized by `Bundle.ContMDiffRiemannianMetric.ofLE`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html#of-le).

## Lowering the smoothness keeps the inner product

Let $E$ be a real vector bundle over a
manifold $B$, let $m \le n$ be smoothness exponents in $\mathbb{N} \cup \{\infty, \omega\}$, and
let $g$ be a $C^n$ Riemannian metric on $E$. For every $b \in B$, the inner product on the fiber
$E_b$ of $g$ viewed as a $C^m$ Riemannian metric equals the inner product of $g$ on $E_b$.

Formalized by `Bundle.ContMDiffRiemannianMetric.ofLE_inner`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html#of-le-inner).

## Conformal scaling of a Riemannian metric

Let $E$ be a real vector bundle over a
manifold $B$, let $n \in \mathbb{N} \cup \{\infty, \omega\}$, let $g$ be a $C^n$ Riemannian
metric on $E$, and let $u : B \to \mathbb{R}$ be a $C^n$ function with $u(b) > 0$ for every
$b \in B$. The conformal scaling of $g$ by $u$ is the $C^n$ Riemannian metric $u g$ on $E$
whose inner product on each fiber $E_b$ is $u(b)$ times the inner product of $g$ on $E_b$.

Formalized by `Bundle.ContMDiffRiemannianMetric.conformalScale`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html#conformal-scale).

## Inner product of a conformally scaled metric

Let $E$ be a real vector bundle over a
manifold $B$, let $n \in \mathbb{N} \cup \{\infty, \omega\}$, let $g$ be a $C^n$ Riemannian
metric on $E$, with inner product $g_b$ on the fiber $E_b$, and let $u : B \to \mathbb{R}$ be a
$C^n$ function with $u(b) > 0$ for every $b \in B$. Then the conformal scaling $u g$ of $g$ by
$u$ satisfies $(u g)_b(v, w) = u(b)\, g_b(v, w)$ for every $b \in B$ and all $v, w \in E_b$.

Formalized by `Bundle.ContMDiffRiemannianMetric.conformalScale_inner_apply`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html#conformal-scale-inner-apply).

## A conformal factor at a point is positive

Let $E$ be a real vector bundle over a
manifold $B$, let $n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $g$ and $g'$ be $C^n$
Riemannian metrics on $E$, with inner products $g_b$ and $g'_b$ on the fiber $E_b$. Let
$u : B \to \mathbb{R}$ and $b \in B$. If $g'_b(v, w) = u(b)\, g_b(v, w)$ for all $v, w \in E_b$
and $E_b$ contains a nonzero vector, then $u(b) > 0$.

Formalized by `Bundle.ContMDiffRiemannianMetric.pos_of_inner_eq_mul`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html#pos-of-inner-eq-mul).

## Conformal class of a Riemannian metric

Let $M$ be a $C^\infty$ manifold modeled on a
real normed space, and let $g$ be a $C^\infty$ Riemannian metric on $M$, with inner product $g_x$
on the tangent space $T_x M$. The conformal class of $g$ is the set of $C^\infty$ Riemannian
metrics $g'$ on $M$ for which there is a $C^\infty$ function $u : M \to \mathbb{R}$ with
$u(x) > 0$ for all $x \in M$ and $g'_x(v, w) = u(x)\, g_x(v, w)$ for all $x \in M$ and all
$v, w \in T_x M$.

Formalized by `Manifold.conformalClass`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html#conformal-class).

## Conformal metrics via an exponential factor

Let $M$ be a $C^\infty$ manifold modeled on
a real normed space, and let $g$ and $g'$ be $C^\infty$ Riemannian metrics on $M$, with inner
products $g_x$ and $g'_x$ on the tangent space $T_x M$. Then $g'$ lies in the conformal class of
$g$ if and only if there is a $C^\infty$ function $f : M \to \mathbb{R}$ with
$g'_x(v, w) = e^{f(x)}\, g_x(v, w)$ for all $x \in M$ and all $v, w \in T_x M$.

Formalized by `Manifold.mem_conformalClass_iff_exp`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html#mem-conformal-class-iff-exp).

## A metric lies in its own conformal class

Every smooth Riemannian metric $g$ on a
smooth manifold $M$ lies in the conformal class of $g$.

Formalized by `Manifold.self_mem_conformalClass`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html#self-mem-conformal-class).

## Conformal scalings lie in the conformal class

Let $M$ be a $C^\infty$ manifold modeled
on a real normed space, let $g$ be a $C^\infty$ Riemannian metric on $M$, and let
$u : M \to \mathbb{R}$ be a $C^\infty$ function with $u(x) > 0$ for all $x \in M$. Then the
conformal scaling $u g$ of $g$ by $u$ lies in the conformal class of $g$.

Formalized by `Manifold.conformalScale_mem_conformalClass`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html#conformal-scale-mem-conformal-class).

## Conformal equivalence is symmetric

Let $M$ be a $C^\infty$ manifold modeled on a real
normed space, and let $g$ and $g'$ be $C^\infty$ Riemannian metrics on $M$. If $g'$ lies in the
conformal class of $g$, then $g$ lies in the conformal class of $g'$.

Formalized by `Manifold.mem_conformalClass_symm`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html#mem-conformal-class-symm).

## Conformal equivalence is transitive

Let $M$ be a $C^\infty$ manifold modeled on a real
normed space, and let $g$, $g'$ and $g''$ be $C^\infty$ Riemannian metrics on $M$. If $g'$ lies
in the conformal class of $g$ and $g''$ lies in the conformal class of $g'$, then $g''$ lies in
the conformal class of $g$.

Formalized by `Manifold.mem_conformalClass_trans`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Conformal.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html#mem-conformal-class-trans).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conformal classes of Riemannian metrics](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/riemannian-geometry/conformal-classes-of-riemannian-metrics)
