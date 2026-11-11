---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Ramsey.ramsey_two_uniform, MathlibExt.Combinatorics.ParisHarringtonWanted.paris_harrington
statement: formalized
proof: formalized
---

# Ramsey's theorem, Hales–Jewett and Hindman: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/index.html).

Ramsey's theorem for sets and hypergraphs (including size Ramsey numbers and Paris–Harrington), Hales–Jewett and density Hales–Jewett, Hindman's and the pairwise sum theorem via ultrafilters, central, J-, C- and piecewise syndetic sets in semigroups, and grid Ramsey properties.

## Finite Ramsey theorem for pairs

For every number of colors $r \ge 1$ and every natural
number $k$ there is a natural number $N$ such that for every coloring of the subsets of
$\{0, 1, \dots, N - 1\}$ with $r$ colors there are a $k$-element subset $S$ and a color $c$ such
that every $2$-element subset of $S$ has color $c$.

## Sources

- F. P. Ramsey, On a Problem of Formal Logic, Proc. London Math. Soc. s2-30 (1930), 264-286, DOI 10.1112/PLMS/S2-30.1.264.

Formalized by `MathlibExt.Combinatorics.Ramsey.ramsey_two_uniform`, a theorem declared in [MathlibExt/Combinatorics/Ramsey.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Ramsey.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/index.html#ramsey-two-uniform).

## Strengthened finite Ramsey theorem (Paris–Harrington principle)

For all integers $c \ge 1$,
$k \ge 1$ and $m \ge 1$ there is a natural number $N$ such that for every coloring $f$ of the
finite subsets of $\mathbb{N}$ with $c$ colors there is a nonempty set $H \subseteq \{1, \dots, N\}$
with $|H| \ge m$ and $\min H \le |H|$ such that all $k$-element subsets of $H$ have the same color:
some color $t$ satisfies $f(S) = t$ for every $k$-element subset $S \subseteq H$.

## Sources

- J. Paris and L. Harrington, Handbook of Mathematical Logic, ed. Barwise (1977); Graham-Rothschild-Spencer, Ramsey Theory. The statement is the finite combinatorial form with the largeness condition; its independence from PA is not part of it.

Formalized by `MathlibExt.Combinatorics.ParisHarringtonWanted.paris_harrington`, a theorem declared in [MathlibExt/Combinatorics/ParisHarrington.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ParisHarrington.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/index.html#paris-harrington).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramsey's theorem, Hales–Jewett and Hindman](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/structural-ramsey)
