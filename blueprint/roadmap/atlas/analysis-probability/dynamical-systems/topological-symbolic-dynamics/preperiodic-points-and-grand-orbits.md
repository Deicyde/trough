---
declaration: section
origin: cited
lean: Function.forwardOrbit, Function.IsPreperiodicPt, Function.IsStrictlyPreperiodicPt, Function.IsPreperiodicPtOfType, Function.GrandOrbitRel, Function.grandOrbitSetoid, Function.grandOrbit
statement: formalized
proof: formalized
---

# Preperiodic points and grand orbits

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/preperiodic-points-and-grand-orbits/index.html).

## Forward orbit

For a self-map $f$ of a set $X$ and a point $x \in X$, the forward orbit
of $x$ under $f$ is the set $\{f^n(x) : n \in \mathbb{N}\}$ of all iterates of $x$, including
$f^0(x) = x$.

Formalized by `Function.forwardOrbit`, a definition declared in [MathlibExt/Dynamics/Preperiodic.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Preperiodic.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/preperiodic-points-and-grand-orbits/index.html#forward-orbit).

## Preperiodic point

A point $x$ is preperiodic for a self-map $f$ when its forward orbit
$\{f^n(x) : n \in \mathbb{N}\}$ under $f$ is a finite set.

Formalized by `Function.IsPreperiodicPt`, a definition declared in [MathlibExt/Dynamics/Preperiodic.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Preperiodic.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/preperiodic-points-and-grand-orbits/index.html#is-preperiodic-pt).

## Strictly preperiodic point

A point $x$ is strictly preperiodic for a self-map $f$ when it
is preperiodic for $f$ but not periodic, that is, there is no $n > 0$ with $f^n(x) = x$.

Formalized by `Function.IsStrictlyPreperiodicPt`, a definition declared in [MathlibExt/Dynamics/Preperiodic.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Preperiodic.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/preperiodic-points-and-grand-orbits/index.html#is-strictly-preperiodic-pt).

## Preperiodic point of a given type

Let $f$ be a self-map of a set $X$ and let $m$ and $n$
be natural numbers. A point $x \in X$ is preperiodic of type $(m, n)$ when $n > 0$ and
$f^{m+n}(x) = f^m(x)$, that is, $f^m(x)$ is periodic with period $n$. Neither $m$ nor $n$ is
required to be minimal.

Formalized by `Function.IsPreperiodicPtOfType`, a definition declared in [MathlibExt/Dynamics/Preperiodic.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Preperiodic.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/preperiodic-points-and-grand-orbits/index.html#is-preperiodic-pt-of-type).

## Grand orbit relation

For a self-map $f$ of a set $X$, points $x, y \in X$ are related,
that is, lie in the same grand orbit of $f$, when $f^m(x) = f^n(y)$ for some natural numbers
$m$ and $n$.

Formalized by `Function.GrandOrbitRel`, a definition declared in [MathlibExt/Dynamics/Preperiodic.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Preperiodic.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/preperiodic-points-and-grand-orbits/index.html#grand-orbit-rel).

## Grand orbit equivalence relation

For a self-map $f$ of a set $X$, the relation on $X$ in
which $x \sim y$ when $f^m(x) = f^n(y)$ for some natural numbers $m$ and $n$ is an equivalence
relation; its equivalence classes are the grand orbits of $f$.

Formalized by `Function.grandOrbitSetoid`, a definition declared in [MathlibExt/Dynamics/Preperiodic.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Preperiodic.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/preperiodic-points-and-grand-orbits/index.html#grand-orbit-setoid).

## Grand orbit

For a self-map $f$ of a set $X$ and a point $x \in X$, the grand orbit of $x$
is the set of all $y \in X$ such that $f^m(x) = f^n(y)$ for some natural numbers $m$ and $n$,
that is, the equivalence class of $x$ under the grand orbit relation.

Formalized by `Function.grandOrbit`, a definition declared in [MathlibExt/Dynamics/Preperiodic.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Preperiodic.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/preperiodic-points-and-grand-orbits/index.html#grand-orbit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Preperiodic points and grand orbits](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/preperiodic-points-and-grand-orbits/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/topological-symbolic-dynamics/preperiodic-points-and-grand-orbits)
