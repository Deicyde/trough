---
declaration: theorem
origin: cited
lean: Module.determinant_tensorProduct_map, Module.rankPower_tensorProduct
statement: formalized
proof: formalized
---

# Tensor-product determinants and rank powers

For finite projective R-modules P and Q over a commutative ring R, det(f ⊗ g) = rankPower_Q(det(f)) · rankPower_P(det(g)) for all endomorphisms f of P and g of Q, and the rank-power map of P ⊗ Q is rankPower_P ∘ rankPower_Q.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/formalization.yaml) of [FormalFrontier/projective-modules](https://github.com/FormalFrontier/projective-modules) at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.determinant_tensorProduct_map` (theorem), declared in [ProjectiveModules/ExteriorPower/DeterminantLine/Tensor.lean, line 46](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/DeterminantLine/Tensor.lean#L46).
- `Module.rankPower_tensorProduct` (theorem), declared in [ProjectiveModules/ExteriorPower/DeterminantLine/Tensor.lean, line 97](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/DeterminantLine/Tensor.lean#L97).

Read from the source at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75), without running Lean.

## Sources

- [projective-modules at 27f95a8b: formalization.yaml](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/formalization.yaml)
- [Source of `Module.determinant_tensorProduct_map` in ProjectiveModules/ExteriorPower/DeterminantLine/Tensor.lean](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/DeterminantLine/Tensor.lean#L46)
- [Source of `Module.rankPower_tensorProduct` in ProjectiveModules/ExteriorPower/DeterminantLine/Tensor.lean](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/DeterminantLine/Tensor.lean#L97)
