---
declaration: section
origin: cited
lean: Cslib.Decidability.enumRE, Cslib.Decidability.Productive, Cslib.Decidability.Creative, Cslib.Decidability.Immune, Cslib.Decidability.Simple, Cslib.Decidability.productive_not_re, Cslib.Decidability.immune_not_re, Cslib.Decidability.simple_not_computable
statement: formalized
proof: formalized
---

# Productive, creative, simple and immune sets

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html).

## Standard enumeration of the recursively enumerable sets

For natural numbers $e$ and $n$,
$n$ belongs to $W_e$, the $e$-th recursively enumerable set, when the partial recursive function
$\varphi_e$ computed by the program with index $e$ in the standard numbering of partial recursive
programs is defined at $n$; thus $W_e$ is the domain of $\varphi_e$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (standard enumeration of the partial recursive functions).

Formalized by `Cslib.Decidability.enumRE`, a definition declared in [CSLibExt/Computability/Decidability/SpecialSets.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/SpecialSets.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html#enum-re).

## Productive set

A set $A$ of natural numbers is productive when there is a partial
recursive function $f$ such that for every natural number $e$ with $W_e \subseteq A$, where $W_e$
is the $e$-th recursively enumerable set in the standard enumeration, $f(e)$ is defined,
$f(e) \in A$ and $f(e) \notin W_e$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 5.1.

Formalized by `Cslib.Decidability.Productive`, a definition declared in [CSLibExt/Computability/Decidability/SpecialSets.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/SpecialSets.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html#productive).

## Creative set

A set $A$ of natural numbers is creative when it is recursively enumerable
and its complement $\mathbb{N} \setminus A$ is productive.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 5.2.

Formalized by `Cslib.Decidability.Creative`, a definition declared in [CSLibExt/Computability/Decidability/SpecialSets.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/SpecialSets.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html#creative).

## Immune set

A set $A$ of natural numbers is immune when it is infinite and every
recursively enumerable set $B \subseteq A$ is finite.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 5.4.

Formalized by `Cslib.Decidability.Immune`, a definition declared in [CSLibExt/Computability/Decidability/SpecialSets.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/SpecialSets.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html#immune).

## Simple set

A set $P$ of natural numbers is **simple** when it is recursively enumerable
and its complement $\{n \mid \neg P(n)\}$ is immune.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 5.3.

Formalized by `Cslib.Decidability.Simple`, a definition declared in [CSLibExt/Computability/Decidability/SpecialSets.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/SpecialSets.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html#simple).

## A productive set is not recursively enumerable

No productive set of natural numbers is
recursively enumerable: if it were the $e$-th recursively enumerable set $W_e$, its productive
function would produce a member of it outside $W_e$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 5.5.

Formalized by `Cslib.Decidability.productive_not_re`, a theorem declared in [CSLibExt/Computability/Decidability/SpecialSets.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/SpecialSets.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html#productive-not-re).

## An immune set is not recursively enumerable

It would be an infinite
RE subset of itself.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 5.6.

Formalized by `Cslib.Decidability.immune_not_re`, a theorem declared in [CSLibExt/Computability/Decidability/SpecialSets.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/SpecialSets.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html#immune-not-re).

## A simple set is not computable

Its complement would be an infinite
RE set, contradicting immunity.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 5.6.

Formalized by `Cslib.Decidability.simple_not_computable`, a theorem declared in [CSLibExt/Computability/Decidability/SpecialSets.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/SpecialSets.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html#simple-not-computable).

## A simple set is recursively enumerable

**A simple set is recursively enumerable**, by definition.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 5.3.

Formalized by `Cslib.Decidability.simple_re`, a theorem declared in [CSLibExt/Computability/Decidability/SpecialSets.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/SpecialSets.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html#simple-re).

## The complement of a simple set is immune

**The complement of a simple set is immune**, by definition.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 5.3.

Formalized by `Cslib.Decidability.simple_complement_immune`, a theorem declared in [CSLibExt/Computability/Decidability/SpecialSets.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/SpecialSets.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html#simple-complement-immune).

## A creative set is recursively enumerable

**A creative set is recursively enumerable**, by definition.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 5.2.

Formalized by `Cslib.Decidability.creative_re`, a theorem declared in [CSLibExt/Computability/Decidability/SpecialSets.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/SpecialSets.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html#creative-re).

## A creative set is not computable

Its complement is productive, hence
not RE, but the complement of a computable set is RE.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 5.7.

Formalized by `Cslib.Decidability.creative_not_computable`, a theorem declared in [CSLibExt/Computability/Decidability/SpecialSets.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/SpecialSets.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html#creative-not-computable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Productive, creative, simple and immune sets](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/degrees-and-hierarchies/productive-creative-simple-and-immune-sets)
