---
declaration: section
origin: cited
lean: MathlibExt.Algebra.ScottishBook171Wanted.IsAssociative, MathlibExt.Algebra.ScottishBook171Wanted.IsPermutationInvariant, MathlibExt.Algebra.ScottishBook171Wanted.scottishBook171_refuted
statement: formalized
---

# Associative operations on self-maps

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/associative-operations-on-self-maps/index.html).

## Associative operations on self-maps

Let $A$ be a set and let $U$ be an operation that
assigns to any two maps $f, g \colon A \to A$ a map $U(f, g) \colon A \to A$. We say $U$ is
associative (condition (1) of Problem 171) if $U(f, U(g, h)) = U(U(f, g), h)$ for all maps
$f, g, h \colon A \to A$.

Formalized by `MathlibExt.Algebra.ScottishBook171Wanted.IsAssociative`, a definition declared in [WantedExt/Algebra/ScottishBook171Wanted.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/ScottishBook171Wanted.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/associative-operations-on-self-maps/index.html#is-associative).

## Permutation-invariant operations on self-maps

Let $A$ be a set and let $U$ be an
operation that assigns to any two maps $f, g \colon A \to A$ a map $U(f, g) \colon A \to A$. We
say $U$ is invariant under permutations of $A$ (condition (2) of Problem 171) if conjugating the
arguments by a permutation conjugates the result: for every permutation $p$ of $A$ and all maps
$f, g \colon A \to A$, $U(p^{-1} \circ f \circ p, p^{-1} \circ g \circ p) = p^{-1} \circ U(f, g)
\circ p$.

Formalized by `MathlibExt.Algebra.ScottishBook171Wanted.IsPermutationInvariant`, a definition declared in [WantedExt/Algebra/ScottishBook171Wanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/ScottishBook171Wanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/associative-operations-on-self-maps/index.html#is-permutation-invariant).

## Scottish Book Problem 171 is false

Not every associative, permutation-invariant operation
on self-maps is composition: there are a set $A$, an operation $U$ that assigns to any two maps
$f, g \colon A \to A$ a map $U(f, g) \colon A \to A$ and is both associative (condition (1) of
Problem 171) and invariant under permutations of $A$ (condition (2)), and maps
$f, g \colon A \to A$ with $U(f, g) \ne f \circ g$, where $(f \circ g)(x) = f(g(x))$.

Reverse composition $U(f, g) = g \circ f$ and the two projections $U(f, g) = f$ and
$U(f, g) = g$ satisfy (1) and (2) but are not composition in general. The typescript's
parenthetical $(U(f,g) \ne 1)$ is of unclear meaning and is not read as excluding these
counterexamples.

## Sources

- J. Schreier – S. Ulam, Problem 171 of the Scottish Book, typescript p. 76.

Stated but not proved: `MathlibExt.Algebra.ScottishBook171Wanted.scottishBook171_refuted` is written with `theorem_wanted` in [WantedExt/Algebra/ScottishBook171Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/ScottishBook171Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/associative-operations-on-self-maps/index.html#scottish-book171-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Associative operations on self-maps](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/associative-operations-on-self-maps/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/algebraic-identities/associative-operations-on-self-maps)
