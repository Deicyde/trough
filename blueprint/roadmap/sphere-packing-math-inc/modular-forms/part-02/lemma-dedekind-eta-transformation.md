---
declaration: lemma
origin: cited
lean: eta_equality
statement: formalized
proof: formalized
---

# dedekind_eta_transformation

The Dedekind eta function transforms as

$$
\eta\left(-\frac{1}{z}\right) = \sqrt{-iz} \eta(z).
$$

## Depends on

- [dedekind_eta](def-dedekind-eta.md)

## Proof

Consider the logarithmic derivative of $\eta$, which one can easily see is equal to $\frac{\pi i}{12} E_2$. The result then follows from the transformation of $E_2$.

See (first course, proposition 1.2.5).

## Lean

Formalized as [`eta_equality`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/eta_equality).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 195](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L195)
