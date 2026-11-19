---
declaration: theorem
origin: cited
lean: groupCohomology.trivialCohomology_of_even_of_odd
statement: formalized
---

# triviality criterion

Let $M$ be a representation of a finite group $G$ (no longer assumed to be solvable). Suppose we have positive natural numbers $e$ and $o$ with $e$ even and $o$ odd, such that for all subgroups $S$ of $G$ we have

$$
H^e(S,M) =0, \qquad H^o(S,M) = 0.
$$

Then $M$ has trivial cohomology.

## Depends on

- [triviality criterion solvable](thm-triviality-criterion-solvable.md)

## Proof

Let $S$ be a subgroup of $G$. Fix a prime number $p$ and let $S_p$ be a Sylow $p$-subgroup of $S$. Since $S_p$ is solvable, [triviality criterion solvable](thm-triviality-criterion-solvable.md) implies that $H^n(S_p,M) \cong 0$ for all $n > 0$. By [cohomology sub Sylow](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1483), it follows that $H^n(S,M)[p^\infty] \cong 0$. Since this holds for all primes $p$, [cohomology G-torsion](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1464) implies that $H^n(S,M) \cong 0$.

## Lean

Stated as [`groupCohomology.trivialCohomology_of_even_of_odd`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.trivialCohomology_of_even_of_odd); the blueprint marks no proof of it as formalized.

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1807](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1807)
