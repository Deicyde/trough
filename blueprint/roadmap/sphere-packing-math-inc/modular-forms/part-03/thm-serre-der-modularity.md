---
declaration: theorem
origin: cited
lean: serre_D_slash_invariant
statement: formalized
proof: formalized
---

# serre-der-modularity

Let $F$ be a modular form of weight $k$ and level $\Gamma$. Then, $\partial_{k}F$ is a modular form of weight $k + 2$ of the same level.

## Depends on

- [serre-der](def-serre-der.md)
- [holomorphic-modular-form](../part-01/def-holomorphic-modular-form.md)
- [serre-der-equiv-action](thm-serre-der-equiv-action.md)

## Proof

Immediate from Theorem [serre-der-equiv-action](thm-serre-der-equiv-action.md) since $F|_k\gamma = F$ for all $\gamma \in \Gamma$.

## Lean

Formalized as [`serre_D_slash_invariant`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/serre_D_slash_invariant).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 595](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L595)
