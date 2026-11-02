---
declaration: theorem
origin: cited
lean: Refutation_854.not_3316_3925
statement: formalized
---

# 854 does not imply 3316, 3925

The laws

$$
x \diamond y = x \diamond (y \diamond (x \diamond y))
$$

and

$$
x \diamond y = (x \diamond (y \diamond x)) \diamond y
$$

are not implied by [E854](https://teorth.github.io/equational_theories/implications/?854).

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We work in the free group $M_X$ on two generators $X = \{x,y\}$. It suffices to show that

$$
x \diamond y \not \sim x \diamond (y \diamond (x \diamond y))
$$

and

$$
x \diamond y \not \sim (x \diamond (y \diamond x)) \diamond y.
$$

We begin with the first claim. Suppose this were not the case, then by [Unique factorization](unique-factorization.md) one of the following statements must hold:

- (i)

    $$
    y \to x
    $$

    .
- (ii)

    $$
    (y \diamond (x \diamond y)) \to x
    $$

    .
- (iii)

    $$
    y \diamond (x \diamond y) \sim y.
    $$

If (i) holds, then we have $x \diamond y = x$ (Equation 4) in $M_X/\sim$, hence in every magma satisfying [E854](https://teorth.github.io/equational_theories/implications/?854). But we have examples of such magmas in which this fails.

Similarly, if (iii) holds, then $y \diamond (x \diamond y) = y$ (Equation 10) holds in $M_X/\sim$, hence in every magma satisfying [E854](https://teorth.github.io/equational_theories/implications/?854). But we have examples of such magmas in which this fails.

Finally, if (ii) holds, then the claim

$$
x \diamond y \sim x \diamond (y \diamond (x \diamond y))
$$

to refute simplifies to

$$
x \diamond y \sim x
$$

and we are back to (i), which we already know not to be the case.

For the latter equation, we similarly have the cases

- (iv)

    $$
    y \to x
    $$

    .
- (v)

    $$
    y \to x \diamond (y \diamond x)
    $$

    .
- (vi)

    $$
    x \sim x \diamond (y \diamond x).
    $$

(iv) is (i), which was already ruled out, and (vi) is similarly a relabeled version of (iii). In case (v) holds, the claim to refute simplifies to

$$
x \diamond y \sim x \diamond (y \diamond x)
$$

and using [Unique factorization](unique-factorization.md) we reduce to either $y \sim y \diamond x$, $y \to x$, or $y \diamond x \to x$, and each of these is already known to fail.

## Lean

Formalized as [`Refutation_854.not_3316_3925`](https://teorth.github.io/equational_theories/docs/find/#doc/Refutation_854.not_3316_3925).

## Sources

- [Equational Theories blueprint: chapter/854.tex, line 83](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/854.tex#L83)
