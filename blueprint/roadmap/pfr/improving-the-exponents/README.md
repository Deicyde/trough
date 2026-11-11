# Improving the exponents

The arguments here are due to Jyun-Jie Liao.

Previously in [Definition eta-def](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy_pfr.tex#L3) we had set $\eta=1/9$. To implement this chapter, one should refactor the previous arguments so that $\eta$ is now free to be a positive number, though the specific hypothesis $\eta=1/9$ would now need to be added to [$\tau$-decrement](../entropy-version-of-pfr/endgame/de-prop.md).

Let $X^0_1, X^0_2$ be $G$-valued random variables, and let $X_1, X_2$ be $\tau$-minimizers as defined in [$\tau$-minimizer](../entropy-version-of-pfr/tau-min-def.md).

For the next two lemmas, let $(T_1,T_2,T_3)$ be a $G^3$-valued random variable such that $T_1+T_2+T_3=0$ holds identically. Let $\delta$ be the quantity in [(1)](../entropy-version-of-pfr/endgame/README.md).

We have the following variant of [Constructing good variables, I](../entropy-version-of-pfr/endgame/construct-good-prelim.md):

- [Constructing good variables, I'](construct-good-prelim-improv.md)

(One could in fact refactor [Constructing good variables, I](../entropy-version-of-pfr/endgame/construct-good-prelim.md) to follow from [Constructing good variables, I'](construct-good-prelim-improv.md) and [Upper bound on conditioned Ruzsa distance](../entropic-ruzsa-calculus/part-02/cond-dist-fact.md)).

- [Constructing good variables, II'](construct-good-improv.md)

Now let $X_1, X_2, \tilde X_1, \tilde X_2$ be independent copies of $X_1, X_2, X_1, X_2$, and set

$$
U := X_1 + X_2, \qquad V := \tilde X_1 + X_2, \qquad W := X_1 + \tilde X_1
$$

and

$$
S := X_1 + X_2 + \tilde X_1 + \tilde X_2
$$

and introduce the quantities

$$
k = d[X_1;X_2]
$$

and

$$
I_1 = I(U : V \, | \, S).
$$

- [Constructing good variables, III'](averaged-construct-good.md)

To control the expressions in the right-hand side of this lemma we need a general entropy inequality.

- [General inequality](gen-ineq.md)

Returning to our specific situation, we now have

- [Bound on distance differences](dist-diff-bound.md)
- [Improved $\tau$-decrement](de-prop-improv.md)
- [Limiting improved $\tau$-decrement](de-prop-lim-improv.md)
- [Improved entropy version of PFR](entropy-pfr-improv.md)

One can then replace [Lemma pfr_aux](../proof-of-pfr/pfr-aux.md) with

- [pfr_aux-improv](pfr-aux-improv.md)

This implies the following improved version of Theorem [PFR](../proof-of-pfr/pfr.md):

- [Improved PFR](pfr-improv.md)

Of course, by replacing [PFR](../proof-of-pfr/pfr.md) with [Improved PFR](pfr-improv.md) we may also improve constants in downstream theorems in a straightforward manner.
