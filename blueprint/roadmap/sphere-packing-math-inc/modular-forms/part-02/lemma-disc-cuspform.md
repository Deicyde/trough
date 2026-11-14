---
declaration: lemma
origin: cited
lean: Delta
statement: formalized
proof: formalized
---

# disc-cuspform

$\Delta(z) \in M_{12}(\Gamma_1)$. Especially, we have

$$
\Delta\left(-\frac{1}{z}\right) = z^{12} \Delta(z).\qquad\text{(8)}
$$

Also, it vanishes at the unique cusp, i.e. it is a cusp form of level $\Gamma_1$ and weight $12$.

## Depends on

- [disc-definition](../part-01/def-disc-definition.md)
- [dedekind_eta_transformation](lemma-dedekind-eta-transformation.md)

## Proof

The fact that it is invariant under translation is clear from the definition, so we only need to check transformation under $S$. Now, note that $\eta^{24} = \Delta$, and from [dedekind_eta_transformation](lemma-dedekind-eta-transformation.md) we have $\eta(-1/z) = \sqrt{-iz} \eta(z)$, so $\Delta(-1/z) = z^{12} \Delta(z)$ as required.

## Lean

Formalized as [`Delta`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Delta).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 209](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L209)
