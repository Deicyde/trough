---
declaration: section
origin: cited
lean: Ideal.stabilizer_eq_bot_iff_ncard_primesOver_eq_card, arithFrobAt_eq_one_iff_ncard_primesOver_eq_card_of_generates, arithFrobAt_generates_stabilizer_of_isUnramifiedAt, arithFrobAt_eq_one_iff_ncard_primesOver_eq_card
statement: formalized
proof: formalized
---

# Frobenius elements and complete splitting

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/frobenius-elements-and-complete-splitting/index.html).

## Splits Completely

## Trivial decomposition group and the number of primes above

Let $B$ be a commutative
algebra over a commutative ring $A$, and let a finite group $G$ act on $B$ by $A$-algebra
automorphisms such that every element of $B$ fixed by $G$ is the image of an element of $A$. Let
$p$ be an ideal of $A$ and $P$ a prime of $B$ lying over $p$. Then the stabilizer of $P$ in $G$
(the decomposition group of $P$) is trivial if and only if the number of primes of $B$ lying
over $p$ equals the order of $G$.

Formalized by `Ideal.stabilizer_eq_bot_iff_ncard_primesOver_eq_card`, a theorem declared in [MathlibExt/RingTheory/Frobenius/Splitting.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Frobenius/Splitting.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/frobenius-elements-and-complete-splitting/index.html#stabilizer-eq-bot-iff-ncard-primes-over).

## Trivial Frobenius and the number of primes above, assuming the Frobenius generates

Let $B$ be a commutative algebra over a commutative ring $A$, and let a finite group $G$ act on
$B$ by $A$-algebra automorphisms such that every element of $B$ fixed by $G$ is the image of an
element of $A$. Let $p$ be an ideal of $A$ and $P$ a prime of $B$ lying over $p$ with $B/P$
finite, and let $\mathrm{Frob}_P \in G$ be the chosen arithmetic Frobenius element at $P$, an
element $\sigma \in G$ with $\sigma(x) \equiv x^q \pmod P$ for all $x \in B$, where $q$ is the
number of elements of $A/p$. Suppose every element of the stabilizer of $P$ in $G$ equals
$\mathrm{Frob}_P^n$ for some natural number $n$. Then $\mathrm{Frob}_P = 1$ if and only if the
number of primes of $B$ lying over $p$ equals the order of $G$.

Formalized by `arithFrobAt_eq_one_iff_ncard_primesOver_eq_card_of_generates`, a theorem declared in [MathlibExt/RingTheory/Frobenius/Splitting.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Frobenius/Splitting.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/frobenius-elements-and-complete-splitting/index.html#arith-frob-at-eq-one-iff-ncard-primes-ov).

## The Frobenius element generates the decomposition group at an unramified prime

Let $A$
and $B$ be integral domains with $B$ a finite flat $A$-algebra, and let $G$ be a finite group
acting faithfully on $B$ by $A$-algebra automorphisms such that every element of $B$ fixed by
$G$ is the image of an element of $A$. Let $p$ be a prime of $A$ and $P$ a prime of $B$ lying
over $p$, with $B/P$ finite and $B$ unramified over $A$ at $P$ (the localization $B_P$ is
formally unramified over $A$). Let $\mathrm{Frob}_P \in G$ be the chosen arithmetic Frobenius
element at $P$, an element $\sigma \in G$ with $\sigma(x) \equiv x^q \pmod P$ for all
$x \in B$, where $q$ is the number of elements of $A/p$. Then every element of the stabilizer of
$P$ in $G$ (the decomposition group of $P$) equals $\mathrm{Frob}_P^n$ for some natural
number $n$.

Formalized by `arithFrobAt_generates_stabilizer_of_isUnramifiedAt`, a theorem declared in [MathlibExt/RingTheory/Frobenius/Splitting.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Frobenius/Splitting.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/frobenius-elements-and-complete-splitting/index.html#arith-frob-at-generates-stabilizer-of-is).

## The Frobenius element is trivial iff the prime splits completely

Let $A$ and $B$ be
integral domains with $B$ a finite flat $A$-algebra, and let $G$ be a finite group acting
faithfully on $B$ by $A$-algebra automorphisms such that every element of $B$ fixed by $G$ is
the image of an element of $A$. Let $p$ be a prime of $A$ and $P$ a prime of $B$ lying over $p$,
with $B/P$ finite and $B$ unramified over $A$ at $P$ (the localization $B_P$ is formally
unramified over $A$). Let $\mathrm{Frob}_P \in G$ be the chosen arithmetic Frobenius element at
$P$, an element $\sigma \in G$ with $\sigma(x) \equiv x^q \pmod P$ for all $x \in B$, where $q$
is the number of elements of $A/p$. Then $\mathrm{Frob}_P = 1$ if and only if the number of
primes of $B$ lying over $p$ equals the order of $G$.

Formalized by `arithFrobAt_eq_one_iff_ncard_primesOver_eq_card`, a theorem declared in [MathlibExt/RingTheory/Frobenius/Splitting.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Frobenius/Splitting.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/frobenius-elements-and-complete-splitting/index.html#arith-frob-at-eq-one-iff-ncard-primes-ov-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Frobenius elements and complete splitting](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/frobenius-elements-and-complete-splitting/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/ramification/frobenius-elements/frobenius-elements-and-complete-splitting)
