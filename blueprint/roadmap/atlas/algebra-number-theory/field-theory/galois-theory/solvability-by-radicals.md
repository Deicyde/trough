---
declaration: section
origin: cited
lean: GaloisTheory.not_solvableByRad_of_gal_iso_perm, GaloisTheory.not_solvableByRad_of_gal_iso_S5, MathlibExt.Algebra.AbelRuffiniWanted.abel_ruffini, MathlibExt.Algebra.SolvableByRadicalsWanted.Algebra.solvable_iff_solvableByRad
statement: formalized
---

# Solvability by radicals

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/solvability-by-radicals/index.html).

## Abel–Ruffini, contrapositive form

Let $F$ be a field, let $E$ be a field extension of $F$,
and let $n \ge 5$. If $p \in F[X]$ is irreducible and the Galois group of $p$ over $F$ is isomorphic
to the symmetric group $S_n$, then no root of $p$ in $E$ is solvable by radicals over $F$.

Formalized by `GaloisTheory.not_solvableByRad_of_gal_iso_perm`, a theorem declared in [MathlibExt/FieldTheory/Galois/NotSolvableByRadicals.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Galois/NotSolvableByRadicals.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/solvability-by-radicals/index.html#not-solvable-by-rad-of-gal-iso-perm).

## Abel–Ruffini for $S_5$

Let $F$ be a field and let $E$ be a field extension of $F$. If
$p \in F[X]$ is irreducible and the Galois group of $p$ over $F$ is isomorphic to the symmetric
group $S_5$, then no root of $p$ in $E$ is solvable by radicals over $F$.

Formalized by `GaloisTheory.not_solvableByRad_of_gal_iso_S5`, a theorem declared in [MathlibExt/FieldTheory/Galois/NotSolvableByRadicals.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Galois/NotSolvableByRadicals.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/solvability-by-radicals/index.html#not-solvable-by-rad-of-gal-iso-s5).

## Abel–Ruffini theorem

Let $n \ge 1$ be a natural number. Every complex root of every
polynomial with rational coefficients of degree exactly $n$ is expressible by radicals over
$\mathbb{Q}$ if and only if $n \le 4$. Here a complex number is expressible by radicals over
$\mathbb{Q}$ when it lies in the smallest subfield $S$ of $\mathbb{C}$ such that $z \in S$
whenever $z \in \mathbb{C}$ and $z^k \in S$ for some integer $k \ge 1$.

The direction from radical solvability to $n \le 4$ is the classical insolvability of the
general quintic, extended to higher degrees; the converse follows from the explicit formulas
of Cardano and Ferrari for degrees at most four.

## Sources

- P. Ruffini (1799), N. H. Abel (1824), É. Galois (1832). Listed as §57 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf); the general-quintic insolvability is #16 on Freek Wiedijk's *Formalizing 100 Theorems* list (https://www.cs.ru.nl/~freek/100/). Problem `abel_ruffini` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Algebra.AbelRuffiniWanted.abel_ruffini` is written with `theorem_wanted` in [WantedExt/Algebra/AbelRuffiniWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/AbelRuffiniWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/solvability-by-radicals/index.html#abel-ruffini).

## Solvable extensions ↔ solvable groups

Let $F$ be a field of characteristic zero and let
$p \in F[X]$ be a nonzero polynomial. Every root of $p$ in an algebraic closure $\overline{F}$ of
$F$ is solvable by radicals over $F$ (obtainable from $F$ by field operations and $n$-th roots
inside $\overline{F}$) if and only if the Galois group of $p$ over $F$ is solvable.

## Sources

- É. Galois (1832); the iff appears in standard texts such as Stewart, *Galois Theory* (Theorem 18.10); Lang, *Algebra* (VI §7); Rotman, *Galois Theory* (Theorem 73). Listed as §58 (additional statement 2) in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `solvable_by_radicals_converse` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Algebra.SolvableByRadicalsWanted.Algebra.solvable_iff_solvableByRad` is written with `theorem_wanted` in [WantedExt/Algebra/SolvableByRadicalsWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/SolvableByRadicalsWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/solvability-by-radicals/index.html#solvable-iff-solvable-by-rad).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Solvability by radicals](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/solvability-by-radicals/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/FieldTheory/galois-theory/solvability-by-radicals)
