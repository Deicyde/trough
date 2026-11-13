---
declaration: section
origin: cited
lean: OrdinalCardinalRamsey, MetaMathlibExt.IsHomogeneousFor, MathlibExt.Combinatorics.AlephOmegaPartitionSumErdosProblem1219Wanted.ArrowsPairs, MathlibExt.Combinatorics.AlephOmegaPartitionSumErdosProblem1219Wanted.alephOmegaPartitionOfCardinalSum, MathlibExt.Combinatorics.AlephOmegaPartitionSumErdosProblem1219Wanted.alephOmegaPartitionOfCardinalSum_holds, MathlibExt.Combinatorics.ErdosProblem591Wanted.conjecture, MathlibExt.Combinatorics.ErdosProblem591Wanted.conjecture_holds, MathlibExt.Combinatorics.PartitionOrdinalTriangleCliqueErdosProblem118Wanted.PartitionRel
statement: formalized
---

# Partition calculus

10 results, 7 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/partition-calculus/index.html).

## Ordinal–cardinal Ramsey property

For ordinals $\alpha$, $\beta$ and a cardinal $c$, the
partition property $\alpha \to (\beta, c)^2$ holds if for every coloring of the edges of the
complete graph on the ordinals less than $\alpha$ in red and blue, either some set of vertices
whose order type is $\beta$ has all its edges red, or some set of vertices of cardinality exactly
$c$ has all its edges blue.

Formalized by `OrdinalCardinalRamsey`, a definition declared in [MathlibExt/SetTheory/Cardinal/SimpleGraph.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Cardinal/SimpleGraph.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/partition-calculus/index.html#ordinal-cardinal-ramsey).

## Homogeneous set

Let $c$ assign a colour in $\gamma$ to each finite subset of a type
$I$, and let $n \in \mathbb{N}$. A set $H \subseteq I$ is homogeneous for $c$ with colour
$k \in \gamma$ if $c(s) = k$ for every $n$-element subset $s$ of $H$.

Only the values of $c$ on $n$-element sets matter, so $c$ plays the role of a colouring
$[I]^n \to \gamma$ of the $n$-element subsets of $I$.

Formalized by `MetaMathlibExt.IsHomogeneousFor`, a definition declared in [MathlibExt/SetTheory/InfinitaryCombinatorics/PartitionCalculus.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/InfinitaryCombinatorics/PartitionCalculus.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/partition-calculus/index.html#is-homogeneous-for).

## Partition relation for pairs with two colours

For cardinals $\kappa$ and $\mu$, the
relation $\kappa \to (\mu)^2_2$ holds if for every set $X$ of cardinality $\kappa$ and every
symmetric colouring $c$ of the ordered pairs of elements of $X$ with two colours, there are a
subset $H \subseteq X$ of cardinality $\mu$ and a colour $b$ such that $c(x, y) = b$ for all
distinct $x, y \in H$.

Formalized by `MathlibExt.Combinatorics.AlephOmegaPartitionSumErdosProblem1219Wanted.ArrowsPairs`, a definition declared in [WantedExt/Combinatorics/AlephOmegaPartitionSumErdosProblem1219Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AlephOmegaPartitionSumErdosProblem1219Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/partition-calculus/index.html#arrows-pairs).

## Erdős Problem 1219: a partition relation for sums of powers of two

The statement that for
every strictly increasing sequence $n_0 < n_1 < \cdots$ of natural numbers such that the cardinals
$2^{\aleph_{n_k}}$ are strictly increasing in $k$ and $2^{\aleph_{n_0}} > \aleph_\omega$, the
partition relation $\sum_k 2^{\aleph_{n_k}} \to (\aleph_\omega)^2_2$ holds: for every set $X$ of
cardinality $\sum_k 2^{\aleph_{n_k}}$ and every symmetric colouring of the pairs of elements of $X$
with two colours, some subset of $X$ of cardinality $\aleph_\omega$ has all pairs of distinct
elements of the same colour.

Formalized by `MathlibExt.Combinatorics.AlephOmegaPartitionSumErdosProblem1219Wanted.alephOmegaPartitionOfCardinalSum`, a definition declared in [WantedExt/Combinatorics/AlephOmegaPartitionSumErdosProblem1219Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AlephOmegaPartitionSumErdosProblem1219Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/partition-calculus/index.html#aleph-omega-partition-of-cardinal-sum).

## Shelah's theorem (Erdős Problem 1219)

For every strictly increasing sequence
$n_0 < n_1 < \cdots$ of natural numbers such that the cardinals $2^{\aleph_{n_k}}$ are strictly
increasing in $k$ and $2^{\aleph_{n_0}} > \aleph_\omega$, the partition relation
$\sum_k 2^{\aleph_{n_k}} \to (\aleph_\omega)^2_2$ holds: for every set $X$ of cardinality
$\sum_k 2^{\aleph_{n_k}}$ and every symmetric colouring of the pairs of elements of $X$ with two
colours, some subset of $X$ of cardinality $\aleph_\omega$ has all pairs of distinct elements of
the same colour.

## Sources

- T. F. Bloom, Erdős Problems, Problem #1219, https://www.erdosproblems.com/1219 (status PROVED); resolution: S. Shelah, Notes on partition calculus, in Infinite and Finite Sets (Colloq. Keszthely, 1973), Colloq. Math. Soc. János Bolyai 10, North-Holland (1975), 1257-1276, erdosproblems.com/1219: proved by Shelah (a problem of Erdős, Hajnal and Rado; P. Komjáth, The Erdős-Hajnal problem list, Bull. Symb. Log. (2025), p. 2).

Stated but not proved: `MathlibExt.Combinatorics.AlephOmegaPartitionSumErdosProblem1219Wanted.alephOmegaPartitionOfCardinalSum_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/AlephOmegaPartitionSumErdosProblem1219Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AlephOmegaPartitionSumErdosProblem1219Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/partition-calculus/index.html#aleph-omega-partition-of-cardinal-sum-ho).

## Erdős Problem 591

The statement that, for $\alpha = \omega^{\omega^2}$, every red/blue
colouring of the edges of the complete graph on the ordinals less than $\alpha$ (that is, every
pair of complementary simple graphs, red and blue, on this set) has a red clique whose order
type is $\alpha$ or a blue clique with exactly $3$ elements. In partition notation,
$\alpha \to (\alpha, 3)^2$.

Formalized by `MathlibExt.Combinatorics.ErdosProblem591Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem591Wanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem591Wanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/partition-calculus/index.html#conjecture).

## Erdős Problem 591 is true

Let $\alpha = \omega^{\omega^2}$. For every red/blue colouring of
the edges of the complete graph on the ordinals less than $\alpha$, that is, every pair of
complementary simple graphs (red and blue) on this set, there is a red clique whose order type
is $\alpha$ or a blue clique with exactly $3$ elements. In partition notation,
$\alpha \to (\alpha, 3)^2$.

## Sources

- Schipperus [Sc10] and Darby, independently, per erdosproblems.com/591, https://www.erdosproblems.com/591.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem591Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem591Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem591Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/partition-calculus/index.html#conjecture-holds).

## Ordinal partition relation

For an ordinal $\alpha$ and a natural number $n$, the partition
relation $\alpha \to (\alpha, n)^2$ holds when every colouring of the pairs $x < y$ of ordinals
below $\alpha$ in red and blue has a red set of order type $\alpha$ or a blue set of size $n$:
either there is a strictly increasing map $f$ from the ordinals below $\alpha$ to the ordinals
below $\alpha$ such that the pair $\{f(x), f(y)\}$ is red for all $x < y < \alpha$, or there is a
set of $n$ ordinals below $\alpha$ all of whose pairs are blue.

Formalized by `MathlibExt.Combinatorics.PartitionOrdinalTriangleCliqueErdosProblem118Wanted.PartitionRel`, a definition declared in [WantedExt/Combinatorics/PartitionOrdinalTriangleCliqueErdosProblem118Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PartitionOrdinalTriangleCliqueErdosProblem118Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/partition-calculus/index.html#partition-rel).

## Erdős Problem 118 for ordinals

The statement that for every ordinal $\alpha$ satisfying
the partition relation $\alpha \to (\alpha, 3)^2$ and every natural number $n \ge 3$, the ordinal
$\alpha$ also satisfies $\alpha \to (\alpha, n)^2$.

Formalized by `MathlibExt.Combinatorics.PartitionOrdinalTriangleCliqueErdosProblem118Wanted.partitionOrdinalTriangleImpliesClique`, a definition declared in [WantedExt/Combinatorics/PartitionOrdinalTriangleCliqueErdosProblem118Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PartitionOrdinalTriangleCliqueErdosProblem118Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/partition-calculus/index.html#partition-ordinal-triangle-implies-cliqu).

## Erdős Problem 118 fails for ordinals

There exist an ordinal $\alpha$ satisfying the partition
relation $\alpha \to (\alpha, 3)^2$ and a natural number $n \ge 3$ such that $\alpha$ does not
satisfy $\alpha \to (\alpha, n)^2$.

Schipperus and Darby independently answered the question in the negative. A concrete
counterexample is $\alpha = \omega^{\omega^2}$ with $n = 5$: Schipperus proved
$\omega^{\omega^\beta} \to (\omega^{\omega^\beta}, 3)^2$ when $\beta$ is a sum of two additively
indecomposable ordinals (here $\beta = 1 + 1$), and Larson proved
$\omega^{\omega^\beta} \not\to (\omega^{\omega^\beta}, 5)^2$ for every $\beta$ that is not
additively indecomposable.

## Sources

- T. F. Bloom, Erdős Problems, Problem #118, https://www.erdosproblems.com/118 (status DISPROVED); resolution: R. Schipperus, Countable partition ordinals, Ann. Pure Appl. Logic 161 (2010), 1195-1215; C. Darby, Negative partition relations for ordinals ω^{ω^α}, J. Combin. Theory Ser. B 76 (1999), 205-222; J. A. Larson, An ordinal partition avoiding pentagrams, J. Symbolic Logic 65 (2000), 969-978, erdosproblems.com/118: answered no independently by Schipperus and Darby; for α = ω^{ω²}: ω^{ω²} → (ω^{ω²}, 3)² (Schipperus: ω^{ω^β} → (ω^{ω^β}, 3)² when β is a sum of two additively indecomposable ordinals) and ω^{ω²} ↛ (ω^{ω²}, 5)² (Larson, main theorem: ω^{ω^β} ↛ (ω^{ω^β}, 5)² for β not additively indecomposable; zbMATH 0967.03042); Hajnal-Larson, Handbook of Set Theory, Chapter 2.9.

Stated but not proved: `MathlibExt.Combinatorics.PartitionOrdinalTriangleCliqueErdosProblem118Wanted.partitionOrdinalTriangleImpliesClique_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/PartitionOrdinalTriangleCliqueErdosProblem118Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PartitionOrdinalTriangleCliqueErdosProblem118Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/partition-calculus/index.html#partition-ordinal-triangle-implies-cliqu-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partition calculus](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/partition-calculus/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/SetTheory/infinitary-combinatorics/partition-calculus)
