---
declaration: section
origin: cited
lean: Hamming.expansion, Hamming.IsBall, MathlibExt.Combinatorics.HarperIsoperimetricWanted.harper_isoperimetric_inequality
statement: formalized
proof: formalized
---

# Harper's isoperimetric inequality

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/harper-s-isoperimetric-inequality/index.html).

## Hamming expansion

Let $\iota$ and $F$ be finite, and view functions $\iota \to F$ as
words with the Hamming distance. For a finite set $A$ of words and $t \in \mathbb{N}$, the
$t$-expansion of $A$ is the set of words at Hamming distance at most $t$ from some element of
$A$, that is, the union over $a \in A$ of the closed Hamming balls of radius $t$ about $a$.

Formalized by `Hamming.expansion`, a definition declared in [MathlibExt/InformationTheory/HammingExpansion.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/HammingExpansion.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/harper-s-isoperimetric-inequality/index.html#expansion).

## Hamming ball predicate

Let $\iota$ and $F$ be finite, and view functions $\iota \to F$
as words with the Hamming distance. A set $B$ of words is a Hamming ball if there are a word
$c$ and a radius $e \in \mathbb{N}$ such that $B$ is the closed Hamming ball of radius $e$
about $c$.

Formalized by `Hamming.IsBall`, a definition declared in [MathlibExt/InformationTheory/HammingExpansion.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/HammingExpansion.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/harper-s-isoperimetric-inequality/index.html#is-ball).

## Harper's isoperimetric inequality on the Hamming cube

Let $n$ be a natural number. For
points $x, y \in \{0,1\}^n$, write $d_H(x, y)$ for the Hamming distance between them, the number
of coordinates in which they differ. For a set $S \subseteq \{0,1\}^n$ and a natural number $t$,
write $S_t$ for the set of points $x \in \{0,1\}^n$ with $d_H(x, s) \le t$ for some $s \in S$.
Let $A$ and $B$ be subsets of $\{0,1\}^n$ such that $B$ is a closed Hamming ball, that is,
$B = \{x : d_H(c, x) \le e\}$ for some $c \in \{0,1\}^n$ and some natural number $e$, and such
that $|B| \le |A|$. Then $|B_t| \le |A_t|$ for every natural number $t \ge 1$.

This is only the ball-comparison form of Harper's theorem: it does not assert that a ball
exists at every cardinality and gives no equality cases.

## Sources

- ATLAS ProbabilisticMethodsInCombinatorics, Theorem 9.4.3; the course text cites Harper without proof.
- L. H. Harper, "Optimal numberings and isoperimetric problems on graphs," Journal of Combinatorial Theory 1(3) (1966), 385–393, DOI 10.1016/S0021-9800(66)80059-5.

Formalized by `MathlibExt.Combinatorics.HarperIsoperimetricWanted.harper_isoperimetric_inequality`, a theorem declared in [MathlibExt/Combinatorics/HarperIsoperimetric.lean, line 1675](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/HarperIsoperimetric.lean#L1675). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/harper-s-isoperimetric-inequality/index.html#harper-isoperimetric-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Harper's isoperimetric inequality](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/harper-s-isoperimetric-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/intersecting-families/harper-s-isoperimetric-inequality)
