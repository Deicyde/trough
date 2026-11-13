---
declaration: section
origin: cited
lean: MathlibExt.Algebra.Lie.PoissonBracket.PoissonBracket, MathlibExt.Algebra.Lie.PoissonBracket.IsPoissonIdeal, MathlibExt.Algebra.Lie.PoissonBracket.IsPoissonPrime, MathlibExt.Algebra.Lie.PoissonBracket.poissonCore, MathlibExt.Algebra.Lie.PoissonBracket.bracket_zero, MathlibExt.Algebra.Lie.PoissonBracket.bot_poisson, MathlibExt.Algebra.Lie.PoissonBracket.sup_poisson, MathlibExt.Algebra.Lie.PoissonBracket.poissonCore_poisson
statement: formalized
proof: formalized
---

# Poisson algebras and Poisson ideals

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html).

## Poisson bracket

Let $A$ be a commutative $\mathbb{C}$-algebra. A Poisson bracket on $A$
is a map assigning to $x, y \in A$ an element $\lbrace x, y \rbrace \in A$ such that for all
$x, y, z \in A$ and $c \in \mathbb{C}$: $\lbrace x + y, z \rbrace = \lbrace x, z \rbrace +
\lbrace y, z \rbrace$ and $\lbrace x, y + z \rbrace = \lbrace x, y \rbrace + \lbrace x, z \rbrace$;
$\lbrace x, y \rbrace = -\lbrace y, x \rbrace$; the Leibniz rule
$\lbrace x, yz \rbrace = y \lbrace x, z \rbrace + \lbrace x, y \rbrace z$ holds; the Jacobi
identity $\lbrace x, \lbrace y, z \rbrace \rbrace + \lbrace y, \lbrace z, x \rbrace \rbrace +
\lbrace z, \lbrace x, y \rbrace \rbrace = 0$ holds; and $\lbrace c x, y \rbrace =
c \lbrace x, y \rbrace$ and $\lbrace x, c y \rbrace = c \lbrace x, y \rbrace$.

Formalized by `MathlibExt.Algebra.Lie.PoissonBracket.PoissonBracket`, a structure declared in [MathlibExt/Algebra/Lie/PoissonBracket.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Lie/PoissonBracket.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html#poisson-bracket).

## Poisson ideal

Let $A$ be a commutative $\mathbb{C}$-algebra with a Poisson bracket
$\lbrace \cdot, \cdot \rbrace$. An ideal $P$ of $A$ is a Poisson ideal when
$\lbrace a, p \rbrace \in P$ for all $a \in A$ and all $p \in P$.

Formalized by `MathlibExt.Algebra.Lie.PoissonBracket.IsPoissonIdeal`, a definition declared in [MathlibExt/Algebra/Lie/PoissonBracket.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Lie/PoissonBracket.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html#is-poisson-ideal).

## Poisson prime ideal

Let $A$ be a commutative $\mathbb{C}$-algebra with a Poisson bracket.
An ideal $P$ of $A$ is a Poisson prime when it is both a prime ideal and a Poisson ideal.

Formalized by `MathlibExt.Algebra.Lie.PoissonBracket.IsPoissonPrime`, a definition declared in [MathlibExt/Algebra/Lie/PoissonBracket.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Lie/PoissonBracket.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html#is-poisson-prime).

## Poisson core

Let $A$ be a commutative $\mathbb{C}$-algebra with a Poisson bracket. For an
ideal $J$ of $A$, the Poisson core of $J$ is the supremum, in the lattice of ideals of $A$, of the
set of all Poisson ideals of $A$ contained in $J$.

It is the largest Poisson ideal contained in $J$ (universal property of the Poisson core).

Formalized by `MathlibExt.Algebra.Lie.PoissonBracket.poissonCore`, a definition declared in [MathlibExt/Algebra/Lie/PoissonBracket.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Lie/PoissonBracket.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html#poisson-core).

## Bracket with zero

Let $A$ be a commutative $\mathbb{C}$-algebra with a Poisson bracket
$\lbrace \cdot, \cdot \rbrace$. For every $a \in A$, $\lbrace a, 0 \rbrace = 0$.

Formalized by `MathlibExt.Algebra.Lie.PoissonBracket.bracket_zero`, a theorem declared in [MathlibExt/Algebra/Lie/PoissonBracket.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Lie/PoissonBracket.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html#bracket-zero).

## The zero ideal is a Poisson ideal

Let $A$ be a commutative $\mathbb{C}$-algebra with a
Poisson bracket. The zero ideal of $A$ is a Poisson ideal.

Formalized by `MathlibExt.Algebra.Lie.PoissonBracket.bot_poisson`, a theorem declared in [MathlibExt/Algebra/Lie/PoissonBracket.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Lie/PoissonBracket.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html#bot-poisson).

## The sum of two Poisson ideals inside an ideal

Let $A$ be a commutative
$\mathbb{C}$-algebra with a Poisson bracket, and let $I$, $K$ and $J$ be ideals of $A$. If $I$
and $K$ are Poisson ideals contained in $J$, then their sum $I + K$ is a Poisson ideal contained
in $J$.

Formalized by `MathlibExt.Algebra.Lie.PoissonBracket.sup_poisson`, a theorem declared in [MathlibExt/Algebra/Lie/PoissonBracket.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Lie/PoissonBracket.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html#sup-poisson).

## The Poisson core is a Poisson ideal

Let $A$ be a commutative $\mathbb{C}$-algebra with a
Poisson bracket. For every ideal $J$ of $A$, the Poisson core of $J$ is a Poisson ideal.

The family of Poisson ideals contained in $J$ is nonempty and directed (the sum of two members
is again a member), so every element of the core lies in some member of the family.

Formalized by `MathlibExt.Algebra.Lie.PoissonBracket.poissonCore_poisson`, a theorem declared in [MathlibExt/Algebra/Lie/PoissonBracket.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Lie/PoissonBracket.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html#poisson-core-poisson).

## The Poisson core is contained in the ideal

Let $A$ be a commutative $\mathbb{C}$-algebra
with a Poisson bracket. For every ideal $J$ of $A$, the Poisson core of $J$ is contained in $J$.

Formalized by `MathlibExt.Algebra.Lie.PoissonBracket.poissonCore_le`, a theorem declared in [MathlibExt/Algebra/Lie/PoissonBracket.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Lie/PoissonBracket.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html#poisson-core-le).

## Poisson ideals inside an ideal lie in its Poisson core

Let $A$ be a commutative
$\mathbb{C}$-algebra with a Poisson bracket, and let $J$ and $P$ be ideals of $A$. If
$P \subseteq J$ and $P$ is a Poisson ideal, then $P$ is contained in the Poisson core of $J$.

Formalized by `MathlibExt.Algebra.Lie.PoissonBracket.le_poissonCore`, a theorem declared in [MathlibExt/Algebra/Lie/PoissonBracket.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Lie/PoissonBracket.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html#le-poisson-core).

## Universal property of the Poisson core

Let $A$ be a commutative $\mathbb{C}$-algebra
with a Poisson bracket. For every ideal $J$ of $A$, the Poisson core of $J$ is the greatest
element of the set of Poisson ideals of $A$ contained in $J$: it is a Poisson ideal contained in
$J$, and it contains every Poisson ideal of $A$ contained in $J$.

Formalized by `MathlibExt.Algebra.Lie.PoissonBracket.poissonCore_isGreatest`, a theorem declared in [MathlibExt/Algebra/Lie/PoissonBracket.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Lie/PoissonBracket.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html#poisson-core-is-greatest).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poisson algebras and Poisson ideals](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/nonassociative-algebras/poisson-algebras-and-poisson-ideals)
