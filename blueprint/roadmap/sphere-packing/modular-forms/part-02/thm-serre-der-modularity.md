---
declaration: theorem
origin: cited
lean: Derivative.serreDerivativeMF, Derivative.serreDerivative_slash_invariant
statement: formalized
proof: formalized
---

# serre-der-modularity

Let $F$ be a modular form of weight $k$ and level $\Gamma$. Then, $\partial_{k}F$ is a modular form of weight $k + 2$ of the same level.

## Depends on

- [serre-der](def-serre-der.md)
- [Mk](../part-01/def-mk.md)
- [serre-der-equiv-action](thm-serre-der-equiv-action.md)

## Proof

Immediate from Theorem [serre-der-equiv-action](thm-serre-der-equiv-action.md) since $F|_k\gamma = F$ for all $\gamma \in \Gamma$.

## Lean

Formalized as [`Derivative.serreDerivativeMF`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Derivative.serreDerivativeMF), [`Derivative.serreDerivative_slash_invariant`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Derivative.serreDerivative_slash_invariant).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 618](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L618)
