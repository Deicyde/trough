---
declaration: theorem
origin: cited
lean: Subgraph.Equation953_implies_Equation2
statement: formalized
proof: formalized
---

# 953 is equivalent to 2

[E953](https://teorth.github.io/equational_theories/implications/?953) $({x = y \diamond ((z \diamond x) \diamond (z \diamond z))})$ is equivalent to [E2](https://teorth.github.io/equational_theories/implications/?2).

## Depends on

- [Equation 953](../selected-laws/part-02/eq953.md)
- [Equation 2](../selected-laws/part-01/eq2.md)

## Proof

It suffices to show that [E953](https://teorth.github.io/equational_theories/implications/?953) implies [E2](https://teorth.github.io/equational_theories/implications/?2). Pick an element $0$ of $G$ and define $1 = 0 \diamond 0$ and $2 = 1 \diamond 1$ (we do not require $0,1,2$ to be distinct). From [E953](https://teorth.github.io/equational_theories/implications/?953) with $x=z=0$ we have

$$
0 = y \diamond 2.
$$

If we then apply [E953](https://teorth.github.io/equational_theories/implications/?953) with $z=1$ we conclude that

$$
x = y \diamond 0
$$

for all $x,y$, from which one concludes $x=x'$ for any $x,x' \in G$, giving [E2](https://teorth.github.io/equational_theories/implications/?2).

## Lean

Formalized as [`Subgraph.Equation953_implies_Equation2`](https://teorth.github.io/equational_theories/docs/find/#doc/Subgraph.Equation953_implies_Equation2).

## Sources

- [Equational Theories blueprint: chapter/implications.tex, line 158](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/implications.tex#L158)
