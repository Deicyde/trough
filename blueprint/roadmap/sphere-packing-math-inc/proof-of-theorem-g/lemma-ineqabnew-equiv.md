---
declaration: lemma
origin: cited
lean: MagicFunction.g.CohnElkies.A, MagicFunction.g.CohnElkies.B
statement: formalized
proof: formalized
---

# ineqABnew-equiv

Inequality [(2)](prop-ineqa.md) and [(4)](prop-ineqb.md) are equivalent to

$$
\begin{aligned}
F(it) + \frac{18}{\pi^2} G(it) > 0\qquad\text{(9)}\\
F(it) - \frac{18}{\pi^2} G(it) > 0\qquad\text{(10)}\end{aligned}
$$

respectively.

## Depends on

- [F-G-phi-psi-identities](lemma-f-g-phi-psi-identities.md)
- [psiI-psiT-psiS](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/def-psii-psit-psis.md)
- [disc-pos](../modular-forms/part-02/cor-disc-pos.md)

## Proof

By [(25)](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/def-psii-psit-psis.md),

$$
\psi_I(it) = (\psi_S|_{-2}S)(it) = (it)^{2}\psi_S\left(-\frac{1}{it}\right) = -t^2 \psi_S\left(\frac{i}{t}\right).
$$

Combined with Lemma [F-G-phi-psi-identities](lemma-f-g-phi-psi-identities.md) we can rewrite [(2)](prop-ineqa.md) as

$$
A(t) = -t^2 \phi_0\left(\frac{i}{t}\right) + \frac{36}{\pi^2} \psi_S\left(\frac{i}{t}\right) < 0 \Leftrightarrow \frac{F(it)}{\Delta(it)} + \frac{18}{\pi^2} \frac{G(it)}{\Delta(it)} > 0
$$

for $t > 0$, which is equivalent to (9) by Corollary [disc-pos](../modular-forms/part-02/cor-disc-pos.md). Equivalences of [(4)](prop-ineqb.md) and (10) follows similarly; just change the sign.

## Lean

Formalized as [`MagicFunction.g.CohnElkies.A`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.g.CohnElkies.A), [`MagicFunction.g.CohnElkies.B`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.g.CohnElkies.B).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modform-ineq.tex, line 56](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modform-ineq.tex#L56)
