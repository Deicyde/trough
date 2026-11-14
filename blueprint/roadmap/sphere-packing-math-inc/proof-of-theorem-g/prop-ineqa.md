---
declaration: proposition
origin: cited
lean: MagicFunction.g.CohnElkies.A_neg
statement: formalized
proof: formalized
---

# ineqA

Consider the function $A:(0,\infty)\to\mathbb{C}$ defined as

$$
A(t):=-t^2\phi_0(i/t)-\frac{36}{\pi^2}\,\psi_I(it).\qquad\text{(1)}
$$

Then

$$
A(t) < 0\qquad\text{(2)}
$$

for all $t > 0$.

## Depends on

- [ineqABnew-equiv](lemma-ineqabnew-equiv.md)
- [F-G-phi-psi-identities](lemma-f-g-phi-psi-identities.md)
- [F-G-pos](lemma-f-g-pos.md)
- [ineqAnew](cor-ineqanew.md)

## Lean

Formalized as [`MagicFunction.g.CohnElkies.A_neg`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.g.CohnElkies.A_neg).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modform-ineq.tex, line 3](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modform-ineq.tex#L3)
