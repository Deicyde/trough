# Basic theory of magmas

- [Magma](magma-def.md)

Groups, semi-groups, and monoids are familiar examples of magmas. However, in general we do not expect magmas to have any associative properties. In some literature, magmas are also known as groupoids, although this term is also used for a slightly different object (a category with inverses).

A magma is called *empty* if it has cardinality zero, *singleton* if it has cardinality one, and *non-trivial* otherwise.

The number of magma structures on a set $G$ of cardinality $n$ is of course $n^{n^2}$, which is (All sequences start from $n=0$ unless otherwise specified.)

$$
1, 1, 16, 19683, 4294967296, 298023223876953125, \dots
$$

([OEIS A002489](https://oeis.org/A002489)). Up to isomorphism, the number of finite magmas of cardinality $n$ up to isomorphism is the slightly slower growing sequence

$$
1, 1, 10, 3330, 178981952, 2483527537094825, 14325590003318891522275680, \dots
$$

([OEIS A001329](https://oeis.org/A001329)). As there are $n!$ ways to rearrange the elements of a set of cardinality $n$, the number of non-isomorphic magmas on a set of cardinality $n$ is at least $n^{n^2}/n!$; as it turns out, most magmas are idemprimal (which implies in particular that there are no non-trivial isomorphisms), so the number of non-isomorphic magmas is fairly close to this lower bound.

- [Free Magma](free-magma-def.md)

For sake of concreteness, we will take the alphabet $X$ to default to the natural numbers $\mathbb{N}$ if not otherwise specified.

For instance, if $X = \{0,1\}$, then $M_X$ would consist of the following words:

- $0$, $1$ (the words of order $0$);
- $0 \diamond 0$, $0 \diamond 1$, $1 \diamond 0$, $1 \diamond 1$ (the words of order $1$);
- $0 \diamond (0 \diamond 0)$, $0 \diamond (0 \diamond 1)$, $0 \diamond (1 \diamond 0)$, $0 \diamond (1 \diamond 1)$, $1 \diamond (0 \diamond 0)$, $1 \diamond (0 \diamond 1)$, $1 \diamond (1 \diamond 0)$, $1 \diamond (1 \diamond 1)$, $(0 \diamond 0) \diamond 0$, $(0 \diamond 0) \diamond 1$, $(0 \diamond 1) \diamond 0$, $(0 \diamond 1) \diamond 1$, $(1 \diamond 0) \diamond 0$, $(1 \diamond 0) \diamond 1$, $(1 \diamond 1) \diamond 0$, $(1 \diamond 1) \diamond 1$ (the words of order $2$);
- etc.

- [Lemma: For a finite alphabet $X$, the number of…](lemma-intro-1.md)

The first few Catalan numbers are

$$
1, 1, 2, 5, 14, 42, 132, \dots
$$

([OEIS A000108](https://oeis.org/A000108)).

For instance, if $f : \{0,1\} \to G$ maps $0,1$ to $x,y$ respectively, then

$$
\varphi_f(0 \diamond 1) = x \diamond y
$$

$$
\varphi_f(1 \diamond (0 \diamond 1)) = y \diamond (x \diamond y)
$$

and so forth. If $\pi \colon \mathbb{N} \to \mathbb{N}$ is the map $\pi(n) := n+1$, then

$$
\pi_*(0 \diamond 1) = 1 \diamond 2
$$

$$
\pi_*(1 \diamond (0 \diamond 1)) = 2 \diamond (1 \diamond 2)
$$

and so forth.

- [Law](law-def.md)

Thus, for instance, the commutative law

$$
0 \diamond 1 \simeq 1 \diamond 0\qquad\text{(1)}
$$

is satisfied by a magma $G$ if and only if

$$
x \diamond y = y \diamond x\qquad\text{(2)}
$$

for all $x, y \in G$. We refer to (2) as the *equation* associated to the law (1). One can think of equations as the “semantic” interpretation of a “syntactic” law. However, we shall often abuse notation and identify a law with its associated equation. In particular, we shall (somewhat carelessly) also refer to (2) as “the commutative law” (rather than “the commutative equation”).

- [Models](models-def.md)
- [Derivation](derivation-def.md)

This definition is useful because of the following theorem:

- [Birkhoff's completeness theorem](sound-complete.md)

If $\pi$ is a bijection, we will call $\pi_*(w) \simeq \pi_*(w')$ a *relabeling* of the law $w \simeq w'$. Thus for instance

$$
5 \diamond 7 \simeq 7 \diamond 5
$$

is a relabeling of the commutative law (1). By the above lemma, relabeling does not affect whether a given magma satisfies a given law.

Define the total order of a law $w \simeq w'$ to be the sum of the orders of $w$ and $w'$.

The first few Bell numbers are

$$
1, 1, 2, 5, 15, 52, 203, \dots
$$

([OEIS A000110](https://oeis.org/A000110)).

The sequence in [Counting laws up to relabeling](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/intro.tex#L153) is

$$
2, 10, 75, 728, 8526, 115764, \dots
$$

([OEIS A289679](https://oeis.org/A289679)).

Now we would also like to count laws up to relabeling and symmetry.

The sequence $D_n$ is

$$
1, 1, 2, 4, 11, 32, 117, \dots
$$

([OEIS A103293](https://oeis.org/A103293)), and the sequence in [Counting laws up to relabeling and symmetry](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/intro.tex#L171) is

$$
2, 5, 41, 364, 4294, 57882, 888440, \dots
$$

([OEIS A376620](https://oeis.org/A376620)).

We can also identify all laws of the form $w \simeq w$ with the trivial law $0 \simeq 0$. The number of such laws of total order $n$ is zero if $n$ is odd, and $C_{n/2} B_{n/2+1}$ if $n$ is even. We conclude:

This sequence is

$$
2, 5, 39, 364, 4284, 57882, 888365, \dots
$$

([OEIS A376640](https://oeis.org/A376640)).

In particular, up to relabeling, symmetry, and triviality, there are exactly $2+5+39+364+4284=4694$ laws of total order at most $4$. A list can be found [here](https://github.com/teorth/equational_theories/blob/main/data/equations.txt). A script for generating them may be found [here](https://github.com/teorth/equational_theories/blob/main/scripts/generate_eqs_list.py). The ordering of these equations is according to the following rules. First, an ordering on expressions with placeholder variables $\ast$ (such as $\ast \diamond (\ast \diamond \ast)$):

- (i) Expressions of lower order come before expressions of higher order.
- (ii) Expressions $w_L \diamond w_R$ of a given total order that is at least one are ordered lexicographically first by the ordering on the left component $w_L$, and then by the ordering on the right component $w_R$ if the left components agree.

For instance, $\ast \diamond \ast$ is less than $\ast \diamond (\ast \diamond \ast)$, which is less than $(\ast \diamond \ast) \diamond \ast$.

Then, we order placeholder equations such as $\ast \diamond (\ast \diamond \ast) \simeq (\ast \diamond \ast) \diamond \ast$, where both sides are given placeholder variables:

- (i) Equations of lower total order come before equations of higher total order.
- (ii) Equations $w \simeq w'$ of a given total order are ordered lexicographically first by the ordering on the left-hand side $w$, and then by the ordering on the right hand side $w'$ if the left-hand sides agree.

For instance, $\ast \diamond \ast \simeq \ast \diamond (\ast \diamond \ast)$ is less than $\ast \diamond \ast \simeq (\ast \diamond \ast) \diamond \ast$.

Finally, we order (and reduce) equations of the form $w \simeq w'$ as follows. Define the *shape* of an equation to be the equation in which all variables are replaced by placeholders $\ast$.

- (i) Equations of lower shape will be of lower order. For instance, any equation of shape $\ast \diamond \ast \simeq \ast \diamond (\ast \diamond \ast)$ is less than any equation $\ast \diamond \ast \simeq (\ast \diamond \ast) \diamond \ast$.
- (ii) Among equations of equal shape, equations whose variables are first in the lexicographical ordering will be lower. For instance, $0 \diamond 0 \simeq 0 \diamond (0 \diamond 0)$ is less than $0 \diamond 0 \simeq 1 \diamond (1 \diamond 1)$, which is in turn less than $0 \diamond 1 \simeq 0 \diamond (0 \diamond 0)$.
- (iii) Only the arrangement of the equation (up to relabeling and symmetry) which is minimal in this ordering is retained in the list. For instance, we do not retain $1 \diamond 2 \simeq 1$ because it can be replaced by $0 \simeq 0 \diamond 1$, which is earlier in the ordering.
- (iv) Any trivial equation $w \simeq w$, other than the order zero law $0 \simeq 0$, is discarded.

- [Alternate formula](alternate-formula/README.md)
