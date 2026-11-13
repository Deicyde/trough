---
declaration: section
origin: cited
lean: Set.IsSidon, MathlibExt.Combinatorics.ErdosSidonIsolatedSumsWanted.IsSidon, MathlibExt.Combinatorics.ErdosSidonIsolatedSumsWanted.Sumset, MathlibExt.Combinatorics.ErdosSidonIsolatedSumsWanted.IsIsolated, MathlibExt.Combinatorics.ErdosSidonIsolatedSumsWanted.IsolatedCount, MathlibExt.Combinatorics.ErdosSidonIsolatedSumsWanted.conjecture, MathlibExt.Combinatorics.ErdosSidonIsolatedSumsWanted.conjecture_holds
statement: formalized
---

# Sidon sets

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets/index.html).

## Sidon set

A set in an additive commutative monoid is Sidon when every equality of
two pairwise sums is trivial up to swapping the summands. Repeated summands
are included.

Formalized by `Set.IsSidon`, a definition declared in [MathlibExt/Combinatorics/Additive/Sidon.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Additive/Sidon.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets/index.html#is-sidon).

## Finite Sidon sets of natural numbers

A finite set $A$ of natural numbers is a Sidon set
when every equality $a + b = c + d$ with $a, b, c, d \in A$ is trivial, that is, $a = c$ and
$b = d$, or $a = d$ and $b = c$.

Formalized by `MathlibExt.Combinatorics.ErdosSidonIsolatedSumsWanted.IsSidon`, a definition declared in [WantedExt/Combinatorics/ErdosSidonIsolatedSumsWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosSidonIsolatedSumsWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets/index.html#is-sidon-2).

## Sumset of a finite set of natural numbers

For a finite set $A$ of natural numbers, the
sumset $A + A$ is the finite set of all sums $x + y$ with $x, y \in A$.

Formalized by `MathlibExt.Combinatorics.ErdosSidonIsolatedSumsWanted.Sumset`, a definition declared in [WantedExt/Combinatorics/ErdosSidonIsolatedSumsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosSidonIsolatedSumsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets/index.html#sumset).

## Isolated elements of a set of natural numbers

Let $S$ be a finite set of natural numbers.
A natural number $a$ is isolated in $S$ when $a \in S$, $a + 1 \notin S$, and either $a = 0$ or
$a - 1 \notin S$.

For $a = 0$ the condition on the predecessor is vacuous, since $0$ has no predecessor among the
natural numbers.

Formalized by `MathlibExt.Combinatorics.ErdosSidonIsolatedSumsWanted.IsIsolated`, a definition declared in [WantedExt/Combinatorics/ErdosSidonIsolatedSumsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosSidonIsolatedSumsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets/index.html#is-isolated).

## Number of isolated elements

For a finite set $S$ of natural numbers, the isolated count
of $S$ is the number of elements $a \in S$ with $a + 1 \notin S$ and either $a = 0$ or
$a - 1 \notin S$.

Formalized by `MathlibExt.Combinatorics.ErdosSidonIsolatedSumsWanted.IsolatedCount`, a definition declared in [WantedExt/Combinatorics/ErdosSidonIsolatedSumsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosSidonIsolatedSumsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets/index.html#isolated-count).

## Erdős Problem 152 on isolated sums of Sidon sets

A finite set $A$ of natural numbers is
a Sidon set when $a + b = c + d$ with $a, b, c, d \in A$ implies $\{a, b\} = \{c, d\}$, and its
sumset is $A + A = \{x + y : x, y \in A\}$. An element $s$ of a finite set $S$ of natural numbers
is isolated in $S$ when $s + 1 \notin S$ and either $s = 0$ or $s - 1 \notin S$. The proposition
asserts that for every natural number $M \ge 1$ there is a natural number $K$ such that every
finite Sidon set $A$ of natural numbers with at least $K$ elements has at least $M$ isolated
elements in $A + A$.

Formalized by `MathlibExt.Combinatorics.ErdosSidonIsolatedSumsWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosSidonIsolatedSumsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosSidonIsolatedSumsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets/index.html#conjecture).

## Large Sidon sets have many isolated sums

For every natural number $M \ge 1$ there is a
natural number $K$ such that every finite Sidon set $A$ of natural numbers with at least $K$
elements has at least $M$ isolated elements in its sumset $A + A = \{x + y : x, y \in A\}$. Here
$A$ is a Sidon set when $a + b = c + d$ with $a, b, c, d \in A$ implies $\{a, b\} = \{c, d\}$,
and an element $s$ of $A + A$ is isolated when $s + 1 \notin A + A$ and either $s = 0$ or
$s - 1 \notin A + A$.

This answers Erdős Problem 152 affirmatively: Tsoukalas et al. show, with a Lean proof, that
every Sidon set $A$ of $n$ natural numbers has at least $(n^2 - 100n - 16)/16$ isolated elements
in $A + A$.

## Sources

- George Tsoukalas et al., Advancing Mathematics Research with AI-Driven Formal Proof Search, arXiv preprint (2026), arXiv:2605.22763, https://arxiv.org/abs/2605.22763.

Stated but not proved: `MathlibExt.Combinatorics.ErdosSidonIsolatedSumsWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosSidonIsolatedSumsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosSidonIsolatedSumsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sidon sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets)
