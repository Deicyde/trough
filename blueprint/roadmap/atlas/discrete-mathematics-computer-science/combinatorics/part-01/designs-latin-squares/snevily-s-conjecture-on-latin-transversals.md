---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SnevilyTransversalWanted.conjecture, MathlibExt.Combinatorics.SnevilyTransversalWanted.conjecture_holds
statement: formalized
---

# Snevily's conjecture on Latin transversals

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/snevily-s-conjecture-on-latin-transversals/index.html).

## Snevily's conjecture

The statement that for every finite abelian group $G$ of odd order,
written additively, and all subsets $A, B \subseteq G$ with $|A| = |B|$, there is a bijection
$f \colon A \to B$ such that the sums $a + f(a)$, for $a \in A$, are pairwise distinct.

Equivalently, $A$ and $B$ can be enumerated as $a_1, \dots, a_k$ and $b_1, \dots, b_k$ so that
the sums $a_i + b_i$ are pairwise distinct: given such enumerations, send $a_i$ to $b_i$;
conversely, enumerate $A$ and transport the enumeration along $f$.

## Sources

- OPG-655.

Formalized by `MathlibExt.Combinatorics.SnevilyTransversalWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/SnevilyTransversalWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SnevilyTransversalWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/snevily-s-conjecture-on-latin-transversals/index.html#conjecture).

## Snevily's conjecture is true

Let $G$ be a finite abelian group of odd order, written
additively, and let $A, B \subseteq G$ be subsets with $|A| = |B|$. Then there is a bijection
$f \colon A \to B$ such that the sums $a + f(a)$, for $a \in A$, are pairwise distinct.

## Sources

- Boris Arsovski, A proof of Snevily's conjecture, Israel J. Math. 182 (2011), 505-508.

Stated but not proved: `MathlibExt.Combinatorics.SnevilyTransversalWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SnevilyTransversalWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SnevilyTransversalWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/snevily-s-conjecture-on-latin-transversals/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Snevily's conjecture on Latin transversals](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/snevily-s-conjecture-on-latin-transversals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/designs-latin-squares/snevily-s-conjecture-on-latin-transversals)
