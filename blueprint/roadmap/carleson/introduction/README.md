# Introduction

Trigonometric series represent functions as possibly infinite linear combinations of pure frequencies. They gained particular prominence through the work of J. Fourier, who used them in his analytical theory of heat (Fourier), see also (MR3470070), thereby establishing them as a tool for solving partial differential equations. Fourier also made the groundbreaking claim that a wide range of functions could be represented using trigonometric series. This sparked the interest of many mathematicians, including Dirichlet, who gave some rigorous conditions for convergence of Fourier series, as trigonometric series are now called. Dirichlet also opened a branch of analytic number theory partially inspired by the ideas of Fourier. Nowadays, Fourier analysis plays an important role in many areas of mathematics.

With Euler's formula to represent pure frequencies in mind, a trigonometric polynomial can be expressed as

$$
S_N(x):= \sum_{n=-N}^N c_n e^{inx} \ .\qquad\text{(1)}
$$

The Fourier series is then defined as the limit $f$ of such a sequence $S_N$ as $N$ tends to $\infty$. Fourier's vision to represent rather general functions raises two fundamental questions. The first question is to identify the appropriate choice of coefficients $c_n$ to use to represent a given $f$. The second question addresses the convergence of $S_N$ to $f$.

The first question has a fairly canonical and standard answer, provided by the Fourier integral formula:

$$
c_n:=\widehat{f}_n:=\frac 1{2\pi}\int_0^{2\pi}f(x) e^{- i nx}\, dx,\qquad\text{(2)}
$$

where the precise interpretation of the integral depends on the chosen theory of integration. For a continuous function $f$, Riemann's notion of the integral suffices. If $f$ is integrable in the Lebesgue sense, $f\in L^1(0,2\pi)$, the Lebesgue integral is appropriate. More generally, if $f$ is a distribution in the sense of Schwartz, supported in $[0,2\pi]$ the integral can be understood as an evaluation against the periodic test function $e^{-i nx}$. In each case, the more general definition reduces to the simpler one within the respective more restrictive domain. Hence, the Fourier coefficients given by (2) serve as a universal choice. This choice is unique in several respects, in particular if one is to exactly reproduce a trigonometric polynomial $f$ in the form (1).

The second question of convergence bifurcates into the question of pointwise convergence of the series (1) (with coefficients given by (2)) for a given $x$ on the one hand and convergence of the functions $S_N$ to the function $f$ in a suitable function space with corresponding topology on the other hand. There are at least as many function spaces for the question of convergence as there are different definitions of the integral elaborated earlier. There are some very canonical answers to the convergence question in function spaces, albeit not known at the time of Fourier and Dirichlet. One example is convergence in the Hilbert space sense for $f$ in $L^2(0,2\pi)$, as discovered in the first decade of the twentieth century as a consequence of the rapid development of Lebesgue integration theory. Another canonical example is convergence in the sense of distributions for general distributional $f$, as discovered a few decades after Lebesgue integration. For some other natural spaces, such as $L^1(0,2\pi)$, there is no guarantee of convergence in the norm of that space even if $f$ is in the space.

In contrast to these examples of function spaces with a very natural theory of convergence of Fourier series in the topology of the function space, there are no similarly elegant solutions to the characterization of pointwise convergence. In particular, the space of functions $f$ such that the sequence $S_N(x)$ converges for every $x$ does not have a good characterization in terms of $f$ itself. Similarly, the space of all functions $f$ such that the sequence of coefficients $\widehat{f}_n$ is absolutely summable has also no good characterization.

When the Fourier integral is defined in the Lebesgue sense and $f\in L^1(0,2\pi)$, then the function $f$ itself is meaningful not everywhere but only pointwise almost everywhere in the Lebesgue sense. The question of pointwise convergence to $f$ for all $x$ then becomes meaningless, and instead one asks for almost everywhere convergence. Such convergence was conjectured by N. Luzin (Luzin13) for the space $L^2(0,2\pi)$, see also the collected works (Luzin53). Kolmogorov's example (Kolmogorov) of an $L^1$ function whose Fourier series diverges at almost every point seemed to provide some evidence against Luzin's conjecture. Indeed, in the 1960s, L. Carleson tried to construct a counterexample to Luzin's conjecture. In his own recollection, his efforts led him to better and better understand how such a potential counterexample should look like. In the end, the counterexample had to satisfy so many properties that the properties started to contradict each other, and Carleson realized that a counterexample could not exist. Thus, he had proved Luzin's conjecture (carleson). In particular, he had proven the more elementary statement

- [classical Carleson](classical-carleson.md)

Here, almost every $x$ means in the Lebesgue sense, i.e., for every $\epsilon>0$ the set of $x$ where convergence fails can be covered by a sequence of intervals such that the sum of the lengths of these intervals is less than $\epsilon$. While Carleson had proven the more general Luzin conjecture for functions in $L^2[0,2\pi]$, even the more elementary statement for continuous functions was not known before Carleson's work. Moreover, until now, the elementary statement has not seen any substantially easier proof than those generalizing to $L^2$, partially because there is no readily usable criterion on the level of Fourier coefficients to distinguish between continuous functions and $L^2$ functions.

Shortly after Carleson's breakthrough, Hunt (MR238019) proved the analogous result for $L^p$ functions with $p>1$ and for functions in $L^1\log(L)^2$. Billard (MR217510) adapted Carleson's arguments to prove almost everywhere convergence of Walsh-Fourier series for functions in $L^2$.

In (fefferman), C. Fefferman gave an alternative proof of Carleson's theorem via an a priori bound for Carleson's operator, the maximally modulated singular integral

$$
Tf(x):=\sup_{N} \int_{-\pi}^\pi e^{iNy}f(x-y)\frac 1y {dy}\, .\qquad\text{(4)}
$$

In (lacey-thiele), a duality between the approaches by Carleson and Fefferman was pointed out and a more symmetric and self-dual proof was presented.

Various strengthenings of Fefferman's estimates for Carleson's operator have appeared since, such as bounds for a higher dimensional Carleson operator in the isotropic (MR336222), (MR2007237) and anisotropic (MR4014801) setting. The supremum norm in the variable $N$ in (4) was strengthened to maximal multiplier norms in (MR2420509) with applications to return times theorems in ergodic theory. It was strengthened to variation norms $V^r$ with $r>2$ in (MR2881301) with applications to nonlinear analysis.

Stein and Wainger (stein-wainger) proposed to study variants of (4) replacing the linear modulation phase $Ny$ by polynomial phases in $y$ and proved a result for polynomials without a linear term. This was generalized by Lie to general polynomial Carleson operators, first for a supremum over all quadratic polynomials (lie-quadratic) and then for a supremum over all polynomials in (lie-polynomial). The polynomial Carleson operator was further generalized to higher dimensions and Hölder regular kernels in (zk-polynomial). The development of polynomial Carleson operators has led to further generalisations, for example to almost everywhere convergence of Malmquist-Takenaka series (mnatsakanyan) and maximally modulated singular Radon transforms (ramos), (becker2024maximal).

Surveys to Carleson's theorem can be found in (MR2091007), (MR3334208).

In this blueprint, we prove Theorem [classical Carleson](classical-carleson.md) as a corollary to a further generalization of the polynomial Carleson operator towards doubling metric measure spaces, Theorem [metric space Carleson](metric-space-carleson.md) below, which is new and appears in the sibling communication (becker2024carlesonoperatorsdoublingmetric). Theorem [metric space Carleson](metric-space-carleson.md) is an axiomatic approach to Carleson type theorems on doubling metric measure spaces. This axiomatic approach is suitable for formalization and a good route towards the classical theorem.

Early drafts of the sibling communication (becker2024carlesonoperatorsdoublingmetric) existed in summer 2023. Based on this, the first draft of the present blueprint was written in the first half of 2024, containing a much more detailed proof, which involved increasing the size by a factor of four, and adding the derivation of Carleson's classical result. In June 2024, the fourth author launched a [public website](https://florisvandoorn.com/carleson/) to post the blueprint, using the open-source software `leanblueprint` developed by Patrick Massot, calling for contributions to formalize the proof. The goal was to formalize the blueprint in the Lean proof assistant (moura2021lean), building on top of its mathematical library `Mathlib` (mathlib). The work was split up into about 180 tasks, to be claimed by individual contributors. Most tasks were to formalize the proof of a single lemma from the blueprint, and some were to develop basic theory or refactor existing code. The contributors adapted the blueprint to fix some gaps found during the formalization and gave feedback that led to discussions about the proof. This even resulted in a few changes to the general setup and the main theorems. All of the gaps found required only fairly localized changes to the blueprint, indicating that the initial blueprint was already of high quality. The formalization was completed in July 2025. It is attached to this arXiv posting, and the latest version can be found [on Github](https://github.com/fpvandoorn/carleson).

Everyone that completed a substantial amount of tasks is included as a coauthor of the blueprint. The authors acknowledge contributions in the form of small formalization additions, pointing out corrections to the blueprint, or supplying ideas to the Lean efforts by the following people: Michel Alexis, Bolton Bailey, Julian Berman, Joachim Breitner, Martin Dvořák, Georges Gonthier, Aaron Hill, Austin Letson, Bhavik Mehta, Eric Paul, Clara Torres, Dennis Tsar, Andrew Yang, Ruben van de Velde.

*Acknowledgement.* L.B., M.I.d.F.F., L.D., F.v.D., M.R., R.S., and C.T. were funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under Germany's Excellence Strategy – EXC-2047/1 – 390685813. L.B., R.S., and C.T. were also supported by SFB 1060. A.J. is funded by the TÜBITAK (Scientific and Technological Research Council of Türkiye) under Grant Number 123F122. J.R. was supported in part by NSF grant DMS-2154835 and a HIM fellowship for the Fall 2024 trimester program in Bonn.

## Statement of the metric space Carleson theorems

Let

$$
a\ge 4
$$

be a natural number that as it gets larger will allow for more general applications of Theorem [metric space Carleson](metric-space-carleson.md) but will worsen the constants in the estimates.

A doubling metric measure space $(X,\rho,\mu, a)$ is a complete and locally compact metric space $(X,\rho)$ equipped with a non-zero locally finite Borel measure $\mu$ that satisfies the doubling condition that for all $x\in X$ and all $R>0$ we have

$$
\mu(B(x,2R))\le 2^a\mu(B(x,R))\,,\qquad\text{(5)}
$$

where we have denoted by $B(x,R)$ the open ball of radius $R$ centered at $x$:

$$
B(x,R):=\{y\in X: \rho(x,y)\lt R\}.\qquad\text{(6)}
$$

In a doubling metric measure space the closed balls are compact and $\mu$ is positive on all non-empty open sets.

A collection ${\Theta}$ of real valued continuous functions on the doubling metric measure space $(X,\rho,\mu,a)$ is called compatible, if there is a point $o\in X$ where all the functions are equal to $0$, and if there exists for each ball $B \subset X$ a metric $d_B$ on ${\Theta}$, such that the following five properties (7), (8), (9), (10), and (11) are satisfied. For every ball $B \subset X$

$$
\sup_{x,y\in B}|{\vartheta}(x)-{{\vartheta}(y)}- {\theta}(x)+{{\theta}(y)}| \le d_{B}({\vartheta},{\theta})\,.\qquad\text{(7)}
$$

For any two balls $B_1=B(x_1,R)$, $B_2= B(x_2,2R)$ in $X$ with $x_1\in B_2$ and any ${\vartheta},{\theta}\in {\Theta}$,

$$
d_{B_2}({\vartheta},{\theta})\le 2^a d_{B_1}({\vartheta},{\theta}) .\qquad\text{(8)}
$$

For any two balls $B_1, B_2$ in $X$ with $B_1 \subset B_2$ and any ${\vartheta}, {\theta} \in {\Theta}$

$$
d_{B_1}({\vartheta},{\theta}) \le d_{B_2}({\vartheta}, {\theta})\qquad\text{(9)}
$$

and for any two balls $B_1=B(x_1,R)$, $B_2= B(x_2,2^aR)$ with $B_1\subset B_2$, and ${\vartheta},{\theta}\in {\Theta}$,

$$
2d_{B_1}({\vartheta},{\theta})
\le d_{B_2}({\vartheta},{\theta}) .\qquad\text{(10)}
$$

For every ball $B$ in $X$ and every $d_B$-ball $\tilde B$ of radius $2R$ in ${\Theta}$, there is a collection $\mathcal{B}$ of at most $2^a$ many $d_B$-balls of radius $R$ covering $\tilde B$, that is,

$$
\tilde B\subset \bigcup \mathcal{B}.\qquad\text{(11)}
$$

Further, a compatible collection ${\Theta}$ is called cancellative, if for any ball $B$ in $X$ of radius $R$, any Lipschitz function $\varphi: X\to {\mathbb{C}}$ supported on $B$, and any ${\vartheta},{\theta}\in {\Theta}$ we have

$$
|\int_B e({\vartheta}(x)-{{\theta}(x)}) \varphi(x) d\mu(x)|\le 2^a \mu(B)\|\varphi\|_{\operatorname{\operatorname{Lip}}(B)}
(1+d_B({\vartheta},{\theta}))^{-\frac{1}{a}},\qquad\text{(12)}
$$

where $\|\cdot\|_{\operatorname{\operatorname{Lip}}(B)}$ denotes the inhomogeneous Lipschitz norm on $B$:

$$
\|\varphi\|_{\operatorname{\operatorname{Lip}}(B)} = \sup_{x \in B} |\varphi(x)| + R \sup_{x,y \in B, x \neq y} \frac{|\varphi(x) - \varphi(y)|}{\rho(x,y)}\,.
$$

A one-sided Calderón–Zygmund kernel $K$ on the doubling metric measure space $(X, \rho, \mu, a)$ is a measurable function

$$
K:X\times X\to \mathbb{C}\qquad\text{(13)}
$$

such that for all $x,y',y\in X$ with $x\neq y$, we have

$$
|K(x,y)| \leq \frac{2^{a^3}}{V(x,y)}\qquad\text{(14)}
$$

and if $2\rho(y,y') \leq \rho(x,y)$, then

$$
|K(x,y) - K(x,y')| \leq \left(\frac{\rho(y,y')}{\rho(x,y)}\right)^{\frac{1}{a}}\frac{2^{a^3}}{V(x,y)},\qquad\text{(15)}
$$

where

$$
V(x,y):=\mu(B(x,\rho(x,y))).
$$

Define the maximally truncated non-tangential singular integral $T_{*}$ associated with $K$ by

$$
T_{*}f(x):=\sup_{R_1 < R_2} \sup_{\rho(x,x')\lt R_1} \left|\int_{R_1< \rho(x',y) < R_2} K(x',y) f(y) \, \mathrm{d}\mu(y) \right|\,.\qquad\text{(16)}
$$

We define the generalized Carleson operator $T$ by

$$
Tf(x):=\sup_{{\vartheta}\in{\Theta}} \sup_{0 < R_1 < R_2}\left| \int_{R_1 < \rho(x,y) < R_2} K(x,y) f(y) e({\vartheta}(y)) \, \mathrm{d}\mu(y) \right|\, ,\qquad\text{(17)}
$$

where $e(r)=e^{ir}$.

Our first main result is the following restricted weak type estimate for $T$ in the range $1\lt q\le 2$, which by interpolation techniques recovers $L^q$ estimates for the open range $1\lt q<2$.

- [metric space Carleson](metric-space-carleson.md)

In some applications, such as the Walsh-case of Carleson's theorem, the kernel $K$ naturally depends also on the modulation functions ${\vartheta}$. The fact that we don't assume Hölder-continuity of the kernel $K$ in the first argument allows us to also capture this situation.

We now state another Theorem with a slightly weaker replacement of the assumption [(18)](metric-space-carleson.md). It implies the Walsh-case of Carleson's theorem. For a Borel function ${Q}:X\to {\Theta}$, and ${\vartheta} \in {\Theta}$ and $x\in X$ define

$$
R_{{Q}}({\vartheta},x)=\sup\{r>0:d_{B(x,r)}({\vartheta}, {Q}(x))<1\}
$$

and define further

$$
T_{{Q}}^{\vartheta} f(x):=\sup_{R_1\lt R_2} \ \sup_{\rho(x,x')\lt R_1}
\left|\int_{R_1< \rho(x',y) < \min\{R_2, R_{{Q}}({\vartheta},x')\}} K(x',y) f(y) \, \mathrm{d}\mu(y) \right|\qquad\text{(20)}
$$

Define further the linearized generalized Carleson operator $T_{Q}$ by

$$
T_{Q} f(x):= \sup_{0 < R_1 < R_2}\left| \int_{R_1 < \rho(x,y) < R_2} K(x,y) f(y) e({Q}(x)(y)) \, \mathrm{d}\mu(y) \right|\, ,\qquad\text{(21)}
$$

where again $e(r)=e^{ir}$.

- [linearised metric Carleson](linearised-metric-carleson.md)

**Remark.** The value of the constant factor $2^{443a^3}$ in Theorems [metric space Carleson](metric-space-carleson.md) and [linearised metric Carleson](linearised-metric-carleson.md) is by no means sharp. One source of non-sharpness is our choice to write for readability most constants in the form $2^{na^3}$ for some explicit constant $n$.

An a posteriori byproduct of the Lean formalization of this document is that Theorems [metric space Carleson](metric-space-carleson.md) and [linearised metric Carleson](linearised-metric-carleson.md) remain true with $2^{44a^3}$ instead of $2^{443a^3}$. This is obtained by changing the parameter $D$ introduced in [(1)](../proof-of-metric-space-carleson-overview/README.md) from $2^{100a^2}$ to $2^{7a^2}$, checking that exactly the same proof goes through, tracking the constants, and getting $2^{44a^3}$ in the end. This value is again by no means sharp. In the formalization we define the parameter $D$ as $2^{\mathbb{c}a^2}$ and the constants in this blueprint are obtained by setting $\mathbb{c} = 100$.
