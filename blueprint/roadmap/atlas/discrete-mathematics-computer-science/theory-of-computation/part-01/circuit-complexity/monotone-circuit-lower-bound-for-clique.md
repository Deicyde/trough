---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.RazborovMonotoneClique.cliqueHolds, MetaMathlibExt.Complexity.KeyTheorems.RazborovMonotoneClique.razborov_monotone_clique
statement: formalized
---

# Monotone circuit lower bound for clique

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/monotone-circuit-lower-bound-for-clique/index.html).

## The clique function on adjacency-matrix bits

For a natural number $n$ and a bitstring
$x$, read $x$ as an $n \times n$ adjacency matrix in row-major order: the entry for a pair
$(a, b)$ is the bit of $x$ at position $an + b$, where a position beyond the end of $x$ reads as
false. The clique predicate holds for $n$ and $x$ when there is a set $S$ of exactly
$\lfloor n/3 \rfloor$ vertices among $0, \dots, n - 1$ such that the entry for $(a, b)$ is true
for all distinct $a, b \in S$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.RazborovMonotoneClique.cliqueHolds`, a definition declared in [WantedExt/Complexity/KeyTheorems/RazborovMonotoneCliqueWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/RazborovMonotoneCliqueWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/monotone-circuit-lower-bound-for-clique/index.html#clique-holds).

## Razborov: monotone circuits for clique need superpolynomial size

For every polynomial
$p$ with natural-number coefficients there is a natural number $n$ with the following property.
Let $C$ be a well-formed monotone flat circuit on $n^2$ inputs, that is, every gate of $C$ is an
input variable, an and gate or an or gate, and refers only to earlier gates. Suppose that for
every bitstring $x$ of length $n^2$, when input variable $i$ is given the $i$-th bit of $x$, $C$
has a last gate with value true if and only if the $n \times n$ matrix read from $x$ in
row-major order has a clique of size $\lfloor n/3 \rfloor$, that is, a set
$S \subseteq \{0, \dots, n - 1\}$ of $\lfloor n/3 \rfloor$ vertices whose entries $(a, b)$ are
true for all distinct $a, b \in S$. Then $C$ has more than $p(n^2)$ gates.

## Sources

- A. A. Razborov, "Lower bounds on the monotone complexity of some Boolean functions", Soviet Mathematics Doklady 31 (1985), 354-357.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.RazborovMonotoneClique.razborov_monotone_clique` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/RazborovMonotoneCliqueWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/RazborovMonotoneCliqueWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/monotone-circuit-lower-bound-for-clique/index.html#razborov-monotone-clique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monotone circuit lower bound for clique](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/monotone-circuit-lower-bound-for-clique/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/circuit-complexity/monotone-circuit-lower-bound-for-clique)
