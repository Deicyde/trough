---
declaration: theorem
origin: cited
---

# Description of equivalence

Let $w$ be an irreducible word, and let $w'$ be a word equivalent to $w$.

- (i) If $w$ is a product $w = w_1 \diamond w_2$, then $w'$ takes the form

    $$
    w' = (((w'_1 \diamond w'_2) \diamond v_1) \diamond \dots \diamond v_n)
    $$

    for some $w'_1 \sim w_1$, $w'_2 \sim w_2$, some $n \geq 0$, and some words $v_1, \dots, v_n$ such that for all $0 \leq i < n$, $v_{i+1}$ is of the form

    $$
    v_{i+1} \sim (y_i \diamond z_i) \diamond (x_i \diamond z_i)
    $$

    for some $x_i, y_i, z_i$ with

    $$
    x_i \sim (((w'_1 \diamond w'_2) \diamond v_1) \diamond \dots \diamond v_i).
    $$

    In particular, $v_{i+1} \to x_i$.

- (ii) Similarly, if $w$ is a generator, then $w'$ takes the form

    $$
    w' = ((w \diamond v_1) \diamond \dots \diamond v_n)
    $$

    for some $n \geq 0$, and some words $v_1, \dots, v_n$ such that for all $0 \leq i < n$, $v_{i+1}$ is of the form

    $$
    v_{i+1} \sim (y_i \diamond z_i) \diamond (x_i \diamond z_i)
    $$

    for some $x_i, y_i, z_i$ with

    $$
    x_i \sim ((w \diamond v_1) \diamond \dots \diamond v_i).
    $$

    In particular, $v_{i+1} \to x_i$.

Conversely, any word of the above forms is equivalent to $w$.

## Depends on

- [Equation 854](../selected-laws/part-02/eq854.md)

## Proof

We just verify claim (i), as claim (ii) is similar. The converse direction is clear from [(5)](README.md) (after quotienting down to $M_X/\sim$), so it suffices to prove the forward claim. By [Birkhoff's completeness theorem](../basic-theory-of-magmas/sound-complete.md), it suffices to prove that the class of words described by (i) is preserved by any term rewriting operation, in which a term in the word is replaced by an equivalent term using [(1)](README.md). Clearly the term is in $w'_1$ or $w'_2$ then the form of the word is preserved, and similarly if the term is in one of the $v_i$. The only remaining case is if we are rewriting a term of the form

$$
x_i = (((w'_1 \diamond w'_2) \diamond v_1) \diamond \dots \diamond v_i).
$$

If $i>0$ we can rewrite this term down to $x_{i-1}$, and this still preserves the required form (decrementing $n$ by one). If $i=0$ then we cannot perform such a rewriting because of the irreducibility of $w_1 \diamond w_2$ and hence $w'_1 \diamond w'_2$. Finally, we can rewrite $x_i$ to $x_i \diamond v$ where $v$ is of the form

$$
v_i = (y \diamond z) \diamond (x_i \diamond z),
$$

and after some relabeling we are again of the required form (now incrementing $n$ by one).

## Sources

- [Equational Theories blueprint: chapter/854.tex, line 38](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/854.tex#L38)
