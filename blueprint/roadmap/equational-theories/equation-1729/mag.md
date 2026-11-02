---
declaration: theorem
origin: cited
---

# Extending a 1729 magma

Let $SM$ be a magma satisfying 1729, and let $N$ be another set disjoint from $SM$, and set $M := SM \uplus N$. Suppose that we have a squaring map $S': N \to SM$ (which will complement the existing squaring map $S: SM \to SM$), and bijections $L'_a, R'_a: N \to N$ for all $a \in SM$ (which will complement the existing bijections $L_a, R_a: SM \to SM$ coming from $SM$), satisfying the following axioms:

- (i) For all $a \in SM$, we have $L'_a = (R'_a)^{-1} (L'_{Sa})^{-1}$.
- (ii) For all $y \in N$, the elements $R'_a y \in N$ are distinct from each other and from $y$ as $a \in SM$ varies.
- (iii) If $R'_a x = y$ for some $a \in SM$ and some $x,y \in N$, then $L'_{S'y} L_{L_{S'x}^{-1} a} y = x$.
- (iv) For all $x \in N$, we have $(L'_{S'x})^2 x = x$.

Suppose also that we have an operation $\diamond': N \times N \to M$ satisfying the following axioms:

- (v) For all $x \in N$, we have $x \diamond' x = S'x$.
- (vi) For all $y \in N$ and $a \in SM$, we have $R'_a y \diamond' y = L_{S'y}^{-1} a$.
- (vii) For all $x,y \in N$ with $x \diamond' y$ not already covered by rules (v) or (vi), we have $x \diamond' y = z$ for some $z \in N$. Furthermore, $z \diamond' x = (L'_{S'x})^{-1} y$.

Then one can endow $M$ with an operation $\diamond'': M \times M \to M$ satisfying 1729 defined as follows:

- If $a,b \in SM$, then $a \diamond'' b = a \diamond b$.
- If $a \in SM$ and $x \in N$, then $a \diamond'' b := L'_a b$.
- If $x \in N$ and $a \in SM$, then $b \diamond'' a := R'_a b$.
- If $x,y \in N$, then $x \diamond'' y := x \diamond' y$.

Furthermore, the 817 law $x \diamond'' SS' x = x$ fails for any $x \in N$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We need to show that $\diamond''$ verifies the law 1729. In the case when $x,y \in SM$, then the claim follows from the fact that $SM$ already satisfied this equation. If $x$ was equal to an element $a \in SM$ and $y \in N$, then by construction the law is equivalent to $L'_{Sa} R'_a L'_a y = y$, which follows from axiom (i).

Now suppose that $x \in N$ and $y$ is equal to some element $a$ of $SM$. From axiom (v) we have $x \diamond'' x = S'x$, and then this case of 1729 becomes

$$
L_{S'x} ( R'_a x \diamond' x ) = a
$$

which follows from axiom (vi). So the only remaining case is when $x,y \in N$. Using axiom (ii), we can divide into cases:

- Case 1: $x=y$. Then by (v) we need to show that $L'_{S'x} L'_{S'x} x = x$, which follows from axiom (iv).
- Case 2: $y = R'_a x$ for some $a \in SM$. Then by axiom (vi), we need to show that $L'_{S'y} L'_{L_{S'x}^{-1} a} y = x$, which follows from axiom (iii).
- Case 3: We are not in case 1 or case 2. Then by axiom (vii), we have $y \diamond'' x = z$ for some $z \in N$ with $z \diamond'' y = (L'_{S'y})^{-1} x$. But this implies $L'_{S'y} (z \diamond'' y) = x$, which is 1729.

We have now verified that $\diamond''$ satisfies 1729. For any $x \in N$, we have $x \diamond'' SS' x = R'_{SS' x} x$, and so the final claim follows from axiom (ii).

## Sources

- [Equational Theories blueprint: chapter/1729.tex, line 17](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1729.tex#L17)
