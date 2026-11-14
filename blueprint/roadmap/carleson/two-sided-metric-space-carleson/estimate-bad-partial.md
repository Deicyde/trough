---
declaration: lemma
origin: cited
lean: estimate_bad_partial
statement: formalized
proof: formalized
---

# Estimate bad partial

Let $x\in X\setminus\Omega$. Then

$$
|T_rb(x)| \le 3F(x)+\alpha/8,
$$

where

$$
F(x) := 2^{a^3+2a+1} c\alpha \sum_{j\in J} \left(\frac{3r_j}{\rho(x,x_j)}\right)^{\frac{1}{a}}\frac{\mu(B_{3,j})}{V(x,x_j)}.
$$

## Depends on

- [Calderon Zygmund decomposition](calderon-zygmund-decomposition.md)

## Proof

We decompose the index set $J$ into the following disjoint sets:

$$
\begin{aligned}
\mathcal{J}_1(x)&:=\{j\,: r+3r_j \le \rho(x,x_j) \},\\
\mathcal{J}_2(x)&:=\{j\,: r-3r_j \le \rho(x,x_j) < r+3r_j\},\\
\mathcal{J}_3(x)&:=\{j\,: \rho(x,x_j) < r-3r_j\}.
\end{aligned}
$$

Then

$$
\begin{alignedat}{3}
|T_r b(x)|\le&&&\sum_{j\in \mathcal{J}_1(x)} |T_rb_j(x)|\qquad\text{(67)}\\
&+&&\sum_{j\in \mathcal{J}_2(x)} |T_rb_j(x)|\qquad\text{(68)}\\
&+&&\sum_{j\in \mathcal{J}_3(x)} |T_rb_j(x)|.\qquad\text{(69)}\end{alignedat}
$$

For all $j\in \mathcal{J}_3(x)$, $\operatorname{\operatorname{supp}} b_j\subset B_{3,j}\subset B(x,r)$, and thus $T_rb_j(x)=0$, so $\eqref{eq-b-dec-3} = 0$.

Next, for $j\in \mathcal{J}_1(x)$, $\operatorname{\operatorname{supp}} b_j\subset B_{3,j}\subset X \setminus B(x,r)$, and we have

$$
T_rb_j(x)=\int_{X\setminus B(x,r)} K(x,y) b_j(y)\,d\mu(y)=\int_{B_{3,j}} K(x,y) b_j(y)\,d\mu(y)\,.
$$

Using [(54)](calderon-zygmund-decomposition.md), the above is equal to

$$
\int_{{3,j}} (K(x,y)-K(x,x_j)) b_j(y)\,d\mu(y)\,.
$$

Since $x\in X\setminus\Omega$, we have for each $y\in B_{3,j}$ that

$$
\rho(x,x_j)\ge 6r_j > 2\rho(x_j,y),\qquad\text{(70)}
$$

so we can apply [(15)](../introduction/README.md) to estimate

$$
\eqref{eq-b-dec-1} \le \sum_{j\in \mathcal{J}_1(x)}\int_{B_{3,j}}\left(\frac{\rho(x_j,y)}{\rho(x,x_j)}\right)^{\frac{1}{a}}\frac{2^{a^3}}{V(x,x_j)} |b_j(y)|\, d\mu(y)
$$

$$
\le 2^{a^3} \sum_{j} \left(\frac{3r_j}{\rho(x,x_j)}\right)^{\frac{1}{a}}\frac{1}{V(x,x_j)}\int_{B_{3,j}} |b_j(y)|\, dy
$$

and by [(55)](calderon-zygmund-decomposition.md),

$$
\le 2^{a^3+2a+1} c\alpha \sum_{j} \left(\frac{3r_j}{\rho(x,x_j)}\right)^{\frac{1}{a}}\frac{\mu(B_{3,j})}{V(x,x_j)} = F(x).\qquad\text{(71)}
$$

Next, we estimate (68). For each $j\in \mathcal{J}_2(x)$, set

$$
d_j:=\frac{1}{\mu(B_{3,j})}\int_{B_{3,j}} \mathbf{1}_{X\setminus B(x,r)}(y) b_j(y)\, dy.
$$

Then by [(55)](calderon-zygmund-decomposition.md)

$$
|d_j|\le 2^{2a+1} c\alpha.\qquad\text{(72)}
$$

For each $j\in \mathcal{J}_2(x)$, we have

$$
\begin{aligned}
T_r b_j(x)&=\int_{B_{3,j}} K(x,y) (\mathbf{1}_{X\setminus B(x,r)}(y)b_j(y)-d_j)\, dy + \int_{B_{3,j}} d_j K(x,y) \, dy \\
&= \int_{B_{3,j}} (K(x,y)-K(x,x_j)) (\mathbf{1}_{X\setminus B(x,r)}(y)b_j(y)-d_j)\, dy + \int_{B_{3,j}} d_j K(x,y) \, dy.
\end{aligned}
$$

Thus, using the triangle inequality, the equation above and (72), we obtain

$$
|T_r b_j(x)|\le
$$

$$
\int_{B_{3,j}} |K(x,y)-K(x,x_j)| \left(|b_j(y)|+2^{2a+1} c\alpha\right)\, dy +2^{2a+1} c\alpha \int_{B_{3,j}}  |K(x,y)| \, dy.\qquad\text{(73)}
$$

By (70), we can apply [(15)](../introduction/README.md) and arguing as in (71), we get that

$$
\eqref{eq-b-dec-2} \le 2F(x) + 2^{2a+1}c\alpha \sum_{j\in\mathcal{J}_2(x)} \int_{B_{3,j}}  |K(x,y)|\,d\mu(y),\qquad\text{(74)}
$$

with $F$ as in (71). Define

$$
A := \bigcup_{j \in \mathcal{J}_2(x)} B_{3,j}.
$$

We claim that

$$
A\subset B(x,3r) \setminus B(x,\frac{r}{3}).\qquad\text{(75)}
$$

Indeed, for each $j\in \mathcal{J}_2(x)$ and $y\in B_{3,j}$, using again (70),

$$
\rho(x,x_j) < r+r_{3,j} \le r + \frac{1}{2} \rho(x,x_j) \implies \rho(x,x_j) < 2r
$$

and hence

$$
\rho(x,y) \le \rho(x,x_j) + \rho(x_j,y) < 2r + 3r_j \le 2r + \frac{1}{2}\rho(x,x_j) < 3r.
$$

For the lower bound, we observe

$$
\rho(x,x_j) \ge r-3r_j \ge r - \frac{1}{2} \rho(x,x_j) \implies \rho(x,x_j) \ge \frac{2}{3}r,
$$

and conclude

$$
\rho(x,y) \ge \rho(x,x_j) - \rho(y,x_j) \ge \rho(x,x_j) - 3r_j \ge \rho(x,x_j) - \frac{1}{2}\rho(x,x_j) \ge \frac{1}{3} r.
$$

Using the bounded intersection property of the $B_{3,j}$, (75) and [(14)](../introduction/README.md), we get

$$
\begin{aligned}
\sum_{j\in\mathcal{J}_2(x)} \int_{B_{3,j}}  |K(x,y)|\,d\mu(y) &\le 2^{6a} \int_{A}  |K(x,y)|\,d\mu(y) \\
&\le 2^{6a} \int_{B(x,3r) \setminus B(x,\frac{r}{3})}  |K(x,y)|\,d\mu(y) \\
&\le 2^{6a} \int_{B(x,3r) \setminus B(x,\frac{r}{3})} \frac{2^{a^3}}{V(x,y)} \,d\mu(y) \\
&\le 2^{a^3+6a} \int_{B(x,3r) \setminus B(x,\frac{r}{3})} \frac{1}{\mu(B(x,\frac{r}{3}))} \,d\mu(y) \\
&\le 2^{a^3+6a} \frac{\mu(B(x,3r))}{\mu(B(x,\frac{r}{3}))} \\
&\le 2^{a^3+10a}.\qquad\text{(76)}\end{aligned}
$$

Combining the estimates (71) for (67), (74) for (68), and (76), we get

$$
|T_rb(x)|\leq 3F(x)+2^{a^3+12a+1}c\alpha.
$$

By the definition [(61)](README.md) of $c$, this equals

$$
3F(x)+\alpha/8.
$$

## Lean

Formalized as [`estimate_bad_partial`](https://fpvandoorn.github.io/carleson/docs/find/#doc/estimate_bad_partial).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7894](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7894)
