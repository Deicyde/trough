---
declaration: section
origin: cited
lean: Manifold.IsImmersionAtOfComplement.comp, Manifold.IsImmersionAt.comp, Manifold.IsImmersionOfComplement.comp, Manifold.IsImmersion.comp, MathlibExt.Geometry.Manifold.ImmersionCompWanted.immersionAt_comp, MathlibExt.Geometry.Manifold.ImmersionCompWanted.immersion_comp, Manifold.IsImmersionAt.of_injective_mfderiv_of_closedComplemented_range, MathlibExt.Geometry.Manifold.ImmersionOfInjectiveMFDerivWanted.immersionAt_of_injective_mfderiv
statement: formalized
proof: formalized
---

# Immersions

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/immersions/index.html).

## Composition of immersions at a point with fixed complements

Let $\mathbb{K}$ be a
nontrivially normed field, let $n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$, $N$, $N'$
be charted spaces modelled through models with corners on normed spaces over $\mathbb{K}$, where
the models of $N$ and $N'$ are boundaryless. Let $F_1$ and $F_2$ be normed spaces over
$\mathbb{K}$. If $f : M \to N$ is a $C^n$ immersion at a point $x \in M$ with complement $F_1$
and $g : N \to N'$ is a $C^n$ immersion at $f(x)$ with complement $F_2$, then $g \circ f$ is a
$C^n$ immersion at $x$ with complement $F_1 \times F_2$.

Here a map is a $C^n$ immersion at a point with complement $F$ when there are charts of the
maximal $C^n$ atlases around the point and its image, the first mapped by the map into the
second, in which the map reads $u \mapsto \varphi(u, 0)$ for a continuous linear isomorphism
$\varphi$ from the product of the source model space with $F$ onto the target model space.

Formalized by `Manifold.IsImmersionAtOfComplement.comp`, a theorem declared in [MathlibExt/Geometry/Manifold/ImmersionComp.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/ImmersionComp.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/immersions/index.html#comp).

## Composition of immersions at a point over boundaryless models

Let $\mathbb{K}$ be a
nontrivially normed field, let $n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$, $N$, $N'$
be charted spaces modelled through models with corners on normed spaces over $\mathbb{K}$, where
the models of $N$ and $N'$ are boundaryless. If $f : M \to N$ is a $C^n$ immersion at a point
$x \in M$ and $g : N \to N'$ is a $C^n$ immersion at $f(x)$, then $g \circ f$ is a $C^n$
immersion at $x$.

Here a map is a $C^n$ immersion at a point when, for some normed space $F$ over $\mathbb{K}$,
there are charts of the maximal $C^n$ atlases around the point and its image, the first mapped by
the map into the second, in which the map reads $u \mapsto \varphi(u, 0)$ for a continuous linear
isomorphism $\varphi$ from the product of the source model space with $F$ onto the target model
space.

Formalized by `Manifold.IsImmersionAt.comp`, a theorem declared in [MathlibExt/Geometry/Manifold/ImmersionComp.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/ImmersionComp.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/immersions/index.html#comp-2).

## Composition of immersions with fixed complements

Let $\mathbb{K}$ be a nontrivially normed
field, let $n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$, $N$, $N'$ be charted spaces
modelled through models with corners on normed spaces over $\mathbb{K}$, where the models of $N$
and $N'$ are boundaryless. Let $F_1$ and $F_2$ be normed spaces over $\mathbb{K}$. If
$f : M \to N$ is a $C^n$ immersion with complement $F_1$ and $g : N \to N'$ is a $C^n$ immersion
with complement $F_2$, then $g \circ f$ is a $C^n$ immersion with complement $F_1 \times F_2$.

Here a map is a $C^n$ immersion with complement $F$ when for every point there are charts of the
maximal $C^n$ atlases around the point and its image, the first mapped by the map into the
second, in which the map reads $u \mapsto \varphi(u, 0)$ for a continuous linear isomorphism
$\varphi$ from the product of the source model space with $F$ onto the target model space.

Formalized by `Manifold.IsImmersionOfComplement.comp`, a theorem declared in [MathlibExt/Geometry/Manifold/ImmersionComp.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/ImmersionComp.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/immersions/index.html#comp-3).

## Composition of immersions over boundaryless models

Let $\mathbb{K}$ be a nontrivially
normed field, let $n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$, $N$, $N'$ be charted
spaces modelled through models with corners on normed spaces over $\mathbb{K}$, where the models
of $N$ and $N'$ are boundaryless. If $f : M \to N$ and $g : N \to N'$ are $C^n$ immersions, then
$g \circ f$ is a $C^n$ immersion.

Here a map is a $C^n$ immersion when there is a normed space $F$ over $\mathbb{K}$ such that for
every point there are charts of the maximal $C^n$ atlases around the point and its image, the
first mapped by the map into the second, in which the map reads $u \mapsto \varphi(u, 0)$ for a
continuous linear isomorphism $\varphi$ from the product of the source model space with $F$ onto
the target model space.

Formalized by `Manifold.IsImmersion.comp`, a theorem declared in [MathlibExt/Geometry/Manifold/ImmersionComp.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/ImmersionComp.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/immersions/index.html#comp-4).

## Composition of immersions at a point

Let $\mathbb{K}$ be a nontrivially normed field, let
$n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$, $N$, $N'$ be $C^n$ manifolds without
boundary modeled on Banach spaces over $\mathbb{K}$. If $f : M \to N$ is a $C^n$ immersion at a
point $x \in M$ and $g : N \to N'$ is a $C^n$ immersion at $f(x)$, then $g \circ f$ is a $C^n$
immersion at $x$.

Here a map is a $C^n$ immersion at a point when, in suitable charts around the point and its
image, it reads $u \mapsto \varphi(u, 0)$ for a continuous linear isomorphism
$\varphi : E \times F \to E'$, where $E$ and $E'$ are the model spaces of the source and target
and $F$ is some normed space over $\mathbb{K}$.

Proof: Restrict the first immersion's codomain chart to the second immersion's domain chart, then
conjugate that chart transition through the second linear normal form. The normal forms compose
with the product of their complements.

## Sources

- J. Lee, Introduction to Smooth Manifolds, 2nd ed., Ch. 4.

Formalized by `MathlibExt.Geometry.Manifold.ImmersionCompWanted.immersionAt_comp`, a theorem declared in [MathlibExt/Geometry/Manifold/ImmersionComp.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/ImmersionComp.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/immersions/index.html#immersion-at-comp).

## Composition of immersions

Let $\mathbb{K}$ be a nontrivially normed field, let
$n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$, $N$, $N'$ be $C^n$ manifolds without
boundary modeled on Banach spaces over $\mathbb{K}$. If $f : M \to N$ and $g : N \to N'$ are
$C^n$ immersions, then $g \circ f$ is a $C^n$ immersion.

Here a map is a $C^n$ immersion when there is a normed space $F$ over $\mathbb{K}$ such that
around every point, in suitable charts around the point and its image, the map reads
$u \mapsto \varphi(u, 0)$ for some continuous linear isomorphism $\varphi : E \times F \to E'$,
where $E$ and $E'$ are the model spaces of the source and target.

Proof: Apply the pointwise composition construction using the product of the two global
complements, then package the resulting fixed-complement immersion.

## Sources

- J. Lee, Introduction to Smooth Manifolds, 2nd ed., Ch. 4.

Formalized by `MathlibExt.Geometry.Manifold.ImmersionCompWanted.immersion_comp`, a theorem declared in [MathlibExt/Geometry/Manifold/ImmersionComp.lean, line 492](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/ImmersionComp.lean#L492). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/immersions/index.html#immersion-comp).

## Injective differential with complemented range gives an immersion

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $n \ge 1$ be a smoothness degree (possibly $\infty$ or
$\omega$), and let $M$ and $N$ be $C^n$ manifolds without boundary over $\mathbb{K}$, modelled on
Banach spaces $E$ and $E'$. Let $f \colon M \to N$ be $C^n$ at every point of some neighbourhood
of a point $x \in M$, and suppose that its differential $df_x \colon E \to E'$ is injective and
that there is a continuous linear projection of $E'$ onto the range of $df_x$. Then $f$ is a
$C^n$ immersion at $x$.

Formalized by `Manifold.IsImmersionAt.of_injective_mfderiv_of_closedComplemented_range`, a theorem declared in [MathlibExt/Geometry/Manifold/ImmersionOfInjectiveMFDeriv.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/ImmersionOfInjectiveMFDeriv.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/immersions/index.html#of-injective-mfderiv-of-closed-complemen).

## Injective differential gives an immersion

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $n \ge 1$ be a smoothness degree (possibly $\infty$ or $\omega$), and let
$M$ and $N$ be $C^n$ manifolds without boundary over $\mathbb{K}$, modelled on
finite-dimensional normed $\mathbb{K}$-vector spaces. If a map $f \colon M \to N$ is $C^n$ at
every point of some neighbourhood of a point $x \in M$ and its differential $df_x$ at $x$ is
injective, then $f$ is a $C^n$ immersion at $x$.

Proof: Choose a complement to the differential's range, apply the inverse function theorem to
the resulting product map in extended charts, and use its local inverse as a target chart.

## Sources

- J. Lee, Introduction to Smooth Manifolds, 2nd ed., Ch. 4.

Formalized by `MathlibExt.Geometry.Manifold.ImmersionOfInjectiveMFDerivWanted.immersionAt_of_injective_mfderiv`, a theorem declared in [MathlibExt/Geometry/Manifold/ImmersionOfInjectiveMFDeriv.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/ImmersionOfInjectiveMFDeriv.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/immersions/index.html#immersion-at-of-injective-mfderiv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Immersions](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/immersions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/differential-topology/immersions)
