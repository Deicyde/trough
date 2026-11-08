---
declaration: theorem
origin: cited
lean: LinearMap.toMatrix₂_compl₁₂_algebra
statement: formalized
proof: formalized
---

# Algebra-valued pairing matrices

For finite based modules over a commutative semiring
`R` and a semiring `R`-algebra `S`,
[`LinearMap.toMatrix₂_compl₁₂_algebra`](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Free/BilinearMatrix.lean)
expresses composition of an `S`-valued `R`-bilinear map by coefficient-matrix
multiplication after `algebraMap R S`. The target algebra need not be commutative,
finite or projective over `R`; the identity-algebra formula recovers the scalar case.
For integer-bilinear pairings into a linearly ordered commutative ring,
[subgroup-index comparison](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Free/BilinearIndex.lean) scales absolute
Gram determinants by the relative indices of nested free subgroups of equal finite
rank. The ambient groups need not be free or finitely generated, and a one-sided
comparison allows an arbitrary family in the other variable. Empty matrices and
zero determinants are included.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/README.md#headline-results) of [FormalFrontier/projective-modules](https://github.com/FormalFrontier/projective-modules) at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `LinearMap.toMatrix₂_compl₁₂_algebra` (theorem), declared in [ProjectiveModules/Free/BilinearMatrix.lean, line 56](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Free/BilinearMatrix.lean#L56).

Read from the source at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75), without running Lean.

## Sources

- [projective-modules at 27f95a8b: README, headline results](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/README.md#headline-results)
- [Source of `LinearMap.toMatrix₂_compl₁₂_algebra` in ProjectiveModules/Free/BilinearMatrix.lean](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Free/BilinearMatrix.lean#L56)
