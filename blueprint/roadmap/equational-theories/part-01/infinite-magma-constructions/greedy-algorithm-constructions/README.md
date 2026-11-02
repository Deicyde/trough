# Greedy algorithm constructions

In [The Asterix equation](../the-asterix-equation/README.md) a magma satisfying one law and refuting another was obtained by using the fact that over translation-invariant magmas, equational laws simplify to univariate functional equations, and solving the resulting equation using a greedy algorithm.

One way to construct infinite magmas satisfying specific laws is via a greedy algorithm construction not on a one-variable functional equation, but on the operation table of the magma itself.

Here, it is best to work with *partially defined magma operations* on some carrier $G$. These can be interpreted as ternary relations $R(x,y,z)$ in three variables $x,y,z \in G$ which pass the following “vertical line test”:

- **(VLT)** If $R(x,y,z)$ and $R(x,y,z')$ both hold for some $x,y,z,z' \in G$, then $z=z'$.

Such an operation is then associated (via a one-to-one correspondence) to a partially defined operation $\diamond : S \to G$ for some $S \subseteq G \times G$, with $R(x,y,z)$ holding if and only if $x \diamond y$ is well-defined (i.e., $(x,y) \in S$) and equal to $z$. By abuse of notation, we shall also refer to $R$ as a partially defined magma operation. Genuine magmas then correspond to the special case where $S = G \times G$, that is to say $x \diamond y$ is well-defined for all $x,y \in G$.

Given a word $w(x_1,\dots,x_n)$ in variables $x_1,\dots,x_n$ (so $w$ is an element of the free magma on $n$ generators), we can say that $w(x_1,\dots,x_n)$ is *well-defined* with respect to a partially defined magma operation $R$ if it can be fully evaluated using $R$. For instance, the word $(x \diamond y) \diamond z$ is well-defined if there exists $w,u \in G$ such that $R(x,y,w)$ and $R(w,z,u)$ both hold, in which case $(x \diamond y) \diamond z$ evaluates to $u$. Note from the axiom (VLT) that this evaluation is unique, if it exists. Of course, in a genuine magma, all expressions are well-defined. We say that an expression $w(x_1,\dots,x_n)$ is *almost well-defined* if all strict subexpressions of $w$ are well-defined. For instance, $(x \diamond y) \diamond z$ is almost well-defined if there exists $w \in G$ such that $R(x,y,w)$ holds.

An equational law $w_1 \simeq w_2$ involving some variables $x_1,\dots,x_n$ is said to be *locally satisfied* by $R$ if, whenever $w_1(x_1,\dots,x_n)$, $w_2(x_1,\dots,x_n)$ are almost well-defined, and one of the two expressions is well-defined and evaluates to some output $y$, then the other expression is also well-defined and evaluates to the same output $y$. For instance, in order for $R$ to locally satisfy the associative law $(x \diamond y) \diamond z = x \diamond (y \diamond z)$ ([E4512](https://teorth.github.io/equational_theories/implications/?4512)), we require the following two axioms:

- **(4512-1)** If $R(x,y,w)$, $R(w,z,u)$, and $R(y,z,v)$, then $R(x,v,u)$.
- **(4512-2)** If $R(y,z,w)$, $R(x,w,u)$, and $R(x,y,v)$, then $R(v,z,u)$.

If a law involves a single variable on one side, then we only need one axiom. For instance, the Asterix law ([E65](https://teorth.github.io/equational_theories/implications/?65)) is locally satisfied by $R$ if and only if the following axiom holds:

- **(65)** If $R(y,x,z)$ and $R(x,z,u)$, then $R(y,u,x)$.

Note that if the relation $R$ is associated to a genuine magma operation $\diamond$, then it locally satisfies a law $w_1 \simeq w_2$ if and only if the magma operation $\diamond$ satisfies the law $w_1 \simeq w_2$. For instance, the relation $R$ associated to a globally defined magma operation $\diamond$ satisfies (4512-1) and (4512-2) if and only if the magma is associative.

More generally, one can ask for a ternary relation $R$ to satisfy some theory $\Gamma$ of universal laws, using the language of one ternary relation $R$, the equality symbol $=$, and possibly some constants (we will shortly introduce three constants $a,b,c$ for this purpose).

Suppose we have a relation $R$ satisfying some theory $\Gamma$ (for instance, (VLT) together with (65)), but which is only finitely supported (there are only finitely many triples $(x,y,z)$ for which $R(x,y,z)$ holds). Then one can find $a,b \in G$ such that $a \diamond b$ is currently undefined. If the carrier $G$ is infinite (e.g., if $G = \mathbb{N}$), one can then find another element $c$ which is *novel*: it is not equal to $a, b$, or any of the $x,y,z$ for which $R(x,y,z)$ hold. In other words, the relation $R$ and the constants $a,b,c$ satisfy the following additional axioms:

- **(novel-1)** $c \neq a$ and $c \neq b$.
- **(novel-2)** If $R(x,y,z)$, then $c \neq x$, $c \neq y$, and $c \neq z$.
- **(undefined)** $R(a,b,x)$ does not hold for any $x$.

Let us say that a theory $\Gamma$ is *greedily extensible* if, whenever $R$ is a finitely supported ternary relation satisfying $\Gamma$, and $a,b,c$ are constants satisfying (novel-1), (novel-2), (undefined), then there exists an extension $R'$ of $R$, thus

- **(extend)** $R(x,y,z) \implies R'(x,y,z)$ for all $x,y,z$,

which is also finitely supported and satisfies $\Gamma$, and which also satisfies the additional axiom

- **(define)** $R'(a,b,c)$.

Informally, $R'$ is formed from $R$ by “forcing” $a \diamond b = c$ and then adding other axioms as needed. (Indeed, our construction here can be viewed as a simple analogue of the forcing construction in set theory.)

Observe that if a theory $\Gamma$ containing (VLT) is greedily extensible, then any finitely supported ternary relation $R$ satisfying $\Gamma$ on a countably infinite carrier $G$ can be extended to a globally defined relation satisfying $\Gamma$, by iteratively selecting the first $(a,b)$ (in some fixed enumeration of $G \times G$) for which $a \diamond b$ is undefined, and then selecting a novel element $c$ to define as $a \diamond b$, and applying the greedily extensible property, and then taking a direct limit of the countable sequence of relations thus produced. This gives a flexible way to construct magmas that satisfy a given theory $\Gamma$, but which violate some other law $w_1 \simeq w_2$, as the task then reduces to just finding a partial solution $R$ to $\Gamma$ and some constants $x_1,\dots,x_n$ for which the expressions $w_1(x_1,\dots,x_n), w_2(x_1,\dots,x_n)$ are already well-defined, but not equal to each other.

Unfortunately, most theories are not greedily extensible without further modification. Consider for instance the theory $\Gamma$ consisting of (VLT) and the Asterix law (65). Given $a,b,c$ and a finitely supported $R$ satisfying $\Gamma$ as well as (novel-1), (novel-2), (undefined), we would like to construct a finitely supported $R'$ satisfying $\Gamma$, (extend), (define). The naive guess would just be to take the minimal construction

$$
R'(x,y,z) \hbox{ iff } R(x,y,z) \hbox{ or } (x,y,z) = (a,b,c).
$$

This can work, but there is an obstruction: if $R(w,a,b)$ for some $w$, then (65) forces $R'(w,c,a)$. So one would have to enlarge the definition of $R'(x,y,z)$, to hold true if one of the following statements holds:

- $R(x,y,z)$ holds.
- $(x,y,z) = (a,b,c)$.
- $(x,y,z) = (w,c,a)$ for some $w$ with $R(w,a,b)$.

This works more often, but there is then a second obstruction: if $R(b,a,b)$, then we now have $R'(b,c,a)$, and (65) then forces $R'(a,a,b)$. So we need to add a fourth item to the above list defining $R'$:

- $(x,y,z) = (a,a,b)$, assuming $R(b,a,b)$ holds.

But now if we had $R(a,a,z)$ for some $z \neq b$, this would then create a violation of (VLT). To fix this, we need to extend $\Gamma$ by adding an additional axiom:

- (65') If $R(y,x,y)$, then $R(x,x,y)$.

With this modification to $\Gamma$, if we run the above analysis, we now see that if $R(b,a,b)$ hold (so that $R(a,a,b)$ also holds), then (65) will force $R'(a,c,a)$, $R'(b,c,a)$, and $R'(c,c,a)$. So now the modified definition of $R'$ is that $R'(x,y,z)$ holds if one of the following statements holds:

- $R(x,y,z)$ holds.
- $(x,y,z) = (a,b,c)$.
- $(x,y,z) = (w,c,a)$ for some $w$ with $R(w,a,b)$.
- $(x,y,z) = (a,c,a)$, $(b,c,a)$, or $(c,c,a)$, assuming $R(b,a,b)$ holds.

One can then finally (for instance, with the assistance of a automated theorem prover) verify that if $R$ is finitely supported and satisfies $\Gamma = (VLT) + (65) + (65')$ and $a,b,c$ satisfy (novel-1), (novel-2), (undefined), then the $R'$ defined above is also finitely supported and satisfies $\Gamma$, (extend), (define). This shows that the theory $\Gamma$ is greedily extensible.

Using this, one can for instance find a magma satisfying [E65](https://teorth.github.io/equational_theories/implications/?65) that fails the left-cancellative property

$$
y \diamond x = y \diamond x' \implies x=x'
$$

or in terms of ternary relations

$$
R(y,x,z) \hbox{ and } R(y,x',z) \implies x=x'\qquad\text{(1)}
$$

simply by starting with a partial solution, say on the natural numbers in which (e.g.) $R(1,2,0)$, $R(1,3,0)$ are the only situations in which $R$ holds. One can easily verify that this satisfies (VLT) and (65), (65'), but not (1), and so any magma constructed by the above greedy construction will not be left-cancellative. Since the Obelix law [E1491](https://teorth.github.io/equational_theories/implications/?1491) forces left-cancellativity, this gives an alternate proof of [Asterix does not imply Obelix](../the-asterix-equation/asterix-obelix.md).

## Equation 1722

We illustrate the above technique by constructing solutions to equation 1722,

$$
(y \diamond y) \diamond ((x \diamond y) \diamond y) = x.\qquad\text{(2)}
$$

We abbreviate $Sy := y \diamond y$.

Define a *partial solution* to be a partial function $\diamond: E \to \mathbb{N}$ on some finite subset $E$ of $\mathbb{N} \times \mathbb{N}$ (which one can also think of as a finitely supported ternary relation $R(x,y,z)$ satisfying VLT) satisfying the following axioms:

- (Law 1) If $(x \diamond y) \diamond y$ is defined, then $Sy \diamond ((x \diamond y) \diamond y)$ is defined and equal to $x$.
- (Law 2) If If $x \diamond y$ and $z \diamond y$ are defined and equal to each other, then $x=z$.
- (Law 3) If $Sx$ is defined, then $(Sx \diamond x) \diamond x$ is defined.
- (Law 4) If there exists a $z$ such that $z \diamond x = x$ then $x \diamond x$ is defined.

- [1722 extension](1722-extension.md)

By the greedy algorithm, this implies that any partial solution can be extended to a 1722 magma on $\mathbb{N}$. We can now refute the implication to equation 1832

$$
x = (x \diamond Sx) \diamond Sx,
$$

equation 2644

$$
x = S^2 x \diamond x,
$$

and equation 3050,

$$
x = ((Sx \diamond x) \diamond x) \diamond x
$$

by using the partial solution

$$
0 \diamond 0 = 1, 0 \diamond 1 = 2, 1 \diamond 0 = 2, 1 \diamond 1 = 3, 1 \diamond 2 = 0, 1 \diamond 3 = 1, 1 \diamond 4 = 2
$$

$$
2 \diamond 0 = 3, 2 \diamond 1 = 4, 3 \diamond 0 = 4, 3 \diamond 1 = 1, 3 \diamond 3 = 3, 3 \diamond 4 = 0
$$

which violates all three equations at $x=0$.

## Equation 713

Similar arguments can actually handle 713: $x = y \diamond (y \diamond ((y \diamond x) \diamond x))$. Here, the laws defining a partial solution are

- (Law 1) If $(y \diamond x) \diamond x$ is defined, then $y \diamond (y \diamond ((y \diamond x) \diamond x))$ is defined and equal to $x$.
- (Law 2) $x \diamond y \neq y$ for all $x,y$.
- (Law 3) If $Sx$ is defined, then so is $Sx \diamond x$.

- [713 extension](713-extension.md)

One can now refute the implications of the equations $x = x \diamond ((x \diamond x) \diamond (x \diamond x))$ (817), $x = (x \diamond x) \diamond (x \diamond (x \diamond x))$ (1426), $x \diamond x = (x \diamond (x \diamond x)) \diamond x$ (3862), $x \diamond x = ((x \diamond x) \diamond x) \diamond x$ (4065) by using the partial solution

$$
0 \diamond 0 = 1, 0 \diamond 1 = 3, 0 \diamond 2 = 3, 0 \diamond 3 = 0
$$

$$
1\diamond 0 = 2, 1 \diamond 1 = 0, 1 \diamond 2 = 1, 1 \diamond 3 =2 , 1 \diamond 4 = 3
$$

$$
2 \diamond 0 = 2, 2 \diamond 2 = 4, 2 \diamond 4 = 0
$$

$$
4 \diamond 1 = 2, 4 \diamond 2 = 4, 4 \diamond 3 = 2, 4 \diamond 4 = 1.
$$

which violates 3862 at $x=2$ and the other three laws at $x=0.$

## Equation 1289

For $x = y \diamond (((x \diamond y) \diamond y) \diamond y)$ (1289), one can similarly argue using the rules

- (Law 1) If $((x \diamond y) \diamond y) \diamond y$ is already defined, then $y \diamond (((x \diamond y) \diamond y) \diamond y)$ is also defined and equals $x$.
- (Law 2) $R_x$ is injective for all $x$ currently in the table.
- (Law 3) $x\diamond x=x$ for all $x$ currently in the table.

- [1289 extension](1289-extension.md)

To refute $x \diamond (y \diamond x) = (x \diamond y) \diamond x$ (4435) and $x = (((y \diamond x) \diamond y) \diamond y) \diamond y$ (3316) we use the partial solution

$$
0 \diamond 0 = 0; 0 \diamond 1 = 2; 0 \diamond 2 = 1; 0 \diamond 4 = 1
$$

$$
1 \diamond 0 = 2; 1 \diamond 1 = 1
$$

$$
2 \diamond 0 = 3; 2 \diamond 2 = 2
$$

$$
3 \diamond 0 = 4; 3 \diamond 3 = 3
$$

$$
4 \diamond 4 = 4
$$

which violates 4435 at $(x,y)=(0,1)$ and 3116 at $(x,y)=(2,0).$

## Equation 73

For $x = y \diamond (y \diamond (x \diamond y))$ (73), we argue similarly, now with laws

- Law 1. If $y \diamond (x \diamond y)$ is defined, then $y \diamond (y \diamond (x \diamond y))$ is defined and equal to $x$.
- Law 2. $R_y$ is injective for all $y$ currently in the table.
- Law 3. $x \diamond y \neq y$ for all $x,y$ currently in the table.

- [73 extension](73-extension.md)

One can obtain various refutations by using the countermodels [here](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/713.2C.201289.2C.201447/near/483735768).

## Equation 63

For $x = y \diamond (x \diamond (x \diamond y))$ (63), we argue similarly, now with laws

- Law 1. If $x \diamond (x \diamond y)$ is defined, then $y \diamond (x \diamond (x \diamond y))$ is defined and equal to $x$.
- Law 2. If $x \diamond y = x \diamond z$ with $y,z$ distinct, then $y \diamond x$ (if defined) is not equal to $z$ or to $z \diamond x$ (if defined).
- Law 3: If $x \diamond x$ is defined, it is equal to $x$.
- Law 4: If $x \neq y$, then $x \diamond y$ is not equal to $x$.

- [63 extension](63-extension.md)

One can obtain various refutations by using the countermodels [here](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/713.2C.201289.2C.201447/near/483735768).

## Equation 1076

For $x = y \diamond ((x \diamond (x \diamond y)) \diamond y)$ (1076), we argue similarly. There are just two laws:

- Law 1. If $x \diamond (x \diamond y)$ is defined and equal to some $z$, then $y \diamond (z \diamond y)$ is defined and equal to $x$.
- Law 2. $x \diamond x$ is not equal to $x$.

- [1076 extension](1076-extension.md)

One can obtain various refutations by using the countermodels [here](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/713.2C.201289.2C.201447/near/483735768).

## Equation 3308

Similar: see [here](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/713.2C.201289.2C.201447/near/482066500) and [here](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/713.2C.201289.2C.201447/near/483735768).
