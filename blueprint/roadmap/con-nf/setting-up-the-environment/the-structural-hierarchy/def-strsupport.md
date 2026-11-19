---
declaration: definition
origin: cited
lean: ConNF.Support
statement: formalized
---

# structural support

A *$\beta$-structural support* (or just *$\beta$-support*) is a pair $S = (S^{\mathcal A}, S^{\mathcal N})$ where $S^{\mathcal A}$ is an enumeration of $(\beta \rightsquigarrow \bot) \times {\mathcal A}$ and $S^{\mathcal N}$ is an enumeration of $(\beta \rightsquigarrow \bot) \times {\mathcal N}$. The type of $\beta$-supports is written $\mathsf{StrSupp}_\beta$. There are precisely $\#\mu$ structural supports for any type index $\beta$.

For a path $A : \beta \rightsquigarrow \bot$, we write $S_A$ for the base support $T$ given by

$$
T^{\mathcal A} = \{ (i, a) \mid (i, (A, a)) \in S^{\mathcal A} \};\quad T^{\mathcal N} = \{ (i, N) \mid (i, (A, N)) \in S^{\mathcal N} \}
$$

More generally, for a path $A : \beta \rightsquigarrow \gamma$, we write $S_A$ for the $\gamma$-support $T$ given by

$$
T^{\mathcal A} = \{ (i, (B, a)) \mid (i, (A_B, a)) \in S^{\mathcal A} \};\quad T^{\mathcal N} = \{ (i, (B, N)) \mid (i, (A_B, N)) \in S^{\mathcal N} \}
$$

For a path $A : \alpha \rightsquigarrow \beta$, we write $S^A$ for the $\alpha$-support $T$ given by

$$
T^{\mathcal A} = \{ (i, (A_B, a)) \mid (i, (B, a)) \in S^{\mathcal A} \};\quad T^{\mathcal N} = \{ (i, (A_B, N)) \mid (i, (B, N)) \in S^{\mathcal N} \}
$$

Clearly, $(S^A)_A = S$.

$\beta$-structural permutations act on pairs $(A, x)$ by $\pi(A, x) = (A, \pi_A(x))$, where $x$ is either an atom or a near-litter. Hence, structural permutations act on structural supports.

Let $\tau$ be a type, and let $G$ be a $\texttt{StrPermClass}_\beta$-group that acts on $\tau$. We say that $S$ *supports* $x : \tau$ under the action of $G$ if whenever $\pi : G$ fixes $S$, it also fixes $x$, and moreover, if $\beta = \bot$ then $S_A^{\mathcal N}$ is empty for any $A : \bot \rightsquigarrow \bot$ (and of course there is exactly one such path).

## Depends on

- [base support](def-basesupport.md)
- [structural permutation](def-strperm.md)

## Lean

Formalized as [`ConNF.Support`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.Support).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 250](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L250)
