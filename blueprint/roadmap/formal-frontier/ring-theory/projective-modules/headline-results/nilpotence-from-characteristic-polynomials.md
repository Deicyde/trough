---
declaration: theorem
origin: cited
lean: Module.isNilpotent_of_isNilpotent_charpoly_sub_charpoly_zero
statement: formalized
proof: formalized
---

# Nilpotence from characteristic polynomials

For a finite projective module
over any commutative ring,
[`Module.isNilpotent_of_isNilpotent_charpoly_sub_charpoly_zero`](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/LinearAlgebra/Charpoly/CayleyHamilton/Nilpotent.lean)
shows that a nilpotent difference between the characteristic polynomials of an
endomorphism and zero forces the endomorphism to be nilpotent. Equality is a
special case. The underlying
[`Module.charpoly_zero_dvd_X_pow`](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/LinearAlgebra/Charpoly/MonicMultiple.lean)
needs no constant-rank, faithfulness or global-monicity assumption. The given
module action and independent universes are retained; the `LinearMap` corollary
agrees with the ordinary characteristic polynomial on finite free modules.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/README.md#headline-results) of [FormalFrontier/projective-modules](https://github.com/FormalFrontier/projective-modules) at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.isNilpotent_of_isNilpotent_charpoly_sub_charpoly_zero` (theorem), declared in [ProjectiveModules/LinearAlgebra/Charpoly/CayleyHamilton/Nilpotent.lean, line 40](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/LinearAlgebra/Charpoly/CayleyHamilton/Nilpotent.lean#L40).

Read from the source at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75), without running Lean.

## Sources

- [projective-modules at 27f95a8b: README, headline results](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/README.md#headline-results)
- [Source of `Module.isNilpotent_of_isNilpotent_charpoly_sub_charpoly_zero` in ProjectiveModules/LinearAlgebra/Charpoly/CayleyHamilton/Nilpotent.lean](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/LinearAlgebra/Charpoly/CayleyHamilton/Nilpotent.lean#L40)
