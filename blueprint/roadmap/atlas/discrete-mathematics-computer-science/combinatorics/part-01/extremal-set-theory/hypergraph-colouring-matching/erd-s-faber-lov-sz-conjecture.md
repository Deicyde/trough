---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosFaberLovaszConjectureWanted.ErdosFaberLovaszConjecture.Hypergraph, MathlibExt.Combinatorics.ErdosFaberLovaszConjectureWanted.ErdosFaberLovaszConjecture.Hypergraph.Coloring, MathlibExt.Combinatorics.ErdosFaberLovaszConjectureWanted.ErdosFaberLovaszConjecture.Hypergraph.IsLinear, MathlibExt.Combinatorics.ErdosFaberLovaszConjectureWanted.ErdosFaberLovaszConjecture.Hypergraph.chromaticIndex, MathlibExt.Combinatorics.ErdosFaberLovaszConjectureWanted.ErdosFaberLovaszConjecture.theorem_1_1
statement: formalized
---

# Erdős–Faber–Lovász conjecture

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/erd-s-faber-lov-sz-conjecture/index.html).

## Hypergraph

A hypergraph on a type $V$ of vertices is a set of subsets of $V$; its elements
are the edges of the hypergraph. Edges may be empty, and no finiteness condition is imposed.

Formalized by `MathlibExt.Combinatorics.ErdosFaberLovaszConjectureWanted.ErdosFaberLovaszConjecture.Hypergraph`, an abbreviation declared in [WantedExt/Combinatorics/ErdosFaberLovaszConjectureWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosFaberLovaszConjectureWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/erd-s-faber-lov-sz-conjecture/index.html#hypergraph).

## Edge coloring of a hypergraph

Let $\mathcal{H}$ be a hypergraph on a vertex type $V$ and
let $\alpha$ be a type. An $\alpha$-coloring of $\mathcal{H}$ is a map $c$ from the set of edges of
$\mathcal{H}$ to $\alpha$ such that $c(e_1) \ne c(e_2)$ for any two distinct edges $e_1$ and $e_2$
of $\mathcal{H}$ that have a vertex in common.

Formalized by `MathlibExt.Combinatorics.ErdosFaberLovaszConjectureWanted.ErdosFaberLovaszConjecture.Hypergraph.Coloring`, a structure declared in [WantedExt/Combinatorics/ErdosFaberLovaszConjectureWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosFaberLovaszConjectureWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/erd-s-faber-lov-sz-conjecture/index.html#coloring).

## Linear hypergraph

A hypergraph $\mathcal{H}$ is linear if any two distinct edges of
$\mathcal{H}$ have at most one vertex in common.

Formalized by `MathlibExt.Combinatorics.ErdosFaberLovaszConjectureWanted.ErdosFaberLovaszConjecture.Hypergraph.IsLinear`, a definition declared in [WantedExt/Combinatorics/ErdosFaberLovaszConjectureWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosFaberLovaszConjectureWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/erd-s-faber-lov-sz-conjecture/index.html#is-linear).

## Chromatic index of a hypergraph

The chromatic index of a hypergraph $\mathcal{H}$ is the
least natural number $n$ such that $\mathcal{H}$ has a coloring with colors in
$\{0, 1, \dots, n-1\}$, and $0$ if there is no such $n$.

Formalized by `MathlibExt.Combinatorics.ErdosFaberLovaszConjectureWanted.ErdosFaberLovaszConjecture.Hypergraph.chromaticIndex`, a definition declared in [WantedExt/Combinatorics/ErdosFaberLovaszConjectureWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosFaberLovaszConjectureWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/erd-s-faber-lov-sz-conjecture/index.html#chromatic-index).

## Erdős–Faber–Lovász conjecture for sufficiently many vertices

For every sufficiently large
natural number $n$, every linear hypergraph on the vertex set $\{0, 1, \dots, n-1\}$ has chromatic
index at most $n$.

## Sources

- D. Y. Kang, T. Kelly, D. Kühn, A. Methuku, and D. Osthus, `A proof of the Erdős–Faber–Lovász conjecture`, Annals of Math, 198 (2) 2023. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_erdos_faber_lovasz_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.ErdosFaberLovaszConjectureWanted.ErdosFaberLovaszConjecture.theorem_1_1` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosFaberLovaszConjectureWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosFaberLovaszConjectureWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/erd-s-faber-lov-sz-conjecture/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Erdős–Faber–Lovász conjecture](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/erd-s-faber-lov-sz-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/erd-s-faber-lov-sz-conjecture)
