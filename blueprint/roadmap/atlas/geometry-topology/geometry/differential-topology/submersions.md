---
declaration: section
origin: cited
lean: Manifold.IsSubmersionAtOfComplement.exists_domChart_of_codChart, Manifold.IsSubmersionAtOfComplement.comp, Manifold.IsSubmersionAt.comp, Manifold.IsSubmersionOfComplement.comp, Manifold.IsSubmersion.comp, MathlibExt.Geometry.Manifold.SubmersionCompWanted.submersionAt_comp, MathlibExt.Geometry.Manifold.SubmersionCompWanted.submersion_comp, Manifold.IsSubmersionAt.of_surjective_mfderiv
statement: formalized
proof: formalized
---

# Submersions

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/submersions/index.html).

## Changing the target chart of a submersion at a point

Let $\mathbb{K}$ be a nontrivially
normed field, let $n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$ and $N$ be charted spaces
modelled, through models with corners, on normed spaces $E$ and $E''$ over $\mathbb{K}$, both
models without boundary. Let $f : M \to N$ be a $C^n$ submersion at $x \in M$ with complement $F$,
and let $e : E \to E'' \times F$ be the continuous linear equivalence chosen for it. Then for every
chart $\psi$ of $N$ in the $C^n$ maximal atlas with $f(x)$ in its domain there is a chart
$\varphi$ of $M$ in the $C^n$ maximal atlas with $x$ in its domain, such that $f$ maps the domain
of $\varphi$ into the domain of $\psi$ and
$\hat\psi \circ f \circ \hat\varphi^{-1} = \mathrm{pr}_1 \circ e$ on the image of $\hat\varphi$,
where $\hat\varphi$ and $\hat\psi$ denote the charts followed by the models with corners.

Here $f$ is a $C^n$ submersion at $x$ with complement $F$ (a normed space over $\mathbb{K}$) when
there are charts of $M$ around $x$ and of $N$ around $f(x)$ in the $C^n$ maximal atlases, the
first mapped by $f$ into the second, in which $f$ reads $\mathrm{pr}_1 \circ e$ on the image of
the first, for some continuous linear equivalence $e : E \to E'' \times F$; a witness of this
fixes one such $e$.

Formalized by `Manifold.IsSubmersionAtOfComplement.exists_domChart_of_codChart`, a theorem declared in [MathlibExt/Geometry/Manifold/SubmersionComp.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/SubmersionComp.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/submersions/index.html#exists-dom-chart-of-cod-chart).

## Composition of submersions at a point with chosen complements

Let $\mathbb{K}$ be a
nontrivially normed field, let $n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$, $N$, $N'$
be charted spaces modelled, through models with corners, on normed spaces $E$, $E''$, $E'''$ over
$\mathbb{K}$, where the models of $M$ and $N$ have no boundary. Let $F_1$ and $F_2$ be normed
spaces over $\mathbb{K}$. If $f : M \to N$ is a $C^n$ submersion at $x \in M$ with complement
$F_1$ and $g : N \to N'$ is a $C^n$ submersion at $f(x)$ with complement $F_2$, then
$g \circ f$ is a $C^n$ submersion at $x$ with complement $F_2 \times F_1$.

Here $f$ is a $C^n$ submersion at $x$ with complement $F$ when there are charts $\varphi$ of $M$
around $x$ and $\psi$ of $N$ around $f(x)$ in the $C^n$ maximal atlases, with $f$ mapping the
domain of $\varphi$ into the domain of $\psi$, and a continuous linear equivalence
$e : E \to E'' \times F$ such that
$\hat\psi \circ f \circ \hat\varphi^{-1} = \mathrm{pr}_1 \circ e$ on the image of $\hat\varphi$,
where $\hat\varphi$ and $\hat\psi$ denote the charts followed by the models with corners.

Formalized by `Manifold.IsSubmersionAtOfComplement.comp`, a theorem declared in [MathlibExt/Geometry/Manifold/SubmersionComp.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/SubmersionComp.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/submersions/index.html#comp).

## Submersions at a point are closed under composition

Let $\mathbb{K}$ be a nontrivially
normed field, let $n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$, $N$, $N'$ be charted
spaces modelled, through models with corners, on normed spaces $E$, $E''$, $E'''$ over
$\mathbb{K}$, where the models of $M$ and $N$ have no boundary. If $f : M \to N$ is a $C^n$
submersion at $x \in M$ and $g : N \to N'$ is a $C^n$ submersion at $f(x)$, then $g \circ f$ is a
$C^n$ submersion at $x$.

Here $f$ is a $C^n$ submersion at $x$ when, for some normed space $F$ over $\mathbb{K}$, there are
charts $\varphi$ of $M$ around $x$ and $\psi$ of $N$ around $f(x)$ in the $C^n$ maximal atlases,
with $f$ mapping the domain of $\varphi$ into the domain of $\psi$, and a continuous linear
equivalence $e : E \to E'' \times F$ such that
$\hat\psi \circ f \circ \hat\varphi^{-1} = \mathrm{pr}_1 \circ e$ on the image of $\hat\varphi$,
where $\hat\varphi$ and $\hat\psi$ denote the charts followed by the models with corners.

Formalized by `Manifold.IsSubmersionAt.comp`, a theorem declared in [MathlibExt/Geometry/Manifold/SubmersionComp.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/SubmersionComp.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/submersions/index.html#comp-2).

## Composition of submersions with chosen complements

Let $\mathbb{K}$ be a nontrivially
normed field, let $n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$, $N$, $N'$ be charted
spaces modelled, through models with corners, on normed spaces $E$, $E''$, $E'''$ over
$\mathbb{K}$, where the models of $M$ and $N$ have no boundary. Let $F_1$ and $F_2$ be normed
spaces over $\mathbb{K}$. If $f : M \to N$ is a $C^n$ submersion with complement $F_1$ and
$g : N \to N'$ is a $C^n$ submersion with complement $F_2$, then $g \circ f$ is a $C^n$
submersion with complement $F_2 \times F_1$.

Here $f$ is a $C^n$ submersion with complement $F$ when at every $x \in M$ there are charts
$\varphi$ of $M$ around $x$ and $\psi$ of $N$ around $f(x)$ in the $C^n$ maximal atlases, with
$f$ mapping the domain of $\varphi$ into the domain of $\psi$, and a continuous linear
equivalence $e : E \to E'' \times F$ such that
$\hat\psi \circ f \circ \hat\varphi^{-1} = \mathrm{pr}_1 \circ e$ on the image of $\hat\varphi$,
where $\hat\varphi$ and $\hat\psi$ denote the charts followed by the models with corners.

Formalized by `Manifold.IsSubmersionOfComplement.comp`, a theorem declared in [MathlibExt/Geometry/Manifold/SubmersionComp.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/SubmersionComp.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/submersions/index.html#comp-3).

## Submersions are closed under composition

Let $\mathbb{K}$ be a nontrivially normed
field, let $n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$, $N$, $N'$ be charted spaces
modelled, through models with corners, on normed spaces $E$, $E''$, $E'''$ over $\mathbb{K}$,
where the models of $M$ and $N$ have no boundary. If $f : M \to N$ and $g : N \to N'$ are $C^n$
submersions, then so is $g \circ f$.

Here $f$ is a $C^n$ submersion when there is one normed space $F$ over $\mathbb{K}$ such that at
every $x \in M$ there are charts $\varphi$ of $M$ around $x$ and $\psi$ of $N$ around $f(x)$ in
the $C^n$ maximal atlases, with $f$ mapping the domain of $\varphi$ into the domain of $\psi$, and
a continuous linear equivalence $e : E \to E'' \times F$ such that
$\hat\psi \circ f \circ \hat\varphi^{-1} = \mathrm{pr}_1 \circ e$ on the image of $\hat\varphi$,
where $\hat\varphi$ and $\hat\psi$ denote the charts followed by the models with corners.

Formalized by `Manifold.IsSubmersion.comp`, a theorem declared in [MathlibExt/Geometry/Manifold/SubmersionComp.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/SubmersionComp.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/submersions/index.html#comp-4).

## Composition of submersions at a point

Let $\mathbb{K}$ be a nontrivially normed field, let
$n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$, $N$, $N'$ be $C^n$ manifolds without
boundary over $\mathbb{K}$ modelled on Banach spaces. If $f : M \to N$ is a $C^n$ submersion at
$x \in M$ and $g : N \to N'$ is a $C^n$ submersion at $f(x)$, then $g \circ f$ is a $C^n$
submersion at $x$. Here $f$ is a $C^n$ submersion at $x$ when there are charts of the $C^n$
maximal atlases around $x$ and $f(x)$, the first mapped by $f$ into the second, in which $f$ reads
$(u, v) \mapsto u$ after a continuous linear identification of the model space of $M$ with the
product of the model space of $N$ and some normed space.

Proof: Replace the first submersion's target chart by the second submersion's source chart, then
compose the two projection normal forms and use the product of their complements.

## Sources

- J. Lee, Introduction to Smooth Manifolds, 2nd ed., Ch. 4.

Formalized by `MathlibExt.Geometry.Manifold.SubmersionCompWanted.submersionAt_comp`, a theorem declared in [MathlibExt/Geometry/Manifold/SubmersionComp.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/SubmersionComp.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/submersions/index.html#submersion-at-comp).

## Composition of submersions

Let $\mathbb{K}$ be a nontrivially normed field, let
$n \in \mathbb{N} \cup \{\infty, \omega\}$, and let $M$, $N$, $N'$ be $C^n$ manifolds without
boundary over $\mathbb{K}$ modelled on Banach spaces. If $f : M \to N$ and $g : N \to N'$ are
$C^n$ submersions, then so is $g \circ f$. Here $f$ is a $C^n$ submersion when there is one normed
space $F$ such that at every $x \in M$ there are charts of the $C^n$ maximal atlases around $x$ and
$f(x)$, the first mapped by $f$ into the second, in which $f$ reads $(u, v) \mapsto u$ after a
continuous linear identification of the model space of $M$ with the product of the model space of
$N$ and $F$.

Proof: Apply the complement-level pointwise composition theorem using the two fixed global
complements, then package their product as the complement of the composite.

## Sources

- J. Lee, Introduction to Smooth Manifolds, 2nd ed., Ch. 4.

Formalized by `MathlibExt.Geometry.Manifold.SubmersionCompWanted.submersion_comp`, a theorem declared in [MathlibExt/Geometry/Manifold/SubmersionComp.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/SubmersionComp.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/submersions/index.html#submersion-comp).

## Surjective differential into a finite-dimensional manifold gives a submersion

Let
$\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let $n \in \mathbb{N} \cup \{\infty, \omega\}$ with
$n \ge 1$, let $M$ be a $C^n$ manifold without boundary over $\mathbb{K}$ modelled on a Banach
space, and let $N$ be a $C^n$ manifold, possibly with boundary or corners, over $\mathbb{K}$
modelled on a finite-dimensional space. If $f : M \to N$ is $C^n$ at every point of some
neighbourhood of $x \in M$ and the manifold derivative of $f$ at $x$ is surjective, then $f$ is a
$C^n$ submersion at $x$: there are charts of the $C^n$ maximal atlases around $x$ and $f(x)$, the
first mapped by $f$ into the second, in which $f$ reads $(u, v) \mapsto u$ after a continuous linear
identification of the model space of $M$ with the product of the model space of $N$ and some
normed space.

Formalized by `Manifold.IsSubmersionAt.of_surjective_mfderiv`, a theorem declared in [MathlibExt/Geometry/Manifold/SubmersionOfSurjectiveMFDeriv.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/SubmersionOfSurjectiveMFDeriv.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/submersions/index.html#of-surjective-mfderiv).

## Surjective differential gives a submersion between finite-dimensional manifolds

Let
$\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let $n \in \mathbb{N} \cup \{\infty, \omega\}$ with
$n \ge 1$, and let $M$ and $N$ be $C^n$ manifolds without boundary over $\mathbb{K}$ modelled on
finite-dimensional spaces. If $f : M \to N$ is $C^n$ at every point of some neighbourhood of
$x \in M$ and the manifold derivative of $f$ at $x$ is surjective, then $f$ is a $C^n$ submersion
at $x$: there are charts of the $C^n$ maximal atlases around $x$ and $f(x)$, the first mapped by
$f$ into the second, in which $f$ reads $(u, v) \mapsto u$ after a linear identification of the
model space of $M$ with the product of the model space of $N$ and some normed space.

Proof: Split the surjective derivative, augment the map by its kernel coordinate, and apply the
inverse function theorem to obtain charts in which the map is the first projection.

## Sources

- J. Lee, Introduction to Smooth Manifolds, 2nd ed., Ch. 4.

Formalized by `MathlibExt.Geometry.Manifold.SubmersionOfSurjectiveMFDerivWanted.submersionAt_of_surjective_mfderiv`, a theorem declared in [MathlibExt/Geometry/Manifold/SubmersionOfSurjectiveMFDeriv.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/SubmersionOfSurjectiveMFDeriv.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/submersions/index.html#submersion-at-of-surjective-mfderiv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Submersions](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/submersions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/differential-topology/submersions)
