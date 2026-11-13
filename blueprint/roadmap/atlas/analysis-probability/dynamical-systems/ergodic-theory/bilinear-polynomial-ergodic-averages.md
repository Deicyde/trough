---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.Lacunary, MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.variationalNorm, MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.A, MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.theorem_1_17_i, MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.theorem_1_17_ii, MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.theorem_1_17_iii, MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.theorem_1_17_iv
statement: formalized
---

# Bilinear polynomial ergodic averages

7 results, 3 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bilinear-polynomial-ergodic-averages/index.html).

## Lacunary sequence

For a real number $\Lambda \ge 0$, a sequence
$(a_n)_{n \in \mathbb{N}}$ of nonnegative real numbers is $\Lambda$-lacunary if
$a_{n+1} / a_n > \Lambda$ for every $n \in \mathbb{N}$, where division by $0$ gives $0$; in
particular every term of a $\Lambda$-lacunary sequence is positive.

Formalized by `MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.Lacunary`, a definition declared in [WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bilinear-polynomial-ergodic-averages/index.html#lacunary).

## Variational norm

For a real number $r \ge 0$ and a sequence
$a = (a_n)_{n \in \mathbb{N}}$ of complex numbers, the $r$-variational norm of $a$ is the
element of $[0, \infty]$

$$\|a\|_{\mathbb{V}^r} = \sup_{n \in \mathbb{N}} |a_n| +
\sup_{J \in \mathbb{N}} \sup_{N_0 \le N_1 \le \dots \le N_J}
\Big( \sum_{j=0}^{J-1} |a_{N_{j+1}} - a_{N_j}|^r \Big)^{1/r},$$

where the inner supremum runs over nondecreasing finite sequences of natural numbers
$N_0 \le N_1 \le \dots \le N_J$ and the empty sum ($J = 0$) is $0$. For $r = 0$ the whole term
$\big( \sum_{j=0}^{J-1} |a_{N_{j+1}} - a_{N_j}|^r \big)^{1/r}$ is replaced by the number of
indices $j < J$ with $a_{N_{j+1}} \ne a_{N_j}$.

Formalized by `MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.variationalNorm`, a definition declared in [WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bilinear-polynomial-ergodic-averages/index.html#variational-norm).

## Bilinear polynomial ergodic averages

Let $X$ be a measurable space and let
$T : X \to X$ be a measurable bijection with measurable inverse. For a real number $N \ge 0$,
polynomials $P_1, P_2 \in \mathbb{Z}[t]$, functions $f, g : X \to \mathbb{C}$ and a point
$x \in X$, the bilinear average is the complex number

$$A_N^{P_1, P_2}(f, g)(x) = \frac{1}{\lfloor N \rfloor}
\sum_{n=1}^{\lfloor N \rfloor} f(T^{P_1(n)} x)\, g(T^{P_2(n)} x),$$

where $T^k$ for $k \in \mathbb{Z}$ is the $k$-th power of $T$ in the group of bijections of $X$
(so negative powers are iterates of $T^{-1}$), and $A_N^{P_1, P_2}(f, g)(x) = 0$ when
$\lfloor N \rfloor = 0$.

Formalized by `MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.A`, a definition declared in [WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bilinear-polynomial-ergodic-averages/index.html#a).

## Mean ergodic theorem for bilinear polynomial averages

Let $(X, \mu)$ be a $\sigma$-finite
measure space and let $T : X \to X$ be a measurable bijection with measurable inverse that
preserves $\mu$. Let $P \in \mathbb{Z}[t]$ have degree at least $2$, and let
$p_1, p_2 \in (1, \infty)$ and $p \in [0, \infty]$ satisfy $p_1^{-1} + p_2^{-1} = p^{-1}$ and
$p^{-1} \le 1$. For a real number $N \ge 0$, functions $f, g : X \to \mathbb{C}$ and $x \in X$ let

$$A_N(f, g)(x) = \frac{1}{\lfloor N \rfloor}
\sum_{n=1}^{\lfloor N \rfloor} f(T^n x)\, g(T^{P(n)} x),$$

with $A_N(f, g)(x) = 0$ when $\lfloor N \rfloor = 0$, where $T^k$ for $k \in \mathbb{Z}$ is the
$k$-th power of $T$ in the group of bijections of $X$. Then for all
$f \in L^{p_1}(\mu)$ and $g \in L^{p_2}(\mu)$ with values in $\mathbb{C}$ there is a function
$h : X \to \mathbb{C}$ in $L^p(\mu)$ such that $\|A_N(f, g) - h\|_{L^p(\mu)} \to 0$ as the real
number $N$ tends to $\infty$.

This is Theorem 1.17(i) of Krause, Mirek and Tao.

## Sources

- B. Krause, M. Mirek, and T. Tao, `Pointwise ergodic theorems for non-conventional bilinear polynomial averages`, Annals of Math, 195 (3) 2022. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_pointwise_ergodic_theorems` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.theorem_1_17_i` is written with `theorem_wanted` in [WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bilinear-polynomial-ergodic-averages/index.html#theorem-1-17-i).

## Pointwise ergodic theorem for bilinear polynomial averages

Let $(X, \mu)$ be a $\sigma$-finite
measure space and let $T : X \to X$ be a measurable bijection with measurable inverse that
preserves $\mu$. Let $P \in \mathbb{Z}[t]$ have degree at least $2$, and let
$p_1, p_2 \in (1, \infty)$ and $p \in [0, \infty]$ satisfy $p_1^{-1} + p_2^{-1} = p^{-1}$ and
$p^{-1} \le 1$. For a real number $N \ge 0$, functions $f, g : X \to \mathbb{C}$ and $x \in X$ let

$$A_N(f, g)(x) = \frac{1}{\lfloor N \rfloor}
\sum_{n=1}^{\lfloor N \rfloor} f(T^n x)\, g(T^{P(n)} x),$$

with $A_N(f, g)(x) = 0$ when $\lfloor N \rfloor = 0$, where $T^k$ for $k \in \mathbb{Z}$ is the
$k$-th power of $T$ in the group of bijections of $X$. Then for
all $f \in L^{p_1}(\mu)$ and $g \in L^{p_2}(\mu)$ with values in $\mathbb{C}$ there is a function
$h : X \to \mathbb{C}$ in $L^p(\mu)$ such that for $\mu$-almost every $x \in X$,
$A_N(f, g)(x) \to h(x)$ as the real number $N$ tends to $\infty$.

This is Theorem 1.17(ii) of Krause, Mirek and Tao.

## Sources

- B. Krause, M. Mirek, and T. Tao, `Pointwise ergodic theorems for non-conventional bilinear polynomial averages`, Annals of Math, 195 (3) 2022. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_pointwise_ergodic_theorems` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.theorem_1_17_ii` is written with `theorem_wanted` in [WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bilinear-polynomial-ergodic-averages/index.html#theorem-1-17-ii).

## Maximal inequality for bilinear polynomial averages

Let $(X, \mu)$ be a $\sigma$-finite
measure space and let $T : X \to X$ be a measurable bijection with measurable inverse that
preserves $\mu$. Let $P \in \mathbb{Z}[t]$ have degree at least $2$, and let
$p_1, p_2 \in (1, \infty)$ and $p \in [0, \infty]$ satisfy $p_1^{-1} + p_2^{-1} = p^{-1}$ and
$p^{-1} \le 1$. For a real number $N \ge 0$, functions $f, g : X \to \mathbb{C}$ and $x \in X$ let

$$A_N(f, g)(x) = \frac{1}{\lfloor N \rfloor}
\sum_{n=1}^{\lfloor N \rfloor} f(T^n x)\, g(T^{P(n)} x),$$

with $A_N(f, g)(x) = 0$ when $\lfloor N \rfloor = 0$, where $T^k$ for $k \in \mathbb{Z}$ is the
$k$-th power of $T$ in the group of bijections of $X$. Then there is
a constant $C \ge 0$, which may depend on $(X, \mu, T)$, $P$, $p_1$, $p_2$ and $p$, such that
for all $f \in L^{p_1}(\mu)$ and $g \in L^{p_2}(\mu)$ with values in $\mathbb{C}$,

$$\Big\| \sup_{N \in \mathbb{Z}_{>0}} |A_N(f, g)| \Big\|_{L^p(\mu)} \le
C \, \|f\|_{L^{p_1}(\mu)} \, \|g\|_{L^{p_2}(\mu)},$$

where the supremum is taken pointwise in $[0, \infty]$.

This is Theorem 1.17(iii) of Krause, Mirek and Tao.

## Sources

- B. Krause, M. Mirek, and T. Tao, `Pointwise ergodic theorems for non-conventional bilinear polynomial averages`, Annals of Math, 195 (3) 2022. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_pointwise_ergodic_theorems` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.theorem_1_17_iii` is written with `theorem_wanted` in [WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bilinear-polynomial-ergodic-averages/index.html#theorem-1-17-iii).

## Long variational inequality for bilinear polynomial averages

Let $(X, \mu)$ be a
$\sigma$-finite measure space and let $T : X \to X$ be a measurable bijection with measurable
inverse that preserves $\mu$. Let $P \in \mathbb{Z}[t]$ have degree at least $2$, and let
$p_1, p_2 \in (1, \infty)$ and $p \in [0, \infty]$ satisfy $p_1^{-1} + p_2^{-1} = p^{-1}$ and
$p^{-1} \le 1$. For a real number $N \ge 0$, functions $f, g : X \to \mathbb{C}$ and $x \in X$ let

$$A_N(f, g)(x) = \frac{1}{\lfloor N \rfloor}
\sum_{n=1}^{\lfloor N \rfloor} f(T^n x)\, g(T^{P(n)} x),$$

with $A_N(f, g)(x) = 0$ when $\lfloor N \rfloor = 0$, where $T^k$ for $k \in \mathbb{Z}$ is the
$k$-th power of $T$ in the group of bijections of $X$. Then
for all real numbers $r > 2$ and $\Lambda > 1$ there is a constant $C \ge 0$, which may depend
on $r$, $\Lambda$ and all of the data above, such that for all $f \in L^{p_1}(\mu)$ and
$g \in L^{p_2}(\mu)$ with values in $\mathbb{C}$ and every $\Lambda$-lacunary sequence
$(a_n)_{n \in \mathbb{N}}$ of nonnegative reals (that is, $a_{n+1} / a_n > \Lambda$ for all $n$)
with $a_n \ge 1$ for all $n$,

$$\Big\| x \mapsto \big\| (A_{a_n}(f, g)(x))_{n \in \mathbb{N}} \big\|_{\mathbb{V}^r}
\Big\|_{L^p(\mu)} \le C \, \|f\|_{L^{p_1}(\mu)} \, \|g\|_{L^{p_2}(\mu)},$$

where $\| \cdot \|_{\mathbb{V}^r}$ is the $r$-variational norm of a sequence of complex numbers.

This is Theorem 1.17(iv) of Krause, Mirek and Tao.

## Sources

- B. Krause, M. Mirek, and T. Tao, `Pointwise ergodic theorems for non-conventional bilinear polynomial averages`, Annals of Math, 195 (3) 2022. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_pointwise_ergodic_theorems` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.PointwiseErgodicTheoremsWanted.PointwiseErgodicTheorems.theorem_1_17_iv` is written with `theorem_wanted` in [WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/PointwiseErgodicTheoremsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bilinear-polynomial-ergodic-averages/index.html#theorem-1-17-iv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bilinear polynomial ergodic averages](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bilinear-polynomial-ergodic-averages/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/ergodic-theory/bilinear-polynomial-ergodic-averages)
