---
declaration: theorem
origin: cited
lean: Module.injective_of_nondegenerate_mul
statement: formalized
proof: formalized
---

# Frobenius functionals and self-injectivity

For a finite-dimensional algebra `A` over a field `K`,
[`Module.injective_of_nondegenerate_mul`](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/Injective/Frobenius.lean)
proves `Module.Injective A A` from a given linear functional
`l : A →ₗ[K] K` whose multiplication pairing `l (x * y)` is nondegenerate.
The algebra may be noncommutative, the scalar and algebra universes are independent,
and no normalization such as `l 1 = 1` is required. The resulting injectivity applies
to arbitrary left modules, without finiteness or common-universe assumptions.
This is conditional on the functional, not a construction of one.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/README.md#headline-results) of [FormalFrontier/projective-modules](https://github.com/FormalFrontier/projective-modules) at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.injective_of_nondegenerate_mul` (theorem), declared in [ProjectiveModules/Module/Injective/Frobenius.lean, line 55](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/Injective/Frobenius.lean#L55).

Read from the source at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75), without running Lean.

## Sources

- [projective-modules at 27f95a8b: README, headline results](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/README.md#headline-results)
- [Source of `Module.injective_of_nondegenerate_mul` in ProjectiveModules/Module/Injective/Frobenius.lean](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/Injective/Frobenius.lean#L55)
