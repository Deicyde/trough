---
declaration: section
origin: cited
lean: Cslib.Decidability.eval_comp_const, Cslib.Decidability.REPred.of_manyOneReducible, Cslib.Decidability.rePred_haltingSet, Cslib.Decidability.oneOneReducible_haltingSet, Cslib.Decidability.manyOneReducible_haltingSet, Cslib.Decidability.rePred_iff_manyOneReducible_haltingSet, Cslib.Decidability.rePred_iff_oneOneReducible_haltingSet
statement: formalized
proof: formalized
---

# Completeness of the halting set

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/completeness-of-the-halting-set/index.html).

## Composing a code with a constant code ignores the input

Let $c$ be a code of a partial
recursive function and let $n, m \in \mathbb{N}$. The code that first computes the constant
function with value $n$ and then applies $c$, evaluated at $m$, gives the same partial value as
$c$ evaluated at $n$: one is defined exactly when the other is, and then they are equal.

Formalized by `Cslib.Decidability.eval_comp_const`, a theorem declared in [CSLibExt/Computability/Decidability/REComplete.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/REComplete.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/completeness-of-the-halting-set/index.html#eval-comp-const).

## Recognizability transfers down many-one reductions

Let $\alpha$ and $\beta$ be types
with primitive recursive encodings into $\mathbb{N}$, and let $p$ and $q$ be predicates on
$\alpha$ and on $\beta$. Suppose that $p$ many-one reduces to $q$, that is, there is a computable
function $f : \alpha \to \beta$ such that for every $a \in \alpha$, $p(a)$ holds if and only if
$q(f(a))$ holds. If $q$ is recognizable (recursively enumerable: the domain of a partial
computable function on $\beta$), then $p$ is recognizable.

Formalized by `Cslib.Decidability.REPred.of_manyOneReducible`, a theorem declared in [CSLibExt/Computability/Decidability/REComplete.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/REComplete.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/completeness-of-the-halting-set/index.html#of-many-one-reducible).

## The halting set is recognizable

The halting set, the set of numbers $n$ such that the
code with number $n$ halts on input $0$, is recursively enumerable: it is the domain of a partial
computable function on $\mathbb{N}$.

Formalized by `Cslib.Decidability.rePred_haltingSet`, a theorem declared in [CSLibExt/Computability/Decidability/REComplete.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/REComplete.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/completeness-of-the-halting-set/index.html#re-pred-halting-set).

## Every recognizable predicate one-one reduces to the halting set

Let $\alpha$ be a type
with a primitive recursive encoding into $\mathbb{N}$, and let $p$ be a recognizable (recursively
enumerable) predicate on $\alpha$, that is, the domain of a partial computable function on
$\alpha$. Here the halting set is the set of $n \in \mathbb{N}$ such that the partial recursive
function with code number $n$ halts on input $0$. Then there is an injective computable function
$f : \alpha \to \mathbb{N}$ such that for every $a \in \alpha$, $p(a)$ holds if and only if $f(a)$
lies in the halting set.

The proof takes for $f(a)$ the number of the code that ignores its input and runs a code for $p$
on the number encoding $a$; distinct $a$ give distinct codes.

Formalized by `Cslib.Decidability.oneOneReducible_haltingSet`, a theorem declared in [CSLibExt/Computability/Decidability/REComplete.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/REComplete.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/completeness-of-the-halting-set/index.html#one-one-reducible-halting-set).

## Every recognizable predicate many-one reduces to the halting set

Let $\alpha$ be a type
with a primitive recursive encoding into $\mathbb{N}$, and let $p$ be a recognizable (recursively
enumerable) predicate on $\alpha$, that is, the domain of a partial computable function on
$\alpha$. Here the halting set is the set of $n \in \mathbb{N}$ such that the partial recursive
function with code number $n$ halts on input $0$. Then there is a computable function
$f : \alpha \to \mathbb{N}$ such that for every $a \in \alpha$, $p(a)$ holds if and only if $f(a)$
lies in the halting set.

Formalized by `Cslib.Decidability.manyOneReducible_haltingSet`, a theorem declared in [CSLibExt/Computability/Decidability/REComplete.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/REComplete.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/completeness-of-the-halting-set/index.html#many-one-reducible-halting-set).

## A predicate is recognizable iff it many-one reduces to the halting set

Let $\alpha$ be a
type with a primitive recursive encoding into $\mathbb{N}$ and let $p$ be a predicate on $\alpha$.
Here the halting set is the set of $n \in \mathbb{N}$ such that the partial recursive function
with code number $n$ halts on input $0$. Then $p$ is recognizable (recursively enumerable: the
domain of a partial computable function on $\alpha$) if and only if there is a computable function
$f : \alpha \to \mathbb{N}$ such that for every $a \in \alpha$, $p(a)$ holds if and only if $f(a)$
lies in the halting set.

Formalized by `Cslib.Decidability.rePred_iff_manyOneReducible_haltingSet`, a theorem declared in [CSLibExt/Computability/Decidability/REComplete.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/REComplete.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/completeness-of-the-halting-set/index.html#re-pred-iff-many-one-reducible-halting-s).

## A predicate is recognizable iff it one-one reduces to the halting set

Let $\alpha$ be a
type with a primitive recursive encoding into $\mathbb{N}$ and let $p$ be a predicate on $\alpha$.
Here the halting set is the set of $n \in \mathbb{N}$ such that the partial recursive function
with code number $n$ halts on input $0$. Then $p$ is recognizable (recursively enumerable: the
domain of a partial computable function on $\alpha$) if and only if there is an injective
computable function $f : \alpha \to \mathbb{N}$ such that for every $a \in \alpha$, $p(a)$ holds
if and only if $f(a)$ lies in the halting set.

Formalized by `Cslib.Decidability.rePred_iff_oneOneReducible_haltingSet`, a theorem declared in [CSLibExt/Computability/Decidability/REComplete.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/REComplete.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/completeness-of-the-halting-set/index.html#re-pred-iff-one-one-reducible-halting-se).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Completeness of the halting set](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/completeness-of-the-halting-set/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/degrees-and-hierarchies/completeness-of-the-halting-set)
