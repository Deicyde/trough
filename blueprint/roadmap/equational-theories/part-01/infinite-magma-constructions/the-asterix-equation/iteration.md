---
declaration: lemma
origin: cited
---

# Enlarging a partial solution

Let $(E_0, E_1, E_2, f)$ be a partial solution to [(1)](README.md), and let $h$ be an element of $\mathbb{Z}$ that does not lie in $E_0$. Then there exists a partial solution $(E'_0, E'_1, E'_2, f')$ to [(1)](README.md) that extends $(E_0, E_1, E_2, f)$, such that $h \in E_0'$.

## Depends on

- [partial-solution](partial-solution.md)

## Proof

Because $f$ maps $E_1 \backslash E_0$ bijectively to $E_2 \backslash E_1$, there are three cases:

- $h$ is equal to an element $h_0$ of $\mathbb{Z} \backslash E_2$.
- $h$ is equal to an element $h_0$ of $E_1 \backslash E_0$.
- $h$ is equal to $h_1 = f(h_0)$ for some $h_0 \in E_1 \backslash E_0$, so that $h_1 \in E_2 \backslash E_1$.

We deal with these three cases in turn.

First suppose that $h = h_0\in \mathbb{Z} \backslash E_2$. We perform the following construction.

- Choose an element $h_1 \in \mathbb{Z}$ that does not lie in $E_2 \cup \{h_0, -h_0\}$; this is possible because $E_2$ is finite.

- Choose an element $h_2 \in \mathbb{Z}$ such that $h_2, h_0+h_1+h_2$, $-h_1$, and $-h_1-h_2$ are all distinct from each other and lie outside of $E_2 \cup \{h_0, h_1\}$; this is possible because $E_2$ is finite and $h_0+h_1 \neq 0$.

- Promote $h_0$ to $E_0$, promote $h_1, h_0+h_1+h_2$ to $E_1$, and promote $h_2, -h_1-h_2$ to $E_2$, creating new sets

    $$
    \begin{aligned}
    E'_0 &:= E_0 \cup \{h_0\} \\
    E'_1 &:= E_1 \cup \{h_0, h_1, h_0+h_1+h_2\} \\
    E'_2 &:= E_2 \cup \{h_0, h_1, h_0+h_1+h_2, h_2, -h_1-h_2\}.
    \end{aligned}
    $$

    Clearly we still have nested finite sets $E'_0 \subseteq E'_1 \subseteq E'_2$.

- Extend $f : E_1 \to E_2$ to a function $f': E'_1 \to E'_2$ by defining

    $$
    \begin{aligned}
    f'(h_0) &:= h_1 \\
    f'(h_1) &:= h_2 \\
    f'(h_0+h_1+h_2) &:= -h_1-h_2
    \end{aligned}
    $$

    while keeping $f'(h)=f(h)$ for all $h \in E_1$.

It is then a routine matter to verify that $(E'_0,E'_1,E'_2,f')$ is a partial solution to [(1)](README.md) extending $(E_0,E_1,E_2,f)$ and that $E'_0$ contains $h_0$, as required.

Now suppose that $h = h_0 \in E_1 \backslash E_0$, then the quantity $h_1 := f(h_0)$ lies in $E_2 \backslash E_1$. We perform the following variant of the above construction:

- Choose an element $h_2 \in \mathbb{Z}$ such that $h_2, h_0+h_1+h_2$, and $-h_1-h_2$, $-h_1$ are all distinct and lie outside of $E_2$. This is possible because $E_2$ is finite and $h_0+h_1 = h_0+f(h_0) \neq 0$.

- Promote $h_0$ to $E_0$, promote $h_1$ and $h_0+h_1+h_2$ to $E_1$, and promote $h_2, -h_1-h_2$ to $E_2$, thus creating new sets

    $$
    \begin{aligned}
    E'_0 &:= E_0 \cup \{h_0\} \\
    E'_1 &:= E_1 \cup \{h_1, h_0+h_1+h_2\} \\
    E'_2 &:= E_2 \cup \{h_0+h_1+h_2, h_2, -h_1-h_2\}.
    \end{aligned}
    $$

    Clearly we still have nested finite sets $E'_0 \subseteq E'_1 \subseteq E'_2$.

- Extend $f : E_1 \to E_2$ to a function $f': E'_1 \to E'_2$ by defining

    $$
    \begin{aligned}
    f'(h_1) &:= h_2 \\
    f'(h_0+h_1+h_2) &:= -h_1-h_2
    \end{aligned}
    $$

    while keeping $f'(h)=f(h)$ for all $h \in E_1$.

It is then a routine matter to verify that $(E'_0,E'_1,E'_2,f')$ is a partial solution to [(1)](README.md) extending $(E_0,E_1,E_2,f)$ and that $E'_0$ contains $h_0$, as required.

Finally, suppose that $h = h_1 = f(h_0)$ for some $h_0 \in E_1 \backslash E_0$, so that $h_1 \in E_2 \backslash E_1$. Then we perform the following algorithm.

- Choose an element $h_2 \in \mathbb{Z}$ such that $h_2, h_0+h_1+h_2$, $-h_1$, and $-h_1-h_2$ are all distinct and lie outside of $E_2$. This is possible because $E_2$ is finite and $h_0+h_1 = h_0+f(h_0) \neq 0$.

- Choose an element $h_3 \in \mathbb{Z}$ such that $h_3, h_1+h_2+h_3$, and $-h_2-h_3$ are all distinct and lie outside of $E_2 \cup \{h_2, h_0+h_1+h_2,-h_1-h_2\}$. This is possible because $E_2$ is finite.

- Promote $h_0, h_1$ to $E_0$, promote $h_2, h_0+h_1+h_2, h_1+h_2+h_3$ to $E_1$, and promote $h_3, -h_1-h_2,-h_2-h_3$ to $E_2$, creating new sets

    $$
    \begin{aligned}
    E'_0 &:= E_0 \cup \{h_0, h_1 \}\\
    E'_1 &:= E_1 \cup \{h_1, h_2, h_0+h_1+h_2, h_1+h_2+h_3 \}\\
    E'_2 &:= E_2 \cup \{h_2, h_3, h_0+h_1+h_2, h_1+h_2+h_3, -h_1-h_2, -h_2-h_3\}.
    \end{aligned}
    $$

    Clearly we still have nested finite sets $E'_0 \subseteq E'_1 \subseteq E'_2$.

- Extend $f : E_1 \to E_2$ to a function $f': E'_1 \to E'_2$ by defining

    $$
    \begin{aligned}
    f'(h_1) &:= h_2 \\
    f'(h_0+h_1+h_2) &:= -h_1-h_2 \\
    f'(h_2) &:= h_3 \\
    f'(h_1+h_2+h_3) &:= -h_2-h_3
    \end{aligned}
    $$

    while keeping $f'(h)=f(h)$ for all $h \in E_1$.

It is then a routine matter to verify that $(E'_0,E'_1,E'_2,f')$ is a partial solution to [(1)](README.md) extending $(E_0,E_1,E_2,f)$ and that $E'_0$ contains $h_0$, as required.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 71](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L71)
