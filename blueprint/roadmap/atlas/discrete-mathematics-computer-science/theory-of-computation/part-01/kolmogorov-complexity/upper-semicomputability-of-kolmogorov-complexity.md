---
declaration: section
origin: cited
lean: Cslib.Kolmogorov.rePred_mem_U, Cslib.Kolmogorov.rePred_K_le, Cslib.Kolmogorov.exists_K_map_le, Cslib.Kolmogorov.exists_shortest_incompressible, Cslib.Kolmogorov.exists_bound_of_rePred_le_K, Cslib.Kolmogorov.exists_bound_of_computable_le_K, Cslib.Kolmogorov.not_rePred_le_K, Cslib.Kolmogorov.not_rePred_of_forall_incompressible
statement: formalized
proof: formalized
---

# Upper semicomputability of Kolmogorov complexity, and incompressible strings

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity/index.html).

## The description relation is recognizable

Let $U$ be the universal description method.
The set of pairs $(x, p)$ of binary strings such that $U(p)$ is defined and equal to $x$ is
recursively enumerable (recognizable).

Formalized by `Cslib.Kolmogorov.rePred_mem_U`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Semicomputable.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Kolmogorov/Semicomputable.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity/index.html#re-pred-mem-u).

## Kolmogorov complexity is upper semicomputable

Let $K$ denote Kolmogorov complexity. The
set of pairs $(x, n)$ of a binary string $x$ and a natural number $n$ with $K(x) \le n$ is
recursively enumerable (recognizable).

Formalized by `Cslib.Kolmogorov.rePred_K_le`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Semicomputable.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Kolmogorov/Semicomputable.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity/index.html#re-pred-k-le).

## A partial recursive map raises complexity by at most a constant

Let $K$ denote Kolmogorov
complexity and let $f$ be a partial recursive function from binary strings to binary strings.
Then there is a natural number $c$ such that $K(y) \le K(x) + c$ for all binary strings $x$ and
$y$ such that $f(x)$ is defined and equal to $y$.

Formalized by `Cslib.Kolmogorov.exists_K_map_le`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Semicomputable.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Kolmogorov/Semicomputable.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity/index.html#exists-k-map-le).

## Shortest descriptions are incompressible

Let $U$ be the universal description method,
$K$ Kolmogorov complexity, and $|p|$ the length of a binary string $p$. There is a natural number
$b$ such that for all binary strings $x$ and $p$, if $p$ is a shortest description of $x$, that
is, $U(p)$ is defined and equal to $x$ and $|p| = K(x)$, then $|p| \le K(p) + b$.

Formalized by `Cslib.Kolmogorov.exists_shortest_incompressible`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Semicomputable.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Kolmogorov/Semicomputable.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity/index.html#exists-shortest-incompressible).

## Chaitin's incompleteness theorem

Let $K$ denote Kolmogorov complexity, and let $S$ be a
recursively enumerable (recognizable) set of pairs $(x, n)$ of a binary string $x$ and a natural
number $n$ such that $n \le K(x)$ for every $(x, n) \in S$. Then there is a natural number $B$
with $n \le B$ for every $(x, n) \in S$.

This is the abstract form of the theorem: think of $S$ as the statements $K(x) \ge n$ that a sound
formal system proves. The proof searches $S$ for a pair with a large bound $n$ and applies
optimality of the universal description method (Berry's paradox).

Formalized by `Cslib.Kolmogorov.exists_bound_of_rePred_le_K`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Semicomputable.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Kolmogorov/Semicomputable.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity/index.html#exists-bound-of-re-pred-le-k).

## A computable lower bound of Kolmogorov complexity is bounded

Let $K$ denote Kolmogorov
complexity. If $f$ is a computable function from binary strings to natural numbers with
$f(x) \le K(x)$ for every binary string $x$, then there is a natural number $B$ with $f(x) \le B$
for every binary string $x$.

Formalized by `Cslib.Kolmogorov.exists_bound_of_computable_le_K`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Semicomputable.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Kolmogorov/Semicomputable.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity/index.html#exists-bound-of-computable-le-k).

## Kolmogorov complexity is not lower semicomputable

Let $K$ denote Kolmogorov complexity.
The set of pairs $(x, n)$ of a binary string $x$ and a natural number $n$ with $n \le K(x)$ is not
recursively enumerable (recognizable).

Formalized by `Cslib.Kolmogorov.not_rePred_le_K`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Semicomputable.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Kolmogorov/Semicomputable.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity/index.html#not-re-pred-le-k).

## No recognizable set with arbitrarily long members consists of incompressible strings

Let $K$ denote Kolmogorov complexity and $|x|$ the length of a binary string $x$. There is no
recursively enumerable (recognizable) set $S$ of binary strings such that for every natural
number $n$ some $x \in S$ has $|x| \ge n$, and every $x \in S$ satisfies $|x| \le K(x)$.

Formalized by `Cslib.Kolmogorov.not_rePred_of_forall_incompressible`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Semicomputable.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Kolmogorov/Semicomputable.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity/index.html#not-re-pred-of-forall-incompressible).

## The incompressible strings are not recognizable

Let $K$ denote Kolmogorov complexity
and $|x|$ the length of a binary string $x$. The set of incompressible binary strings, that is,
of binary strings $x$ with $|x| \le K(x)$, is not recursively enumerable (recognizable).

Formalized by `Cslib.Kolmogorov.not_rePred_incompressible`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Semicomputable.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Kolmogorov/Semicomputable.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity/index.html#not-re-pred-incompressible).

## The incompressible strings are not decidable

Let $K$ denote Kolmogorov complexity and
$|x|$ the length of a binary string $x$. The set of incompressible binary strings, that is, of
binary strings $x$ with $|x| \le K(x)$, is not decidable.

Formalized by `Cslib.Kolmogorov.not_computablePred_incompressible`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Semicomputable.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Kolmogorov/Semicomputable.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity/index.html#not-computable-pred-incompressible).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Upper semicomputability of Kolmogorov complexity, and incompressible strings](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/kolmogorov-complexity/upper-semicomputability-of-kolmogorov-complexity)
