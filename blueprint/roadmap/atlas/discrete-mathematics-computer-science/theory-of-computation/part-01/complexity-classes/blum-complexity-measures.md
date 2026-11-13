---
declaration: section
origin: cited
lean: Cslib.Decidability.BlumMeasure, Cslib.Decidability.BlumClass, Cslib.Decidability.BlumClass.mono, Cslib.Decidability.blumClass_iff
statement: formalized
proof: formalized
---

# Blum complexity measures

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/blum-complexity-measures/index.html).

## Blum complexity measure

A Blum measure $\Phi$ assigns to every program $c$ and input
$n \in \mathbb{N}$ a partially defined cost $\Phi_c(n) \in \mathbb{N}$ satisfying Blum's two axioms:
$\Phi_c(n)$ is defined exactly when program $c$ halts on input $n$, and the relation
$\Phi_c(n) = m$ between $c$, $n$ and $m$ is decidable.

## Sources

- Blum, "A machine-independent theory of the complexity of recursive functions", *Journal of the ACM* 14 (1967), 322–336, Definition 1.

Formalized by `Cslib.Decidability.BlumMeasure`, a structure declared in [CSLibExt/Computability/Decidability/Blum.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Blum.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/blum-complexity-measures/index.html#blum-measure).

## Blum complexity class

Given a Blum measure $\Phi$ and a function $t$ from $\mathbb{N}$ to
$\mathbb{N}$, the Blum class of $t$ consists of the partial functions $f$ from $\mathbb{N}$ to
$\mathbb{N}$ that are computed by some program $c$ whose cost $\Phi_c(n)$ is defined and at most
$t(n)$ for all but finitely many inputs $n$.

The bound is not required at every input: Blum's classes are defined up to finite exceptions,
and the finite exceptions are essential to the gap and union theorems (a program may be slow on
finitely many inputs without leaving the class).

## Sources

- Blum, "A machine-independent theory of the complexity of recursive functions", *Journal of the ACM* 14 (1967), 322–336, Definition 2.

Formalized by `Cslib.Decidability.BlumClass`, a definition declared in [CSLibExt/Computability/Decidability/Blum.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Blum.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/blum-complexity-measures/index.html#blum-class).

## Blum classes are monotone in the bound

If `t` is eventually
dominated by `t'`, every function in the `t`-class is in the `t'`-class.

## Sources

- Blum, "A machine-independent theory of the complexity of recursive functions", *Journal of the ACM* 14 (1967), 322–336, Definition 2.

Formalized by `Cslib.Decidability.BlumClass.mono`, a theorem declared in [CSLibExt/Computability/Decidability/Blum.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Blum.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/blum-complexity-measures/index.html#mono).

## Blum classes via an explicit threshold

Let $\Phi$ be a Blum measure, $t$ a function from
$\mathbb{N}$ to $\mathbb{N}$ and $f$ a partial function from $\mathbb{N}$ to $\mathbb{N}$. Then $f$
lies in the Blum class of $t$ with respect to $\Phi$ if and only if there are a program $c$ that
computes $f$ and a threshold $N$ such that for every input $n \ge N$ the cost $\Phi_c(n)$ is
defined and at most $t(n)$.

## Sources

- Blum, "A machine-independent theory of the complexity of recursive functions", *Journal of the ACM* 14 (1967), 322–336, Definition 2.

Formalized by `Cslib.Decidability.blumClass_iff`, a theorem declared in [CSLibExt/Computability/Decidability/Blum.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Blum.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/blum-complexity-measures/index.html#blum-class-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Blum complexity measures](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/blum-complexity-measures/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/complexity-classes/blum-complexity-measures)
