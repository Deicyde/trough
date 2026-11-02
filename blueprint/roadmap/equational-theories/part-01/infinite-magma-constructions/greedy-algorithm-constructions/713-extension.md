---
declaration: lemma
origin: cited
lean: Eq1722.Greedy.lift
statement: formalized
---

# 713 extension

Suppose that $\diamond$ is a partial solution, and $a \diamond b$ is currently undefined. Then there exists an extension $\diamond'$ of $\diamond$ for which $a \diamond' b$ is defined.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

First suppose that $a \diamond a$ is not defined. Set $a_0 := a$ and select three new elements $a_1,a_2,a_3$. Define $a_0 \diamond a_0 = a_1$, $a_1 \diamond a_0 = a_2$, $a_0 \diamond a_2 = a_3$, $a_0 \diamond a_1 = a_3$, $a_0 \diamond a_3 = a_0$. It is a routine but tedious matter to check that Laws 1,2,3 are preserved by these operations. (The trickiest case is the $x=a_0$ case of Law 1; here we need Law 2 to prevent $y \diamond a_0$ from equalling $a_0$.)

Now suppose that $a \diamond b$ is undefined for some $a \neq b$. Let $d_1,d_2,\dots,d_n$ be all the elements with $d_i \diamond b = a$. Note from Law 3 that none of the $d_i$ can be equal to $b$. Choose a new element $c$, as well as $c_i$ for each $d_i$, and set $a \diamond b = c$, $d_i \diamond c = c_i$, and $d_i \diamond c_i = b$. It is easy to see that this preserves Laws 2,3. For Law 1 ,we do the usual case analysis:

- Case 1: $y = c$, $y = c_i$, $y \diamond x = c$, or $y \diamond x = c_i$. This case cannot occur because we have not defined left multiplication with $c$ or $c_i$.
- Case 2: $x = c$ or $x = c_i$. Because $d_i \neq b$, it is easy to see that $(y \diamond x) \diamond x$ is not defined for any $x$.
- Case 3: $(y \diamond x) \diamond x = c$ or $(y \diamond x) \diamond x = c_i$. This is only possible if $x=b$ and $y = d_j$ for some $j$, and the claim then follows from construction.
- Case 4: None of the terms in $(y \diamond x) \diamond x$ are equal to $c$ or $c_i$. This follows from the previous seed.

## Lean

Formalized as [`Eq1722.Greedy.lift`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1722.Greedy.lift).

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 407](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L407)
