# A crash course in tensor products

We've defined $\widehat{\mathbb{Q}}$ to be $\mathbb{Q}\otimes\widehat{\mathbb{Z}}$. Whatever does this mean? Well just to orient yourself, if $A$ and $B$ are additive abelian groups, then $A\otimes B$ is also an abelian group. And if $A$ and $B$ are commutative rings (as they are in our case), then $A\otimes B$ is also a commutative ring.

Even if $A$ and $B$ are completely concrete commutative rings, their tensor product $A\otimes B$ might be incomprehensible. For example $\mathbb{C}\otimes\mathbb{C}$ is completely incomprehensible (note that we are tensoring over the integers). It is not like the product of groups or the disjoint union of two sets, where you have a completely explicit unambiguous formula for each element.

In this sense, the theory of tensor products is a bit like the theory of continuous functions. Humanity started off studying concrete polynomial equations such as $x^2+1$ and then moved on to concrete analytic functions such as $\log(x)$ and $\sin(x)$, but eventually the abstract concept of a continuous function from the reals to the reals was born. There is no “formula” for a general continuous function, and continuous functions such as $e^{-1/x^2}$ or $|x|$ have no power series. Even if there *were* a formula for a specific continuous function of interest, it is not clear in general how to make sense of the claim that it's the “best” formula. In other words, there is no "canonical form" for a general continuous function, and yet we prove things about them anyway. We shall adopt the same attitude for elements of $A\otimes B$.

The first thing to know about the tensor product $A\otimes B$ of two abelian groups $A$ and $B$ is a “constructor” for the type. In other words, how can we make elements $A\otimes B$? Well, it turns out that given elements $a\in A$ and $b\in B$, we can form the element $a\otimes_t b\in A\otimes B$.

**Example.** Recall that the sum of all the factorials is an element $e\in\widehat{\mathbb{Z}}$, and $22/7$ is certainly a rational number, so we can make the element $\frac{22}{7}\otimes_te\in\widehat{\mathbb{Q}}$.

This example is in the Lean code.

Elements of the form $a\otimes_t b\in A\otimes B$ are known as *pure tensors*. In the literature, pure tensors are often written $a\otimes b$, but we shall follow mathlib's convention in reserving the $\otimes$ symbol for *groups* like $A \otimes B$, and adorning it with a $t$ when using it on *elements* of the groups (or, as Lean calls them, *terms*, which explains the notation).

Addition of pure tensors obeys the “distributivity” rules $a\otimes_t b_1+a\otimes_t b_2=a\otimes_t(b_1+b_2)$ and $a_1\otimes_t b+a_2\otimes_t b=(a_1+a_2)\otimes_t b$, but there is no rule which simplifies a general sum $a\otimes_t b + c\otimes_t d$ into a pure tensor. Indeed, in general it is *not* the case that every element of a tensor product $A\otimes B$ is of the form $a\otimes_t b$; there can be tensors which aren't pure. However every element of $A\otimes B$ is a finite sum of pure tensors, with the result that one can attempt to define additive maps from $A\otimes B$ by saying what they do on pure tensors, and then extending linearly.

Another thing worth understanding is that just like how rational numbers can be written as quotients of integers in several ways (for example $1/2=2/4=3/6=\cdots$), a general pure tensor in $A\otimes B$ can be represented as $a\otimes_t b$ in many ways. For example, in $\widehat{\mathbb{Q}}$ we have $1\otimes_t 2=2\otimes_t 1$. A general rule for equality of pure tensors is that if $a\in A$ and $b\in B$ and $z\in\mathbb{Z}$, then $za\otimes_tb=a\otimes_tzb$; integers can move over the tensor symbol. But equality is hard: in general there may not be an algorithm to decide whether two pure tensors $a\otimes_t b$ and $c\otimes_t d$ are equal in $A\otimes B$.

**Remark.** A summary of the situation: if $A$ and $B$ are abelian groups, then every element of $A\otimes B$ can be written in the form $\sum_{i=1}^Na_i\otimes_tb_i$. It's just that this representation is highly nonunique, and furthermore given explicit elements $a_1,a_2\in A$ and $b_1,b_2\in B$ it might be a hard problem to figure out if $a_1\otimes_t b_1=a_2\otimes_t b_2$.

For example, it turns out that $(\mathbb{Z}/2\mathbb{Z})\otimes(\mathbb{Z}/3\mathbb{Z})=0$ and so in this tensor product all the $a\otimes_t b$ are equal to each other and to $0\otimes 0$.

Having said all of that, one nice property of $\widehat{\mathbb{Q}}$ is that every tensor *is* pure; let's prove this now.

- [QHat.canonicalForm](qhat-canonicalform.md)

Be careful though: just because every element of $\widehat{\mathbb{Q}}$ can be written as $q\otimes z$, this representation may not be unique. For example $2\otimes 1=1\otimes 2$. However, writing $\frac{1}{N}\otimes_t z$ as $z/N$ does tempt us into the following definition.

- [QHat.IsCoprime](qhat-iscoprime.md)
- [QHat.lowestTerms](qhat-lowestterms.md)

If $A$ and $B$ are additive abelian groups then $A\otimes B$ is also an additive abelian group. However if $A$ and $B$ are commutative rings, then $A\otimes B$ also inherits the structure of a commutative ring, with $0=0\otimes_t 0$ and $1=1\otimes_t 1$. Pure tensors multiply in the obvious way: the product of $a_1\otimes_t b_1$ and $a_2\otimes_t b_2$ is $a_1a_2\otimes_t b_1b_2.$ There are ring homomorphisms $A\to A\otimes B$ and $B\to A\otimes B$ sending $a$ to $a\otimes_t 1$ and $b$ to $1\otimes_t b$. In general such maps are not injective, but in the case of $\widehat{\mathbb{Q}}=\mathbb{Q}\otimes\widehat{\mathbb{Z}}$ both maps from $\mathbb{Q}$ and $\widehat{\mathbb{Z}}$ are inclusions.

- [QHat.injective\_rat](qhat-injective-rat.md)
- [QHat.injective\_zHat](qhat-injective-zhat.md)

We can thus identify $\mathbb{Q}=\mathbb{Q}\otimes\mathbb{Z}$ and $\widehat{\mathbb{Z}}=\mathbb{Z}\otimes\widehat{\mathbb{Z}}$ with subrings of $\widehat{\mathbb{Q}}=\mathbb{Q}\otimes\widehat{\mathbb{Z}}$. Note that, being commutative rings, $\mathbb{Q}$ and $\widehat{\mathbb{Z}}$ both contain a copy of $\mathbb{Z}$ as a subring, and the corresponding copies of $\mathbb{Z}$ in $\widehat{\mathbb{Q}}$ are equal; this is because $1\otimes a=a\otimes 1$ for all $a\in\mathbb{Z}$.
