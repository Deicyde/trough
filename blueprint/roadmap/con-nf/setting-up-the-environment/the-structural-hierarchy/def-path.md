---
declaration: definition
origin: cited
lean: ConNF.Path
statement: formalized
---

# path

If $\alpha, \beta$ are type indices, then a *path* $\alpha \rightsquigarrow \beta$ is given by the constructors

- $\operatorname{\mathsf{nil}} : \alpha \rightsquigarrow \alpha$;
- $\operatorname{\mathsf{cons}} : (\alpha \rightsquigarrow \beta) \to (\gamma < \beta) \to (\alpha \rightsquigarrow \gamma)$.

We define by recursion a $\operatorname{\mathsf{snoc}}$ operation on the top of paths. We also prove the induction principle for $\operatorname{\mathsf{nil}}$ and $\operatorname{\mathsf{snoc}}$.

A path $\alpha \rightsquigarrow \bot$ is called an *$\alpha$-extended index*. We write $\operatorname{\mathsf{nil}}(\alpha)$ for the path $\{ \alpha \} : \alpha \rightsquigarrow \alpha$. If $h$ is a proof of $\beta < \alpha$, we write $\operatorname{\mathsf{single}}(h)$ for the path $\{ \alpha, \beta \} : \alpha \rightsquigarrow \beta$.

We have the inequality

$$
\begin{aligned}
\#(\alpha \rightsquigarrow \beta)
&\leq (\#\{ \gamma : \lambda^\bot \mid \gamma \leq \alpha \})^{\lt \omega} \\
&= \max(\aleph_0, \#\{ \gamma : \lambda^\bot \mid \gamma \leq \alpha \}) \\
&< \operatorname{\mathsf{cof}}(\operatorname{\mathsf{ord}}(\#\mu))
\end{aligned}
$$

## Depends on

- [type index](../model-parameters/def-typeindex.md)

## Lean

Formalized as [`ConNF.Path`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.Path).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 121](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L121)
