---
declaration: lemma
origin: cited
lean: Eq63.Greedy.Extension.next
statement: formalized
---

# Extension

If $f: E \to \mathbb{Z}$ is a partial solution and $h_0 \in \mathbb{Z}$, then there exists an extension $f': E' \to \mathbb{Z}$ for which axiom (ii) applies, i.e., $h_0 \in E'$, $f'(h_0) \in E'$, $(f')^2(h_0)-h_0 \in E'$, and $f'((f')^2(h_0)-h_0) = -h_0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We divide into cases.

**Case 1:** $h_0 \in E$ and $f(h_0) \in E$. In this case we are already done thanks to axiom (ii).

**Case 2:** $h_0 \in E$ but $f(h_0) \not \in E$. This is the main case. Let $H$ be the set of all $h \in E$ such that $f(h) = f(h_0)$; this is a finite set containing $h_0$. Let $H' \subseteq H$ be the set of all $h' \in H$ such that $-h' \in E$. We make the following observations:

- (a) All elements $h$ of $H$ are non-zero. For if $h=0$ then $f(h_0)=f(h)=1 \in E$, contradicting the hypothesis $f(h_0) \not \in E$.
- (b) If $h' \in H'$ then $h' \neq h'+f(-h')$. Otherwise we would have $f(-h')=0$, then by axiom (iii) we have $h' = -3$, hence $f(h_0) = f(h') = 4 \in E$ by axiom (i). But this again contradicts the hypothesis $f(h_0) \not \in E$. (This is the main reason we take $E_0$ to be so large.)
- (c) If $h_1 \in H$ and $h_2 \in H'$ are distinct then $h_1 \neq h_2+f(-h_2)$. This follows from axiom (iv).
- (d) If $h_1, h_2\in H'$ are distinct then $h_1+f(-h_1) \neq h_2+f(-h_2)$. This follows from axiom (v).

From these observations, we see that if we take $c$ to be a sufficiently large integer, the following claims hold:

- 1. The expressions $\pm c$, $\pm(c - h)$ for $h \in H$, and $\pm(c-h'-f(-h'))$ for $h \in H'$ are all distinct from each other.
- 2. $c$ is not expressible as the sum of four or fewer elements of $\pm (E \cup f(E))$.

We select such a $c$. We then promote $f(h_0)$, $c - h$ for $h \in H$, and $-c+h'+f(-h')$ for $h' \in H'$, thus setting

$$
E' := E \cup \{f(h_0)\} \cup \{ c-h: h \in H\} \cup \{ -c+h'+f(-h'): h' \in H'\}.
$$

We then extend $f$ to $f': E' \to \mathbb{Z}$ by setting

$$
\begin{aligned}
f(f(h_0)) &:= c \\
f(c-h) &:= -h \\
f(-c+h'+f(-h')) &:= h' - c
\end{aligned}
$$

for all $h \in H$ and $h' \in H'$. Axiom (i) is then obvious. Axiom (ii) needs to be verified for the new elements $h_0$ and $c-h'$, $h' \in H'$ of $E'$ (the other elements will not satisfy the hypotheses of this axiom), but this is routine. In particular $h_0$ satisfies the required conclusion of this lemma.

We need to verify (iii) for the new elements of $E'$, but this is clear from property (a) and claim 2.

Now we need to verify (iv). It suffices to do so when at least one of $a,a',-a$ are new elements of $E'$. If neither of $a$, $-a$ are new, then the only new elements $a'$ for which $f(a')$ could equal $f(a)$ take the form $c-h$ (thanks to claim 2), but then $a'$ cannot equal $a+f(-a)$, again thanks to claim 2. If instead one of $a, -a$ is new, then from claim 1 the new element must be $f(h_0)$. There is no old element $a'$ with $f(a') = c = f(f(h_0))$, so we must have $a = -f(h_0)$, but then $a + f(-a) = -f(h_0)+c$ will not equal $a'$, again thanks to claim 2.

Finally, we need verify to (v). We may assume that at least one of $a,a',-a,-a'$ are new elements of $E'$. As before, this forces the new element to be $f(h_0)$, and this cannot be $a$ or $a'$, so without loss of generality we have $a = -f(h_0)$ and $a' \in E$. But then $a + f(-a) = -f(h_0)+c$ will not equal $a' + f(-a')$, again thanks to claim 2.

**Case 3:** $h_0 \not \in E$ but $h_0 \in f(E)$. Here we can write $h_0 = f(h_1)$ where $h_1$ is of the form in Case 2. Applying the Case 2 construction, we can pass to an extension in which $f(h_1) = h_0$ lies in $E$, and so we are now in either Case 1 or Case 2, and so we can again conclude.

**Case 4:** $h_0 \not \in E$ and $h_0 \not \in f(E)$. We let $c$ be an integer so large that it is not expressible as the sum of four or fewer elements of $\pm (E \cup f(E))$. We then promote $h_0$ to $E$ by setting

$$
E' := E \cup \{h_0\}
$$

and define an extension $f': E' \to \mathbb{Z}$ by setting $f'(h_0) := c$. Axioms (i)-(iii) are obvious. For axiom (iv), since $f'(h_0)$ is not equal to any other value of $f'$, the only new case introduced is if $-a = h_0$, but then $a+f(-a) = -h_0+c$ is distinct from $a'$ by choice of $c$. A similar argument yields axiom (v). With this extension, we are now in Case 2, and so we repeat the previous analysis to conclude.

## Lean

Formalized as [`Eq63.Greedy.Extension.next`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq63.Greedy.Extension.next).

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 801](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L801)
