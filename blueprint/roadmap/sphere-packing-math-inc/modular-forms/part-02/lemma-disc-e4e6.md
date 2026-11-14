---
declaration: lemma
origin: cited
lean: Delta_E4_eqn
statement: formalized
proof: formalized
---

# disc-E4E6

We have

$$
\Delta(z) = (E_4^3-E_6^2)/1728.
$$

## Depends on

- [disc-definition](../part-01/def-disc-definition.md)

## Proof

We only need to show its a cuspform, since once we have this, dividing the rhs by $\Delta$ would give a modular form of weight $0$ which is a constant, and so we can determine the constant easily.

To check its a cuspform, we just look at the $q$-expansions of $E_4$ and $E_6$ and prove directly that the first term vanishes.

## Lean

Formalized as [`Delta_E4_eqn`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Delta_E4_eqn).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 223](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L223)
