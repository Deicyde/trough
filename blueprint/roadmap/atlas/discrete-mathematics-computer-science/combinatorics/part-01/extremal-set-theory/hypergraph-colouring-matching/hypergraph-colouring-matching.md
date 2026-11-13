---
declaration: section
origin: cited
lean: MetaMathlibExt.baranyai_theorem, Finset.HasPropertyB, MathlibExt.Combinatorics.ScottishBook9Wanted.finiteSetsCommonElement
statement: formalized
---

# Hypergraph colouring, matchings and covers: its own results

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/index.html).

Property B and hypergraph colouring, Erdős–Faber–Lovász, Kneser hypergraphs, independence in Steiner and linear triple systems, set mappings, strongly maximal matchings, minimal covers, transversals, Baranyai's theorem and common elements of small set families.

## Baranyai's theorem

Let $n$ and $h$ be natural numbers with $h \mid n$, and let
$V = \{0, \dots, n-1\}$. The $h$-element subsets of $V$, the edges of the complete
$h$-uniform hypergraph on $V$, can be partitioned into perfect matchings: there is a finite
family $\mathcal{P}$ of sets of subsets of $V$ such that the union of the members of
$\mathcal{P}$ is exactly the set of $h$-element subsets of $V$, distinct members of
$\mathcal{P}$ are disjoint, and each member of $\mathcal{P}$ consists of pairwise disjoint sets
whose union is $V$.

## Sources

- https://en.wikipedia.org/wiki/Baranyai%27s_theorem.

Formalized by `MetaMathlibExt.baranyai_theorem`, a theorem declared in [MathlibExt/Combinatorics/Baranyai.lean, line 899](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Baranyai.lean#L899). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/index.html#baranyai-theorem).

## Property B for families of finite sets

A family `F` of finite sets has **property B** (equivalently, it is
`2`-colourable, i.e. its chromatic number is at most `2`) if there is a
`2`-colouring of the ground set under which no
member of `F` is monochromatic.

Formalized by `Finset.HasPropertyB`, a definition declared in [MathlibExt/Data/Finset/PropertyB.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Finset/PropertyB.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/index.html#has-property-b).

## Scottish Book Problem 9 (a common element of small finite sets)

Let $n$ be a natural
number, let $\alpha$ be a nonempty set, and let $(E_i)_{i \in I}$ be a family of finite subsets
of $\alpha$, indexed by an arbitrary set $I$, with $|E_i| \le n$ for every $i \in I$. Suppose
that for all indices $i_0, i_1, \dots, i_n \in I$, not necessarily distinct, the sets
$E_{i_0}, E_{i_1}, \dots, E_{i_n}$ have an element in common. Then some element of $\alpha$
lies in every $E_i$.

The hypothesis is read with repetitions allowed: it quantifies over all choices of $n + 1$
indices, not only over $n + 1$ distinct members. Under the distinct-members reading the claim
would be false when the family has at most $n$ members (the hypothesis is then vacuous), so the
repetition reading is the intended one.

## Sources

- S. Mazur and W. Orlicz, Problem 9 of the Scottish Book, stated as a theorem by Ulam in the Scottish Book typescript; see also the 2026 survey "90+ years of the Scottish Book" (arXiv:2603.27867), which records that Ulam solved Problem 9.

Stated but not proved: `MathlibExt.Combinatorics.ScottishBook9Wanted.finiteSetsCommonElement` is written with `theorem_wanted` in [WantedExt/Combinatorics/ScottishBook9Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ScottishBook9Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/index.html#finite-sets-common-element).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hypergraph colouring, matchings and covers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching)
