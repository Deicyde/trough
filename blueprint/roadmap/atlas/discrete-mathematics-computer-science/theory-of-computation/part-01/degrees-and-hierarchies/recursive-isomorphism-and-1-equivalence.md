---
declaration: section
origin: cited
lean: Cslib.Decidability.RecursiveIsomorphic, Cslib.Decidability.computable_invFun_of_bijective, Cslib.Decidability.recursiveIsomorphic_to_oneOneEquiv
statement: formalized
proof: formalized
---

# Recursive isomorphism and 1-equivalence

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/recursive-isomorphism-and-1-equivalence/index.html).

## Recursively isomorphic predicates

Two predicates $P$ and $Q$ on $\mathbb{N}$ are
recursively isomorphic when there is a computable bijection $f : \mathbb{N} \to \mathbb{N}$ such
that for every $n$, $P(n)$ holds if and only if $Q(f(n))$ holds.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 7.1.

Formalized by `Cslib.Decidability.RecursiveIsomorphic`, a definition declared in [CSLibExt/Computability/Decidability/Myhill.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Myhill.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/recursive-isomorphism-and-1-equivalence/index.html#recursive-isomorphic).

## The inverse of a computable bijection is computable

Let
$f : \mathbb{N} \to \mathbb{N}$ be a computable bijection. Then its inverse function
$f^{-1} : \mathbb{N} \to \mathbb{N}$ is computable.

The inverse is computed by unbounded search for the unique preimage.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (inverses of recursive permutations).

Formalized by `Cslib.Decidability.computable_invFun_of_bijective`, a theorem declared in [CSLibExt/Computability/Decidability/Myhill.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Myhill.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/recursive-isomorphism-and-1-equivalence/index.html#computable-inv-fun-of-bijective).

## A recursive isomorphism gives a 1-equivalence

Let $P$ and $Q$ be predicates on
$\mathbb{N}$. If $P$ and $Q$ are recursively isomorphic, then they are 1-equivalent: $P$ is
one-one reducible to $Q$ and $Q$ is one-one reducible to $P$. Here $P$ is one-one reducible to
$Q$ when there is a computable injective function $g : \mathbb{N} \to \mathbb{N}$ such that for
every $n$, $P(n)$ holds if and only if $Q(g(n))$ holds.

This is the easy direction of Myhill's isomorphism theorem.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 7.1.

Formalized by `Cslib.Decidability.recursiveIsomorphic_to_oneOneEquiv`, a theorem declared in [CSLibExt/Computability/Decidability/Myhill.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Myhill.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/recursive-isomorphism-and-1-equivalence/index.html#recursive-isomorphic-to-one-one-equiv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Recursive isomorphism and 1-equivalence](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/recursive-isomorphism-and-1-equivalence/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/degrees-and-hierarchies/recursive-isomorphism-and-1-equivalence)
