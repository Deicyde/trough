---
declaration: section
origin: cited
lean: Cslib.Complexity.Karp.IsHamPath, Cslib.Complexity.Karp.hamPathDec, Cslib.Complexity.Karp.hamVars, Cslib.Complexity.Karp.hpT, Cslib.Complexity.Karp.hpR, Cslib.Complexity.Karp.diamondEdges, Cslib.Complexity.Karp.hamEdges, Cslib.Complexity.Karp.toHam
statement: formalized
proof: formalized
---

# Hamiltonian path in directed graphs

214 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/index.html).

## Hamiltonian paths

Let $E$ be a list of pairs of natural numbers, viewed as the digraph
on $0, \dots, n - 1$ whose arcs are the pairs in $E$ with both ends below $n$. A list $p$ is a
Hamiltonian path from $s$ to $t$ when it lists each of the vertices $0, \dots, n - 1$ exactly
once, starts at $s$, ends at $t$, and each two consecutive entries of $p$ form an arc.

Formalized by `Cslib.Complexity.Karp.IsHamPath`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#is-ham-path).

## The HAMPATH problem

The decision problem that accepts a bit string $x$ exactly when, for
some $s$, $t$, $n$ and list of pairs $E$, $x$ is the PATH encoding of $s$, $t$ and the digraph on
$0, \dots, n - 1$ with edge list $E$, and this digraph has a Hamiltonian path from $s$ to $t$.

Formalized by `Cslib.Complexity.Karp.hamPathDec`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#ham-path-dec).

## Distinct variables of a formula

The list of the distinct variables of a CNF formula
$\varphi$, in order of occurrence in $\varphi$, with each variable kept at its last occurrence.

Formalized by `Cslib.Complexity.Karp.hamVars`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#ham-vars).

## Tops of the diamonds

In the HAMPATH construction with $m$ clauses, the top of
diamond $i$ is the vertex $m + i(3m + 2)$; it is also the bottom of diamond $i - 1$.

Formalized by `Cslib.Complexity.Karp.hpT`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#hp-t).

## Row vertices of a diamond

In the HAMPATH construction with $m$ clauses, write $T(i)$
for the top of diamond $i$. Row vertex $l$ of diamond $i$ is the number $T(i) + 1 + l$; the row
of diamond $i$ consists of the vertices with $l \le 3m$.

Formalized by `Cslib.Complexity.Karp.hpR`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#hp-r).

## Arcs of a variable diamond

Let $\varphi$ be a CNF formula with $m$ clauses, and write
$T(i)$ for the top of diamond $i$ and $R(i, l)$ for its row vertex $l$. The arcs of diamond $i$
for variable $x$ are $T(i) \to R(i, 0)$, $T(i) \to R(i, 3m)$, $R(i, 0) \to T(i + 1)$ and
$R(i, 3m) \to T(i + 1)$; for every $l < 3m$, both $R(i, l) \to R(i, l + 1)$ and
$R(i, l + 1) \to R(i, l)$; and for every clause $j < m$, the arcs $R(i, 3j + 1) \to j$ and
$j \to R(i, 3j + 2)$ if $x$ occurs positively in clause $j$, and the arcs $R(i, 3j + 2) \to j$
and $j \to R(i, 3j + 1)$ if $x$ occurs negatively in clause $j$. Here $j$ is the vertex of
clause $j$.

Formalized by `Cslib.Complexity.Karp.diamondEdges`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#diamond-edges).

## Arcs of the HAMPATH construction

Let $\varphi$ be a CNF formula and let
$x_0, \dots, x_{k-1}$ be its distinct variables, in the order of the distinct-variable list of
$\varphi$. The arcs of the construction for $\varphi$ are the arcs of diamond $i$ for variable
$x_i$, for $i = 0, \dots, k - 1$, concatenated in this order.

Formalized by `Cslib.Complexity.Karp.hamEdges`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#ham-edges).

## Sipser's HAMPATH instance of a CNF formula

Let $\varphi$ be a CNF formula with $m$
clauses, numbered $0, \dots, m - 1$, and let $x_0, \dots, x_{k-1}$ be its distinct variables,
in the order of their last occurrences in $\varphi$ (clauses read in order, and the literals of
each clause in order). Put $T_i = m + i(3m + 2)$ and $R_{i,l} = T_i + 1 + l$. The result is the
encoded PATH instance with vertices $0, \dots, T_k$, source $T_0$, target $T_k$, and, for each
$i < k$, the following arcs: the frame arcs $T_i \to R_{i,0}$, $T_i \to R_{i,3m}$,
$R_{i,0} \to T_{i+1}$ and $R_{i,3m} \to T_{i+1}$; the row arcs $R_{i,l} \to R_{i,l+1}$ and
$R_{i,l+1} \to R_{i,l}$ for every $l < 3m$; and, for every clause $j < m$, the arcs
$R_{i,3j+1} \to j$ and $j \to R_{i,3j+2}$ if the literal $x_i$ occurs in clause $j$, and the
arcs $R_{i,3j+2} \to j$ and $j \to R_{i,3j+1}$ if the literal $\neg x_i$ occurs in clause $j$.

Formalized by `Cslib.Complexity.Karp.toHam`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#to-ham).

## A fixed HAMPATH no-instance

The encoded PATH instance on the two vertices $0$ and $1$,
with no arcs, whose source and target are both $0$.

It is a no-instance of HAMPATH: a Hamiltonian path would visit both vertices and start and end
at $0$, so it would visit $0$ twice.

Formalized by `Cslib.Complexity.Karp.noHam`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#no-ham).

## The SAT-to-HAMPATH reduction map

A bit string $x$ that decodes to a CNF formula
$\varphi$ is sent to Sipser's HAMPATH instance of $\varphi$, and a bit string that does not
decode to a CNF formula is sent to the fixed HAMPATH no-instance (two vertices, no arcs, source
and target $0$).

Formalized by `Cslib.Complexity.Karp.reduceHam`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#reduce-ham).

## Normal clause detours

Let $\varphi$ be a CNF formula with $m$ clauses and $k$ distinct
variables, and write $R(i, l)$ for row vertex $l$ of diamond $i$ in the HAMPATH construction for
$\varphi$. A list of vertices $p$ has normal detours when for every clause $j < m$ there is a
diamond $i < k$ such that $p$ contains $R(i, 3j + 1), j, R(i, 3j + 2)$ or
$R(i, 3j + 2), j, R(i, 3j + 1)$ as consecutive entries.

Formalized by `Cslib.Complexity.Karp.DetoursNormal`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#detours-normal).

## Tops are monotone in the diamond index

In the HAMPATH construction with $m$ clauses,
if $i \le i'$ then the top of diamond $i$ is at most the top of diamond $i'$.

Formalized by `Cslib.Complexity.Karp.hpT_mono`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#hp-t-mono).

## Row vertices lie below the next top

In the HAMPATH construction with $m$ clauses, for
every diamond $i$ and every $l \le 3m$, row vertex $l$ of diamond $i$ is a smaller number than
the top of diamond $i + 1$.

Formalized by `Cslib.Complexity.Karp.hpR_lt_hpT_succ`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPath.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPath.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#hp-r-lt-hp-t-succ).

## Bits of an edge list, first edge first

For natural numbers $u, v$ and a list $E$ of pairs
of natural numbers, the bit encoding of the edge list whose first edge is $(u, v)$ and whose
remaining edges are $E$ is: $u$ copies of true, then false, then $v$ copies of true, then false,
then the bit encoding of $E$.

Formalized by `Cslib.Complexity.Karp.HamVerify.edgeBits_cons`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#edge-bits-cons).

## Edge bits of the empty edge list

The edge-list bit encoding of the empty list of edges
is the empty bit string.

Formalized by `Cslib.Complexity.Karp.HamVerify.edgeBits_nil`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#edge-bits-nil).

## Bits of concatenated edge lists

For all lists $E$ and $E'$ of pairs of natural numbers,
the bit encoding of the concatenation of $E$ and $E'$ is the bit encoding of $E$ followed by the
bit encoding of $E'$.

Formalized by `Cslib.Complexity.Karp.HamVerify.edgeBits_append`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#edge-bits-append).

## Witness encoding

The witness encoding of a list $p$ of natural numbers (the vertices of a
candidate path) is the bit string obtained by writing each entry $v$ of $p$, in order, as $v$
copies of true followed by one false, and concatenating the results.

Formalized by `Cslib.Complexity.Karp.HamVerify.encW`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#enc-w).

## Witness decoder

The witness decoder reads a list $w$ of bits as a list of natural numbers.
On the empty list it returns the empty list. Otherwise it reads a unary number $v$ from the front
of $w$, a run of $v$ copies of true ended by false, and if decoding the remaining bits gives a
list $p$, it returns $v$ followed by $p$. It fails if no unary number can be read from a
nonempty list, or if decoding the remaining bits fails.

Formalized by `Cslib.Complexity.Karp.HamVerify.decodeW`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#decode-w).

## Witness encoding of the empty list

The witness encoding of the empty list of vertices is
the empty bit string.

Formalized by `Cslib.Complexity.Karp.HamVerify.encW_nil`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#enc-w-nil).

## Witness encoding of a nonempty list

For a natural number $v$ and a list $p$ of natural
numbers, the witness encoding of the list with first entry $v$ followed by $p$ is the bit string
made of $v$ copies of true, then one false, then the witness encoding of $p$.

Formalized by `Cslib.Complexity.Karp.HamVerify.encW_cons`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-01/index.html#enc-w-cons).

## The witness encoding respects concatenation

For lists $p$ and $p'$ of natural numbers,
the witness encoding of the concatenation of $p$ and $p'$ is the witness encoding of $p$ followed
by the witness encoding of $p'$.

Formalized by `Cslib.Complexity.Karp.HamVerify.encW_append`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#enc-w-append).

## Decoding the empty witness

The witness decoder succeeds on the empty list of bits and
returns the empty list of vertices.

Formalized by `Cslib.Complexity.Karp.HamVerify.decodeW_nil`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#decode-w-nil).

## Witness decoding fails on a cut-off first number

If a list $w$ of bits is nonempty and
reading a unary number (a run of true ended by false) from the front of $w$ fails, that is, every
bit of $w$ is true, then the witness decoder fails on $w$.

Formalized by `Cslib.Complexity.Karp.HamVerify.decodeW_of_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#decode-w-of-none).

## Decoding peels off the first number

If reading a unary number from the front of a list
$w$ of bits returns $v$ with remaining bits $r$, that is, $w$ is $v$ copies of true, then false,
then $r$, then the witness decoder succeeds on $w$ exactly when it succeeds on $r$, and its
result on $w$ is $v$ followed by its result on $r$.

Formalized by `Cslib.Complexity.Karp.HamVerify.decodeW_of_some`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#decode-w-of-some).

## Decoding inverts the witness encoding

For every list $p$ of natural numbers, the witness
decoder applied to the witness encoding of $p$ (each entry $v$ written as $v$ copies of true
followed by false) succeeds and returns $p$.

Formalized by `Cslib.Complexity.Karp.HamVerify.decodeW_encW`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#decode-w-enc-w).

## The witness decoder succeeds only on encodings

For every bit string $w$ and every list
$p$ of natural numbers, if the witness decoder returns $p$ on $w$, then $w$ is the witness
encoding of $p$.

Formalized by `Cslib.Complexity.Karp.HamVerify.encW_of_decodeW`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#enc-w-of-decode-w).

## The witness codec

For every list $w$ of bits and every list $p$ of natural numbers, the
witness decoder returns $p$ on $w$ if and only if $w$ is the witness encoding of $p$, which
writes each entry $v$ of $p$ as $v$ copies of true followed by false.

Formalized by `Cslib.Complexity.Karp.HamVerify.decodeW_eq_some`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#decode-w-eq-some).

## Witness length

For every list $p = (v_1, \dots, v_k)$ of natural numbers, the witness
encoding of $p$ has length $\sum_{i=1}^{k} (v_i + 1)$.

Formalized by `Cslib.Complexity.Karp.HamVerify.length_encW`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#length-enc-w).

## Witness length bound

For every natural number $n$ and every list $p$ of natural numbers
all below $n$, the witness encoding of $p$ has length at most $|p| \cdot n$.

Formalized by `Cslib.Complexity.Karp.HamVerify.length_encW_le`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#length-enc-w-le).

## A witness is at least as long as its vertex list

For every list $p$ of natural numbers,
the witness encoding of $p$ has length at least $|p|$.

Formalized by `Cslib.Complexity.Karp.HamVerify.length_le_length_encW`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#length-le-length-enc-w).

## Arc check of a vertex list

Given $n \in \mathbb{N}$ and a list $E$ of pairs of natural
numbers, the arc check of a list $p$ of natural numbers returns true when every two consecutive
entries $u, v$ of $p$ satisfy $(u, v) \in E$, $u < n$ and $v < n$, and false otherwise; in
particular every list with fewer than two entries passes.

Formalized by `Cslib.Complexity.Karp.HamVerify.chainOk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#chain-ok).

## Checking a vertex list against the arcs

For every $n \in \mathbb{N}$, every list $E$ of
pairs of natural numbers and every list $p$ of natural numbers, the arc check of $p$ against
$n$ and $E$ returns true if and only if every two consecutive entries $u, v$ of $p$ form an arc
of the digraph on $0, \dots, n - 1$ listed by $E$, that is, $(u, v) \in E$, $u < n$ and $v < n$.

Formalized by `Cslib.Complexity.Karp.HamVerify.chainOk_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#chain-ok-iff).

## The Hamiltonian path check

Given a natural number $n$, an edge list $E$, vertices $s$ and
$t$ and a list $p$ of natural numbers, the Boolean test that $p$ has no repeated entries, has
length $n$, has all entries below $n$, has first entry $s$ and last entry $t$, and that every two
consecutive entries $u, v$ of $p$ satisfy $(u, v) \in E$, $u < n$ and $v < n$.

Formalized by `Cslib.Complexity.Karp.HamVerify.hamOk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#ham-ok).

## The Hamiltonian path check is correct

For all natural numbers $n$, $s$, $t$, every edge
list $E$ and every list $p$ of natural numbers, the Hamiltonian path check on $(n, E, s, t, p)$
returns true if and only if $p$ is a Hamiltonian path from $s$ to $t$ in the digraph on
$\{0, \dots, n-1\}$ with edge list $E$.

Formalized by `Cslib.Complexity.Karp.HamVerify.hamOk_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#ham-ok-iff).

## The HAMPATH verifier

Given bit strings $x$ and $w$, the verifier decodes $x$ as a PATH
instance, consisting of a start vertex $s$, a target vertex $t$, a vertex count $n$ and an edge
list $E$, and decodes $w$ as a witness, a list $p$ of natural numbers each written in unary. If
both decodings succeed, it accepts exactly when the Hamiltonian path check passes, that is, when
$p$ is a Hamiltonian path from $s$ to $t$ in the digraph on $\{0, \dots, n-1\}$ with edge list
$E$. If either decoding fails, it rejects.

Formalized by `Cslib.Complexity.Karp.HamVerify.hamCheck`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#ham-check).

## What the HAMPATH verifier accepts

For bit strings $x$ and $w$, the HAMPATH verifier
accepts $(x, w)$ if and only if there are natural numbers $s$, $t$, $n$, a list $es$ of pairs of
natural numbers and a list $p$ of natural numbers such that $x$ is the PATH encoding of
$(s, t, n, es)$, $w$ is the witness encoding of $p$, and $p$ is a Hamiltonian path from $s$ to $t$
in the digraph on $0, \dots, n - 1$ with edge list $es$.

Formalized by `Cslib.Complexity.Karp.HamVerify.hamCheck_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#ham-check-iff).

## The verifier on an encoded instance and witness

For natural numbers $s$, $t$, $n$, a list
$es$ of pairs of natural numbers and a list $p$ of natural numbers, the HAMPATH verifier applied to
the PATH encoding of $(s, t, n, es)$ and the witness encoding of $p$ returns the same boolean as
the Hamiltonian path check on $n$, $es$, $s$, $t$ and $p$.

Formalized by `Cslib.Complexity.Karp.HamVerify.hamCheck_encode`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#ham-check-encode).

## Instances that do not decode are rejected

If the PATH instance decoder fails on a bit
string $x$, then for every bit string $w$ the HAMPATH verifier rejects $(x, w)$, that is, returns
false.

Formalized by `Cslib.Complexity.Karp.HamVerify.hamCheck_of_decodeP`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#ham-check-of-decode-p).

## Witnesses that do not decode are rejected

If the witness decoder fails on a bit string
$w$, then for every bit string $x$ the HAMPATH verifier rejects $(x, w)$, that is, returns false.

Formalized by `Cslib.Complexity.Karp.HamVerify.hamCheck_of_decodeW`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#ham-check-of-decode-w).

## Length of an encoded PATH instance

For all natural numbers $s$, $t$, $n$ and every edge
list $E$, the encoding of the PATH instance $(s, t, n, E)$ has length $s + t + n + 3 + \ell$,
where $\ell$ is the length of the bit encoding of the edge list $E$.

Formalized by `Cslib.Complexity.Karp.HamVerify.length_encodeP`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-02/index.html#length-encode-p).

## HAMPATH is verified with quadratic-size witnesses

For every bit string $x$, $x$ is a
yes-instance of HAMPATH if and only if there is a bit string $w$ of length at most
$(|x| + 1)^2$ such that the HAMPATH verifier accepts $(x, w)$.

Formalized by `Cslib.Complexity.Karp.HamVerify.hamPathDec_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#ham-path-dec-iff).

## One step of the HAMPATH walk

Given natural numbers $s$ and $n$, an edge list $E$, a count
$c$ of vertices already seen, the previous vertex $b$, the current vertex $a$ and the list $q$ of
remaining vertices, the step check is true exactly when $a < n$, $a$ does not occur in $q$, and
either $c = 0$ and $a = s$, or $c \neq 0$ and $(b, a) \in E$.

Formalized by `Cslib.Complexity.Karp.HamVerify.stepOk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#step-ok).

## The walk check of the HAMPATH verifier

Fix natural numbers $s, t, n$ and a list $E$ of
pairs of natural numbers. The walk check accepts a list $q$ of natural numbers after $c$ vertices,
the last of which was $b$, by recursion on $q$. On the empty list it accepts if and only if
$c = n$, $c \neq 0$ and $b = t$. On a list with first entry $a$ and remaining entries $q'$ it
accepts if and only if the step check passes and the walk check accepts $q'$ after $c + 1$
vertices, the last of which was $a$. The step check requires $a < n$; it requires $a = s$ when
$c = 0$, and that $(b, a)$ is an entry of $E$ when $c \neq 0$; and it requires that $a$ does not
occur in $q'$.

Formalized by `Cslib.Complexity.Karp.HamVerify.walkOk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#walk-ok).

## The walk check after the first vertex

Let $s, t, n$ be natural numbers and $E$ a list of
pairs of natural numbers. For every list $q = (q_1, \dots, q_k)$ of natural numbers and all
natural numbers $c \neq 0$ and $b$, the walk check for $s, t, n, E$ accepts $q$ after $c$ vertices
the last of which was $b$ if and only if every $q_i$ is less than $n$, every pair $(u, v)$ of
consecutive entries of the list $(b, q_1, \dots, q_k)$ is an entry of $E$, the entries of $q$ are
pairwise distinct, $c + k = n$, and the last entry of $(b, q_1, \dots, q_k)$ is $t$.

Formalized by `Cslib.Complexity.Karp.HamVerify.walkOk_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#walk-ok-iff).

## The machine's walk is the check

For all natural numbers $s$, $t$, $n$, every edge list
$E$ and every list $p$ of natural numbers, the walk over $p$ started with count $0$ and previous
vertex $0$ returns the same Boolean value as the Hamiltonian path check on $(n, E, s, t, p)$.

Formalized by `Cslib.Complexity.Karp.HamVerify.walkOk_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCheck.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#walk-ok-eq).

## Tops of distinct diamonds are at least $3m + 2$ apart

In the vertex numbering of the
Hamiltonian path construction with $m$ clauses, where the top of diamond $i$ is the vertex
$T(i) = m + i(3m + 2)$, any two indices $i \ne i'$ satisfy $T(i) + 3m + 2 \le T(i')$ or
$T(i') + 3m + 2 \le T(i)$.

Formalized by `Cslib.Complexity.Karp.hpT_sep`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#hp-t-sep).

## Arcs of the Hamiltonian path construction

Let $\varphi$ be a CNF formula with clauses
$C_0, \dots, C_{m-1}$ and distinct variables $x_0, \dots, x_{k-1}$ (in the order the
construction lists them), and write $T(i) = m + i(3m + 2)$ for the top of diamond $i$ and
$R(i, l) = T(i) + 1 + l$ for its row vertex $l$. Then $(u, v)$ is an arc of the Hamiltonian path
instance of $\varphi$ if and only if there is an $i < k$ such that $(u, v)$ is one of the frame
arcs $(T(i), R(i, 0))$, $(T(i), R(i, 3m))$, $(R(i, 0), T(i + 1))$ and $(R(i, 3m), T(i + 1))$;
or $(u, v)$ is a row arc $(R(i, l), R(i, l + 1))$ or $(R(i, l + 1), R(i, l))$ for some
$l < 3m$; or, for some $j < m$, either $C_j$ contains the literal $x_i$ and $(u, v)$ is
$(R(i, 3j + 1), j)$ or $(j, R(i, 3j + 2))$, or $C_j$ contains the literal $\lnot x_i$ and
$(u, v)$ is $(R(i, 3j + 2), j)$ or $(j, R(i, 3j + 1))$.

Formalized by `Cslib.Complexity.Karp.mem_hamEdges`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#mem-ham-edges).

## Classification of the arcs of Sipser's graph

Let $\varphi$ be a CNF formula with $m$
clauses and $k$ distinct variables, and write $T_i = m + i(3m + 2)$ and $R_{i,l} = T_i + 1 + l$.
If $(u, v)$ is an arc of Sipser's construction for $\varphi$, then there is $i < k$ such that one
of the following holds: $u = T_i$ and $v \in \{R_{i,0}, R_{i,3m}\}$; or
$u \in \{R_{i,0}, R_{i,3m}\}$ and $v = T_{i+1}$; or there is $l < 3m$ with
$(u, v) = (R_{i,l}, R_{i,l+1})$ or $(u, v) = (R_{i,l+1}, R_{i,l})$; or there is $j < m$ with
$u \in \{R_{i,3j+1}, R_{i,3j+2}\}$ and $v = j$, or with $u = j$ and
$v \in \{R_{i,3j+1}, R_{i,3j+2}\}$.

The last case does not record whether the detour comes from a positive or a negative literal.

Formalized by `Cslib.Complexity.Karp.hamEdges_cases`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#ham-edges-cases).

## In-neighbours of a row vertex in Sipser's graph

Let $\varphi$ be a CNF formula with $m$
clauses, and write $T_i = m + i(3m + 2)$ and $R_{i,l} = T_i + 1 + l$. Let $i$ and $l \le 3m$ be
natural numbers, and let $(v, R_{i,l})$ be an arc of Sipser's construction for $\varphi$. Then
$l < 3m$ and $v = R_{i,l+1}$; or $0 < l$ and $v = R_{i,l-1}$; or $l \in \{0, 3m\}$ and
$v = T_i$; or $v < m$ and $l \in \{3v + 1, 3v + 2\}$.

Formalized by `Cslib.Complexity.Karp.hamEdges_to_hpR`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#ham-edges-to-hp-r).

## Out-neighbours of a row vertex in Sipser's graph

Let $\varphi$ be a CNF formula with $m$
clauses, and write $T_i = m + i(3m + 2)$ and $R_{i,l} = T_i + 1 + l$. Let $i$ and $l \le 3m$ be
natural numbers, and let $(R_{i,l}, v)$ be an arc of Sipser's construction for $\varphi$. Then
$l < 3m$ and $v = R_{i,l+1}$; or $0 < l$ and $v = R_{i,l-1}$; or $l \in \{0, 3m\}$ and
$v = T_{i+1}$; or $v < m$ and $l \in \{3v + 1, 3v + 2\}$.

Formalized by `Cslib.Complexity.Karp.hamEdges_from_hpR`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#ham-edges-from-hp-r).

## In-neighbours of a clause vertex in Sipser's graph

Let $\varphi$ be a CNF formula with
$m$ clauses and $k$ distinct variables, and write $R_{i,l} = m + i(3m + 2) + 1 + l$ for row
vertex $l$ of diamond $i$. If $j < m$ and $(v, j)$ is an arc of Sipser's construction for
$\varphi$, then there is $i < k$ with $v = R_{i,3j+1}$ or $v = R_{i,3j+2}$.

Formalized by `Cslib.Complexity.Karp.hamEdges_to_clause`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#ham-edges-to-clause).

## Out-neighbours of a clause vertex in Sipser's graph

Let $\varphi$ be a CNF formula with
$m$ clauses and $k$ distinct variables, and write $R_{i,l} = m + i(3m + 2) + 1 + l$ for row
vertex $l$ of diamond $i$. If $j < m$ and $(j, v)$ is an arc of Sipser's construction for
$\varphi$, then there is $i < k$ with $v = R_{i,3j+1}$ or $v = R_{i,3j+2}$.

Formalized by `Cslib.Complexity.Karp.hamEdges_from_clause`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#ham-edges-from-clause).

## A Hamiltonian path visits every vertex

If $p$ is a Hamiltonian path from $s$ to $t$ in
the digraph on the vertices $0, \dots, n - 1$ with arc list $E$, then every vertex $v < n$
occurs in $p$.

Formalized by `Cslib.Complexity.Karp.mem_of_isHamPath`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#mem-of-is-ham-path).

## Consecutive vertices of a Hamiltonian path of Sipser's graph form arcs

Let $\varphi$ be a
CNF formula with $m$ clauses and $k$ distinct variables, let $T_i = m + i(3m + 2)$, and let $p$
be a Hamiltonian path from $T_0$ to $T_k$ in the digraph on the vertices $0, \dots, T_k$ whose
arcs are those of Sipser's construction for $\varphi$. If $v$ comes immediately after $u$ in $p$,
then $(u, v)$ is an arc of the construction.

Formalized by `Cslib.Complexity.Karp.hamEdges_of_infix`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#ham-edges-of-infix).

## A Hamiltonian path of Sipser's graph does not cross a diamond through one row end

Let
$\varphi$ be a CNF formula with $m \ge 1$ clauses and $k$ distinct variables, write
$T_i = m + i(3m + 2)$ and $R_{i,l} = T_i + 1 + l$, and let $p$ be a Hamiltonian path from $T_0$
to $T_k$ in the digraph on the vertices $0, \dots, T_k$ whose arcs are those of Sipser's
construction for $\varphi$. For $i < k$ and $l \in \{0, 3m\}$, it is impossible that $R_{i,l}$
comes immediately after $T_i$ in $p$ and $T_{i+1}$ comes immediately after $R_{i,l}$ in $p$.

Formalized by `Cslib.Complexity.Karp.hamPath_rowEnd_false`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#ham-path-row-end-false).

## A separator is next to each of its row neighbours on a Hamiltonian path

Let $\varphi$ be
a CNF formula with $m$ clauses and $k$ distinct variables, write $T_i = m + i(3m + 2)$ and
$R_{i,l} = T_i + 1 + l$, and let $p$ be a Hamiltonian path from $T_0$ to $T_k$ in the digraph on
the vertices $0, \dots, T_k$ whose arcs are those of Sipser's construction for $\varphi$. Let
$i < k$, let $l \le 3m$ be a multiple of $3$, and let $l' \le 3m$ satisfy $l' = l + 1$ or
$l' + 1 = l$. Then $R_{i,l'}$ comes immediately before or immediately after $R_{i,l}$ in $p$.

Formalized by `Cslib.Complexity.Karp.hamPath_separator_false`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#ham-path-separator-false).

## A clause detour returns to its own pair (Sipser's separator argument)

Let $\varphi$ be a
CNF formula with $m$ clauses and $k$ distinct variables, write $T_i = m + i(3m + 2)$ and
$R_{i,l} = T_i + 1 + l$, and let $p$ be a Hamiltonian path from $T_0$ to $T_k$ in the digraph on
the vertices $0, \dots, T_k$ whose arcs are those of Sipser's construction for $\varphi$. Let
$i < k$ and $j < m$, and let $(l_a, l_c)$ be $(3j + 1, 3j + 2)$ or $(3j + 2, 3j + 1)$. If the
clause vertex $j$ comes immediately after $R_{i,l_a}$ in $p$, then every vertex that comes
immediately after $j$ in $p$ is $R_{i,l_c}$.

Formalized by `Cslib.Complexity.Karp.hamPath_pair_false`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#ham-path-pair-false).

## Hamiltonian paths of Sipser's graph have normal detours

Let $\varphi$ be a CNF formula
with $m$ clauses and $k$ distinct variables, and write $T_i = m + i(3m + 2)$ and
$R_{i,l} = T_i + 1 + l$ for the top and the row vertices of diamond $i$. Every Hamiltonian path
from $T_0$ to $T_k$ in the digraph on the vertices $0, \dots, T_k$ whose arcs are those of
Sipser's construction for $\varphi$ has normal detours: for every clause $j < m$ there is $i < k$
such that $R_{i,3j+1}, j, R_{i,3j+2}$ or $R_{i,3j+2}, j, R_{i,3j+1}$ occur in this order as
consecutive vertices of the path.

Formalized by `Cslib.Complexity.Karp.detoursNormal_of_isHamPath`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathDetours.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#detours-normal-of-is-ham-path).

## The HAMPATH instance as unary blocks and arc bits

Let $\varphi$ be a CNF formula with $m$
clauses and $k$ distinct variables, and let $t = m + k(3m + 2)$ be the top of diamond $k$. Then
the HAMPATH instance of $\varphi$ is the bit string made of $m$ ones and a zero (the start
vertex $s = m$), then $t$ ones and a zero (the target vertex $t$), then $t + 1$ ones and a zero
(the vertex count $n = t + 1$), followed by the arcs of the construction, each arc $(u, v)$
written as $u$ ones, a zero, $v$ ones and a zero.

Formalized by `Cslib.Complexity.Karp.EmitHam.toHam_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#to-ham-eq).

## The frame of a diamond

For natural numbers $m$ (the number of clauses) and $i$, write
$t_i = m + i(3m + 2)$ for the top of diamond $i$ and $r_{i,l} = t_i + 1 + l$ for its row
vertex $l$. The frame of diamond $i$ is the list of the four arcs $(t_i, r_{i,0})$,
$(t_i, r_{i,3m})$, $(r_{i,0}, t_{i+1})$ and $(r_{i,3m}, t_{i+1})$: the top points to both row
ends, and both row ends point to the top of the next diamond.

Formalized by `Cslib.Complexity.Karp.EmitHam.frameE`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-03/index.html#frame-e).

## The row arcs of a diamond

For natural numbers $m$ (the number of clauses), $i$ and $l$,
let $r_{i,l} = m + i(3m + 2) + 1 + l$ be row vertex $l$ of diamond $i$. The row arcs between row
vertices $l$ and $l + 1$ of diamond $i$ are the list of the two arcs $(r_{i,l}, r_{i,l+1})$ and
$(r_{i,l+1}, r_{i,l})$.

Formalized by `Cslib.Complexity.Karp.EmitHam.rowE`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#row-e).

## Clause detours in a diamond

For natural numbers $m$ (the number of clauses), $i$, $x$
and $j$, let $r_{i,l} = m + i(3m + 2) + 1 + l$ be row vertex $l$ of diamond $i$. For a clause
$C$, a list of literals, the detours of clause $j$ with contents $C$ in diamond $i$ of variable
$x$ are the list of the arcs $(r_{i,3j+1}, j)$ and $(j, r_{i,3j+2})$ if the positive literal
$x$ is in $C$, followed by the arcs $(r_{i,3j+2}, j)$ and $(j, r_{i,3j+1})$ if the negative
literal $\lnot x$ is in $C$.

Formalized by `Cslib.Complexity.Karp.EmitHam.detE`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#det-e).

## The next diamond top follows the row

For natural numbers $m$ (the number of clauses) and
$i$, write $t_i = m + i(3m + 2)$ for the top of diamond $i$ and $r_{i,l} = t_i + 1 + l$ for its
row vertex $l$. Then $t_{i+1} = r_{i,3m} + 1$: the top of diamond $i + 1$ comes right after the
last row vertex of diamond $i$.

Formalized by `Cslib.Complexity.Karp.EmitHam.hpT_succ_eq_hpR`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#hp-t-succ-eq-hp-r).

## Splitting off the middle clause of a concatenation

Let $P$ and $Q$ be CNF formulas, $C$ a
clause, and $\varphi$ the formula whose clauses are those of $P$, then $C$, then those of $Q$.
Write $|P|$ for the number of clauses of $P$ and $\varphi_j$ for clause $j$ of $\varphi$, counting
from $0$ (the empty clause if $j$ is out of range). Let $f$ map each natural number $j$ and clause
to a list of elements of a type $\alpha$. Then concatenating the lists $f(j, \varphi_j)$ over
$j < |P| + 1$ in increasing order gives the concatenation of the lists $f(j, \varphi_j)$ over
$j < |P|$, followed by $f(|P|, C)$.

Formalized by `Cslib.Complexity.Karp.EmitHam.range_flatMap_getD`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#range-flat-map-get-d).

## Insert a variable if new

For a natural number $x$ and a list $V$ of natural numbers,
inserting $x$ into $V$ gives $V$ itself if $x$ occurs in $V$, and otherwise the list obtained
by prepending $x$ to $V$.

Formalized by `Cslib.Complexity.Karp.EmitHam.insV`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#ins-v).

## Removing duplicates by insertion

For every list $l$ of natural numbers, folding $l$ from
the right into the empty list, prepending each element unless it is already present, gives
$l$ with duplicates removed: each element is kept at its last occurrence in $l$, in order.

Formalized by `Cslib.Complexity.Karp.EmitHam.foldr_insV`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#foldr-ins-v).

## Consecutive row vertices

In the HAMPATH construction with $m$ clauses, for every diamond
$i$ and every $l \in \mathbb{N}$, row vertex $l + 1$ of diamond $i$ is one more than row
vertex $l$ of diamond $i$.

Formalized by `Cslib.Complexity.Karp.EmitHam.hpR_succ`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#hp-r-succ).

## Length bound for the bit encoding of an edge list

Let $B$ be a natural number and $E$ a
list of pairs of natural numbers such that every pair $(u, v)$ in $E$ has $u \le B$ and
$v \le B$. Then the bit encoding of $E$, which writes each pair $(u, v)$ as $u$ ones, a zero,
$v$ ones and a zero, has length at most $|E| \cdot (2B + 2)$, where $|E|$ is the length of $E$.

Formalized by `Cslib.Complexity.Karp.EmitHam.edgeBits_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitSpec.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#edge-bits-length-le).

## Stacks of the HAMPATH emitter

The emitter has eighteen distinct stacks: $T$ (the tokens),
$O$ (the output), $F$ (the tokens in reading order), $V$ (the distinct variables), $W$ (the other
side of the walk over $V$), $Q$ (the edges in progress), $G$ (garbage), $X$ and $Y$ (comparison
scratch), $C$ (the clause count), $M$ (three times the clause count), $P$ (the diamond top), $N$
(the row end), $R$ (the row vertex), $L$ (the row loop index), $J$ (the clause index), $D$ (the
detour vertex) and $Z$ (copy scratch).

Formalized by `Cslib.Complexity.Karp.EmitHam.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#k).

## Stack alphabets of the HAMPATH emitter

The alphabet of the output stack $O$ is the set of
bits (booleans); every other stack has the token symbols as its alphabet.

The counter stacks only ever hold the symbol $\mathrm{cl}$.

Formalized by `Cslib.Complexity.Karp.EmitHam.Γ`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#untitled).

## Counters read by HAMPATH copy sites

The type with the five elements $p, n, r, j, d$, naming
the counters of the HAMPATH emitter that a copy site can read: the diamond top $p$, the row end
$n$, the row vertex $r$, the clause index $j$ and the detour vertex $d$.

Formalized by `Cslib.Complexity.Karp.EmitHam.Src`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#src).

## Stack of a HAMPATH copy-site counter

The counters $p$, $n$, $r$, $j$, $d$ that a copy site
of the HAMPATH emitter reads are held on the emitter's stacks $P$, $N$, $R$, $J$, $D$ respectively
(the diamond top, the row end, the row vertex, the clause index and the detour vertex).

Formalized by `Cslib.Complexity.Karp.EmitHam.Src.k`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#k-2).

## Unit symbol of an emitter counter

For every counter $s$ read by copy sites, the unit
symbol of $s$ is the token symbol $\mathrm{cl}$, as a letter of the alphabet of the stack that
holds $s$.

Formalized by `Cslib.Complexity.Karp.EmitHam.Src.unit`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#unit).

## Copy sites of the HAMPATH emitter

The type of the twenty copy sites of the emitter
machine. Each site writes one endpoint of an edge of the emitted HAMPATH instance, $u$ for the
source and $v$ for the target: the sites $f_iu, f_iv$ for $i = 1, \dots, 4$ belong to the four
frame edges, $w_iu, w_iv$ for $i = 1, 2$ to the two row edges, and $d_iu, d_iv$ for
$i = 1, \dots, 4$ to the detour edges, positive for $i = 1, 2$ and negative for $i = 3, 4$.

Formalized by `Cslib.Complexity.Karp.EmitHam.Site`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#site).

## Copy sites of the HAMPATH emitter, listed

The list of the twenty copy sites of the
HAMPATH emitter, in this order: the frame sites $f_1u, f_1v, f_2u, f_2v, f_3u, f_3v, f_4u, f_4v$,
the row sites $w_1u, w_1v, w_2u, w_2v$, and the detour sites
$d_1u, d_1v, d_2u, d_2v, d_3u, d_3v, d_4u, d_4v$.

Formalized by `Cslib.Complexity.Karp.EmitHam.Site.all`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#all).

## Counter read by a copy site

The map from copy sites to counters sending
$f_1u, f_1v, f_2u, f_3u$ to the diamond top $p$; $f_2v, f_3v, f_4u, f_4v$ to the row end $n$;
$w_1u, w_1v, w_2u, w_2v$ to the row vertex $r$; $d_1u, d_2v, d_3u, d_4v$ to the detour vertex
$d$; and $d_1v, d_2u, d_3v, d_4u$ to the clause index $j$.

Formalized by `Cslib.Complexity.Karp.EmitHam.Site.src`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#src-2).

## Extra ones of a copy site

The number of extra ones a copy site adds to its counter's value
is $1$ for the sites $f_{1v}$, $f_{3u}$, $f_{3v}$, $f_{4v}$, $w_{1v}$, $w_{2u}$, $d_{2v}$ and
$d_{3u}$, and $0$ for every other site.

Formalized by `Cslib.Complexity.Karp.EmitHam.Site.ext`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#ext).

## Labels of the HAMPATH emitter

Let $f$, $p_p$, $p_n$ and $b$ range over bits and $j$ over
copy sites. A label of the emitter is one of $\mathrm{a0}$, $\mathrm{anm}$, $\mathrm{aw}(f)$,
$\mathrm{ac}(f)$, $\mathrm{ar1}(f)$, $\mathrm{ar2}(f)$, $\mathrm{amv}(f)$, $\mathrm{asep}(f)$,
$\mathrm{ab}(f)$, $\mathrm{ad2}$, $\mathrm{ad3}$, $\mathrm{b0}$, $\mathrm{b1}$,
$\mathrm{h0}, \dots, \mathrm{h5}$, $\mathrm{r0}, \dots, \mathrm{r4}$, $\mathrm{wi}$,
$\mathrm{e0}$, $\mathrm{e1}$, $\mathrm{e2}$, $\mathrm{dw}(p_p, p_n)$, $\mathrm{dk}(p_p, p_n)$,
$\mathrm{dr1}(p_p, p_n, b)$, $\mathrm{dr2}(p_p, p_n, b)$, $\mathrm{dm}(p_p, p_n, b)$,
$\mathrm{dl}(p_p, p_n, b)$, $\mathrm{dj}$, $\mathrm{t0}, \dots, \mathrm{t8}$,
$\mathrm{z0}, \dots, \mathrm{z9}$, $\mathrm{cpA}(j, b)$, $\mathrm{cpB}(j, b)$,
$\mathrm{post}(j, b)$ and $\mathrm{done}$, all distinct.

Their roles, in terms of the emitter's stacks: in phase A, $\mathrm{a0}$ reads a token,
$\mathrm{anm}$ moves a name to $F$, and $\mathrm{aw}(f)$ to $\mathrm{asep}(f)$ walk $V$, with $f$
recording whether a match was found ($\mathrm{ac}$ compares, $\mathrm{ar1}$ and $\mathrm{ar2}$
restore, $\mathrm{amv}$ and $\mathrm{asep}$ move the entry to $W$); $\mathrm{ab}(f)$ moves $W$ back
(and, when no match was found, pushes a separator), and $\mathrm{ad2}$, $\mathrm{ad3}$ copy the
name onto $V$. For the diamonds, $\mathrm{b0}$, $\mathrm{b1}$ set $P$; $\mathrm{h0}$ takes the next
entry; $\mathrm{h1}$ to $\mathrm{h5}$ set $N$; $\mathrm{r0}$ to $\mathrm{r4}$ run the row loop, with
$\mathrm{wi}$ advancing $R$; $\mathrm{e0}$ to $\mathrm{e2}$ set $D$; $\mathrm{dw}(p_p, p_n)$ walks
$F$ with the clause flags, $\mathrm{dk}$, $\mathrm{dr1}$, $\mathrm{dr2}$, $\mathrm{dm}$,
$\mathrm{dl}$ handle a literal with match bit $b$, and $\mathrm{dj}$ ends a clause; $\mathrm{t0}$
moves $T$ back to $F$, and $\mathrm{t1}$ to $\mathrm{t8}$ drop the entry and advance $P$. The labels
$\mathrm{z0}$ to $\mathrm{z9}$ produce the output, and $\mathrm{cpA}(j, b)$, $\mathrm{cpB}(j, b)$,
$\mathrm{post}(j, b)$ copy site $j$, passing $b$ on.

Formalized by `Cslib.Complexity.Karp.EmitHam.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#lab).

## The four pairs of Booleans

The list of all pairs of Booleans in the order
$(\mathrm{true}, \mathrm{true})$, $(\mathrm{true}, \mathrm{false})$,
$(\mathrm{false}, \mathrm{true})$, $(\mathrm{false}, \mathrm{false})$.

Formalized by `Cslib.Complexity.Karp.EmitHam.bb`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#bb).

## Label after a HAMPATH copy site

For a copy site $j$ and a bit $b$, the label that follows
$j$ is $\mathrm{cpA}(j', b)$, where $j'$ is the site after $j$ in one of the chains
$f_{1u}, f_{1v}, f_{2u}, f_{2v}, f_{3u}, f_{3v}, f_{4u}, f_{4v}$, or
$w_{1u}, w_{1v}, w_{2u}, w_{2v}$, or $d_{1u}, d_{1v}, d_{2u}, d_{2v}$, or
$d_{3u}, d_{3v}, d_{4u}, d_{4v}$. At the ends of the chains it is $\mathrm{r0}$ after $f_{4v}$,
$\mathrm{wi}$ after $w_{2v}$ and $\mathrm{dj}$ after $d_{4v}$, whatever $b$ is; after $d_{2v}$ it
is $\mathrm{cpA}(d_{3u}, \mathrm{false})$ if $b$ is true and $\mathrm{dj}$ if $b$ is false.

Formalized by `Cslib.Complexity.Karp.EmitHam.Site.nxt`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-04/index.html#nxt).

## End of a clause in the detour walk

For booleans $p_p$ and $p_n$ (the flags recording
whether the current clause contains the current variable positively, respectively negatively),
the detour walk continues at the end of the clause at the label where the first positive detour
site $d_{1u}$ starts with passed bit $p_n$ if $p_p$ is true; otherwise, if $p_n$ is true, at the
label where the first negative detour site $d_{3u}$ starts with passed bit false; and otherwise at
the label that ends the clause.

Formalized by `Cslib.Complexity.Karp.EmitHam.clEnd`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#cl-end).

## The HAMPATH emitter machine

The emitter is the multi-stack machine with the emitter's
stacks (the output stack $O$ holds bits, every other stack holds token symbols), the emitter's
labels, and a boolean internal state. Below, *moving the bit block* of a stack $A$ onto a stack
$B$ means popping $A$ while its top is a name bit $\mathrm{bit}(b)$ and pushing each popped bit
onto $B$ (as $\mathrm{bit}(b)$, or as the bit $b$ when $B = O$). *Comparing* $F$ with $V$ means
popping both while their tops are equal name bits, pushing each such bit onto $X$ and onto $Y$,
and ending with "equal" if both bit blocks end together and with "different", without popping,
at the first mismatch. *Draining* $A$, pushing on given stacks, means popping $A$ until it is
empty and pushing on each of those stacks one symbol per popped symbol. Every pushed symbol not
otherwise named is the separator $\mathrm{cl}$. A list of steps written for several labels in
turn is done one label at a time, each label passing to the next.

Phase A. At $\mathrm{a0}$: if $T$ is empty, go to $\mathrm{b0}$; if its top is $\mathrm{cl}$, pop
it, push $\mathrm{cl}$ once on $F$, once on $C$ and three times on $M$, and go to $\mathrm{a0}$;
otherwise pop it, push on $F$ the polarity marker $\mathrm{lit}(s)$, where $s$ is true exactly
when the popped symbol is $\mathrm{lit}(\mathrm{true})$, and go to $\mathrm{anm}$. At
$\mathrm{anm}$: move the bit block of $T$ onto $F$, then go to $\mathrm{aw}(\mathrm{false})$. At
$\mathrm{aw}(f)$: go to $\mathrm{ab}(f)$ if $V$ is empty and to $\mathrm{ac}(f)$ otherwise. At
$\mathrm{ac}(f)$: compare $F$ with $V$, then go to $\mathrm{ar1}(\mathrm{true})$ if equal and to
$\mathrm{ar1}(f)$ if different. At $\mathrm{ar1}(f)$, $\mathrm{ar2}(f)$, $\mathrm{amv}(f)$ in
turn: move the bit block of $X$ onto $F$, of $Y$ onto $V$, and of $V$ onto $W$, then go to
$\mathrm{asep}(f)$. At $\mathrm{asep}(f)$: pop $V$, push $\mathrm{cl}$ on $W$ and go to
$\mathrm{aw}(f)$. At $\mathrm{ab}(f)$: if $W$ is empty, go to $\mathrm{a0}$ if $f$ is true, and
otherwise push $\mathrm{cl}$ on $V$ and go to $\mathrm{ad2}$; if the top of $W$ is $\mathrm{cl}$,
pop it and push $\mathrm{cl}$ on $V$; otherwise pop it and push $\mathrm{bit}(s)$ on $V$, where
$s$ is true exactly when the popped symbol is $\mathrm{bit}(\mathrm{true})$; in these last two
cases go to $\mathrm{ab}(f)$. At $\mathrm{ad2}$: move the bit block of $F$ onto $X$ and go to
$\mathrm{ad3}$. At $\mathrm{ad3}$: if the top of $X$ is a name bit, pop it, push it on $F$ and on
$V$ and go to $\mathrm{ad3}$; otherwise go to $\mathrm{a0}$.

Diamonds. At $\mathrm{b0}$, $\mathrm{b1}$ in turn: drain $C$ pushing on $P$ and $Z$, then drain
$Z$ pushing on $C$, then go to $\mathrm{h0}$. At $\mathrm{h0}$: go to $\mathrm{z0}$ if $V$ is empty
and to $\mathrm{h1}$ otherwise. At $\mathrm{h1}, \dots, \mathrm{h5}$ in turn: drain $P$ pushing on
$N$ and $Z$, drain $Z$ pushing on $P$, drain $M$ pushing on $N$ and $Z$, drain $Z$ pushing on
$M$, and push $\mathrm{cl}$ on $N$, then go to $\mathrm{cpA}(f_{1u}, \mathrm{false})$. At
$\mathrm{r0}$, $\mathrm{r1}$, $\mathrm{r2}$ in turn: drain $P$ pushing on $R$ and $Z$, drain $Z$
pushing on $P$, and push $\mathrm{cl}$ on $R$, then go to $\mathrm{r3}$. At $\mathrm{r3}$: if $M$
is empty go to $\mathrm{r4}$, and otherwise pop it, push $\mathrm{cl}$ on $L$ and go to
$\mathrm{cpA}(w_{1u}, \mathrm{false})$. At $\mathrm{r4}$: drain $L$ pushing on $M$ and go to
$\mathrm{e0}$. At $\mathrm{wi}$: push $\mathrm{cl}$ on $R$ and go to $\mathrm{r3}$. At
$\mathrm{e0}$, $\mathrm{e1}$, $\mathrm{e2}$ in turn: drain $P$ pushing on $D$ and $Z$, drain $Z$
pushing on $P$, and push $\mathrm{cl}$ twice on $D$, then go to
$\mathrm{dw}(\mathrm{false}, \mathrm{false})$.

Detours. At $\mathrm{dw}(p_p, p_n)$: if $F$ is empty go to $\mathrm{t0}$; if its top is
$\mathrm{cl}$, go to $\mathrm{cpA}(d_{1u}, p_n)$ if $p_p$ is true, else to
$\mathrm{cpA}(d_{3u}, \mathrm{false})$ if $p_n$ is true, else to $\mathrm{dj}$; otherwise go to
$\mathrm{dk}(p_p, p_n)$. At $\mathrm{dk}(p_p, p_n)$: compare $F$ with $V$, then go to
$\mathrm{dr1}(p_p, p_n, \mathrm{true})$ if equal and to $\mathrm{dr1}(p_p, p_n, \mathrm{false})$
if different. At $\mathrm{dr1}$, $\mathrm{dr2}$, $\mathrm{dm}$ with parameters $(p_p, p_n, b)$ in
turn: move the bit block of $X$ onto $F$, of $Y$ onto $V$, and of $F$ onto $T$, then go to
$\mathrm{dl}(p_p, p_n, b)$. At $\mathrm{dl}(p_p, p_n, b)$: pop $F$, push $\mathrm{lit}(s)$ on $T$,
where $s$ is true exactly when the popped symbol is $\mathrm{lit}(\mathrm{true})$, and go to
$\mathrm{dw}(p_p \lor (b \land s), p_n \lor (b \land \lnot s))$. At $\mathrm{dj}$: pop $F$, push
$\mathrm{cl}$ once on $T$, once on $J$ and three times on $D$, and go to
$\mathrm{dw}(\mathrm{false}, \mathrm{false})$. At $\mathrm{t0}$: if $T$ is empty go to
$\mathrm{t1}$; otherwise pop it, push on $F$ the symbol $\mathrm{cl}$ if the popped symbol is
$\mathrm{cl}$, $\mathrm{bit}(b)$ if it is $\mathrm{bit}(b)$, and otherwise $\mathrm{lit}(s)$ with
$s$ true exactly when it is $\mathrm{lit}(\mathrm{true})$, and go to $\mathrm{t0}$. At
$\mathrm{t1}, \dots, \mathrm{t8}$ in turn: move the bit block of $V$ onto $G$, pop $V$, drain $P$
pushing nothing, drain $N$ pushing on $P$, push $\mathrm{cl}$ on $P$, and drain $R$, $J$ and $D$
pushing nothing, then go to $\mathrm{h0}$.

Output. At $\mathrm{z0}$: move the bit block of $Q$ onto $O$ and go to $\mathrm{z1}$. At
$\mathrm{z1}, \dots, \mathrm{z9}$ in turn: push false and then true on $O$; drain $P$ pushing
true on $O$ and $\mathrm{cl}$ on $Z$; drain $Z$ pushing on $P$; push false on $O$; drain $P$
pushing true on $O$ and $\mathrm{cl}$ on $Z$; drain $Z$ pushing on $P$; push false on $O$; drain
$C$ pushing true on $O$ and $\mathrm{cl}$ on $Z$; and drain $Z$ pushing on $C$; then go to
$\mathrm{done}$. At $\mathrm{done}$: halt.

Copy sites. For a copy site $j$ and a bit $b$: at $\mathrm{cpA}(j, b)$, drain the stack of the
counter that $j$ reads, pushing $\mathrm{bit}(\mathrm{true})$ on $Q$ and $\mathrm{cl}$ on $Z$, and
go to $\mathrm{cpB}(j, b)$; at $\mathrm{cpB}(j, b)$, drain $Z$ pushing $\mathrm{cl}$ on the stack
of the counter that $j$ reads, and go to $\mathrm{post}(j, b)$; at $\mathrm{post}(j, b)$, in one
step push on $Q$ one $\mathrm{bit}(\mathrm{true})$ for each of the ones that $j$ adds to its
counter and then $\mathrm{bit}(\mathrm{false})$, and go to the label that follows $j$ for $b$.

Formalized by `Cslib.Complexity.Karp.EmitHam.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#prog).

## Start label of the HAMPATH emitter

The emitter machine starts at the label $a_0$, the
first phase A label, which reads the next token.

Formalized by `Cslib.Complexity.Karp.EmitHam.start`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#start).

## Quiescent states of the HAMPATH emitter

A quiescent state consists of lists of token
symbols $t$, $f$, $v$, $w$, $g$, $x$ (meant as the token stack, the tokens in reading order, the
distinct variables, the other side of the variable walk, garbage, and the first comparison
scratch stack), a list of bits $o$ (the output stack), a list of bits $q$ (the edge bits so far,
in reading order), and natural numbers $c$, $c_3$, $p$, $n$, $r$, $l$, $j$, $d$ (meant as the
clause count, three times it, the diamond top, the row end, the row vertex, the row loop index,
the clause index and the detour vertex).

On the emitter's stacks such a state holds each counter as a unary stack of $\mathrm{cl}$ symbols
and the edge bits $q$ on $Q$ reversed, as name-bit symbols; the scratch stacks $Y$ and $Z$ are
empty, and $X$ is empty except while a new name is copied onto $V$.

Formalized by `Cslib.Complexity.Karp.EmitHam.MS`, a structure declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#ms).

## Stacks of a quiescent emitter state

In a quiescent state $s$, the stacks $T$, $O$, $F$,
$V$, $W$, $G$ and $X$ hold the lists that $s$ records for them; the stack $Q$ holds the edge
bits of $s$ as bit symbols, reversed so that the last bit is on top; each counter stack $C$,
$M$, $P$, $N$, $R$, $L$, $J$, $D$ holds as many copies of the symbol $\mathrm{cl}$ as the
value that $s$ records for the corresponding counter (the clause count, the counter reserved
for three times the clause count, the diamond top, the row end, the row vertex, the row loop
index, the clause index and the detour vertex), with no relation imposed between these values;
and the scratch stacks $Y$ and $Z$ are empty.

Formalized by `Cslib.Complexity.Karp.EmitHam.MS.stk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#stk).

## Counter values of a quiescent emitter state

For a quiescent state $s$, the value of the
counters $p$, $n$, $r$, $j$, $d$ is respectively the diamond top, the row end, the row vertex,
the clause index and the detour vertex recorded in $s$.

Formalized by `Cslib.Complexity.Karp.EmitHam.MS.val`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#val).

## Copying a counter in the HAMPATH emitter

Let $a$, $c$ and $Z$ be three distinct stacks of
the emitter machine (with $Z$ its copy scratch stack), $u$ a symbol of $a$ and $x$ a symbol of $c$.
Suppose the machine at label $l_1$ pops $a$ until it is empty, pushing $x$ onto $c$ and the
clause separator $\mathrm{cl}$ onto $Z$ for each popped symbol, and then continues at $l_2$; and
at $l_2$ pops $Z$ until it is empty, pushing $u$ onto $a$ for each popped symbol, and then
continues at $l'$. If the stacks $S$ hold exactly $n$ copies of $u$ on $a$ and nothing on $Z$,
then for every flag $v$ there is a flag $v'$ such that the machine goes in exactly $2n + 2$ steps
from label $l_1$ with flag $v$ and stacks $S$ to label $l'$ with flag $v'$ and the stacks $S$
with $n$ copies of $x$ pushed onto $c$.

Formalized by `Cslib.Complexity.Karp.EmitHam.cp_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#cp-run).

## Bits pushed by a copy site of the HAMPATH emitter

For a quiescent state $s$ of the
HAMPATH emitter and a copy site $j$, the atom of $j$ in $s$ is the list of $c + e$ copies of
true followed by one false, where $c$ is the value in $s$ of the counter that $j$ copies and
$e \in \{0, 1\}$ is the number of extra ones that $j$ adds.

Formalized by `Cslib.Complexity.Karp.EmitHam.atom`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#atom).

## Run of a HAMPATH copy site

Let $j$ be a copy site, $b$ and $v$ bits and $s$ a quiescent
state of the HAMPATH emitter; let $c$ be the value in $s$ of the counter that $j$ reads and $e$
the number of ones that $j$ adds to its counter. Started at label $\mathrm{cpA}(j, b)$ with
internal state $v$ and the stacks of $s$, the emitter runs in exactly $2c + 3$ steps to the label
that follows $j$ for $b$, with some internal state and the stacks of the quiescent state obtained
from $s$ by appending $c + e$ copies of true followed by one false to its edge bits.

Formalized by `Cslib.Complexity.Karp.EmitHam.site_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#site-run).

## Copy sites chained in the HAMPATH emitter

Copy sites $j_1, \dots, j_n$ are chained from
label $l_0$ to label $l$ with passed bit $b$ when $l_0$ is the label at which $j_1$ starts with
passed bit $b$, the label where each $j_i$ with $i < n$ continues with passed bit $b$ is the label
at which $j_{i+1}$ starts with passed bit $b$, and $j_n$ continues at $l$ with passed bit $b$. The
empty list of sites is chained from $l_0$ to $l$ exactly when $l_0 = l$.

Formalized by `Cslib.Complexity.Karp.EmitHam.Chain`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#chain).

## Step count of a list of copy sites in the HAMPATH emitter

For a quiescent state $s$ and
copy sites $j_1, \dots, j_n$, the step count is $\sum_{i=1}^{n} (2 v_i + 3)$, where $v_i$ is the
value in $s$ of the counter that $j_i$ copies.

Formalized by `Cslib.Complexity.Karp.EmitHam.chainCost`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#chain-cost).

## Running a chain of copy sites in the HAMPATH emitter

Let $j_1, \dots, j_n$ be copy sites
chained from label $l_0$ to label $l$ with passed bit $b$. Then for every quiescent state $s$ and
every flag $v$ there is a flag $v'$ such that the emitter machine goes, in exactly as many steps as
the step count of $j_1, \dots, j_n$ at $s$, from label $l_0$ with flag $v$ and the stacks of $s$ to
label $l$ with flag $v'$ and the stacks of the state that differs from $s$ only in that the atoms
of $j_1, \dots, j_n$ at $s$, concatenated in this order, are appended to its edge bits.

Formalized by `Cslib.Complexity.Karp.EmitHam.chain_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 507](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L507). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#chain-run).

## A symbol that reads as a name bit is that bit

For every symbol $x$ of the stack alphabet
of the SAT verifier and every bit $b$, if $x$ reads as the name bit $b$, then $x$ is the name-bit
symbol for $b$.

Formalized by `Cslib.Complexity.Karp.EmitHam.bit_inv`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 532](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L532). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#bit-inv).

## Comparing a name with the top entry of the variable stack

Let $l_c$ be a label at which
the emitter machine compares the bit blocks of the stacks $F$ and $V$, with scratch stacks $X$ and
$Y$, going to $r_1(b_T)$ if the blocks are equal and to $r_1(b_F)$ otherwise. Suppose that for each
bit $b$ the machine at $r_1(b)$ moves the bit block of $X$ onto $F$ and then continues at
$r_2(b)$, and at $r_2(b)$ moves the bit block of $Y$ onto $V$ and then continues at $n_x(b)$. Let
$s$ be a quiescent state whose stack $F$ holds the bit symbols of a bit list $u$ followed by a list
$A$, whose stack $V$ holds the bit symbols of a bit list $w$ followed by a list $B$, where neither
$A$ nor $B$ starts with a bit symbol, and whose stack $X$ is empty. Then for every flag $v$ there is
a flag $v'$ such that the machine goes in at most $3 |w| + 3$ steps from label $l_c$ with flag $v$
and the stacks of $s$ to label $n_x(b_T)$ if $u = w$ and to $n_x(b_F)$ otherwise, with flag $v'$
and again the stacks of $s$.

Formalized by `Cslib.Complexity.Karp.EmitHam.cmpR_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 537](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#cmp-r-run).

## Name of a variable in the HAMPATH emitter

The name of a variable $x \in \mathbb{N}$ is the
list of name-bit symbols $\mathrm{bit}(b_0), \dots, \mathrm{bit}(b_{k-1})$, where
$b_0 \cdots b_{k-1}$ is the binary encoding of $x$, least significant bit first (the empty list
for $x = 0$).

Formalized by `Cslib.Complexity.Karp.EmitHam.name`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 574](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L574). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#name).

## Variable stack of the HAMPATH emitter

For a list $x_1, \dots, x_k$ of variables (natural
numbers), the variable stack is the list of symbols obtained by concatenating, for
$i = 1, \dots, k$ in order, the name bits of $x_i$ followed by the separator symbol
$\mathrm{cl}$. With the head of the list on top, $x_1$ is the top entry and each name sits above
its separator.

Formalized by `Cslib.Complexity.Karp.EmitHam.vstk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 577](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L577). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#vstk).

## Variable-stack symbols of the HAMPATH emitter

A token symbol is a variable-stack symbol
when it is a name bit $\mathrm{bit}(b)$ for some bit $b$ or the separator $\mathrm{cl}$; the
polarity markers, the value markers and the dead marker are not.

Formalized by `Cslib.Complexity.Karp.EmitHam.isVS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 580](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L580). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#is-vs).

## HAMPATH emitter, phase A: moving the walk stack back onto the variable stack

Let $f$ be
a Boolean, let $L$ be a list of symbols each of which is a name bit or the separator
$\mathrm{cl}$, and let $s$ be a quiescent state of the HAMPATH emitter whose stack $W$ is $L$.
Then for every value $v$ of the machine's Boolean variable there is a value $v'$ such that the
emitter goes in exactly $|L|$ steps from label $\mathrm{ab}(f)$, variable $v$ and the stacks of
$s$ to label $\mathrm{ab}(f)$, variable $v'$ and the stacks of the state obtained from $s$ by
emptying $W$ and replacing $V$ by the reverse of $L$ followed by the old contents of $V$.

Formalized by `Cslib.Complexity.Karp.EmitHam.ab_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#ab-run).

## HAMPATH emitter, phase A: searching the variable stack for a name

For $y \in \mathbb{N}$
write $\mathrm{name}(y)$ for the canonical binary encoding of $y$ as name-bit symbols, and for a
list $\mathit{vs}$ of naturals write $\mathrm{vstk}(\mathit{vs})$ for the variable stack: the
names of the entries of $\mathit{vs}$, each followed by the separator $\mathrm{cl}$. Let
$x \in \mathbb{N}$ and let $A$ be a list of symbols that is empty or does not start with a name
bit. Then for every list $\mathit{vs}$ of naturals, every Boolean $f$, every quiescent state $s$
of the HAMPATH emitter whose stack $F$ is $\mathrm{name}(x)$ followed by $A$, whose stack $V$ is
$\mathrm{vstk}(\mathit{vs})$ and whose stack $X$ is empty, and every value $v$ of the machine's
Boolean variable, writing $g$ for the Boolean that is true exactly when $f$ is true or $x$
occurs in $\mathit{vs}$, there is a value $v'$ such that the emitter goes in at most
$6|\mathrm{vstk}(\mathit{vs})| + 1$ steps from label $\mathrm{aw}(f)$, variable $v$ and the
stacks of $s$ to label $\mathrm{ab}(g)$, variable $v'$ and the stacks of the state obtained
from $s$ by emptying $V$ and replacing $W$ by the reverse of $\mathrm{vstk}(\mathit{vs})$
followed by the old contents of $W$.

Formalized by `Cslib.Complexity.Karp.EmitHam.aw_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 660](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L660). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#aw-run).

## HAMPATH emitter, phase A: copying a reversed name onto two stacks

Let $u$ be a list of
bits and let $s$ be a quiescent state of the HAMPATH emitter whose stack $X$ holds $u$ as
name-bit symbols. Then for every value $v$ of the machine's Boolean variable there is a value
$v'$ such that the emitter goes in exactly $|u| + 1$ steps from label $\mathrm{ad3}$, variable
$v$ and the stacks of $s$ to label $\mathrm{a0}$, variable $v'$ and the stacks of the state
obtained from $s$ by emptying $X$ and replacing each of $F$ and $V$ by the reverse of $u$ (as
name-bit symbols) followed by its old contents.

Formalized by `Cslib.Complexity.Karp.EmitHam.ad3_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 710](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L710). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-05/index.html#ad3-run).

## HAMPATH emitter, phase A: one literal

For $x \in \mathbb{N}$ write $\mathrm{name}(x)$
for the canonical binary encoding of $x$ as name-bit symbols. Let $\ell = (x, p)$ be a literal
with variable $x$ and polarity $p$: its tokens are $\mathrm{name}(x)$ followed by the polarity
marker $\mathrm{lit}(p)$, and its reversed tokens $r_\ell$ are $\mathrm{lit}(p)$ followed by the
reverse of $\mathrm{name}(x)$. For a list $\mathit{vs}$ of naturals write
$\mathrm{vstk}(\mathit{vs})$ for the names of the entries of $\mathit{vs}$, each followed by the
separator $\mathrm{cl}$, and $\mathrm{ins}(x, \mathit{vs})$ for $\mathit{vs}$ if $x$ occurs in
$\mathit{vs}$ and for $\mathit{vs}$ with $x$ added at the front otherwise. Let $R$ be a list of
symbols that is empty or does not start with a name bit, let $\mathit{vs}$ be a list of
naturals, and let $s$ be a quiescent state of the HAMPATH emitter whose stack $T$ is $r_\ell$
followed by $R$, whose stack $V$ is $\mathrm{vstk}(\mathit{vs})$ and whose stacks $W$ and $X$
are empty. Then for every value $v$ of the machine's Boolean variable there is a value $v'$ such
that the emitter goes in at most $8|\mathrm{vstk}(\mathit{vs})| + 4|r_\ell| + 8$ steps from
label $\mathrm{a0}$, variable $v$ and the stacks of $s$ to label $\mathrm{a0}$, variable $v'$
and the stacks of the state obtained from $s$ by setting $T$ to $R$, $F$ to the tokens of $\ell$
followed by the old contents of $F$, and $V$ to $\mathrm{vstk}(\mathrm{ins}(x, \mathit{vs}))$.

Formalized by `Cslib.Complexity.Karp.EmitHam.alit_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 757](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L757). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#alit-run).

## HAMPATH emitter, phase A: the literals of a clause

Notation: $\mathrm{name}(x)$ is the
canonical binary encoding of $x \in \mathbb{N}$ as name-bit symbols; a literal $\ell = (x, p)$
has tokens $\mathrm{name}(x)$ followed by the polarity marker $\mathrm{lit}(p)$ and reversed
tokens $r_\ell$, namely $\mathrm{lit}(p)$ followed by the reverse of $\mathrm{name}(x)$;
$\mathrm{vstk}(\mathit{vs})$ is the list of the names of the entries of a list $\mathit{vs}$ of
naturals, each followed by the separator $\mathrm{cl}$; and $\mathrm{ins}(x, \mathit{vs})$ is
$\mathit{vs}$ if $x$ occurs in $\mathit{vs}$ and $\mathit{vs}$ with $x$ added at the front
otherwise. Let $L_b \in \mathbb{N}$, let $\ell_1, \dots, \ell_k$ be literals with variables
$x_1, \dots, x_k$, let $n = |r_{\ell_1}| + \dots + |r_{\ell_k}|$, and let $R$ be a list of
symbols that is empty or does not start with a name bit. Then for every list $\mathit{vs}$ of
naturals with $|\mathrm{vstk}(\mathit{vs})| + n \le L_b$, every quiescent state $s$ of the
HAMPATH emitter whose stack $T$ is the concatenation of $r_{\ell_k}, \dots, r_{\ell_1}$ followed
by $R$, whose stack $V$ is $\mathrm{vstk}(\mathit{vs})$ and whose stacks $W$ and $X$ are empty,
and every value $v$ of the machine's Boolean variable, there is a value $v'$ such that the
emitter goes in at most $n(8L_b + 12)$ steps from label $\mathrm{a0}$, variable $v$ and the
stacks of $s$ to label $\mathrm{a0}$, variable $v'$ and the stacks of the state obtained from
$s$ by setting $T$ to $R$, $F$ to the concatenated tokens of $\ell_1, \dots, \ell_k$ followed by
the old contents of $F$, and $V$ to
$\mathrm{vstk}(\mathrm{ins}(x_1, \dots \mathrm{ins}(x_k, \mathit{vs}) \dots))$.

Formalized by `Cslib.Complexity.Karp.EmitHam.alits_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 812](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L812). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#alits-run).

## HAMPATH emitter, phase A: one clause

Notation: $\mathrm{name}(x)$ is the canonical
binary encoding of $x \in \mathbb{N}$ as name-bit symbols; a literal $\ell = (x, p)$ has tokens
$\mathrm{name}(x)$ followed by the polarity marker $\mathrm{lit}(p)$ and reversed tokens
$r_\ell$, namely $\mathrm{lit}(p)$ followed by the reverse of $\mathrm{name}(x)$;
$\mathrm{vstk}(\mathit{vs})$ is the list of the names of the entries of a list $\mathit{vs}$ of
naturals, each followed by the separator $\mathrm{cl}$; and $\mathrm{ins}(x, \mathit{vs})$ is
$\mathit{vs}$ if $x$ occurs in $\mathit{vs}$ and $\mathit{vs}$ with $x$ added at the front
otherwise. Let $L_b \in \mathbb{N}$ and let $C$ be a clause with literals $\ell_1, \dots, \ell_k$
and variables $x_1, \dots, x_k$. The tokens of $C$ are the concatenated tokens of
$\ell_1, \dots, \ell_k$ followed by $\mathrm{cl}$, and its reversed tokens $r_C$ are
$\mathrm{cl}$ followed by the concatenation of $r_{\ell_k}, \dots, r_{\ell_1}$. Let $R$ be a list
of symbols that is empty or starts with $\mathrm{cl}$, let $\mathit{vs}$ be a list of naturals
with $|\mathrm{vstk}(\mathit{vs})| + |r_C| \le L_b$, and let $s$ be a quiescent state of the
HAMPATH emitter whose stack $T$ is $r_C$ followed by $R$, whose stack $V$ is
$\mathrm{vstk}(\mathit{vs})$ and whose stacks $W$ and $X$ are empty. Then for every value $v$ of
the machine's Boolean variable there is a value $v'$ such that the emitter goes in at most
$|r_C|(8L_b + 12)$ steps from label $\mathrm{a0}$, variable $v$ and the stacks of $s$ to label
$\mathrm{a0}$, variable $v'$ and the stacks of the state obtained from $s$ by setting $T$ to
$R$, $F$ to the tokens of $C$ followed by the old contents of $F$, and $V$ to
$\mathrm{vstk}(\mathrm{ins}(x_1, \dots \mathrm{ins}(x_k, \mathit{vs}) \dots))$, and by
increasing the clause count by $1$ and the triple clause count by $3$.

Formalized by `Cslib.Complexity.Karp.EmitHam.aclause_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 850](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L850). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#aclause-run).

## HAMPATH emitter, phase A: the clauses of a formula

Notation: $\mathrm{name}(x)$ is the
canonical binary encoding of $x \in \mathbb{N}$ as name-bit symbols; a literal $\ell = (x, p)$
has tokens $\mathrm{name}(x)$ followed by the polarity marker $\mathrm{lit}(p)$; a clause $C$
with literals $\ell_1, \dots, \ell_k$ has tokens the concatenated tokens of
$\ell_1, \dots, \ell_k$ followed by the separator $\mathrm{cl}$, and reversed tokens $r_C$,
namely $\mathrm{cl}$ followed by, for $\ell = \ell_k, \dots, \ell_1$ in turn,
$\mathrm{lit}(p)$ and the reverse of $\mathrm{name}(x)$; $\mathrm{vstk}(\mathit{vs})$ is the
list of the names of the entries of a list $\mathit{vs}$ of naturals, each followed by
$\mathrm{cl}$; and $\mathrm{ins}(x, \mathit{vs})$ is $\mathit{vs}$ if $x$ occurs in
$\mathit{vs}$ and $\mathit{vs}$ with $x$ added at the front otherwise. Let $L_b \in \mathbb{N}$,
let $\varphi$ be a CNF formula with clauses $C_1, \dots, C_m$, whose tokens are the
concatenated tokens of $C_1, \dots, C_m$, let $y_1, \dots, y_n$ be the variables of the literals
of $\varphi$ in order of occurrence (with repetitions), let
$N = |r_{C_1}| + \dots + |r_{C_m}|$, and let $R$ be a list of symbols that is empty or starts
with $\mathrm{cl}$. Then for every list $\mathit{vs}$ of naturals with
$|\mathrm{vstk}(\mathit{vs})| + N \le L_b$, every quiescent state $s$ of the HAMPATH emitter
whose stack $T$ is the concatenation of $r_{C_m}, \dots, r_{C_1}$ followed by $R$, whose stack
$V$ is $\mathrm{vstk}(\mathit{vs})$ and whose stacks $W$ and $X$ are empty, and every value $v$
of the machine's Boolean variable, there is a value $v'$ such that the emitter goes in at most
$N(8L_b + 12)$ steps from label $\mathrm{a0}$, variable $v$ and the stacks of $s$ to label
$\mathrm{a0}$, variable $v'$ and the stacks of the state obtained from $s$ by setting $T$ to
$R$, $F$ to the tokens of $\varphi$ followed by the old contents of $F$, and $V$ to
$\mathrm{vstk}(\mathrm{ins}(y_1, \dots \mathrm{ins}(y_n, \mathit{vs}) \dots))$, and by
increasing the clause count by $m$ and the triple clause count by $3m$.

Formalized by `Cslib.Complexity.Karp.EmitHam.aformula_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 880](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L880). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#aformula-run).

## Initial state of the HAMPATH emitter

For a CNF formula $\varphi$ and an output list $o$,
the initial state is the quiescent state whose token stack holds the tokens of $\varphi$ in
reverse reading order, whose output stack is $o$, and all of whose other stacks are empty and
counters zero.

Formalized by `Cslib.Complexity.Karp.EmitHam.initMS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 914](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L914). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#init-ms).

## The emitter state before the diamonds

For a CNF formula $\varphi$ with $m$ clauses and an
output list $o$, this is the quiescent state whose output stack is $o$, whose stack $F$ holds the
tokens of $\varphi$ in reading order, whose stack $V$ is the variable stack of the distinct
variables of $\varphi$ (each kept at its last occurrence), whose clause count and diamond top are
both $m$, whose count of three times the clauses is $3m$, and all of whose other stacks are empty
and other counters zero.

It is the state that phase A, followed by setting the diamond top, reaches from the initial
state.

Formalized by `Cslib.Complexity.Karp.EmitHam.diaMS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 919](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L919). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#dia-ms).

## Phase A of the HAMPATH emitter

Let $\varphi$ be a CNF formula with $m$ clauses whose token
list has length $L$, let $o$ be a list of bits and let $v$ be a bit. Started at label
$\mathrm{a0}$ with internal state $v$ and the stacks of the initial emitter state of $\varphi$ and
$o$ (the token stack holding the tokens of $\varphi$ reversed, the output stack holding $o$, and
everything else empty), the emitter reaches, within at most $L(8L + 12) + 2m + 3$ steps, label
$\mathrm{h0}$ with some internal state and the stacks of the emitter state of $\varphi$ and $o$
after phase A (the tokens of $\varphi$ on $F$, the variable stack of the distinct variables of
$\varphi$ on $V$, $m$ on the counters $C$ and $P$, $3m$ on $M$, $o$ on the output stack, and
everything else empty).

Formalized by `Cslib.Complexity.Karp.EmitHam.phaseA_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean, line 924](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmitMachine.lean#L924). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#phase-a-run).

## Token symbols of the HAMPATH emitter

A symbol is a token when it is a name bit, a
polarity marker or the clause separator $\mathsf{cl}$; the value markers and the dead marker are
not tokens. The emitter moves tokens between its stacks $T$ and $F$.

Formalized by `Cslib.Complexity.Karp.EmitHam.isTok`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#is-tok).

## The tokens of a literal do not start with a clause end

For every literal $(n, p)$ with
variable index $n \in \mathbb{N}$ and polarity $p$, the token list of $(n, p)$ is nonempty and
its first symbol is not the clause-end marker $\mathsf{cl}$.

Formalized by `Cslib.Complexity.Karp.EmitHam.litToks_head`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#lit-toks-head).

## One literal of the detour walk

Let $y \in \mathbb{N}$ have binary encoding
$\mathrm{bin}(y)$, let $l = (z, b)$ be a literal with token list $\tau$, let $\rho$ and $\nu$ be
lists of symbols, let $p_+$, $p_-$ and $v$ be bits, and let $s$ be a quiescent state of the
HAMPATH emitter such that $F$ holds $\tau$ followed by $\rho$, $V$ holds the name of $y$, then
the clause symbol $\mathrm{cl}$, then $\nu$, and the scratch stack $X$ is empty. Then there is a
bit $v'$ such that the emitter goes in at most $3|\mathrm{bin}(y)| + |\tau| + 5$ steps from the
detour-walk label with clause flags $(p_+, p_-)$, state bit $v$ and the stacks of $s$ to the
detour-walk label with clause flags $(p_+ \lor (z = y \land b), p_- \lor (z = y \land \lnot b))$
and state bit $v'$, with the stacks of $s$ changed as follows: $F$ becomes $\rho$ and $\tau$
reversed is prepended to $T$.

Formalized by `Cslib.Complexity.Karp.EmitHam.dlit_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#dlit-run).

## The literals of a clause in the detour walk

Let $y \in \mathbb{N}$ have binary encoding
$\mathrm{bin}(y)$ and let $\nu$ and $\rho$ be lists of symbols. For every list $C$ of literals
with token list $\tau$ (the tokens of its literals in order, without a clause separator), all
bits $p_+, p_-, b$, and every quiescent state $s$ of the emitter such that $F$ holds $\tau$
followed by $\rho$, $V$ holds the name of $y$, then a clause separator, then $\nu$, and the
scratch stack $X$ is empty, there is a state bit $b'$ such that the emitter goes in at most
$|\tau|(3|\mathrm{bin}(y)| + 6)$ steps from the detour-walk label with clause flags
$(p_+, p_-)$, state bit $b$ and the stacks of $s$ to the detour-walk label with clause flags
$(p_+ \lor ((y, \mathrm{true}) \in C), p_- \lor ((y, \mathrm{false}) \in C))$ and state bit $b'$,
with the stacks of $s$ changed as follows: $F$ becomes $\rho$ and $\tau$ reversed is prepended to
$T$.

Formalized by `Cslib.Complexity.Karp.EmitHam.dlits_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#dlits-run).

## One clause of the detour walk

Let $B, m, i, y, j \in \mathbb{N}$, let $C$ be a clause
with token list $\mathrm{toks}(C)$, let $\rho$ and $\nu$ be lists of symbols and $b$ a state bit,
and let $s$ be a quiescent state of the emitter such that $F$ holds $\mathrm{toks}(C)$ followed by
$\rho$, $V$ holds the name of $y$, then a clause separator, then $\nu$, the scratch stack $X$ is
empty, the counter $J$ equals $j$, the counter $D$ equals row vertex $3j + 1$ of diamond $i$ for
$m$ clauses, each of the counters $P, N, R, J, D$ is at most $B$, and the binary encoding of $y$
has length at most $B$. Then for some state bit $b'$ the emitter goes in at most
$|\mathrm{toks}(C)|(3B + 6) + 16B + 26$ steps from the detour-walk label with both clause flags
false, state bit $b$ and the stacks of $s$ back to the same label with state bit $b'$ and the
stacks of $s$ changed as follows: $F$ becomes $\rho$, $\mathrm{toks}(C)$ reversed is prepended to
$T$, $J$ becomes $j + 1$, $D$ increases by $3$, and the edge-bit list $q$ is extended by the bits
of the detour arcs of clause $j$ (contents $C$) in diamond $i$ for variable $y$.

Formalized by `Cslib.Complexity.Karp.EmitHam.dclause_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#dclause-run).

## The detour walk of a diamond in the HAMPATH emitter

Let $B$, $m$, $i$ and $y$ be natural
numbers and $\varphi = C_0 \cdots C_{m-1}$ a CNF formula with $m$ clauses. Write
$\tau = m + i(3m+2)$ for the top vertex of diamond $i$ and $\rho_l = \tau + 1 + l$ for its row
vertices, encode an arc $(a, b)$ by the bits $1^a 0 1^b 0$, write $\mathrm{toks}(\psi)$ for the
token sequence of a list of clauses $\psi$, and call the bits of the binary code
$\mathrm{enc}(y)$ of $y$, as symbols, the name bits of $y$. The detour arcs of clause $j$ are
$(\rho_{3j+1}, j)$ and $(j, \rho_{3j+2})$ if the literal $(y, \mathrm{true})$ is in $C_j$,
followed by $(\rho_{3j+2}, j)$ and $(j, \rho_{3j+1})$ if $(y, \mathrm{false})$ is in $C_j$. Let
$\sigma$ be a list of symbols and $q_0$ a list of bits, and suppose $|\mathrm{enc}(y)| \le B$
and $\rho_{3m} \le B$. Then for every splitting $\varphi = \pi \kappa$ into a prefix $\pi$ and a
suffix $\kappa$ of clauses, every quiescent state $s$ of the emitter and every internal bit $v$:
if $F$ holds $\mathrm{toks}(\kappa)$, $T$ holds $\mathrm{toks}(\pi)$ reversed, $V$ holds the name
bits of $y$ followed by the separator $\mathsf{cl}$ and then $\sigma$, $X$ is empty,
$J = |\pi|$, $D = \rho_{3|\pi|+1}$, the edge bits are $q_0$ followed by the codes of the detour
arcs of the clauses $j < |\pi|$ in increasing order of $j$, and $P$, $N$, $R$ are at most $B$,
then there is an internal bit $v'$ such that the emitter goes, in at most
$|\mathrm{toks}(\kappa)|(3B+6) + |\kappa|(16B+26) + 1$ steps, from label
$\mathsf{dw}(\mathrm{false}, \mathrm{false})$ with bit $v$ and the stacks of $s$ to label
$\mathsf{t0}$ with bit $v'$ and the stacks of the state obtained from $s$ by emptying $F$,
setting $T$ to $\mathrm{toks}(\varphi)$ reversed, $J = m$ and $D = \rho_{3m+1}$, and setting the
edge bits to $q_0$ followed by the codes of the detour arcs of the clauses $j < m$ in increasing
order of $j$.

Formalized by `Cslib.Complexity.Karp.EmitHam.dwalk_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#dwalk-run).

## Frame copy sites of the HAMPATH emitter

The list of the eight copy sites of a diamond's
frame arcs, in order: the source site and then the target site of the first, second, third and
fourth frame arc.

Formalized by `Cslib.Complexity.Karp.EmitHam.frameSites`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#frame-sites).

## Row copy sites of the HAMPATH emitter

The list of the four copy sites of the two row arcs
between consecutive row vertices of a diamond, in order: the source site and then the target site
of the first and of the second row arc.

Formalized by `Cslib.Complexity.Karp.EmitHam.rowSites`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#row-sites).

## Front of a diamond

Let $B, m, i \in \mathbb{N}$, let $b$ be a state bit, and let $s$ be a
quiescent state of the emitter whose stack $V$ is nonempty, whose counter $P$ equals the top of
diamond $i$ for $m$ clauses, whose counter $M$ equals $3m$, whose counter $N$ is $0$, and whose
counters $R$, $J$, $D$ are at most $B$, and suppose row vertex $3m$ of diamond $i$ is at most $B$.
Then for some state bit $b'$ the emitter goes in at most $20B + 30$ steps from label $\mathrm{h0}$
with state bit $b$ and the stacks of $s$ to label $\mathrm{r0}$ with state bit $b'$ and the stacks
of $s$ with $N$ set to row vertex $3m$ of diamond $i$ and the edge-bit list $q$ extended by the
bits of the frame arcs of diamond $i$.

Formalized by `Cslib.Complexity.Karp.EmitHam.dfront_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#dfront-run).

## The row loop of a diamond in the HAMPATH emitter

Let $B$, $m$ and $i$ be natural
numbers, write $\tau = m + i(3m+2)$ for the top vertex of diamond $i$ and $\rho_l = \tau + 1 + l$
for its row vertices, and encode an arc $(a, b)$ by the bits $1^a 0 1^b 0$. Let $s$ be a quiescent
state of the emitter whose counters satisfy $M = 3m$, $L = 0$, $R = \rho_0$, $P \le B$,
$N \le B$, $J \le B$ and $D \le B$, and suppose $\rho_{3m} \le B$ and $3m \le B$. Then for every
internal bit $v$ there is an internal bit $v'$ such that the emitter goes, in at most
$B(8B+15) + 2$ steps, from label $\mathsf{r3}$ with bit $v$ and the stacks of $s$ to label
$\mathsf{e0}$ with bit $v'$ and the stacks of the state obtained from $s$ by setting
$R = \rho_{3m}$ and appending to its edge bits the codes of the arcs $(\rho_l, \rho_{l+1})$ and
$(\rho_{l+1}, \rho_l)$ for $l = 0, \dots, 3m-1$, in this order.

Formalized by `Cslib.Complexity.Karp.EmitHam.drow_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#drow-run).

## Adding units along no stacks

For every $i \in \mathbb{N}$ and all stack contents $S$ of
the HAMPATH emitter, adding $i$ units to the stacks named in the empty list of (stack, symbol)
pairs leaves $S$ unchanged: $\mathrm{addU}([\,], i, S) = S$.

Formalized by `Cslib.Complexity.Karp.EmitHam.addU_nil`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#add-u-nil).

## Draining a counter

Let $k$ be a stack of the emitter and $\ell, \ell'$ labels such that
the instruction at $\ell$ is the transfer loop that pops stack $k$ until it is empty, pushing
nothing, and then goes to $\ell'$. If $S$ is an assignment of stack contents in which stack $k$
consists of $n$ copies of a symbol $u$, then for every state bit $b$ the emitter goes in exactly
$n + 1$ steps from label $\ell$ with state bit $b$ and stacks $S$ to label $\ell'$ with state bit
false and the stacks $S$ with stack $k$ emptied.

Formalized by `Cslib.Complexity.Karp.EmitHam.drain_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 445](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#drain-run).

## Moving the tokens back in the HAMPATH emitter

Let $L$ be a list of symbols that are all
tokens, $s$ a quiescent state of the emitter whose stack $T$ holds $L$, and $v$ an internal bit.
Then there is an internal bit $v'$ such that the emitter goes in exactly $|L| + 1$ steps from label
$\mathsf{t0}$ with bit $v$ and the stacks of $s$ to label $\mathsf{t1}$ with bit $v'$ and the
stacks of the state obtained from $s$ by emptying $T$ and replacing $F$ by $L$ reversed followed
by $F$.

Formalized by `Cslib.Complexity.Karp.EmitHam.t0_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-06/index.html#t0-run).

## The row of a diamond in the HAMPATH emitter

Let $B$, $m$ and $i$ be natural numbers,
write $\tau = m + i(3m+2)$ for the top vertex of diamond $i$ and $\rho_l = \tau + 1 + l$ for its
row vertices, and encode an arc $(a, b)$ by the bits $1^a 0 1^b 0$. Let $s$ be a quiescent state
of the emitter whose counters satisfy $P = \tau$, $M = 3m$, $L = 0$, $R = 0$, $N \le B$,
$J \le B$ and $D \le B$, and suppose $\rho_{3m} \le B$. Then for every internal bit $v$ there is
an internal bit $v'$ such that the emitter goes, in at most $B(8B+15) + 2B + 5$ steps, from label
$\mathsf{r0}$ with bit $v$ and the stacks of $s$ to label $\mathsf{e0}$ with bit $v'$ and the
stacks of the state obtained from $s$ by setting $R = \rho_{3m}$ and appending to its edge bits
the codes of the arcs $(\rho_l, \rho_{l+1})$ and $(\rho_{l+1}, \rho_l)$ for $l = 0, \dots, 3m-1$,
in this order.

Formalized by `Cslib.Complexity.Karp.EmitHam.drowFull_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#drow-full-run).

## The detours of a diamond

Let $B, i, y \in \mathbb{N}$, let $\varphi$ be a CNF formula
with $m$ clauses and token list $\mathrm{toks}(\varphi)$, let $\nu$ be a list of symbols and $b$
a state bit, and let $s$ be a quiescent state of the emitter such that $F$ holds
$\mathrm{toks}(\varphi)$, $T$ and the scratch stack $X$ are empty, $V$ holds the name of $y$, then
a clause separator, then $\nu$, the counter $P$ equals the top of diamond $i$ for $m$ clauses, the
counters $J$ and $D$ are $0$, the counters $N$ and $R$ are at most $B$, the binary encoding of $y$
has length at most $B$, and row vertex $3m$ of diamond $i$ is at most $B$. Then for some state bit
$b'$ the emitter goes in at most
$|\mathrm{toks}(\varphi)|(3B + 6) + m(16B + 26) + 2B + 5$ steps from label $\mathrm{e0}$ with state
bit $b$ and the stacks of $s$ to label $\mathrm{t0}$ with state bit $b'$ and the stacks of $s$
changed as follows: $F$ becomes empty, $T$ becomes $\mathrm{toks}(\varphi)$ reversed, $J$ becomes
$m$, $D$ becomes row vertex $3m + 1$ of diamond $i$, and the edge-bit list $q$ is extended by the
bits of the detour arcs, for $j = 0, \dots, m - 1$ in order, of clause $j$ of $\varphi$ in diamond
$i$ for variable $y$.

Formalized by `Cslib.Complexity.Karp.EmitHam.ddet_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 495](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#ddet-run).

## End of a diamond

Let $\varphi$ be a CNF formula with token list $\mathrm{toks}(\varphi)$,
let $y \in \mathbb{N}$ have binary encoding $\mathrm{bin}(y)$, let $\nu$ be a list of symbols and
$b$ a state bit, and let $s$ be a quiescent state of the emitter whose stack $T$ holds
$\mathrm{toks}(\varphi)$ reversed, whose stack $F$ is empty, and whose stack $V$ holds the name of
$y$, then a clause separator, then $\nu$. Let $p, n, r, j, d$ be the values of the counters
$P, N, R, J, D$ of $s$. Then for some state bit $b'$ the emitter goes in exactly
$|\mathrm{toks}(\varphi)| + |\mathrm{bin}(y)| + n + p + r + j + d + 9$ steps from label
$\mathrm{t0}$ with state bit $b$ and the stacks of $s$ to label $\mathrm{h0}$ with state bit $b'$
and the stacks of the quiescent state obtained from $s$ by emptying $T$, setting $F$ to
$\mathrm{toks}(\varphi)$ and $V$ to $\nu$, prepending the reversed name of $y$ to $G$, setting
$P$ to $n + 1$, and setting $N$, $R$, $J$ and $D$ to $0$.

Formalized by `Cslib.Complexity.Karp.EmitHam.dback_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 519](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L519). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#dback-run).

## One diamond

Let $B, i, y \in \mathbb{N}$, let $u$ be a list of natural numbers, let
$\varphi$ be a CNF formula with $m$ clauses and token list $\mathrm{toks}(\varphi)$, let $b$ be a
state bit, and let $s$ be a quiescent state of the emitter such that $T$ and the scratch stack $X$
are empty, $F$ holds $\mathrm{toks}(\varphi)$, $V$ is the variable stack of the list $y$ followed
by $u$, the counter $P$ equals the top of diamond $i$ for $m$ clauses, the counter $M$ equals
$3m$, the counters $N, R, L, J, D$ are $0$, and $B$ bounds the top of diamond $i + 1$, the length
of the binary encoding of $y$, and the length of $\mathrm{toks}(\varphi)$. Then for some state bit
$b'$ the emitter goes in at most $30B^2 + 100B + 100$ steps from label $\mathrm{h0}$ with state
bit $b$ and the stacks of $s$ back to label $\mathrm{h0}$ with state bit $b'$ and the stacks of
$s$ changed as follows: $V$ becomes the variable stack of $u$, $P$ becomes the top of diamond
$i + 1$, the edge-bit list $q$ is extended by the bits of the arcs of diamond $i$ of $\varphi$ for
variable $y$, and the reversed name of $y$ is prepended to $G$.

Formalized by `Cslib.Complexity.Karp.EmitHam.diamond_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 569](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L569). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#diamond-run).

## The diamonds

Let $B \in \mathbb{N}$ and let $\varphi$ be a CNF formula with $m$ clauses,
token list $\mathrm{toks}(\varphi)$ and list of distinct variables $\mathrm{vars}(\varphi)$ of
length $k$. Suppose the top of diamond $k$ for $m$ clauses, the length of $\mathrm{toks}(\varphi)$,
and the length of the binary encoding of every $y \in \mathrm{vars}(\varphi)$ are at most $B$.
Let $\mathrm{vars}(\varphi)$ split as a list $\pi$ followed by a list $u$, let $b$ be a state bit,
and let $s$ be a quiescent state of the emitter such that $T$ and the scratch stack $X$ are empty,
$F$ holds $\mathrm{toks}(\varphi)$, $V$ is the variable stack of $u$, the counter $P$ equals the
top of diamond $|\pi|$, the counter $M$ equals $3m$, the counters $N, R, L, J, D$ are $0$, and the
edge-bit list $q$ is the bits of the arcs of diamonds $0, \dots, |\pi| - 1$ in order, diamond
$i$ taken for the $i$-th entry of $\mathrm{vars}(\varphi)$. Then for some state bit $b'$ and some
stack contents $g'$ the emitter goes in at most $|u|(30B^2 + 100B + 100)$ steps from label
$\mathrm{h0}$ with state bit $b$ and the stacks of $s$ back to label $\mathrm{h0}$ with state bit
$b'$ and the stacks of $s$ changed as follows: $V$ becomes empty, $P$ becomes the top of diamond
$k$, $q$ becomes the bits of all arcs of the construction for $\varphi$, and $G$ becomes $g'$.

Formalized by `Cslib.Complexity.Karp.EmitHam.diamonds_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#diamonds-run).

## The output phase of the HAMPATH emitter

Let $s$ be a quiescent state of the emitter
whose variable stack $V$ is empty, with clause count $C = c$, diamond-top counter $P = p$, edge
bits $q$ and output stack $o$. Then for every internal bit $v$ there are an internal bit $v'$ and
stacks $S'$ such that the emitter goes in exactly $|q| + 4p + 2c + 11$ steps from label
$\mathsf{h0}$ with bit $v$ and the stacks of $s$ to label $\mathsf{done}$ with bit $v'$ and stacks
$S'$, and the output stack of $S'$ is $1^c 0 1^p 0 1^{p+1} 0$ followed by $q$ and then $o$.

Formalized by `Cslib.Complexity.Karp.EmitHam.final_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 650](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L650). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#final-run).

## Correctness and running time of the HAMPATH emitter

Let $\varphi$ be a CNF formula with
token sequence $\mathrm{toks}(\varphi)$, let $o$ be a list of bits, and let $S$ be stacks in which
the token stack $T$ holds $\mathrm{toks}(\varphi)$ reversed, the output stack $O$ holds $o$, and
every other stack is empty. Then for every internal bit $v$ there are an internal bit $v'$ and
stacks $S'$ such that the emitter goes, in at most $2000(|\mathrm{toks}(\varphi)| + 1)^5$ steps,
from its start label with bit $v$ and stacks $S$ to label $\mathsf{done}$ with bit $v'$ and stacks
$S'$, and the output stack of $S'$ is Sipser's HAMPATH instance for $\varphi$ followed by $o$
(so the instance is read top-first).

Formalized by `Cslib.Complexity.Karp.EmitHam.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean, line 694](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathEmit.lean#L694). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#run).

## The row of a diamond with its clauses inserted

Let $m$ and $i$ be natural numbers and
$c : \mathbb{N} \to \mathbb{N}$ a map, and write $r_l = m + i(3m + 2) + 1 + l$ for the row
vertices of diamond $i$. The row of diamond $i$ for $c$ is the list $r_0, r_1, \dots, r_{3m}$ in
which, for every $j < m$ with $c(j) = i$, the clause vertex $j$ is inserted right after
$r_{3j+1}$.

Formalized by `Cslib.Complexity.Karp.hfRow`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#hf-row).

## Clauses picked up by a diamond

For natural numbers $m$ and $i$ and a map
$c : \mathbb{N} \to \mathbb{N}$, the clauses picked up by diamond $i$ are the list of all
$j < m$ with $c(j) = i$, in increasing order.

These are the clause vertices of the row of diamond $i$, in row order.

Formalized by `Cslib.Complexity.Karp.hfPicks`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#hf-picks).

## The visit of a diamond

For $m$ clauses, a diamond $i$, a clause-to-diamond map $c$ and
a direction $b$, the visit of diamond $i$ is the list consisting of its top
$T_i = m + i(3m+2)$ followed by its row with the clauses sent to $i$ by $c$ inserted, read left
to right if $b$ is true and right to left otherwise.

Formalized by `Cslib.Complexity.Karp.hfDiamond`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#hf-diamond).

## The forward path through the diamonds

Let $m$ and $k$ be natural numbers, let
$c : \mathbb{N} \to \mathbb{N}$ be a map and let $d : \mathbb{N} \to \{\mathrm{true},
\mathrm{false}\}$ give each diamond $i$ a direction $d(i)$. The forward path through the first
$k$ diamonds is the list obtained by concatenating, for $i = 0, 1, \dots, k - 1$ in this order,
the traversal of diamond $i$ for $c$ in direction $d(i)$, and then appending the vertex
$m + k(3m + 2)$, the top of diamond $k$. Here the traversal of diamond $i$ is its top
$m + i(3m + 2)$ followed by its row $r_0, r_1, \dots, r_{3m}$, where
$r_l = m + i(3m + 2) + 1 + l$ and the clause vertex $j$ is inserted right after $r_{3j+1}$ for
every $j < m$ with $c(j) = i$; the row is read left to right if $d(i)$ is true and right to left
otherwise.

Formalized by `Cslib.Complexity.Karp.hfPath`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#hf-path).

## Clause vertices picked up by a row

Let $m$ and $i$ be natural numbers and let
$c : \mathbb{N} \to \mathbb{N}$. A natural number $v$ is one of the clause vertices picked up by the
row of diamond $i$ under $c$, for $m$ clauses, if and only if $v < m$ and $c(v) = i$.

Formalized by `Cslib.Complexity.Karp.mem_hfPicks`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#mem-hf-picks).

## The clause vertices of a row are distinct

For all natural numbers $m$, $i$ and every
function $c : \mathbb{N} \to \mathbb{N}$, the list of clause vertices picked up by the row of
diamond $i$ under $c$, for $m$ clauses, has no repeated entries.

Formalized by `Cslib.Complexity.Karp.nodup_hfPicks`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#nodup-hf-picks).

## Each clause is picked up by exactly one row

Let $m, k$ be natural numbers and let $c$
send every clause $j < m$ to a diamond $c(j) < k$. For each diamond $i$, list the clauses
$j < m$ with $c(j) = i$ in increasing order (the clause vertices picked up by the row of
diamond $i$). Concatenating these lists for $i = 0, \dots, k - 1$ gives a permutation of
$0, 1, \dots, m - 1$.

Formalized by `Cslib.Complexity.Karp.flatMap_hfPicks_perm`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#flat-map-hf-picks-perm).

## The vertices of a diamond row

For natural numbers $m$ and $i$ and a map
$c : \mathbb{N} \to \mathbb{N}$, let $r = m + i(3m + 2) + 1$ be the left end of the row of
diamond $i$. The row of diamond $i$ for $c$ (with its clause vertices inserted) is a permutation
of the concatenation of the list $r, r + 1, \dots, r + 3m$ and the list of clauses picked up by
diamond $i$ for $c$, that is, of all $j < m$ with $c(j) = i$ in increasing order.

Formalized by `Cslib.Complexity.Karp.hfRow_perm`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#hf-row-perm).

## A diamond visit is a block of consecutive vertices plus its clauses

For $m$ clauses, a
diamond $i$, a clause-to-diamond map $c$ and a direction $b$, let $T_i = m + i(3m+2)$ be the top
of diamond $i$. The visit of diamond $i$ in direction $b$ is a rearrangement of the list that
consists of $T_i, T_i + 1, \dots, T_i + 3m + 1$ and then the clauses $j < m$ with $c(j) = i$ in
increasing order.

Formalized by `Cslib.Complexity.Karp.hfDiamond_perm`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#hf-diamond-perm).

## The first $t$ diamonds occupy consecutive vertices

For natural numbers $m$ and $t$, let
$T_i = m + i(3m+2)$. Concatenating, for $i = 0, \dots, t - 1$, the lists
$T_i, T_i + 1, \dots, T_i + 3m + 1$ of $3m + 2$ consecutive numbers (the top and the row of
diamond $i$) gives the list $m, m + 1, \dots, m + t(3m+2) - 1$, that is, the numbers from $m$
to $T_t - 1$ in increasing order.

Formalized by `Cslib.Complexity.Karp.flatMap_range'_hpT`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#flat-map-range-hp-t).

## The forward path visits every vertex once

Let $m, k$ be natural numbers, let $c$ send
every clause $j < m$ to a diamond $c(j) < k$, let $d$ be any directions, and let
$T_k = m + k(3m+2)$. The forward path through the first $k$ diamonds in directions $d$ with
clause choice $c$ is a permutation of the list $0, 1, \dots, T_k$.

Formalized by `Cslib.Complexity.Karp.hfPath_perm`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#hf-path-perm).

## Chain condition for a diamond row

Let $R$ be a relation on $\mathbb{N}$, let $m$ and $i$
be natural numbers and $c : \mathbb{N} \to \mathbb{N}$ a map, and write
$r_l = m + i(3m + 2) + 1 + l$ for the row vertices of diamond $i$. If $R(r_l, r_{l+1})$ holds
for every $l < 3m$, and $R(r_{3j+1}, j)$ and $R(j, r_{3j+2})$ hold for every $j < m$ with
$c(j) = i$, then the row of diamond $i$ for $c$ is a chain for $R$: every entry is related by
$R$ to the next one.

Formalized by `Cslib.Complexity.Karp.isChain_hfRow`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#is-chain-hf-row).

## A row starts at its left end

For $m$ clauses, a diamond $i$ and any clause-to-diamond
map $c$, the row of diamond $i$ read left to right, with the clauses sent to $i$ by $c$
inserted, starts at its left end, the row vertex $T_i + 1$, where $T_i = m + i(3m+2)$ is the
top of diamond $i$.

Formalized by `Cslib.Complexity.Karp.head?_hfRow`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-07/index.html#head-hf-row).

## A row ends at its right end

For $m$ clauses, a diamond $i$ and any clause-to-diamond
map $c$, the row of diamond $i$ read left to right, with the clauses sent to $i$ by $c$
inserted, ends at the row vertex $T_i + 1 + 3m$, where $T_i = m + i(3m+2)$ is the top of
diamond $i$.

Formalized by `Cslib.Complexity.Karp.getLast?_hfRow`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#get-last-hf-row).

## Chain condition for a diamond traversal

Let $R$ be a relation on $\mathbb{N}$, let $m$
and $i$ be natural numbers, $c : \mathbb{N} \to \mathbb{N}$ a map and $b$ a boolean, and write
$t_a = m + a(3m + 2)$ for the top of diamond $a$ and $r_l = t_i + 1 + l$ for the row vertices
of diamond $i$. Suppose that $R(t_i, r_0)$, $R(t_i, r_{3m})$, $R(r_0, t_{i+1})$ and
$R(r_{3m}, t_{i+1})$ hold; that $R(r_l, r_{l+1})$ and $R(r_{l+1}, r_l)$ hold for every
$l < 3m$; that if $b$ is true, then $R(r_{3j+1}, j)$ and $R(j, r_{3j+2})$ hold for every
$j < m$ with $c(j) = i$; and that if $b$ is false, then $R(r_{3j+2}, j)$ and $R(j, r_{3j+1})$
hold for every $j < m$ with $c(j) = i$. Then the traversal of diamond $i$ for $c$ in
direction $b$, followed by $t_{i+1}$, is a chain for $R$: every entry is related by $R$ to the
next one.

Formalized by `Cslib.Complexity.Karp.isChain_hfDiamond`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#is-chain-hf-diamond).

## Chain condition for the forward path

Let $R$ be a relation on $\mathbb{N}$, let $m$ and
$k$ be natural numbers, $c : \mathbb{N} \to \mathbb{N}$ a map and $d : \mathbb{N} \to
\{\mathrm{true}, \mathrm{false}\}$ a choice of directions, and write $t_a = m + a(3m + 2)$ for
the top of diamond $a$. If for every $i < k$ the traversal of diamond $i$ for $c$ in direction
$d(i)$, followed by $t_{i+1}$, is a chain for $R$ (every entry is related by $R$ to the next
one), then the forward path through the first $k$ diamonds for $c$ and $d$ is a chain for
$R$.

Formalized by `Cslib.Complexity.Karp.isChain_hfPath`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#is-chain-hf-path).

## The forward path starts at the first top

For $m$ clauses, $k$ diamonds, any
clause-to-diamond map $c$ and any directions $d$, the forward path through the first $k$
diamonds in directions $d$ with clause choice $c$ starts at the top $T_0 = m$ of diamond $0$.

Formalized by `Cslib.Complexity.Karp.head?_hfPath`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#head-hf-path).

## The forward path ends at the last top

For $m$ clauses, $k$ diamonds, any
clause-to-diamond map $c$ and any directions $d$, the forward path through the first $k$
diamonds in directions $d$ with clause choice $c$ ends at the top $T_k = m + k(3m+2)$.

Formalized by `Cslib.Complexity.Karp.getLast?_hfPath`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#get-last-hf-path).

## Diamond arcs are arcs of the construction

Let $\varphi$ be a CNF formula, let
$x_0, \dots, x_{k-1}$ be its distinct variables in the order used by the construction, and let
$i < k$. Every arc of diamond $i$ for variable $x_i$ is an arc of the HAMPATH construction for
$\varphi$.

Formalized by `Cslib.Complexity.Karp.mem_hamEdges_of_mem_diamondEdges`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#mem-ham-edges-of-mem-diamond-edges).

## The frame arcs of a diamond

Let $\varphi$ be a CNF formula with $m$ clauses, let $i$
and $x$ be natural numbers, and write $t_a = m + a(3m + 2)$ for the top of diamond $a$ and
$r_l = t_i + 1 + l$ for the row vertices of diamond $i$. The four arcs $(t_i, r_0)$,
$(t_i, r_{3m})$, $(r_0, t_{i+1})$ and $(r_{3m}, t_{i+1})$ are arcs of diamond $i$ for the
variable $x$ in the construction for $\varphi$.

Formalized by `Cslib.Complexity.Karp.mem_diamondEdges_frame`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#mem-diamond-edges-frame).

## Row arcs of a diamond

Let $\varphi$ be a CNF formula with $m$ clauses, let $i$ and $x$ be
natural numbers, and write $r_i(l)$ for row vertex $l$ of diamond $i$. For every $l < 3m$, the arcs
of diamond $i$ for variable $x$ include both the arc from $r_i(l)$ to $r_i(l+1)$ and the arc from
$r_i(l+1)$ to $r_i(l)$.

Formalized by `Cslib.Complexity.Karp.mem_diamondEdges_row`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#mem-diamond-edges-row).

## Positive detour arcs of a diamond

Let $\varphi$ be a CNF formula with $m$ clauses, let
$i$, $x$, $j$ be natural numbers with $j < m$, and write $r_i(l)$ for row vertex $l$ of diamond
$i$. If the variable $x$ occurs positively in clause $j$ of $\varphi$ (counting clauses from $0$),
then the arcs of diamond $i$ for variable $x$ include both the arc from $r_i(3j+1)$ to clause
vertex $j$ and the arc from clause vertex $j$ to $r_i(3j+2)$.

Formalized by `Cslib.Complexity.Karp.mem_diamondEdges_pos`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#mem-diamond-edges-pos).

## The detour arcs of a negative occurrence

Let $\varphi$ be a CNF formula with $m$
clauses, let $i$, $x$ and $j$ be natural numbers with $j < m$, and write
$r_l = m + i(3m + 2) + 1 + l$ for the row vertices of diamond $i$. If the negative literal
$\neg x$ occurs in clause $j$ of $\varphi$, then $(r_{3j+2}, j)$ and $(j, r_{3j+1})$ are arcs
of diamond $i$ for the variable $x$ in the construction for $\varphi$.

Formalized by `Cslib.Complexity.Karp.mem_diamondEdges_neg`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#mem-diamond-edges-neg).

## A satisfying choice gives a Hamiltonian path

Let $\varphi$ be a CNF formula with $m$
clauses, let $v_0, \dots, v_{k-1}$ be its distinct variables in the order used by the
construction, let $\sigma$ assign a truth value to every variable, and write
$t_a = m + a(3m + 2)$ for the top of diamond $a$. Let $c : \mathbb{N} \to \mathbb{N}$ be such
that for every $j < m$ we have $c(j) < k$ and clause $j$ of $\varphi$ contains the literal over
$v_{c(j)}$ that $\sigma$ makes true (positive if $\sigma(v_{c(j)})$ is true, negative
otherwise). Then the forward path through the first $k$ diamonds for $c$, with diamond $i$
traversed in direction $\sigma(v_i)$, is a Hamiltonian path from $t_0$ to $t_k$ in the digraph
on the vertices $0, \dots, t_k$ whose arcs are the arcs of the construction for $\varphi$.

Formalized by `Cslib.Complexity.Karp.isHamPath_hfPath`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#is-ham-path-hf-path).

## Satisfiable formulas give Hamiltonian paths (SAT ≤ HAMPATH, forward direction)

Let
$\varphi$ be a satisfiable CNF formula with $m$ clauses and $k$ distinct variables, and let
$T_i = m + i(3m+2)$ be the top of diamond $i$. Then the digraph on the vertices
$0, \dots, T_k$ whose arcs are the arcs of the HAMPATH construction for $\varphi$ has a
Hamiltonian path from $T_0$ to $T_k$.

Formalized by `Cslib.Complexity.Karp.exists_isHamPath_of_cnfSat`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathForward.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathForward.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#exists-is-ham-path-of-cnf-sat).

## Out-neighbours of a top

Let $\varphi$ be a CNF formula with $m$ clauses. In Sipser's
HAMPATH graph for $\varphi$, every arc out of the top $t_i$ of diamond $i$ ends at one of the two
ends $r_{i,0}$ and $r_{i,3m}$ of the row of diamond $i$.

Formalized by `Cslib.Complexity.Karp.hpT_arc`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#hp-t-arc).

## Arcs from a row into a clause vertex

Let $\varphi$ be a CNF formula with $m$ clauses
$C_0, \dots, C_{m-1}$, and let $x_i$ be the $i$-th of its distinct variables (variable $0$ if
$\varphi$ has at most $i$ distinct variables). In Sipser's HAMPATH graph for $\varphi$, clause $j$
is vertex $j$, and $r_{i,l}$ denotes vertex $l$ of the row of diamond $i$. If $l \le 3m$, $j < m$
and $(r_{i,l}, j)$ is an arc of the graph, then either $l = 3j + 1$ and the literal $x_i$ occurs
in $C_j$, or $l = 3j + 2$ and the literal $\neg x_i$ occurs in $C_j$.

Formalized by `Cslib.Complexity.Karp.hpR_arc_clause`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#hp-r-arc-clause).

## Row vertices counted from either end

For $m$ clauses, let $r_{i,l} = m + i(3m + 2) + 1 + l$
be vertex $l$ of the row of diamond $i$. For a Boolean $b$ and a natural number $l$, this is
$r_{i,l}$ if $b$ is true and $r_{i,3m - l}$ if $b$ is false, where $3m - l$ is truncated
subtraction ($0$ when $l > 3m$). For $l \le 3m$ it is vertex $l$ of the row counted from the left
end ($b$ true) or from the right end ($b$ false).

Formalized by `Cslib.Complexity.Karp.hpRo`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#hp-ro).

## Out-neighbours of a row vertex outside the clause vertices

Let $\varphi$ be a CNF formula
with $m$ clauses. In Sipser's HAMPATH graph for $\varphi$, clause $j$ is vertex $j < m$, the top of
diamond $i$ is $t_i = m + i(3m + 2)$ (and $t_{i+1}$ is its bottom), and $\rho_b(i, l)$ denotes
vertex $l$ of the row of diamond $i$ counted from the left end if $b$ is true and from the right
end if $b$ is false. Let $l \le 3m$ and $v \ge m$. If $(\rho_b(i, l), v)$ is an arc of the graph,
then $l < 3m$ and $v = \rho_b(i, l + 1)$, or $l > 0$ and $v = \rho_b(i, l - 1)$, or
$l \in \{0, 3m\}$ and $v = t_{i+1}$.

Formalized by `Cslib.Complexity.Karp.hpRo_arc`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#hp-ro-arc).

## In-neighbours of a row vertex outside the clause vertices

Let $\varphi$ be a CNF formula
with $m$ clauses. In Sipser's HAMPATH graph for $\varphi$, clause $j$ is vertex $j < m$, the top of
diamond $i$ is $t_i = m + i(3m + 2)$, and $\rho_b(i, l)$ denotes vertex $l$ of the row of diamond
$i$ counted from the left end if $b$ is true and from the right end if $b$ is false. Let
$l \le 3m$ and $u \ge m$. If $(u, \rho_b(i, l))$ is an arc of the graph, then $l > 0$ and
$u = \rho_b(i, l - 1)$, or $l < 3m$ and $u = \rho_b(i, l + 1)$, or $l \in \{0, 3m\}$ and
$u = t_i$.

Formalized by `Cslib.Complexity.Karp.arc_hpRo`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#arc-hp-ro).

## Deleting the clause vertices from a path

For a CNF formula $\varphi$ with $m$ clauses
(the clause vertices of Sipser's HAMPATH graph are $0, \dots, m - 1$) and a list $p$ of natural
numbers, the list obtained from $p$ by deleting every entry $v < m$, keeping the other entries in
their order.

Formalized by `Cslib.Complexity.Karp.dropClauses`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#drop-clauses).

## Contracting a clause detour

Let $\varphi$ be a CNF formula with $m$ clauses, let $p$ be
a list of natural numbers, and let $q$ be the list obtained from $p$ by deleting every entry less
than $m$. If $a, j, c$ occur consecutively in $p$ with $j < m$, $a \ge m$ and $c \ge m$, then
$a$ is immediately followed by $c$ in $q$.

Formalized by `Cslib.Complexity.Karp.infix_dropClauses`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#infix-drop-clauses).

## Consecutive vertices of the contracted path are joined by arcs

Let $\varphi$ be a CNF
formula with $m$ clauses and $k$ distinct variables. In Sipser's HAMPATH graph for $\varphi$, clause
$j$ is vertex $j < m$, the top of diamond $i$ is $t_i = m + i(3m + 2)$, and vertex $l \le 3m$ of
its row is $r_{i,l} = t_i + 1 + l$. Let $p$ be a Hamiltonian path of this graph (on the vertices
$0, \dots, t_k$) from $t_0$ to $t_k$ whose detours are normal: for every $j < m$ there is $i < k$
such that $j$ sits in $p$ immediately between $r_{i,3j+1}$ and $r_{i,3j+2}$, in either order. Let
$p'$ be $p$ with the clause vertices deleted. If $v$ comes right after $u$ in $p'$, then
$(u, v)$ is an arc of the graph, $u \ge m$ and $v \ge m$.

Formalized by `Cslib.Complexity.Karp.arc_of_infix_dropClauses`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-08/index.html#arc-of-infix-drop-clauses).

## Every vertex of the contracted path except its end has a successor

Let $\varphi$ be a CNF
formula with $m$ clauses and $k$ distinct variables. In Sipser's HAMPATH graph for $\varphi$, clause
$j$ is vertex $j < m$ and the top of diamond $i$ is $t_i = m + i(3m + 2)$. Let $p$ be a
Hamiltonian path of this graph (on the vertices $0, \dots, t_k$) from $t_0$ to $t_k$, and let $p'$
be $p$ with the clause vertices deleted. Then every vertex $v \ne t_k$ of $p'$ is immediately
followed in $p'$ by some vertex $w$.

Formalized by `Cslib.Complexity.Karp.exists_infix_dropClauses`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#exists-infix-drop-clauses).

## Entering a row and leaving it at once is impossible

Let $\varphi$ be a CNF formula with
$m > 0$ clauses and $n$ distinct variables. For $k \le n$ let $t_k = m + k(3m + 2)$ be the top
of diamond $k$, and for $k < n$ let row $k$ consist of the vertices $t_k + 1 + l$ with
$0 \le l \le 3m$; its left end is $t_k + 1$ and its right end is $t_k + 1 + 3m$. Let $p$ be a
Hamiltonian path from $t_0$ to $t_n$ in Sipser's digraph for $\varphi$ on the vertices
$0, \dots, t_n$ whose clause detours are normal: every clause vertex $j < m$ occurs in $p$
immediately between the vertices $t_k + 3j + 2$ and $t_k + 3j + 3$ of some row $k < n$, in
either order. Let $q$ be $p$ with the clause vertices $0, \dots, m - 1$ deleted. Then for every
$i < n$ and each end $e$ of row $i$, it is not the case that in $q$ the top $t_i$ is immediately
followed by $e$ and $e$ is immediately followed by $t_{i+1}$.

Formalized by `Cslib.Complexity.Karp.no_shortcut`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#no-shortcut).

## A row entered at one end is run to the other end

Let $\varphi$ be a CNF formula with
$m$ clauses and $n$ distinct variables. For $k \le n$ let $t_k = m + k(3m + 2)$ be the top of
diamond $k$, and for $k < n$ let row $k$ consist of the vertices $t_k + 1 + l$ with
$0 \le l \le 3m$; its left end is $t_k + 1$ and its right end is $t_k + 1 + 3m$. Let $p$ be a
Hamiltonian path from $t_0$ to $t_n$ in Sipser's digraph for $\varphi$ on the vertices
$0, \dots, t_n$ whose clause detours are normal: every clause vertex $j < m$ occurs in $p$
immediately between the vertices $t_k + 3j + 2$ and $t_k + 3j + 3$ of some row $k < n$, in
either order. Let $q$ be $p$ with the clause vertices $0, \dots, m - 1$ deleted. Let $i < n$,
let $e$ be an end of row $i$, and for $0 \le l \le 3m$ let $r_l$ be the $l$-th vertex of row $i$
counted from $e$, that is $r_l = t_i + 1 + l$ if $e$ is the left end and $r_l = t_i + 1 + 3m - l$
if $e$ is the right end. If the top $t_i$ is immediately followed by $r_0$ in $q$, then for every
$l < 3m$ the vertex $r_l$ is immediately followed by $r_{l+1}$ in $q$.

Formalized by `Cslib.Complexity.Karp.row_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#row-run).

## Every top but the last is followed by an end of its row

Let $\varphi$ be a CNF formula
with $m$ clauses and $k$ distinct variables. In Sipser's HAMPATH graph for $\varphi$, clause $j$ is
vertex $j < m$, the top of diamond $i$ is $t_i = m + i(3m + 2)$, and vertex $l \le 3m$ of its row
is $r_{i,l} = t_i + 1 + l$. Let $p$ be a Hamiltonian path of this graph (on the vertices
$0, \dots, t_k$) from $t_0$ to $t_k$ whose detours are normal: for every $j < m$ there is $i < k$
such that $j$ sits in $p$ immediately between $r_{i,3j+1}$ and $r_{i,3j+2}$, in either order. Let
$p'$ be $p$ with the clause vertices deleted. Then for every $i < k$, the top $t_i$ is
immediately followed in $p'$ by $r_{i,0}$ or by $r_{i,3m}$.

Formalized by `Cslib.Complexity.Karp.exists_top_succ`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#exists-top-succ).

## Positions in the list of distinct variables

Let $\varphi$ be a CNF formula, let
$v_0, \dots, v_{k-1}$ be the list of distinct variables of $\varphi$, and let $i < k$. Then the
first position at which $v_i$ occurs in this list is $i$.

Formalized by `Cslib.Complexity.Karp.idxOf_getD_hamVars`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 459](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L459). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#idx-of-get-d-ham-vars).

## Backward direction of SAT ≤ HAMPATH for paths with normal detours

Let $\varphi$ be a CNF
formula with $m$ clauses and $k$ distinct variables. In Sipser's HAMPATH graph for $\varphi$, clause
$j$ is vertex $j < m$, the top of diamond $i$ is $t_i = m + i(3m + 2)$, and vertex $l \le 3m$ of
its row is $r_{i,l} = t_i + 1 + l$. If $p$ is a Hamiltonian path of this graph (on the vertices
$0, \dots, t_k$) from $t_0$ to $t_k$ whose detours are normal, that is, for every $j < m$ there is
$i < k$ such that $j$ sits in $p$ immediately between $r_{i,3j+1}$ and $r_{i,3j+2}$, in either
order, then $\varphi$ is satisfiable.

The satisfying assignment makes the variable of diamond $i$ true iff row $i$ is traversed from
left to right.

Formalized by `Cslib.Complexity.Karp.cnfSat_of_isHamPath`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathNormal.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#cnf-sat-of-is-ham-path).

## The construction has a Hamiltonian path iff the formula is satisfiable

Let
$\varphi$ be a CNF formula with $m$ clauses and $k$ distinct variables, and let
$t_i = m + i(3m + 2)$ be the top vertex of diamond $i$ in Sipser's construction. The digraph on
the vertices $0, \dots, t_k$ whose arcs are the arcs of the construction for $\varphi$ has a
Hamiltonian path from $t_0$ to $t_k$ if and only if $\varphi$ is satisfiable.

Formalized by `Cslib.Complexity.Karp.exists_isHamPath_iff_cnfSat`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCorrect.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCorrect.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#exists-is-ham-path-iff-cnf-sat).

## HAMPATH on an encoded instance

For all natural numbers $s$, $t$, $n$ and every list $E$
of pairs of natural numbers, the HAMPATH decision problem accepts the PATH encoding of
$(s, t, n, E)$ if and only if the digraph on $0, \dots, n - 1$ with edge list $E$ has a
Hamiltonian path from $s$ to $t$.

Formalized by `Cslib.Complexity.Karp.hamPathDec_encodeP`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCorrect.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCorrect.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#ham-path-dec-encode-p).

## HAMPATH rejects the fixed no-instance

The HAMPATH decision problem rejects the PATH
encoding of the digraph on the two vertices $0, 1$ with no arcs and $s = t = 0$: a path from $0$
to $0$ that visits both vertices would repeat $0$.

Formalized by `Cslib.Complexity.Karp.hamPathDec_noHam`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCorrect.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCorrect.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#ham-path-dec-no-ham).

## SAT ≤ HAMPATH preserves membership

For every bit string $x$, SAT accepts $x$ if and only
if HAMPATH accepts the image of $x$ under the SAT-to-HAMPATH reduction map.

Formalized by `Cslib.Complexity.Karp.satDec_eq_hamPathDec_reduceHam`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathCorrect.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathCorrect.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#sat-dec-eq-ham-path-dec-reduce-ham).

## Stacks of the Hamiltonian path verifier

The verifier has twelve stacks: the input $X$
and the witness $W$; the counters $S$, $T$, $N$ (holding $s$, $t$, $n$), $C$ (the number of
vertices seen), $A$ (the current vertex) and $B$ (the previous one); the save stacks $E$ (for
$X$) and $Z$ (for $W$); and the scratch stacks $R$ and $Q$.

Formalized by `Cslib.Complexity.Karp.HamVerify.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#k).

## Counter comparisons of the HAMPATH verifier

The four-element type of the comparisons the
verifier makes between its counters: the current vertex $a$ with the vertex count $n$, the
current vertex $a$ with the start vertex $s$, the number $c$ of vertices seen with $n$, and the
previous vertex $b$ with the end vertex $t$.

Formalized by `Cslib.Complexity.Karp.HamVerify.CI`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#ci).

## Labels of the Hamiltonian path verifier

The instruction labels of the verifier: reading
$s$, $t$, $n$; validating the edge list and putting it back; validating the witness and putting
it back; the vertex loop, reading a vertex, and the head-or-edge dispatch; for each of the four
counter comparisons, the comparison itself and, for each of its three outcomes, the two loops
restoring the compared counters; the edge scan (comparing an edge's ends, with a flag for the
verdict so far, restoring the counters, putting the edge list back); the repeat scan (likewise
flagged comparisons and restores, then putting the witness back); the final nonzero-count
check; counting the vertex and making it the previous one; accept; and reject.

Formalized by `Cslib.Complexity.Karp.HamVerify.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#lab).

## Statements of the Hamiltonian-path verifier

A statement of the verifier is a statement of
a multi-stack Turing machine whose stacks are indexed by the verifier's stacks $K$, each stack
over the alphabet $\mathrm{Sym}$, with labels $\mathrm{Lab}$ and a Boolean internal variable.

Formalized by `Cslib.Complexity.Karp.HamVerify.Stmt`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#stmt).

## The unary reader of the Hamiltonian path verifier

For stacks $\mathsf{src}$ and $c$ and
labels $\ell$ (its own) and $m$ (the next one), the statement that goes to label $\mathrm{no}$
if $\mathsf{src}$ is empty; otherwise it pops the top symbol of $\mathsf{src}$ and, if that
symbol is the bit `true`, pushes the bit `true` (one unit) onto $c$ and goes to $\ell$, while
if it is anything else it goes to $m$. Each of the two tests also stores its outcome in the
Boolean variable.

Run in a loop at $\ell$, it reads a unary number off $\mathsf{src}$ onto the counter $c$ and
consumes the terminator.

Formalized by `Cslib.Complexity.Karp.HamVerify.readU`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#read-u).

## The unary mover of the Hamiltonian path verifier

For stacks $\mathsf{src}$ and
$\mathsf{dst}$ and labels $\ell$ (its own) and $m$ (the next one), the statement that goes to
label $\mathrm{no}$ if $\mathsf{src}$ is empty; otherwise it pops the top symbol of
$\mathsf{src}$, reads it as the bit `true` if it is the bit `true` and as `false` otherwise,
pushes that bit onto $\mathsf{dst}$, and goes to $\ell$ if the bit is `true` and to $m$ if it
is `false`. Each of the two tests also stores its outcome in the Boolean variable.

Run in a loop at $\ell$, it moves a unary number, terminator included, from $\mathsf{src}$ to
$\mathsf{dst}$.

Formalized by `Cslib.Complexity.Karp.HamVerify.skipU`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#skip-u).

## Emptiness test

For a stack $k$ and labels $e$ and $ne$, the verifier instruction that
looks at the top of stack $k$ without changing any stack, then goes to $e$ if $k$ is empty and
to $ne$ otherwise.

Formalized by `Cslib.Complexity.Karp.HamVerify.ifE`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#if-e).

## Step of the HAMPATH verifier's unary comparison loop

For stacks $\mathit{src}$,
$\mathit{sv}$, $c$ of the HAMPATH verifier, label families $\mathit{self}$ and $\mathit{fin}$
indexed by booleans, and a boolean verdict $\mathit{ok}$, this is the instruction that pops the top
of $\mathit{src}$, reads it as a bit $b$ (false if $\mathit{src}$ is empty or its top is not a bit
symbol), and pushes the bit symbol of $b$ onto $\mathit{sv}$. If $b$ is true, it pops $c$; if $c$
was nonempty it pushes the bit symbol of true onto the scratch stack $R$ and goes to
$\mathit{self}(\mathit{ok})$, and otherwise it goes to $\mathit{self}(\mathrm{false})$. If $b$ is
false, it goes to $\mathit{fin}(\mathit{ok})$ when $c$ is empty and to
$\mathit{fin}(\mathrm{false})$ otherwise.

Iterated, it compares the next unary number of $\mathit{src}$ with the counter $c$, one unit of $c$
per true, parked on $R$: $\mathit{ok}$ is the verdict so far, falsified when $c$ runs out early.

Formalized by `Cslib.Complexity.Karp.HamVerify.cbS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#cb-s).

## First counter of a HAMPATH-verifier comparison

The function from the four counter
comparisons of the HAMPATH verifier to its stacks that sends the comparisons of the current
vertex with the vertex count and of the current vertex with the start vertex to the
current-vertex counter $A$, the comparison of the number of vertices seen with the vertex count
to the vertices-seen counter $C$, and the comparison of the previous vertex with the end vertex
to the previous-vertex counter $B$.

Formalized by `Cslib.Complexity.Karp.HamVerify.ca`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#ca).

## Second counter of a HAMPATH-verifier comparison

The function from the four counter
comparisons of the HAMPATH verifier to its stacks that sends the comparisons of the current
vertex with the vertex count and of the number of vertices seen with the vertex count to the
vertex-count counter $N$, the comparison of the current vertex with the start vertex to the
start-vertex counter $S$, and the comparison of the previous vertex with the end vertex to the
end-vertex counter $T$.

Formalized by `Cslib.Complexity.Karp.HamVerify.cb`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-09/index.html#cb).

## Exit labels of the counter comparisons

The label the verifier goes to after comparing
two counters, where $a$ is the current vertex, $b$ the previous one, $c$ the number of vertices
seen, $n$ the number of vertices and $s$, $t$ the two ends: after comparing $a$ with $n$ it goes
to the head-or-edge dispatch if $a < n$; after comparing $a$ with $s$ it goes to the repeat scan
if $a = s$; after comparing $c$ with $n$ it goes to the nonzero-count check if $c = n$; after
comparing $b$ with $t$ it goes to the accept label if $b = t$; in every other case it goes to
the reject label.

Formalized by `Cslib.Complexity.Karp.HamVerify.cout`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#cout).

## The Hamiltonian path verifier machine

The verifier is the program of the multi-stack
machine with the stacks and labels of the Hamiltonian path verifier, every stack over the
alphabet $\mathrm{Sym}$, and a Boolean internal variable, given below label by label. Write
$\mathrm{bit}(x)$ for the bit symbol of a boolean $x$. Write $(a, n)$, $(a, s)$, $(c, n)$ and
$(b, t)$ for the four counter comparisons, and $\alpha(i)$ and $\beta(i)$ for the first and the
second counter of comparison $i$. Every unary reader, unary mover, bit-moving loop and transfer
below has the label it sits at as its own label; the bit-moving loops read bit symbols as bits
and every other symbol as a marker, and push $\mathrm{bit}(x)$ for a bit $x$. The transfer from a
stack $k$ onto a list of stacks with next label $m$ pops $k$; if it popped a symbol, it pushes
$\mathrm{bit}(\mathrm{true})$ onto each listed stack and returns to its own label, and otherwise
it goes to $m$. An emptiness test of a stack "to $e$, else $e'$" goes to $e$ if the stack is
empty and to $e'$ otherwise. A transfer also stores in the Boolean variable whether its pop
found a symbol, and an emptiness test stores there whether the stack is empty.

- $\mathsf{rdS}$, $\mathsf{rdT}$, $\mathsf{rdN}$: the unary reader from $X$ onto $S$, $T$, $N$
  respectively, with next labels $\mathsf{rdT}$, $\mathsf{rdN}$, $\mathsf{vE}$ respectively.
- $\mathsf{vE}$: the emptiness test of $X$ to $\mathsf{vEb}$, else $\mathsf{vEU}$. $\mathsf{vEU}$
  and $\mathsf{vEV}$: the unary mover from $X$ to $E$, with next labels $\mathsf{vEV}$ and
  $\mathsf{vE}$ respectively. $\mathsf{vEb}$: the bit-moving loop from $E$ to $X$ with next label
  $\mathsf{vW}$.
- $\mathsf{vW}$: the emptiness test of $W$ to $\mathsf{vWb}$, else $\mathsf{vWU}$. $\mathsf{vWU}$:
  the unary mover from $W$ to $Z$ with next label $\mathsf{vW}$. $\mathsf{vWb}$: the bit-moving
  loop from $Z$ to $W$ with next label $\mathsf{loop}$.
- $\mathsf{loop}$: the emptiness test of $W$ to $\mathsf{cmp}(c, n)$, else $\mathsf{rdA}$.
  $\mathsf{rdA}$: the unary reader from $W$ onto $A$ with next label $\mathsf{cmp}(a, n)$.
  $\mathsf{hd}$: the emptiness test of $C$ to $\mathsf{cmp}(a, s)$, else $\mathsf{scan}$.
- For each comparison $i$, $\mathsf{cmp}(i)$ is one round of counter comparison of $\alpha(i)$
  and $\beta(i)$, with scratch stacks $R$ (for $\alpha(i)$) and $Q$ (for $\beta(i)$), both units
  $\mathrm{bit}(\mathrm{true})$, own label $\mathsf{cmp}(i)$, and $\mathsf{cr}(i, <)$,
  $\mathsf{cr}(i, =)$, $\mathsf{cr}(i, >)$ as its labels $\mathit{lt}$, $\mathit{eq}$ and
  $\mathit{gt}$. For each ordering $o$, $\mathsf{cr}(i, o)$ is the transfer from $R$ onto
  $\alpha(i)$ with next label $\mathsf{crb}(i, o)$, and $\mathsf{crb}(i, o)$ is the transfer from
  $Q$ onto $\beta(i)$ whose next label is the exit label of the counter comparison $i$ with
  outcome $o$.
- $\mathsf{scan}$: the emptiness test of $X$ to $\mathsf{no}$, else
  $\mathsf{ceU}(\mathrm{true})$. For each boolean $\mathit{ok}$: $\mathsf{ceU}(\mathit{ok})$ is
  the step of the unary comparison loop with source $X$, save stack $E$, counter $B$, label
  families $\mathsf{ceU}$ and $\mathsf{rsU}$, and verdict $\mathit{ok}$; $\mathsf{rsU}(\mathit{ok})$
  is the transfer from $R$ onto $B$ with next label $\mathsf{ceV}(\mathit{ok})$;
  $\mathsf{ceV}(\mathit{ok})$ is the step of the unary comparison loop with source $X$, save stack
  $E$, counter $A$, label families $\mathsf{ceV}$ and $\mathsf{rsV}$, and verdict $\mathit{ok}$;
  and $\mathsf{rsV}(\mathit{ok})$ is the transfer from $R$ onto $A$ with next label $\mathsf{scB}$
  if $\mathit{ok}$ is true and $\mathsf{scan}$ otherwise. $\mathsf{scB}$: the bit-moving loop from
  $E$ to $X$ with next label $\mathsf{nd}$.
- $\mathsf{nd}$: the emptiness test of $W$ to $\mathsf{ndB}$, else $\mathsf{cbN}(\mathrm{true})$.
  For each boolean $\mathit{ok}$: $\mathsf{cbN}(\mathit{ok})$ is the step of the unary comparison
  loop with source $W$, save stack $Z$, counter $A$, label families $\mathsf{cbN}$ and
  $\mathsf{rsN}$, and verdict $\mathit{ok}$; and $\mathsf{rsN}(\mathit{ok})$ is the transfer from
  $R$ onto $A$ with next label $\mathsf{no}$ if $\mathit{ok}$ is true and $\mathsf{nd}$
  otherwise. $\mathsf{ndB}$: the bit-moving loop from $Z$ to $W$ with next label $\mathsf{incC}$.
- $\mathsf{fin}$: the emptiness test of $C$ to $\mathsf{no}$, else $\mathsf{cmp}(b, t)$.
  $\mathsf{incC}$: the counter increment pushing $\mathrm{bit}(\mathrm{true})$ onto $C$ and going
  to $\mathsf{dB}$. $\mathsf{dB}$: the transfer from $B$ onto no stack (it drains $B$) with next
  label $\mathsf{mA}$. $\mathsf{mA}$: the transfer from $A$ onto $B$ with next label
  $\mathsf{loop}$.
- $\mathsf{yes}$ and $\mathsf{no}$: halt.

The verifier parses and validates the input and the witness, then walks the vertices.

Formalized by `Cslib.Complexity.Karp.HamVerify.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#prog).

## Start label of the Hamiltonian-path verifier

The verifier starts at the label
$\mathsf{rdS}$, where it reads the first unary number of the input stack $X$ (the start vertex
$s$) onto the counter stack $S$.

Formalized by `Cslib.Complexity.Karp.HamVerify.start`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#start).

## Interleaved stack updates in the Hamiltonian-path verifier

Let $a \ne b$ be two stacks of
the verifier, $S$ an assignment of a list of symbols to each stack, and $p, p', t, t'$ lists of
symbols. Setting $a$ to $p$, then $b$ to $t$, then $a$ to $p'$, then $b$ to $t'$ in $S$ gives the
same assignment as setting $a$ to $p'$ and then $b$ to $t'$.

Formalized by `Cslib.Complexity.Karp.HamVerify.update_update_update_update`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#update-update-update-update).

## A single step of the Hamiltonian-path verifier

Let $l, l'$ be labels, $v$ a flag value
and $S, S'$ assignments of a list of symbols to each stack. If executing the verifier's statement
at $l$ with flag $v$ and stacks $S$ jumps to the label $l'$ and leaves the stacks $S'$, then the
verifier goes in exactly one step from label $l$, flag $v$ and stacks $S$ to label $l'$ and
stacks $S'$, with some flag value.

Formalized by `Cslib.Complexity.Karp.HamVerify.step1`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#step1).

## One step of the emptiness test

If the verifier's instruction at label $l$ is the
emptiness test of stack $k$ with targets $e$ and $ne$, then from label $l$, in any internal state
and on any stacks, exactly one step of the verifier leads to label $e$ if stack $k$ is empty and
to label $ne$ otherwise, in some internal state and with the stacks unchanged.

Formalized by `Cslib.Complexity.Karp.HamVerify.ifE_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#if-e-run).

## The unary reader of the Hamiltonian path verifier reads a terminated number

Let
$\mathsf{src} \ne c$ be stacks and $\ell$, $m$ labels such that the verifier's statement at
$\ell$ is the unary reader from $\mathsf{src}$ onto $c$ with own label $\ell$ and next label
$m$. Let $k, j$ be natural numbers and $r$ a bit list, and suppose that $\mathsf{src}$ holds
$k$ copies of `true`, then `false`, then $r$ (as bit symbols, first bit on top) and that $c$
holds $j$ copies of the bit `true`. Then from label $\ell$, with either value of the Boolean
variable, the verifier reaches label $m$ in exactly $k + 1$ steps, with $\mathsf{src}$ holding
the bits of $r$, $c$ holding $k + j$ copies of the bit `true`, and every other stack
unchanged.

Formalized by `Cslib.Complexity.Karp.HamVerify.readU_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#read-u-run).

## The unary reader of the Hamiltonian path verifier rejects an unterminated number

Let
$\mathsf{src} \ne c$ be stacks and $\ell$, $m$ labels such that the verifier's statement at
$\ell$ is the unary reader from $\mathsf{src}$ onto $c$ with own label $\ell$ and next label
$m$. Let $l$ be a bit list from which no unary length can be read (that is, $l$ contains no
`false`), and suppose that $\mathsf{src}$ holds the bits of $l$ (as bit symbols, first bit on
top). Then from label $\ell$, with either value of the Boolean variable and any contents of the
other stacks, the verifier reaches label $\mathrm{no}$ within $|l| + 1$ steps.

Formalized by `Cslib.Complexity.Karp.HamVerify.readU_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#read-u-none).

## Extending a reversed unary block

For $a \in \mathbb{N}$, let $\beta_a$ be the list of
symbols obtained by mapping the bit symbol over the reversal of the unary block of $a$ ($a$ copies
of true followed by one false), that is, the bit symbol of false followed by $a$ bit symbols of
true. Then for every list $L$ of symbols, $\beta_a$ followed by the bit symbol of true and then
$L$ equals $\beta_{a+1}$ followed by $L$.

Formalized by `Cslib.Complexity.Karp.HamVerify.blk_succ`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#blk-succ).

## The unary mover of the Hamiltonian path verifier moves a terminated number

Let
$\mathsf{src} \ne \mathsf{dst}$ be stacks and $\ell$, $m$ labels such that the verifier's
statement at $\ell$ is the unary mover from $\mathsf{src}$ to $\mathsf{dst}$ with own label
$\ell$ and next label $m$. Let $k$ be a natural number and $r$ a bit list, and suppose that
$\mathsf{src}$ holds $k$ copies of `true`, then `false`, then $r$ (as bit symbols, first bit on
top). Then from label $\ell$, with either value of the Boolean variable, the verifier reaches
label $m$ in exactly $k + 1$ steps, with $\mathsf{src}$ holding the bits of $r$, with
$\mathsf{dst}$ holding the bit `false` followed by $k$ copies of the bit `true` on top of its
previous contents, and with every other stack unchanged.

Formalized by `Cslib.Complexity.Karp.HamVerify.skipU_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#skip-u-run).

## The unary mover of the Hamiltonian path verifier rejects an unterminated number

Let
$\mathsf{src} \ne \mathsf{dst}$ be stacks and $\ell$, $m$ labels such that the verifier's
statement at $\ell$ is the unary mover from $\mathsf{src}$ to $\mathsf{dst}$ with own label
$\ell$ and next label $m$. Let $l$ be a bit list from which no unary length can be read (that
is, $l$ contains no `false`), and suppose that $\mathsf{src}$ holds the bits of $l$ (as bit
symbols, first bit on top). Then from label $\ell$, with either value of the Boolean variable
and any contents of the other stacks, the verifier reaches label $\mathrm{no}$ within
$|l| + 1$ steps.

Formalized by `Cslib.Complexity.Karp.HamVerify.skipU_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#skip-u-none).

## Moving a stack of bits

Suppose the verifier's instruction at label $p$ is the bit-moving
loop from a stack $a$ to a different stack $b$, continuing at label $p'$ when done. If stack $a$
holds exactly the bits of a list $l$, then from label $p$ in any internal state the verifier
takes exactly $|l| + 1$ steps to reach label $p'$, in some internal state, with stack $a$ empty,
stack $b$ holding the bits of $l$ in reverse order followed by its old contents, and every other
stack unchanged.

Formalized by `Cslib.Complexity.Karp.HamVerify.mv_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#mv-run).

## Run of a HAMPATH-verifier counter comparison

Let $i$ be one of the four counter
comparisons of the HAMPATH verifier, with first counter $\mathrm{ca}(i)$ and second counter
$\mathrm{cb}(i)$, and let $m, n \in \mathbb{N}$. Suppose the stacks $\sigma$ hold $m$ units (bit
symbols of true) on $\mathrm{ca}(i)$, $n$ units on $\mathrm{cb}(i)$, and nothing on the scratch
stacks $R$ and $Q$. Then for every flag $v$ the verifier goes, in at most
$3 \min(m, n) + 4$ steps, from label $\mathrm{cmp}(i)$ with flag $v$ and stacks $\sigma$ to the
label $\mathrm{cout}(i, o)$ that comparison $i$ picks on the ordering
$o = \mathrm{compare}(m, n) \in \{\mathrm{lt}, \mathrm{eq}, \mathrm{gt}\}$ of $m$ and $n$, with flag
false and the same stacks $\sigma$.

Formalized by `Cslib.Complexity.Karp.HamVerify.cmpI_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#cmp-i-run).

## Outcome of the HAMPATH verifier's vertex-range comparison

For all $m, n \in \mathbb{N}$,
the label that the comparison of the current vertex with the vertex count picks on the ordering
$\mathrm{compare}(m, n)$ of $m$ and $n$ is the head-or-edge dispatch label $\mathrm{hd}$ if
$m < n$, and the reject label $\mathrm{no}$ otherwise.

Formalized by `Cslib.Complexity.Karp.HamVerify.cout_an`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#cout-an).

## Outcome of a HAMPATH-verifier equality comparison

Write $\mathrm{cout}(i, o)$ for the
label that counter comparison $i$ of the HAMPATH verifier picks on the ordering
$o \in \{\mathrm{lt}, \mathrm{eq}, \mathrm{gt}\}$. Let $i$ be a counter comparison and $l$ a label
such that $\mathrm{cout}(i, \mathrm{eq}) = l$ and $\mathrm{cout}(i, o)$ is the reject label
$\mathrm{no}$ for every ordering $o \ne \mathrm{eq}$. Then for all $m, n \in \mathbb{N}$, the label
$\mathrm{cout}(i, \mathrm{compare}(m, n))$ on the ordering of $m$ and $n$ is $l$ if $m = n$ and
$\mathrm{no}$ otherwise.

Formalized by `Cslib.Complexity.Karp.HamVerify.cout_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#cout-eq).

## Run of the HAMPATH verifier's unary comparison loop

Let $\mathit{src}$, $\mathit{sv}$, $c$
and the scratch stack $R$ be four distinct stacks of the HAMPATH verifier, and let $\mathrm{cb}$ and
$\mathrm{fin}$ be families of labels indexed by booleans such that for every boolean $\mathit{ok}$
the instruction at $\mathrm{cb}(\mathit{ok})$ is the unary comparison step on $\mathit{src}$,
$\mathit{sv}$, $c$ with loop labels $\mathrm{cb}$, exit labels $\mathrm{fin}$ and verdict
$\mathit{ok}$. Write $1$ and $0$ for the bit symbols of true and false, $1^k$ for $k$ copies of
$1$, and $\bar r$ for the list of bit symbols of a list of booleans $r$; stacks are listed from the
top. Then for all $a, u, j \in \mathbb{N}$, every boolean $\mathit{ok}$, every list of booleans
$r$, every flag $v$ and all stack contents $\sigma$ with $\sigma(\mathit{src}) = 1^a\,0\,\bar r$,
$\sigma(c) = 1^u$ and $\sigma(R) = 1^j$, the verifier runs in exactly $a + 1$ steps from label
$\mathrm{cb}(\mathit{ok})$ with flag $v$ and stacks $\sigma$ to label $\mathrm{fin}(b)$, where $b$
is true exactly when $\mathit{ok}$ is true and $a = u$, with some flag and some stacks $\sigma'$
such that $\sigma'(\mathit{src}) = \bar r$, $\sigma'(\mathit{sv}) = 0\,1^a\,\sigma(\mathit{sv})$,
$\sigma'(c) = 1^{\max(u - a, 0)}$, $\sigma'(R) = 1^{\min(a, u) + j}$, and $\sigma'(k) = \sigma(k)$
for every other stack $k$.

Formalized by `Cslib.Complexity.Karp.HamVerify.cb_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#cb-run).

## HAMPATH-verifier unary comparison with the counter restored

Let $\mathit{src}$,
$\mathit{sv}$, $c$ and the scratch stack $R$ be four distinct stacks of the HAMPATH verifier, and
let $\mathrm{cb}$, $\mathrm{rs}$ and $\mathrm{nx}$ be families of labels indexed by booleans such
that for every boolean $\mathit{ok}$ the instruction at $\mathrm{cb}(\mathit{ok})$ is the unary
comparison step on $\mathit{src}$, $\mathit{sv}$, $c$ with loop labels $\mathrm{cb}$, exit labels
$\mathrm{rs}$ and verdict $\mathit{ok}$, and the instruction at $\mathrm{rs}(\mathit{ok})$ is the
transfer loop that pops $R$ until it is empty, pushing one unit (the bit symbol of true) on $c$
per symbol popped, and then goes to $\mathrm{nx}(\mathit{ok})$. Write $1$ and $0$ for the bit
symbols of true and false, $1^k$ for $k$ copies of $1$, and $\bar r$ for the list of bit symbols
of a list of booleans $r$; stacks are listed from the top. Let $a, u \in \mathbb{N}$, let
$\mathit{ok}$ be a boolean, $r$ a list of booleans, $v$ a flag, and $\sigma$ stack contents with
$\sigma(\mathit{src}) = 1^a\,0\,\bar r$, $\sigma(c) = 1^u$ and $\sigma(R)$ empty. Then the verifier
runs in exactly $(a + 1) + (\min(a, u) + 1)$ steps from label $\mathrm{cb}(\mathit{ok})$ with flag
$v$ and stacks $\sigma$ to label $\mathrm{nx}(b)$, where $b$ is true exactly when $\mathit{ok}$ is
true and $a = u$, with some flag and with the stacks of $\sigma$ except that $\mathit{src}$ now
holds $\bar r$ and $\mathit{sv}$ holds $0\,1^a$ followed by $\sigma(\mathit{sv})$.

Formalized by `Cslib.Complexity.Karp.HamVerify.cmpN_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#cmp-n-run).

## The edge-list check of the Hamiltonian-path verifier

Let $r$ and $acc$ be bit lists, and
let the stacks $St$ hold $r$ on the input stack $X$ and the reverse of $acc$ on the save stack
$E$. Started at the label $\mathsf{vE}$ with any flag value, the verifier reaches within at most
$2|r| + 1$ steps the label $\mathsf{vEb}$ if $r$ decodes as an edge list (a sequence of pairs of
unary numbers, each a block of ones ended by a zero) and the label $\mathsf{no}$ otherwise. When
$r$ decodes, the final stacks are $St$ with $X$ emptied and $E$ holding the reverse of the
concatenation of $acc$ and $r$ (that is, $r$ reversed on top of $acc$ reversed), all other
stacks unchanged.

Formalized by `Cslib.Complexity.Karp.HamVerify.valE_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#val-e-run).

## The witness check of the Hamiltonian-path verifier

Let $w$ and $acc$ be bit lists, and
let the stacks $St$ hold $w$ on the witness stack $W$ and the reverse of $acc$ on the save stack
$Z$. Started at the label $\mathsf{vW}$ with any flag value, the verifier reaches within at most
$2|w| + 1$ steps the label $\mathsf{vWb}$ if $w$ decodes as a vertex list (a sequence of unary
numbers, each a block of ones ended by a zero) and the label $\mathsf{no}$ otherwise. When $w$
decodes, the final stacks are $St$ with $W$ emptied and $Z$ holding the reverse of the
concatenation of $acc$ and $w$ (that is, $w$ reversed on top of $acc$ reversed), all other
stacks unchanged.

Formalized by `Cslib.Complexity.Karp.HamVerify.valW_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 535](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L535). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#val-w-run).

## The edge scan of the Hamiltonian path verifier

For a list $e$ of pairs of natural
numbers write $\mathrm{bits}(e)$ for its edge-list encoding, in which each pair $(u, u')$
contributes $u$ copies of `true`, then `false`, then $u'$ copies of `true`, then `false`. Let
$a, b$ be natural numbers and $r$, $d$ lists of pairs of natural numbers. Suppose that the
verifier's stacks hold, as bit symbols with the first bit on top, $\mathrm{bits}(r)$ on
$\mathsf{X}$, $\mathrm{bits}(d)$ in reverse order on $\mathsf{E}$, $a$ copies of the bit `true`
on $\mathsf{A}$, $b$ copies of the bit `true` on $\mathsf{B}$, and nothing on $\mathsf{R}$, the
other stacks being arbitrary. Started at label $\mathrm{scan}$ with either value of its Boolean
variable, the verifier reaches, within $4|\mathrm{bits}(r)| + |\mathrm{bits}(d)| + 2$ steps, the
label $\mathrm{nd}$ if $(b, a)$ is one of the pairs of $r$ and the label $\mathrm{no}$
otherwise. In the first case its stacks are then the initial ones except that $\mathsf{X}$
holds the encoding $\mathrm{bits}$ of the list $d$ followed by $r$, and $\mathsf{E}$ is empty.

Formalized by `Cslib.Complexity.Karp.HamVerify.scan_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 580](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L580). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-10/index.html#scan-run).

## The repeat scan of the Hamiltonian path verifier

For a list $p$ of natural numbers
write $\mathrm{enc}(p)$ for its witness encoding: each entry in unary (that many copies of
`true`) followed by `false`. Let $a$ be a natural number and $q$, $d$ lists of natural numbers.
Suppose that the verifier's stacks hold, as bit symbols with the first bit on top, the bits of
$\mathrm{enc}(q)$ on $\mathsf{W}$, the bits of $\mathrm{enc}(d)$ in reverse order on
$\mathsf{Z}$, $a$ copies of the bit `true` on $\mathsf{A}$, and nothing on $\mathsf{R}$, the
other stacks being arbitrary. Started at label $\mathrm{nd}$ with either value of its Boolean
variable, the verifier reaches, within $4|\mathrm{enc}(q)| + |\mathrm{enc}(d)| + 2$ steps, the
label $\mathrm{no}$ if $a$ is an entry of $q$ and the label $\mathrm{incC}$ otherwise. In the
second case its stacks are then the initial ones except that $\mathsf{W}$ holds the bits of the
encoding of $d$ followed by $q$, and $\mathsf{Z}$ is empty.

Formalized by `Cslib.Complexity.Karp.HamVerify.nd_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#nd-run).

## Stack layout between vertex steps

For an edge list $es$, numbers $s, t, n, c, b$ and a
list $q$ of vertices, the stacks of the verifier between two vertex steps: $X$ holds the bits of
the edge list $es$, $W$ holds the bits of the witness encoding of $q$, the counters $S$, $T$,
$N$, $C$ and $B$ hold $s$, $t$, $n$, $c$ and $b$ in unary, and the stacks $A$, $E$, $Z$, $R$
and $Q$ are empty.

Formalized by `Cslib.Complexity.Karp.HamVerify.lay`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 703](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L703). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#lay).

## Stack layout during a vertex step

For an edge list $es$, numbers $s, t, n, c, b, a$ and
a list $q$ of vertices, the stacks of the verifier during the step on vertex $a$: the layout
between vertex steps for $es, s, t, n, c, b, q$, except that stack $A$ holds $a$ in unary.

Formalized by `Cslib.Complexity.Karp.HamVerify.mid`, a definition declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 718](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L718). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#mid).

## Running the head-or-edge check

Let $es$ be an edge list, $s, t, n, c, b, a$ numbers and
$q$ a list of vertices, and say the check passes when $a = s$ in case $c = 0$, and
$(b, a) \in es$ in case $c \neq 0$. Started at the head-or-edge dispatch, in any internal state,
on the stack layout during the step on vertex $a$ for $es, s, t, n, c, b, a, q$, the verifier
reaches within $3a + 4\ell + 7$ steps, where $\ell$ is the number of bits of $es$, the repeat
scan if the check passes and the reject label otherwise, in some internal state and with some
stacks; if the check passes, these stacks are the ones it started on.

Formalized by `Cslib.Complexity.Karp.HamVerify.hd_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 723](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L723). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#hd-run).

## The rest of a vertex step in the Hamiltonian-path verifier

Let $es$ be an edge list,
$s, t, n, c, b, a$ natural numbers and $q$ a list of natural numbers. Start the verifier, with
any flag value, at the label $\mathsf{nd}$ (the repeat scan) with its stacks in the mid-step
layout: the between-steps layout for $es$, $s$, $t$, $n$, count $c$, previous vertex $b$ and
remaining vertices $q$, with $a$ in unary on the stack $A$. Let $w$ be the unary encoding of $q$.
Then within at most $4|w| + a + b + 6$ steps it reaches the label $\mathsf{no}$ if $a \in q$ and
the label $\mathsf{loop}$ if $a \notin q$. In the second case ($a$ has been counted and become
the previous vertex) the stacks end in the between-steps layout for $es$, $s$, $t$, $n$, count
$c + 1$, previous vertex $a$ and remaining vertices $q$.

Formalized by `Cslib.Complexity.Karp.HamVerify.tail_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 752](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L752). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#tail-run).

## One vertex step of the Hamiltonian-path verifier

Let $es$ be an edge list,
$s, t, n, c, b, a$ natural numbers and $q$ a list of natural numbers. Start the verifier, with
any flag value, at the label $\mathsf{rdA}$ (read the next vertex) with its stacks in the
between-steps layout for $es$, $s$, $t$, $n$, count $c$, previous vertex $b$ and remaining
vertices $a, q$. Let $e$ be the bit encoding of $es$ and $w$ the unary encoding of $q$. Then
within at most $8a + b + 4|e| + 4|w| + 20$ steps it reaches the label $\mathsf{loop}$ if the
step check on $a$ passes and the label $\mathsf{no}$ otherwise. The step check passes when
$a < n$, $a = s$ in case $c = 0$ and $(b, a) \in es$ in case $c \ne 0$, and $a \notin q$. When
it passes, the stacks end in the between-steps layout for $es$, $s$, $t$, $n$, count $c + 1$,
previous vertex $a$ and remaining vertices $q$.

Formalized by `Cslib.Complexity.Karp.HamVerify.step_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 783](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L783). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#step-run).

## Running the vertex loop

Let $es$ be an edge list, $s, t, n$ numbers and $L$ a bound
with $n \le L$, $t \le L$ and at most $L$ bits in the encoding of $es$. For every list $q$ of
vertices whose witness encoding has at most $L$ bits, every count $c$, every previous vertex
$b \le L$ and every internal state, the verifier started at the vertex loop on the stack layout
between vertex steps for $es, s, t, n, c, b, q$ reaches within $(|q| + 1)(20L + 20)$ steps, with
some internal state and stacks, the accept label if the walk check for $s, t, n, es, c, b, q$
passes and the reject label otherwise.

Formalized by `Cslib.Complexity.Karp.HamVerify.loop_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 829](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L829). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#loop-run).

## Correctness and running time of the Hamiltonian path verifier

Let $x$ and $w$ be bit
lists. Start the verifier at its start label, with either value of its Boolean variable, with
$x$ on stack $\mathsf{X}$ and $w$ on stack $\mathsf{W}$ (as bit symbols, first bit on top) and
all other stacks empty. Then within $100(|x| + |w| + 1)^4$ steps it reaches the label
$\mathrm{yes}$ if the Hamiltonian path check accepts $x$ and $w$, and the label $\mathrm{no}$
otherwise.

The machine in fact takes quadratically many steps; the theorem states only the quartic bound.

Formalized by `Cslib.Complexity.Karp.HamVerify.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean, line 890](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathVerify.lean#L890). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#run).

## The HAMPATH verifier as a host component

The component machine whose program and labels
are those of the HAMPATH verifier machine, whose stacks are the twelve stacks of that machine (the
input $X$, the witness $W$, the counters $S, T, N, C, A, B$, the save stacks $E, Z$ and the scratch
stacks $R, Q$), each over the symbol alphabet of the SAT verifier.

Formalized by `Cslib.Complexity.Karp.hamVerifyComp`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/HamPathComplete.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathComplete.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#ham-verify-comp).

## HAMPATH is in NP

**HAMPATH is in NP**.

Formalized by `Cslib.Complexity.Karp.hamPathDec_mem_NP`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathComplete.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathComplete.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#ham-path-dec-mem-np).

## The HAMPATH emitter

The emitter whose stacks, alphabets, labels, program and start label
are those of the HAMPATH emitter machine, which exits at the machine's label $\mathsf{done}$,
reads the tokens of a CNF formula from stack $T$ and writes its output bits on stack $O$ (both
symbol maps being the identity), and has step bound $B(n) = 2000 (n + 1)^5$ for $n$ tokens. Its
output for a CNF formula $\varphi$ is Sipser's HAMPATH instance of $\varphi$, and for an
undecodable input the fixed HAMPATH no-instance (two vertices, no arcs, source and target $0$).

Formalized by `Cslib.Complexity.Karp.emitHam`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/HamPathComplete.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathComplete.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#emit-ham).

## SAT ≤ HAMPATH is polynomial-time

The map on bit strings that sends a bit string decoding
to a CNF formula $\varphi$ to Sipser's HAMPATH instance for $\varphi$, and every other bit string
to the fixed no-instance with two vertices, no arcs and $s = t = 0$, is computable in polynomial
time.

Formalized by `Cslib.Complexity.Karp.isPolyTime_reduceHam`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathComplete.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathComplete.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#is-poly-time-reduce-ham).

## HAMPATH is NP-hard

Every decision problem $L$ in NP has a polynomial-time many-one
reduction to HAMPATH: a polynomial-time computable map $f$ on bit strings such that, for every
bit string $x$, $L$ accepts $x$ exactly when HAMPATH accepts $f(x)$.

Formalized by `Cslib.Complexity.Karp.hamPathDec_npHard`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathComplete.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathComplete.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#ham-path-dec-np-hard).

## HAMPATH is NP-complete

HAMPATH lies in NP, and every decision problem $L$ in NP has a
polynomial-time many-one reduction to HAMPATH: a polynomial-time computable map $f$ on bit
strings such that, for every bit string $x$, $L$ accepts $x$ exactly when HAMPATH accepts $f(x)$.

## Sources

- Sipser, Theorem 7.46.

Formalized by `Cslib.Complexity.Karp.hamPathDec_npComplete`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/HamPathComplete.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/HamPathComplete.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/part-11/index.html#ham-path-dec-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hamiltonian path in directed graphs](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/hamiltonian-path-in-directed-graphs)
