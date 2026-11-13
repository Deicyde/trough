---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.LinearTripleSystemIndependenceErdosProblem1024Wanted.IsLinearTripleSystem, MathlibExt.Combinatorics.LinearTripleSystemIndependenceErdosProblem1024Wanted.linearTripleIndependence, MathlibExt.Combinatorics.LinearTripleSystemIndependenceErdosProblem1024Wanted.linearTripleIndependenceAsymp, MathlibExt.Combinatorics.LinearTripleSystemIndependenceErdosProblem1024Wanted.linearTripleIndependenceAsymp_holds
statement: formalized
---

# Independence in linear triple systems

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independence-in-linear-triple-systems/index.html).

## Linear triple systems

A finite family $H$ of subsets of $\{0, \dots, n-1\}$ is a linear
triple system (a $3$-uniform linear hypergraph, or partial Steiner triple system) when every
member of $H$ has exactly three elements and any two distinct members of $H$ share at most one
element.

Formalized by `MathlibExt.Combinatorics.LinearTripleSystemIndependenceErdosProblem1024Wanted.IsLinearTripleSystem`, a definition declared in [WantedExt/Combinatorics/LinearTripleSystemIndependenceErdosProblem1024Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LinearTripleSystemIndependenceErdosProblem1024Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independence-in-linear-triple-systems/index.html#is-linear-triple-system).

## Independence number of linear triple systems

For $n \in \mathbb{N}$, $f(n)$ is the largest
$m \in \mathbb{N}$ such that every linear triple system $H$ on the vertex set $\{0, \dots, n-1\}$
has an independent set of size at least $m$: a set $I$ of at least $m$ vertices such that no
triple of $H$ is a subset of $I$. The largest such $m$ exists because $m = 0$ qualifies and no
such $m$ exceeds $n$.

Formalized by `MathlibExt.Combinatorics.LinearTripleSystemIndependenceErdosProblem1024Wanted.linearTripleIndependence`, a definition declared in [WantedExt/Combinatorics/LinearTripleSystemIndependenceErdosProblem1024Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LinearTripleSystemIndependenceErdosProblem1024Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independence-in-linear-triple-systems/index.html#linear-triple-independence).

## Erdős Problem 1024: the Phelps–Rödl asymptotic

For $n \in \mathbb{N}$ let $f(n)$ be the
independence number of linear triple systems on $n$ vertices: the largest $m$ such that every
linear triple system on $n$ vertices has an independent set (a set of vertices containing no
triple of the system) of at least $m$ vertices. This is the statement that
$f(n) = \Theta(\sqrt{n \log n})$ as $n \to \infty$, that is, $f(n) = O(\sqrt{n \log n})$ and
$\sqrt{n \log n} = O(f(n))$.

Formalized by `MathlibExt.Combinatorics.LinearTripleSystemIndependenceErdosProblem1024Wanted.linearTripleIndependenceAsymp`, a definition declared in [WantedExt/Combinatorics/LinearTripleSystemIndependenceErdosProblem1024Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LinearTripleSystemIndependenceErdosProblem1024Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independence-in-linear-triple-systems/index.html#linear-triple-independence-asymp).

## Phelps–Rödl theorem on independence in linear triple systems

For $n \in \mathbb{N}$ let
$f(n)$ be the largest $m$ such that every linear triple system on $\{0, \dots, n-1\}$ (a family
of $3$-element sets, any two distinct ones sharing at most one element) has an independent set of
at least $m$ vertices, that is, a set of at least $m$ vertices containing no triple of the system.
Then $f(n) = \Theta(\sqrt{n \log n})$ as $n \to \infty$: there are constants $c, C > 0$ such that
$c \sqrt{n \log n} \le f(n) \le C \sqrt{n \log n}$ for all sufficiently large $n$.

Erdős had shown $n^{1/2} \ll f(n) \ll n^{2/3}$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #1024, https://www.erdosproblems.com/1024 (status SOLVED); resolution: K. T. Phelps and V. Rödl, Steiner triple systems with minimum independence number, Ars Combin. (1986), 167-172, f(n) ≍ (n log n)^{1/2} (erdosproblems.com/1024), https://www.erdosproblems.com/1024.

Stated but not proved: `MathlibExt.Combinatorics.LinearTripleSystemIndependenceErdosProblem1024Wanted.linearTripleIndependenceAsymp_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/LinearTripleSystemIndependenceErdosProblem1024Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LinearTripleSystemIndependenceErdosProblem1024Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independence-in-linear-triple-systems/index.html#linear-triple-independence-asymp-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Independence in linear triple systems](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independence-in-linear-triple-systems/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independence-in-linear-triple-systems)
