---
declaration: lemma
origin: cited
lean: CuspForm.discriminant
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

- [disc-definition](def-disc-definition.md)
- [dedekind_eta_transformation](lemma-dedekind-eta-transformation.md)

## Proof

The fact that it is invariant under translation is clear from the definition, so we only need to check transformation under $S$. Now, note that $\eta^{24} = \Delta$, and from [dedekind_eta_transformation](lemma-dedekind-eta-transformation.md) we have $\eta(-1/z) = \sqrt{-iz} \eta(z)$, so $\Delta(-1/z) = z^{12} \Delta(z)$ as required.

## Lean

Formalized as [`CuspForm.discriminant`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/CuspForm.discriminant).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 224](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L224)
