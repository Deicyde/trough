---
declaration: proposition
origin: cited
lean: MagicFunction.g.CohnElkies.B_pos
statement: formalized
proof: formalized
---

# ineqB

Consider the function $B:(0,\infty)\to\mathbb{C}$ defined as

$$
B(t) := -t^2\phi_0(i/t)+\frac{36}{\pi^2}\,\psi_I(it)\qquad\text{(3)}
$$

Then

$$
B(t) > 0\qquad\text{(4)}
$$

for all $t > 0$.

## Depends on

- [ineqABnew-equiv](lemma-ineqabnew-equiv.md)
- [F-G-phi-psi-identities](lemma-f-g-phi-psi-identities.md)
- [ineqBnew](cor-ineqbnew.md)

## Lean

Formalized as [`MagicFunction.g.CohnElkies.B_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.g.CohnElkies.B_pos).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modform-ineq.tex, line 18](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modform-ineq.tex#L18)
