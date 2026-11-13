---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.PairSetMappingIndependenceErdosProblem1025Wanted.IsIndependentFor, MathlibExt.Combinatorics.PairSetMappingIndependenceErdosProblem1025Wanted.setMappingIndependence, MathlibExt.Combinatorics.PairSetMappingIndependenceErdosProblem1025Wanted.setMappingIndependenceAsymp, MathlibExt.Combinatorics.PairSetMappingIndependenceErdosProblem1025Wanted.setMappingIndependenceAsymp_holds
statement: formalized
---

# Independent sets of set mappings on pairs

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-of-set-mappings-on-pairs/index.html).

## Independent set of a set mapping on pairs

Let $n$ be a natural number and let $f$ assign
to each unordered pair $\{x, y\}$ of elements of $\{0, \dots, n-1\}$ (possibly with $x = y$) an
element of $\{0, \dots, n-1\}$. A finite set $X \subseteq \{0, \dots, n-1\}$ is independent for $f$
if $f(\{x, y\}) \notin X$ for all distinct $x, y \in X$.

Formalized by `MathlibExt.Combinatorics.PairSetMappingIndependenceErdosProblem1025Wanted.IsIndependentFor`, a definition declared in [WantedExt/Combinatorics/PairSetMappingIndependenceErdosProblem1025Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PairSetMappingIndependenceErdosProblem1025Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-of-set-mappings-on-pairs/index.html#is-independent-for).

## Independence number of set mappings on pairs

For a natural number $n$, $g(n)$ is the
largest $k$ such that every map $f$ from the unordered pairs $\{x, y\}$ of elements of
$\{0, \dots, n-1\}$ (possibly with $x = y$) to $\{0, \dots, n-1\}$ with
$f(\{x, y\}) \notin \{x, y\}$ for all distinct $x, y$ has an independent set of at least $k$
elements, that is, a set $X \subseteq \{0, \dots, n-1\}$ with $|X| \ge k$ and
$f(\{x, y\}) \notin X$ for all distinct $x, y \in X$. If no largest such $k$ exists, $g(n) = 0$;
this happens for $n = 2$, where no such $f$ exists.

Formalized by `MathlibExt.Combinatorics.PairSetMappingIndependenceErdosProblem1025Wanted.setMappingIndependence`, a definition declared in [WantedExt/Combinatorics/PairSetMappingIndependenceErdosProblem1025Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PairSetMappingIndependenceErdosProblem1025Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-of-set-mappings-on-pairs/index.html#set-mapping-independence).

## Statement of Erdős Problem 1025

For a natural number $n$, let $g(n)$ be the largest $k$
such that every map $f$ from the unordered pairs of elements of $\{0, \dots, n-1\}$ to
$\{0, \dots, n-1\}$ with $f(\{x, y\}) \notin \{x, y\}$ for all distinct $x, y$ admits a set $X$
of at least $k$ elements with $f(\{x, y\}) \notin X$ for all distinct $x, y \in X$ (and
$g(n) = 0$ if no largest such $k$ exists). This is the proposition that $g(n) \asymp \sqrt{n}$ as
$n \to \infty$, that is, that there are constants $c, C > 0$ with
$c \sqrt{n} \le g(n) \le C \sqrt{n}$ for all sufficiently large $n$.

Spencer proved the lower bound and Conlon, Fox and Sudakov the upper bound.

Formalized by `MathlibExt.Combinatorics.PairSetMappingIndependenceErdosProblem1025Wanted.setMappingIndependenceAsymp`, a definition declared in [WantedExt/Combinatorics/PairSetMappingIndependenceErdosProblem1025Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PairSetMappingIndependenceErdosProblem1025Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-of-set-mappings-on-pairs/index.html#set-mapping-independence-asymp).

## Erdős Problem 1025 (Spencer; Conlon, Fox and Sudakov)

For a natural number $n$, let $g(n)$
be the largest $k$ such that every map $f$ from the unordered pairs of elements of
$\{0, \dots, n-1\}$ to $\{0, \dots, n-1\}$ with $f(\{x, y\}) \notin \{x, y\}$ for all distinct
$x, y$ admits a set $X$ of at least $k$ elements with $f(\{x, y\}) \notin X$ for all distinct
$x, y \in X$ (and $g(n) = 0$ if no largest such $k$ exists). Then there are constants $c, C > 0$
such that $c \sqrt{n} \le g(n) \le C \sqrt{n}$ for all sufficiently large $n$, that is,
$g(n) \asymp \sqrt{n}$ as $n \to \infty$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #1025, https://www.erdosproblems.com/1025 (status SOLVED (LEAN)); resolution: J. Spencer, Turán's theorem for k-graphs, Discrete Math. (1972), 183-186; D. Conlon, J. Fox and B. Sudakov, Short proofs of some extremal results II, J. Combin. Theory Ser. B (2016), 173-196, Spencer: g(n) ≫ n^{1/2}; Conlon-Fox-Sudakov: g(n) ≪ n^{1/2} (erdosproblems.com/1025), https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1025.lean#L829.

Stated but not proved: `MathlibExt.Combinatorics.PairSetMappingIndependenceErdosProblem1025Wanted.setMappingIndependenceAsymp_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/PairSetMappingIndependenceErdosProblem1025Wanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PairSetMappingIndependenceErdosProblem1025Wanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-of-set-mappings-on-pairs/index.html#set-mapping-independence-asymp-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Independent sets of set mappings on pairs](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-of-set-mappings-on-pairs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-of-set-mappings-on-pairs)
