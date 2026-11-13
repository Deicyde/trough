---
declaration: section
origin: cited
lean: Nat.sq_mod_eight, Nat.not_isSquare_of_mod_eight_eq_three, Nat.not_isSquare_of_mod_eight_eq_six, Nat.not_isSquare_sub_sq_of_mod_eight_eq_six, Nat.sq_mod_sixteen_of_odd, Int.sq_emod_eight
statement: formalized
proof: formalized
---

# Squares modulo powers of two

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/squares-modulo-powers-of-two/index.html).

## Squares of natural numbers

## Squares of natural numbers modulo 8

For every natural number $r$, the remainder of $r^2$
on division by $8$ is $0$, $1$ or $4$.

Formalized by `Nat.sq_mod_eight`, a theorem declared in [MathlibExt/NumberTheory/SquareModEight.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SquareModEight.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/squares-modulo-powers-of-two/index.html#sq-mod-eight).

## Numbers congruent to 3 mod 8 are not squares

If a natural number $n$ satisfies
$n \equiv 3 \pmod 8$, then $n$ is not the square of a natural number.

Formalized by `Nat.not_isSquare_of_mod_eight_eq_three`, a theorem declared in [MathlibExt/NumberTheory/SquareModEight.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SquareModEight.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/squares-modulo-powers-of-two/index.html#not-is-square-of-mod-eight-eq-three).

## Numbers congruent to 6 mod 8 are not squares

If a natural number $n$ satisfies
$n \equiv 6 \pmod 8$, then $n$ is not the square of a natural number.

Formalized by `Nat.not_isSquare_of_mod_eight_eq_six`, a theorem declared in [MathlibExt/NumberTheory/SquareModEight.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SquareModEight.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/squares-modulo-powers-of-two/index.html#not-is-square-of-mod-eight-eq-six).

## A number that is 6 mod 8 minus a smaller square is not a square

Let $N$ and $k$ be
natural numbers with $N \equiv 6 \pmod 8$ and $k^2 < N$. Then $N - k^2$ is not the square of a
natural number.

Formalized by `Nat.not_isSquare_sub_sq_of_mod_eight_eq_six`, a theorem declared in [MathlibExt/NumberTheory/SquareModEight.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SquareModEight.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/squares-modulo-powers-of-two/index.html#not-is-square-sub-sq-of-mod-eight-eq-six).

## Odd squares modulo 16

For every odd natural number $k$, either $k^2 \equiv 1 \pmod{16}$
and $k \equiv 1$ or $7 \pmod 8$, or $k^2 \equiv 9 \pmod{16}$ and $k \equiv 3$ or $5 \pmod 8$.

Formalized by `Nat.sq_mod_sixteen_of_odd`, a theorem declared in [MathlibExt/NumberTheory/SquareModEight.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SquareModEight.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/squares-modulo-powers-of-two/index.html#sq-mod-sixteen-of-odd).

## Squares of integers modulo 8

For every integer $x$, the remainder of $x^2$ on division
by $8$, taken in $\{0, 1, \dots, 7\}$, is $0$, $1$ or $4$.

Formalized by `Int.sq_emod_eight`, a theorem declared in [MathlibExt/NumberTheory/SquareModEight.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SquareModEight.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/squares-modulo-powers-of-two/index.html#sq-emod-eight).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Squares modulo powers of two](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/squares-modulo-powers-of-two/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/power-residues-reciprocity/squares-modulo-powers-of-two)
