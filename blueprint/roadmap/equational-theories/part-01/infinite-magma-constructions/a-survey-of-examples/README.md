# A survey of examples

## Translation-invariant models

The implication between the laws [E1648](https://teorth.github.io/equational_theories/implications/?1648) $({x = (x \diamond y) \diamond ((x \diamond y) \diamond y)})$ and [E206](https://teorth.github.io/equational_theories/implications/?206) $({x = (x \diamond (x \diamond y)) \diamond y})$ can be refuted by a translation-invariant magma on the integers. Define the function $f: \mathbb{Z} \to \mathbb{Z}$ by

$$
f(x) =
\begin{cases}
-1  & \text{if } x > 0, \\
0  & \text{if } x = 0, \\
1  & \text{if } x < 0,
\end{cases}
$$

and consider the translation-invariant magma on $\mathbb{Z}$ given by the operation $x \diamond y = x + f(y-x)$.

The resulting magma satisfies Equation 1648: one can show this by a case analysis on $f(y-x)$. If $f(y-x)=1$ we have $x \diamond y = x + f(y-x) = x + 1$, so

$$
(x \diamond y) \diamond ((x \diamond y) \diamond y) = (x + 1) \diamond ((x + 1) \diamond y) = (x + 1) \diamond (x + 2) = (x + 1) - 1 = x.
$$

Similar computations verify the other two cases.

However, setting $x=0$ and $y=-1$ in Equation 206, we get

$$
(x \diamond (x \diamond y)) \diamond y = (x \diamond 1) \diamond y = (-1) \diamond y = -1 \neq x
$$

so the magma does not satisfy [E206](https://teorth.github.io/equational_theories/implications/?206). We can conclude

- [1648 does not imply 206](non-imp-1648-206-thm.md)

There are variation of the translation-invariant constructions refuting implications: e.g. in some cases, similar constructions are carried out starting with a non-abelian group. Translation-invariant models are also useful building blocks for the *modified base model* constructions explained below.

## Modified base models

For some pairs of laws $P$ and $Q$, it is possible to start with an infinite model $(M,\diamond)$ satisfying both $P$ and $Q$, then modify the operation $\diamond$ in a limited way, resulting in a model $(M,\diamond')$ of $P$ that does not satisfy $Q$.

This works especially well when this *base model* $(M,\diamond)$ is a translation-invariant magma in which the function $f$ takes finitely many different values. This is common: e.g. the translation-invariant model refuting the implication above is of the required sort!

The strategy is to first modify the magma operation in a naive way, by introducing a counterexample to the consequent $Q$. This generally yields one or more counterexamples to the antecedent $P$, but one can *trace* the effects of this initial modification and make further adjustments which restore the antecedent.

A model refuting the implication between the laws [E1659](https://teorth.github.io/equational_theories/implications/?1659) $({x = (x \diamond y) \diamond ((y \diamond y) \diamond z)})$ and [E4315](https://teorth.github.io/equational_theories/implications/?4315) $({x \diamond (y \diamond x) = x \diamond (y \diamond z)})$ can be constructed using the modified base model technique. Start with the infinite model $(\mathbb{Z},\diamond)$ of [E1659](https://teorth.github.io/equational_theories/implications/?1659) given by the following operation:

$$
x\diamond y = \begin{cases} x+1 & \text{if } x,y \text{ have the same parity} \\ x -1 & \text{otherwise} \end{cases}
$$

A case analysis shows that the magma $(\mathbb{Z},\diamond)$ satisfies both [E1659](https://teorth.github.io/equational_theories/implications/?1659) and [E4315](https://teorth.github.io/equational_theories/implications/?4315). We will eventually *modify* it by setting

$$
x \diamond' y = \begin{cases} 0 & \text{if } x=0,\: x,y \text{ do not have the same parity} \\  x+1 & \text{if } x,y \text{ have the same parity} \\ x -1 & \text{otherwise} \end{cases}
$$

and checking that $(\mathbb{N}, \diamond' )$ satisfies [E1659](https://teorth.github.io/equational_theories/implications/?1659) but refutes [E4315](https://teorth.github.io/equational_theories/implications/?4315).

One finds these modifications using the following strategy:

First, choose some element (tuple) of the carrier $M$ that will constitute a counterexample to the consequent in the modified model. In this specific case, the consequent, [E4315](https://teorth.github.io/equational_theories/implications/?4315), can be written as

$$
x \diamond (y \diamond x) = x \diamond (y \diamond z)
$$

in equational form, which always holds when $x = z$. So let's choose the tuple $(0,0,1)$ to constitute the required counterexample. Computing $0 \diamond (0 \diamond 0) = 0 \diamond 1 = -1$ and similarly $0 \diamond (0 \diamond 1) = -1$ suggest that we could force this tuple to be a counterexample by defining a new operation $\diamond''$ and setting $0 \diamond'' 1$ to something other than $-1$. One seemingly has many choices here: should we take $0 \diamond'' 1 =0$, $0 \diamond'' 1 = 1$, $0 \diamond'' 1 = 2$, or perhaps even $0 \diamond'' 1 = -1$?

It's easy to rule out some of the possibilities. For instance, setting $0 \diamond'' 1 = 1$ would yield $0 \diamond'' (0 \diamond'' 0) = 0 \diamond'' 1 = 0 \diamond'' (0 \diamond'' 1)$ again. The simplest possibility which results in a counterexample to [E4315](https://teorth.github.io/equational_theories/implications/?4315) sets $0 \diamond'' 1 = 0$ and $x \diamond'' y = x \diamond y$ for any $x \neq 0, y \neq 1$.

Unfortunately, the resulting $(M,\diamond'')$ would not then satisfy [E1659](https://teorth.github.io/equational_theories/implications/?1659). For any $z \in M$, one would have

$$
(0 \diamond'' 1) \diamond'' ((1 \diamond'' 1) \diamond'' z) = 0 \diamond'' (2 \diamond'' z)
$$

which equals $0 \diamond'' 1 = 0$ as desired for even $z$, but equals $0 \diamond'' 3 = -1 \neq 0$ for odd $z$.

However, since $f$ takes finitely many values in the base model, the breakage is tightly controlled: by considering what happens if $x \neq 0$ and $y \neq 1$, we see that all new counterexamples to [E4315](https://teorth.github.io/equational_theories/implications/?4315) have this form. The calculation now suggests defining yet another $\diamond'''$, where setting $0 \diamond''' 3 = 0$ would eliminate this counterexample. But doing that just moves the issue one level higher: one then has

$$
(0 \diamond''' 3) \diamond''' ((3 \diamond''' 3) \diamond''' z) = 0 \diamond''' (4 \diamond''' z)
$$

which equals $0 \diamond''' 3 = 0$ as desired for even $z$, but equals $0 \diamond''' 5 = -1 \neq 0$ for odd $z$.

Instead, the infinitely many counterexamples arising from the iterated redefinition can be eliminated all at once by setting:

$$
x \diamond' y = \begin{cases} 0 & \text{if } x=0,\: x,y \text{ do not have the same parity} \\  x+1 & \text{if } x,y \text{ have the same parity} \\ x -1 & \text{otherwise} \end{cases}
$$

and also truncating the model to $\mathbb{N}$ since the result of the $\diamond'$ operation is nonnegative whenever the operands are nonnegative. This finishes the construction without generating any further violations of [E1659](https://teorth.github.io/equational_theories/implications/?1659) and proves

- [1659 does not imply 4315](non-imp-1659-4315-thm.md)

The result of a modified base model construction can be a finite modification (when $\diamond$ and $\diamond'$ differ in finitely many inputs) or one in which they differ in infinitely many coefficients. Note that if the base model $(M,\diamond)$ was obtained by a greedy construction, and $(M,\diamond')$ is a finite modification, then the modified model could also have been obtained using the same greedy construction. It is not surprising that more difficult refutations using this construction tend to require the latter sort of modification.
