---
declaration: proposition
origin: cited
lean: Eq1729.enlarge_L₀'
statement: formalized
proof: formalized
---

# Enlarging $L'_0$

Suppose one has a partial solution in which $L'_0 x$ is undefined for some $x \in N$. Then one can extend the partial solution so that $L'_0 x$ is now defined.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By axiom (i”), $L'_0 (R'_0)^n x$ is undefined for every integer $n$. Let $d = E_m$ be a generator of $SM$ that does not appear as a component of any index of any of the generators $e_a$ appearing anywhere in the partial solution; such a $d$ exists due to the finiteness hypotheses. We set $L'_0 x := e_d$, and then extend by [(6)](README.md), [(7)](README.md), thus

$$
L'_0 (R'_0)^n x := (R'_0)^n e_d
$$

and

$$
L'_0 (R'_0)^n e_d := (R'_0)^{n-1} x.
$$

Because of the new nature of $d$, no collisions in the partial function $L_0$ are created by this operation. It is then easy to check that axiom (i”) is preserved by this operation, whereas none of the other axioms (S), (iii”), (iv”), (v”), (vi”), (vii”), (P), (P'), (P”) are affected by this extension. With some effort, axiom (L) can also be verified.

## Lean

Formalized as [`Eq1729.enlarge_L₀'`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1729.enlarge_L₀').

## Sources

- [Equational Theories blueprint: chapter/1729.tex, line 198](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1729.tex#L198)
