---
declaration: lemma
origin: cited
lean: Eq1729.L', Eq1729.L'_0_eq_L₀'
statement: formalized
proof: formalized
---

# Using $L'_0$ to construct $L'_a$

Suppose we have a bijection $L'_0: N \to N$ that satisfies axiom (i'), and then define $L'_a$ for all $a \in SM$ by the formula [(4)](README.md). Then this recovers $L'_0$ when $a=0$ (to formalize this it may be convenient to give $L'_0$ and $L'_a$ distinct names), and the $L'_a$ are all bijections and satisfy axiom (i). Furthermore, we have

$$
(L'_a)^{-1} := (R'_{2a})^{-1} L'_0 R'_0 R'_{a}\qquad\text{(5)}
$$

for all $a \in SM$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Routine verification.

## Lean

Formalized as [`Eq1729.L'`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1729.L'), [`Eq1729.L'_0_eq_L₀'`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1729.L'_0_eq_L₀').

## Sources

- [Equational Theories blueprint: chapter/1729.tex, line 115](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/1729.tex#L115)
