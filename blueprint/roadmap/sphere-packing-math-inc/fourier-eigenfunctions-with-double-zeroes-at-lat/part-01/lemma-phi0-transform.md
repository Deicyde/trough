---
declaration: lemma
origin: cited
lean: φ₀_periodic, φ₀_S_transform
statement: formalized
proof: formalized
---

# phi0-transform

We have

$$
\begin{aligned}
\phi_0(z + 1) &= \phi_0(z)\qquad\text{(6)}\\
\phi_0\left(-\frac{1}{z}\right) &= \phi_0(z)-\frac{12i}{\pi}\,\frac{1}{z}\,\phi_{-2}(z)-\frac{36}{\pi^2}\,\frac{1}{z^2}\,\phi_{-4}(z).\qquad\text{(7)}\end{aligned}
$$

## Depends on

- [phi4-phi2-phi0](def-phi4-phi2-phi0.md)
- [Ek-is-modular-form](../../modular-forms/part-01/lemma-ek-is-modular-form.md)
- [E2-transform-S](../../modular-forms/part-01/lemma-e2-transform-s.md)
- [disc-cuspform](../../modular-forms/part-02/lemma-disc-cuspform.md)

## Proof

(6) easily follows from periodicity of Eisenstein series and $\Delta(z)$. For (7),

$$
\begin{aligned}
\phi_{0}\left(-\frac{1}{z}\right) &= \frac{(E_2(-1/z) E_4(-1/z) - E_6(-1/z))^{2}}{\Delta(-1/z)} \\
&= \frac{((z^2 E_2(z) - 6iz / \pi) \cdot z^4 E_4(z) - z^6 E_6(z))^{2}}{z^{12} \Delta(z)} \\
&= \frac{\left(E_2(z) E_4(z) - E_6(z) - \frac{6i}{\pi z} E_4(z)\right)^2}{\Delta(z)} \\
&= \frac{(E_2(z) E_4(z) - E_6(z))^{2} - \frac{12i}{\pi z}(E_2(z) E_4(z) - E_6(z)) E_4(z) - \frac{36}{\pi^2 z^2} E_4(z)^{2}}{\Delta(z)} \\
&= \phi_0(z) - \frac{12 i}{\pi z} \phi_{-2}(z) - \frac{36}{\pi^2 z^2} \phi_{-4}(z).
\end{aligned}
$$

## Lean

Formalized as [`φ₀_periodic`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/φ₀_periodic), [`φ₀_S_transform`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/φ₀_S_transform).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/construct-a-b.tex, line 42](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L42)
