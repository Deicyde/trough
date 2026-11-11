---
declaration: section
origin: cited
lean: arithFrobConjClass, arithFrobConjClass_mem_carrier, arithFrobConjClass_eq_of_under_eq
statement: formalized
proof: formalized
---

# Conjugacy class of the arithmetic Frobenius at an unramified prime

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/conjugacy-class-of-the-arithmetic-frobenius-at-a/index.html).

## Frobenius conjugacy class

Let $S$ be a commutative algebra over a commutative ring $R$,
and let a finite group $G$ act on $S$ by $R$-algebra automorphisms such that every element of
$S$ fixed by $G$ is the image of an element of $R$. Let $Q$ be a prime of $S$ with $S/Q$ finite
at which $S$ is unramified over $R$ (the localization $S_Q$ is formally unramified over $R$).
The Frobenius conjugacy class at $Q$ is the conjugacy class in $G$ of the chosen arithmetic
Frobenius element $\mathrm{Frob}_Q$ at $Q$: an element $\sigma \in G$ with
$\sigma(x) \equiv x^q \pmod Q$ for all $x \in S$, where $q$ is the number of elements of $R$
modulo the preimage of $Q$ in $R$, chosen so that the elements chosen at primes with the same
preimage in $R$ are conjugate.

Formalized by `arithFrobConjClass`, a definition declared in [MathlibExt/RingTheory/Frobenius/ConjugacyClass.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/ConjugacyClass.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/conjugacy-class-of-the-arithmetic-frobenius-at-a/index.html#arith-frob-conj-class).

## The Frobenius element lies in the Frobenius conjugacy class

Let a finite group $G$ act
on a commutative algebra $S$ over a commutative ring $R$ by $R$-algebra automorphisms such that
every element of $S$ fixed by $G$ is the image of an element of $R$. For every prime $Q$ of $S$
with $S/Q$ finite at which $S$ is unramified over $R$, the chosen arithmetic Frobenius element
$\mathrm{Frob}_Q$ at $Q$ belongs to the Frobenius conjugacy class at $Q$.

Formalized by `arithFrobConjClass_mem_carrier`, a theorem declared in [MathlibExt/RingTheory/Frobenius/ConjugacyClass.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/ConjugacyClass.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/conjugacy-class-of-the-arithmetic-frobenius-at-a/index.html#arith-frob-conj-class-mem-carrier).

## The Frobenius conjugacy class depends only on the prime below

Let a finite group $G$
act on a commutative algebra $S$ over a commutative ring $R$ by $R$-algebra automorphisms such
that every element of $S$ fixed by $G$ is the image of an element of $R$. Let $Q$ and $Q'$ be
primes of $S$ with $S/Q$ and $S/Q'$ finite at which $S$ is unramified over $R$. If $Q$ and $Q'$
have the same preimage in $R$, then the Frobenius conjugacy classes at $Q$ and $Q'$ are
equal.

Formalized by `arithFrobConjClass_eq_of_under_eq`, a theorem declared in [MathlibExt/RingTheory/Frobenius/ConjugacyClass.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/ConjugacyClass.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/conjugacy-class-of-the-arithmetic-frobenius-at-a/index.html#arith-frob-conj-class-eq-of-under-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conjugacy class of the arithmetic Frobenius at an unramified prime](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/conjugacy-class-of-the-arithmetic-frobenius-at-a/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ramification/frobenius-elements/conjugacy-class-of-the-arithmetic-frobenius-at-a)
