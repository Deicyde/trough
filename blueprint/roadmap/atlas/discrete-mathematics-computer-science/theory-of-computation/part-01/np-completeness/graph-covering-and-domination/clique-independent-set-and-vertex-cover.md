---
declaration: section
origin: cited
lean: Cslib.Complexity.Karp.pairs, Cslib.Complexity.Karp.adjBits, Cslib.Complexity.Karp.toGraph, Cslib.Complexity.Karp.encodeKG, Cslib.Complexity.Karp.decodeKG, Cslib.Complexity.Karp.noKG, Cslib.Complexity.Karp.kgDec, Cslib.Complexity.Karp.cliqueDec
statement: formalized
proof: formalized
---

# Clique, independent set and vertex cover

151 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/index.html).

## Vertex pairs in encoding order

For a natural number $n$, the list of all pairs $(i, j)$ of
natural numbers with $i < j < n$, ordered by $i$ ascending and, for each $i$, by $j$ descending
from $n - 1$ to $i + 1$.

Formalized by `Cslib.Complexity.Karp.pairs`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#pairs).

## Adjacency bit of a vertex pair

Let $n$, $i$, $j$ be natural numbers and $b$ a list of
bits. List the pairs $(i', j')$ with $i' < j' < n$ in encoding order ($i'$ ascending and, for
each $i'$, $j'$ descending) and match the $t$-th pair with the $t$-th bit of $b$, for as many
positions as both lists have. The adjacency bit of $\{i, j\}$ is the bit matched with
$(\min(i, j), \max(i, j))$, and false when that pair has no matched bit (for instance when
$i = j$, when $\max(i, j) \ge n$, or when $b$ is too short).

Formalized by `Cslib.Complexity.Karp.adjBits`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#adj-bits).

## The graph encoded by pair bits

List the pairs $(i, j)$ of natural numbers with
$i < j < n$ by $i$ ascending and, for each $i$, by $j$ descending, and give the $t$-th pair the
$t$-th bit of a list of bits. The simple graph on the vertex set $\{0, \dots, n - 1\}$ given by
the list makes two vertices $i < j$ adjacent when the bit of $(i, j)$ is true; a pair left
without a bit because the list is too short is not an edge, and bits beyond the last pair are
ignored.

Formalized by `Cslib.Complexity.Karp.toGraph`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#to-graph).

## Encoding of a graph instance

For natural numbers $k$, $n$ and a list of bits $b$, the
encoding is $1^k\,0\,1^n\,0\,b$, writing $1$ for true and $0$ for false: $k$ ones, a zero,
$n$ ones, a zero, and then $b$. Here $k$ is the target size and $b$ lists the pair bits of a
graph on $n$ vertices.

Formalized by `Cslib.Complexity.Karp.encodeKG`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#encode-kg).

## Decoding a graph instance

Writing $1$ for true and $0$ for false, a bit string of the
form $1^k\,0\,1^n\,0\,b$ with natural numbers $k$, $n$ and a list of bits $b$ decodes to the
triple $(k, n, b)$. A bit string with fewer than two zeros does not decode.

Formalized by `Cslib.Complexity.Karp.decodeKG`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#decode-kg).

## Fixed no-instance

The bit string $1\,0\,0$ (writing $1$ for true and $0$ for false),
which encodes $k = 1$ together with the graph with no vertices ($n = 0$ and no pair bits).

A graph with no vertices has no clique, independent set or vertex cover of exactly one vertex,
so this string lies in none of CLIQUE, INDEPENDENT-SET and VERTEX-COVER.

Formalized by `Cslib.Complexity.Karp.noKG`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#no-kg).

## Language of graph instances with a property

Let $P$ be a property of a natural number
$n$, a natural number $k$ and a simple graph on $\{0, \dots, n-1\}$. The decision problem accepts
a bit string $x$ exactly when, writing $1$ for true and $0$ for false, $x = 1^k\,0\,1^n\,0\,b$
for some natural numbers $k$, $n$ and a list of bits $b$ with one entry for each pair
$i < j < n$, such that $P$ holds of $n$, $k$ and the graph on $\{0, \dots, n-1\}$ given by $b$.
In that graph, distinct $i$ and $j$ are adjacent when the bit of the pair $\{i, j\}$ is true,
the pairs being listed with $i$ ascending and, for each $i$, $j$ descending.

Formalized by `Cslib.Complexity.Karp.kgDec`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#kg-dec).

## CLIQUE

The decision problem CLIQUE accepts a bit string $x$ exactly when, writing $1$
for true and $0$ for false, $x = 1^k\,0\,1^n\,0\,b$ for some natural numbers $k$, $n$ and a list
of bits $b$ with one entry for each pair $i < j < n$, such that the graph on
$\{0, \dots, n-1\}$ given by $b$ has a clique of exactly $k$ vertices. In that graph, distinct
$i$ and $j$ are adjacent when the bit of the pair $\{i, j\}$ is true, the pairs being listed
with $i$ ascending and, for each $i$, $j$ descending.

Formalized by `Cslib.Complexity.Karp.cliqueDec`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#clique-dec).

## INDEPENDENT-SET

The decision problem INDEPENDENT-SET accepts a bit string $x$ exactly
when, writing $1$ for true and $0$ for false, $x = 1^k\,0\,1^n\,0\,b$ for some natural numbers
$k$, $n$ and a list of bits $b$ with one entry for each pair $i < j < n$, such that the graph on
$\{0, \dots, n-1\}$ given by $b$ has an independent set of exactly $k$ vertices. In that graph,
distinct $i$ and $j$ are adjacent when the bit of the pair $\{i, j\}$ is true, the pairs being
listed with $i$ ascending and, for each $i$, $j$ descending.

Formalized by `Cslib.Complexity.Karp.indSetDec`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#ind-set-dec).

## The VERTEX-COVER problem

The decision problem that accepts a bit string exactly when it
encodes an instance $(k, G)$, where $G$ is a simple graph on $n$ vertices, and $G$ has a vertex
cover of exactly $k$ vertices. The encoding is $k$ ones, a zero, $n$ ones, a zero, then one bit
for each pair $(i, j)$ with $i < j < n$, listed by $i$ ascending and, for each $i$, by $j$
descending, a true bit meaning that $i$ and $j$ are adjacent; a string with any other number of
pair bits is rejected.

This is Sipser's $k$-node vertex cover; for $k \le n$ it is the same as a cover of at most $k$
vertices.

Formalized by `Cslib.Complexity.Karp.vertexCoverDec`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#vertex-cover-dec).

## Literal occurrences of a CNF formula

For a CNF formula $\varphi$ with clauses
$C_0, \dots, C_{m-1}$, the list of triples $(i, x, b)$, one for each literal $(x, b)$ of each
clause $C_i$, where $x$ is the variable index and $b$ the polarity. The triples are listed clause
by clause in order of $i$, and within a clause in the order of its literals.

Formalized by `Cslib.Complexity.Karp.occs`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#occs).

## Adjacency of literal occurrences in Karp's clique graph

A literal occurrence is a triple
$(c, x, b)$ of a clause index $c$, a variable index $x$ and a polarity $b$. Two occurrences
$(c, x, b)$ and $(c', x', b')$ are adjacent when $c \ne c'$ and they are not complementary, that
is, it is not the case that $x = x'$ and $b \ne b'$.

Formalized by `Cslib.Complexity.Karp.occAdj`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#occ-adj).

## Adjacency bits of Karp's clique graph

For a CNF formula $\varphi$, list its literal
occurrences $o_0, \dots, o_{m-1}$ in formula order, each recorded by its clause index, its
variable and its polarity. The result has one bit for each pair $(i, j)$ with $i < j < m$, the
pairs taken in encoding order ($i$ ascending and, for each $i$, $j$ descending). The bit of
$(i, j)$ is true exactly when $o_i$ and $o_j$ lie in different clauses and are not
complementary, that is, are not occurrences of the same variable with opposite polarities.

Formalized by `Cslib.Complexity.Karp.cliqueBits`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#clique-bits).

## Karp's CLIQUE instance of a CNF formula

For a CNF formula $\varphi$ with $m$ clauses and
$N$ literal occurrences, the bit string encoding the instance $(m, G)$: $m$ ones, a zero, $N$
ones, a zero, then one adjacency bit for each pair $(i, j)$ with $i < j < N$, listed by $i$
ascending and, for each $i$, by $j$ descending, a true bit meaning that $i$ and $j$ are adjacent.
The graph $G$ has the literal occurrences of $\varphi$, in order, as its vertices
$0, \dots, N - 1$, and two occurrences are adjacent when they lie in different clauses and are
not complementary (the same variable with opposite polarities).

Formalized by `Cslib.Complexity.Karp.toClique`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#to-clique).

## Karp's SAT-to-CLIQUE map on bit strings

The map on bit strings that decodes its input as
a CNF formula $\varphi$ (rejecting missing or trailing bits) and returns Karp's CLIQUE instance of
$\varphi$; an input that does not decode is sent to the fixed no-instance $k = 1$ on the graph
with no vertices.

Formalized by `Cslib.Complexity.Karp.reduceClique`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#reduce-clique).

## Complementing map from CLIQUE to INDEPENDENT-SET instances

Writing $1$ for true and $0$
for false, the map sends a bit string $1^k\,0\,1^n\,0\,b$ to $1^k\,0\,1^n\,0\,\bar b$, where
$\bar b$ is $b$ with every bit complemented. A bit string with fewer than two zeros goes to the
fixed no-instance $1\,0\,0$.

Formalized by `Cslib.Complexity.Karp.flipKG`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#flip-kg).

## Map from INDEPENDENT-SET to VERTEX-COVER instances

Writing $1$ for true and $0$ for
false, the map sends a bit string $1^k\,0\,1^n\,0\,b$ with $k \le n$ to $1^{n-k}\,0\,1^n\,0\,b$.
Every other bit string, namely one of this form with $k > n$ or one with fewer than two zeros,
goes to the fixed no-instance $1\,0\,0$.

Formalized by `Cslib.Complexity.Karp.isToVc`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Clique.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Clique.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#is-to-vc).

## Unparsable input is rejected

Let $P$ be any property of a triple $(n, k, G)$, where $n$ and
$k$ are natural numbers and $G$ is a simple graph on the vertices $0, 1, \dots, n - 1$. A bit string
that does not begin with two unary numbers (each a run of $1$s ended by a $0$) is rejected by the
language of valid instances $(k, G)$ satisfying $P$.

Formalized by `Cslib.Complexity.Karp.kgDec_of_decodeKG_eq_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#kg-dec-of-decode-kg-eq-none).

## Membership in the vertex pairs

For natural numbers $n$, $i$ and $j$, the pair
$(i, j)$ belongs to the list of vertex pairs in encoding order for $n$ if and only if $i < j$
and $j < n$.

Formalized by `Cslib.Complexity.Karp.mem_pairs`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#mem-pairs).

## The vertex pairs are listed without repetition

For every natural number $n$, the list
of pairs $(i, j)$ of natural numbers with $i < j < n$, in encoding order ($i$ ascending and, for
each $i$, $j$ descending from $n - 1$ to $i + 1$), contains no pair twice.

Formalized by `Cslib.Complexity.Karp.pairs_nodup`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-01/index.html#pairs-nodup).

## Pair bits are read off by position

Let $n$ be a natural number, and let the pair list of
$n$ be the list of pairs $(i, j)$ with $i < j < n$ in encoding order. Let $b$ be a list of bits
whose length equals the length of the pair list of $n$. For all $i < j < n$, the bit of the pair
$(i, j)$ in $b$ is the entry of $b$ at the position of $(i, j)$ in the pair list of $n$.

Formalized by `Cslib.Complexity.Karp.adjBits_eq_getElem`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#adj-bits-eq-get-elem).

## Pair bits computed by a function

Let $n$ be a natural number, let $f$ be a function from
pairs of natural numbers to bits, and let $b$ be the list obtained by applying $f$ to each entry of
the pair list of $n$ (the pairs $(i, j)$ with $i < j < n$ in encoding order). Then for all
$i < j < n$, the bit of the pair $(i, j)$ in $b$ is $f(i, j)$.

Formalized by `Cslib.Complexity.Karp.adjBits_map_pairs`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#adj-bits-map-pairs).

## Complementing the pair bits complements the graph

Let $n \in \mathbb{N}$ and let $b$ be a
list of bits whose length is the number of pairs $(i, j)$ with $i < j < n$. Then the graph on
$\{0, \dots, n-1\}$ read off the list obtained by negating every bit of $b$ is the complement of
the graph on $\{0, \dots, n-1\}$ read off $b$.

Formalized by `Cslib.Complexity.Karp.toGraph_map_not`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#to-graph-map-not).

## Correctness of the complementing map from CLIQUE to INDEPENDENT-SET

For every bit
string $x$, CLIQUE accepts $x$ if and only if INDEPENDENT-SET accepts the image of $x$ under the
complementing map from CLIQUE to INDEPENDENT-SET instances.

Formalized by `Cslib.Complexity.Karp.cliqueDec_eq_indSetDec_flipKG`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#clique-dec-eq-ind-set-dec-flip-kg).

## Independent sets and vertex covers of complementary sizes

Let $G$ be a simple graph whose
vertices are $0, 1, \dots, n - 1$, and let $k \le n$. Then $G$ has an independent set of exactly
$k$ vertices if and only if $G$ has a vertex cover of exactly $n - k$ vertices.

Formalized by `Cslib.Complexity.Karp.exists_isNIndepSet_iff_exists_isVertexCover`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#exists-is-nindep-set-iff-exists-is-verte).

## Membership in the literal occurrences of a CNF formula

Let $\varphi$ be a CNF formula
with clauses $C_0, \dots, C_{m-1}$, let $i$ and $x$ be natural numbers and let $b$ be a Boolean.
The triple $(i, x, b)$ belongs to the list of literal occurrences of $\varphi$ if and only if
$i < m$ and the literal $(x, b)$ belongs to $C_i$.

Formalized by `Cslib.Complexity.Karp.mem_occs`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#mem-occs).

## Adjacency in Karp's clique graph

Let $\varphi$ be a CNF formula and let
$o_0, \dots, o_{m-1}$ be its literal occurrences (clause index, variable, polarity) in formula
order. In Karp's graph of $\varphi$, the graph on $\{0, \dots, m-1\}$ read off the clique pair
bits of $\varphi$, vertices $i$ and $j$ are adjacent if and only if $i \ne j$ and the occurrences
$o_i$ and $o_j$ are adjacent, that is, they lie in different clauses and are not complementary
(they are not the same variable with opposite polarities).

Formalized by `Cslib.Complexity.Karp.toGraph_cliqueBits_adj`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#to-graph-clique-bits-adj).

## Karp's reduction from SAT to CLIQUE is correct

A CNF formula $\varphi$ with $m$ clauses is
satisfiable if and only if Karp's graph of $\varphi$ has a clique of exactly $m$ vertices. Karp's
graph has one vertex for each literal occurrence of $\varphi$, and two occurrences are adjacent
when they lie in different clauses and are not complementary.

Formalized by `Cslib.Complexity.Karp.cnfSat_iff_exists_isNClique`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#cnf-sat-iff-exists-is-nclique).

## SAT decision on undecodable input (moved alias)

Moved to `DenseSAT.ToBinary.satDec_of_decodeCNF_eq_none` (`DenseToBinary`).

Formalized by `Cslib.Complexity.Karp.satDec_of_decodeCNF_eq_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueCorrect.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#sat-dec-of-decode-cnf-eq-none).

## Modes of the clique verifier

A mode is one of three values, clique, independent set
and vertex cover, naming the three graph problems CLIQUE, INDEPENDENT-SET and VERTEX-COVER that
share one NP verifier.

Formalized by `Cslib.Complexity.Karp.KGVerify.Mode`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#mode).

## Pair condition of the clique verifier

For a mode $m$, the adjacency bit $b$ of a vertex
pair $\{i, j\}$, and flags $s_i$, $s_j$ saying whether $i$ and $j$ are chosen, the pair
condition $\mathrm{ok}_m(b, s_i, s_j)$ is $\lnot(s_i \land s_j) \lor b$ for clique,
$\lnot(s_i \land s_j) \lor \lnot b$ for independent set, and $\lnot b \lor s_i \lor s_j$ for
vertex cover.

Formalized by `Cslib.Complexity.Karp.KGVerify.Mode.ok`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#ok).

## The verifier for CLIQUE, INDEPENDENT-SET and VERTEX-COVER

For a mode $m$, an input
$x$ and a witness $w$ (bit lists), the verifier rejects if $x$ does not decode to a triple
$(k, n, \mathit{bits})$. Otherwise it accepts if and only if $\mathit{bits}$ has one bit per
pair $(i, j)$ with $i < j < n$, $w$ has at least $n$ bits, exactly $k$ of the first $n$ bits of
$w$ are set, and for every pair $(i, j)$, matched with its bit $b$ in the encoding order of the
pairs, the pair condition of $m$ holds for $b$, $w_i$ and $w_j$. So the first $n$ bits of $w$
choose the vertices.

Formalized by `Cslib.Complexity.Karp.KGVerify.kgCheck`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#kg-check).

## Vertices that settle their pairs alone

For a mode and the Boolean saying whether a
vertex $i$ is chosen, the result is true when $i$ alone settles the condition on every pair
$\{i, j\}$: in the clique and independent-set modes it is true exactly when $i$ is not chosen,
and in the vertex-cover mode exactly when $i$ is chosen.

Formalized by `Cslib.Complexity.Karp.KGVerify.Mode.free`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#free).

## The pair condition left to the later vertex

For a mode $m$, a pair bit $b$ and a
flag $s_j$ saying whether vertex $j$ is chosen, $\mathrm{sat}_m(b, s_j)$ is
$\lnot s_j \lor b$ for clique, $\lnot s_j \lor \lnot b$ for independent set, and
$\lnot b \lor s_j$ for vertex cover.

It is the pair condition on $\{i, j\}$ when vertex $i$ does not settle it.

Formalized by `Cslib.Complexity.Karp.KGVerify.Mode.sat`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#sat).

## The pair condition splits by vertex

For a mode $m$ and Booleans $b$, $s_i$, $s_j$, let
$\mathrm{ok}_m(b, s_i, s_j)$ be the pair condition of $m$: $\lnot(s_i \land s_j) \lor b$ for
clique, $\lnot(s_i \land s_j) \lor \lnot b$ for independent set and $\lnot b \lor s_i \lor s_j$
for vertex cover. Let $\mathrm{free}_m(s_i)$, the part that vertex $i$ alone settles, be
$\lnot s_i$ for clique and independent set and $s_i$ for vertex cover, and let
$\mathrm{sat}_m(b, s_j)$, the part left to $j$, be $\lnot s_j \lor b$ for clique,
$\lnot s_j \lor \lnot b$ for independent set and $\lnot b \lor s_j$ for vertex cover. Then for
every mode $m$ and all Booleans $b$, $s_i$, $s_j$, we have
$\mathrm{ok}_m(b, s_i, s_j) = \mathrm{free}_m(s_i) \lor \mathrm{sat}_m(b, s_j)$.

Formalized by `Cslib.Complexity.Karp.KGVerify.Mode.ok_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#ok-eq).

## Vertex pairs in encoding order for one more vertex

For a natural number $m$, write
$P(m)$ for the list of pairs $(i, j)$ of natural numbers with $i < j < m$, ordered by $i$
ascending and, for each $i$, by $j$ descending. Then for every natural number $n$, $P(n + 1)$ is
the list $(0, n), (0, n - 1), \dots, (0, 1)$ (empty when $n = 0$) followed by the pairs
$(i + 1, j + 1)$ for the pairs $(i, j)$ of $P(n)$, in the order of $P(n)$.

Formalized by `Cslib.Complexity.Karp.KGVerify.pairs_succ`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#pairs-succ).

## Chosen-flag pairs

For a list $s = (s_0, \dots, s_{\ell - 1})$ of Booleans, the
chosen-flag pairs of $s$ are the pairs $(s_i, s_j)$, one for each vertex pair $(i, j)$ with
$i < j < \ell$, listed in the encoding order of the vertex pairs of $\ell$ vertices (rows $i$
ascending, within a row $j$ descending).

Formalized by `Cslib.Complexity.Karp.KGVerify.pairVals`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#pair-vals).

## Reading a list at every index

For every list $s$ of Booleans of length $\ell$,
reading $s$ at the indices $0, 1, \dots, \ell - 1$ in turn (with default value false) gives
back $s$.

Formalized by `Cslib.Complexity.Karp.KGVerify.map_getD_range`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#map-get-d-range).

## Chosen-flag pairs of a list with a new head

For a Boolean $a$ and a list
$s = (s_0, \dots, s_{\ell - 1})$ of Booleans, the chosen-flag pairs of the list
$(a, s_0, \dots, s_{\ell - 1})$ are $(a, s_{\ell - 1}), (a, s_{\ell - 2}), \dots, (a, s_0)$,
followed by the chosen-flag pairs of $s$.

Formalized by `Cslib.Complexity.Karp.KGVerify.pairVals_cons`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#pair-vals-cons).

## The row-by-row check of the clique verifier

For a mode $m$, the row-by-row check of
a list of chosen-flags against a list $b$ of pair bits is defined by recursion on the flags.
For the empty list it holds iff $b$ is empty. For a flag $a$ followed by the flags $r$ of the
later vertices, write $\rho$ for the reverse of $r$: the check holds iff $|r| \le |b|$,
either $a$ is free for $m$ or $\mathrm{sat}_m(b_t, \rho_t)$ holds for every $t < |r|$
(indices from $0$), and the check of $r$ against $b$ with its first $|r|$ bits dropped holds.

This is what the machine checks, vertex by vertex; at the end no bit may be left.

Formalized by `Cslib.Complexity.Karp.KGVerify.rowsOk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-02/index.html#rows-ok).

## The row-by-row check is the pairwise check

For every mode $m$ and all lists of bits
$s$ and $b$, the row-by-row check of $s$ against $b$ holds if and only if $b$ has exactly
one bit per pair $i < j < |s|$ and, listing these pairs in encoding order (rows $i$
ascending, within a row $j$ descending), the $t$-th pair $(i, j)$ and the $t$-th bit $b_t$
satisfy the pair condition $\mathrm{ok}_m(b_t, s_i, s_j)$ for every $t$.

Formalized by `Cslib.Complexity.Karp.KGVerify.rowsOk_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#rows-ok-eq).

## The verifier as a row-by-row check

Let $m$ be a mode and $x$, $w$ bit lists.
Suppose that $x$ decodes to $(k, n, \mathit{bits})$, that $w$ has at least $n$ bits, and that
exactly $k$ of the first $n$ bits of $w$ are set. Then the verifier for mode $m$ on input $x$
and witness $w$ returns the same value as the row-by-row check for mode $m$ of the first $n$
bits of $w$ against the pair bits $\mathit{bits}$.

Formalized by `Cslib.Complexity.Karp.KGVerify.kgCheck_eq_rowsOk`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#kg-check-eq-rows-ok).

## Lookup in a list of pairs with distinct keys

Let $l$ be a list of pairs whose keys lie
in a type with a lawful Boolean equality and are pairwise distinct. If $(a, b)$ occurs in $l$,
then looking up the key $a$ in $l$ returns $b$.

Formalized by `Cslib.Complexity.Karp.KGVerify.lookup_of_mem`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#lookup-of-mem).

## Checking each listed vertex pair against its bit

Let $n$ be a natural number and $b$ a
list of bits with one bit per vertex pair, that is, with as many entries as the list of pairs
$(i, j)$ with $i < j < n$. Then for every Boolean predicate $P$ on a pair of natural numbers and
a bit, $P$ holds on every entry of the pair list zipped with $b$ (the $t$-th pair together with
the $t$-th bit of $b$) if and only if, for all natural numbers $i < j < n$, $P$ holds on the
pair $(i, j)$ together with the adjacency bit of $\{i, j\}$ in $b$.

Formalized by `Cslib.Complexity.Karp.KGVerify.all_zip_pairs`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#all-zip-pairs).

## Characterization of the CLIQUE verifier

For a mode $m$ and bit lists $x$ and $w$, the
verifier for mode $m$ accepts input $x$ with witness $w$ if and only if there are $k$, $n$ and a
bit list $\mathit{bits}$ such that $x$ is the encoding of the instance $(k, n, \mathit{bits})$,
$\mathit{bits}$ has one bit per pair $(i, j)$ with $i < j < n$, $w$ has at least $n$ bits,
exactly $k$ of the first $n$ bits of $w$ are set, and for all $i < j < n$ the pair condition of
$m$ holds for the bit of the pair $\{i, j\}$ and the bits $w_i$ and $w_j$.

Formalized by `Cslib.Complexity.Karp.KGVerify.kgCheck_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#kg-check-iff).

## Counting the set bits of a list built from a function

For every natural number $n$ and
every function $f$ from $\{0, \dots, n-1\}$ to the Booleans, the number of entries equal to
true in the list $f(0), f(1), \dots, f(n-1)$ equals the number of indices $i < n$ with $f(i)$
true.

Formalized by `Cslib.Complexity.Karp.KGVerify.count_ofFn`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#count-of-fn).

## The first $n$ bits of a list, read index by index

If a bit list $w$ has length at
least $n$, then the first $n$ entries of $w$ form the list $(w_0, \dots, w_{n-1})$, where $w_i$
is the entry of $w$ at index $i$ (taken as false past the end of $w$).

Formalized by `Cslib.Complexity.Karp.KGVerify.take_eq_ofFn`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#take-eq-of-fn).

## Vertex sets meeting a mode's pair condition

For a mode $m$, a number $n$, a list of
pair bits and a set $s$ of vertices in $\{0, \dots, n - 1\}$, the set $s$ meets the condition
of $m$ when for all vertices $i < j$ the pair condition
$\mathrm{ok}_m(b_{ij}, [i \in s], [j \in s])$ holds, where $[i \in s]$ says whether $i$ is
chosen and $b_{ij}$ is the bit of the pair $\{i, j\}$: listing the pairs $i' < j' < n$ in
encoding order (rows $i'$ ascending, within a row $j'$ descending), the $t$-th bit of the list
belongs to the $t$-th pair, and $b_{ij}$ is false if the list has no bit for $\{i, j\}$.

Formalized by `Cslib.Complexity.Karp.KGVerify.SetOk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#set-ok).

## An accepted input encodes an instance with a good vertex set

Fix a mode (clique,
independent set or vertex cover) and bit strings $x$ and $w$. If the verifier in that mode
accepts the input $x$ with witness $w$, then there are natural numbers $k$ and $n$ and a list of
bits $b$ such that $x$ is the encoding of the instance $(k, n, b)$, $b$ has exactly one bit per
vertex pair $(i, j)$ with $i < j < n$, and some set of exactly $k$ of the vertices
$0, \dots, n-1$ meets the mode's pair condition on every pair $i < j$.

Formalized by `Cslib.Complexity.Karp.KGVerify.exists_setOk`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#exists-set-ok).

## The characteristic vector of a good vertex set is accepted

Let $m$ be a mode, $k$ and
$n$ natural numbers, let $\mathit{bits}$ be a bit list with one bit per pair $(i, j)$,
$i < j < n$, and let $s$ be a set of $k$ vertices of $\{0, \dots, n - 1\}$ that meets the pair
condition of $m$ on every pair $i < j$. Then the verifier for mode $m$ accepts the encoding of
$(k, n, \mathit{bits})$ with witness the characteristic vector of $s$: the list of $n$ bits whose
$i$-th bit is set if and only if $i \in s$.

Formalized by `Cslib.Complexity.Karp.KGVerify.kgCheck_ofFn`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#kg-check-of-fn).

## Verifying a graph language defined by a vertex-set condition

Let $m$ be a mode and
$P$ a property of a number $k$ and a graph on $n$ vertices. Suppose that for all $n$, $k$ and
every bit list $\mathit{bits}$ with one bit per pair $(i, j)$, $i < j < n$, the property $P$
holds for $k$ and the graph given by $\mathit{bits}$ exactly when some set of $k$ vertices meets
the pair condition of $m$ on every pair $i < j$. Then for every bit list $x$, $x$ belongs to
the language of instances satisfying $P$ if and only if the verifier for mode $m$ accepts $x$
with some witness $w$ of length $|w| \le |x|$.

Formalized by `Cslib.Complexity.Karp.KGVerify.kgDec_iff_exists`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#kg-dec-iff-exists).

## Symmetric relations on increasing pairs

Let $n$ be a natural number and $R$ a relation
on $\{0, \dots, n-1\}$ such that $R(i, j)$ implies $R(j, i)$. Then $R(i, j)$ holds for all
$i \ne j$ if and only if $R(i, j)$ holds for all $i < j$.

Formalized by `Cslib.Complexity.Karp.KGVerify.forall_ne_iff_lt`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#forall-ne-iff-lt).

## Cliques of the graph given by pair bits

For natural numbers $n$ and $k$ and a list of
bits $b$, the graph on the vertices $0, \dots, n-1$ read off $b$ has a clique of exactly $k$
vertices if and only if there is a set $s$ of exactly $k$ of these vertices meeting the
clique-mode pair condition on every pair $i < j$: whenever $i$ and $j$ both lie in $s$, the
bit of the pair $\{i, j\}$ in $b$ is set.

Formalized by `Cslib.Complexity.Karp.KGVerify.clique_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#clique-iff).

## Independent sets of the graph given by pair bits

For natural numbers $n$ and $k$ and a
list of bits $b$, the graph on the vertices $0, \dots, n-1$ read off $b$ has an independent set
of exactly $k$ vertices if and only if there is a set $s$ of exactly $k$ of these vertices
meeting the independent-set-mode pair condition on every pair $i < j$: whenever $i$ and $j$ both
lie in $s$, the bit of the pair $\{i, j\}$ in $b$ is not set.

Formalized by `Cslib.Complexity.Karp.KGVerify.indep_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#indep-iff).

## Vertex covers of the graph given by pair bits

For natural numbers $n$ and $k$ and a list
of bits $b$, the graph on the vertices $0, \dots, n-1$ read off $b$ has a vertex cover of
exactly $k$ vertices if and only if there is a set $s$ of exactly $k$ of these vertices meeting
the cover-mode pair condition on every pair $i < j$: whenever the bit of the pair $\{i, j\}$ in
$b$ is set, $i$ or $j$ lies in $s$.

Formalized by `Cslib.Complexity.Karp.KGVerify.cover_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#cover-iff).

## CLIQUE is verified with witnesses no longer than the input

For every bit string $x$,
$x$ is in CLIQUE if and only if there is a bit string $w$ of length at most the length of $x$
such that the shared CLIQUE / INDEPENDENT-SET / VERTEX-COVER verifier, run in clique mode,
accepts the input $x$ with witness $w$.

Formalized by `Cslib.Complexity.Karp.KGVerify.cliqueDec_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#clique-dec-iff).

## INDEPENDENT-SET is verified with witnesses no longer than the input

For every bit string
$x$, $x$ is in INDEPENDENT-SET if and only if there is a bit string $w$ of length at most the
length of $x$ such that the shared CLIQUE / INDEPENDENT-SET / VERTEX-COVER verifier, run in
independent-set mode, accepts the input $x$ with witness $w$.

Formalized by `Cslib.Complexity.Karp.KGVerify.indSetDec_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#ind-set-dec-iff).

## VERTEX-COVER is verified by the clique verifier in cover mode

A bit string $x$ is in
VERTEX-COVER if and only if there is a bit string $w$, no longer than $x$, such that the
clique-family verifier in vertex-cover mode accepts $x$ with witness $w$.

Formalized by `Cslib.Complexity.Karp.KGVerify.vertexCoverDec_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#vertex-cover-dec-iff).

## Stacks of the CLIQUE verifier

The verifier machine for CLIQUE, INDEPENDENT-SET and
VERTEX-COVER, run on an instance with target size $k$ and $n$ vertices, has six stacks: the
input $X$, the witness $W$, the counter $C$ (holding $k$), the counter $N$ (holding $n$), the
vertex stack $V$ and its scratch stack $T$.

Formalized by `Cslib.Complexity.Karp.KGVerify.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#k).

## Labels of the CLIQUE verifier

On an instance with target size $k$ and $n$ vertices, the
verifier machine has the labels: read $k$, read $n$, load the witness, walk a row (carrying a bit
$c$, the conjunction of the row's pair conditions so far), put the row back, accept, and
reject.

Formalized by `Cslib.Complexity.Karp.KGVerify.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-03/index.html#lab).

## Statements of the clique verifier

The statements of the verifier are those of a
multi-stack Turing machine (Mathlib's TM2 model) with the six stacks $X, W, C, N, V, T$, each
over the symbol alphabet of the SAT verifier, the verifier's labels, and one Boolean of local
state.

Formalized by `Cslib.Complexity.Karp.KGVerify.Stmt`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#stmt).

## The clique verifier's unary reader

For a stack $c$ and labels $\ell$ (its own) and
$\ell'$ (the next), the unary reader onto $c$ is the verifier statement that inspects the
input stack $X$ and sets the state to whether $X$ is empty: if it is, it goes to the rejecting
label; otherwise it pops the top symbol of $X$ and sets the state to whether that symbol is
the bit $1$; if so, it pushes the bit $1$ onto $c$ and goes to $\ell$, while any other symbol
(normally the terminating $0$) sends it to $\ell'$.

Run from $\ell$, it reads a unary number off $X$ onto the counter $c$.

Formalized by `Cslib.Complexity.Karp.KGVerify.readU`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#read-u).

## Load step of the CLIQUE verifier

The statement run at the load label. If the counter
$N$ is nonempty, it takes a unit off $N$, rejects if the witness stack $W$ is empty, and
otherwise pops the top of $W$ and pushes its bit (false for a non-bit symbol) onto the vertex
stack $V$; if that bit is set it also takes a unit off the counter $C$, rejecting if $C$ is
empty; then it returns to the load label. If $N$ is empty, it goes to the walk label with its
flag $c$ (the conjunction of the row's pair conditions so far) set to true when $C$ is empty,
and rejects otherwise.

Started from $n$ on $N$ and $k$ on $C$, it loads the first $n$ witness bits onto $V$, bit
$n - 1$ on top, and rejects if $W$ runs out or the number of set bits among them is not $k$.

Formalized by `Cslib.Complexity.Karp.KGVerify.loadS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#load-s).

## Rest of a walk step of the clique verifier

Write $\mathrm{free}_m(s)$ for the condition
that, in mode $m$, a vertex with chosen-flag $s$ settles every pair of its row, and
$\mathrm{sat}_m(b', s')$ for the pair condition on pair bit $b'$ and later vertex flag $s'$. In
mode $m$ with row flag $c$, after a bit $z$ has been popped off the vertex stack $V$: if $V$ is
now empty, the machine moves to the put-back label when $\mathrm{free}_m(z)$ or $c$ holds, and to
the reject label otherwise. If $V$ is not empty, it pushes $z$ onto the scratch stack $T$; then
it moves to the reject label if the input stack $X$ is empty, and otherwise pops the top symbol
of $X$, reads it as a bit $b$ (a non-bit symbol reads as false), and moves to the walk label
with flag $c \wedge \mathrm{sat}_m(b, z)$.

Formalized by `Cslib.Complexity.Karp.KGVerify.walkZ`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#walk-z).

## Walk step of the clique verifier

In mode $m$ with row flag $c$, the walk step looks at
the vertex stack $V$. If $V$ is empty, it moves to the accept label if the input stack $X$ is
empty and to the reject label otherwise. If $V$ is not empty, it pops the top symbol of $V$,
reads it as a bit $z$ (a non-bit symbol reads as false), and continues with the rest of the walk
step for $m$, $c$ and $z$.

Formalized by `Cslib.Complexity.Karp.KGVerify.walkS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#walk-s).

## Program of the clique verifier

For a mode $m$ (clique, independent set or vertex
cover), the verifier program of mode $m$ assigns a statement to each label of the verifier: to
the label that reads the instance's target size $k$, the unary reader onto the counter $C$ with
own label this label and next label the label that reads the instance's number $n$ of vertices;
to the label that reads $n$, the unary reader onto the counter $N$ with own label this label and
next label the load label; to the load label, the load step; to the walk label with flag $c$,
the walk step of mode $m$ with flag $c$; to the put-back label, the bit-moving loop from the
scratch stack $T$ to the vertex stack $V$ that reads name-bit symbols as bits and writes each
bit $b$ as the name bit $b$, with own label the put-back label and next label the walk label
with flag true; and to the accept and reject labels, the statement that halts.

Run from the label that reads $k$, it parses $k$ and $n$, loads the witness and walks the
rows.

Formalized by `Cslib.Complexity.Karp.KGVerify.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#prog).

## Start label of the clique verifier

The verifier for CLIQUE, INDEPENDENT-SET and
VERTEX-COVER starts at the label that reads the instance's size parameter $k$ (the number of
vertices to choose) in unary off the input stack $X$ onto the counter $C$.

Formalized by `Cslib.Complexity.Karp.KGVerify.start`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#start).

## One step of a clique-verifier program to a known label

Let $M$ be a program that
assigns a verifier statement to each label, $\ell$ and $\ell'$ labels, $v$ a state and $S$
stack contents. If executing the statement $M(\ell)$ from state $v$ and stacks $S$ ends at
label $\ell'$, then there are a state $v'$ and stack contents $S'$ such that $M$ runs in
exactly one step from label $\ell$ with state $v$ and stacks $S$ to label $\ell'$ with
state $v'$ and stacks $S'$.

Formalized by `Cslib.Complexity.Karp.KGVerify.run_one`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#run-one).

## The clique verifier's unary reader succeeds

Let $m$ be a mode, $c$ a stack other
than the input stack $X$, and $\ell$, $\ell'$ labels such that the verifier program of
mode $m$ runs, at label $\ell$, the unary reader onto $c$ with own label $\ell$ and next
label $\ell'$. Let $k, j \in \mathbb{N}$, let $r$ be a list of bits, $v$ a state and $S$
stack contents in which $X$ holds, from the top, $k$ ones, then a zero, then the bits of
$r$, and $c$ holds exactly $j$ copies of the bit $1$. Then there are a state $v'$ and
stack contents $S'$ such that the program runs in exactly $k + 1$ steps from label $\ell$
with state $v$ and stacks $S$ to label $\ell'$ with state $v'$ and stacks $S'$, where in
$S'$ the stack $X$ holds the bits of $r$, the stack $c$ holds exactly $k + j$ copies of
the bit $1$, and every stack other than $X$ and $c$ is as in $S$.

Formalized by `Cslib.Complexity.Karp.KGVerify.readU_some`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#read-u-some).

## Reading an unterminated unary number rejects

Let $m$ be a mode, $c$ a stack other
than the input stack $X$, and $\lambda$, $\mu$ labels such that the verifier for $m$ runs at
$\lambda$ the unary reader onto $c$ that loops at $\lambda$ and exits to $\mu$. Let $l$ be a
list of Booleans from which no unary length can be read (it contains no false). Then for every
machine variable $v$ and all stack contents in which $X$ holds exactly the bits of $l$, the
verifier for $m$ goes from label $\lambda$ to the rejecting label no in at most $|l| + 1$
steps.

Formalized by `Cslib.Complexity.Karp.KGVerify.readU_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#read-u-none).

## Run of the load phase

Let $m$ be a mode, $n$ and $j$ natural numbers and $w$ and
$\mathit{acc}$ bit lists. Start the verifier for mode $m$ at the load label, in any internal
state, with $n$ in unary on the counter $N$, $j$ in unary on the counter $C$, $w$ on the witness
stack $W$ and $\mathit{acc}$ on the vertex stack $V$. Then within at most $n + 1$ steps the
machine reaches the walk label with its flag $c$ (the conjunction of the row's pair conditions
so far) set to true if $w$ has at least $n$ bits and exactly $j$ of its first $n$ bits are set,
and the reject label otherwise. In the first case $V$ then holds the first $n$ bits of $w$, bit
$n - 1$ on top, above $\mathit{acc}$, and the stacks $X$ and $T$ are unchanged.

Formalized by `Cslib.Complexity.Karp.KGVerify.load_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 501](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L501). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#load-run).

## Walking the pairs of one row of the clique verifier

Let $m$ be a mode and $s$ a bit.
Let $z = (z_0, \dots, z_{r-1})$ and $b = (b_0, \dots, b_{q-1})$ be lists of bits, $c$ a bit, $v$
a state and $S$ stack contents in which the vertex stack $V$ holds, from the top, the name bits
$z_0, \dots, z_{r-1}$ followed by the name bit $s$, and the input stack $X$ holds, from the top,
the name bits $b_0, \dots, b_{q-1}$. Then there are a state $v'$ and stack contents $S'$ such
that within at most $r + 1$ steps the verifier program of mode $m$ goes from the walk label with
flag $c$, state $v$ and stacks $S$ to state $v'$ and stacks $S'$ at the put-back label if
$r \le q$ and either $\mathrm{free}_m(s)$ holds (a vertex with chosen-flag $s$ settles its pairs
alone) or both $c$ and $\mathrm{sat}_m(b_t, z_t)$ for every $t < r$ hold (the pair condition
left to the later vertex, with pair bit $b_t$ and later-vertex flag $z_t$), and at the reject
label otherwise. Moreover, if $r \le q$, then in $S'$ the stack $V$ is empty, the scratch stack
$T$ holds $z_{r-1}, \dots, z_0$ from the top above its contents in $S$, and $X$ holds, from the
top, $b_r, \dots, b_{q-1}$.

Formalized by `Cslib.Complexity.Karp.KGVerify.walkRow_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 571](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L571). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#walk-row-run).

## One row of the clique verifier's walk

Let $m$ be a mode, $s_i$ a bit, $r$ and $b$
lists of bits, $v$ a state and $S$ stack contents in which the vertex stack $V$ holds, from
the top, the bits of the reverse $\rho$ of $r$ followed by $s_i$, the scratch stack $T$ is
empty, and the input stack $X$ holds the bits $b$. Call the row condition: $|r| \le |b|$,
and either $s_i$ is free for $m$ or $\mathrm{sat}_m(b_t, \rho_t)$ holds for every $t < |r|$
(indices from $0$). Then there are a state $v'$ and stack contents $S'$ such that within at
most $2|r| + 2$ steps the verifier program of mode $m$ goes from label walk(true) with
state $v$ and stacks $S$ to state $v'$ and stacks $S'$ at label walk(true) if the row
condition holds and at the rejecting label otherwise; and if the row condition holds, then
in $S'$ the stack $V$ holds the bits of $\rho$, $T$ is empty, and $X$ holds $b$ with its
first $|r|$ bits dropped.

Formalized by `Cslib.Complexity.Karp.KGVerify.row_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 610](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L610). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#row-run).

## All rows of the clique verifier's walk

Let $m$ be a mode, $r$ and $b$ lists of
bits, $v$ a state and $S$ stack contents in which the vertex stack $V$ holds, from the top,
the bits of the reverse of $r$ (so the last entry of $r$ is on top), the scratch stack $T$
is empty, and the input stack $X$ holds the bits $b$. Then there are a state $v'$ and stack
contents $S'$ such that within at most $|r|(2|r| + 2) + 1$ steps the verifier program of
mode $m$ goes from label walk(true) with state $v$ and stacks $S$ to state $v'$ and stacks
$S'$ at the accepting label if the row-by-row check of $r$ against $b$ holds for $m$, and
at the rejecting label otherwise.

Formalized by `Cslib.Complexity.Karp.KGVerify.rows_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 639](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L639). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#rows-run).

## The verifier machine for clique, independent set and vertex cover

Let $m$ be a
mode, $x$ and $w$ lists of bits, $v$ a state and $S$ stack contents in which the input
stack $X$ holds the bits of $x$, the witness stack $W$ holds the bits of $w$, and every other
stack is empty. Then there are a state $v'$ and stack contents $S'$ such that within at most
$8(|x| + |w| + 1)^3$ steps the verifier program of mode $m$ goes from the start label with
state $v$ and stacks $S$ to state $v'$ and stacks $S'$ at the accepting label if the
verifier check of mode $m$ accepts $x$ with witness $w$, and at the rejecting label
otherwise.

Formalized by `Cslib.Complexity.Karp.KGVerify.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 680](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L680). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#run).

## Distinctness of CLIQUE verifier pairs (moved alias)

Moved to `Cslib.Complexity.Karp.pairs_nodup` (`Karp.CliqueCorrect`).

Formalized by `Cslib.Complexity.Karp.KGVerify.pairs_nodup`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean, line 756](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueVerify.lean#L756). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#pairs-nodup).

## Karp adjacency of two literals

For literals $l = (x, p)$ and $l' = (x', q)$, each a
variable $x, x' \in \mathbb{N}$ with a polarity $p, q \in \{\mathrm{true}, \mathrm{false}\}$, the
adjacency bit of $l$ and $l'$ is false when they are complementary, that is $x = x'$ and
$p \ne q$, and true otherwise. It is the adjacency of two occurrences in different clauses in
Karp's graph.

Formalized by `Cslib.Complexity.Karp.EmitClique.adjL`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#adj-l).

## Row-by-row pair bits of an occurrence list

For a list of literal occurrences (clause
index, variable, polarity), the row-by-row pair bits are defined recursively: the empty list has
none, and for a list $o, o_1, \dots, o_k$ they are the adjacency bits of $o$ with
$o_k, \dots, o_1$, in that order, followed by the row-by-row pair bits of $o_1, \dots, o_k$.
Two occurrences are adjacent when they lie in different clauses and are not complementary.

Formalized by `Cslib.Complexity.Karp.EmitClique.bitsRec`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#bits-rec).

## Pair bits of an occurrence list, row by row

Let $o_0, \dots, o_{m-1}$ be a list of
literal occurrences (clause index, variable, polarity). The list of adjacency bits of $o_i$ and
$o_j$ over the pairs $(i, j)$ with $i < j < m$ in encoding order (rows $i$ ascending, and $j$
descending within a row) equals the recursive pair bits of the list, which are empty for the
empty list and otherwise are the adjacency bits of $o_0$ with $o_{m-1}, o_{m-2}, \dots, o_1$, in
this order, followed by the recursive pair bits of $o_1, \dots, o_{m-1}$. Two occurrences are
adjacent when they lie in different clauses and are not complementary.

Formalized by `Cslib.Complexity.Karp.EmitClique.pairBits_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#pair-bits-eq).

## Row-by-row pair bits see only adjacency

Call two literal occurrences (clause index,
variable, polarity) adjacent when they lie in different clauses and are not complementary. Let
$f$ be a map on occurrences such that $f(a)$ and $f(b)$ are adjacent exactly when $a$ and $b$
are, for all occurrences $a$ and $b$. Then for every list of occurrences $o_1, \dots, o_k$, the
row-by-row pair bits of $f(o_1), \dots, f(o_k)$ equal those of $o_1, \dots, o_k$.

Formalized by `Cslib.Complexity.Karp.EmitClique.bitsRec_map`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-04/index.html#bits-rec-map).

## Occurrences of a formula with a first clause

Let $C$ be a clause and $\varphi$ a CNF
formula, and write a literal occurrence as a pair $(i, \ell)$ of a clause index $i$ and a literal
$\ell$. The list of literal occurrences of the formula whose first clause is $C$ and whose
remaining clauses are those of $\varphi$ is the list of $(0, \ell)$ for the literals $\ell$ of $C$
in order, followed by the list of $(i + 1, \ell)$ for the occurrences $(i, \ell)$ of $\varphi$ in
order.

Formalized by `Cslib.Complexity.Karp.EmitClique.occs_cons`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#occs-cons).

## Polarity-first tokens of a literal

For a literal $(x, p)$ with variable index
$x \in \mathbb{N}$ and polarity $p$, the token list is the polarity marker symbol for $p$
followed by one name-bit symbol for each bit of the canonical binary representation of $x$
(least significant bit first, empty for $x = 0$), in order.

This is how the CLIQUE emitter writes a walked literal occurrence on its stack $D$, top first.

Formalized by `Cslib.Complexity.Karp.EmitClique.dTok`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#d-tok).

## Tokens of an item on the walked stack

An item of the stack $D$ is either $\mathrm{none}$,
standing for a clause marker, or an occurrence $(x, p)$ of the variable $x$ with polarity $p$. The
tokens of $\mathrm{none}$ are the single clause-marker symbol; the tokens of $(x, p)$ are the
polarity marker of $p$ followed by the binary encoding of $x$ as name-bit symbols.

Formalized by `Cslib.Complexity.Karp.EmitClique.itemTok`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#item-tok).

## Bits pushed by a walk of the CLIQUE emitter

Let $l = (x, p)$ be a literal occurrence
with name $x \in \mathbb{N}$ and polarity $p$, let $f$ be a Boolean, and let $ds$ be a list whose
items are literal occurrences or clause markers. The bit list $\mathrm{walkBits}(l, f, ds)$ is
defined by recursion on $ds$: it is empty if $ds$ is empty; if $ds$ is a clause marker followed
by $ds'$, it is $\mathrm{walkBits}(l, \mathrm{true}, ds')$; and if $ds$ is an occurrence $l'$
followed by $ds'$, it is the bit $f \wedge \mathrm{adj}(l, l')$ followed by
$\mathrm{walkBits}(l, f, ds')$. Here $\mathrm{adj}(l, l')$ is the Karp adjacency of literals: it
is false exactly when $l$ and $l'$ have the same name and opposite polarities.

The flag $f$ records whether a clause marker has been passed; while it is false, each occurrence
contributes a false bit.

Formalized by `Cslib.Complexity.Karp.EmitClique.walkBits`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#walk-bits).

## Walked items of a formula

For a CNF formula $\varphi$ with clauses $C_1, \dots, C_m$ in
order, the items of $\varphi$ are the list made of, for each $i = 1, \dots, m$ in turn, the
literals of $C_i$ in order, each as an occurrence item, followed by one clause-marker item
$\mathrm{none}$. These are the items on the stack $D$ once the clauses of $\varphi$ are walked.

Formalized by `Cslib.Complexity.Karp.EmitClique.items`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#items).

## Rows pushed for a clause's literals

For a list $I$ of items and literals
$l_1, \dots, l_k$, the rows are the concatenation, for $i = 1, \dots, k$ in turn, of the reverse
of the walk bits of $l_i$ with flag false over the items $l_{i+1}, \dots, l_k$ (as occurrence
items) followed by $I$. These are the bits pushed when the literals of a clause are walked above
the items $I$.

Formalized by `Cslib.Complexity.Karp.EmitClique.lrows`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#lrows).

## Row bits of a formula for the CLIQUE emitter

A literal is a pair $(x, s)$ of a variable
$x \in \mathbb{N}$ and a polarity $s$, and an item is a literal or a clause marker. For a literal
$\ell = (x, s)$, a Boolean $f$ and a list of items, the walk bits are defined by recursion on the
list: there are none for the empty list; for a list starting with a clause marker they are the
walk bits of the rest with $f$ replaced by true; for a list starting with a literal $(x', s')$
they are the bit "$f$ and not ($x = x'$ and $s \ne s'$)" followed by the walk bits of the rest
with the same $f$. For a list $\delta$ of items, the rows of a list of literals are none for the
empty list, and for a list $\ell_1, \dots, \ell_k$ with $k \ge 1$ they are the reverse of the walk
bits of $\ell_1$ with $f$ false over the list $\ell_2, \dots, \ell_k$ followed by $\delta$, then
the rows of $\ell_2, \dots, \ell_k$. The items of a CNF formula $\psi$ are, for each clause of
$\psi$ in order, its literals followed by a clause marker. The row bits of a CNF formula are
defined by recursion on its clauses: the empty formula has none, and for the formula with first
clause $C$ and remaining clauses $\varphi$ they are the rows of the literals of $C$ for $\delta$
the clause marker followed by the items of $\varphi$, followed by the row bits of $\varphi$.

Formalized by `Cslib.Complexity.Karp.EmitClique.rowsF`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#rows-f).

## Pair bits of a leading clause

Let $C$ be a clause and $\varphi$ a CNF formula. Let
$O_\varphi$ be the list of literal occurrences of $\varphi$ (clause index, variable, polarity),
with every clause index increased by $1$. Then the row-by-row pair bits of the list made of the
literals of $C$, each with clause index $0$, followed by $O_\varphi$, are the rows pushed for the
literals of $C$ walked above a clause marker and the items of $\varphi$, followed by the
row-by-row pair bits of $O_\varphi$.

Formalized by `Cslib.Complexity.Karp.EmitClique.bitsRec_clause`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#bits-rec-clause).

## The CLIQUE emitter's row bits are Karp's pair bits

For every CNF formula $\varphi$, the
row bits of $\varphi$ equal the pair bits of Karp's CLIQUE graph of $\varphi$: with
$o_0, \dots, o_{m-1}$ the literal occurrences of $\varphi$, these are, for the pairs $(i, j)$ with
$i < j < m$ in encoding order (rows $i$ ascending, and $j$ descending within a row), the bits
telling whether $o_i$ and $o_j$ lie in different clauses and are not complementary.

Formalized by `Cslib.Complexity.Karp.EmitClique.rowsF_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#rows-f-eq).

## Stacks of the SAT-to-CLIQUE emitter

The emitter has nine stacks: $T$ (tokens), $O$
(output), $A$ (the current name), $B$ (scratch), $D$ (walked occurrences), $E$ (the walk's other
side), $X$ (scratch), $C$ (the clause count) and $N$ (the occurrence count).

Formalized by `Cslib.Complexity.Karp.EmitClique.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#k).

## Stack alphabets of the CLIQUE emitter

In the CLIQUE emitter, the output stack $O$ has
the Booleans as its alphabet, and every other stack has the token symbols as its alphabet.

The counter stacks $C$ and $N$ hold copies of the clause marker.

Formalized by `Cslib.Complexity.Karp.EmitClique.Γ`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#untitled).

## Labels of the SAT-to-CLIQUE emitter

For bits $p, q, f, b$ the labels are
$\mathsf{start}$, $\mathsf{lits}$, $\mathsf{nm}(p)$, $\mathsf{walk}(p, f)$, $\mathsf{cmp}(p, q)$,
$\mathsf{res}(p, b)$, $\mathsf{rsA}(p)$, $\mathsf{rsD}(p)$, $\mathsf{mvN}(p, f)$,
$\mathsf{back}(p)$, $\mathsf{put}(p)$, $\mathsf{put2}(p)$, $\mathsf{put3}(p)$, $\mathsf{fin}$,
$\mathsf{finN}$, $\mathsf{fin2}$, $\mathsf{finC}$ and $\mathsf{done}$. Here $p$ is the polarity
of the current occurrence. $\mathsf{start}$ begins a clause and $\mathsf{lits}$ pops a literal
marker; $\mathsf{nm}$ moves its name to $A$; $\mathsf{walk}(p, f)$ walks $D$, where $f$ tells
whether a clause marker was passed; $\mathsf{cmp}(p, q)$, $\mathsf{res}$, $\mathsf{rsA}$ and
$\mathsf{rsD}$ compare with an occurrence of polarity $q$, push the bit $b$ and restore;
$\mathsf{mvN}$ moves that occurrence's name to $E$; $\mathsf{back}$ moves $E$ back to $D$;
$\mathsf{put}$, $\mathsf{put2}$ and $\mathsf{put3}$ put the current occurrence on $D$;
$\mathsf{fin}$ to $\mathsf{finC}$ push the instance prefix, and $\mathsf{done}$ halts.

Formalized by `Cslib.Complexity.Karp.EmitClique.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#lab).

## The CLIQUE emitter machine

The CLIQUE emitter is the multi-stack machine with stacks
$T, O, A, B, D, E, X, C, N$, a Boolean flag and the labels named below. The stack $O$ holds
Booleans and the others hold symbols, among them the bit symbols $\mathrm{bit}(b)$, the literal
symbols $\mathrm{lit}(p)$ and the clause marker $\mathrm{cl}$. Each test sets the flag to its
outcome, a pop that reads a polarity or a bit sets the flag to it, and other pops leave the flag
unchanged. To move the bits of $Y$ to $Z$ and then go to $\lambda$ means: while the top of $Y$ is
a bit symbol, pop it and push it onto $Z$; once $Y$ is empty or its top is another symbol, go to
$\lambda$ (the flag serves as scratch). The instruction at each label is as follows.

At $\mathrm{start}$: test whether $T$ is empty; if so go to $\mathrm{fin}$, else pop $T$, push
$\mathrm{cl}$ onto $D$ and onto $C$, and go to $\mathrm{lits}$. At $\mathrm{lits}$: test whether
the top of $T$ is a literal symbol; if so pop it, reading the polarity $q$ (true exactly for
$\mathrm{lit}(\mathrm{true})$), push $\mathrm{cl}$ onto $N$ and go to $\mathrm{nm}(q)$; else go
to $\mathrm{start}$. At $\mathrm{nm}(p)$: move the bits of $T$ to $A$, then go to
$\mathrm{walk}(p, \mathrm{false})$. At $\mathrm{walk}(p, f)$: test whether $D$ is empty; if so
go to $\mathrm{back}(p)$; else test whether the top of $D$ is $\mathrm{cl}$; if so pop it, push
$\mathrm{cl}$ onto $E$ and go to $\mathrm{walk}(p, \mathrm{true})$; else pop $D$, reading $q$
(true exactly for $\mathrm{lit}(\mathrm{true})$), push $\mathrm{lit}(q)$ onto $E$, and if $f$ go
to $\mathrm{cmp}(p, q)$, else push false onto $O$ and go to $\mathrm{mvN}(p, \mathrm{false})$.
At $\mathrm{cmp}(p, q)$: compare the bits of $A$ and $D$, that is, while both tops are bit
symbols of the same bit, pop both and push that bit symbol onto $X$ and onto $B$; when both bit
blocks end together go to $\mathrm{res}(p, b)$ with $b$ true exactly when $p = q$, and on a
mismatch (different bits, or one block ending first) go to $\mathrm{res}(p, \mathrm{true})$
without popping (the flag serves as scratch). At $\mathrm{res}(p, b)$: push $b$ onto $O$ and go
to $\mathrm{rsA}(p)$. At $\mathrm{rsA}(p)$: move the bits of $X$ to $A$, then go to
$\mathrm{rsD}(p)$. At $\mathrm{rsD}(p)$: move the bits of $B$ to $D$, then go to
$\mathrm{mvN}(p, \mathrm{true})$. At $\mathrm{mvN}(p, f)$: move the bits of $D$ to $E$, then go
to $\mathrm{walk}(p, f)$. At $\mathrm{back}(p)$: test whether $E$ is empty; if so go to
$\mathrm{put}(p)$; else test whether its top is $\mathrm{cl}$; if so pop it and push
$\mathrm{cl}$ onto $D$; else test whether its top is a literal symbol; if so pop it, reading $q$
(true exactly for $\mathrm{lit}(\mathrm{true})$), and push $\mathrm{lit}(q)$ onto $D$; else pop
it, reading $b$ (true exactly for $\mathrm{bit}(\mathrm{true})$), and push $\mathrm{bit}(b)$ onto
$D$; in these three cases stay at $\mathrm{back}(p)$. At $\mathrm{put}(p)$: move the bits of $A$
to $B$, then go to $\mathrm{put2}(p)$. At $\mathrm{put2}(p)$: move the bits of $B$ to $D$, then
go to $\mathrm{put3}(p)$. At $\mathrm{put3}(p)$: push $\mathrm{lit}(p)$ onto $D$ and go to
$\mathrm{lits}$. At $\mathrm{fin}$: push false onto $O$ and go to $\mathrm{finN}$. At
$\mathrm{finN}$: pop $N$, testing whether a symbol was popped; if so push true onto $O$ and stay,
else go to $\mathrm{fin2}$. At $\mathrm{fin2}$: push false onto $O$ and go to $\mathrm{finC}$. At
$\mathrm{finC}$: pop $C$, testing whether a symbol was popped; if so push true onto $O$ and stay,
else go to $\mathrm{done}$. At $\mathrm{done}$: halt.

Formalized by `Cslib.Complexity.Karp.EmitClique.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#prog).

## Start label of the CLIQUE emitter

The start label of the CLIQUE emitter machine is its
label $\mathsf{start}$.

Formalized by `Cslib.Complexity.Karp.EmitClique.start`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#start).

## Configuration stacks of the CLIQUE emitter

For a token stack $t$, an output stack $o$
of bits, stacks $a$, $d$, $e$ of token symbols and natural numbers $c$ and $n$, this assigns to
each stack of the CLIQUE emitter its contents: the token stack $T$ holds $t$, the output stack
$O$ holds $o$, the name stack $A$ holds $a$, the walked-occurrence stack $D$ holds $d$, the
walk's other stack $E$ holds $e$, the clause counter $C$ holds $c$ copies of the clause marker,
the occurrence counter $N$ holds $n$ copies of the clause marker, and the scratch stacks $B$ and
$X$ are empty.

Formalized by `Cslib.Complexity.Karp.EmitClique.st`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#st).

## CLIQUE emitter: recognizing a standard state

Let $S$ assign contents to the stacks of
the CLIQUE emitter and let $c, n \in \mathbb{N}$. If the scratch stacks $B$ and $X$ are empty and
the counters $C$ and $N$ hold exactly $c$ and $n$ clause markers, then $S$ is the standard state
whose stacks $T$, $O$, $A$, $D$, $E$ hold what they hold in $S$, whose stacks $B$ and $X$ are
empty and whose counters $C$ and $N$ hold $c$ and $n$ clause markers.

Formalized by `Cslib.Complexity.Karp.EmitClique.st_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#st-eq).

## Tokens moved by the walk

A symbol is a token of the walk between the stacks $D$ and $E$
when it is a name bit, a literal marker or a clause marker; the value symbols and the dead
symbol are not.

Formalized by `Cslib.Complexity.Karp.EmitClique.isTok`, a definition declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#is-tok).

## Name bits of a variable in the CLIQUE emitter

For $x \in \mathbb{N}$, the name of $x$ is
the list of symbols obtained from the binary encoding of $x$ (least significant bit first, empty
for $x = 0$) by writing each bit $b$ as the bit symbol $\mathrm{bit}(b)$. This is the form in which
the stacks $A$ and $D$ of the CLIQUE emitter hold variable names.

Formalized by `Cslib.Complexity.Karp.EmitClique.name`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#name).

## CLIQUE emitter: reading a variable name

Stacks are listed top first. Let $p$ be a Boolean,
$x \in \mathbb{N}$ with name $w$ (its binary encoding written as bit symbols) of length $\ell$, and
$R$ a list of symbols that is empty or whose top symbol is not a bit symbol. Let $v$ be a flag,
$o$ a list of Booleans, $d$ and $e$ lists of symbols, and $c, n \in \mathbb{N}$. Started at label
$\mathrm{nm}(p)$ with flag $v$, the token stack $T$ holding $w$ reversed on top of $R$, empty
stacks $A$, $B$, $X$, stacks $O$, $D$, $E$ holding $o$, $d$, $e$, and $c$ and $n$ clause markers
on the counters $C$ and $N$, the CLIQUE emitter reaches, in exactly $\ell + 1$ steps and with
some flag, the label $\mathrm{walk}(p, \mathrm{false})$ with $T$ holding $R$, $A$ holding $w$,
and all other stacks as before.

Formalized by `Cslib.Complexity.Karp.EmitClique.nm_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#nm-run).

## Moving a walked name from $D$ to $E$

Write
$\langle \ell, v \mid t, o, a, d, e, c, n\rangle$ for the configuration of the SAT-to-CLIQUE
emitter at label $\ell$ with local bit $v$, stacks $T = t$, $O = o$, $A = a$, $D = d$, $E = e$,
empty scratch stacks $B$ and $X$, and $c$ and $n$ marks on the counters $C$ and $N$;
juxtaposition of lists is concatenation. Let $p, f$ be bits, $w$ a list of bits with $\bar w$ the
corresponding list of name-bit symbols, $R$ a list of symbols that is empty or does not start
with a name-bit symbol, and $t, o, a, e, c, n, v$ arbitrary. Then for some bit $v'$ the machine
goes in exactly $|w| + 1$ steps from
$\langle \mathsf{mvN}(p, f), v \mid t, o, a, \bar w R, e, c, n\rangle$ to
$\langle \mathsf{walk}(p, f), v' \mid t, o, a, R, \bar w^{\mathrm{rev}} e, c, n\rangle$, where
$\bar w^{\mathrm{rev}}$ is the reverse of $\bar w$.

Formalized by `Cslib.Complexity.Karp.EmitClique.mvN_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-05/index.html#mv-n-run).

## Clique emitter: comparing two names

Let $p$, $q$ and $v$ be Booleans, $u$ and $w$ lists
of bits, $t$, $e$ and $R$ stack-symbol lists with $R$ empty or not starting with a name bit, $o$
a list of bits and $c, n \in \mathbb{N}$. Let $b$ be $(p = q)$ if $u = w$ and true otherwise.
For some flag $v'$, the emitter machine goes in at most $3|w| + 4$ steps from label
$\mathrm{cmp}(p, q)$ with flag $v$ and the state with token stack $t$, output $o$, name stack
$u$, walked stack $w$ followed by $R$, walk side $e$, clause count $c$, occurrence count $n$ and
empty scratch stacks to label $\mathrm{mvN}(p, \mathrm{true})$ with flag $v'$ and the same state
except that the output is $b$ followed by $o$. Here $u$ and $w$ lie on the stacks as name-bit
symbols.

Formalized by `Cslib.Complexity.Karp.EmitClique.cmp_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#cmp-run).

## CLIQUE emitter: putting the current occurrence on the walked stack

Stacks are listed top
first. Let $p$ be a Boolean, $u$ a list of Booleans and $\bar u$ the list of bit symbols
$\mathrm{bit}(b)$ for $b$ in $u$, let $v$ be a flag, $t$, $d$, $e$ lists of symbols, $o$ a list of
Booleans and $c, n \in \mathbb{N}$. Started at label $\mathrm{put}(p)$ with flag $v$, stacks $T$,
$O$, $A$, $D$, $E$ holding $t$, $o$, $\bar u$, $d$, $e$, empty scratch stacks $B$ and $X$, and $c$
and $n$ clause markers on the counters $C$ and $N$, the CLIQUE emitter reaches, in exactly
$2|u| + 3$ steps and with some flag, the label $\mathrm{lits}$ with $A$ empty, $D$ holding the
literal marker $\mathrm{lit}(p)$ on top of $\bar u$ on top of $d$, and all other stacks as before.

The name goes from $A$ to $D$ through $B$, so it is reversed twice.

Formalized by `Cslib.Complexity.Karp.EmitClique.put_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#put-run).

## Clique emitter: moving the walk side back

Let $p$ and $v$ be Booleans, $t$, $a$ and $d$
stack-symbol lists, $o$ a list of bits, $c, n \in \mathbb{N}$, and let $L$ be a list of stack
symbols each of which is a name bit, a polarity marker or a clause marker. From label
$\mathrm{back}(p)$ with flag $v$ and the state with token stack $t$, output $o$, name stack $a$,
walked stack $d$, walk side $L$, clause count $c$, occurrence count $n$ and empty scratch stacks,
the emitter machine reaches in exactly $|L| + 1$ steps, for some flag $v'$, label
$\mathrm{put}(p)$ with flag $v'$ and the same state except that the walked stack is the reverse
of $L$ followed by $d$ and the walk side is empty.

Formalized by `Cslib.Complexity.Karp.EmitClique.back_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#back-run).

## Clique emitter: the instance prefix

Let $v$ be a Boolean, $d$ and $e$ stack-symbol lists,
$o$ a list of bits and $c, n \in \mathbb{N}$. From label fin with flag $v$ and the state with
empty token stack, output $o$, empty name stack, walked stack $d$, walk side $e$, clause count
$c$, occurrence count $n$ and empty scratch stacks, the emitter machine reaches in exactly
$n + c + 4$ steps label done with some flag and some state whose output, read top-down, is $c$
ones, false, $n$ ones, false, then $o$.

Formalized by `Cslib.Complexity.Karp.EmitClique.fin_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#fin-run).

## Reversing a list preserves the length of a flat map

Let $\alpha$ and $\beta$ be types,
$l$ a list of elements of $\alpha$ and $f$ a function from $\alpha$ to lists of elements of
$\beta$. Concatenating the lists $f(a)$ for $a$ running through the reverse of $l$ gives a list
of the same length as concatenating them for $a$ running through $l$.

Formalized by `Cslib.Complexity.Karp.EmitClique.flatMap_reverse_length`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#flat-map-reverse-length).

## Walk over the occurrence stack in the CLIQUE emitter

Let $l = (x, p)$ be a literal
occurrence, $ds$ a list of items (literal occurrences or clause markers), $f$ and $v$ Booleans,
$t$ a token stack, $o$ an output stack of bits, $e$ a stack of token symbols and
$c, n \in \mathbb{N}$. Let $D$ be the concatenation of the tokens of the items of $ds$: a clause
marker for a clause marker, and the polarity marker of $l'$ above the name bits of $l'$ (the
binary encoding of its name as bit symbols) for an occurrence $l'$. Start the CLIQUE emitter at
label $\mathsf{walk}(p, f)$ with internal variable $v$, on the configuration stacks with token
stack $t$, output $o$, name stack the name bits of $x$, walked-occurrence stack $D$, other walk
stack $e$ and counts $c$ and $n$. Then for some Boolean $v'$ the machine reaches, in at most
$6\,|D| + 1$ steps, label $\mathsf{back}(p)$ with internal variable $v'$ on the configuration
stacks with token stack $t$, output stack the reverse of $\mathrm{walkBits}(l, f, ds)$ followed
by $o$, name stack the name bits of $x$, empty walked-occurrence stack, other walk stack the
reverse of $D$ followed by $e$, and counts $c$ and $n$.

Formalized by `Cslib.Complexity.Karp.EmitClique.walk_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 597](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L597). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#walk-run).

## Emitter run over one literal occurrence

Write
$\langle \ell, v \mid t, o, a, d, e, c, n\rangle$ for the configuration of the SAT-to-CLIQUE
emitter at label $\ell$ with local bit $v$, stacks $T = t$, $O = o$, $A = a$, $D = d$, $E = e$,
empty scratch stacks $B$ and $X$, and $c$ and $n$ marks on the counters $C$ and $N$;
juxtaposition of lists is concatenation. Let $l = (x, p)$ be a literal, $R$ a list of symbols that
is empty or does not start with a name-bit symbol, $I$ a list of items, $o$ a list of bits,
$c, n \in \mathbb{N}$ and $v$ a bit. Let $\delta$ be the concatenation of the tokens of the items
of $I$, $\lambda$ the token list of $l$ as it lies on the token stack, $\rho$ the reverse of the
walk bits of $l$ with flag false over $I$, and $\delta'$ the concatenation of the tokens of the
item $l$ followed by those of $I$. Then for some bit $v'$ the machine goes in at most
$7|\delta| + 3|\mathrm{enc}(x)| + 7$ steps, where $\mathrm{enc}(x)$ is the binary encoding of $x$,
from $\langle \mathsf{lits}, v \mid \lambda R, o, [], \delta, [], c, n\rangle$ to
$\langle \mathsf{lits}, v' \mid R, \rho\, o, [], \delta', [], c, n + 1\rangle$.

Formalized by `Cslib.Complexity.Karp.EmitClique.lit_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#lit-run).

## Emitter run over a clause's literals

Write
$\langle \ell, v \mid t, o, a, d, e, c, n\rangle$ for the configuration of the SAT-to-CLIQUE
emitter at label $\ell$ with local bit $v$, stacks $T = t$, $O = o$, $A = a$, $D = d$, $E = e$,
empty scratch stacks $B$ and $X$, and $c$ and $n$ marks on the counters $C$ and $N$;
juxtaposition of lists is concatenation. Let $L, c \in \mathbb{N}$, let $I$ be a list of items
and $\delta$ the concatenation of their tokens, let $l_1, \dots, l_k$ be literals, $R$ a list of
symbols that is empty or does not start with a name-bit symbol, $o$ a list of bits,
$n \in \mathbb{N}$ and $v$ a bit. Let $\lambda_i$ be the token list of $l_i$ as it lies on the
token stack and $\Lambda = |\lambda_1| + \dots + |\lambda_k|$. If $\Lambda + |\delta| \le L$, then
for some bit $v'$ the machine goes in at most $\Lambda (7L + 7)$ steps from
$\langle \mathsf{lits}, v \mid \lambda_k \cdots \lambda_1 R, o, [], \delta, [], c, n\rangle$ to
$\langle \mathsf{lits}, v' \mid R, \rho\, o, [], \delta', [], c, n + k\rangle$, where $\rho$ is the
rows pushed for the literals $l_1, \dots, l_k$ above the items $I$ and $\delta'$ is the
concatenation of the tokens of the items $l_1, \dots, l_k$ followed by those of $I$.

Formalized by `Cslib.Complexity.Karp.EmitClique.lits_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#lits-run).

## Clique emitter: one clause

Let $C$ be a clause, $\varphi$ a CNF formula, $R$ a token list
that is empty or starts with a clause marker, $o$ a list of bits, $c, n, B \in \mathbb{N}$ and $v$
a Boolean. Write $T_C$ for the tokens of $C$ as they lie on the token stack (a clause marker,
then the literals last-first) and $D_\psi$ for the tokens of the items of a formula $\psi$. If
$|T_C| + |D_\varphi| \le B$, then for some flag $v'$ the emitter machine goes in at most
$|T_C| \cdot (7B + 7)$ steps from label start with flag $v$ and the state with token stack $T_C$
followed by $R$, output $o$, walked stack $D_\varphi$, clause count $c$, occurrence count $n$ and
all other stacks empty, to label start with flag $v'$ and the state with token stack $R$, output
the rows pushed for the literals of $C$ walked above a clause marker and the items of $\varphi$,
followed by $o$, walked stack $D_{C \varphi}$ for the formula $C\varphi$ with first clause $C$,
clause count $c + 1$, occurrence count $n + |C|$ and all other stacks empty.

Formalized by `Cslib.Complexity.Karp.EmitClique.clause_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 713](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L713). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#clause-run).

## Emitter run over a formula's clauses

Write
$\langle \ell, v \mid t, o, a, d, e, c, n\rangle$ for the configuration of the SAT-to-CLIQUE
emitter at label $\ell$ with local bit $v$, stacks $T = t$, $O = o$, $A = a$, $D = d$, $E = e$,
empty scratch stacks $B$ and $X$, and $c$ and $n$ marks on the counters $C$ and $N$;
juxtaposition of lists is concatenation. Let $L \in \mathbb{N}$, let $\varphi$ be a CNF formula
with clauses $C_1, \dots, C_m$ in order, let $R$ be a list of symbols that is empty or starts
with the clause marker, $o$ a list of bits and $v$ a bit. Let $\kappa_i$ be the token list of
$C_i$ as it lies on the token stack and $\tau = \kappa_m \cdots \kappa_1$. If $|\tau| \le L$,
then for some bit $v'$ the machine goes in at most $|\tau| (7L + 7)$ steps from
$\langle \mathsf{start}, v \mid \tau R, o, [], [], [], 0, 0\rangle$ to
$\langle \mathsf{start}, v' \mid R, \rho\, o, [], \delta, [], m, s\rangle$, where $\rho$ is the
row bits of $\varphi$, $\delta$ is the concatenation of the tokens of the items of $\varphi$ and
$s = |C_1| + \dots + |C_m|$ is the total number of literals of $\varphi$.

Formalized by `Cslib.Complexity.Karp.EmitClique.formula_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 739](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L739). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#formula-run).

## The CLIQUE emitter computes Karp's instance in cubic time

Let $\varphi$ be a CNF formula
with token list $\tau$ (in reading order), $o$ a list of Booleans, $v$ a flag, and $S$ stack
contents in which the token stack $T$ holds $\tau$ reversed (stacks are listed top first), the
output stack $O$ holds $o$ and every other stack is empty. Started at its start label with flag
$v$ and stacks $S$, the CLIQUE emitter reaches the label $\mathrm{done}$ in at most
$8(|\tau| + 1)^3$ steps, with some flag and stacks $S'$ such that $O$ holds, in $S'$, Karp's
CLIQUE instance of $\varphi$ followed by $o$.

Formalized by `Cslib.Complexity.Karp.EmitClique.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean, line 771](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueEmit.lean#L771). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#run).

## Modes of the CLIQUE/VERTEX-COVER reduction machine

A mode is one of two values, the
flip mode and the vertex-cover mode. They select the reduction that the machine of this module
computes: CLIQUE to INDEPENDENT-SET in the flip mode, INDEPENDENT-SET to VERTEX-COVER in the
vertex-cover mode.

Formalized by `Cslib.Complexity.Karp.KGMap.Mode`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#mode).

## Reduction computed in each mode

The map on bit strings that a mode of the
CLIQUE/VERTEX-COVER reduction machine computes: in the flip mode it is the reduction from CLIQUE
to INDEPENDENT-SET on bit strings, and in the vertex-cover mode it is the reduction from
INDEPENDENT-SET to VERTEX-COVER on bit strings.

Formalized by `Cslib.Complexity.Karp.KGMap.Mode.f`, a definition declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#f).

## Stacks of the CLIQUE to VERTEX-COVER reduction machine

Stacks: input `X`, output `O`, counters `A` (`k`), `B` (`n`), `D` (`n`, then `n - k`), and
the reversed pair bits `Y`.

Formalized by `Cslib.Complexity.Karp.KGMap.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#k).

## Stack alphabets of the clique reduction machine

The alphabet $\Gamma(k)$ of a stack $k$
is the Booleans if $k$ is the output stack $O$, and the token alphabet $\mathrm{Sym}$ for every
other stack ($X$, $A$, $B$, $D$ and $Y$).

Formalized by `Cslib.Complexity.Karp.KGMap.Γ`, a definition declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#untitled).

## Labels of the KG-map machine

The type of the ten instruction labels of the KG-map
machine: read $k$, read $n$, move the pair bits, subtract, output the pair bits, output $n$, write
the separator, output the last number, the failure label and the halting label.

The machine reaches the subtraction label only in the vertex-cover mode, and at the failure label
it writes the fixed no-instance.

Formalized by `Cslib.Complexity.Karp.KGMap.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#lab).

## Counter unit symbol of the clique reduction machine

$U$ is the symbol $\mathsf{cl}$ of
the token alphabet $\mathrm{Sym}$.

It is the unit of the counter stacks $A$, $B$ and $D$, which hold a number $n$ as $n$ copies of
$U$.

Formalized by `Cslib.Complexity.Karp.KGMap.U`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#u).

## Test for the input bit true

A test on the result of popping a stack: it is true
exactly when a symbol was popped and that symbol is $\mathrm{bit}(\mathrm{true})$, and false for
every other symbol and for an empty stack.

Formalized by `Cslib.Complexity.Karp.KGMap.isT`, a definition declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#is-t).

## Test for the moved bit true

A test on the result of popping a stack: it is true
exactly when a symbol was popped and that symbol is $\mathrm{val}(\mathrm{true})$, and false for
every other symbol and for an empty stack.

Formalized by `Cslib.Complexity.Karp.KGMap.isV`, a definition declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#is-v).

## Pair-bit transform of each mode

For a mode of the CLIQUE/VERTEX-COVER reduction
machine, the map on booleans applied to each pair bit as it is written to the output: negation in
the flip mode and the identity in the vertex-cover mode.

Formalized by `Cslib.Complexity.Karp.KGMap.Mode.fb`, a definition declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-06/index.html#fb).

## Label after the move phase of the KG-map machine

The map from the modes of the KG-map
machine to its labels that sends the flip mode to the label output the pair bits and the
vertex-cover mode to the subtraction label. The machine goes to this label after moving the pair
bits.

Formalized by `Cslib.Complexity.Karp.KGMap.Mode.next`, a definition declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#next).

## Counter of the first output number of the KG-map machine

The map from the modes of the
KG-map machine to its stacks that sends the flip mode to the counter $A$ and the vertex-cover
mode to the counter $D$.

This is the counter the machine drains last, as the first number of its output: $A$ holds $k$,
and in the vertex-cover mode $D$ holds $n - k$ by then.

Formalized by `Cslib.Complexity.Karp.KGMap.Mode.ctr`, a definition declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#ctr).

## The KG-map machine

For a mode $m$ (flip or vc), the KG-map machine $M_m$ is the
multi-stack machine with stacks $X$, $A$, $B$, $D$, $Y$ of symbols and an output stack $O$ of
bits, whose labels act as follows; the counters $A$, $B$, $D$ use a fixed unit symbol.

- Read $k$: if $X$ is empty, go to the failure label. Otherwise pop $X$; if the popped symbol is
  the input bit $\mathrm{bit}(\mathit{true})$, push a unit onto $A$ and repeat, else go to read $n$.
- Read $n$: if $X$ is empty, go to the failure label. Otherwise pop $X$; if the popped symbol is
  $\mathrm{bit}(\mathit{true})$, push a unit onto $B$ and onto $D$ and repeat, else go to move.
- Move: if $X$ is empty, go to output pair bits (flip) or subtract (vc). Otherwise pop $X$, push
  $\mathrm{val}(b)$ onto $Y$, where $b$ is true exactly when the popped symbol was
  $\mathrm{bit}(\mathit{true})$, and repeat.
- Subtract: pop $A$. If $A$ was empty, go to output pair bits. Otherwise pop $D$; if $D$ was
  nonempty repeat, else go to the failure label.
- Output pair bits: if $Y$ is empty, push false onto $O$ and go to output $n$. Otherwise pop $Y$,
  push $\beta_m(b)$ onto $O$, where $b$ is true exactly when the popped symbol was
  $\mathrm{val}(\mathit{true})$ and $\beta_m$ is negation for flip and the identity for vc, and
  repeat.
- Output $n$: pop $B$; if $B$ was nonempty, push true onto $O$ and repeat, else go to separator.
- Separator: push false onto $O$ and go to output last number.
- Output last number: as output $n$, but popping the counter of $m$ ($A$ for flip, $D$ for vc)
  and going to the halting label when it is empty.
- Failure: push the bits true, false, false of the fixed no-instance (the encoding of $k = 1$ on
  the empty graph) onto $O$ so that $O$ starts with them, and go to the halting label.
- Halting label: halt.

Formalized by `Cslib.Complexity.Karp.KGMap.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#prog).

## Start label of the KG-map machine

The KG-map machine starts at the label read $k$.

Formalized by `Cslib.Complexity.Karp.KGMap.start`, a definition declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#start).

## Reading the first unary number in the KG-map machine

Let $m$ be a mode, $k$ and $i$
natural numbers and $r$ a list of bits. Consider a configuration of the KG-map machine $M_m$ at
the label read $k$, with any internal bit, in which stack $X$ holds the input symbols
$\mathrm{bit}(b)$ for the bits $b$ of the list of $k$ trues, a false and then $r$, top first, and
stack $A$ holds $i$ copies of the unit symbol. Then in exactly $k + 1$ steps $M_m$ reaches the
label read $n$ with $X$ holding $\mathrm{bit}(b)$ for the bits $b$ of $r$, $A$ holding $i + k$
copies of the unit symbol, and every stack other than $X$ and $A$ unchanged.

Formalized by `Cslib.Complexity.Karp.KGMap.rdK_some`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#rd-k-some).

## Unterminated first unary number in the KG-map machine

Let $m$ be a mode and $r$ a list
of bits on which reading a unary length prefix fails (this happens exactly when $r$ contains no
false). From any configuration of the KG-map machine $M_m$ at the label read $k$, with any
internal bit, in which stack $X$ holds the input symbols $\mathrm{bit}(b)$ for the bits $b$ of
$r$, top first, $M_m$ reaches the failure label in exactly $|r| + 1$ steps, with every stack
other than $X$ and $A$ unchanged.

Formalized by `Cslib.Complexity.Karp.KGMap.rdK_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#rd-k-none).

## Reading the second unary number in the KG-map machine

Let $m$ be a mode, $n$ and $i$
natural numbers and $r$ a list of bits. Consider a configuration of the KG-map machine $M_m$ at
the label read $n$, with any internal bit, in which stack $X$ holds the input symbols
$\mathrm{bit}(b)$ for the bits $b$ of the list of $n$ trues, a false and then $r$, top first, and
stacks $B$ and $D$ each hold $i$ copies of the unit symbol. Then in exactly $n + 1$ steps $M_m$
reaches the label move with $X$ holding $\mathrm{bit}(b)$ for the bits $b$ of $r$, $B$ and $D$
each holding $i + n$ copies of the unit symbol, and every stack other than $X$, $B$ and $D$
unchanged.

Formalized by `Cslib.Complexity.Karp.KGMap.rdN_some`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#rd-n-some).

## Unterminated second unary number in the KG-map machine

Let $m$ be a mode and $r$ a list
of bits on which reading a unary length prefix fails (this happens exactly when $r$ contains no
false). From any configuration of the KG-map machine $M_m$ at the label read $n$, with any
internal bit, in which stack $X$ holds the input symbols $\mathrm{bit}(b)$ for the bits $b$ of
$r$, top first, $M_m$ reaches the failure label in exactly $|r| + 1$ steps, with every stack
other than $X$, $B$ and $D$ unchanged.

Formalized by `Cslib.Complexity.Karp.KGMap.rdN_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#rd-n-none).

## Moving the pair bits onto stack $Y$

Fix a mode $m$ of the CLIQUE/VERTEX-COVER
reduction machine, a list of bits $r$ and a list of symbols $y$. Start the machine for $m$ at the
label for moving the pair bits, with any internal state and any stacks such that stack $X$ holds
$r$ as the symbols $\mathrm{bit}(b)$ and stack $Y$ holds $y$. Then after exactly $|r| + 1$ steps
it is at the label that follows moving the pair bits in mode $m$, with some internal state and
stacks in which $Y$ holds the symbols $\mathrm{val}(b)$ for the bits $b$ of $r$, in reverse
order, on top of $y$, and every stack other than $X$ and $Y$ is unchanged.

Formalized by `Cslib.Complexity.Karp.KGMap.mv_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#mv-run).

## Subtraction loop of the clique reduction machine

Let $m$ be a mode of the machine, let
$k \le n$ be natural numbers, and let $S$ be stack contents in which the counter stack $A$ holds
$U^k$ ($k$ copies of the unit symbol $U$) and the counter stack $D$ holds $U^n$. Then for every
Boolean local state $v$ there are a local state $v'$ and stack contents $S'$ such that the machine
of mode $m$ runs in exactly $k + 1$ steps from label $\mathsf{sub}$ with local state $v$ and
stacks $S$ to label $\mathsf{outY}$ with local state $v'$ and stacks $S'$, the stack $D$ of $S'$
holds $U^{n-k}$, and every stack other than $A$ and $D$ has the same contents in $S'$ as in $S$.

Formalized by `Cslib.Complexity.Karp.KGMap.sub_le`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#sub-le).

## Failed subtraction in the KG-map machine

Let $m$ be a mode and $n < k$ natural numbers.
From any configuration of the KG-map machine $M_m$ at the label subtract, with any internal bit,
in which stack $A$ holds $k$ copies of the unit symbol and stack $D$ holds $n$ copies, $M_m$
reaches the failure label in exactly $n + 1$ steps, with every stack other than $A$ and $D$
unchanged.

Formalized by `Cslib.Complexity.Karp.KGMap.sub_gt`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#sub-gt).

## Output loop for the pair bits of the KG-map machine

Let $m$ be a mode and $y$ and $o$
lists of bits. Consider a configuration of the KG-map machine $M_m$ at the label output pair
bits, with any internal bit, in which stack $Y$ holds the symbols $\mathrm{val}(b)$ for the bits
$b$ of $y$, the first bit of $y$ on top, and the output stack $O$ holds $o$. Then in exactly
$|y| + 1$ steps $M_m$ reaches the label output $n$ with $O$ equal, top first, to false, then the
reverse of $\beta_m(y)$, then $o$, where $\beta_m$ negates every bit for flip and leaves the
bits unchanged for vc; every stack other than $Y$ and $O$ is unchanged.

Formalized by `Cslib.Complexity.Karp.KGMap.outY_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#out-y-run).

## Number output of the clique reduction machine

Let $m$ be a mode of the machine and $C$
its final counter stack ($A$ for the flip mode, $D$ for the vertex-cover mode). Let $n, c$ be
natural numbers, $u$ a symbol of the alphabet of $C$, and $S$ stack contents in which the stack
$B$ holds $U^n$ ($n$ copies of the unit symbol $U$) and $C$ holds $u^c$. Then for every Boolean
local state $v$ there are a local state $v'$ and stack contents $S'$ such that the machine of
mode $m$ runs in exactly $n + c + 3$ steps from label $\mathsf{outB}$ with local state $v$ and
stacks $S$ to label $\mathsf{done}$ with local state $v'$ and stacks $S'$, and the output stack
$O$ of $S'$ holds, from the top, $c$ copies of $\mathrm{true}$, then $\mathrm{false}$, then $n$
copies of $\mathrm{true}$, then the contents of $O$ in $S$.

Formalized by `Cslib.Complexity.Karp.KGMap.tail_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#tail-run).

## Output phase of the KG-map machine

Let $m$ be a mode, $r$ a list of bits and $n$ and
$c$ natural numbers. Consider a configuration of the KG-map machine $M_m$ at the label output
pair bits, with any internal bit, in which stack $Y$ holds the symbols $\mathrm{val}(b)$ for the
bits $b$ of $r$ in reverse order (the last bit of $r$ on top), stack $B$ holds $n$ copies of the
unit symbol, the counter of $m$ ($A$ for flip, $D$ for vc) holds $c$ copies of some symbol, and
the output stack $O$ is empty. Then in exactly $|r| + n + c + 4$ steps $M_m$ reaches the halting
label with $O$ equal, top first, to the encoding of the instance with numbers $c$ and $n$ and
pair bits $\beta_m(r)$: $c$ trues, a false, $n$ trues, a false, then $\beta_m(r)$, where
$\beta_m$ negates every bit for flip and leaves the bits unchanged for vc.

Formalized by `Cslib.Complexity.Karp.KGMap.out_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#out-run).

## Correctness and running time of the KG-map machine

Let $m$ be a mode and $x$ a list of
bits, and let $F_m$ be the clique-to-independent-set map on bit strings for flip and the
independent-set-to-vertex-cover map for vc. From any configuration of the KG-map machine $M_m$
at its start label, with any internal bit, in which stack $X$ holds the input symbols
$\mathrm{bit}(b)$ for the bits $b$ of $x$, top first, and every other stack is empty, $M_m$
reaches the halting label in at most $3(|x| + 1)$ steps with the output stack $O$ equal to
$F_m(x)$, top first.

Formalized by `Cslib.Complexity.Karp.KGMap.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/KGMap.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/KGMap.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#run).

## The CLIQUE-to-INDEPENDENT-SET and INDEPENDENT-SET-to-VERTEX-COVER map as a host component

**The CLIQUE-to-INDEPENDENT-SET and INDEPENDENT-SET-to-VERTEX-COVER map as a host
component.** For a mode $m$, standing for the reduction from CLIQUE to INDEPENDENT-SET or the one
from INDEPENDENT-SET to VERTEX-COVER, this is the host component whose stacks (listed as
$X, O, A, B, D, Y$), stack alphabets, labels and program are those of the Turing machine that
computes the reduction of mode $m$.

Formalized by `Cslib.Complexity.Karp.kgMapComp`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#kg-map-comp).

## CLIQUE ≤ INDEPENDENT-SET is polynomial-time

The map on bit strings that sends
$1^k 0 1^n 0 b$, for natural numbers $k$ and $n$ and a bit string $b$, to $1^k 0 1^n 0 \bar b$,
where $\bar b$ is $b$ with every bit complemented, and sends every string not of this form to the
string $100$, is computable in polynomial time.

Formalized by `Cslib.Complexity.Karp.isPolyTime_flipKG`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#is-poly-time-flip-kg).

## INDEPENDENT-SET ≤ VERTEX-COVER is polynomial-time

The map on bit strings that sends
$1^k 0 1^n 0 b$, for natural numbers $k \le n$ and a bit string $b$, to $1^{n-k} 0 1^n 0 b$, and
sends every other string (including $1^k 0 1^n 0 b$ with $k > n$) to the string $100$, is
computable in polynomial time.

Formalized by `Cslib.Complexity.Karp.isPolyTime_isToVc`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#is-poly-time-is-to-vc).

## The CLIQUE emitter

The emitter given by the CLIQUE emitter machine, run from its start
label to its exit label, with token stack $T$ and output stack $O$. Its output on a CNF formula
$\varphi$ is Karp's CLIQUE instance of $\varphi$, its output on undecodable input is the string
$100$, and its step bound on $m$ tokens is $8(m + 1)^3$. Let $\varphi$ be a CNF formula with $m$
tokens. Started with the tokens of $\varphi$ on $T$, last token on top, and all other stacks
empty, the machine reaches its exit label within $8(m + 1)^3$ steps, with Karp's CLIQUE instance
of $\varphi$ on $O$, first bit on top.

Formalized by `Cslib.Complexity.Karp.emitClique`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#emit-clique).

## SAT ≤ CLIQUE is polynomial-time

Let $f$ be the map on bit strings that sends the
binary code of a CNF formula $\varphi$ to the encoding of Karp's CLIQUE instance $(k, G)$ of
$\varphi$, and sends every string that is not the code of a CNF formula to the string $100$.
Here $G$ has one vertex per literal occurrence in $\varphi$, two occurrences are adjacent when
they lie in different clauses and are not complementary, and $k$ is the number of clauses of
$\varphi$. Then $f$ is computable in polynomial time.

Formalized by `Cslib.Complexity.Karp.isPolyTime_reduceClique`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-07/index.html#is-poly-time-reduce-clique).

## CLIQUE is NP-hard

Every decision problem $L$ in NP has a polynomial-time many-one
reduction to CLIQUE: a polynomial-time computable map $f$ on bit strings such that, for every
bit string $x$, $L$ accepts $x$ exactly when CLIQUE accepts $f(x)$.

Formalized by `Cslib.Complexity.Karp.cliqueDec_npHard`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-08/index.html#clique-dec-np-hard).

## INDEPENDENT-SET is NP-hard

Every decision problem $L$ in NP has a polynomial-time
many-one reduction to INDEPENDENT-SET: a polynomial-time computable map $f$ on bit strings such
that, for every bit string $x$, $L$ accepts $x$ exactly when INDEPENDENT-SET accepts $f(x)$.

Formalized by `Cslib.Complexity.Karp.indSetDec_npHard`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-08/index.html#ind-set-dec-np-hard).

## VERTEX-COVER (exact size `k`) is NP-hard

Every decision problem in NP reduces by a
polynomial-time many-one reduction to the decision problem VERTEX-COVER, which accepts exactly
the valid encodings of a number $k$ and a graph $G$ such that $G$ has a vertex cover of exactly
$k$ vertices.

Formalized by `Cslib.Complexity.Karp.vertexCoverDec_npHard`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-08/index.html#vertex-cover-dec-np-hard).

## The CLIQUE, INDEPENDENT-SET and VERTEX-COVER verifier as a host component

For a mode $m$
(clique, independent set or vertex cover), this is the host component whose stacks are
$X, W, C, N, V, T$, each over the symbol alphabet of the SAT verifier, and whose labels and
program are those of the verifier machine of mode $m$.

Formalized by `Cslib.Complexity.Karp.kgVerifyComp`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-08/index.html#kg-verify-comp).

## NP membership from the CLIQUE, INDEPENDENT-SET and VERTEX-COVER verifier

Let $L$ be a
decision problem, let $m$ be a mode (clique, independent set or vertex cover), and let $V_m$ be
the verifier of mode $m$. If for every bit string $x$, $L$ accepts $x$ exactly when there is a
bit string $w$ with $|w| \le |x|$ such that $V_m$ accepts $(x, w)$, then $L$ is in NP.

Formalized by `Cslib.Complexity.Karp.mem_NP_of_kgCheck`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-08/index.html#mem-np-of-kg-check).

## CLIQUE is in NP

**CLIQUE is in NP**.

Formalized by `Cslib.Complexity.Karp.cliqueDec_mem_NP`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-08/index.html#clique-dec-mem-np).

## INDEPENDENT-SET is in NP

**INDEPENDENT-SET is in NP**.

Formalized by `Cslib.Complexity.Karp.indSetDec_mem_NP`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-08/index.html#ind-set-dec-mem-np).

## VERTEX-COVER (exact size `k`) is in NP

The decision problem VERTEX-COVER, which accepts
exactly the valid encodings of a number $k$ and a graph $G$ such that $G$ has a vertex cover of
exactly $k$ vertices, is in NP.

Formalized by `Cslib.Complexity.Karp.vertexCoverDec_mem_NP`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-08/index.html#vertex-cover-dec-mem-np).

## CLIQUE is NP-complete

CLIQUE lies in NP, and every decision problem in NP has a
polynomial-time many-one reduction to CLIQUE.

Formalized by `Cslib.Complexity.Karp.cliqueDec_npComplete`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-08/index.html#clique-dec-np-complete).

## INDEPENDENT-SET is NP-complete

INDEPENDENT-SET lies in NP, and every decision problem
in NP has a polynomial-time many-one reduction to INDEPENDENT-SET.

Formalized by `Cslib.Complexity.Karp.indSetDec_npComplete`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-08/index.html#ind-set-dec-np-complete).

## VERTEX-COVER (exact size `k`) is NP-complete

The decision problem VERTEX-COVER, which
accepts exactly the valid encodings of a number $k$ and a graph $G$ such that $G$ has a vertex
cover of exactly $k$ vertices, is in NP, and every decision problem in NP reduces to it by a
polynomial-time many-one reduction.

Formalized by `Cslib.Complexity.Karp.vertexCoverDec_npComplete`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/CliqueComplete.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/part-08/index.html#vertex-cover-dec-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Clique, independent set and vertex cover](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/clique-independent-set-and-vertex-cover)
