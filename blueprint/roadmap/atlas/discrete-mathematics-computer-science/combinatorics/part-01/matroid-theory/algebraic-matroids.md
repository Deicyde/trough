---
declaration: section
origin: cited
lean: Matroid.AlgebraicRepresentation, Matroid.IsAlgebraicOver, Matroid.AlgebraicRepresentationSomeField, Matroid.IsAlgebraic, Matroid.AlgebraicRepresentation.toIsAlgebraicOver, Matroid.AlgebraicRepresentationSomeField.toIsAlgebraic
statement: formalized
proof: formalized
---

# Algebraic matroids

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/algebraic-matroids/index.html).

## Algebraic representation of a matroid

Let $K$ be a field and $M$ a matroid on a type $E$.
An algebraic representation of $M$ over $K$ consists of a field extension $L$ of $K$ and a map
$\varphi \colon E \to L$ such that $L$ is generated over $K$ by the image under $\varphi$ of the
ground set of $M$, and a set $I$ is independent in $M$ exactly when $I$ is contained in the ground
set of $M$, $\varphi$ is injective on $I$, and $\varphi(I)$ is algebraically independent over
$K$.

Formalized by `Matroid.AlgebraicRepresentation`, a structure declared in [MathlibExt/Combinatorics/Matroid/Algebraic.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Matroid/Algebraic.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/algebraic-matroids/index.html#algebraic-representation).

## Algebraic matroid over a field

Let $K$ be a field. A matroid $M$ on a type $E$ is
algebraic over $K$ if it has an algebraic representation over $K$ whose extension field lies in
the larger of the universes of $K$ and $E$.

Universe encoding: Lean fixes universes, so the witness extension is required to live in a
universe holding both $K$ and $E$.

Formalized by `Matroid.IsAlgebraicOver`, a definition declared in [MathlibExt/Combinatorics/Matroid/Algebraic.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Matroid/Algebraic.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/algebraic-matroids/index.html#is-algebraic-over).

## Algebraic representation of a matroid over some field

Let $M$ be a matroid on a type
$E$. An algebraic representation of $M$ over some field consists of a field $K$, a field extension
$L$ of $K$ and a map $\varphi \colon E \to L$ such that $L$ is generated over $K$ by the image
under $\varphi$ of the ground set of $M$, and a set $I$ is independent in $M$ exactly when $I$ is
contained in the ground set of $M$, $\varphi$ is injective on $I$, and $\varphi(I)$ is
algebraically independent over $K$.

Universe encoding: both $K$ and $L$ lie in the same universe as $E$, so matroids on $E$ need no
larger universes.

Formalized by `Matroid.AlgebraicRepresentationSomeField`, a structure declared in [MathlibExt/Combinatorics/Matroid/Algebraic.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Matroid/Algebraic.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/algebraic-matroids/index.html#algebraic-representation-some-field).

## Algebraic matroid

A matroid $M$ on a type $E$ is algebraic if it has an algebraic
representation over some field whose base field and extension field lie in the same universe
as $E$.

Universe encoding: this is the universe-local form of algebraicity for matroids on $E$.

Formalized by `Matroid.IsAlgebraic`, a definition declared in [MathlibExt/Combinatorics/Matroid/Algebraic.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Matroid/Algebraic.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/algebraic-matroids/index.html#is-algebraic).

## Algebraic representations witness algebraicity over a field

Let $K$ be a field and $M$
a matroid on a type $E$. If $M$ has an algebraic representation over $K$ whose extension field
lies in the larger of the universes of $K$ and $E$, then $M$ is algebraic over $K$.

Formalized by `Matroid.AlgebraicRepresentation.toIsAlgebraicOver`, a theorem declared in [MathlibExt/Combinatorics/Matroid/Algebraic.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Matroid/Algebraic.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/algebraic-matroids/index.html#to-is-algebraic-over).

## Representations over some field witness algebraicity

If a matroid $M$ on a type $E$
has an algebraic representation over some field whose base field and extension field lie in the
same universe as $E$, then $M$ is algebraic.

Formalized by `Matroid.AlgebraicRepresentationSomeField.toIsAlgebraic`, a theorem declared in [MathlibExt/Combinatorics/Matroid/Algebraic.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Matroid/Algebraic.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/algebraic-matroids/index.html#to-is-algebraic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Algebraic matroids](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/algebraic-matroids/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/matroid-theory/algebraic-matroids)
