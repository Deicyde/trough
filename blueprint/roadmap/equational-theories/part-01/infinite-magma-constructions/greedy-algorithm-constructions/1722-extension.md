---
declaration: lemma
origin: cited
lean: Eq1722.Greedy.lift
statement: formalized
---

# 1722 extension

Suppose that $\diamond$ is a partial solution, and $a \diamond b$ is currently undefined. Then there exists an extension $\diamond'$ of $\diamond$ for which $a \diamond' b$ is defined.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Suppose first that $b=a$, so $a \diamond a$ is undefined, then by Law 4 we have $d \diamond a \neq a$ for all $d$ with $d \diamond a$ defined. Set $a_0=a$ and find nine distinct elements $a_1,a_2,a_3,a_4,b_0,b_1,b_2,b_3,b_4$ not previously appearing in the domain or range of $\diamond$. Extend the indices periodically by setting $a_{i+4} = a_i,b_{i+4} = b_i$ for $i \ge 1$, and define $a_i \diamond' a_i = a_{i+1}$ (so $a_i = S^i a$), $a_{i+1} \diamond' a_i = b_i$, $b_i \diamond' a_i = a_{i+2}$, $a_{i+3} \diamond' a_{i+1} = a_{i+1}$, $a_{i+1} \diamond' a_{i+2} = a_{i+1}$, $a_{i+1} \diamond' b_i = a_i$. We also define $x \diamond' y = x \diamond y$ whenever the right-hand side is defined. It is easy to see that laws 2,3,4 are preserved (though for law 2 note that we have not defined $a_2 \diamond' a_0$ due to the way indices are extended). Now we case check Law 1.

- Case 1. $y$ is fresh, that is $y \in \{a_1,a_2,a_3,a_4,b_0,b_1,b_2,b_3,b_4\}$. If $x \diamond' y$ is not defined, we are done, so assume this is so. In particular, $x \in \{a_1,a_2,a_3,a_4,b_0,b_1,b_2,b_3,b_4\}$. If $x,y \in \{a_1,a_2,a_3,a_4\}$ we are done by construction. If $x = b_i$ for some $i$, then $y = a_i$ and we are again done by construction. Finally, if $y = b_i$ for some $i$, then $x = a_{i+1}$ and $(x \diamond' y) \diamond' y$ is undefined.
- Case 2. $x$ is fresh, that is $x \in \{a_1,a_2,a_3,a_4,b_0,b_1,b_2,b_3,b_4\}$. If we are not in Case 1 and $x \diamond' y$ is defined, we must have $y = a_0$ and $x \in \{a_1, b_0\}$. The case $x = a_1$ holds by construction, and the case $x = b_0$ holds as $a_2 \diamond' a_0$ is not defined.
- Case 3. $x,y \not \in \{a_1,a_2,a_3,a_4,b_0,b_1,b_2,b_3,b_4\}$ and $x \diamond y$ was undefined. Then $x \diamond' y$ is undefined unless $x=y=a_0$, in which case Law 1 holds by construction.
- Case 4. $x,y \not \in \{a_1,a_2,a_3,a_4,b_0,b_1,b_2,b_3,b_4\}$, $x \diamond y$ was defined, and $(x \diamond y) \diamond y$ was not defined. Then $(x \diamond' y) \diamond' y$ is undefined unless $(x \diamond y) = a = y$, but this is impossible by Law $4$ as already observed.
- Case 5. $x,y \not \in \{a_1,a_2,a_3,a_4,b_0,b_1,b_2,b_3,b_4\}$ and $x \diamond y$ and $(x \diamond y) \diamond y$ were defined. Then the claim follows from Law 1 applied to $\diamond$.

Now suppose that $a \diamond b$ is undefined for some $a \neq b$. By applying the previous construction, we may assume without loss of generality that $Sb$ is defined. We may assume that $a \diamond b$ remains undefined after doing so, since we are done otherwise. By Law 3, $a \neq Sb \diamond b$. By Law 2, we have $d \diamond b = a$ for at most one $d$, which is necessarily different from $Sb$. Choose a $c$ not previously appearing in the domain or range of $\diamond$, and set $a \diamond' b = c$. If a $d$ exists as before, we additionally set $Sb \diamond' c = d$. Finally we define $x \diamond' y = x \diamond y$ whenever the right-hand side is defined. It is again routine to check that $\diamond'$ satisfies Laws 2,3,4. Now we case check Law 1.

- Case 1. $x=c$ or $x \diamond' y = c$. Not possible since no left multiplication by $c$ is defined.
- Case 2. $y=c$. This would force $x = Sb$ and $d = Sb$, but this is not possible since $d$ is different from $Sb$.
- Case 3: $(x \diamond' y) \diamond' y = c$. This forces $x=d$ and $y=b$, and the claim follows from construction.
- Case 4: None of the terms in $(x \diamond' y) \diamond' y$ are equal to $c$. Then the claim follows from Law 1 applied to $\diamond$.

## Lean

Formalized as [`Eq1722.Greedy.lift`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1722.Greedy.lift).

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 365](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L365)
