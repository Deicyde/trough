---
declaration: section
origin: cited
lean: MetaMathlibExt.angle_trisection_impossible
statement: formalized
proof: formalized
---

# Foundations and constructions: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/foundations-and-constructions/index.html).

Axiom systems for plane geometry and the limits of compass-and-straightedge constructions.

## Impossibility of angle trisection

Let "constructible" be any property of real numbers such
that a real number $x$ is constructible exactly when there are $n \ge 0$ and subfields
$K_0 \subseteq K_1 \subseteq \dots \subseteq K_n$ of $\mathbb{R}$ with $K_0 = \mathbb{Q}$ (the
smallest subfield of $\mathbb{R}$), $x \in K_n$, and, for each $i < n$, some $b \in K_{i+1}$ with
$b^2 \in K_i$ such that every element of $K_{i+1}$ equals $u + bv$ for some $u, v \in K_i$. Let
an angle $\theta$ be constructible exactly when $\cos \theta$ is constructible. Then the polynomial
$8X^3 - 6X - 1$ is irreducible over $\mathbb{Q}$, $\cos(\pi/9)$ is a root of it, $\cos(\pi/9)$ is
not constructible, and it is not true that $\theta / 3$ is a constructible angle for every
constructible angle $\theta$.

In particular the $60^\circ$ angle, whose cosine $1/2$ is constructible, cannot be trisected: by
the triple-angle formula, $\cos 20^\circ = \cos(\pi/9)$ is a root of $8X^3 - 6X - 1$.

## Sources

- https://en.wikipedia.org/wiki/Angle_trisection.

Formalized by `MetaMathlibExt.angle_trisection_impossible`, a theorem declared in [MathlibExt/Geometry/Euclidean/AngleTrisectionImpossible.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/AngleTrisectionImpossible.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/foundations-and-constructions/index.html#angle-trisection-impossible).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Foundations and constructions](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/foundations-and-constructions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/euclidean-geometry/foundations-and-constructions)
