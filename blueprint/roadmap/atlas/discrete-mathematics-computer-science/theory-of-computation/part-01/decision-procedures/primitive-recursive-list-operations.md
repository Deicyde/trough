---
declaration: section
origin: cited
lean: Cslib.Decidability.memB, Cslib.Decidability.dedupB, Cslib.Decidability.iterate_closed, Cslib.Decidability.computablePred_of_primrec_bool
statement: formalized
proof: formalized
---

# Primitive recursive list operations

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/primitive-recursive-list-operations/index.html).

## Boolean membership test for lists of natural numbers

For a list $G$ of natural numbers
and a natural number $j$, the Boolean value that is true exactly when $j$ is an entry of $G$.

Formalized by `Cslib.Decidability.memB`, a definition declared in [CSLibExt/Computability/Decidability/PrimrecList.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PrimrecList.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/primitive-recursive-list-operations/index.html#mem-b).

## Duplicate removal for lists of natural numbers

For a list $l$ of natural numbers, the list
obtained from $l$ by deleting every entry that occurs again later in $l$: each element of $l$ is
kept once, at its last occurrence, and the kept entries stay in their order in $l$.

Formalized by `Cslib.Decidability.dedupB`, a definition declared in [CSLibExt/Computability/Decidability/PrimrecList.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PrimrecList.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/primitive-recursive-list-operations/index.html#dedup-b).

## Bounded monotone rounds on lists close off

Let $f$ map lists of natural numbers to lists
of natural numbers and be monotone for list inclusion: $f(G) \subseteq f(G')$ whenever
$G \subseteq G'$, where $G \subseteq G'$ means that every entry of $G$ is an entry of $G'$. If $B$
is a list with $f(G) \subseteq B$ for every list $G$, and $n$ is the length of $B$, then
$f(f^n([\,])) \subseteq f^n([\,])$, where $f^n$ is the $n$-fold iterate of $f$ and $[\,]$ is the
empty list.

Formalized by `Cslib.Decidability.iterate_closed`, a theorem declared in [CSLibExt/Computability/Decidability/PrimrecList.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PrimrecList.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/primitive-recursive-list-operations/index.html#iterate-closed).

## Predicates with a primitive recursive decision procedure are computable

Let $\beta$ be a
primcodable type, $p$ a predicate on $\beta$, and $f : \beta \to \mathrm{Bool}$ a primitive
recursive function such that $f(b) = \mathrm{true}$ exactly when $p(b)$ holds, for every
$b \in \beta$. Then $p$ is a computable predicate.

Formalized by `Cslib.Decidability.computablePred_of_primrec_bool`, a theorem declared in [CSLibExt/Computability/Decidability/PrimrecList.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PrimrecList.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/primitive-recursive-list-operations/index.html#computable-pred-of-primrec-bool).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primitive recursive list operations](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/primitive-recursive-list-operations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/decision-procedures/primitive-recursive-list-operations)
