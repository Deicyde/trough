---
declaration: lemma
origin: cited
lean: ModularForm.eta_comp_eq_csqrt_I_inv
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

Formalized as [`ModularForm.eta_comp_eq_csqrt_I_inv`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ModularForm.eta_comp_eq_csqrt_I_inv).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 209](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L209)
