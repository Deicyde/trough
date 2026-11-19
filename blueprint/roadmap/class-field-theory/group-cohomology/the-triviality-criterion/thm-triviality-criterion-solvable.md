---
declaration: theorem
origin: cited
lean: groupCohomology.trivialCohomology_of_even_of_odd_of_solvable
statement: formalized
---

# triviality criterion solvable

Let $M$ be a representation of a finite solvable group $G$ (note that the solvability condition will be removed in the next theorem). Suppose we have positive natural numbers $e$ and $o$ with $e$ even and $o$ odd, such that for all subgroups $S$ of $G$ we have

$$
H^e(S,M) \cong 0, \qquad H^o(S,M) \cong 0.
$$

Then $M$ has trivial cohomology.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We must prove that $H^{n}(S,M) = 0$ for all $S$ and all $n > 0$. We'll prove this by induction on $S$. The result is true for the trivial subgroup of $G$. Assume that the result is true for $S$, and assume that $S' / S$ is cyclic. The inductive hypothesis implies that (for all $n$) the inflation restriction sequence is exact:

$$
0 \to H^{n} (S'/S, M^S) \to H^{n}(S' , M) \to H^{n}(S,M)= 0.
$$

We therefore have isomorphisms $H^{n} (S'/S, M^S) \cong H^{n}(S' , M)$. In particular we have $H^{e} (S'/S, M^S) \cong 0$ and $H^{o} (S'/S, M^S) \cong 0$. Using periodicity of the cohomology of a cyclic group, we have $H^{n}(S'/S,M^S) \cong 0$ for all $n>0$.

## Lean

Stated as [`groupCohomology.trivialCohomology_of_even_of_odd_of_solvable`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.trivialCohomology_of_even_of_odd_of_solvable); the blueprint marks no proof of it as formalized.

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1780](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1780)
