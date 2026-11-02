# Alternate formula

For integers $0 \le a \le b$ let $E(a,b)$ be the number of magma equations $t_1 = t_2$ with $t_1$ of order $a$, $t_2$ of order $b$, counting up to relabelling, up to switching terms, and only allowing the equation $x=x$ of the form $t=t$. Then one has

- $E(0,0) = 2$.

- If $a\neq b$:

    $$
    E(a,b) = T(a) \cdot T(b) \cdot
    \sum_{\begin{smallmatrix} 1 \le p \le a+1 \\ 1 \le q \le b+1 \\ 0 \le s \le \min(p,q) \end{smallmatrix}}
    \left\{\begin{array}{c} a+1 \\ p \end{array}\right\}
    \left\{\begin{array}{c} b+1 \\ q \end{array}\right\}
    \binom{p}{s} \binom{q}{s} s! \ .
    $$

- If $a= b > 0$:

    $$
    \begin{aligned}
    E(a,b) &= \frac{1}{2} T(a)^2 \cdot \sum_{\begin{smallmatrix}1 \le p,q \le a+1\\ 0 \le s \le \min(p,q)\end{smallmatrix}}
    \left\{\begin{array}{c} a+1 \\ p \end{array}\right\}
    \left\{\begin{array}{c} a+1 \\ q \end{array}\right\}
    \binom{p}{s} \binom{q}{s} s! \\
    &\quad + \frac{1}{2} T(a) \cdot \sum_{\begin{smallmatrix}1 \le p \le a+1\\ 0 \le s \le p\end{smallmatrix}}
    \left\{\begin{array}{c} a+1 \\ p \end{array}\right\}
    \binom{p}{s} \, {\sf Invol}(s) \\
    &\quad - T(a) \cdot \sum_{1 \le p \le a+1}
    \left\{\begin{array}{c} a+1 \\ p \end{array}\right\}.
    \end{aligned}
    $$

Here the *Stirling numbers $\left\{\substack{n\\m}\right\}$ of the second kind* count the number of ways to partition a set of $n$ elements into $m$ non-empty subsets,

$$
T(n) = \frac{1}{n+1} \cdot \binom{2n}{n}
$$

counts the number of plane binary trees of order $n$, and.

$$
{\sf Invol}(n) = \sum_{0 \leq k \leq \lfloor n/2 \rfloor}  \binom{n}{2k} (2k-1)!!
$$

counts the number of involutions on $n$ elements.

The number of magma equations of order $n$ (under the given constraints) is then equal to

$$
\sum_{0 \le a \le \lfloor n/2 \rfloor } E(a,n-a) .
$$

For further details, as well as Maple calculations for $E(a,b)$, see [this folder](https://github.com/teorth/equational_theories/tree/main/scripts/count_magma_eqns).
