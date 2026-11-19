---
declaration: definition
origin: cited
lean: SubgroupTestValue.SofValueApproximable
statement: formalized
---

# Approximating the sofic value

The sofic value is approximable when a computable function $f$ of a test $T$ and $k \in \mathbb{N}$ satisfies $|\mathrm{val}_{\mathrm{sof}}(T) - f(T, k)/(k+1)| \leq 1/(k+1)$ for all $T$ and $k$.

## Depends on

- [Subgroup tests and their sofic value; I:439–520](def-subgroup-test.md)

## Lean

Formalized as [`SubgroupTestValue.SofValueApproximable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.SofValueApproximable).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 49](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L49)
